"""Slack crawler configuration - independent of analysis/LLM settings."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv


UNEXPANDED_ENV_PLACEHOLDER_RE = re.compile(r"\$\{[A-Za-z_][A-Za-z0-9_]*\}")
DEFAULT_CONFIG_PATHS = (
    Path("~/.slackbox/config.env"),
    Path("~/.config/slackbox/config.env"),
)
DEFAULT_DATA_DIR = Path("~/.slackbox/data")


def has_unexpanded_env_placeholder(value: object) -> bool:
    return bool(UNEXPANDED_ENV_PLACEHOLDER_RE.search(str(value)))


def _expand_path(value: str | Path) -> Path:
    return Path(os.path.expandvars(str(value))).expanduser()


def default_config_paths() -> list[Path]:
    paths: list[Path] = []
    explicit_path = os.getenv("SLACKBOX_CONFIG", "")
    if explicit_path:
        paths.append(_expand_path(explicit_path))
    paths.extend(_expand_path(path) for path in DEFAULT_CONFIG_PATHS)
    return paths


def load_slackbox_env(env_path: Path | None = None) -> list[Path]:
    if env_path is not None:
        candidates = [_expand_path(env_path)]
    else:
        candidates = [*default_config_paths(), Path.cwd() / ".env"]

    loaded: list[Path] = []
    for candidate in candidates:
        if candidate.is_file():
            load_dotenv(candidate, override=False)
            loaded.append(candidate)
    return loaded


@dataclass
class CrawlerConfig:
    """Slack crawling configuration only. Analysis/LLM settings are excluded."""

    slack_user_token: str = ""
    target_user_ids: list[str] = field(default_factory=list)
    timezone: str = "Asia/Seoul"
    page_limit: int = 200
    base_delay: float = 1.2
    data_dir: Path = field(default_factory=lambda: _expand_path(DEFAULT_DATA_DIR))
    config_sources: list[Path] = field(default_factory=list)

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
        config_sources = load_slackbox_env(env_path)
        raw_ids = os.getenv("TARGET_USER_IDS", os.getenv("TARGET_USER_ID", ""))
        user_ids = [uid.strip() for uid in raw_ids.split(",") if uid.strip()]
        data_dir_value = (
            _expand_path(data_dir)
            if data_dir is not None
            else _expand_path(os.getenv("SLACK_FETCH_DATA_DIR", str(DEFAULT_DATA_DIR)))
        )
        return cls(
            slack_user_token=os.getenv("SLACK_USER_TOKEN", ""),
            target_user_ids=user_ids,
            timezone=os.getenv("TIMEZONE", "Asia/Seoul"),
            data_dir=data_dir_value,
            config_sources=config_sources,
        )

    def validate(self) -> list[str]:
        errors = []
        if not self.slack_user_token:
            errors.append("SLACK_USER_TOKEN is missing.")
        elif has_unexpanded_env_placeholder(self.slack_user_token):
            errors.append(
                "SLACK_USER_TOKEN contains an unexpanded ${VAR} placeholder; "
                "use Codex env_vars or Claude sensitive config."
            )
        elif not self.slack_user_token.startswith("xoxp-"):
            errors.append("SLACK_USER_TOKEN is missing or does not start with xoxp-.")
        errors.extend(self.validate_data_dir())
        return errors

    def validate_data_dir(self) -> list[str]:
        errors = []
        if has_unexpanded_env_placeholder(self.data_dir):
            errors.append(
                "SLACK_FETCH_DATA_DIR contains an unexpanded ${VAR} placeholder; "
                "set a literal path or forward the parent environment variable."
            )
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
