"""Record the EXISTING AtomS3R text monitor as CSV without controlling the pump.

This is a host-side archival logger; it does NOT turn the original ~1.35 Hz
firmware into a 100 Hz sampler. The host receipt time is not the ADC sample time.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
import re
import sys
import time

PATTERN = re.compile(
    r"^ADC=(?P<adc>\d+)\s+Voltage=(?P<voltage>\d+)\s+mV\s+"
    r"P_abs=(?P<absolute>-?\d+(?:\.\d+)?)\s+kPa\s+"
    r"P_gauge=(?P<gauge>-?\d+(?:\.\d+)?)\s+kPa\s+"
    r"Air=(?P<air>[A-Z]+)\s*$"
)
FIELDS = [
    "received_utc", "host_elapsed_ms", "sample_index",
    "config", "trial_id", "phase", "adc", "voltage_mv",
    "reported_p_abs_kpa", "reported_p_gauge_kpa", "air_status",
    "pump_state",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", default="COM4")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--config", required=True, choices=["raw", "opamp"],
                        help="MUST match the actual electrical wiring.")
    parser.add_argument("--trial-id", required=True,
                        help="Identifier of the physical trial, not automatically inferred.")
    parser.add_argument("--phase", default="unknown",
                        choices=["unknown", "baseline", "plateau", "transient"])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--duration", type=float, default=0,
                        help="Seconds; 0 = until Ctrl+C.")
    args = parser.parse_args()

    try:
        import serial
    except ImportError:
        print("Missing dependency: python -m pip install pyserial", file=sys.stderr)
        return 2

    if args.output.exists():
        print(f"Output file already exists (will not overwrite): {args.output}", file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    started = time.monotonic()
    try:
        with serial.Serial(args.port, args.baud, timeout=0.3,
                           dsrdtr=False, rtscts=False) as port:
            port.dtr = False
            port.rts = False
            with args.output.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS)
                writer.writeheader()
                while True:
                    if args.duration and time.monotonic() - started >= args.duration:
                        break
                    line = port.readline().decode("utf-8", errors="replace").strip()
                    matched = PATTERN.fullmatch(line)
                    if matched is None:
                        continue
                    writer.writerow({
                        "received_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                        "host_elapsed_ms": round((time.monotonic() - started) * 1000, 3),
                        "sample_index": count,
                        "config": args.config,
                        "trial_id": args.trial_id,
                        "phase": args.phase,
                        "adc": matched.group("adc"),
                        "voltage_mv": matched.group("voltage"),
                        "reported_p_abs_kpa": matched.group("absolute"),
                        "reported_p_gauge_kpa": matched.group("gauge"),
                        "air_status": matched.group("air"),
                        "pump_state": "",  # Cannot be obtained from the old firmware.
                    })
                    handle.flush()
                    count += 1
    except KeyboardInterrupt:
        pass
    except (OSError, serial.SerialException) as error:
        print(f"Serial capture failed: {error}", file=sys.stderr)
        return 1
    print(f"Wrote {count} readings to {args.output}")
    print("Host timestamps are approximate receipt times, NOT 100 Hz ADC timestamps.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
