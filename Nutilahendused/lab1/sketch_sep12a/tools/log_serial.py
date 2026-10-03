import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

import serial
from serial import SerialException


DEFAULT_PORT = "COM4"
DEFAULT_BAUD = 115200


def default_output_path() -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    project_dir = Path(__file__).resolve().parents[1]
    return project_dir / "logs" / f"pressure-{timestamp}.log"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Log AtomS3 pressure readings from the serial port."
    )
    parser.add_argument("--port", default=DEFAULT_PORT, help="Serial port, e.g. COM4.")
    parser.add_argument("--baud", type=int, default=DEFAULT_BAUD, help="Serial baud rate.")
    parser.add_argument(
        "--output",
        type=Path,
        default=default_output_path(),
        help="Output log file. Defaults to logs/pressure-YYYYMMDD-HHMMSS.log.",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=0,
        help="Seconds to log. Use 0 to keep logging until Ctrl+C.",
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Append to the output file instead of replacing it.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = args.output.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    mode = "a" if args.append else "w"
    started_at = time.monotonic()

    print(f"Logging {args.port} at {args.baud} baud")
    print(f"Writing to {output_path}")
    print("Press Ctrl+C to stop.")

    try:
        with serial.Serial(args.port, args.baud, timeout=1, dsrdtr=False, rtscts=False) as port:
            port.dtr = False
            port.rts = False

            with output_path.open(mode, encoding="utf-8", newline="\n") as log_file:
                if mode == "w":
                    log_file.write("# timestamp\tserial_output\n")

                while True:
                    if args.duration > 0 and time.monotonic() - started_at >= args.duration:
                        break

                    raw_line = port.readline()
                    if not raw_line:
                        continue

                    line = raw_line.decode("utf-8", errors="replace").rstrip()
                    timestamp = datetime.now().isoformat(timespec="milliseconds")
                    log_line = f"{timestamp}\t{line}"
                    print(log_line)
                    log_file.write(log_line + "\n")
                    log_file.flush()
    except KeyboardInterrupt:
        print("\nStopped.")
    except SerialException as error:
        print(f"Could not open {args.port}: {error}", file=sys.stderr)
        print(
            "Close any other serial monitor or terminal using the board, then try again.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
