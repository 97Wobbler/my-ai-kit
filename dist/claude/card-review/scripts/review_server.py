#!/usr/bin/env python3
"""Run the local card-review GUI and persist review state."""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import mimetypes
import os
import sys
import threading
import webbrowser
from copy import deepcopy
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from review_schema import fail, load_and_validate_input


SKILL_ROOT = Path(__file__).resolve().parent.parent
APP_DIR = SKILL_ROOT / "assets"
APP_PATH = APP_DIR / "index.html"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def result_path_for(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}-results.jsonl")


def state_path_for(output_path: Path) -> Path:
    return output_path.with_name(f"{output_path.stem}.state.json")


def input_fingerprint(data: dict[str, Any]) -> str:
    encoded = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def is_loopback_host(host: str) -> bool:
    if host.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def url_host(host: str) -> str:
    try:
        return f"[{host}]" if ipaddress.ip_address(host).version == 6 else host
    except ValueError:
        return host


def app_version() -> str:
    digest = hashlib.sha256()
    for path in sorted(APP_DIR.rglob("*")):
        if not path.is_file():
            continue
        stat = path.stat()
        digest.update(str(path.relative_to(APP_DIR)).encode("utf-8"))
        digest.update(str(stat.st_mtime_ns).encode("ascii"))
        digest.update(str(stat.st_size).encode("ascii"))
    return digest.hexdigest()[:16]


class ReviewStore:
    def __init__(self, input_path: Path, output_path: Path, dev_mode: bool = False) -> None:
        self.input_path = input_path.resolve()
        self.output_path = output_path.resolve()
        self.state_path = state_path_for(self.output_path)
        self.dev_mode = dev_mode
        self.data = load_and_validate_input(self.input_path)
        self.input_fingerprint = input_fingerprint(self.data)
        self.items = self.data["items"]
        self.item_by_id = {item["id"]: item for item in self.items}
        self.lock = threading.RLock()
        self.state = self._load_state()
        self._write_results()

    def _empty_snapshot(self) -> dict[str, Any]:
        return {
            "statuses": {item["id"]: None for item in self.items},
            "skipped": [],
            "currentId": self.items[0]["id"],
        }

    def _new_state(self) -> dict[str, Any]:
        return {
            "version": 2,
            "inputPath": str(self.input_path),
            "inputFingerprint": self.input_fingerprint,
            "outputPath": str(self.output_path),
            "finished": False,
            "memos": {},
            "timeline": [self._empty_snapshot()],
            "cursor": 0,
            "updatedAt": now_iso(),
        }

    def _state_ids_match(self, state: dict[str, Any]) -> bool:
        timeline = state.get("timeline")
        cursor = state.get("cursor", 0)
        if not isinstance(timeline, list) or not timeline:
            return False
        if not isinstance(cursor, int) or isinstance(cursor, bool):
            return False
        if cursor < 0 or cursor >= len(timeline):
            return False
        snapshot = timeline[cursor]
        if not isinstance(snapshot, dict):
            return False
        statuses = snapshot.get("statuses")
        return isinstance(statuses, dict) and set(statuses) == set(self.item_by_id)

    def _load_state(self) -> dict[str, Any]:
        if self.state_path.exists():
            try:
                saved = json.loads(self.state_path.read_text(encoding="utf-8"))
                if not isinstance(saved, dict):
                    raise ValueError("Resume state root must be an object.")
                same_input = saved.get("inputPath") == str(self.input_path)
                fingerprint = saved.get("inputFingerprint")
                fingerprint_matches = fingerprint == self.input_fingerprint
                legacy_ids_match = fingerprint is None and self._state_ids_match(saved)
                if same_input and (fingerprint_matches or legacy_ids_match):
                    repaired = self._repair_state(saved)
                    self._write_state(repaired)
                    return repaired
            except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
                pass

        state = self._new_state()
        if self.output_path.exists():
            self._merge_existing_output(state)
        self._write_state(state)
        return state

    def _repair_snapshot(self, snapshot: Any) -> dict[str, Any]:
        if not isinstance(snapshot, dict):
            raise ValueError("Resume timeline entries must be objects.")

        raw_statuses = snapshot.get("statuses")
        if not isinstance(raw_statuses, dict):
            raise ValueError("Resume statuses must be an object.")
        statuses = {
            item_id: raw_statuses.get(item_id)
            if raw_statuses.get(item_id) in {"A", "B"}
            else None
            for item_id in self.item_by_id
        }

        raw_skipped = snapshot.get("skipped", [])
        if not isinstance(raw_skipped, list):
            raw_skipped = []
        skipped: list[str] = []
        for item_id in raw_skipped:
            if item_id in self.item_by_id and statuses[item_id] is None and item_id not in skipped:
                skipped.append(item_id)

        current_id = snapshot.get("currentId")
        if current_id not in self.item_by_id:
            current_id = next(
                (item_id for item_id, status in statuses.items() if status is None and item_id not in skipped),
                None,
            )
            if current_id is None:
                current_id = next((item_id for item_id in skipped if statuses[item_id] is None), None)

        return {"statuses": statuses, "skipped": skipped, "currentId": current_id}

    def _repair_state(self, state: dict[str, Any]) -> dict[str, Any]:
        raw_timeline = state.get("timeline")
        if not isinstance(raw_timeline, list) or not raw_timeline:
            raise ValueError("Resume timeline must be a non-empty array.")
        timeline = [self._repair_snapshot(snapshot) for snapshot in raw_timeline]

        cursor = state.get("cursor", len(timeline) - 1)
        if not isinstance(cursor, int) or isinstance(cursor, bool):
            cursor = len(timeline) - 1
        cursor = max(0, min(cursor, len(timeline) - 1))

        legacy_memos = raw_timeline[cursor].get("memos", {})
        raw_memos = state.get("memos", legacy_memos)
        if not isinstance(raw_memos, dict):
            raw_memos = {}
        memos = {
            item_id: memo
            for item_id, memo in raw_memos.items()
            if item_id in self.item_by_id and isinstance(memo, str) and memo.strip()
        }

        return {
            "version": 2,
            "inputPath": str(self.input_path),
            "inputFingerprint": self.input_fingerprint,
            "outputPath": str(self.output_path),
            "finished": state.get("finished") is True,
            "memos": memos,
            "timeline": timeline,
            "cursor": cursor,
            "updatedAt": state.get("updatedAt", now_iso()),
        }

    def _merge_existing_output(self, state: dict[str, Any]) -> None:
        snapshot = state["timeline"][0]
        try:
            lines = self.output_path.read_text(encoding="utf-8").splitlines()
        except OSError:
            return
        for line in lines:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                if not isinstance(row, dict):
                    continue
                item_id = row.get("id")
                if item_id not in self.item_by_id:
                    continue
                result = row.get("result")
                if result in {"A", "B", None}:
                    snapshot["statuses"][item_id] = result
                memo = row.get("memo")
                if isinstance(memo, str) and memo.strip():
                    state["memos"][item_id] = memo
            except (json.JSONDecodeError, TypeError):
                continue

        if snapshot["statuses"].get(snapshot.get("currentId")) is not None:
            snapshot["currentId"] = self._next_candidate(snapshot)
            if snapshot["currentId"] is None:
                snapshot["currentId"] = self._next_candidate(snapshot, include_skipped=True)

    def _write_state(self, state: dict[str, Any] | None = None) -> None:
        target = state or self.state
        target["updatedAt"] = now_iso()
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = self.state_path.with_suffix(self.state_path.suffix + ".tmp")
        tmp_path.write_text(json.dumps(target, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp_path, self.state_path)

    def _snapshot(self) -> dict[str, Any]:
        return deepcopy(self.state["timeline"][self.state["cursor"]])

    def _apply_snapshot(self, snapshot: dict[str, Any]) -> None:
        timeline = self.state["timeline"]
        timeline[self.state["cursor"]] = deepcopy(snapshot)

    def _commit_snapshot(self, snapshot: dict[str, Any]) -> None:
        cursor = self.state["cursor"]
        self.state["timeline"] = self.state["timeline"][: cursor + 1]
        self.state["timeline"].append(deepcopy(snapshot))
        self.state["cursor"] += 1
        self._write_state()

    def _next_candidate(self, snapshot: dict[str, Any], include_skipped: bool = False) -> str | None:
        current_id = snapshot.get("currentId")
        start = 0
        if current_id in self.item_by_id:
            start = (list(self.item_by_id).index(current_id) + 1) % len(self.items)
        skipped = set(snapshot.get("skipped", []))
        ordered = self.items[start:] + self.items[:start]
        for item in ordered:
            item_id = item["id"]
            if snapshot["statuses"].get(item_id) is not None:
                continue
            if not include_skipped and item_id in skipped:
                continue
            return item_id
        return None

    def _summary(self, snapshot: dict[str, Any]) -> dict[str, int]:
        values = list(snapshot["statuses"].values())
        return {
            "total": len(values),
            "a": sum(value == "A" for value in values),
            "b": sum(value == "B" for value in values),
            "unclassified": sum(value is None for value in values),
            "skipped": len(snapshot.get("skipped", [])),
        }

    def _set_memo(self, item_id: str, memo: Any) -> None:
        if not isinstance(memo, str):
            return
        if memo.strip():
            self.state["memos"][item_id] = memo
        else:
            self.state["memos"].pop(item_id, None)

    def _public_state(self, include_static: bool = False) -> dict[str, Any]:
        with self.lock:
            snapshot = self._snapshot()
            result = {
                "statuses": snapshot["statuses"],
                "memos": self.state["memos"],
                "skipped": snapshot.get("skipped", []),
                "currentId": snapshot.get("currentId"),
                "finished": self.state.get("finished", False),
                "summary": self._summary(snapshot),
                "canUndo": self.state["cursor"] > 0,
                "canRedo": self.state["cursor"] < len(self.state["timeline"]) - 1,
                "outputPath": str(self.output_path),
                "statePath": str(self.state_path),
                "updatedAt": self.state.get("updatedAt"),
                "devMode": self.dev_mode,
            }
            if include_static:
                result["option"] = self.data["option"]
                result["items"] = self.items
            return result

    def _write_results(self) -> None:
        snapshot = self._snapshot()
        lines: list[str] = []
        for item in self.items:
            item_id = item["id"]
            row: dict[str, Any] = {"id": item_id, "result": snapshot["statuses"].get(item_id)}
            if self.state["memos"].get(item_id):
                row["memo"] = self.state["memos"][item_id]
            lines.append(json.dumps(row, ensure_ascii=False))
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = self.output_path.with_suffix(self.output_path.suffix + ".tmp")
        tmp_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        os.replace(tmp_path, self.output_path)

    def action(self, payload: dict[str, Any]) -> dict[str, Any]:
        with self.lock:
            action = payload.get("action")
            if action == "undo":
                if self.state["cursor"] > 0:
                    self.state["cursor"] -= 1
                    self._write_results()
                    self._write_state()
                return self._public_state()
            if action == "redo":
                if self.state["cursor"] < len(self.state["timeline"]) - 1:
                    self.state["cursor"] += 1
                    self._write_results()
                    self._write_state()
                return self._public_state()
            if action == "focus":
                item_id = payload.get("id")
                if item_id not in self.item_by_id:
                    fail(f"Unknown item id: {item_id}")
                snapshot = self._snapshot()
                snapshot["currentId"] = item_id
                self._apply_snapshot(snapshot)
                self._write_state()
                return self._public_state()
            if action == "memo":
                item_id = payload.get("id")
                if item_id not in self.item_by_id:
                    fail(f"Unknown item id: {item_id}")
                snapshot = self._snapshot()
                memo = payload.get("memo", "")
                if not isinstance(memo, str):
                    fail("memo must be a string.")
                self._set_memo(item_id, memo)
                self._write_state()
                self._write_results()
                return self._public_state()
            if action == "classify":
                result = payload.get("result")
                if result not in {"A", "B"}:
                    fail('classify action requires result "A" or "B".')
                snapshot = self._snapshot()
                item_id = snapshot.get("currentId")
                if item_id not in self.item_by_id:
                    fail("There is no current item.")
                snapshot["statuses"][item_id] = result
                snapshot["skipped"] = [value for value in snapshot.get("skipped", []) if value != item_id]
                self._set_memo(item_id, payload.get("memo"))
                snapshot["currentId"] = self._next_candidate(snapshot)
                if snapshot["currentId"] is None:
                    snapshot["currentId"] = self._next_candidate(snapshot, include_skipped=True)
                self._commit_snapshot(snapshot)
                self._write_results()
                return self._public_state()
            if action == "skip":
                snapshot = self._snapshot()
                item_id = snapshot.get("currentId")
                if item_id not in self.item_by_id:
                    fail("There is no current item.")
                if item_id not in snapshot["skipped"] and snapshot["statuses"].get(item_id) is None:
                    snapshot["skipped"].append(item_id)
                self._set_memo(item_id, payload.get("memo"))
                snapshot["currentId"] = self._next_candidate(snapshot)
                if snapshot["currentId"] is None:
                    snapshot["currentId"] = self._next_candidate(snapshot, include_skipped=True)
                self._commit_snapshot(snapshot)
                self._write_results()
                return self._public_state()
            if action == "finish":
                snapshot = self._snapshot()
                item_id = snapshot.get("currentId")
                if item_id in self.item_by_id:
                    self._set_memo(item_id, payload.get("memo"))
                self.state["finished"] = True
                self._write_results()
                self._write_state()
                return self._public_state()
            if action == "reopen":
                self.state["finished"] = False
                self._write_state()
                return self._public_state()
            fail(f"Unknown action: {action}")


class RequestHandler(BaseHTTPRequestHandler):
    store: ReviewStore

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _send_json(self, body: dict[str, Any], status: int = HTTPStatus.OK) -> None:
        encoded = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(encoded)

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        value = json.loads(raw.decode("utf-8"))
        if not isinstance(value, dict):
            fail("Request body must be a JSON object.")
        return value

    def _send_file(self, path: Path) -> None:
        try:
            body = path.read_bytes()
        except OSError as exc:
            self._send_json({"error": str(exc)}, HTTPStatus.NOT_FOUND)
            return
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        if content_type.startswith("text/") or content_type in {"application/javascript", "application/json"}:
            content_type += "; charset=utf-8"
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store" if self.store.dev_mode else "no-cache")
        self.end_headers()
        self.wfile.write(body)

    def _asset_path(self, route: str) -> Path | None:
        relative = unquote(route.removeprefix("/assets/")).lstrip("/")
        target = (APP_DIR / relative).resolve()
        if target == APP_DIR or APP_DIR not in target.parents:
            return None
        return target

    def do_GET(self) -> None:
        route = urlparse(self.path).path
        if route == "/api/state":
            self._send_json(self.store._public_state(include_static=True))
            return
        if route == "/api/dev-version":
            self._send_json({"enabled": self.store.dev_mode, "version": app_version()})
            return
        if route == "/":
            self._send_file(APP_PATH)
            return
        if route.startswith("/assets/"):
            asset_path = self._asset_path(route)
            if asset_path is None:
                self._send_json({"error": "Invalid asset path"}, HTTPStatus.BAD_REQUEST)
                return
            self._send_file(asset_path)
            return
        self._send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)

    def do_POST(self) -> None:
        route = urlparse(self.path).path
        if route != "/api/action":
            self._send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
            return
        try:
            result = self.store.action(self._read_json())
            self._send_json(result)
        except (ValueError, json.JSONDecodeError) as exc:
            self._send_json({"error": str(exc)}, HTTPStatus.BAD_REQUEST)
        except Exception as exc:  # pragma: no cover - defensive server boundary
            self._send_json({"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local card-review GUI.")
    parser.add_argument("input", type=Path, help="Standard review input JSON file")
    parser.add_argument("--output", type=Path, help="Result JSONL path")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=0, help="Port; 0 selects a free local port")
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--dev", action="store_true", help="Auto-reload the browser when frontend assets change")
    args = parser.parse_args()

    if not is_loopback_host(args.host):
        print(
            "card-review: --host must be localhost or a loopback IP address; "
            "the review API is not authenticated.",
            file=sys.stderr,
        )
        return 2

    input_path = args.input.resolve()
    output_path = (args.output or result_path_for(input_path)).resolve()
    try:
        store = ReviewStore(input_path, output_path, dev_mode=args.dev)
    except ValueError as exc:
        print(f"card-review: {exc}", file=sys.stderr)
        return 2

    class BoundHandler(RequestHandler):
        pass

    BoundHandler.store = store
    server = ThreadingHTTPServer((args.host, args.port), BoundHandler)
    url = f"http://{url_host(args.host)}:{server.server_port}/"
    print(f"card-review URL: {url}", flush=True)
    print(f"card-review results: {output_path}", flush=True)
    print(f"card-review state: {store.state_path}", flush=True)
    if args.dev:
        print("card-review dev reload: on", flush=True)
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\ncard-review stopped; the latest state is saved.", flush=True)
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
