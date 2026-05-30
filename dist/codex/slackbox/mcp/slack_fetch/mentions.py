"""타인 언급 수집: 다른 사람이 대상 사용자를 멘션한 메시지를 수집."""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from slack_fetch.config import CrawlerConfig
from slack_fetch.rate_limit import handle_rate_limit
from slack_fetch.utils import checkpoint_load, checkpoint_save

logger = logging.getLogger(__name__)


def _mentions_path(cfg: CrawlerConfig, user_id: str) -> Path:
    return cfg.user_raw_dir(user_id) / "mentions.jsonl"


def _checkpoint_path(cfg: CrawlerConfig, user_id: str) -> Path:
    return cfg.user_raw_dir(user_id) / ".mention_checkpoint.json"


def _load_checkpoint(cfg: CrawlerConfig, user_id: str) -> dict:
    return checkpoint_load(_checkpoint_path(cfg, user_id))


def _save_checkpoint(cfg: CrawlerConfig, user_id: str, data: dict) -> None:
    checkpoint_save(_checkpoint_path(cfg, user_id), data)


def collect_mentions(client: WebClient, cfg: CrawlerConfig,
                     *, since: str | None = None, until: str | None = None,
                     user_id: str | None = None) -> int:
    """다른 사람이 대상 사용자를 멘션한 메시지를 수집한다."""
    uid = user_id or cfg.target_user_id
    out_path = _mentions_path(cfg, uid)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    query = f"<@{uid}> -from:<@{uid}>"
    if since:
        query += f" after:{since}"
    if until:
        query += f" before:{until}"

    seen_ts: set[str] = set()
    if out_path.exists():
        with open(out_path, encoding="utf-8") as ef:
            for line in ef:
                if line.strip():
                    rec = json.loads(line)
                    seen_ts.add(f"{rec['ts']}_{rec.get('channel_id', '')}")

    total = 0
    page = 1

    with open(out_path, "a", encoding="utf-8") as f:
        while True:
            try:
                resp = client.search_messages(
                    query=query, sort="timestamp",
                    sort_dir="asc", count=100, page=page
                )
            except SlackApiError as e:
                if e.response.status_code == 429:
                    handle_rate_limit(e)
                    continue
                raise

            messages = resp.get("messages", {}).get("matches", [])
            if not messages:
                break

            for msg in messages:
                ts = msg.get("ts", "")
                channel_id = msg.get("channel", {}).get("id", "")
                dedup_key = f"{ts}_{channel_id}"

                if dedup_key in seen_ts:
                    continue
                seen_ts.add(dedup_key)

                sender = msg.get("user") or msg.get("username", "")
                if sender == uid:
                    continue

                record = {
                    "ts": ts,
                    "channel_id": channel_id,
                    "channel_name": msg.get("channel", {}).get("name", ""),
                    "user": sender,
                    "text": msg.get("text", ""),
                    "thread_ts": msg.get("thread_ts"),
                    "permalink": msg.get("permalink", ""),
                    "mention_type": "direct_mention",
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                total += 1

            paging = resp.get("messages", {}).get("paging", {})
            if page >= paging.get("pages", 1):
                break
            page += 1
            time.sleep(1.0)

    _save_checkpoint(cfg, uid, {"phase": "mentions_done", "total_mentions": total})
    logger.info("[%s] 타인 언급 %d건 수집 완료", uid, total)
    return total


def collect_mention_threads(client: WebClient, cfg: CrawlerConfig,
                            *, user_id: str | None = None) -> int:
    """수집된 멘션의 스레드 맥락을 수집한다."""
    uid = user_id or cfg.target_user_id
    mentions_file = _mentions_path(cfg, uid)
    if not mentions_file.exists():
        logger.warning("[%s] mentions.jsonl이 없습니다. 먼저 mentions를 실행하세요.", uid)
        return 0

    threads_dir = cfg.user_raw_dir(uid) / "mention_threads"
    threads_dir.mkdir(parents=True, exist_ok=True)

    done_threads: set[str] = set()
    ckpt = _load_checkpoint(cfg, uid)
    if ckpt.get("phase") == "mention_threads":
        done_threads = set(ckpt.get("done_threads", []))

    thread_keys: dict[str, str] = {}
    with open(mentions_file, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            tts = rec.get("thread_ts")
            if not tts:
                continue
            key = f"{rec['channel_id']}|{tts}"
            if key not in done_threads:
                thread_keys[key] = rec.get("channel_name", "")

    logger.info("[%s] 멘션 스레드 %d개 수집 대상 (%d개 완료됨)",
                uid, len(thread_keys), len(done_threads))

    collected = 0
    for key, ch_name in thread_keys.items():
        channel_id, thread_ts = key.split("|", 1)
        out_file = threads_dir / f"{channel_id}_{thread_ts}.jsonl"

        if out_file.exists():
            done_threads.add(key)
            continue

        try:
            replies = []
            cursor = None
            while True:
                kwargs = {"channel": channel_id, "ts": thread_ts, "limit": 200}
                if cursor:
                    kwargs["cursor"] = cursor
                resp = client.conversations_replies(**kwargs)
                replies.extend(resp.get("messages", []))
                cursor = resp.get("response_metadata", {}).get("next_cursor")
                if not cursor:
                    break
                time.sleep(1.0)

            with open(out_file, "w", encoding="utf-8") as tf:
                for r in replies:
                    tf.write(json.dumps({
                        "ts": r.get("ts", ""),
                        "user": r.get("user", ""),
                        "text": r.get("text", ""),
                        "thread_ts": thread_ts,
                        "channel_id": channel_id,
                        "channel_name": ch_name,
                    }, ensure_ascii=False) + "\n")

            collected += 1
            done_threads.add(key)

        except SlackApiError as e:
            if e.response.status_code == 429:
                handle_rate_limit(e)
                continue
            if e.response.get("error") in ("channel_not_found", "thread_not_found", "not_in_channel"):
                logger.warning("스레드 접근 불가: %s/%s (%s)", channel_id, thread_ts, e.response["error"])
                done_threads.add(key)
                continue
            raise

        if collected % 10 == 0:
            _save_checkpoint(cfg, uid, {
                "phase": "mention_threads",
                "done_threads": list(done_threads),
                "collected": collected,
            })
        time.sleep(1.2)

    _save_checkpoint(cfg, uid, {
        "phase": "mention_threads_done",
        "done_threads": list(done_threads),
        "collected": collected,
    })
    logger.info("[%s] 멘션 스레드 %d개 수집 완료", uid, collected)
    return collected
