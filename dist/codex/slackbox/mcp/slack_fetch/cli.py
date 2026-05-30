"""slack-fetch CLI — 설치 후 사용하는 독립 CLI.

명령어:
  slack-fetch init   — .env 초기 설정 (토큰 입력 안내)
  slack-fetch serve  — MCP 서버 실행 (stdio transport)
  slack-fetch status — 수집 현황 확인
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click


@click.group()
@click.version_option(version="0.1.1", prog_name="slackbox")
def cli():
    """Slack Fetch MCP — 벌크 수집 + MCP 서버"""
    pass


# ── init ──────────────────────────────────────────────────────────

@cli.command()
@click.option("--output", "-o", default=".env", help=".env 파일 경로 (기본: .env)")
def init(output: str):
    """초기 설정: Slack 토큰 등 필요한 값을 입력받아 .env 파일을 생성합니다."""
    env_path = Path(output)

    if env_path.exists():
        if not click.confirm(f"{env_path} 가 이미 존재합니다. 덮어쓸까요?", default=False):
            click.echo("취소되었습니다.")
            return

    click.echo()
    click.secho("=== Slack Fetch MCP 초기 설정 ===", fg="cyan", bold=True)
    click.echo()

    # Slack User Token
    click.echo("Slack User Token (xoxp-...)")
    click.echo("  Slack 앱 설정 > OAuth & Permissions > User OAuth Token")
    click.echo("  필요한 scopes: channels:history, channels:read, users:read, search:read")
    click.echo()
    token = click.prompt("  Slack User Token", type=str)
    if not token.startswith("xoxp-"):
        click.secho("  경고: xoxp-로 시작하지 않습니다. User Token이 맞는지 확인하세요.", fg="yellow")
    click.echo()

    # .env 생성
    lines = [
        f"SLACK_USER_TOKEN={token}",
    ]

    env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    click.echo()
    click.secho(f".env 파일 생성 완료: {env_path.resolve()}", fg="green", bold=True)
    click.echo()
    click.echo("다음 단계:")
    click.echo("  slack-fetch serve     # MCP 서버 실행")
    click.echo("  slack-fetch status    # 수집 현황 확인")


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
