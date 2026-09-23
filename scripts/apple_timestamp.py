#!/usr/bin/env python3
"""Convert explicitly specified Apple/Cocoa epoch timestamps.

No unit is guessed. The caller must state seconds, milliseconds,
microseconds, or nanoseconds.
"""

from __future__ import annotations
import argparse
from datetime import datetime, timedelta, timezone
from decimal import Decimal

APPLE_EPOCH = datetime(2001, 1, 1, tzinfo=timezone.utc)
DIVISORS = {
    "seconds": Decimal(1),
    "milliseconds": Decimal(1_000),
    "microseconds": Decimal(1_000_000),
    "nanoseconds": Decimal(1_000_000_000),
}

def convert(value: str, unit: str) -> datetime:
    seconds = Decimal(value) / DIVISORS[unit]
    whole = int(seconds)
    micros = int((seconds - whole) * Decimal(1_000_000))
    return APPLE_EPOCH + timedelta(seconds=whole, microseconds=micros)

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Apple epoch values to UTC.")
    parser.add_argument("value", help="Numeric timestamp value")
    parser.add_argument("--unit", required=True, choices=DIVISORS.keys())
    args = parser.parse_args()
    print(convert(args.value, args.unit).isoformat())

if __name__ == "__main__":
    main()
