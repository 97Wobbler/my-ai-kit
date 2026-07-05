# Slackbox

Slackbox collects Slack workspace context through a local stdio MCP workflow.
It is for fetching channel, user, search, mention, and thread data into a
local runtime data area so the user can inspect, retrieve, or hand off the
collected context.

The current plugin is collection-focused. Analysis, evaluation, summaries,
people reports, and management-style reporting are intentionally out of scope
for this skill and are deferred to a future `slackbox:analyze` skill.

## Modes

Slackbox local mode and Slack's official remote MCP connection are separate
paths. They both connect AI tools to Slack, but they are not equivalent.

### Local Slackbox Mode

Local Slackbox mode is this plugin's bundled local stdio MCP server. It runs on
the user's machine and uses a Slack User OAuth Token to crawl, cache, and
retrieve Slack context through Slack Web API calls.

Use this mode when the workflow needs Slackbox's local collection behavior:

- channel and user lookup;
- recent message collection;
- search, mention, and thread collection;
- retrieval from the local Slackbox data area.

### Official Slack Remote MCP Mode

Official Slack Remote MCP mode uses Slack's official remote HTTP MCP server at
`https://mcp.slack.com/mcp` with runtime OAuth. It is a separate official
connection path for live Slack MCP tools. It does not provide Slackbox's local
cache, crawl, or retrieval behavior.

Use this mode when the desired behavior is the official Slack MCP connection
managed by the runtime and workspace OAuth flow, rather than Slackbox local
collection.

## Skills

- `slackbox`: Route natural-language Slack collection requests to the
  available Slackbox MCP tools.

## What It Can Collect

Slackbox can help with:

- channel and user lookup;
- recent channel message collection;
- recent user activity collection;
- keyword search collection;
- mention collection;
- thread collection;
- retrieval of already collected local data.

Examples use synthetic names only:

```text
Use slackbox to list available channels.
Use slackbox to collect the last 7 days from #project-updates.
Use slackbox to collect messages from user U123EXAMPLE for the last 30 days.
Use slackbox to search for "release checklist" across the last 14 days.
Use slackbox to collect threads related to the collected context.
Show the Slackbox data that has already been collected.
```

## Privacy Boundaries

Slackbox is designed for controlled collection, not judgment.

- Do not use real workspace names, channel names, user names, message excerpts,
  or tokens in examples, tests, documentation, or plugin source.
- Do not save collected Slack outputs inside `plugins/slackbox/` or any plugin
  source directory.
- Do not produce evaluative people reports, productivity rankings, sentiment
  judgments, performance narratives, or disciplinary summaries.
- Do not imply that collected data is complete or representative unless the
  collection request and returned data prove that scope.
- Keep analysis and reporting requests deferred to a future
  `slackbox:analyze` skill.

## Invocation

Claude Code:

```text
/slackbox
/slackbox list channels
/slackbox collect #project-updates for 7 days
```

Codex CLI:

```text
$slackbox
use slackbox to list users
use slackbox to collect mentions for U123EXAMPLE
```

## Configuration

Slackbox local mode requires a Slack User OAuth Token with an `xoxp-` prefix
and read access appropriate to the requested workspace data. Never paste real
tokens into chat, examples, tests, documentation, or plugin source.

Use the minimum Slack scopes and workspace permissions needed for the
collection task. If token setup or permissions are missing, the skill should
explain the missing setup and stop before attempting collection.

### Slack App And User Token Setup

Local Slackbox uses Slack Web API calls through a Slack User OAuth Token. This
is different from Slack's official remote MCP OAuth flow.

1. Open `https://api.slack.com/apps`.
2. Create a new internal Slack app for the target workspace, or open an
   existing app you control.
3. Go to **OAuth & Permissions**.
4. Under **User Token Scopes**, add only the scopes needed for the collection
   target.
5. Install or reinstall the app to the workspace after changing scopes.
6. Copy the **User OAuth Token** from the OAuth page. It should begin with
   `xoxp-`. A bot token beginning with `xoxb-` is not the expected token for
   Local Slackbox.

Do not paste the token into chat. Store it only in the runtime's sensitive
configuration UI or in the local Slackbox config file described below.

### Claude Code Local Slackbox Mode

Claude Code local mode uses this plugin's `userConfig` sensitive configuration
for the Slack User OAuth Token. Enter the token only through the plugin
configuration prompt or runtime configuration UI. Do not ask users to paste
tokens into chat.

The token is exposed to the local Slackbox MCP server through the plugin's
sensitive runtime configuration, not as a public README value.

### Codex Local Slackbox Mode

Codex local mode should use a one-time local Slackbox config file by default:

```text
~/.slackbox/config.env
```

This avoids asking non-technical users to export shell environment variables
before every Codex run. Prefer the setup wizard over manual file editing.

Ask Slackbox for setup help or run `slackbox_setup_guide()` from the MCP tools.
The guide prints exact commands for the installed plugin. On macOS or Linux it
looks like this:

```bash
cd '/path/to/installed/slackbox'
scripts/slackbox-setup
```

On Windows PowerShell it looks like this:

```powershell
cd "C:\path\to\installed\slackbox"
powershell -ExecutionPolicy Bypass -File .\scripts\slackbox-setup.ps1
```

Open a new terminal, paste those lines, and press Enter. When the
wizard asks for a token, paste the copied `xoxp-` User OAuth Token into the
terminal prompt. Do not paste the real token into Codex chat. A token beginning
with `xoxb-` is a bot token and is not the expected token for Local Slackbox.

The wizard creates `~/.slackbox/config.env` with user-only file permissions.
The equivalent manual setup is:

```bash
mkdir -p "$HOME/.slackbox"
chmod 700 "$HOME/.slackbox"

cat > "$HOME/.slackbox/config.env" <<'EOF'
SLACK_USER_TOKEN=xoxp-your-token-here
SLACK_FETCH_DATA_DIR=~/.slackbox/data
EOF

chmod 600 "$HOME/.slackbox/config.env"
```

Replace `xoxp-your-token-here` locally in the terminal or a local editor. Do
not paste the real token into chat.

After creating the file, restart Codex and verify:

```text
/mcp
$slackbox --doctor
```

Advanced users may still use environment variables. The installed Codex plugin
forwards `SLACK_USER_TOKEN` and `SLACK_FETCH_DATA_DIR` with `env_vars`, and
sets only the fixed `PYTHONPATH` literal through `env`.

Codex MCP `env` values are copied as literal values, so do not put shell-style
placeholders such as `${SLACK_USER_TOKEN}` in `env`. Reserve `env` for fixed
values such as `PYTHONPATH`.

Do not claim that Codex provides a plugin `userConfig` secret prompt for this
value unless official Codex docs document that behavior. `codex mcp login` is
for OAuth-capable streamable HTTP MCP servers; it does not authenticate this
local Slackbox stdio server.

For a manually registered local MCP server, prefer `config.toml` when you need
parent-env forwarding:

```toml
[mcp_servers.slackbox]
command = "python3"
args = ["/path/to/slackbox/mcp/server.py"]
env_vars = ["SLACK_USER_TOKEN", "SLACK_FETCH_DATA_DIR"]
```

Codex's `codex mcp add --env KEY=VALUE` CLI flag stores environment values for
stdio servers. Use it only when that literal value is what you want saved in
the MCP config.

```bash
codex mcp list
codex mcp get slackbox
```

In the Codex TUI, use `/mcp` to check whether the Slackbox MCP server is
active. Run `slackbox_setup_guide()` or ask for Slackbox setup help when the
steps are unclear.

### Official Remote MCP Mode

Claude Code can connect to the official Slack remote HTTP MCP path through the
official Slack plugin or a remote HTTP MCP configuration, then use `/mcp` to
complete OAuth.

Codex can connect to the official Slack remote HTTP MCP path with `codex mcp`
configuration and OAuth login:

```bash
codex mcp add slack-official --url https://mcp.slack.com/mcp
codex mcp login slack-official
```

This configures the official Slack Remote MCP mode only. It does not enable
Slackbox local cache, crawl, or retrieval behavior.

### Required Slack Scopes

Slackbox local mode currently expects a Slack User OAuth Token, not a bot
token. Use a token beginning with `xoxp-`.

Minimum public-channel collection scopes:

- `channels:read`
- `channels:history`
- `users:read`
- `search:read`

Add these scopes when the collection target includes private channels, direct
messages, or group direct messages:

- private channels: `groups:read`, `groups:history`
- direct messages: `im:read`, `im:history`
- group direct messages: `mpim:read`, `mpim:history`

After changing Slack app scopes, reinstall or reauthorize the Slack app so the
issued user token includes the updated scopes.

## Official Docs Consulted

Docs consulted on 2026-05-30 and 2026-07-05:

- Claude Code MCP documentation:
  `https://code.claude.com/docs/en/mcp`
- Claude Code plugin reference:
  `https://code.claude.com/docs/en/plugins-reference`
- OpenAI Codex MCP servers documentation:
  `https://developers.openai.com/codex/configuration/mcp-servers`
- OpenAI Codex current manual, MCP section:
  `https://developers.openai.com/codex/mcp`
- Slack OAuth scopes reference:
  `https://docs.slack.dev/reference/scopes/`
- Slack tokens reference:
  `https://docs.slack.dev/authentication/tokens`
- Slack installing with OAuth guide:
  `https://docs.slack.dev/authentication/installing-with-oauth`
- Slack `conversations.history` method:
  `https://docs.slack.dev/reference/methods/conversations.history/`
- Slack `conversations.replies` method:
  `https://docs.slack.dev/reference/methods/conversations.replies/`
- Slack official MCP server overview:
  `https://docs.slack.dev/ai/mcp-server`
