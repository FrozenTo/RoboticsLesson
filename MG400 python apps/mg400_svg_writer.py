"""Small adapter between the SVG drawer and the tested MG400 driver."""

from dataclasses import dataclass
from pathlib import Path
import sys
import time
from typing import Callable, Optional

MG400_BASE = Path(__file__).resolve().parents[2] / "mg400-base"
if str(MG400_BASE) not in sys.path:
    sys.path.insert(0, str(MG400_BASE))

from mg400.driver import DobotError, DobotMG400


@dataclass
class WriterSettings:
    ip: str = "192.168.1.6"
    dashboard_port: int = 29999
    motion_port: int = 30003
    feedback_port: int = 30004
    live_robot: bool = False
    speed_factor: int = 25


class MG400Writer:
    """Driver adapter used by the SVG planner and drawer.

    Live control must be explicitly enabled with ``settings.live_robot = True``.
    Setup only checks the existing enabled state and sets the speed factor; it
    does not clear faults or enable the robot.
    """

    def __init__(self, logger: Optional[Callable[[str], None]] = None):
        self.settings = WriterSettings()
        self._logger = logger or print
        self._robot = None

    @property
    def is_connected(self) -> bool:
        return self._robot is not None and self._robot.is_connected()

    def log(self, message: str) -> None:
        self._logger(message)

    def _require_live_connection(self):
        if not self.settings.live_robot:
            raise RuntimeError("Live robot control is disabled in WriterSettings.")
        if not self.is_connected:
            raise RuntimeError("Writer is not connected to the MG400.")
        return self._robot

    def connect_robot(self) -> None:
        if not self.settings.live_robot:
            raise RuntimeError("Set live_robot=True explicitly before connecting.")
        if self.is_connected:
            return

        robot = DobotMG400(
            self.settings.ip,
            ports=(
                self.settings.dashboard_port,
                self.settings.motion_port,
                self.settings.feedback_port,
            ),
        )
        robot.connect()
        deadline = time.monotonic() + 2.0
        while time.monotonic() < deadline:
            state = robot.get_state()
            if state["feedback_ok"]:
                self._robot = robot
                self.log(
                    f"Connected to {self.settings.ip}; mode={state['mode_name']}, "
                    f"feedback OK."
                )
                return
            time.sleep(0.02)

        robot.close()
        raise DobotError(-1, "No feedback received within 2 seconds", "connect")

    def setup_robot(self) -> None:
        robot = self._require_live_connection()
        state = robot.get_state()
        if not state["enabled"]:
            raise RuntimeError(
                f"Robot must already be enabled before writing; mode is {state['mode_name']}."
            )
        robot.speed_factor(self.settings.speed_factor)
        self.log(f"Robot ready; speed factor set to {self.settings.speed_factor}%. ")

    def get_current_pose(self):
        return self._require_live_connection().get_pose()

    def wait_for_pose(
        self,
        target_pose,
        timeout: float = 30.0,
        position_tolerance: float = 1.5,
        angle_tolerance: float = 2.0,
    ):
        robot = self._require_live_connection()
        target = [float(value) for value in target_pose]
        deadline = time.monotonic() + timeout

        while time.monotonic() < deadline:
            state = robot.get_state()
            if not state["connected"]:
                raise RuntimeError(f"Robot connection lost: {state['link_error']}")
            pose = state.get("pose")
            if pose and len(pose) >= 4:
                angle_error = (pose[3] - target[3] + 180.0) % 360.0 - 180.0
                if (
                    max(abs(pose[index] - target[index]) for index in range(3))
                    <= position_tolerance
                    and abs(angle_error) <= angle_tolerance
                ):
                    return list(pose)
            time.sleep(0.04)

        state = robot.get_state()
        raise TimeoutError(
            f"Robot did not reach {target} within {timeout:g} s; "
            f"last feedback pose was {state.get('pose')}"
        )

    def send_dashboard(self, command: str) -> str:
        robot = self._require_live_connection()
        _, response = robot._dash(command, raise_on_error=False)
        return response

    def send_motion(self, command: str) -> str:
        robot = self._require_live_connection()
        _, response = robot._move(command)
        return response

    def close_robot(self) -> None:
        robot, self._robot = self._robot, None
        if robot is not None:
            robot.close()
