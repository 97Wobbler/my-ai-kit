"""Slack WebClient factory with SSL configuration."""

from __future__ import annotations

import ssl

import certifi
from slack_sdk import WebClient

from slack_fetch.config import CrawlerConfig


def create_slack_client(cfg: CrawlerConfig) -> WebClient:
    """Create a Slack WebClient with SSL configuration."""
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    return WebClient(token=cfg.slack_user_token, ssl=ssl_context)
