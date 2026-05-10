"""Filesystem state backend for Autorun MCP plans."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Mapping


def resolve_repo_root(repo_root_arg: Any, cwd: Path | None = None) -> Path:
    cwd = (cwd or Path.cwd()).resolve()
    if repo_root_arg is None or repo_root_arg == "":
        return cwd
    if not isinstance(repo_root_arg, str):
        raise ValueError("repo_root must be a string when provided")
    path = Path(os.path.expanduser(repo_root_arg))
    if not path.is_absolute():
        path = cwd / path
    return path.resolve()


def resolve_state_root(arguments: Mapping[str, Any], cwd: Path | None = None) -> Path:
    cwd = (cwd or Path.cwd()).resolve()
    state_dir = arguments.get("state_dir")
    if state_dir is not None:
        if not isinstance(state_dir, str):
            raise ValueError("state_dir must be a string when provided")
        path = Path(os.path.expanduser(state_dir))
        if not path.is_absolute():
            path = cwd / path
        return path.resolve()
    return resolve_repo_root(arguments.get("repo_root"), cwd) / ".autorun" / "mcp"


def plan_path(state_root: Path, plan_id: str) -> Path:
    if not plan_id or "/" in plan_id or "\\" in plan_id or plan_id in {".", ".."}:
        raise ValueError("plan_id must be a non-empty file-safe id")
    return state_root / "plans" / f"{plan_id}.json"


def load_plan(state_root: Path, plan_id: str) -> dict[str, Any]:
    path = plan_path(state_root, plan_id)
    if not path.exists():
        raise FileNotFoundError(f"plan not found: {plan_id}")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"plan file is not an object: {plan_id}")
    return data


def save_plan(state_root: Path, plan: Mapping[str, Any]) -> Path:
    plan_id = plan.get("plan_id")
    if not isinstance(plan_id, str):
        raise ValueError("plan_id is required")

    path = plan_path(state_root, plan_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

    fd, tmp_name = tempfile.mkstemp(prefix=f".{plan_id}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise
    return path


def list_plan_ids(state_root: Path) -> list[str]:
    plans_dir = state_root / "plans"
    if not plans_dir.exists():
        return []
    return sorted(path.stem for path in plans_dir.glob("*.json") if path.is_file())
