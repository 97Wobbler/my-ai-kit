#!/usr/bin/env python3
"""Validate a card-review input JSON file without starting the GUI."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from review_schema import load_and_validate_input


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        load_and_validate_input(args.input)
    except ValueError as exc:
        print(f"card-review: {exc}", file=sys.stderr)
        return 2
    print(f"Valid card-review input: {args.input}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
