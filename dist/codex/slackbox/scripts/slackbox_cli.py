#!/usr/bin/env python3
"""Runtime wrapper for the Slackbox CLI."""

from __future__ import annotations

import sys
from pathlib import Path


def _ensure_mcp_importable() -> None:
    plugin_root = Path(__file__).resolve().parents[1]
    mcp_dir = plugin_root / "mcp"
    sys.path.insert(0, str(mcp_dir))


def main() -> None:
    _ensure_mcp_importable()

    from slack_fetch.cli import main as cli_main

    cli_main()


if __name__ == "__main__":
    main()
