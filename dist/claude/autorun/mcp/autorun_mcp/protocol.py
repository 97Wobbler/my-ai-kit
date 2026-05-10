"""Small JSON-RPC helpers for the Autorun MCP server.

This module intentionally uses only the Python standard library. It implements
the response and error handling needed by the stdio entrypoint without taking a
runtime dependency on an MCP SDK.
"""

from __future__ import annotations

import json
from typing import Any, Callable, Mapping

JSONRPC_VERSION = "2.0"

PARSE_ERROR = -32700
INVALID_REQUEST = -32600
METHOD_NOT_FOUND = -32601
INVALID_PARAMS = -32602
INTERNAL_ERROR = -32603
TOOL_ERROR = -32000


class JsonRpcError(Exception):
    """Exception that can be serialized as a JSON-RPC error response."""

    def __init__(self, code: int, message: str, data: Any | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.data = data


Handler = Callable[[Mapping[str, Any]], Any]


class JsonRpcProtocol:
    """Line-oriented JSON-RPC request dispatcher."""

    def __init__(self, handlers: Mapping[str, Handler]):
        self._handlers = dict(handlers)

    def handle_line(self, line: str) -> str | None:
        """Return a JSON-RPC response string for a request line.

        Notifications do not receive responses. Parse failures, invalid
        requests, unknown methods, and handler failures are converted to JSON-RPC
        errors so one bad input line does not terminate the server process.
        """

        try:
            payload = json.loads(line)
        except json.JSONDecodeError as exc:
            return dumps_response(
                error_response(
                    None,
                    PARSE_ERROR,
                    "Parse error",
                    {"message": exc.msg, "line": exc.lineno, "column": exc.colno},
                )
            )

        request_id = payload.get("id") if isinstance(payload, dict) else None
        expects_response = isinstance(payload, dict) and "id" in payload

        try:
            result = self._dispatch(payload)
        except JsonRpcError as exc:
            if not expects_response:
                return None
            return dumps_response(error_response(request_id, exc.code, exc.message, exc.data))
        except Exception as exc:  # Defensive boundary for skeleton tools.
            if not expects_response:
                return None
            return dumps_response(
                error_response(
                    request_id,
                    INTERNAL_ERROR,
                    "Internal error",
                    {"error": str(exc)},
                )
            )

        if not expects_response:
            return None
        return dumps_response(success_response(request_id, result))

    def _dispatch(self, payload: Any) -> Any:
        if not isinstance(payload, dict):
            raise JsonRpcError(INVALID_REQUEST, "Invalid Request")
        if payload.get("jsonrpc") != JSONRPC_VERSION:
            raise JsonRpcError(INVALID_REQUEST, "Invalid Request")

        method = payload.get("method")
        if not isinstance(method, str):
            raise JsonRpcError(INVALID_REQUEST, "Invalid Request")

        params = payload.get("params", {})
        if params is None:
            params = {}
        if not isinstance(params, dict):
            raise JsonRpcError(INVALID_PARAMS, "Invalid params")

        handler = self._handlers.get(method)
        if handler is None:
            raise JsonRpcError(METHOD_NOT_FOUND, f"Method not found: {method}")

        return handler(params)


def success_response(request_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": JSONRPC_VERSION, "id": request_id, "result": result}


def error_response(
    request_id: Any,
    code: int,
    message: str,
    data: Any | None = None,
) -> dict[str, Any]:
    error: dict[str, Any] = {"code": code, "message": message}
    if data is not None:
        error["data"] = data
    return {"jsonrpc": JSONRPC_VERSION, "id": request_id, "error": error}


def dumps_response(response: Mapping[str, Any]) -> str:
    return json.dumps(response, ensure_ascii=False, separators=(",", ":"))
