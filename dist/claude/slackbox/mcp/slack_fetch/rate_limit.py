"""Rate limit 감지 및 대기 유틸리티."""

from __future__ import annotations

import logging
import time

from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)


def detect_tier(resp_headers: dict) -> tuple[int, float]:
    """응답 헤더에서 rate limit tier를 감지하고 (page_limit, delay) 반환."""
    limit_per_min = int(resp_headers.get("X-RateLimit-Limit", "1"))
    if limit_per_min >= 20:
        return 200, 1.2  # Tier 3
    return 15, 6.0  # Tier 1


def rate_wait(delay: float) -> None:
    time.sleep(delay)


def handle_rate_limit(e: SlackApiError) -> None:
    retry_after = int(e.response.headers.get("Retry-After", 30))
    logger.warning("Rate limited. %d초 대기...", retry_after)
    time.sleep(retry_after)
