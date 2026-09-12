"""Transactional session snapshots; read and discovery paths never initialize storage."""

import json
import os
from pathlib import Path
import sqlite3

from .domain import now
from .errors import ClarifyError


def data_root():
    raw = os.environ.get("RESTATE_CLARIFY_DATA_DIR", "~/.restate/clarify")
    path = Path(raw).expanduser()
    if not raw.strip() or "$" in raw or not path.is_absolute():
        raise ClarifyError("invalid_data_root", "RESTATE_CLARIFY_DATA_DIR must be an absolute path with no unresolved placeholders")
    return path.resolve()


class Store:
    def __init__(self, root=None):
        self.path = (Path(root) if root is not None else data_root()) / "sessions.sqlite3"

    def _connect(self, mode):
        return sqlite3.connect(self.path.as_uri() + f"?mode={mode}", uri=True, timeout=5)

    @staticmethod
    def _decode(row):
        state = json.loads(row[0])
        if state.get("schema_version") != 1:
            raise ClarifyError("unsupported_state_version", "This session needs a compatible plugin; stored data was not changed")
        return state

    def create(self, state):
        self.path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        conn = self._connect("rwc")
        try:
            with conn:
                conn.execute("CREATE TABLE IF NOT EXISTS sessions (session_id TEXT PRIMARY KEY, title TEXT NOT NULL, workspace TEXT NOT NULL, revision INTEGER NOT NULL, updated_at TEXT NOT NULL, body TEXT NOT NULL)")
                try:
                    conn.execute("INSERT INTO sessions VALUES (?, ?, ?, ?, ?, ?)",
                                 (state["session_id"], state["title"], state["workspace"],
                                  state["revision"], state["updated_at"], json.dumps(state, ensure_ascii=False)))
                except sqlite3.IntegrityError as exc:
                    raise ClarifyError("session_exists", "Session ID already exists; read it before creating or retrying", session_id=state["session_id"]) from exc
        finally:
            conn.close()
        return state

    def read(self, session_id):
        if not self.path.exists():
            raise ClarifyError("missing_session", "Session store does not exist", session_id=session_id)
        conn = self._connect("ro")
        try:
            row = conn.execute("SELECT body FROM sessions WHERE session_id=?", (session_id,)).fetchone()
            if not row:
                raise ClarifyError("missing_session", "Unknown session", session_id=session_id)
            return self._decode(row)
        finally:
            conn.close()

    def listing(self, workspace=None, limit=20):
        if not self.path.exists():
            return []
        conn = self._connect("ro")
        try:
            query = "SELECT session_id, title, workspace, revision, updated_at FROM sessions"
            params = []
            if workspace is not None:
                query += " WHERE workspace=?"
                params.append(workspace)
            query += " ORDER BY updated_at DESC, session_id LIMIT ?"
            params.append(limit)
            return [dict(zip(["session_id", "title", "workspace", "revision", "updated_at"], row))
                    for row in conn.execute(query, params)]
        finally:
            conn.close()

    def mutate(self, session_id, expected_revision, action):
        if not self.path.exists():
            raise ClarifyError("missing_session", "Session store does not exist", session_id=session_id)
        conn = self._connect("rw")
        try:
            with conn:
                conn.execute("BEGIN IMMEDIATE")
                row = conn.execute("SELECT body FROM sessions WHERE session_id=?", (session_id,)).fetchone()
                if not row:
                    raise ClarifyError("missing_session", "Unknown session", session_id=session_id)
                state = self._decode(row)
                if state["revision"] != expected_revision:
                    raise ClarifyError("stale_revision", "Read the current session before applying changes", current_revision=state["revision"])
                if state["status"] != "active":
                    raise ClarifyError("session_closed", "This session is closed; preserve it and start a new session for further work")
                action(state)
                state["revision"] += 1
                state["updated_at"] = now()
                conn.execute("UPDATE sessions SET revision=?, updated_at=?, body=? WHERE session_id=?",
                             (state["revision"], state["updated_at"], json.dumps(state, ensure_ascii=False), session_id))
                return state
        finally:
            conn.close()
