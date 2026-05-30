"""Slack 텍스트 정제 및 타임스탬프 유틸리티."""

from __future__ import annotations

import importlib
import json
import re
import subprocess
import sys
import zoneinfo
from datetime import datetime
from zoneinfo import ZoneInfo

from slack_fetch.config import CrawlerConfig

# Windows에서 tzdata 없이 ZoneInfo 실패하는 경우 자동 설치
try:
    ZoneInfo("Asia/Seoul")
except KeyError:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--quiet", "--force-reinstall", "tzdata"],
    )
    # 재로드: importlib로 zoneinfo 캐시 초기화
    importlib.reload(zoneinfo)
    from zoneinfo import ZoneInfo  # noqa: F811


class SlackTextCleaner:
    """Slack mrkdwn -> 읽기 쉬운 plaintext 변환."""

    def __init__(
        self,
        user_map: dict[str, str] | None = None,
        channel_map: dict[str, str] | None = None,
    ):
        self.user_map = user_map or {}
        self.channel_map = channel_map or {}

    def clean(self, text: str) -> str:
        text = self._replace_user_mentions(text)
        text = self._replace_channel_mentions(text)
        text = self._replace_links(text)
        text = self._strip_emojis(text)
        text = self._strip_formatting(text)
        return text.strip()

    def _replace_user_mentions(self, text: str) -> str:
        def _repl(m):
            uid = m.group(1)
            return f"@{self.user_map.get(uid, uid)}"

        return re.sub(r"<@(U[A-Z0-9]+)>", _repl, text)

    def _replace_channel_mentions(self, text: str) -> str:
        return re.sub(
            r"<#(C[A-Z0-9]+)(?:\|([^>]+))?>",
            lambda m: f"#{m.group(2) or self.channel_map.get(m.group(1), m.group(1))}",
            text,
        )

    def _replace_links(self, text: str) -> str:
        text = re.sub(r"<(https?://[^|>]+)\|([^>]+)>", r"\2", text)
        text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
        return text

    def _strip_emojis(self, text: str) -> str:
        return re.sub(r":([a-zA-Z0-9_+-]+):", r"[\1]", text)

    def _strip_formatting(self, text: str) -> str:
        text = re.sub(r"\*([^*]+)\*", r"\1", text)
        text = re.sub(r"_([^_]+)_", r"\1", text)
        text = re.sub(r"~([^~]+)~", r"\1", text)
        return text


def ts_to_dt(ts: str, tz_name: str = "Asia/Seoul") -> datetime:
    return datetime.fromtimestamp(float(ts), tz=ZoneInfo(tz_name))


def ts_to_str(ts: str, tz_name: str = "Asia/Seoul", fmt: str = "%Y-%m-%d %H:%M") -> str:
    return ts_to_dt(ts, tz_name).strftime(fmt)


def load_user_map_from_threads(cfg: CrawlerConfig) -> dict[str, str]:
    """공유 스레드 디렉토리의 JSONL에서 user_id -> user_name 매핑 추출."""
    user_map: dict[str, str] = {}
    threads_dir = cfg.shared_threads_dir
    if not threads_dir.exists():
        return user_map
    for fp in threads_dir.glob("*.jsonl"):
        with open(fp, encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                if rec.get("user") and rec.get("user_name"):
                    user_map[rec["user"]] = rec["user_name"]
    return user_map


def load_channel_map(cfg: CrawlerConfig) -> dict[str, str]:
    channels_path = cfg.channels_path()
    if not channels_path.exists():
        return {}
    data = json.loads(channels_path.read_text(encoding="utf-8"))
    return {ch["id"]: ch["name"] for ch in data.get("channels", [])}
