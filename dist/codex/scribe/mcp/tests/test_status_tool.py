import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MCP_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_DIR))

import server  # noqa: E402


class ScribeStatusToolTest(unittest.TestCase):
    def request(self, method, params=None, request_id=1):
        protocol = server.build_protocol()
        payload = {"jsonrpc": "2.0", "id": request_id, "method": method}
        if params is not None:
            payload["params"] = params
        response = protocol.handle_line(json.dumps(payload))
        self.assertIsNotNone(response)
        return json.loads(response)

    def test_initialize_response(self):
        response = self.request("initialize", {"protocolVersion": server.PROTOCOL_VERSION})

        self.assertEqual(response["jsonrpc"], "2.0")
        self.assertEqual(response["id"], 1)
        result = response["result"]
        self.assertEqual(result["protocolVersion"], server.PROTOCOL_VERSION)
        self.assertEqual(result["serverInfo"]["name"], "scribe")
        self.assertEqual(result["serverInfo"]["version"], server.SERVER_VERSION)
        self.assertIn("tools", result["capabilities"])

    def test_tools_list_includes_status_tool(self):
        response = self.request("tools/list")

        tools = response["result"]["tools"]
        by_name = {tool["name"]: tool for tool in tools}
        self.assertIn(server.TOOL_SCRIBE_STT_STATUS, by_name)
        self.assertIn(server.TOOL_SCRIBE_SETUP_STT, by_name)
        schema = by_name[server.TOOL_SCRIBE_STT_STATUS]["inputSchema"]
        self.assertEqual(schema["type"], "object")
        self.assertEqual(schema["properties"], {})
        self.assertEqual(schema["required"], [])
        self.assertFalse(schema["additionalProperties"])

        setup_schema = by_name[server.TOOL_SCRIBE_SETUP_STT]["inputSchema"]
        self.assertEqual(setup_schema["type"], "object")
        self.assertIn("install", setup_schema["properties"])
        self.assertIn("upgrade", setup_schema["properties"])
        self.assertIn("timeout_seconds", setup_schema["properties"])
        self.assertEqual(setup_schema["required"], [])
        self.assertFalse(setup_schema["additionalProperties"])

    def test_status_tool_reports_available_dependencies(self):
        spec = SimpleNamespace(origin="/venv/lib/python/site-packages/faster_whisper/__init__.py")

        with (
            patch("server.importlib.util.find_spec", return_value=spec),
            patch("server.shutil.which", return_value="/usr/local/bin/ffmpeg"),
        ):
            response = self.request(
                "tools/call",
                {"name": server.TOOL_SCRIBE_STT_STATUS, "arguments": {}},
            )

        result = response["result"]
        structured = result["structuredContent"]
        self.assertTrue(structured["stt_ready"])
        self.assertTrue(structured["dependencies"]["faster_whisper"]["available"])
        self.assertEqual(structured["dependencies"]["faster_whisper"]["origin"], spec.origin)
        self.assertTrue(structured["dependencies"]["ffmpeg"]["available"])
        self.assertEqual(structured["dependencies"]["ffmpeg"]["path"], "/usr/local/bin/ffmpeg")
        self.assertEqual(structured["python"]["executable"], sys.executable)
        self.assertEqual(structured["install_guidance"][0]["dependency"], "all")

        text = result["content"][0]["text"]
        self.assertIn("faster-whisper: available=True", text)
        self.assertIn("ffmpeg: available=True", text)

    def test_status_tool_reports_missing_dependencies_without_importing_them(self):
        with (
            patch("server.importlib.util.find_spec", return_value=None) as find_spec,
            patch("server.shutil.which", return_value=None),
        ):
            response = self.request(
                "tools/call",
                {"name": server.TOOL_SCRIBE_STT_STATUS, "arguments": {}},
            )

        find_spec.assert_called_once_with("faster_whisper")
        structured = response["result"]["structuredContent"]
        self.assertFalse(structured["stt_ready"])
        self.assertFalse(structured["dependencies"]["faster_whisper"]["available"])
        self.assertFalse(structured["dependencies"]["ffmpeg"]["available"])

        guidance = structured["install_guidance"]
        self.assertEqual(
            {item["dependency"] for item in guidance},
            {"faster-whisper", "ffmpeg"},
        )
        self.assertIn("python3 -m pip install faster-whisper", guidance[0]["command"])
        self.assertIn("brew install ffmpeg", guidance[1]["command"])

    def test_setup_tool_dry_run_reports_install_command(self):
        with (
            patch("server.importlib.util.find_spec", return_value=None),
            patch("server.shutil.which", return_value="/usr/local/bin/ffmpeg"),
            patch("server.subprocess.run") as run,
        ):
            response = self.request(
                "tools/call",
                {"name": server.TOOL_SCRIBE_SETUP_STT, "arguments": {}},
            )

        run.assert_not_called()
        structured = response["result"]["structuredContent"]
        self.assertFalse(structured["install_requested"])
        self.assertFalse(structured["setup_ready"])
        self.assertFalse(structured["success"])
        self.assertEqual(structured["actions"][0]["dependency"], "faster-whisper")
        self.assertEqual(structured["actions"][0]["status"], "skipped")
        self.assertIn("install=false", structured["actions"][0]["reason"])
        self.assertIn("pip install faster-whisper", structured["actions"][0]["command"])
        self.assertEqual(structured["actions"][1]["dependency"], "ffmpeg")
        self.assertEqual(structured["actions"][1]["status"], "already_available")

    def test_setup_tool_installs_missing_python_dependency(self):
        missing_spec = None
        present_spec = SimpleNamespace(origin="/venv/lib/python/site-packages/faster_whisper/__init__.py")
        completed = SimpleNamespace(returncode=0, stdout="installed", stderr="")

        with (
            patch("server.importlib.util.find_spec", side_effect=[missing_spec, present_spec]),
            patch("server.shutil.which", return_value="/usr/local/bin/ffmpeg"),
            patch("server.subprocess.run", return_value=completed) as run,
        ):
            response = self.request(
                "tools/call",
                {
                    "name": server.TOOL_SCRIBE_SETUP_STT,
                    "arguments": {"install": True, "upgrade": True, "timeout_seconds": 60},
                },
            )

        run.assert_called_once_with(
            [sys.executable, "-m", "pip", "install", "--upgrade", "faster-whisper"],
            check=False,
            capture_output=True,
            text=True,
            timeout=60,
        )
        structured = response["result"]["structuredContent"]
        self.assertTrue(structured["install_requested"])
        self.assertTrue(structured["upgrade_requested"])
        self.assertTrue(structured["setup_ready"])
        self.assertTrue(structured["success"])
        self.assertEqual(structured["actions"][0]["dependency"], "faster-whisper")
        self.assertEqual(structured["actions"][0]["status"], "installed")
        self.assertEqual(structured["actions"][0]["returncode"], 0)
        self.assertEqual(structured["after"]["dependencies"]["faster_whisper"]["origin"], present_spec.origin)

        text = response["result"]["content"][0]["text"]
        self.assertIn("Scribe STT setup", text)
        self.assertIn("faster-whisper: installed", text)

    def test_setup_tool_reports_pip_failure_without_json_rpc_error(self):
        completed = SimpleNamespace(returncode=1, stdout="", stderr="network unavailable")

        with (
            patch("server.importlib.util.find_spec", return_value=None),
            patch("server.shutil.which", return_value="/usr/local/bin/ffmpeg"),
            patch("server.subprocess.run", return_value=completed),
        ):
            response = self.request(
                "tools/call",
                {"name": server.TOOL_SCRIBE_SETUP_STT, "arguments": {"install": True}},
            )

        self.assertNotIn("error", response)
        structured = response["result"]["structuredContent"]
        self.assertFalse(structured["setup_ready"])
        self.assertFalse(structured["success"])
        self.assertEqual(structured["actions"][0]["status"], "failed")
        self.assertEqual(structured["actions"][0]["stderr"], "network unavailable")

    def test_setup_tool_rejects_non_boolean_install(self):
        response = self.request(
            "tools/call",
            {"name": server.TOOL_SCRIBE_SETUP_STT, "arguments": {"install": "yes"}},
        )

        self.assertEqual(response["error"]["code"], server.TOOL_ERROR)
        self.assertEqual(response["error"]["data"]["field"], "install")
        self.assertIn("boolean", response["error"]["data"]["error"])

    def test_unknown_tool_returns_json_rpc_tool_error(self):
        response = self.request(
            "tools/call",
            {"name": "scribe_no_such_tool", "arguments": {}},
        )

        self.assertEqual(response["error"]["code"], server.TOOL_ERROR)
        self.assertIn("Unknown tool", response["error"]["message"])

    def test_non_object_arguments_return_tool_error(self):
        response = self.request(
            "tools/call",
            {"name": server.TOOL_SCRIBE_STT_STATUS, "arguments": []},
        )

        self.assertEqual(response["error"]["code"], server.TOOL_ERROR)
        self.assertIn("Tool arguments must be an object", response["error"]["message"])


if __name__ == "__main__":
    unittest.main()
