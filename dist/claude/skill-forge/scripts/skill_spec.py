#!/usr/bin/env python3
"""Shared parsing helpers for Skill Forge specs."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ALLOWED_TARGETS = {"claude", "codex"}
ALLOWED_CAPABILITIES = {
    "user_questions",
    "file_edits",
    "subagents",
    "plan_mode",
    "network",
    "validation",
}
CHOICE_VALUES = {
    "user_questions": {"none", "optional", "required"},
    "subagents": {"none", "optional", "required"},
    "plan_mode": {"none", "optional", "required"},
    "validation": {"none", "optional", "required"},
}
BOOL_VALUES = {"file_edits", "network"}
DEFAULT_CAPABILITIES: dict[str, Any] = {
    "user_questions": "none",
    "file_edits": False,
    "subagents": "none",
    "plan_mode": "none",
    "network": False,
    "validation": "none",
}


@dataclass(frozen=True)
class SkillSpec:
    path: Path
    frontmatter: dict[str, Any]
    body: str

    @property
    def name(self) -> str:
        return str(self.frontmatter["name"])

    @property
    def description(self) -> str:
        return str(self.frontmatter["description"])

    @property
    def targets(self) -> list[str]:
        return list(self.frontmatter["targets"])

    @property
    def capabilities(self) -> dict[str, Any]:
        merged = dict(DEFAULT_CAPABILITIES)
        merged.update(self.frontmatter.get("capabilities", {}) or {})
        return merged

    @property
    def runtime_overrides(self) -> dict[str, str]:
        value = self.frontmatter.get("runtime_overrides", {}) or {}
        return {str(key): str(item) for key, item in value.items()}

    @property
    def outputs(self) -> dict[str, str]:
        value = self.frontmatter.get("outputs", {}) or {}
        return {str(key): str(item) for key, item in value.items()}


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value in {"null", "None"}:
        return None
    if value.startswith(("'", '"')) and value.endswith(("'", '"')):
        return ast.literal_eval(value)
    return value


def line_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def collect_block_scalar(lines: list[str], start: int, parent_indent: int) -> tuple[str, int]:
    content: list[str] = []
    index = start
    strip_indent = parent_indent + 2

    while index < len(lines):
        raw_line = lines[index].rstrip()
        if raw_line.strip():
            indent = line_indent(raw_line)
            if indent <= parent_indent:
                break
            content.append(raw_line[strip_indent:] if len(raw_line) >= strip_indent else raw_line.lstrip())
        else:
            content.append("")
        index += 1

    return "\n".join(content).rstrip(), index


def parse_frontmatter(text: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    current_key: str | None = None
    lines = text.splitlines()
    index = 0

    while index < len(lines):
        raw_line = lines[index]
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue

        if not line.startswith(" "):
            key, sep, value = line.partition(":")
            if not sep:
                raise ValueError(f"Invalid frontmatter line: {raw_line}")
            key = key.strip()
            value = value.strip()
            current_key = key
            if value == "":
                result[key] = []
            elif value in {"|", ">"}:
                result[key], index = collect_block_scalar(lines, index + 1, parent_indent=0)
                continue
            elif value.startswith("[") and value.endswith("]"):
                result[key] = ast.literal_eval(value)
            else:
                result[key] = parse_scalar(value)
            index += 1
            continue

        if current_key is None:
            raise ValueError(f"Nested value without a parent key: {raw_line}")

        stripped = line.strip()
        if stripped.startswith("- "):
            if not isinstance(result[current_key], list):
                raise ValueError(f"{current_key} mixes list and mapping values")
            result[current_key].append(parse_scalar(stripped[2:]))
            index += 1
            continue

        key, sep, value = stripped.partition(":")
        if not sep:
            raise ValueError(f"Invalid nested frontmatter line: {raw_line}")
        if not isinstance(result[current_key], dict):
            if result[current_key] == []:
                result[current_key] = {}
            else:
                raise ValueError(f"{current_key} mixes scalar and mapping values")
        if value.strip() in {"|", ">"}:
            result[current_key][key.strip()], index = collect_block_scalar(
                lines,
                index + 1,
                parent_indent=line_indent(line),
            )
            continue
        result[current_key][key.strip()] = parse_scalar(value.strip())
        index += 1

    return result


def load_spec(path: Path) -> SkillSpec:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("Spec must start with YAML frontmatter delimited by ---")
    try:
        frontmatter_text, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("Spec must include closing --- frontmatter delimiter") from exc
    frontmatter = parse_frontmatter(frontmatter_text)
    return SkillSpec(path=path, frontmatter=frontmatter, body=body.strip() + "\n")


def validate_spec(spec: SkillSpec) -> list[str]:
    errors: list[str] = []
    for key in ("name", "description", "targets"):
        if key not in spec.frontmatter:
            errors.append(f"missing required frontmatter: {key}")

    name = spec.frontmatter.get("name")
    if name is not None and (not isinstance(name, str) or not name.strip()):
        errors.append("name must be a non-empty string")

    description = spec.frontmatter.get("description")
    if description is not None and (not isinstance(description, str) or not description.strip()):
        errors.append("description must be a non-empty string")

    targets = spec.frontmatter.get("targets")
    if not isinstance(targets, list) or not targets:
        errors.append("targets must be a non-empty list")
    elif unknown := sorted(set(str(target) for target in targets) - ALLOWED_TARGETS):
        errors.append(f"unknown targets: {', '.join(unknown)}")

    raw_capabilities = spec.frontmatter.get("capabilities", {}) or {}
    if not isinstance(raw_capabilities, dict):
        errors.append("capabilities must be a mapping")
        raw_capabilities = {}
    elif unknown := sorted(set(raw_capabilities) - ALLOWED_CAPABILITIES):
        errors.append(f"unknown capabilities: {', '.join(unknown)}")

    capabilities = spec.capabilities
    for key, allowed in CHOICE_VALUES.items():
        if capabilities.get(key) not in allowed:
            errors.append(f"capabilities.{key} must be one of: {', '.join(sorted(allowed))}")
    for key in BOOL_VALUES:
        if not isinstance(capabilities.get(key), bool):
            errors.append(f"capabilities.{key} must be true or false")

    for map_key in ("runtime_overrides", "outputs"):
        value = spec.frontmatter.get(map_key, {}) or {}
        if not isinstance(value, dict):
            errors.append(f"{map_key} must be a mapping")
        elif unknown := sorted(set(str(item) for item in value) - ALLOWED_TARGETS):
            errors.append(f"{map_key} has unknown targets: {', '.join(unknown)}")

    if not spec.body.strip():
        errors.append("body must describe the neutral workflow")

    body_lower = spec.body.lower()
    runtime_terms = (
        "askuserquestion",
        "askuserquestions",
        "request_user_input",
        "taskcreate",
        "taskupdate",
        "update_plan",
    )
    leaked_terms = [term for term in runtime_terms if term in body_lower]
    if leaked_terms:
        errors.append("neutral body contains runtime-specific tool names: " + ", ".join(leaked_terms))

    if "codex" in (targets or []) and capabilities.get("user_questions") == "required":
        override = spec.runtime_overrides.get("codex", "").lower()
        if "plan" not in override and "default" not in override:
            errors.append("codex required user_questions needs a runtime_overrides.codex Plan/Default mode note")

    return errors


def title_from_name(name: str) -> str:
    return " ".join(part.capitalize() for part in name.replace("_", "-").split("-") if part)
