"""Markdown 캐시 — 채널×주 단위로 .md 파일 생성/무효화."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from slack_fetch.config import CrawlerConfig
from slack_fetch.data_loader import _load_all_messages
from slack_fetch.formatting import format_channel_week_md
from slack_fetch.text_cleaner import SlackTextCleaner, ts_to_dt


def sanitize_dirname(channel_id: str, channel_name: str) -> str:
    """채널 ID + 이름으로 안전한 디렉토리명 생성."""
    safe_name = re.sub(r"[^\w가-힣-]", "_", channel_name)
    if not channel_id:
        return safe_name
    return f"{channel_id}_{safe_name}"


def get_source_mtime(cfg: CrawlerConfig) -> float:
    """raw_dir 하위 모든 *.jsonl + channels.json 중 가장 최근 mtime 반환."""
    latest = 0.0
    if not cfg.raw_dir.exists():
        return latest

    for p in cfg.raw_dir.rglob("*.jsonl"):
        latest = max(latest, p.stat().st_mtime)

    channels_json = cfg.channels_path()
    if channels_json.exists():
        latest = max(latest, channels_json.stat().st_mtime)

    return latest


def build_md_cache(cfg: CrawlerConfig, cleaner: SlackTextCleaner, tz: str) -> dict:
    """전체 메시지를 (channel_name, week_key) 단위로 .md 파일 생성/캐싱."""
    all_messages, _ = _load_all_messages(cfg)

    # (channel_name, channel_id, week_key) -> messages
    groups: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for msg in all_messages:
        channel_name = msg.get("channel_name", "unknown")
        channel_id = msg.get("channel_id", "")
        dt = ts_to_dt(msg["ts"], tz)
        iso = dt.isocalendar()
        week_key = f"{iso[0]}-W{iso[1]:02d}"
        groups[(channel_name, channel_id, week_key)].append(msg)

    source_mtime = get_source_mtime(cfg)

    generated = 0
    skipped = 0

    for (channel_name, channel_id, week_key), msgs in groups.items():
        dirname = sanitize_dirname(channel_id, channel_name)
        target_path = cfg.cleaned_dir / dirname / f"{week_key}.md"

        if target_path.exists() and target_path.stat().st_mtime >= source_mtime:
            skipped += 1
            continue

        md_content = format_channel_week_md(msgs, channel_name, week_key, cleaner, tz)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(md_content, encoding="utf-8")
        generated += 1

    total_files = generated + skipped
    return {"generated": generated, "skipped": skipped, "total_files": total_files}


def list_cached_md(cfg: CrawlerConfig) -> list[dict]:
    """cleaned_dir 하위의 모든 **/*.md 파일 스캔."""
    results: list[dict] = []
    if not cfg.cleaned_dir.exists():
        return results

    for md_path in cfg.cleaned_dir.rglob("*.md"):
        results.append(
            {
                "channel": md_path.parent.name,
                "week": md_path.stem,
                "path": str(md_path),
                "size_kb": round(md_path.stat().st_size / 1024, 1),
            }
        )

    results.sort(key=lambda x: x["path"])
    return results
