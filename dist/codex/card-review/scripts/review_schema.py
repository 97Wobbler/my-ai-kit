"""Shared input loading and validation for card-review scripts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ALLOWED_RENDERERS = {"h1", "h2", "h3", "image", "markdown", "ol", "ul", "text", "link"}


def fail(message: str) -> None:
    raise ValueError(message)


def load_and_validate_input(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Input file does not exist: {path}")
    except json.JSONDecodeError as exc:
        fail(f"Input is not valid JSON: {exc}")

    if not isinstance(data, dict):
        fail("Input root must be a JSON object.")
    if data.get("version") != "1":
        fail('Input must contain "version": "1".')

    option = data.get("option")
    if not isinstance(option, dict):
        fail('Input must contain an "option" object.')
    for key in ("title", "groupAName", "groupBName"):
        if not isinstance(option.get(key), str) or not option[key].strip():
            fail(f"option.{key} must be a non-empty string.")

    fields = option.get("fields")
    if not isinstance(fields, dict) or not fields:
        fail("option.fields must be a non-empty object.")
    for key, spec in fields.items():
        if not isinstance(key, str) or not key:
            fail("Every option.fields key must be a non-empty string.")
        if isinstance(spec, str):
            renderer = spec
        elif isinstance(spec, dict):
            renderer = spec.get("render")
        else:
            fail(f"Field spec for {key!r} must be a string or object.")
        if renderer not in ALLOWED_RENDERERS:
            allowed = ", ".join(sorted(ALLOWED_RENDERERS))
            fail(f"Unsupported renderer for {key!r}: {renderer!r}. Use: {allowed}.")

    items = data.get("items")
    if not isinstance(items, list) or not items:
        fail('Input must contain a non-empty "items" array.')
    ids: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            fail(f"items[{index}] must be an object.")
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id.strip():
            fail(f"items[{index}].id must be a non-empty string.")
        if item_id in ids:
            fail(f"Duplicate item id: {item_id}")
        ids.add(item_id)
        for key, spec in fields.items():
            renderer = spec if isinstance(spec, str) else spec.get("render")
            if renderer != "image":
                continue
            value = item.get(key, item.get("fields", {}).get(key) if isinstance(item.get("fields"), dict) else None)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                fail(f"items[{index}].{key} must be a non-empty local image path.")

    return data
