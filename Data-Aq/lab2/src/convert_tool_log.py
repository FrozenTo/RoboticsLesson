"""Export the original 2026-10-25 text monitor log to a faithful CSV.

Only fields explicitly present in the source are copied. No timestamps,
pump states or raw/opamp configuration are inferred.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re

LAB_DIR = Path(__file__).resolve().parents[1]
SOURCE_DEFAULT = LAB_DIR / "logs" / "Tool_logs25102026.md"
OUTPUT_DEFAULT = LAB_DIR / "data" / "pressure_20261025_legacy.csv"
PATTERN = re.compile(
    r"^ADC=(?P<adc>\d+)\s+Voltage=(?P<voltage>\d+)\s+mV\s+"
    r"P_abs=(?P<absolute>-?\d+(?:\.\d+)?)\s+kPa\s+"
    r"P_gauge=(?P<gauge>-?\d+(?:\.\d+)?)\s+kPa\s+"
    r"Air=(?P<air>[A-Z]+)\s*$"
)
COLUMNS = [
    "sample_index",
    "source_line",
    "adc",
    "voltage_mv",
    "reported_p_abs_kpa",
    "reported_p_gauge_kpa",
    "air_status",
    "config",
    "t_ms",
    "pump_state",
]


def convert(source: Path, output: Path) -> int:
    rows = []
    for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        match = PATTERN.fullmatch(line)
        if match is None:
            continue
        rows.append({
            "sample_index": len(rows),
            "source_line": line_number,
            "adc": match.group("adc"),
            "voltage_mv": match.group("voltage"),
            "reported_p_abs_kpa": match.group("absolute"),
            "reported_p_gauge_kpa": match.group("gauge"),
            "air_status": match.group("air"),
            "config": "unverified",
            "t_ms": "",
            "pump_state": "",
        })
    if not rows:
        raise ValueError(f"No pressure readings found in {source}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE_DEFAULT)
    parser.add_argument("--output", type=Path, default=OUTPUT_DEFAULT)
    args = parser.parse_args()
    count = convert(args.source, args.output)
    print(f"Recovered {count} source readings into {args.output}")
    print("config=unverified; t_ms and pump_state are blank (not recorded).")


if __name__ == "__main__":
    main()
