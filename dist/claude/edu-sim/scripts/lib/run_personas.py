#!/usr/bin/env python3
"""Collect one Claude headless response for every persona."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import threading
from pathlib import Path

from persona_tool import personas, render_template


MODEL = "claude-sonnet-4-6"
RATE_LIMIT_RE = re.compile(r"(429|rate.?limit)", re.IGNORECASE)
RATE_LIMIT_STOP_REASON = "stopped after 3 consecutive rate limit failures"


class RateLimitStop(RuntimeError):
    """Raised when the run should stop after repeated rate-limit failures."""


def write_error(path: Path, persona_id: str, reason: str) -> None:
    path.write_text(
        json.dumps(
            {"error": True, "persona_id": persona_id, "reason": reason},
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


def append_error(errors_log: Path, text: str) -> None:
    with errors_log.open("a", encoding="utf-8") as handle:
        handle.write(text)
        if text and not text.endswith("\n"):
            handle.write("\n")


def run_claude(command: list[str], stop_event: threading.Event) -> subprocess.CompletedProcess[str]:
    if stop_event.is_set():
        raise RateLimitStop(RATE_LIMIT_STOP_REASON)

    process = subprocess.Popen(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    while process.poll() is None:
        if stop_event.wait(0.2):
            process.terminate()
            try:
                stdout, stderr = process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate()
            raise RateLimitStop(RATE_LIMIT_STOP_REASON)

    stdout, stderr = process.communicate()
    return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)


def run_one(
    persona: dict[str, object],
    prompt: str,
    run_dir: Path,
    errors_log: Path,
    rate_limit_state: dict[str, int],
    lock: threading.Lock,
    stop_event: threading.Event,
) -> str:
    persona_id = str(persona["id"])
    output_path = run_dir / "responses" / f"{persona_id}.json"
    system_prompt = str(persona.get("system_prompt", ""))
    command = [
        "claude",
        "-p",
        prompt,
        "--append-system-prompt",
        system_prompt,
        "--model",
        MODEL,
        "--output-format",
        "json",
        "--max-turns",
        "1",
        "--disallowedTools",
        "*",
    ]

    for attempt in range(2):
        completed = run_claude(command, stop_event)
        if completed.returncode == 0:
            output_path.write_text(completed.stdout, encoding="utf-8")
            with lock:
                rate_limit_state["consecutive"] = 0
            if completed.stderr:
                append_error(errors_log, f"[{persona_id}] stderr:\n{completed.stderr}")
            return persona_id

        stderr = completed.stderr or completed.stdout or f"exit code {completed.returncode}"
        append_error(errors_log, f"[{persona_id}] attempt {attempt + 1} failed:\n{stderr}")
        is_rate_limit = bool(RATE_LIMIT_RE.search(stderr))
        if is_rate_limit:
            with lock:
                rate_limit_state["consecutive"] += 1
                consecutive = rate_limit_state["consecutive"]
            if consecutive >= 3:
                stop_event.set()
                write_error(output_path, persona_id, RATE_LIMIT_STOP_REASON)
                raise RateLimitStop(RATE_LIMIT_STOP_REASON)
            if stop_event.wait(60):
                raise RateLimitStop(RATE_LIMIT_STOP_REASON)
        elif attempt == 0:
            if stop_event.wait(30):
                raise RateLimitStop(RATE_LIMIT_STOP_REASON)

    write_error(output_path, persona_id, stderr.strip())
    return persona_id


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin_root", type=Path)
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()

    plugin_root = args.plugin_root.resolve()
    run_dir = args.run_dir.resolve()
    input_path = run_dir / "input.md"
    responses_dir = run_dir / "responses"
    errors_log = run_dir / "errors.log"
    responses_dir.mkdir(parents=True, exist_ok=True)

    input_text = input_path.read_text(encoding="utf-8")
    prompt = render_template(plugin_root / "prompts" / "persona_response.tmpl", {"INPUT": input_text})
    pool = personas(plugin_root / "personas.yaml")
    max_workers = int(os.environ.get("MAX_CONCURRENCY", "3"))
    max_workers = max(1, min(max_workers, 3))

    rate_limit_state = {"consecutive": 0}
    lock = threading.Lock()
    stop_event = threading.Event()
    completed_count = 0

    persona_iter = iter(pool)
    pending: set[concurrent.futures.Future[str]] = set()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    def submit_next() -> bool:
        try:
            item = next(persona_iter)
        except StopIteration:
            return False
        pending.add(
            executor.submit(
                run_one,
                item,
                prompt,
                run_dir,
                errors_log,
                rate_limit_state,
                lock,
                stop_event,
            )
        )
        return True

    try:
        for _ in range(max_workers):
            if not submit_next():
                break

        while pending:
            done, pending = concurrent.futures.wait(
                pending,
                return_when=concurrent.futures.FIRST_COMPLETED,
            )
            for future in done:
                try:
                    persona_id = future.result()
                except RateLimitStop as exc:
                    stop_event.set()
                    for queued in pending:
                        queued.cancel()
                    append_error(errors_log, f"[run] {exc}; cancelling queued persona calls")
                    print(str(exc), flush=True)
                    return 1
                completed_count += 1
                print(f"{completed_count}/{len(pool)} complete: {persona_id}", flush=True)

            while not stop_event.is_set() and len(pending) < max_workers and submit_next():
                pass
    finally:
        executor.shutdown(wait=True, cancel_futures=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
