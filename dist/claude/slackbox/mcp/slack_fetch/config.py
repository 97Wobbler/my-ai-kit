"""Slack crawler configuration - independent of analysis/LLM settings."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv


@dataclass
class CrawlerConfig:
    """Slack crawling configuration only. Analysis/LLM settings are excluded."""

    slack_user_token: str = ""
    target_user_ids: list[str] = field(default_factory=list)
    timezone: str = "Asia/Seoul"
    page_limit: int = 200
    base_delay: float = 1.2
    data_dir: Path = field(default_factory=lambda: Path("data"))

    @property
    def target_user_id(self) -> str:
        return self.target_user_ids[0] if self.target_user_ids else ""

    @property
    def all_user_ids_set(self) -> set[str]:
        return set(self.target_user_ids)

    @property
    def raw_dir(self) -> Path:
        return self.data_dir / "raw"

    @property
    def cleaned_dir(self) -> Path:
        return self.data_dir / "cleaned"

    def user_raw_dir(self, user_id: str) -> Path:
        return self.raw_dir / user_id

    def user_messages_path(self, user_id: str) -> Path:
        return self.raw_dir / user_id / "messages.jsonl"

    @property
    def shared_threads_dir(self) -> Path:
        return self.raw_dir / "threads"

    def channels_path(self) -> Path:
        return self.raw_dir / "channels.json"

    def channel_dir(self, channel_id: str) -> Path:
        return self.raw_dir / "channels" / channel_id

    def channel_messages_path(self, channel_id: str) -> Path:
        return self.channel_dir(channel_id) / "messages.jsonl"

    @classmethod
    def from_env(cls, env_path: Path | None = None, data_dir: Path | None = None) -> "CrawlerConfig":
        load_dotenv(env_path or Path.cwd() / ".env")
        raw_ids = os.getenv("TARGET_USER_IDS", os.getenv("TARGET_USER_ID", ""))
        user_ids = [uid.strip() for uid in raw_ids.split(",") if uid.strip()]
        return cls(
            slack_user_token=os.getenv("SLACK_USER_TOKEN", ""),
            target_user_ids=user_ids,
            timezone=os.getenv("TIMEZONE", "Asia/Seoul"),
            data_dir=data_dir or Path(os.getenv("SLACK_FETCH_DATA_DIR", "data")),
        )

    def validate(self) -> list[str]:
        errors = []
        if not self.slack_user_token.startswith("xoxp-"):
            errors.append("SLACK_USER_TOKEN is missing or does not start with xoxp-.")
        return errors

    def ensure_dirs(self) -> None:
        dirs = [
            self.raw_dir,
            self.raw_dir / "channels",
            self.shared_threads_dir,
            self.cleaned_dir,
        ]
        for uid in self.target_user_ids:
            dirs.append(self.user_raw_dir(uid))
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
