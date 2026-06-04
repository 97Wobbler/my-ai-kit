from __future__ import annotations

import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PLUGIN_ROOT / "mcp"))

import server  # noqa: E402


def test_tools_list_exposes_read_only_inspectors() -> None:
    names = {tool["name"] for tool in server.tools_list({})["tools"]}

    assert names == {"waypoint_discover", "waypoint_doctor"}


def test_tools_call_returns_structured_content(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text(
        "# Repository Instructions\n## Document Map\n## Read And Update Routing\n",
        encoding="utf-8",
    )

    result = server.tools_call(
        {
            "name": "waypoint_discover",
            "arguments": {"repo_root": str(tmp_path)},
        }
    )

    assert "structuredContent" in result
    assert result["structuredContent"]["summary"]["has_agents"] is True

