#!/usr/bin/env python3
"""CLI fallback for the Waypoint documentation audit inspector."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLUGIN_ROOT / "mcp"))

from waypoint_mcp.inspectors import audit_repo  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root to inspect.")
    parser.add_argument(
        "--max-files",
        type=int,
        default=500,
        help="Maximum candidate docs to inspect.",
    )
    args = parser.parse_args()

    result = audit_repo(args.repo_root, max_files=args.max_files)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
