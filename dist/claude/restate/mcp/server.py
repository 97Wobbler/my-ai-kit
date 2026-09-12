#!/usr/bin/env python3
"""Restate Clarify stdio MCP server. Python standard library only."""

import json
from pathlib import Path
import sqlite3
import sys

from clarify import domain
from clarify.errors import ClarifyError
from clarify.schema import DESCRIPTIONS, SCHEMAS, validate
from clarify.store import Store

SUPPORTED_PROTOCOLS = ("2025-11-25", "2025-06-18", "2024-11-05")
WRITE_ACTIONS = {"clarify_items_update": domain.update_items,
                 "clarify_round_start": domain.start_round,
                 "clarify_round_review": domain.review_round,
                 "clarify_session_close": domain.close_session}


def version():
    root = Path(__file__).resolve().parent.parent
    for folder in (".claude-plugin", ".codex-plugin"):
        manifest = root / folder / "plugin.json"
        if manifest.exists():
            return json.loads(manifest.read_text())["version"]
    return "0.0.0"


def tools_list():
    return {"tools": [{"name": name, "description": DESCRIPTIONS[name], "inputSchema": schema,
                       "annotations": {"readOnlyHint": name in {"clarify_session_read", "clarify_session_list"},
                                       "destructiveHint": False, "openWorldHint": False}}
                      for name, schema in SCHEMAS.items()]}


def call_tool(name, arguments):
    validate(arguments, SCHEMAS[name])
    if name == "clarify_session_create":
        state = domain.create_state(arguments)
        return domain.snapshot(Store().create(state))
    store = Store()
    if name == "clarify_session_list":
        return {"sessions": store.listing(arguments.get("workspace"), arguments.get("limit", 20)),
                "data_root": str(store.path.parent)}
    if name == "clarify_session_read":
        return domain.snapshot(store.read(arguments["session_id"]), arguments.get("include_history", False))
    state = store.mutate(arguments["session_id"], arguments["expected_revision"],
                         lambda current: WRITE_ACTIONS[name](current, arguments))
    return domain.snapshot(state)


class Protocol:
    def __init__(self):
        self.negotiated = None

    @staticmethod
    def error(request_id, code, message):
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}

    def handle_line(self, line):
        try:
            request = json.loads(line)
        except (ValueError, RecursionError):
            return self.error(None, -32700, "Parse error")
        if not isinstance(request, dict) or request.get("jsonrpc") != "2.0" or not isinstance(request.get("method"), str):
            return self.error(None, -32600, "Invalid Request")
        request_id = request.get("id")
        if "id" not in request:
            # Never execute a tool mutation sent as a notification.
            return None
        if type(request_id) not in (str, int):
            return self.error(None, -32600, "Request id must be a string or integer")
        params = request.get("params", {})
        if not isinstance(params, dict):
            return self.error(request_id, -32602, "params must be an object")
        method = request["method"]
        if method == "initialize":
            if not isinstance(params.get("protocolVersion"), str) or not isinstance(params.get("capabilities"), dict) or not isinstance(params.get("clientInfo"), dict):
                return self.error(request_id, -32602, "Initialization needs protocolVersion, capabilities, and clientInfo")
            proposed = params["protocolVersion"]
            self.negotiated = proposed if proposed in SUPPORTED_PROTOCOLS else SUPPORTED_PROTOCOLS[0]
            result = {"protocolVersion": self.negotiated, "capabilities": {"tools": {}},
                      "serverInfo": {"name": "restate-clarify", "version": version()}}
        elif method == "ping":
            result = {}
        elif method not in {"tools/list", "tools/call"}:
            return self.error(request_id, -32601, "Method not found")
        elif self.negotiated is None:
            return self.error(request_id, -32002, "Initialize the MCP connection first")
        elif method == "tools/list":
            result = tools_list()
            if self.negotiated == "2024-11-05":
                for tool in result["tools"]:
                    tool.pop("annotations")
        else:
            name = params.get("name")
            if not isinstance(name, str) or name not in SCHEMAS:
                return self.error(request_id, -32602, "Unknown tool")
            if "arguments" in params and not isinstance(params["arguments"], dict):
                return self.error(request_id, -32602, "Tool arguments must be an object")
            is_error = False
            try:
                value = call_tool(name, params.get("arguments", {}))
            except ClarifyError as exc:
                value, is_error = {"error": exc.payload()}, True
            except (sqlite3.Error, OSError, ValueError) as exc:
                value, is_error = {"error": {"code": "storage_error", "message": "Could not access interview state; no automatic reset or retry. Check data directory and read the session before retrying.", "type": type(exc).__name__}}, True
            except Exception as exc:
                print(f"Clarify internal error: {type(exc).__name__}", file=sys.stderr)
                return self.error(request_id, -32603, "Internal error; read session state before retrying")
            result = {"content": [{"type": "text", "text": json.dumps(value, ensure_ascii=False)}], "isError": is_error}
            if self.negotiated != "2024-11-05":
                result["structuredContent"] = value
        return {"jsonrpc": "2.0", "id": request_id, "result": result}


def main():
    protocol = Protocol()
    for line in sys.stdin:
        response = protocol.handle_line(line)
        if response is not None:
            print(json.dumps(response, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
