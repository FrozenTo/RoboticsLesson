import argparse
import json
import re
import socket
import sys
import time
from urllib import request

import serial
from serial import SerialException


DEFAULT_ROBOT_IP = "192.168.1.6"
DEFAULT_SERIAL_PORT = "COM4"
DEFAULT_BAUD = 115200
DEFAULT_SUCK_DO = 2
DEFAULT_BLOW_DO = 1

GAUGE_RE = re.compile(r"P_gauge\s*=\s*(-?\d+(?:\.\d+)?)\s*kPa")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Turn suction on until the AtomS3 reports a target gauge pressure."
    )
    parser.add_argument("--target", type=float, default=-20.0, help="Target P_gauge in kPa.")
    parser.add_argument("--port", default=DEFAULT_SERIAL_PORT, help="AtomS3 serial port.")
    parser.add_argument("--baud", type=int, default=DEFAULT_BAUD, help="AtomS3 serial baud.")
    parser.add_argument("--ip", default=DEFAULT_ROBOT_IP, help="MG400 IP address.")
    parser.add_argument(
        "--server",
        default=None,
        help="Use a running mg400 serve API instead of connecting to the robot directly.",
    )
    parser.add_argument("--suck-do", type=int, default=DEFAULT_SUCK_DO, help="Suction DO index.")
    parser.add_argument("--blow-do", type=int, default=DEFAULT_BLOW_DO, help="Blow DO index.")
    parser.add_argument(
        "--timeout",
        type=float,
        default=20.0,
        help="Maximum seconds to wait before turning the pump off.",
    )
    parser.add_argument(
        "--monitor-after-target",
        type=float,
        default=0.0,
        help="Seconds to keep printing and maintaining pressure after the target is reached.",
    )
    parser.add_argument(
        "--hold-band",
        type=float,
        default=2.0,
        help="Restart suction when P_gauge rises this many kPa above the target.",
    )
    parser.add_argument(
        "--no-hold",
        action="store_true",
        help="Only monitor after the target; do not restart suction.",
    )
    parser.add_argument(
        "--pulse-on",
        type=float,
        default=0.0,
        help="Use slow pulsed suction: turn suction on for this many seconds per step.",
    )
    parser.add_argument(
        "--pulse-off",
        type=float,
        default=0.8,
        help="Pause this many seconds between suction pulses.",
    )
    return parser.parse_args()


def set_pump_via_server(server_url: str, mode: str) -> None:
    url = server_url.rstrip("/") + "/api/pump"
    data = json.dumps({"mode": mode}).encode("utf-8")
    http_request = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(http_request, timeout=5) as response:
        payload = json.loads(response.read().decode("utf-8"))
    print(f"pump {mode}: {payload}")
    if not payload.get("ok"):
        raise RuntimeError(f"pump {mode} failed: {payload.get('error', payload)}")


def set_pump_direct(robot, mode: str, suck_do: int, blow_do: int) -> None:
    errid, resp = robot.set_pump(mode, suck_do, blow_do)
    print(f"pump {mode}: {resp}")
    if errid != 0:
        raise RuntimeError(f"pump {mode} failed with ErrorID {errid}: {resp}")


def send_dashboard_command(ip: str, command: str) -> str:
    with socket.create_connection((ip, 29999), timeout=3) as dashboard:
        dashboard.sendall((command + "\n").encode("utf-8"))
        response = dashboard.recv(1024).decode("utf-8", errors="replace").strip()
    if not response.startswith("0,"):
        raise RuntimeError(f"{command} failed: {response}")
    return response


def set_pump_via_dashboard(ip: str, mode: str, suck_do: int, blow_do: int) -> None:
    mode = (mode or "").lower()
    if mode == "suck":
        commands = [(blow_do, 0), (suck_do, 1)]
    elif mode == "blow":
        commands = [(suck_do, 0), (blow_do, 1)]
    elif mode == "off":
        commands = [(suck_do, 0), (blow_do, 0)]
    else:
        raise RuntimeError(f"bad pump mode {mode!r}")

    responses = []
    for index, value in commands:
        command = f"DOExecute({int(index)},{int(value)})"
        responses.append(send_dashboard_command(ip, command))
    print(f"pump {mode}: {'; '.join(responses)}")


def main() -> int:
    args = parse_args()
    if args.target >= 0:
        print("For suction, use a negative target such as --target -20.", file=sys.stderr)
        return 2

    pump_started = False

    print(f"Opening AtomS3 on {args.port} at {args.baud} baud")
    if args.server:
        print(f"Using mg400 server API at {args.server}")
    else:
        print(f"Using MG400 dashboard at {args.ip}:29999")
    print(f"Target: P_gauge <= {args.target:.1f} kPa")
    restart_pressure = args.target + abs(args.hold_band)
    if args.pulse_on > 0:
        print(f"Slow pulsed suction: {args.pulse_on:.3f} s on, {args.pulse_off:.3f} s off")
    if args.monitor_after_target > 0 and not args.no_hold:
        print(f"Holding: restart suction when P_gauge > {restart_pressure:.1f} kPa")

    try:
        if args.server:
            set_pump = lambda mode: set_pump_via_server(args.server, mode)
        else:
            set_pump = lambda mode: set_pump_via_dashboard(
                args.ip, mode, args.suck_do, args.blow_do
            )

        with serial.Serial(args.port, args.baud, timeout=1, dsrdtr=False, rtscts=False) as atom:
            atom.dtr = False
            atom.rts = False
            atom.reset_input_buffer()

            if args.pulse_on <= 0:
                set_pump("suck")
                pump_started = True
            else:
                set_pump("off")

            deadline = time.monotonic() + args.timeout
            monitor_until = None
            while time.monotonic() < deadline:
                raw_line = atom.readline()
                if not raw_line:
                    continue

                line = raw_line.decode("utf-8", errors="replace").rstrip()
                match = GAUGE_RE.search(line)
                if not match:
                    print(line)
                    continue

                pressure = float(match.group(1))
                pump_state = "suck" if pump_started else "off"
                print(f"P_gauge = {pressure:6.1f} kPa   pump={pump_state}")

                if pressure <= args.target:
                    if pump_started:
                        set_pump("off")
                        pump_started = False

                    if monitor_until is None:
                        print(f"Reached {pressure:.1f} kPa, pump is off.")
                        if args.monitor_after_target <= 0:
                            return 0
                        monitor_until = time.monotonic() + args.monitor_after_target
                        deadline = monitor_until

                if monitor_until is not None and time.monotonic() >= monitor_until:
                    return 0

                should_pull_before_target = monitor_until is None and pressure > args.target
                should_hold = (
                    monitor_until is not None
                    and not args.no_hold
                    and pressure > restart_pressure
                )

                if args.pulse_on > 0 and (should_pull_before_target or should_hold):
                    set_pump("suck")
                    pump_started = True
                    print(f"pulse suck for {args.pulse_on:.3f} s")
                    time.sleep(args.pulse_on)
                    set_pump("off")
                    pump_started = False
                    time.sleep(max(0.0, args.pulse_off))
                elif args.pulse_on <= 0 and should_hold and not pump_started:
                    print(f"P_gauge rose above {restart_pressure:.1f} kPa; suction back on.")
                    set_pump("suck")
                    pump_started = True

            print(f"Timeout after {args.timeout:.1f} s; turning pump off.", file=sys.stderr)
            return 1
    except KeyboardInterrupt:
        print("\nInterrupted; turning pump off.", file=sys.stderr)
        return 130
    except (SerialException, RuntimeError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    finally:
        if pump_started:
            try:
                set_pump("off")
            except Exception as error:
                print(f"Could not turn pump off cleanly: {error}", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
