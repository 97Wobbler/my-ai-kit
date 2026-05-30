"""python -m slack_fetch 로 CLI 실행.

인자 없이 실행하면 MCP 서버 (serve), 인자가 있으면 CLI 명령 실행.
"""

import sys

from slack_fetch.cli import cli

if __name__ == "__main__":
    cli()
else:
    # python -m slack_fetch 로 실행 시
    cli()
