"""Capture Lab 2 100 Hz AtomS3R DATA records into a CSV file.

Use with the SEPARATE firmware in src/atom_pressure_100hz.
The firmware device timestamp t_ms is retained; host receive time is diagnostic.
No pump control. No guessed 'raw' / 'opamp' configuration or missing samples.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
import sys
import time

HEADER = [
    "trial_id", "phase", "t_ms", "seq", "config", "adc",
    "voltage_mv", "p_abs_kpa", "p_gauge_kpa", "cal_ok",
    "host_received_utc", "pump_state",
]


def parse_data(line: str):
    items = line.split(",")
    if len(items) != 9 or items[0] != "DATA":
        return None
    try:
        t_ms, seq = int(items[1]), int(items[2])
        config = items[3]
        adc, voltage_mv = int(items[4]), int(items[5])
        abs_kpa = float(items[6])
        gauge = float(items[7])
        cal_ok = int(items[8])
    except ValueError:
        return None
    if config not in {"raw", "opamp"} or cal_ok not in {0, 1}:
        return None
    if t_ms < 0 or seq < 0 or not 0 <= adc <= 4095 or voltage_mv < 0:
        return None
    return (t_ms, seq, config, adc, voltage_mv, abs_kpa, gauge, cal_ok)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", default="COM4")
    parser.add_argument("--baud", type=int, default=230400)
    parser.add_argument("--trial-id", required=True, help="Physical trial ID (e.g. raw_01)")
    parser.add_argument("--phase", default="unknown",
                        choices=["unknown", "baseline", "plateau", "transient"])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--duration", type=float, default=30.0)
    parser.add_argument("--expect-config", choices=["raw", "opamp", "dual"],
                        required=True, help="Expected REAL electrical configuration")
    args = parser.parse_args()
    if args.output.exists():
        print(f"Refusing to replace existing data: {args.output}", file=sys.stderr)
        return 2
    try:
        import serial
    except ImportError:
        print("Install pyserial: python -m pip install pyserial", file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    seen = set()
    last_t = {}
    last_seq = {}
    rows = 0
    misses = 0
    invalid = 0
    start = time.monotonic()
    print("WARNING: Ensure 0..3.3 V on ADC pin; pump OFF during calibration.")
    print("WARNING: Phase and trial-id are user-entered, not sensor measurements.")

    try:
        with serial.Serial(args.port, args.baud, timeout=0.2, dsrdtr=False, rtscts=False) as port:
            port.dtr = False
            port.rts = False
            with args.output.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.DictWriter(fh, fieldnames=HEADER)
                writer.writeheader()
                while args.duration <= 0 or time.monotonic() - start < args.duration:
                    line = port.readline().decode("utf-8", errors="replace").strip()
                    sample = parse_data(line)
                    if sample is None:
                        if line.startswith("WARN,") or line.startswith("ERR,"):
                            print(line, file=sys.stderr)
                        if line.startswith("DATA,"):
                            invalid += 1
                        continue
                    t_ms, seq, config, adc, mv, abs_kpa, gauge, cal_ok = sample
                    if args.expect_config != "dual" and config != args.expect_config:
                        print(f"WRONG CONFIG {config}, expected {args.expect_config}; capture aborted",
                              file=sys.stderr)
                        return 3
                    if args.expect_config == "dual" and config not in {"raw", "opamp"}:
                        return 3
                    key = (seq, config)
                    if key in seen:
                        continue
                    seen.add(key)
                    prev = last_seq.get(config)
                    if prev is not None and seq > prev + 1:
                        misses += seq - prev - 1
                    last_seq[config] = seq
                    previous_time = last_t.get(config)
                    if previous_time is not None and (t_ms - previous_time) % (2 ** 32) not in range(1, 1001):
                        print(f"Unexpected timestamp interval on {config}: {t_ms - previous_time} ms",
                              file=sys.stderr)
                    last_t[config] = t_ms
                    writer.writerow({
                        "trial_id": args.trial_id,
                        "phase": args.phase,
                        "t_ms": t_ms,
                        "seq": seq,
                        "config": config,
                        "adc": adc,
                        "voltage_mv": mv,
                        "p_abs_kpa": abs_kpa if cal_ok else "",
                        "p_gauge_kpa": gauge if cal_ok else "",
                        "cal_ok": cal_ok,
                        "host_received_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                        "pump_state": "",  # not supplied by firmware
                    })
                    rows += 1
                    if rows % 100 == 0:
                        fh.flush()
    except KeyboardInterrupt:
        pass
    except (OSError, serial.SerialException) as exc:
        print(f"Capture error: {exc}", file=sys.stderr)
        return 1
    print(f"Saved {rows} actual firmware records; sequence gaps={misses}; malformed={invalid}.")
    if not rows:
        print("No DATA lines received. Check firmware and selected COM port.", file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
