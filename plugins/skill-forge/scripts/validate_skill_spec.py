#!/usr/bin/env python3
"""Validate a Skill Forge runtime-neutral spec."""

from __future__ import annotations

import argparse
from pathlib import Path

from skill_spec import load_spec, validate_spec


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    args = parser.parse_args()

    try:
        spec = load_spec(args.spec)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    errors = validate_spec(spec)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {args.spec}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
