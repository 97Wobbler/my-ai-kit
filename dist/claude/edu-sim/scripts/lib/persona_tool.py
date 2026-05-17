#!/usr/bin/env python3
"""Utilities for the Edu Sim runtime scripts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from string import Template
from typing import Any


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "PyYAML is required to read personas.yaml. Install it with: python3 -m pip install PyYAML"
        ) from exc

    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict) or not isinstance(data.get("personas"), list):
        raise SystemExit(f"{path} must contain a top-level personas list")
    return data


def personas(path: Path) -> list[dict[str, Any]]:
    items = load_yaml(path)["personas"]
    result: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise SystemExit(f"{path} contains an invalid persona entry")
        result.append(item)
    return result


def persona_by_id(path: Path, persona_id: str) -> dict[str, Any]:
    for item in personas(path):
        if item["id"] == persona_id:
            return item
    raise SystemExit(f"persona not found: {persona_id}")


def compact_response(path: Path) -> dict[str, Any]:
    persona_id = path.stem
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"id": persona_id, "error": True, "response": f"invalid JSON: {exc}"}

    if isinstance(data, dict) and data.get("error") is True:
        return {
            "id": data.get("persona_id", persona_id),
            "error": True,
            "response": data.get("reason", "unknown error"),
        }
    if isinstance(data, dict):
        for key in ("result", "response", "content", "message"):
            value = data.get(key)
            if isinstance(value, str):
                return {"id": persona_id, "response": value}
        return {"id": persona_id, "response": json.dumps(data, ensure_ascii=False)}
    return {"id": persona_id, "response": str(data)}


def render_template(template_path: Path, values: dict[str, str]) -> str:
    template = Template(template_path.read_text(encoding="utf-8"))
    return template.safe_substitute(values)


def slug_from_text(text: str) -> str:
    seed = text.strip()[:30] or "simulation"
    slug = re.sub(r"[^0-9A-Za-z가-힣]+", "-", seed).strip("-")
    return slug or "simulation"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    ids = sub.add_parser("ids")
    ids.add_argument("personas", type=Path)

    system = sub.add_parser("system-prompt")
    system.add_argument("personas", type=Path)
    system.add_argument("persona_id")

    metadata = sub.add_parser("metadata-json")
    metadata.add_argument("personas", type=Path)

    responses = sub.add_parser("responses-json")
    responses.add_argument("responses_dir", type=Path)

    render = sub.add_parser("render")
    render.add_argument("template", type=Path)
    render.add_argument("values_json", type=Path)

    slug = sub.add_parser("slug")
    slug.add_argument("input_file", type=Path)

    args = parser.parse_args()

    if args.command == "ids":
        print("\n".join(item["id"] for item in personas(args.personas)))
    elif args.command == "system-prompt":
        prompt = persona_by_id(args.personas, args.persona_id).get("system_prompt")
        if not isinstance(prompt, str):
            raise SystemExit(f"{args.persona_id} has no system_prompt")
        print(prompt)
    elif args.command == "metadata-json":
        payload = [
            {
                "id": item["id"],
                "metadata": item.get("metadata", {}),
            }
            for item in personas(args.personas)
        ]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif args.command == "responses-json":
        files = sorted(args.responses_dir.glob("P*.json"))
        print(json.dumps([compact_response(path) for path in files], ensure_ascii=False, indent=2))
    elif args.command == "render":
        values = json.loads(args.values_json.read_text(encoding="utf-8"))
        if not isinstance(values, dict):
            raise SystemExit("values_json must contain an object")
        print(render_template(args.template, {str(k): str(v) for k, v in values.items()}))
    elif args.command == "slug":
        print(slug_from_text(args.input_file.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
