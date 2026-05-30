---
name: "slackbox"
description: "Route Slackbox collection requests to local MCP tools. Use when the user asks to list Slack channels or users, collect channel or user messages, search Slack messages, collect mentions or threads, retrieve already collected Slackbox data, or asks what Slackbox can collect. This skill is collection-only; defer analysis and reporting to a future slackbox:analyze skill."
---

# Slackbox

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `slackbox.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- Use network access only when current or external facts are required.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill to route Slack collection requests to the appropriate Slackbox
MCP tool. Slackbox collects workspace context for local review. It does not
analyze, evaluate, score, summarize, or report on people or teams.

Use this skill when the user asks to:

- list Slack channels or users;
- collect messages from a channel;
- collect messages from a user;
- search messages by keyword or query;
- collect messages that mention a user;
- collect threads;
- view data already collected by Slackbox;
- understand what Slackbox can collect, run doctor checks, or identify what
  setup is missing.

Do not use this skill for evaluative people reports, productivity analysis,
sentiment analysis, performance summaries, disciplinary summaries, or manager
briefings. Defer analysis and reporting requests to a future
`slackbox:analyze` skill after collection boundaries are designed.

## Privacy Boundaries

Slackbox is collection-only and must keep workspace data controlled.

- Keep examples synthetic. Do not include real workspace names, channel names,
  user names, message excerpts, customer names, or tokens in responses unless
  the user supplied them in the current request and they are necessary for the
  collection task.
- Do not save collected Slack outputs in plugin source directories, including
  `plugins/slackbox/`, generated skill directories, specs, manifests, docs, or
  examples.
- Do not present collected Slack data as complete or representative unless the
  collection request and returned data prove that scope.
- Do not infer identity, intent, performance, morale, sentiment, productivity,
  or responsibility from collected messages.
- Report collection status, scope, and returned artifact availability. Do not
  turn collected data into an analysis report.

If the user asks for analysis, say that Slackbox can collect the requested
scope but analysis/reporting is deferred to a future `slackbox:analyze` skill.
Offer to collect the bounded source data only.

## Help And Setup Mode

When the user asks what Slackbox can do, invokes the skill without a collection
request, asks for setup help, or uses help-style flags such as `--help`,
provide a short collection-focused help response:

```text
Local Slackbox mode collects Slack context through this plugin's local stdio
MCP server. It can list channels and users, collect channel messages, collect
user activity, search messages, collect mentions, collect threads, and show
already collected data from the local Slackbox data area.

Examples:
- collect the last 7 days from #project-updates
- collect the last 7 days from #project-updates including threads
- collect messages from user U123EXAMPLE for the last 30 days
- search for "release checklist" in the last 14 days
- run --doctor
- setup local Claude
- setup local Codex
- setup remote Claude
- setup remote Codex

Slackbox only collects data. Analysis and reporting are deferred to a future
slackbox:analyze skill.
```

Use these two mode names consistently:

- Local Slackbox: this plugin's bundled local stdio MCP server, Slack Web API
  crawl behavior, local cache, and retrieval from the local Slackbox data area.
- Official Slack Remote MCP: Slack's separate official OAuth HTTP MCP server.
  It is not equivalent to Local Slackbox and does not provide this plugin's
  local cache, crawl, or retrieval behavior.

When the user asks for setup, distinguish the four setup paths:

- setup local Claude: configure the Slackbox plugin's Claude sensitive
  `userConfig` for the Slack User OAuth Token, enable the plugin, reload if
  needed, use `/mcp` to confirm the Local Slackbox MCP server is connected, and
  run `slackbox_doctor` if tools are available.
- setup local Codex: provide `SLACK_USER_TOKEN` to the local Slackbox stdio MCP
  server through Codex plugin/MCP configuration or environment forwarding; use
  `codex mcp list`, `codex mcp get slackbox`, and the TUI `/mcp` view to
  confirm the Local Slackbox server is active.
- setup remote Claude: configure Slack's Official Slack Remote MCP through the
  official Slack remote HTTP MCP/plugin path, then use `/mcp` to complete OAuth
  and inspect the remote server. Explain that this is not Local Slackbox.
- setup remote Codex: configure the Official Slack Remote MCP as a streamable
  HTTP MCP server at `https://mcp.slack.com/mcp`, then run
  `codex mcp login <server-name>` for OAuth-capable remote servers. Explain
  that this does not enable Slackbox local cache, crawl, or retrieval behavior.

If setup is missing, explain only the missing requirement that blocks
collection, such as a Slack user token, required Slack scopes, or workspace
permissions. Do not ask the user to paste tokens into chat.

## Doctor Mode

When the user asks for diagnostics, troubleshooting, health checks, `doctor`,
or `--doctor`, prefer MCP-backed diagnosis when available:

- If Slackbox MCP tools are available and responsive, call
  `slackbox_doctor()` and report the token-safe result in operational terms.
- If MCP tools are unavailable, unlisted, or unresponsive, do not attempt
  collection. Provide skill-only troubleshooting steps without asking for a
  token value:
  - Claude Local Slackbox: confirm plugin sensitive `userConfig` contains a
    Slack User OAuth Token, reload the plugin/session if needed, and inspect
    `/mcp` for the Local Slackbox server and tool count.
  - Codex Local Slackbox: confirm `SLACK_USER_TOKEN` is available to the MCP
    server through `env` or `env_vars`; inspect `codex mcp list`,
    `codex mcp get slackbox`, and the TUI `/mcp` view.
  - Official Slack Remote MCP on Codex: inspect the remote HTTP MCP config and
    use `codex mcp login <server-name>` when OAuth is required.
  - Token shape and scopes: Local Slackbox expects a Slack User OAuth Token
    beginning with `xoxp-`; bot tokens such as `xoxb-` are not the expected
    local token. Confirm the token has the minimum read scopes for the target
    collection and that the Slack app was reinstalled or reauthorized after
    scope changes.
  - Data dir: confirm the Local Slackbox data directory exists or can be
    created and is writable by the MCP server process.

## Tool Routing

Choose the smallest tool or sequence that satisfies the collection request.

| User intent | MCP tool | Synthetic example |
|---|---|---|
| Diagnose setup or runtime health | `slackbox_doctor()` | "run --doctor" |
| List channels | `list_channels(include_private, include_dm)` | "list channels" |
| List users or resolve a user id | `list_users()` | "find user U123EXAMPLE" |
| Collect channel messages | `crawl_channel(channel, days, until, include_threads)` | "collect #project-updates for 7 days" |
| Collect user messages | `crawl_user(user_id, days, include_threads, until)` | "collect U123EXAMPLE for 30 days" |
| Search messages | `search_messages(query, days, until)` | "search release checklist for 14 days" |
| Collect mentions of a user | `crawl_mentions(user_id, days, until)` | "collect mentions of U123EXAMPLE" |
| Collect threads | `crawl_threads(...)` | "collect related threads" |
| Retrieve collected data | `get_collected_data(scope, format)` | "show collected channel data" |

Tool names describe the Slackbox MCP interface. Use the runtime's available
MCP tools rather than shelling out or writing ad hoc Slack API code.

## Parameter Inference

Infer conservative defaults only when the user has provided enough scope to
collect safely.

- If a channel collection request has no period, use `days=7`.
- If a user, mention, search, or thread request has no period, use `days=30`.
- If the user says "all time" or "all available history", use `days=0` only
  after confirming that they really want the broad collection.
- Strip a leading `#` from channel names before passing the channel parameter.
- If the user asks for private channels, set `include_private=true` when
  listing channels.
- If the user asks for direct messages, set `include_dm=true` when listing
  channels if that option is available.
- If the user asks for threads with channel collection, set
  `include_threads=true` on `crawl_channel(...)`.
- If the user asks for threads with user activity, set `include_threads=true`
  on `crawl_user(...)`.
- If the user gives an end date, pass it as `until` in `YYYY-MM-DD` form.
- If a user is named but the user id is missing or uncertain, use
  `list_users()` first and ask the user to choose when multiple matches are
  plausible.
- If a channel name is ambiguous, use `list_channels()` first and ask the user
  to choose when multiple matches are plausible.

Do not broaden scope silently. Ask a concise clarification question when
collection target, identity, time window, or inclusion of private/direct
messages would materially change what gets collected.

## Multi-Step Collection

Some requests require a short sequence:

- User-name collection: `list_users()` first when the id is unknown, then
  `crawl_user(...)`.
- Channel-name collection: `list_channels()` first when the channel id or
  exact channel name is unknown, then `crawl_channel(...)`.
- Collection with threads: use `include_threads=true` on `crawl_channel(...)`
  or `crawl_user(...)` when the primary collection tool supports it. Call
  `crawl_threads(...)` only when explicit thread IDs, user-based thread
  discovery, or a follow-up thread collection step is needed.
- Review existing local output: call `get_collected_data(scope, format)` and
  report what data is available.

Run only the steps needed for collection. Do not add an analysis or summary
step after collection.

## User Communication

Keep user-facing messages short and scoped to collection.

Before collection, state the target and time window when useful:

```text
I will collect #project-updates for the last 7 days.
```

After collection, report:

- what scope was collected;
- whether threads, private channels, direct messages, or broad history were
  included;
- where the runtime says the collected data is available, if it returns an
  artifact or retrieval handle;
- any permission, token, or rate-limit blocker in operational terms.

Do not paste large collected message bodies into chat unless the user
explicitly asks to view already collected data and the returned content is
small enough for the conversation.

## Completion Criteria

The skill is complete when one of these is true:

- the requested collection or retrieval tool has run and the collection scope
  has been reported;
- a blocking setup, permission, identity, or scope question has been asked;
- doctor mode has run `slackbox_doctor()` or provided skill-only
  troubleshooting because MCP was unavailable;
- the request was analysis/reporting-oriented and the user has been redirected
  to bounded collection only;
- help mode has explained the collection capabilities and setup boundary.

## Runtime Overrides

Namespaced plugin skill invocation may vary by runtime and installation. Use the installed Slackbox skill when selected by the runtime, or respond to natural-language requests such as `use slackbox`.
Ask clarification questions sparingly. In Plan Mode, structured user input may be available; in Default mode, ask concise direct questions only when a blocking collection parameter is missing.
