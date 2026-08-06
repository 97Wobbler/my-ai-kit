#!/usr/bin/env python3
"""Dependency-free regression tests for the card-review state machine."""

from __future__ import annotations

import json
import tempfile
import threading
import unittest
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

from review_schema import load_and_validate_input
from review_server import APP_PATH, SKILL_ROOT, RequestHandler, ReviewStore, is_loopback_host


def sample_input() -> dict:
    return {
        "version": "1",
        "option": {
            "title": "Test review",
            "groupAName": "Keep",
            "groupBName": "Drop",
            "fields": {"title": {"label": "Title", "render": "h2"}},
        },
        "items": [
            {"id": "one", "title": "First"},
            {"id": "two", "title": "Second"},
            {"id": "three", "title": "Third"},
        ],
    }


class CardReviewTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        root = Path(self.tempdir.name)
        self.input_path = root / "input.json"
        self.output_path = root / "results.jsonl"
        self.input_path.write_text(json.dumps(sample_input()), encoding="utf-8")

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_shared_schema_rejects_duplicate_ids(self) -> None:
        data = sample_input()
        data["items"][1]["id"] = "one"
        self.input_path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate item id"):
            load_and_validate_input(self.input_path)

    def test_classify_skip_undo_and_redo(self) -> None:
        store = ReviewStore(self.input_path, self.output_path)

        initial = store._public_state(include_static=True)
        self.assertEqual(len(initial["items"]), 3)
        self.assertIn("option", initial)

        classified = store.action({"action": "classify", "result": "A", "memo": "good"})
        self.assertNotIn("items", classified)
        self.assertNotIn("option", classified)
        self.assertEqual(classified["statuses"]["one"], "A")
        self.assertEqual(classified["currentId"], "two")

        skipped = store.action({"action": "skip", "memo": "later"})
        self.assertIn("two", skipped["skipped"])
        self.assertEqual(skipped["currentId"], "three")

        undone = store.action({"action": "undo"})
        self.assertNotIn("two", undone["skipped"])
        self.assertEqual(undone["currentId"], "two")

        redone = store.action({"action": "redo"})
        self.assertIn("two", redone["skipped"])
        self.assertEqual(redone["currentId"], "three")

        rows = [json.loads(line) for line in self.output_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(rows[0], {"id": "one", "result": "A", "memo": "good"})
        self.assertEqual(rows[1], {"id": "two", "result": None, "memo": "later"})
        self.assertEqual(len(rows), 3)

    def test_memos_persist_without_entering_undo_history(self) -> None:
        store = ReviewStore(self.input_path, self.output_path)

        memo_only = store.action({"action": "memo", "id": "one", "memo": "draft"})
        self.assertFalse(memo_only["canUndo"])

        classified = store.action({"action": "classify", "result": "B", "memo": "classified"})
        self.assertTrue(classified["canUndo"])
        store.action({"action": "memo", "id": "one", "memo": "latest"})

        undone = store.action({"action": "undo"})
        self.assertIsNone(undone["statuses"]["one"])
        self.assertEqual(undone["memos"]["one"], "latest")
        self.assertFalse(undone["canUndo"])

        redone = store.action({"action": "redo"})
        self.assertEqual(redone["statuses"]["one"], "B")
        self.assertEqual(redone["memos"]["one"], "latest")

    def test_legacy_snapshot_memos_are_migrated(self) -> None:
        store = ReviewStore(self.input_path, self.output_path)
        legacy = json.loads(store.state_path.read_text(encoding="utf-8"))
        legacy.pop("memos", None)
        legacy["timeline"][0]["memos"] = {"one": "legacy"}
        store.state_path.write_text(json.dumps(legacy), encoding="utf-8")

        restored = ReviewStore(self.input_path, self.output_path)._public_state()
        self.assertEqual(restored["memos"]["one"], "legacy")

    def test_changed_input_rebases_state_and_preserves_matching_results(self) -> None:
        store = ReviewStore(self.input_path, self.output_path)
        store.action({"action": "classify", "result": "A", "memo": "keep"})

        changed = sample_input()
        changed["items"] = [
            {"id": "one", "title": "First, revised"},
            {"id": "four", "title": "Fourth"},
        ]
        self.input_path.write_text(json.dumps(changed), encoding="utf-8")

        restored = ReviewStore(self.input_path, self.output_path)._public_state()
        self.assertEqual(restored["statuses"], {"one": "A", "four": None})
        self.assertEqual(restored["memos"], {"one": "keep"})
        self.assertEqual(restored["currentId"], "four")
        self.assertFalse(restored["canUndo"])

        rows = [json.loads(line) for line in self.output_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(rows, [
            {"id": "one", "result": "A", "memo": "keep"},
            {"id": "four", "result": None},
        ])

    def test_malformed_resume_state_falls_back_to_valid_result(self) -> None:
        store = ReviewStore(self.input_path, self.output_path)
        store.action({"action": "classify", "result": "B", "memo": "drop"})
        store.state_path.write_text(
            json.dumps({"inputPath": str(self.input_path.resolve()), "timeline": "broken"}),
            encoding="utf-8",
        )

        restored = ReviewStore(self.input_path, self.output_path)._public_state()
        self.assertEqual(restored["statuses"]["one"], "B")
        self.assertEqual(restored["memos"]["one"], "drop")
        self.assertFalse(restored["canUndo"])

    def test_plugin_assets_and_loopback_policy(self) -> None:
        self.assertEqual(APP_PATH, SKILL_ROOT / "assets" / "index.html")
        self.assertTrue(APP_PATH.is_file())
        self.assertTrue(is_loopback_host("localhost"))
        self.assertTrue(is_loopback_host("127.0.0.1"))
        self.assertTrue(is_loopback_host("::1"))
        self.assertFalse(is_loopback_host("0.0.0.0"))
        self.assertFalse(is_loopback_host("192.168.0.10"))

    def test_http_server_serves_ui_and_persists_action(self) -> None:
        store = ReviewStore(self.input_path, self.output_path)

        class BoundHandler(RequestHandler):
            pass

        BoundHandler.store = store
        server = ThreadingHTTPServer(("127.0.0.1", 0), BoundHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base_url = f"http://127.0.0.1:{server.server_port}"
        try:
            with urllib.request.urlopen(f"{base_url}/", timeout=2) as response:
                self.assertIn("Card Review", response.read().decode("utf-8"))

            request = urllib.request.Request(
                f"{base_url}/api/action",
                data=json.dumps({"action": "classify", "result": "A", "memo": "http"}).encode(),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=2) as response:
                state = json.loads(response.read().decode("utf-8"))
            self.assertEqual(state["statuses"]["one"], "A")

            finish_request = urllib.request.Request(
                f"{base_url}/api/action",
                data=json.dumps({"action": "finish"}).encode(),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(finish_request, timeout=2) as response:
                finished_state = json.loads(response.read().decode("utf-8"))
            self.assertTrue(finished_state["finished"])

            rows = [json.loads(line) for line in self.output_path.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(rows[0], {"id": "one", "result": "A", "memo": "http"})
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
