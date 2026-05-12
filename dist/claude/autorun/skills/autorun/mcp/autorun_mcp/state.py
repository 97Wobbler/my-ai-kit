"""Filesystem path helpers for Autorun MCP state."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Any, Mapping


def resolve_repo_root(repo_root_arg: Any, cwd: Path | None = None, *, required: bool = False) -> Path:
    cwd = (cwd or Path.cwd()).resolve()
    if repo_root_arg is None or repo_root_arg == "":
        if required:
            raise ValueError("repo_root is required when workplan_path is not provided")
        return cwd
    if not isinstance(repo_root_arg, str):
        raise ValueError("repo_root must be a string when provided")
    path = Path(os.path.expanduser(repo_root_arg))
    if not path.is_absolute():
        path = cwd / path
    return path.resolve()


def resolve_workplan_path(arguments: Mapping[str, Any], cwd: Path | None = None) -> Path:
    cwd = (cwd or Path.cwd()).resolve()
    explicit = arguments.get("workplan_path")
    if explicit is not None:
        if not isinstance(explicit, str) or not explicit:
            raise ValueError("workplan_path must be a non-empty string when provided")
        path = Path(os.path.expanduser(explicit))
        if not path.is_absolute():
            path = cwd / path
        return path.resolve()
    return resolve_repo_root(arguments.get("repo_root"), cwd, required=True) / "workplan.yaml"


def atomic_write_text(path: Path, payload: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
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


def legacy_state_root(arguments: Mapping[str, Any], cwd: Path | None = None) -> Path:
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


def legacy_plan_state_exists(arguments: Mapping[str, Any], cwd: Path | None = None) -> bool:
    return (legacy_state_root(arguments, cwd) / "plans").exists()
