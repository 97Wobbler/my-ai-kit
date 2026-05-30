"""메시지 수집 (search.messages + conversations.history)."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from slack_fetch.config import CrawlerConfig
from slack_fetch.rate_limit import detect_tier, rate_wait, handle_rate_limit
from slack_fetch.utils import checkpoint_load, checkpoint_save

logger = logging.getLogger(__name__)


# -- Checkpoint --

def _checkpoint_path(cfg: CrawlerConfig, user_id: str | None, method: str = "search") -> Path:
    if user_id is None:
        raise ValueError("user_id=None에서는 _checkpoint_path를 직접 호출하지 마세요.")
    filename = f".{method}_checkpoint.json"
    return cfg.user_raw_dir(user_id) / filename


def _channel_checkpoint_path(cfg: CrawlerConfig, channel_id: str) -> Path:
    """user_id=None (채널 전체 수집)일 때 채널 기반 체크포인트 경로."""
    d = cfg.channel_dir(channel_id)
    d.mkdir(parents=True, exist_ok=True)
    return d / ".checkpoint.json"


def _load_checkpoint(cfg: CrawlerConfig, user_id: str, method: str = "search") -> dict:
    return checkpoint_load(_checkpoint_path(cfg, user_id, method))


def _load_channel_checkpoint(cfg: CrawlerConfig, channel_id: str) -> dict:
    return checkpoint_load(_channel_checkpoint_path(cfg, channel_id))


def _save_checkpoint(cfg: CrawlerConfig, user_id: str, data: dict, method: str = "search") -> None:
    checkpoint_save(_checkpoint_path(cfg, user_id, method), data)


def _save_channel_checkpoint(cfg: CrawlerConfig, channel_id: str, data: dict) -> None:
    checkpoint_save(_channel_checkpoint_path(cfg, channel_id), data)


def _extract_thread_ts_from_permalink(permalink: str) -> str | None:
    m = re.search(r"thread_ts=(\d+\.\d+)", permalink)
    return m.group(1) if m else None


# -- search.messages --

def collect_via_search(client: WebClient, cfg: CrawlerConfig,
                       *, since: str | None = None, until: str | None = None,
                       user_id: str | None = None) -> int:
    """search.messages로 대상 사용자의 메시지를 수집. User Token 전용."""
    uid = user_id or cfg.target_user_id
    messages_path = cfg.user_messages_path(uid)
    messages_path.parent.mkdir(parents=True, exist_ok=True)

    query = f"from:<@{uid}>"
    if since:
        query += f" after:{since}"
    if until:
        query += f" before:{until}"

    seen_ts: set[str] = set()
    if messages_path.exists():
        with open(messages_path, encoding="utf-8") as ef:
            for line in ef:
                rec = json.loads(line)
                seen_ts.add(f"{rec['ts']}_{rec.get('channel_id', '')}")

    total = 0
    page = 1

    with open(messages_path, "a", encoding="utf-8") as f:
        while True:
            try:
                resp = client.search_messages(query=query, sort="timestamp",
                                              sort_dir="asc", count=100, page=page)
            except SlackApiError as e:
                if e.response.status_code == 429:
                    handle_rate_limit(e)
                    continue
                raise

            messages = resp.get("messages", {}).get("matches", [])
            if not messages:
                break

            for msg in messages:
                permalink = msg.get("permalink", "")
                thread_ts = msg.get("thread_ts") or _extract_thread_ts_from_permalink(permalink)
                ts = msg.get("ts", "")
                reply_count = msg.get("reply_count", 0)

                if thread_ts and thread_ts == ts and reply_count > 0:
                    msg_type = "thread_parent"
                elif thread_ts and thread_ts != ts:
                    msg_type = "thread_reply"
                elif thread_ts and thread_ts == ts:
                    msg_type = "thread_parent"
                else:
                    msg_type = "message"

                channel_id = msg.get("channel", {}).get("id", "")
                dedup_key = f"{ts}_{channel_id}"
                if dedup_key in seen_ts:
                    continue
                seen_ts.add(dedup_key)

                record = {
                    "ts": ts,
                    "channel_id": channel_id,
                    "channel_name": msg.get("channel", {}).get("name", ""),
                    "text": msg.get("text", ""),
                    "thread_ts": thread_ts,
                    "reply_count": reply_count,
                    "permalink": permalink,
                    "type": msg_type,
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                total += 1

            paging = resp.get("messages", {}).get("paging", {})
            if page >= paging.get("pages", 1):
                break
            page += 1
            rate_wait(1.0)

    _save_checkpoint(cfg, uid, {"phase": "search_done", "total_messages": total}, method="search")
    logger.info("[%s] search.messages로 메시지 %d건 수집 완료", uid, total)
    return total


# -- conversations.history --

def collect_user_history(client: WebClient, cfg: CrawlerConfig, channels: list[dict],
                         *, since: str | None = None, until: str | None = None,
                         user_id: str) -> int:
    """conversations.history로 전체 채널을 순회하며 특정 사용자의 메시지만 수집.

    사용자 필터링, user별 messages.jsonl 저장, user별 체크포인트.
    since/until은 Slack timestamp 문자열(예: "1717000000.000000")이어야 한다.
    """
    uid = user_id or cfg.target_user_id

    delay = cfg.base_delay
    tier_detected = False

    messages_path = cfg.user_messages_path(uid)
    messages_path.parent.mkdir(parents=True, exist_ok=True)
    ckpt = _load_checkpoint(cfg, uid, method="history")
    start_idx = ckpt.get("last_channel_idx", 0) if ckpt.get("phase") == "history" else 0
    user_total = ckpt.get("collected_messages", 0)

    # D2: 기존 파일의 ts를 로드하여 중복 방지
    seen_ts: set[str] = set()
    if messages_path.exists():
        with open(messages_path, encoding="utf-8") as ef:
            for line in ef:
                rec = json.loads(line)
                seen_ts.add(f"{rec['ts']}_{rec.get('channel_id', '')}")

    for i, ch in enumerate(channels):
        if i < start_idx:
            continue
        ch_total = user_total  # 기존 누적 카운터 유지

        cursor = None
        logger.info("[%s] [%d/%d] #%s 수집 중...", uid, i + 1, len(channels), ch["name"])

        with open(messages_path, "a", encoding="utf-8") as f:
            while True:
                try:
                    kwargs = {"channel": ch["id"], "limit": cfg.page_limit}
                    if cursor:
                        kwargs["cursor"] = cursor
                    if since:
                        kwargs["oldest"] = since
                    if until:
                        kwargs["latest"] = until

                    resp = client.conversations_history(**kwargs)

                    if not tier_detected and hasattr(resp, "headers"):
                        cfg.page_limit, delay = detect_tier(resp.headers)
                        tier_detected = True
                        logger.info("Rate limit tier 감지: limit=%d, delay=%.1fs",
                                    cfg.page_limit, delay)

                except SlackApiError as e:
                    if e.response.status_code == 429:
                        handle_rate_limit(e)
                        continue
                    if e.response["error"] == "not_in_channel":
                        logger.warning("#%s: not_in_channel, 건너뜀", ch["name"])
                        break
                    raise

                for msg in resp.get("messages", []):
                    if msg.get("user") != uid:
                        continue
                    if msg.get("subtype") in ("channel_join", "channel_leave", "bot_message"):
                        continue

                    # D2: 중복 메시지 건너뛰기
                    ts = msg.get("ts", "")
                    dedup_key = f"{ts}_{ch['id']}"
                    if dedup_key in seen_ts:
                        continue
                    seen_ts.add(dedup_key)

                    record = {
                        "ts": ts,
                        "user": msg.get("user", ""),
                        "channel_id": ch["id"],
                        "channel_name": ch["name"],
                        "text": msg.get("text", ""),
                        "thread_ts": msg.get("thread_ts"),
                        "reply_count": msg.get("reply_count", 0),
                        "type": "thread_parent" if msg.get("reply_count", 0) > 0 else "message",
                        "files": [fi.get("name", "") for fi in msg.get("files", [])],
                    }
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                    ch_total += 1

                cursor = resp.get("response_metadata", {}).get("next_cursor")
                if not cursor:
                    break
                rate_wait(delay)

        user_total = ch_total
        _save_checkpoint(cfg, uid, {
            "phase": "history",
            "last_channel_idx": i + 1,
            "last_channel_id": ch["id"],
            "collected_messages": user_total,
        }, method="history")

        rate_wait(delay)

    logger.info("[%s] conversations.history로 메시지 %d건 수집 완료", uid, user_total)
    return user_total


def collect_channel_history(client: WebClient, cfg: CrawlerConfig, channels: list[dict],
                            *, since: str | None = None, until: str | None = None) -> int:
    """conversations.history로 전체 채널을 순회하며 모든 메시지를 수집.

    필터 없이 전체 수집, channel별 messages.jsonl 저장, channel별 체크포인트.
    since/until은 Slack timestamp 문자열(예: "1717000000.000000")이어야 한다.
    """
    delay = cfg.base_delay
    tier_detected = False
    grand_total = 0

    for i, ch in enumerate(channels):
        messages_path = cfg.channel_messages_path(ch["id"])
        messages_path.parent.mkdir(parents=True, exist_ok=True)
        ch_ckpt = _load_channel_checkpoint(cfg, ch["id"])

        if ch_ckpt.get("phase") == "history_done":
            prev = ch_ckpt.get("collected_messages", 0)
            grand_total += prev
            logger.info("[channel] #%s 이미 수집 완료 (%d건), 건너뜀", ch["name"], prev)
            continue

        ch_total = ch_ckpt.get("collected_messages", 0)

        # D2: 기존 파일의 ts를 로드하여 중복 방지
        seen_ts: set[str] = set()
        if messages_path.exists():
            with open(messages_path, encoding="utf-8") as ef:
                for line in ef:
                    rec = json.loads(line)
                    seen_ts.add(f"{rec['ts']}_{rec.get('channel_id', '')}")

        cursor = None
        # 커서 기반 이어받기
        ch_ckpt_data = _load_channel_checkpoint(cfg, ch["id"])
        if ch_ckpt_data.get("phase") == "history":
            cursor = ch_ckpt_data.get("next_cursor")
            ch_total = ch_ckpt_data.get("collected_messages", 0)

        logger.info("[channel:%s] [%d/%d] #%s 수집 중...", ch["name"], i + 1, len(channels), ch["name"])

        with open(messages_path, "a", encoding="utf-8") as f:
            while True:
                try:
                    kwargs = {"channel": ch["id"], "limit": cfg.page_limit}
                    if cursor:
                        kwargs["cursor"] = cursor
                    if since:
                        kwargs["oldest"] = since
                    if until:
                        kwargs["latest"] = until

                    resp = client.conversations_history(**kwargs)

                    if not tier_detected and hasattr(resp, "headers"):
                        cfg.page_limit, delay = detect_tier(resp.headers)
                        tier_detected = True
                        logger.info("Rate limit tier 감지: limit=%d, delay=%.1fs",
                                    cfg.page_limit, delay)

                except SlackApiError as e:
                    if e.response.status_code == 429:
                        handle_rate_limit(e)
                        continue
                    if e.response["error"] == "not_in_channel":
                        logger.warning("#%s: not_in_channel, 건너뜀", ch["name"])
                        break
                    raise

                for msg in resp.get("messages", []):
                    if msg.get("subtype") in ("channel_join", "channel_leave", "bot_message"):
                        continue

                    # D2: 중복 메시지 건너뛰기
                    ts = msg.get("ts", "")
                    dedup_key = f"{ts}_{ch['id']}"
                    if dedup_key in seen_ts:
                        continue
                    seen_ts.add(dedup_key)

                    record = {
                        "ts": ts,
                        "user": msg.get("user", ""),
                        "channel_id": ch["id"],
                        "channel_name": ch["name"],
                        "text": msg.get("text", ""),
                        "thread_ts": msg.get("thread_ts"),
                        "reply_count": msg.get("reply_count", 0),
                        "type": "thread_parent" if msg.get("reply_count", 0) > 0 else "message",
                        "files": [fi.get("name", "") for fi in msg.get("files", [])],
                    }
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                    ch_total += 1

                cursor = resp.get("response_metadata", {}).get("next_cursor")
                if not cursor:
                    break
                # 페이지마다 체크포인트 저장 (중단 대비)
                _save_channel_checkpoint(cfg, ch["id"], {
                    "phase": "history",
                    "next_cursor": cursor,
                    "collected_messages": ch_total,
                })
                rate_wait(delay)

        _save_channel_checkpoint(cfg, ch["id"], {
            "phase": "history_done",
            "collected_messages": ch_total,
        })
        grand_total += ch_total

        rate_wait(delay)

    logger.info("[channel-all] conversations.history로 메시지 %d건 수집 완료", grand_total)
    return grand_total


def collect_via_history(client: WebClient, cfg: CrawlerConfig, channels: list[dict],
                        *, since: str | None = None, until: str | None = None,
                        user_id: str | None = None) -> int:
    """conversations.history 래퍼 (하위 호환).

    user_id가 지정되면 collect_user_history, None이면 collect_channel_history로 위임.
    since/until은 conversations.history의 oldest/latest에 전달할 Slack timestamp 문자열이다.
    """
    if user_id is None:
        return collect_channel_history(client, cfg, channels, since=since, until=until)
    return collect_user_history(client, cfg, channels, since=since, until=until, user_id=user_id)
