"""slack-fetch CLI — 설치 후 사용하는 독립 CLI.

명령어:
  slack-fetch init   — 사용자 홈 Slackbox 설정 생성 (토큰 입력 안내)
  slack-fetch serve  — MCP 서버 실행 (stdio transport)
  slack-fetch status — 수집 현황 확인
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from slack_fetch.config import DEFAULT_CONFIG_PATHS, DEFAULT_DATA_DIR


def _plugin_version() -> str:
    plugin_root = Path(__file__).resolve().parents[2]
    for manifest_path in (
        plugin_root / ".codex-plugin" / "plugin.json",
        plugin_root / ".claude-plugin" / "plugin.json",
    ):
        if manifest_path.exists():
            try:
                return str(json.loads(manifest_path.read_text(encoding="utf-8"))["version"])
            except Exception:
                pass
    return "0.0.0"


def _expand_path(value: str | Path) -> Path:
    return Path(str(value)).expanduser()


def _dotenv_value(value: str | Path) -> str:
    text = str(value)
    if not text or any(ch.isspace() for ch in text) or "'" in text:
        return "'" + text.replace("\\", "\\\\").replace("'", "\\'") + "'"
    return text


@click.group()
@click.version_option(version=_plugin_version(), prog_name="slackbox")
def cli():
    """Slack Fetch MCP — 벌크 수집 + MCP 서버"""
    pass


# ── init ──────────────────────────────────────────────────────────

@cli.command()
@click.option(
    "--output",
    "-o",
    default=str(DEFAULT_CONFIG_PATHS[0]),
    help="설정 파일 경로 (기본: ~/.slackbox/config.env)",
)
def init(output: str):
    """초기 설정: Slack 토큰 등 필요한 값을 입력받아 설정 파일을 생성합니다."""
    env_path = _expand_path(output)

    if env_path.exists():
        if not click.confirm(f"{env_path} 가 이미 존재합니다. 덮어쓸까요?", default=False):
            click.echo("취소되었습니다.")
            return

    click.echo()
    click.secho("=== Slack Fetch MCP 초기 설정 (Codex CLI용) ===", fg="cyan", bold=True)
    click.echo()
    click.echo("이 명령은 토큰을 채팅이나 plugin source에 저장하지 않고")
    click.echo(f"로컬 설정 파일에 저장합니다: {env_path}")
    click.echo()

    # Slack User Token
    click.echo("Slack User Token (xoxp-...)")
    click.echo("  1. https://api.slack.com/apps 에서 Slack 앱을 열거나 생성하세요.")
    click.echo("  2. OAuth & Permissions > User Token Scopes에 필요한 scope를 추가하세요.")
    click.echo("     기본: channels:history, channels:read, users:read, search:read")
    click.echo("  3. Install/Reinstall to Workspace 후 User OAuth Token을 복사하세요.")
    click.echo()
    token = click.prompt("  Slack User Token", type=str, hide_input=True)
    if not token.startswith("xoxp-"):
        click.secho("  경고: xoxp-로 시작하지 않습니다. User Token이 맞는지 확인하세요.", fg="yellow")
    click.echo()

    data_dir = click.prompt(
        "  Slackbox 데이터 저장 경로",
        default=str(DEFAULT_DATA_DIR),
        type=str,
    )

    # 설정 파일 생성
    lines = [
        f"SLACK_USER_TOKEN={_dotenv_value(token)}",
        f"SLACK_FETCH_DATA_DIR={_dotenv_value(data_dir)}",
    ]

    env_path.parent.mkdir(parents=True, exist_ok=True)
    env_path.parent.chmod(0o700)
    env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    env_path.chmod(0o600)

    click.echo()
    click.secho(f"설정 파일 생성 완료: {env_path.resolve()}", fg="green", bold=True)
    click.echo()
    click.echo("다음 단계:")
    click.echo("  1. Claude Code 또는 Codex를 재시작하세요.")
    click.echo("  2. Slackbox doctor를 실행해서 auth_test가 ok인지 확인하세요.")
    click.echo("  3. 문제가 있으면 User Token Scopes와 앱 재설치를 다시 확인하세요.")


# ── serve ─────────────────────────────────────────────────────────

@cli.command()
def serve():
    """MCP 서버를 실행합니다 (stdio transport).

    Claude Code에서 직접 호출하거나, MCP 설정에 등록하여 사용합니다.
    """
    from slack_fetch.mcp_server import main as mcp_main
    mcp_main()


# ── status ────────────────────────────────────────────────────────

@cli.command()
def status():
    """수집 현황을 확인합니다."""
    from slack_fetch.config import CrawlerConfig

    try:
        cfg = CrawlerConfig.from_env()
    except Exception as e:
        click.secho(f".env 로드 실패: {e}", fg="red")
        click.echo("slack-fetch init 을 먼저 실행하세요.")
        sys.exit(1)

    errors = cfg.validate()
    if errors:
        click.secho("설정 오류:", fg="red")
        for err in errors:
            click.echo(f"  - {err}")
        click.echo("\nslack-fetch init 을 실행하여 설정을 확인하세요.")
        sys.exit(1)

    click.secho(f"데이터 경로: {cfg.data_dir.resolve()}", fg="cyan")
    click.echo()

    # 채널
    channels_path = cfg.channels_path()
    if channels_path.exists():
        data = json.loads(channels_path.read_text(encoding="utf-8"))
        click.echo(f"채널: {data.get('total', 0)}개")
    else:
        click.echo("채널: 미수집")

    # 채널 전체 수집 현황
    channels_dir = cfg.raw_dir / "channels"
    if channels_dir.exists():
        ch_dirs = [d for d in channels_dir.iterdir() if d.is_dir()]
        total_ch_msgs = 0
        for d in ch_dirs:
            mp = d / "messages.jsonl"
            if mp.exists():
                total_ch_msgs += sum(1 for _ in open(mp, encoding="utf-8"))
        if ch_dirs:
            click.echo(f"채널 수집: {len(ch_dirs)}개 채널, {total_ch_msgs}건")

    # 사용자별 수집 현황
    user_dirs = [d for d in cfg.raw_dir.iterdir()
                 if d.is_dir() and d.name.startswith("U") and len(d.name) >= 9]
    for ud in sorted(user_dirs):
        uid = ud.name
        msg_path = cfg.user_messages_path(uid)
        if msg_path.exists():
            count = sum(1 for _ in open(msg_path, encoding="utf-8"))
            click.echo(f"사용자 {uid}: {count}건")

    # 공유 스레드
    threads_dir = cfg.shared_threads_dir
    if threads_dir.exists():
        thread_files = list(threads_dir.glob("*.jsonl"))
        if thread_files:
            click.echo(f"스레드 (공유): {len(thread_files)}개")

    # 검색 데이터
    search_dir = cfg.raw_dir / "search"
    if search_dir.exists():
        search_files = list(search_dir.glob("*.jsonl"))
        if search_files:
            click.echo(f"검색 데이터: {len(search_files)}개")


# ── 엔트리포인트 ─────────────────────────────────────────────────

def main():
    cli()


if __name__ == "__main__":
    main()
