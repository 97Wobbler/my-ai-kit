#!/usr/bin/env python3
"""Install Stateful into a target repository."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


MARKER_START = "<!-- stateful:start -->"
MARKER_END = "<!-- stateful:end -->"


def plugin_root() -> Path:
    return Path(__file__).resolve().parent.parent


def render(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def write_template(src: Path, dst: Path, values: dict[str, str], force: bool) -> bool:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and not force:
        return False
    dst.write_text(render(src.read_text(encoding="utf-8"), values), encoding="utf-8")
    return True


def patch_routing(path: Path, skill: str, product: str, force: bool) -> bool:
    if product == "claude":
        product_name = "Claude Code"
        entry = f"Start a fresh Claude Code session with `/{skill}`."
        instruction_file = "CLAUDE.md"
    elif product == "codex":
        product_name = "Codex"
        entry = f"Start a fresh Codex session with `${skill}` or ask Codex to use the `{skill}` skill."
        instruction_file = "AGENTS.md"
    else:
        raise ValueError(f"unknown product: {product}")

    block = f"""{MARKER_START}
## Stateful Workflow ({product_name})

This repository uses Stateful for stateful agent work.

- {entry}
- Machine state lives in `.stateful/workplan.yaml`.
- Human-readable state lives in `.stateful/docs/`.
- Latest handoff lives in `.stateful/session/handoff.md`.
- Run `python3 scripts/stateful/status.py` to inspect the next runnable tasks.
- Run `python3 scripts/stateful/validate-workplan.py` before committing workplan changes.

Required recovery order:
1. Read `{instruction_file}`.
2. Read `.stateful/config.yaml`.
3. Read `.stateful/workplan.yaml`.
4. Read `.stateful/protocols/autorun.md`.
5. Read `.stateful/session/handoff.md`.
6. Check `git log --oneline -10`.
{MARKER_END}
"""
    if path.exists():
        current = path.read_text(encoding="utf-8")
        if MARKER_START in current and MARKER_END in current:
            if not force:
                return False
            before = current.split(MARKER_START)[0].rstrip()
            after = current.split(MARKER_END, 1)[1].lstrip()
            path.write_text(before + "\n\n" + block + "\n" + after, encoding="utf-8")
            return True
        path.write_text(current.rstrip() + "\n\n" + block, encoding="utf-8")
        return True
    path.write_text(f"# Repository Instructions\n\n{block}", encoding="utf-8")
    return True


def copy_runtime_scripts(root: Path, force: bool) -> list[str]:
    scripts = {
        "stateful_validate.py": "validate-workplan.py",
        "stateful_sync.py": "sync-state.py",
        "stateful_status.py": "status.py",
        "stateful_close.py": "close-session.py",
        "stateful_task.py": "task.py",
        "stateful_plan.py": "plan.py",
        "stateful_archive.py": "archive.py",
    }
    copied: list[str] = []
    target_dir = root / "scripts" / "stateful"
    target_dir.mkdir(parents=True, exist_ok=True)
    for src_name, dst_name in scripts.items():
        src = plugin_root() / "scripts" / src_name
        dst = target_dir / dst_name
        if dst.exists() and not force:
            continue
        shutil.copy2(src, dst)
        dst.chmod(0o755)
        copied.append(str(dst.relative_to(root)))
    return copied


def git_root(path: Path) -> Path:
    result = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=path, capture_output=True, text=True)
    if result.returncode == 0:
        return Path(result.stdout.strip()).resolve()
    return path.resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="target repository root")
    parser.add_argument("--skill", default="repo", help="repo-local slash skill name")
    parser.add_argument("--force", action="store_true", help="overwrite existing Stateful scaffold files")
    parser.add_argument("--no-agents", action="store_true", help="do not patch AGENTS.md")
    args = parser.parse_args()

    root = git_root(Path(args.root))
    skill = args.skill.strip().strip("/") or "repo"
    templates = plugin_root() / "templates"
    values = {
        "SKILL_NAME": skill,
        "REPO_NAME": root.name,
    }

    created: list[str] = []
    template_map = {
        "stateful/config.yaml": ".stateful/config.yaml",
        "stateful/workplan.yaml": ".stateful/workplan.yaml",
        "stateful/docs/status.md": ".stateful/docs/status.md",
        "stateful/docs/decisions.md": ".stateful/docs/decisions.md",
        "stateful/docs/risks.md": ".stateful/docs/risks.md",
        "stateful/docs/roadmap.md": ".stateful/docs/roadmap.md",
        "stateful/docs/todo.md": ".stateful/docs/todo.md",
        "stateful/session/handoff.md": ".stateful/session/handoff.md",
        "stateful/protocols/autorun.md": ".stateful/protocols/autorun.md",
        "stateful/protocols/gates.md": ".stateful/protocols/gates.md",
        "stateful/protocols/recovery.md": ".stateful/protocols/recovery.md",
        "repo-skills/claude/SKILL.md": f".claude/skills/{skill}/SKILL.md",
        "repo-skills/codex/SKILL.md": f".agents/skills/{skill}/SKILL.md",
    }

    for src_rel, dst_rel in template_map.items():
        if write_template(templates / src_rel, root / dst_rel, values, args.force):
            created.append(dst_rel)

    if patch_routing(root / "CLAUDE.md", skill, "claude", args.force):
        created.append("CLAUDE.md")
    if not args.no_agents:
        if patch_routing(root / "AGENTS.md", skill, "codex", args.force):
            created.append("AGENTS.md")

    created.extend(copy_runtime_scripts(root, args.force))

    subprocess.run([sys.executable, "scripts/stateful/validate-workplan.py"], cwd=root)
    subprocess.run([sys.executable, "scripts/stateful/sync-state.py"], cwd=root)

    print(f"Stateful installed in {root}")
    if created:
        print("created/updated:")
        for item in created:
            print(f"  - {item}")
    else:
        print("no files changed; use --force to refresh scaffold files")
    print(f"next: Claude Code `/{skill}`; Codex `${skill}` or use the `{skill}` skill")
    return 0


if __name__ == "__main__":
    sys.exit(main())
