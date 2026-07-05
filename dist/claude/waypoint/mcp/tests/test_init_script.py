from __future__ import annotations

import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))
sys.path.insert(0, str(PLUGIN_ROOT / "mcp"))

from waypoint_init import run_auto, run_brownfield_audit, run_greenfield  # noqa: E402


def test_greenfield_generation_is_idempotent(tmp_path: Path) -> None:
    first = run_greenfield(tmp_path, with_claude=True)
    second = run_greenfield(tmp_path, with_claude=True)

    assert first["success"] is True
    assert second["success"] is True
    assert (tmp_path / "AGENTS.md").is_file()
    assert (tmp_path / "CLAUDE.md").read_text(encoding="utf-8").count("AGENTS.md") >= 1
    assert (tmp_path / ".waypoint" / "config.yaml").is_file()
    assert not (tmp_path / "docs" / "tracks.md").exists()
    assert ".waypoint/cache/" in (tmp_path / ".gitignore").read_text(encoding="utf-8")
    assert "AGENTS.md" in second["unchanged"]


def test_greenfield_reports_conflict_without_overwrite(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text("custom instructions\n", encoding="utf-8")

    result = run_greenfield(tmp_path)

    assert result["success"] is False
    assert "AGENTS.md" in result["conflicts"]
    assert (tmp_path / "AGENTS.md").read_text(encoding="utf-8") == "custom instructions\n"


def test_brownfield_audit_does_not_write(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Existing\n", encoding="utf-8")

    result = run_brownfield_audit(tmp_path)

    assert result["success"] is True
    assert result["writes"] == []
    assert not (tmp_path / "AGENTS.md").exists()
    assert result["doctor"]["status"] == "fail"


def test_auto_greenfield_creates_when_docs_are_weak(tmp_path: Path) -> None:
    result = run_auto(tmp_path, with_claude=False)

    assert result["mode"] == "greenfield"
    assert result["preflight"]["recommended_mode"] == "greenfield-create"
    assert (tmp_path / "AGENTS.md").is_file()
    assert (tmp_path / ".waypoint" / "config.yaml").is_file()


def test_auto_brownfield_adopt_preserves_coherent_docs(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text(
        "# Repository Instructions\n\n## Document Map\n\n- Plan: `docs/plan.md`\n",
        encoding="utf-8",
    )
    (tmp_path / "docs" / "plan.md").parent.mkdir(parents=True)
    (tmp_path / "docs" / "plan.md").write_text("# Plan\n", encoding="utf-8")

    result = run_auto(tmp_path)

    assert result["mode"] == "brownfield-adopt"
    assert result["writes"] == []
    assert not (tmp_path / ".waypoint" / "config.yaml").exists()


def test_auto_repair_when_waypoint_config_is_broken(tmp_path: Path) -> None:
    (tmp_path / ".waypoint").mkdir()
    (tmp_path / ".waypoint" / "config.yaml").write_text(
        "documents:\n  agents: AGENTS.md\n  plan: docs/plan.md\n",
        encoding="utf-8",
    )

    result = run_auto(tmp_path)

    assert result["mode"] == "repair"
    assert result["writes"] == []
    assert not (tmp_path / "AGENTS.md").exists()


def test_auto_noop_when_waypoint_is_healthy(tmp_path: Path) -> None:
    first = run_greenfield(tmp_path)

    result = run_auto(tmp_path)

    assert first["success"] is True
    assert result["mode"] == "no-op"
    assert result["writes"] == []
