#!/usr/bin/env python3
"""Compile a Skill Forge spec into runtime SKILL.md scaffold outputs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from skill_spec import load_spec, title_from_name, validate_spec


ROOT = Path(__file__).resolve().parents[3]
PLUGIN_ROOT = Path(__file__).resolve().parents[1]


def template_for(target: str) -> str:
    path = PLUGIN_ROOT / "templates" / target / "SKILL.md.tmpl"
    return path.read_text(encoding="utf-8")


def bullet(text: str) -> str:
    return f"- {text}"


def runtime_notes(target: str, capabilities: dict[str, object]) -> str:
    notes: list[str] = []

    if capabilities["user_questions"] == "required":
        if target == "claude":
            notes.append("Use Claude Code's native blocking question flow when clarification is required.")
        else:
            notes.append("Use `request_user_input` only in Plan Mode. In Default mode, ask a concise direct question and wait.")
    elif capabilities["user_questions"] == "optional":
        if target == "claude":
            notes.append("Ask clarification questions only when they materially change the result.")
        else:
            notes.append("Ask clarification questions sparingly; `request_user_input` is Plan Mode only.")

    if capabilities["file_edits"]:
        if target == "codex":
            notes.append("For manual file edits, use `apply_patch` and preserve unrelated user changes.")
        else:
            notes.append("Follow repository edit instructions and preserve unrelated user changes.")

    if capabilities["subagents"] in {"optional", "required"}:
        notes.append("Delegate only when the runtime supports subagents and the task can run safely in parallel.")

    if capabilities["plan_mode"] == "required" and target == "codex":
        notes.append("This skill is Plan Mode oriented; do not mutate repo-tracked files while planning.")

    if capabilities["network"]:
        notes.append("Use network access only when current or external facts are required.")

    if capabilities["validation"] in {"optional", "required"}:
        notes.append("Run the relevant validation checks before reporting completion.")

    if not notes:
        notes.append("No special runtime capabilities are required.")

    return "\n".join(bullet(note) for note in notes)


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def compile_spec(spec_path: Path, target: str) -> str:
    spec = load_spec(spec_path)
    errors = validate_spec(spec)
    if errors:
        formatted = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"Spec validation failed:\n{formatted}")
    if target not in spec.targets:
        raise ValueError(f"Spec does not declare target: {target}")

    override = spec.runtime_overrides.get(target, "No target-specific override.")
    return template_for(target).format(
        name=yaml_string(spec.name),
        description=yaml_string(spec.description),
        title=title_from_name(spec.name),
        source_path=rel(spec_path),
        runtime_notes=runtime_notes(target, spec.capabilities),
        body=spec.body.strip(),
        runtime_overrides=override,
    ).rstrip() + "\n"


def output_path_for(spec_path: Path, target: str, out: Path | None) -> Path:
    if out is not None:
        return out

    spec = load_spec(spec_path)
    output = spec.outputs.get(target)
    if not output:
        raise ValueError(
            f"No output path for target {target}; pass --out or set outputs.{target} in the spec"
        )
    path = Path(output)
    return path if path.is_absolute() else ROOT / path


def target_list(spec_path: Path, target: str) -> list[str]:
    spec = load_spec(spec_path)
    if target == "all":
        return spec.targets
    return [target]


def write_or_check(spec_path: Path, target: str, out: Path | None, check: bool) -> int:
    failures = 0
    for item in target_list(spec_path, target):
        try:
            destination = output_path_for(spec_path, item, out)
            output = compile_spec(spec_path, item)
        except Exception as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1

        if check:
            if not destination.exists():
                print(f"MISSING: {rel(destination)}", file=sys.stderr)
                failures += 1
                continue
            current = destination.read_text(encoding="utf-8")
            if current != output:
                print(f"OUTDATED: {rel(destination)}", file=sys.stderr)
                failures += 1
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(output, encoding="utf-8")
        print(f"wrote {rel(destination)}")

    if check and failures == 0:
        print("OK: compiled skill outputs are in sync")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("--target", choices=("claude", "codex", "all"), required=True)
    parser.add_argument("--out", type=Path, help="output path for a single target")
    parser.add_argument("--check", action="store_true", help="verify generated output without writing")
    args = parser.parse_args()

    if args.target == "all" and args.out is not None:
        print("ERROR: --out cannot be used with --target all", file=sys.stderr)
        return 1
    return write_or_check(args.spec, args.target, args.out, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
