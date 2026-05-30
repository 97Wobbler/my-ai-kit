"""데이터 로드 유틸리티.

channels.json, messages.jsonl 등 로컬 수집 데이터를 로드하는 함수 모음.
"""

from __future__ import annotations

import json
import logging

from slack_fetch.config import CrawlerConfig
from slack_fetch.utils import safe_json_loads

logger = logging.getLogger(__name__)


def _load_channels(cfg: CrawlerConfig) -> list[dict]:
    """channels.json에서 채널 목록 로드."""
    cp = cfg.channels_path()
    if not cp.exists():
        return []
    data = json.loads(cp.read_text(encoding="utf-8"))
    return data.get("channels", [])


def _load_all_messages(cfg: CrawlerConfig) -> tuple[list[dict], dict[str, int]]:
    """3가지 소스에서 메시지를 로드하고 ts+channel_id 기반 dedup.

    Returns:
        (deduplicated messages list, source counts dict)
    """
    seen: set[str] = set()  # "ts_channel_id"
    all_messages: list[dict] = []
    source_counts = {"user": 0, "channel": 0, "search": 0}

    def _add(msg: dict, source: str) -> None:
        ts = msg.get("ts", "")
        ch_id = msg.get("channel_id", "")
        dedup_key = f"{ts}_{ch_id}"
        if dedup_key in seen:
            return
        seen.add(dedup_key)
        all_messages.append(msg)
        source_counts[source] += 1

    # 1) 사용자별 messages.jsonl — 디렉토리 자동 탐색
    #    U로 시작하는 디렉토리를 모두 스캔 (cfg.target_user_ids에 의존하지 않음)
    if cfg.raw_dir.exists():
        for user_dir in sorted(cfg.raw_dir.iterdir()):
            if not user_dir.is_dir() or not user_dir.name.startswith("U"):
                continue
            mp = user_dir / "messages.jsonl"
            if not mp.exists():
                continue
            with open(mp, encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        msg = safe_json_loads(line, mp)
                        if msg is not None:
                            _add(msg, "user")

    # 2) 채널 전체 대화: data/raw/channels/*/messages.jsonl
    channels_dir = cfg.raw_dir / "channels"
    if channels_dir.exists():
        for ch_msg_path in sorted(channels_dir.glob("*/messages.jsonl")):
            with open(ch_msg_path, encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        msg = safe_json_loads(line, ch_msg_path)
                        if msg is not None:
                            _add(msg, "channel")

    # 3) 키워드 검색 결과: data/raw/search/*.jsonl
    search_dir = cfg.raw_dir / "search"
    if search_dir.exists():
        for search_path in sorted(search_dir.glob("*.jsonl")):
            with open(search_path, encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        msg = safe_json_loads(line, search_path)
                        if msg is not None:
                            _add(msg, "search")

    return all_messages, source_counts
