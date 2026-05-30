"""Slackbox MCP plugin entrypoint."""

from __future__ import annotations

import sys
from pathlib import Path


def _ensure_local_import_path() -> None:
    mcp_dir = Path(__file__).resolve().parent
    mcp_path = str(mcp_dir)
    if mcp_path not in sys.path:
        sys.path.insert(0, mcp_path)


def main() -> None:
    _ensure_local_import_path()
    from slack_fetch.mcp_server import main as run_mcp_server

    run_mcp_server()


if __name__ == "__main__":
    main()
