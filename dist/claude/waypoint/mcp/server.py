#!/usr/bin/env python3
"""Waypoint MCP stdio JSON-RPC server."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Mapping

from waypoint_mcp.inspectors import WaypointInspectError, audit_repo, discover_repo, doctor_repo
from waypoint_mcp.protocol import JsonRpcError, JsonRpcProtocol, TOOL_ERROR

SERVER_NAME = "waypoint"
SERVER_VERSION = "0.1.2"
PROTOCOL_VERSION = "2024-11-05"
TOOL_WAYPOINT_AUDIT = "waypoint_audit"
TOOL_WAYPOINT_DISCOVER = "waypoint_discover"
TOOL_WAYPOINT_DOCTOR = "waypoint_doctor"


def initialize(_params: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "protocolVersion": PROTOCOL_VERSION,
        "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "capabilities": {"tools": {}},
    }


def tools_list(_params: Mapping[str, Any]) -> dict[str, Any]:
    repo_root_schema = {
        "type": "string",
        "description": "Repository root to inspect. Defaults to the MCP server current working directory.",
    }
    return {
        "tools": [
            {
                "name": TOOL_WAYPOINT_DISCOVER,
                "description": (
                    "Scan a repository for routers, docs, Waypoint config, and likely document roles. "
                    "This tool is read-only."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "repo_root": repo_root_schema,
                        "max_files": {
                            "type": "integer",
                            "minimum": 20,
                            "maximum": 5000,
                            "description": "Maximum candidate docs to inspect. Defaults to 500.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_WAYPOINT_AUDIT,
                "description": (
                    "Audit Waypoint-style documentation for bloat, SSOT drift, role mixing, "
                    "stale work signals, and decision-consolidation candidates. This tool is read-only."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "repo_root": repo_root_schema,
                        "max_files": {
                            "type": "integer",
                            "minimum": 20,
                            "maximum": 5000,
                            "description": "Maximum candidate docs to inspect. Defaults to 500.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_WAYPOINT_DOCTOR,
                "description": (
                    "Validate Waypoint docs-harness health: configured document homes, marker blocks, "
                    "AGENTS routing, wrapper delegation, and broken local Markdown links. This tool is read-only."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "repo_root": repo_root_schema,
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        ]
    }


def tools_call(params: Mapping[str, Any]) -> dict[str, Any]:
    name = params.get("name")
    arguments = params.get("arguments", {})
    if arguments is None:
        arguments = {}
    if not isinstance(arguments, dict):
        raise JsonRpcError(TOOL_ERROR, "Tool arguments must be an object")

    try:
        result = call_tool(name, arguments)
    except JsonRpcError:
        raise
    except WaypointInspectError as exc:
        raise JsonRpcError(TOOL_ERROR, "Waypoint inspection error", {"error": str(exc)}) from exc
    except Exception as exc:
        raise JsonRpcError(TOOL_ERROR, "Tool error", {"error": str(exc)}) from exc

    return {
        "content": [{"type": "text", "text": format_tool_result(name, result)}],
        "structuredContent": result,
    }


def call_tool(name: Any, arguments: Mapping[str, Any]) -> dict[str, Any]:
    if name == TOOL_WAYPOINT_DISCOVER:
        repo_root = arguments.get("repo_root")
        max_files = arguments.get("max_files", 500)
        if not isinstance(max_files, int):
            raise JsonRpcError(TOOL_ERROR, "max_files must be an integer")
        return discover_repo(repo_root, max_files=max_files)
    if name == TOOL_WAYPOINT_AUDIT:
        repo_root = arguments.get("repo_root")
        max_files = arguments.get("max_files", 500)
        if not isinstance(max_files, int):
            raise JsonRpcError(TOOL_ERROR, "max_files must be an integer")
        return audit_repo(repo_root, max_files=max_files)
    if name == TOOL_WAYPOINT_DOCTOR:
        return doctor_repo(arguments.get("repo_root"))
    raise JsonRpcError(TOOL_ERROR, f"Unknown tool: {name}")


def format_tool_result(name: Any, result: Mapping[str, Any]) -> str:
    if name == TOOL_WAYPOINT_DISCOVER:
        summary = result["summary"]
        return "\n".join(
            [
                f"Waypoint discover: repo={Path(result['repo_root']).name}",
                f"routers={summary['router_count']} documents={summary['document_count']}",
                f"has_agents={summary['has_agents']} has_docs_dir={summary['has_docs_dir']}",
                f"has_waypoint_config={summary['has_waypoint_config']}",
            ]
        )
    if name == TOOL_WAYPOINT_DOCTOR:
        counts = result["counts"]
        return "\n".join(
            [
                f"Waypoint doctor: status={result['status']}",
                f"pass={counts['pass']} warn={counts['warn']} fail={counts['fail']}",
            ]
        )
    if name == TOOL_WAYPOINT_AUDIT:
        summary = result["summary"]
        counts = summary["severity_counts"]
        return "\n".join(
            [
                f"Waypoint audit: status={result['status']}",
                f"documents={summary['document_count']} findings={summary['finding_count']}",
                f"high={counts['high']} medium={counts['medium']} low={counts['low']}",
            ]
        )
    return json.dumps(result, ensure_ascii=False, indent=2)


def build_protocol() -> JsonRpcProtocol:
    return JsonRpcProtocol(
        {
            "initialize": initialize,
            "tools/list": tools_list,
            "tools/call": tools_call,
        }
    )


def main() -> int:
    protocol = build_protocol()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        response = protocol.handle_line(line)
        if response is not None:
            sys.stdout.write(response + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
