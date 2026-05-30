"""채널 목록 수집."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from slack_fetch.config import CrawlerConfig

logger = logging.getLogger(__name__)


def collect_channels(
    client: WebClient,
    cfg: CrawlerConfig,
    *,
    include_archived: bool = False,
    channel_types: str = "public_channel",
) -> list[dict]:
    """채널 목록을 수집하고 channels.json에 저장.

    Args:
        channel_types: conversations.list에 전달할 types 값.
            예: "public_channel", "public_channel,private_channel",
            "public_channel,private_channel,im,mpim"
    """
    channels: list[dict] = []
    cursor = None

    while True:
        try:
            resp = client.conversations_list(
                types=channel_types,
                limit=cfg.page_limit,
                exclude_archived=not include_archived,
                cursor=cursor or "",
            )
        except SlackApiError as e:
            logger.error("conversations_list 실패: %s", e.response["error"])
            raise

        for ch in resp["channels"]:
            is_im = ch.get("is_im", False)
            is_mpim = ch.get("is_mpim", False)
            # 일반 채널은 is_member 확인, DM/그룹DM은 항상 포함
            if not (is_im or is_mpim) and not ch.get("is_member"):
                continue
            channels.append({
                "id": ch["id"],
                "name": ch.get("name") or ch.get("user", ch["id"]),
                "purpose": (ch.get("purpose") or {}).get("value", ""),
                "topic": (ch.get("topic") or {}).get("value", ""),
                "num_members": ch.get("num_members", 0),
                "is_archived": ch.get("is_archived", False),
                "is_im": is_im,
                "is_mpim": is_mpim,
            })

        cursor = resp.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break

    out = {
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "user_id": cfg.target_user_id,
        "total": len(channels),
        "channels": channels,
    }
    out_path = cfg.channels_path()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info("채널 %d개 수집 -> %s", len(channels), out_path)
    return channels
