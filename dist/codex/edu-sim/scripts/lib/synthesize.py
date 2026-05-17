#!/usr/bin/env python3
"""Synthesize persona responses into a Markdown report."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from pathlib import Path

from persona_tool import personas, render_template, compact_response


MODEL = "claude-sonnet-4-6"
RATE_LIMIT_RE = re.compile(r"(429|rate.?limit)", re.IGNORECASE)


def append_error(errors_log: Path, text: str) -> None:
    with errors_log.open("a", encoding="utf-8") as handle:
        handle.write(text)
        if text and not text.endswith("\n"):
            handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin_root", type=Path)
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()

    plugin_root = args.plugin_root.resolve()
    run_dir = args.run_dir.resolve()
    input_text = (run_dir / "input.md").read_text(encoding="utf-8")
    responses = [compact_response(path) for path in sorted((run_dir / "responses").glob("P*.json"))]
    metadata = [
        {
            "id": item["id"],
            "metadata": item.get("metadata", {}),
        }
        for item in personas(plugin_root / "personas.yaml")
    ]
    prompt = render_template(
        plugin_root / "prompts" / "synthesis.tmpl",
        {
            "INPUT": input_text,
            "PERSONA_METADATA_JSON": json.dumps(metadata, ensure_ascii=False, indent=2),
            "ALL_RESPONSES_JSON": json.dumps(responses, ensure_ascii=False, indent=2),
        },
    )
    command = [
        "claude",
        "-p",
        prompt,
        "--model",
        MODEL,
        "--output-format",
        "text",
        "--max-turns",
        "1",
        "--disallowedTools",
        "*",
    ]
    errors_log = run_dir / "errors.log"
    for attempt in range(2):
        completed = subprocess.run(command, text=True, capture_output=True)
        if completed.returncode == 0:
            (run_dir / "report.md").write_text(completed.stdout, encoding="utf-8")
            if completed.stderr:
                append_error(errors_log, f"[synthesis] stderr:\n{completed.stderr}")
            return 0

        stderr = completed.stderr or completed.stdout or f"exit code {completed.returncode}"
        append_error(errors_log, f"[synthesis] attempt {attempt + 1} failed:\n{stderr}")
        time.sleep(60 if RATE_LIMIT_RE.search(stderr) else 30)

    print("synthesis failed; persona response originals are preserved", flush=True)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
