"""Slack Fetch MCP Server.

Claude Code에서 Slack 벌크 크롤링을 수행할 수 있는 MCP 서버.
기존 slack_fetch 함수들을 호출하는 얇은 래퍼.

실행: python -m slack_fetch
"""

from __future__ import annotations

import json
import logging
import importlib.util
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

from mcp.server import FastMCP

from slack_sdk.errors import SlackApiError

from slack_fetch.config import CrawlerConfig
from slack_fetch.client import create_slack_client
from slack_fetch.channels import collect_channels
from slack_fetch.messages import collect_via_search, collect_via_history
from slack_fetch.threads import collect_channel_threads, collect_threads
from slack_fetch.mentions import collect_mentions
from slack_fetch.rate_limit import rate_wait, handle_rate_limit
from slack_fetch.formatting import _format_channel_messages_md, _format_weekly_md
from slack_fetch.text_cleaner import (
    SlackTextCleaner,
    ts_to_dt,
    ts_to_str,
    load_user_map_from_threads,
    load_channel_map,
)
from slack_fetch.utils import safe_json_loads
from slack_fetch.data_loader import _load_channels, _load_all_messages
from slack_fetch.md_cache import build_md_cache, list_cached_md

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

mcp = FastMCP("slackbox", instructions="Slack 워크스페이스 벌크 크롤링 도구")

# ── 설정/클라이언트 싱글턴 ──────────────────────────────────────

_cfg: CrawlerConfig | None = None
_client = None


def _setup_blocker_response(errors: list[str] | None = None) -> str:
    """Return a token-safe setup response for collection tools."""
    blocker = "; ".join(errors or ["Slackbox local setup is incomplete."])
    return "\n".join([
        "Slackbox setup is incomplete; collection stopped before contacting Slack.",
        f"- Blocker: {blocker}",
        "- Configure a Slack User OAuth Token through Claude plugin sensitive config or Codex MCP/env forwarding.",
        "- Expected token type: Slack User OAuth Token beginning with xoxp- plus read scopes for the requested collection.",
        "- Do not paste tokens into chat.",
        "- Run slackbox_doctor() after setup to verify the Local Slackbox MCP server.",
    ])


def _load_cfg(*, require_token: bool) -> tuple[CrawlerConfig | None, str | None]:
    global _cfg
    if require_token and _cfg is not None:
        return _cfg, None

    try:
        cfg = CrawlerConfig.from_env()
    except Exception as e:
        return None, _setup_blocker_response([
            f"configuration could not be loaded ({type(e).__name__})"
        ])

    if require_token:
        errors = cfg.validate()
        if errors:
            return None, _setup_blocker_response(errors)

    try:
        cfg.ensure_dirs()
    except Exception as e:
        return None, _setup_blocker_response([
            f"local data directory could not be prepared ({type(e).__name__})"
        ])

    if require_token:
        _cfg = cfg
    return cfg, None


def _get_collection_cfg() -> tuple[CrawlerConfig | None, str | None]:
    return _load_cfg(require_token=True)


def _get_data_cfg() -> tuple[CrawlerConfig | None, str | None]:
    return _load_cfg(require_token=False)


def _get_cfg() -> CrawlerConfig:
    cfg, blocker = _get_collection_cfg()
    if blocker:
        raise RuntimeError(blocker)
    assert cfg is not None
    return cfg


def _get_client(cfg: CrawlerConfig | None = None):
    global _client
    if _client is None:
        _client = create_slack_client(cfg or _get_cfg())
    return _client


# ── 헬퍼 ─────────────────────────────────────────────────────────

def _refresh_md_cache(cfg: CrawlerConfig) -> None:
    """수집 완료 후 Markdown 캐시를 갱신한다. 실패해도 수집을 중단하지 않는다."""
    try:
        from slack_fetch.md_cache import build_md_cache
        from slack_fetch.text_cleaner import SlackTextCleaner, load_user_map_from_threads, load_channel_map
        user_map = load_user_map_from_threads(cfg)
        channel_map = load_channel_map(cfg)
        cleaner = SlackTextCleaner(user_map, channel_map)
        result = build_md_cache(cfg, cleaner, cfg.timezone)
        logger.info("MD 캐시 갱신: %s", result)
    except Exception as e:
        logger.warning("MD 캐시 갱신 실패 (무시): %s", e)


def _since_date(days: int) -> str | None:
    """N일 전 날짜를 YYYY-MM-DD 문자열로 반환. Slack search query용."""
    if days <= 0:
        return None
    dt = datetime.now(timezone.utc) - timedelta(days=days)
    return dt.strftime("%Y-%m-%d")


def _since_ts(days: int) -> str | None:
    """N일 전 시각을 Slack timestamp 문자열로 반환. conversations.history용."""
    if days <= 0:
        return None
    dt = datetime.now(timezone.utc) - timedelta(days=days)
    return f"{dt.timestamp():.6f}"


def _until_ts(until: str) -> str | None:
    """YYYY-MM-DD 종료일을 UTC 다음 날 00:00:00 Slack timestamp로 변환한다."""
    if not until:
        return None
    dt = datetime.strptime(until, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return f"{(dt + timedelta(days=1)).timestamp():.6f}"


def _doctor_import_status() -> str:
    checks = {
        "mcp": "mcp",
        "slack_sdk": "slack_sdk",
        "slack_fetch": "slack_fetch.config",
    }
    parts = []
    for label, module_name in checks.items():
        state = "ok" if importlib.util.find_spec(module_name) else "missing"
        parts.append(f"{label}={state}")
    return ", ".join(parts)


def _doctor_data_dir_status(data_dir: Path) -> str:
    try:
        data_dir.mkdir(parents=True, exist_ok=True)
        probe = data_dir / ".slackbox_doctor_write_test"
        probe.write_text("ok", encoding="utf-8")
        probe.unlink(missing_ok=True)
        return "writable"
    except Exception as e:
        return f"not_writable ({type(e).__name__})"


# ── MCP Tools ────────────────────────────────────────────────────

@mcp.tool()
def slackbox_doctor() -> str:
    """Slackbox MCP 런타임 설정을 토큰 안전하게 진단합니다."""
    lines = ["slackbox_doctor:"]

    try:
        cfg = CrawlerConfig.from_env()
    except Exception as e:
        cfg = None
        lines.append(f"- config: load_failed ({type(e).__name__})")

    token = cfg.slack_user_token if cfg else ""
    token_present = bool(token)
    lines.append(f"- SLACK_USER_TOKEN: {'present' if token_present else 'missing'}")

    if not token:
        prefix_state = "missing"
    elif token.startswith("xoxp-"):
        prefix_state = "xoxp- OK"
    elif token.startswith("xoxb-"):
        prefix_state = "xoxb- unsupported bot token"
    else:
        prefix_state = "unknown prefix"
    lines.append(f"- token_prefix: {prefix_state}")

    if cfg:
        lines.append(f"- data_dir: {cfg.data_dir}")
        lines.append(f"- data_dir_access: {_doctor_data_dir_status(cfg.data_dir)}")
    else:
        lines.append("- data_dir: unavailable")
        lines.append("- data_dir_access: unknown")

    lines.append(f"- imports: {_doctor_import_status()}")

    if not (cfg and token.startswith("xoxp-")):
        lines.append("- auth_test: skipped (no plausible xoxp token)")
        return "\n".join(lines)

    try:
        client = create_slack_client(cfg)
        resp = client.auth_test()
        team = resp.get("team") or resp.get("team_id") or "unknown_team"
        user = resp.get("user") or resp.get("user_id") or "unknown_user"
        lines.append(f"- auth_test: ok (team={team}, user={user})")
    except SlackApiError as e:
        error_code = e.response.get("error", "unknown_error")
        lines.append(f"- auth_test: slack_error ({error_code})")
    except Exception as e:
        lines.append(f"- auth_test: failed ({type(e).__name__})")

    return "\n".join(lines)


@mcp.tool()
def list_channels(include_private: bool = False, include_dm: bool = False) -> str:
    """워크스페이스의 가입된 채널 목록을 반환합니다.

    Args:
        include_private: True이면 비공개 채널도 포함합니다.
        include_dm: True이면 DM(im) 및 그룹 DM(mpim)도 포함합니다.

    로컬 캐시(channels.json)가 있고 기본 옵션(public만)이면 캐시를 사용하고,
    없거나 추가 타입이 요청되면 Slack API에서 수집합니다.
    """
    cfg, setup_blocker = _get_collection_cfg()
    if setup_blocker:
        return setup_blocker
    assert cfg is not None

    # channel_types 조합
    types_list = ["public_channel"]
    if include_private:
        types_list.append("private_channel")
    if include_dm:
        types_list.extend(["im", "mpim"])
    channel_types = ",".join(types_list)

    # 기본 옵션(public만)이면 캐시 시도
    use_cache = not include_private and not include_dm
    channels = _load_channels(cfg) if use_cache else []

    if not channels:
        client = _get_client(cfg)
        channels = collect_channels(client, cfg, channel_types=channel_types)

    lines = [f"총 {len(channels)}개 채널:\n"]
    for ch in sorted(channels, key=lambda c: -c.get("num_members", 0)):
        archived = " [archived]" if ch.get("is_archived") else ""
        purpose = f" — {ch['purpose']}" if ch.get("purpose") else ""
        if ch.get("is_im"):
            prefix = "[DM] "
        elif ch.get("is_mpim"):
            prefix = "[GroupDM] "
        else:
            prefix = "#"
        lines.append(f"- {prefix}{ch['name']} ({ch.get('num_members', 0)}명){archived}{purpose}")

    return "\n".join(lines)


@mcp.tool()
def list_users() -> str:
    """워크스페이스의 사용자 목록을 반환합니다.

    사용자 이름, 표시 이름, ID를 확인할 수 있습니다.
    crawl_user나 crawl_mentions에 필요한 user_id를 찾는 데 사용하세요.
    """
    cfg, setup_blocker = _get_collection_cfg()
    if setup_blocker:
        return setup_blocker
    assert cfg is not None
    client = _get_client(cfg)

    members: list[dict] = []
    cursor = None

    try:
        while True:
            kwargs: dict = {"limit": 200}
            if cursor:
                kwargs["cursor"] = cursor

            resp = client.users_list(**kwargs)
            rate_wait()

            for m in resp.get("members", []):
                if m.get("is_bot") or m.get("id") == "USLACKBOT":
                    continue
                if m.get("deleted"):
                    continue
                members.append(m)

            cursor = resp.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
    except SlackApiError as e:
        error_code = e.response.get("error", "unknown_error")
        if error_code in ("token_revoked", "invalid_auth", "not_authed", "account_inactive"):
            return f"Slack 인증 오류 ({error_code}): 토큰이 만료되었거나 무효합니다. 재발급이 필요합니다."
        if error_code == "missing_scope":
            return f"Slack 권한 오류 ({error_code}): 토큰에 필요한 scope가 없습니다. users:read 권한을 확인하세요."
        return f"Slack API 오류 ({error_code}): {e}"

    if not members:
        return "사용자가 없습니다."

    lines = [f"총 {len(members)}명의 사용자:\n"]
    for m in sorted(members, key=lambda u: u.get("real_name", "").lower()):
        profile = m.get("profile", {})
        display_name = profile.get("display_name") or profile.get("display_name_normalized") or ""
        real_name = m.get("real_name", "")
        uid = m["id"]

        if display_name:
            lines.append(f"- @{display_name} ({real_name}) — ID: {uid}")
        else:
            lines.append(f"- @{real_name} ({real_name}) — ID: {uid}")

    return "\n".join(lines)


@mcp.tool()
def crawl_channel(channel: str, days: int = 7, until: str = "", include_threads: bool = False) -> str:
    """특정 채널의 최근 N일간 전체 대화를 수집합니다.

    Args:
        channel: 채널 이름 (예: "general") 또는 채널 ID (예: "C01234")
        days: 수집할 기간 (일). 기본값 7일. 0이면 전체 기간 수집.
        until: 수집 종료일 (YYYY-MM-DD). 비어있으면 오늘까지.
        include_threads: True이면 채널 메시지 수집 후 스레드 답글도 수집합니다.

    수집된 데이터는 로컬 data/ 디렉토리에 저장됩니다.
    """
    channel = channel.lstrip("#")
    cfg, setup_blocker = _get_collection_cfg()
    if setup_blocker:
        return setup_blocker
    assert cfg is not None
    client = _get_client(cfg)

    # 채널 목록에서 채널 정보 찾기
    channels = _load_channels(cfg)
    if not channels:
        channels = collect_channels(client, cfg)

    target_ch = None
    for ch in channels:
        if ch["name"] == channel or ch["id"] == channel:
            target_ch = ch
            break

    if not target_ch:
        return f"채널 '{channel}'을 찾을 수 없습니다. list_channels로 확인하세요."

    since = _since_ts(days) if days > 0 else None
    until_val = _until_ts(until)

    # user_id=None → 채널 전체 대화 수집 (사용자 필터 없음)
    try:
        total = collect_via_history(
            client, cfg, [target_ch], since=since, until=until_val, user_id=None
        )
    except SlackApiError as e:
        error_code = e.response.get("error", "unknown_error")
        if error_code in ("token_revoked", "invalid_auth", "not_authed", "account_inactive"):
            return f"Slack 인증 오류 ({error_code}): 토큰이 만료되었거나 무효합니다. 재발급이 필요합니다."
        if error_code == "missing_scope":
            return f"Slack 권한 오류 ({error_code}): 토큰에 필요한 scope가 없습니다. channels:history 권한을 확인하세요."
        if error_code == "channel_not_found":
            return f"Slack API 오류 ({error_code}): 채널 '{channel}'을 찾을 수 없거나 접근 권한이 없습니다."
        if error_code == "not_in_channel":
            return f"Slack API 오류 ({error_code}): 현재 토큰이 #{target_ch['name']} 채널에 접근할 수 없습니다. 채널 참여 여부와 토큰 권한을 확인하세요."
        return f"Slack API 오류 ({error_code}): {e}"

    period_desc = f"최근 {days}일" if days > 0 else "전체 기간"
    thread_info = ""
    if include_threads:
        try:
            thread_count = collect_channel_threads(client, cfg, channel_id=target_ch["id"])
            thread_info = f"\n스레드 수집: {thread_count}개 완료"
        except SlackApiError as e:
            error_code = e.response.get("error", "unknown_error")
            if error_code in ("token_revoked", "invalid_auth", "not_authed", "account_inactive"):
                thread_info = f"\n스레드 수집 실패 ({error_code}): 토큰이 만료되었거나 무효합니다."
            elif error_code == "missing_scope":
                thread_info = f"\n스레드 수집 실패 ({error_code}): conversations.replies에 필요한 권한을 확인하세요."
            else:
                thread_info = f"\n스레드 수집 실패 ({error_code}): 일부 답글을 수집하지 못했습니다."
        except Exception as e:
            thread_info = f"\n스레드 수집 실패 ({type(e).__name__}): 일부 답글을 수집하지 못했습니다."

    _refresh_md_cache(cfg)
    return (
        f"#{target_ch['name']} 채널 {period_desc} 전체 대화 수집 완료.\n"
        f"수집된 메시지: {total}건\n"
        f"저장 위치: {cfg.channel_messages_path(target_ch['id'])}\n"
        f"get_collected_data로 수집 데이터를 조회할 수 있습니다."
        f"{thread_info}"
        + ("" if include_threads else "\n스레드 답글이 필요하면 include_threads=True로 다시 실행하거나 crawl_threads를 사용하세요.")
    )


@mcp.tool()
def crawl_user(user_id: str, days: int = 30, include_threads: bool = False, until: str = "") -> str:
    """특정 사용자의 최근 N일간 활동을 수집합니다.

    search.messages를 우선 사용하고, 실패 시 conversations.history로 fallback합니다.

    Args:
        user_id: Slack 사용자 ID (예: "U0XXX0X0X0X")
        days: 수집할 기간 (일). 기본값 30일. 0이면 전체 기간 수집.
        include_threads: True이면 메시지 수집 후 자동으로 스레드도 수집합니다.
        until: 수집 종료일 (YYYY-MM-DD). 비어있으면 오늘까지.
    """
    cfg, setup_blocker = _get_collection_cfg()
    if setup_blocker:
        return setup_blocker
    assert cfg is not None
    client = _get_client(cfg)

    search_since = _since_date(days) if days > 0 else None
    search_until = until if until else None
    history_since = _since_ts(days) if days > 0 else None
    history_until = _until_ts(until)

    try:
        total = collect_via_search(client, cfg, since=search_since, until=search_until, user_id=user_id)
        method = "search.messages"
    except SlackApiError as e:
        error_code = e.response.get("error", "unknown_error")
        if error_code in ("token_revoked", "invalid_auth", "not_authed", "account_inactive"):
            return f"Slack 인증 오류 ({error_code}): 토큰이 만료되었거나 무효합니다. 재발급이 필요합니다."
        if error_code == "missing_scope":
            return f"Slack 권한 오류 ({error_code}): 토큰에 필요한 scope가 없습니다. search:read 권한을 확인하세요."
        logger.warning("search.messages 실패 (%s), conversations.history로 fallback", error_code)
        try:
            channels = _load_channels(cfg)
            if not channels:
                channels = collect_channels(client, cfg)
            total = collect_via_history(
                client, cfg, channels, since=history_since, until=history_until, user_id=user_id
            )
            method = "conversations.history"
        except SlackApiError as e2:
            error_code2 = e2.response.get("error", "unknown_error")
            if error_code2 in ("token_revoked", "invalid_auth", "not_authed", "account_inactive"):
                return f"Slack 인증 오류 ({error_code2}): 토큰이 만료되었거나 무효합니다. 재발급이 필요합니다."
            if error_code2 == "missing_scope":
                return f"Slack 권한 오류 ({error_code2}): 토큰에 필요한 scope가 없습니다."
            return f"Slack API 오류 ({error_code2}): {e2}"
    except Exception as e:
        return f"예기치 않은 오류: {e}"

    period_desc = f"최근 {days}일" if days > 0 else "전체 기간"

    thread_info = ""
    if include_threads:
        try:
            thread_count = collect_threads(client, cfg, user_id=user_id)
            thread_info = f"\n스레드 수집: {thread_count}개 완료"
        except SlackApiError as e:
            error_code = e.response.get("error", "unknown_error")
            thread_info = f"\n스레드 수집 실패 ({error_code}): {e}"

    _refresh_md_cache(cfg)
    return (
        f"사용자 {user_id}의 {period_desc} 활동 수집 완료.\n"
        f"수집 방법: {method}\n"
        f"수집된 메시지: {total}건"
        f"{thread_info}"
        + ("" if include_threads else "\n스레드 수집이 필요하면 crawl_threads를 실행하세요.")
    )


@mcp.tool()
def search_messages(query: str, days: int = 30, until: str = "") -> str:
    """키워드로 Slack 메시지를 검색하여 수집합니다.

    Slack search.messages API를 사용하여 임의 검색어로 메시지를 찾습니다.

    Args:
        query: 검색 쿼리. Slack 검색 문법 지원 (예: "배포 in:#general", "from:@홍길동 버그")
        days: 검색 기간 (일). 기본값 30일. 0이면 전체 기간.
        until: 수집 종료일 (YYYY-MM-DD). 비어있으면 오늘까지.
    """
    cfg, setup_blocker = _get_collection_cfg()
    if setup_blocker:
        return setup_blocker
    assert cfg is not None
    client = _get_client(cfg)

    # 검색 디렉토리 생성
    search_dir = cfg.raw_dir / "search"
    search_dir.mkdir(parents=True, exist_ok=True)

    # 쿼리에 기간 조건 추가
    full_query = query
    since = _since_date(days)
    if since:
        full_query += f" after:{since}"
    if until:
        full_query += f" before:{until}"

    # 파일명용 쿼리 sanitize
    sanitized = re.sub(r'[^\w가-힣\s-]', '_', query).strip()
    sanitized = re.sub(r'\s+', '_', sanitized)
    if not sanitized:
        sanitized = "empty_query"
    out_path = search_dir / f"{sanitized}.jsonl"

    # 중복 방지: 기존 파일에서 seen_ts 로드
    seen_ts: set[str] = set()
    if out_path.exists():
        with open(out_path, encoding="utf-8") as ef:
            for line in ef:
                if line.strip():
                    rec = safe_json_loads(line, out_path)
                    if rec is not None:
                        seen_ts.add(f"{rec['ts']}_{rec.get('channel_id', '')}")

    total = 0
    page = 1

    with open(out_path, "a", encoding="utf-8") as f:
        while True:
            try:
                resp = client.search_messages(
                    query=full_query, sort="timestamp",
                    sort_dir="asc", count=100, page=page
                )
            except SlackApiError as e:
                if e.response.status_code == 429:
                    handle_rate_limit(e)
                    continue
                error_code = e.response.get("error", "unknown_error")
                if error_code in ("token_revoked", "invalid_auth", "not_authed", "account_inactive"):
                    return (
                        f"Slack 인증 오류 ({error_code}): 토큰이 만료되었거나 무효합니다."
                    )
                if error_code == "missing_scope":
                    return (
                        f"Slack 권한 부족 ({error_code}): 필요한 scope를 확인하세요."
                    )
                return f"Slack API 오류 ({error_code}): {e}"

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

                record = {
                    "ts": ts,
                    "channel_id": channel_id,
                    "channel_name": msg.get("channel", {}).get("name", ""),
                    "user": msg.get("user") or msg.get("username", ""),
                    "text": msg.get("text", ""),
                    "thread_ts": msg.get("thread_ts"),
                    "reply_count": msg.get("reply_count", 0),
                    "permalink": msg.get("permalink", ""),
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                total += 1

            paging = resp.get("messages", {}).get("paging", {})
            if page >= paging.get("pages", 1):
                break
            page += 1
            rate_wait(1.0)

    period_desc = f"최근 {days}일" if days > 0 else "전체 기간"
    _refresh_md_cache(cfg)
    return (
        f"키워드 검색 수집 완료.\n"
        f"검색어: {query}\n"
        f"기간: {period_desc}\n"
        f"수집된 메시지: {total}건 (기존 중복 제외)\n"
        f"저장 경로: {out_path}"
    )


@mcp.tool()
def crawl_threads(
    channel: str = "",
    thread_ts_list: list[str] | None = None,
    user_id: str | None = None,
) -> str:
    """지정된 스레드들의 전체 대화를 수집합니다.

    user_id를 지정하면 해당 사용자의 messages.jsonl에서 thread_ts를 자동 추출하여
    모든 채널의 스레드를 한 번에 수집합니다 (channel 파라미터 무시).

    Args:
        channel: 채널 이름 또는 채널 ID (user_id 미지정 시 필수)
        thread_ts_list: 수집할 스레드의 타임스탬프 목록 (예: ["1717000000.000000"]).
                        비어있거나 미지정 시 user_id의 messages.jsonl에서 자동 추출.
        user_id: Slack 사용자 ID. 지정하면 해당 사용자의 messages.jsonl에서 thread_ts를
                 자동 추출하고 모든 채널의 스레드를 수집합니다.
    """
    channel = channel.lstrip("#")
    cfg, setup_blocker = _get_collection_cfg()
    if setup_blocker:
        return setup_blocker
    assert cfg is not None
    client = _get_client(cfg)

    # ── 자동 발견 모드: user_id가 주어지면 collect_threads 호출 ──
    if user_id:
        thread_count = collect_threads(client, cfg, user_id=user_id)
        _refresh_md_cache(cfg)
        return (
            f"사용자 {user_id}의 스레드 자동 수집 완료.\n"
            f"수집된 스레드: {thread_count}개\n"
            f"messages.jsonl에서 thread_ts를 자동 추출하여 모든 채널 대상으로 수집했습니다."
        )

    # ── 수동 모드: channel + thread_ts_list 지정 ──
    if not channel:
        return "channel 또는 user_id 중 하나는 반드시 지정해야 합니다."

    if not thread_ts_list:
        return (
            "thread_ts_list가 비어있습니다. "
            "수집할 스레드 타임스탬프를 지정하거나 user_id를 지정하여 자동 발견 모드를 사용하세요."
        )

    # 채널 ID 확인
    channels = _load_channels(cfg)
    channel_id = channel
    channel_name = channel
    for ch in channels:
        if ch["name"] == channel or ch["id"] == channel:
            channel_id = ch["id"]
            channel_name = ch["name"]
            break

    collected = 0
    errors_list: list[str] = []

    threads_dir = cfg.shared_threads_dir
    threads_dir.mkdir(parents=True, exist_ok=True)

    for thread_ts in thread_ts_list:
        key = f"{channel_id}_{thread_ts}"
        out_path = threads_dir / f"{key}.jsonl"

        if out_path.exists():
            collected += 1
            continue

        try:
            resp = client.conversations_replies(
                channel=channel_id, ts=thread_ts, limit=cfg.page_limit
            )
            replies = resp.get("messages", [])

            if replies:
                target_ids = cfg.all_user_ids_set
                with open(out_path, "w", encoding="utf-8") as f:
                    for msg in replies:
                        msg_uid = msg.get("user", "unknown")
                        f.write(json.dumps({
                            "ts": msg.get("ts", ""),
                            "user": msg_uid,
                            "user_name": msg_uid,
                            "text": msg.get("text", ""),
                            "is_target_user": msg_uid in target_ids,
                        }, ensure_ascii=False) + "\n")
                collected += 1

        except SlackApiError as e:
            error_code = e.response.get("error", "unknown_error")
            if error_code in ("token_revoked", "invalid_auth", "not_authed", "account_inactive"):
                return f"Slack 인증 오류 ({error_code}): 토큰이 만료되었거나 무효합니다."
            if error_code == "missing_scope":
                return f"Slack 권한 부족 ({error_code}): 필요한 scope를 확인하세요."
            errors_list.append(f"{thread_ts}: {error_code} - {e}")

    result = f"#{channel_name} 스레드 {collected}/{len(thread_ts_list)}개 수집 완료."
    if errors_list:
        result += f"\n오류: {'; '.join(errors_list)}"
    _refresh_md_cache(cfg)
    return result


@mcp.tool()
def crawl_mentions(user_id: str, days: int = 30, until: str = "") -> str:
    """특정 사용자가 멘션된 메시지를 수집합니다.

    다른 사람이 해당 사용자를 @멘션한 메시지를 검색하여 수집합니다.
    본인이 보낸 메시지는 제외됩니다.

    Args:
        user_id: Slack 사용자 ID (예: "U0XXX0X0X0X")
        days: 수집할 기간 (일). 기본값 30일. 0이면 전체 기간 수집.
        until: 수집 종료일 (YYYY-MM-DD). 비어있으면 오늘까지.
    """
    cfg, setup_blocker = _get_collection_cfg()
    if setup_blocker:
        return setup_blocker
    assert cfg is not None
    client = _get_client(cfg)

    since = _since_date(days) if days > 0 else None
    until_val = until if until else None

    try:
        total = collect_mentions(client, cfg, since=since, until=until_val, user_id=user_id)
    except SlackApiError as e:
        error_code = e.response.get("error", "unknown_error")
        if error_code in ("token_revoked", "invalid_auth", "not_authed", "account_inactive"):
            return f"Slack 인증 오류 ({error_code}): 토큰이 만료되었거나 무효합니다."
        if error_code == "missing_scope":
            return f"Slack 권한 부족 ({error_code}): 필요한 scope를 확인하세요."
        return f"Slack API 오류 ({error_code}): {e}"

    period_desc = f"최근 {days}일" if days > 0 else "전체 기간"
    _refresh_md_cache(cfg)
    return (
        f"사용자 {user_id}의 {period_desc} 멘션 수집 완료.\n"
        f"수집된 멘션: {total}건\n"
        f"저장 위치: {cfg.user_raw_dir(user_id) / 'mentions.jsonl'}"
    )



@mcp.tool()
def get_collected_data(scope: str, format: str = "markdown") -> str:
    """수집된 데이터를 정제된 형태로 반환합니다.

    Args:
        scope: 조회 범위.
            - "all": 전체 수집 데이터
            - "channel:<이름>": 특정 채널 데이터 (예: "channel:general")
            - "week:<주>": 특정 주 데이터 (예: "week:2025-W22")
            - "recent:<N>": 최근 N일 데이터 (예: "recent:7")
            - "search:<query>": 특정 키워드 검색 결과 (예: "search:배포")
            - "summary": 수집 현황 요약
        format: 출력 형식. "markdown" (기본값) 또는 "json".
    """
    cfg, setup_blocker = _get_data_cfg()
    if setup_blocker:
        return setup_blocker
    assert cfg is not None

    # 3가지 소스에서 메시지 로드 (dedup 포함)
    all_messages, source_counts = _load_all_messages(cfg)

    if not all_messages and scope != "summary":
        return "수집된 데이터가 없습니다. crawl_user 또는 crawl_channel을 먼저 실행하세요."

    user_map = load_user_map_from_threads(cfg)
    channel_map = load_channel_map(cfg)
    cleaner = SlackTextCleaner(user_map, channel_map)
    tz = cfg.timezone

    # ── summary ──
    if scope == "summary":
        channels = _load_channels(cfg)
        thread_count = 0
        td = cfg.shared_threads_dir
        if td.exists():
            thread_count = len(list(td.glob("*.jsonl")))

        # 채널 수집 현황
        channels_dir = cfg.raw_dir / "channels"
        crawled_channels = 0
        if channels_dir.exists():
            crawled_channels = len(list(channels_dir.glob("*/messages.jsonl")))

        # 검색 수집 현황
        search_dir = cfg.raw_dir / "search"
        search_files: list[str] = []
        if search_dir.exists():
            search_files = [p.stem for p in sorted(search_dir.glob("*.jsonl"))]

        if not all_messages:
            summary = (
                f"수집 현황:\n"
                f"- 채널: {len(channels)}개\n"
                f"- 메시지: 0건\n"
                f"- 스레드: {thread_count}개\n"
                f"- 수집된 사용자: {', '.join(d.name for d in sorted(cfg.raw_dir.iterdir()) if d.is_dir() and d.name.startswith('U')) or ['없음']}\n"
                f"- 채널 전체 크롤: {crawled_channels}개"
            )
            if search_files:
                summary += f"\n- 검색 데이터: {', '.join(search_files)}"
            return summary

        all_messages.sort(key=lambda m: float(m.get("ts", "0")))
        ch_names = set(m.get("channel_name", "?") for m in all_messages)
        first = ts_to_str(all_messages[0]["ts"], tz)
        last = ts_to_str(all_messages[-1]["ts"], tz)

        summary = (
            f"수집 현황:\n"
            f"- 채널: {len(channels)}개 (활동: {len(ch_names)}개)\n"
            f"- 메시지: {len(all_messages)}건 "
            f"(사용자별: {source_counts['user']}, "
            f"채널별: {source_counts['channel']}, "
            f"검색: {source_counts['search']})\n"
            f"- 스레드: {thread_count}개\n"
            f"- 기간: {first} ~ {last}\n"
            f"- 수집된 사용자: {', '.join(d.name for d in sorted(cfg.raw_dir.iterdir()) if d.is_dir() and d.name.startswith('U')) or ['없음']}\n"
            f"- 채널 전체 크롤: {crawled_channels}개\n"
            f"- 활동 채널: {', '.join(sorted(ch_names))}"
        )
        if search_files:
            summary += f"\n- 검색 데이터: {', '.join(search_files)}"
        return summary

    # ── filter messages ──
    messages = all_messages

    if scope.startswith("channel:"):
        ch_name = scope.split(":", 1)[1]
        messages = [m for m in all_messages if m.get("channel_name") == ch_name]
        if not messages:
            return f"채널 '{ch_name}'에 수집된 메시지가 없습니다."

    elif scope.startswith("week:"):
        target_week = scope.split(":", 1)[1]
        messages = []
        for m in all_messages:
            dt = ts_to_dt(m["ts"], tz)
            wk = f"{dt.isocalendar()[0]}-W{dt.isocalendar()[1]:02d}"
            if wk == target_week:
                messages.append(m)
        if not messages:
            return f"주차 '{target_week}'에 수집된 메시지가 없습니다."

    elif scope.startswith("recent:"):
        try:
            recent_days = int(scope.split(":", 1)[1])
        except ValueError:
            return "recent:<숫자> 형식으로 입력하세요. 예: recent:7"
        cutoff = (datetime.now(timezone.utc) - timedelta(days=recent_days)).timestamp()
        messages = [m for m in all_messages if float(m.get("ts", "0")) >= cutoff]
        if not messages:
            return f"최근 {recent_days}일 내 수집된 메시지가 없습니다."

    elif scope.startswith("search:"):
        query_keyword = scope.split(":", 1)[1]
        # 쿼리명과 매칭되는 검색 결과 파일에서만 로드
        search_dir = cfg.raw_dir / "search"
        if not search_dir.exists():
            return "검색 데이터가 없습니다. search_messages를 먼저 실행하세요."
        sanitized = re.sub(r'[^\w가-힣\s-]', '_', query_keyword).strip()
        sanitized = re.sub(r'\s+', '_', sanitized)
        target_path = search_dir / f"{sanitized}.jsonl"
        if target_path.exists():
            matched_paths = [target_path]
        else:
            # 정확한 파일이 없으면, 파일명에 키워드가 포함된 파일들에서 로드
            matched_paths = [
                p for p in search_dir.glob("*.jsonl")
                if query_keyword.lower() in p.stem.lower()
            ]
            if not matched_paths:
                available = [p.stem for p in search_dir.glob("*.jsonl")]
                return (
                    f"검색어 '{query_keyword}'에 해당하는 데이터가 없습니다.\n"
                    f"사용 가능한 검색 데이터: "
                    f"{', '.join(available) if available else '없음'}"
                )

        # 매칭 파일들에서 메시지 로드 (dedup)
        seen_search: set[str] = set()
        messages = []
        for mp in matched_paths:
            with open(mp, encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        msg = safe_json_loads(line, mp)
                        if msg is None:
                            continue
                        dk = f"{msg.get('ts', '')}_{msg.get('channel_id', '')}"
                        if dk not in seen_search:
                            seen_search.add(dk)
                            messages.append(msg)
        if not messages:
            return f"검색어 '{query_keyword}' 결과가 비어 있습니다."

    elif scope != "all":
        return (
            "scope 형식 오류. 사용 가능한 값:\n"
            "- all: 전체\n"
            "- channel:<이름>: 특정 채널\n"
            "- week:<주>: 특정 주 (예: 2025-W22)\n"
            "- recent:<N>: 최근 N일\n"
            "- search:<검색어>: 특정 키워드 검색 결과\n"
            "- summary: 수집 현황"
        )

    # ── format ──
    if format == "json":
        return json.dumps(messages, ensure_ascii=False, indent=2)

    # markdown: 캐시 기반 파일 목록 반환
    cache_status = build_md_cache(cfg, cleaner, tz)
    cached_files = list_cached_md(cfg)

    # scope에 따라 파일 목록 필터링
    if scope.startswith("channel:"):
        ch_name = scope.split(":", 1)[1].lower()
        cached_files = [f for f in cached_files if ch_name in f["channel"].lower()]
    elif scope.startswith("week:"):
        target_week = scope.split(":", 1)[1]
        cached_files = [f for f in cached_files if f["week"] == target_week]
    elif scope.startswith("recent:"):
        # recent:N일에 해당하는 주차들 계산
        try:
            recent_days = int(scope.split(":", 1)[1])
        except ValueError:
            return "recent:<숫자> 형식으로 입력하세요."
        from datetime import datetime, timedelta, timezone as tz_mod
        cutoff = datetime.now(tz_mod.utc) - timedelta(days=recent_days)
        recent_weeks = set()
        for d in range(recent_days + 7):  # 주 경계 커버
            day = cutoff + timedelta(days=d)
            if day <= datetime.now(tz_mod.utc):
                iso = day.isocalendar()
                recent_weeks.add(f"{iso[0]}-W{iso[1]:02d}")
        cached_files = [f for f in cached_files if f["week"] in recent_weeks]
    elif scope.startswith("search:"):
        # 검색 결과는 캐시 미적용 — 기존 방식으로 직접 포매팅
        return _format_weekly_md(messages, cleaner, tz, cfg)
    # scope == "all"이면 필터 없이 전체

    if not cached_files:
        return "해당 범위에 캐시된 Markdown 파일이 없습니다."

    result = {
        "cache_status": cache_status,
        "files": cached_files,
        "hint": "파일 내용은 Read tool로 path를 읽으세요.",
    }
    return json.dumps(result, ensure_ascii=False, indent=2)


# ── 엔트리포인트 ─────────────────────────────────────────────────

def _ensure_dependencies() -> None:
    """필수 의존성이 없으면 자동 설치."""
    try:
        import slack_sdk  # noqa: F401
    except ImportError:
        import subprocess
        import sys
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "slack-sdk", "python-dotenv", "certifi", "mcp"],
            stdout=subprocess.DEVNULL,
        )


def main():
    """stdio transport로 MCP 서버 실행."""
    _ensure_dependencies()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
