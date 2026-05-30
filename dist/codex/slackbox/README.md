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

### Claude Code Local Slackbox Mode

Claude Code local mode uses this plugin's `userConfig` sensitive configuration
for the Slack User OAuth Token. Enter the token only through the plugin
configuration prompt or runtime configuration UI. Do not ask users to paste
tokens into chat.

The token is exposed to the local Slackbox MCP server through the plugin's
sensitive runtime configuration, not as a public README value.

### Codex Local Slackbox Mode

Codex local mode should use Codex MCP configuration or environment forwarding
for `SLACK_USER_TOKEN`. Do not claim that Codex provides a plugin `userConfig`
secret prompt for this value unless official Codex docs document that behavior.

For an installed Slackbox plugin, set the environment before starting Codex and
then verify that the plugin MCP server is visible:

```bash
export SLACK_USER_TOKEN='<set-this-in-your-shell>'
codex
/mcp
```

For a manually registered local MCP server, prefer Codex's MCP configuration
commands and pass the token as an environment variable:

```bash
codex mcp add slackbox --env SLACK_USER_TOKEN="$SLACK_USER_TOKEN" -- python3 /path/to/slackbox/mcp/server.py
codex mcp list
codex mcp get slackbox
```

In the Codex TUI, use `/mcp` to check whether the Slackbox MCP server is
active. A project or user `config.toml` can also pass `SLACK_USER_TOKEN`
through the server's `env` or `env_vars` settings.

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

### Slack App And Token Setup

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

Docs consulted on 2026-05-30:

- Claude Code MCP documentation:
  `https://code.claude.com/docs/en/mcp`
- Claude Code plugin reference:
  `https://code.claude.com/docs/en/plugins-reference`
- OpenAI Codex MCP servers documentation:
  `https://developers.openai.com/codex/configuration/mcp-servers`
- Slack OAuth scopes reference:
  `https://docs.slack.dev/reference/scopes/`
- Slack `conversations.history` method:
  `https://docs.slack.dev/reference/methods/conversations.history/`
- Slack `conversations.replies` method:
  `https://docs.slack.dev/reference/methods/conversations.replies/`
- Slack official MCP server overview:
  `https://docs.slack.dev/ai/mcp-server`
