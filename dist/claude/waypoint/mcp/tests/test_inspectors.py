from __future__ import annotations

import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PLUGIN_ROOT / "mcp"))

from waypoint_mcp.inspectors import audit_repo, discover_repo, doctor_repo  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def create_minimal_waypoint_repo(root: Path) -> None:
    write(
        root / "AGENTS.md",
        "\n".join(
            [
                "# Repository Instructions",
                "## Document Map",
                "## Read And Update Routing",
                "<!-- waypoint:start -->",
                "## Waypoint",
                "<!-- waypoint:end -->",
            ]
        ),
    )
    write(root / ".waypoint/config.yaml", "documents:\n  agents: AGENTS.md\n  plan: docs/plan.md\n")
    write(root / "docs/plan.md", "# Plan\n")
    write(root / ".gitignore", ".waypoint/cache/\n")


def test_discover_classifies_routers_and_config(tmp_path: Path) -> None:
    create_minimal_waypoint_repo(tmp_path)

    result = discover_repo(tmp_path)

    assert result["summary"]["has_agents"] is True
    assert result["summary"]["has_waypoint_config"] is True
    assert result["routers"][0]["path"] == "AGENTS.md"


def test_doctor_passes_minimal_configured_repo(tmp_path: Path) -> None:
    create_minimal_waypoint_repo(tmp_path)

    result = doctor_repo(tmp_path)

    assert result["status"] == "pass"
    assert result["counts"]["fail"] == 0


def test_doctor_fails_duplicate_marker_blocks(tmp_path: Path) -> None:
    create_minimal_waypoint_repo(tmp_path)
    write(
        tmp_path / "AGENTS.md",
        "\n".join(
            [
                "# Repository Instructions",
                "## Document Map",
                "## Read And Update Routing",
                "<!-- waypoint:start -->",
                "one",
                "<!-- waypoint:end -->",
                "<!-- waypoint:start -->",
                "two",
                "<!-- waypoint:end -->",
            ]
        ),
    )

    result = doctor_repo(tmp_path)

    assert result["status"] == "fail"
    assert any(item["code"] == "waypoint-marker-duplicate" for item in result["findings"])


def test_doctor_reports_broken_local_markdown_links(tmp_path: Path) -> None:
    create_minimal_waypoint_repo(tmp_path)
    write(tmp_path / "docs/plan.md", "# Plan\n\n[Missing](missing.md)\n")

    result = doctor_repo(tmp_path)

    assert result["status"] == "warn"
    assert any(item["code"] == "broken-markdown-link" for item in result["findings"])


def test_audit_reports_document_bloat_candidate(tmp_path: Path) -> None:
    create_minimal_waypoint_repo(tmp_path)
    write(tmp_path / "docs/plan.md", "# Plan\n" + "\n".join(f"- item {i}" for i in range(500)))

    result = audit_repo(tmp_path)

    assert result["status"] == "findings"
    assert any(item["code"] == "document-bloat-candidate" for item in result["findings"])


def test_discover_classifies_tracks_document(tmp_path: Path) -> None:
    create_minimal_waypoint_repo(tmp_path)
    write(tmp_path / "docs/tracks.md", "# Tracks\n")

    result = discover_repo(tmp_path)

    tracks = [item for item in result["documents"] if item["path"] == "docs/tracks.md"]
    assert tracks == [{"path": "docs/tracks.md", "role": "tracks", "confidence": "high"}]


def test_doctor_checks_configured_tracks_home(tmp_path: Path) -> None:
    create_minimal_waypoint_repo(tmp_path)
    write(
        tmp_path / ".waypoint/config.yaml",
        "documents:\n  agents: AGENTS.md\n  plan: docs/plan.md\n  tracks: docs/tracks.md\n",
    )

    result = doctor_repo(tmp_path)

    assert result["status"] == "warn"
    assert any(
        item["code"] == "document-home-missing" and item["path"] == "docs/tracks.md"
        for item in result["findings"]
    )


def test_audit_reports_decision_consolidation_candidate(tmp_path: Path) -> None:
    create_minimal_waypoint_repo(tmp_path)
    write(
        tmp_path / "docs/decisions.md",
        "| Date | Decision | Rationale |\n"
        "|---|---|---|\n"
        "| 2026-01-01 | Adopt X. | Initial choice. |\n"
        "| 2026-01-02 | Reverted X. | X is no longer active. |\n",
    )

    result = audit_repo(tmp_path)

    assert any(item["code"] == "decision-consolidation-candidate" for item in result["findings"])
