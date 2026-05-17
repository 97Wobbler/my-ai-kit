# Autorun MCP Runtime Support Decision

Status: accepted for implementation planning.

Official documentation checked: 2026-05-13.

## Scope

This note records the runtime MCP contract to use before implementing Autorun
MCP support. It separates officially documented behavior from behavior that
must be verified against the installed runtime. It also records the boundary
between Autorun's MCP control plane and the experimental worker execution
plane.

## Documentation Basis

Claude Code official docs checked:

- `https://code.claude.com/docs/en/plugins`
- `https://code.claude.com/docs/en/plugins-reference`
- `https://code.claude.com/docs/en/plugin-marketplaces`
- `https://code.claude.com/docs/en/headless`

Claude Code documentation explicitly supports plugin-provided MCP servers via
plugin root `.mcp.json` or inline manifest `mcpServers`. The plugin reference
also documents `${CLAUDE_PLUGIN_ROOT}` for plugin-relative paths and
`${CLAUDE_PLUGIN_DATA}` for plugin data storage.

Claude Code headless documentation says `claude -p` / `--print` runs
non-interactively, reads stdin and writes stdout like a command-line tool, and
supports structured output such as JSON and streaming JSON. It also documents
tool approval controls such as `--allowedTools` and permission modes. This is
official documentation for possible future Claude worker execution, but
Autorun does not wire a Claude worker runtime in the current implementation.

OpenAI Codex official docs and repository examples checked:

- `https://developers.openai.com/codex/noninteractive`
- `https://developers.openai.com/codex/mcp`
- `https://developers.openai.com/codex/subagents`
- `https://developers.openai.com/codex/plugins/build`
- `https://github.com/openai/plugins`

OpenAI Codex documentation supports general MCP configuration through
`codex mcp` commands and `config.toml` entries such as
`[mcp_servers.<server-name>]` in `~/.codex/config.toml` or trusted
project-scoped `.codex/config.toml`. Current Codex plugin docs also document a
plugin manifest `mcpServers` field pointing to plugin root `.mcp.json`, and the
OpenAI plugin examples repository uses companion files next to
`.codex-plugin/plugin.json`, including `.mcp.json`.

Codex non-interactive documentation says `codex exec` is intended for
pipeline, CLI, and automation workflows, can run with explicit sandbox and
approval settings, and can emit machine-readable JSON Lines with `--json`.

Codex MCP documentation says MCP servers can be configured in Codex
`config.toml` and documents `startup_timeout_sec` and `tool_timeout_sec`.
The default `tool_timeout_sec` is 60 seconds. Autorun worker start therefore
must be non-blocking from the MCP tool perspective; long-running worker
execution must be observed through status and collect calls instead of holding
one MCP tool call open for the whole worker lifetime.

Codex subagents documentation says Codex can orchestrate subagent workflows by
spawning specialized agents in parallel, waiting for them, and returning a
consolidated result. It also says Codex only spawns subagents when explicitly
asked to do so. Autorun invocation in RUN mode is the explicit user request
that authorizes delegation inside the main Codex session; it does not by itself
make the experimental MCP worker execution plane mandatory.

## Implementation-Verified Boundary

For Codex CLI/Desktop, plugin packaging shape is documented, but Autorun must
still treat installed plugin-managed MCP runtime behavior as
implementation-verified until smoke-tested locally. In particular, verify:

- whether a plugin-installed MCP server is automatically registered and exposed
  in both CLI and Desktop surfaces;
- the process `cwd` used for stdio MCP launchers from a plugin package;
- whether relative `command`, `args`, and `cwd` values resolve from the
  installed plugin root;
- whether any Codex-specific path variables are available or stable.

Do not present those runtime observations as official OpenAI contract unless
they are added to official documentation.

Local Codex CLI 0.130.0 verification on 2026-05-10 showed that a plugin
`.mcp.json` stdio server with `"cwd": "."` is resolved to the installed plugin
root. Without this field, Codex left `cwd` unset and launched relative
`args` from the active project directory, which broke bundled Python MCP
entrypoints such as `mcp/server.py`.

Experimental worker execution is implementation-backed, not an official
Autorun runtime contract. The current worker runner uses `codex exec --json`
because the Codex official docs provide a documented non-interactive execution
mode, explicit sandbox/approval flags, and a JSONL event stream that can be
captured by the runner.

Proposal-only planning helpers use the same Codex-first worker transport but
remain control-plane inputs, not execution authority. Decomposition, split, and
review workers write structured JSON artifacts outside the repository. The
main session or MCP repair tools must validate and explicitly accept any
proposal before `workplan.yaml` changes.

Claude worker execution is deferred even though Claude headless mode is
officially documented. A safe Claude runner still needs separate implementation
and verification for process lifecycle, permission/tool mapping, output
capture, cancellation, status reporting, changed-path reporting, and how it
coexists with Claude Code plugin MCP packaging. Until that work is added and
smoke-tested, do not claim Claude worker execution support.

## Decisions

Source layout:

- Keep runtime-specific source MCP config files:
  - `plugins/autorun/.mcp.claude.json`
  - `plugins/autorun/.mcp.codex.json`
- During dist build, keep the runtime-specific packaging shape:
  - Claude keeps inline manifest `mcpServers` and also bundles MCP code under
    `skills/autorun/mcp/` for `${CLAUDE_PLUGIN_ROOT}` resolution.
  - Codex rewrites manifest `mcpServers` to `./.mcp.json` and copies the
    selected MCP config to package root `.mcp.json`.

Claude config:

- Use `${CLAUDE_PLUGIN_ROOT}` for bundled executable and reference paths.
- Use `${CLAUDE_PLUGIN_DATA}` for plugin-owned persistent runtime data.
- Bundle through plugin root `.mcp.json` or manifest `mcpServers`, matching the
  official Claude Code plugin contract.

Codex config:

- Use a relative-path stdio config in the Codex `.mcp.json`, with `"cwd": "."`
  so bundled relative `args` resolve from the installed plugin root.
- Do not rely on Codex path variables until they are either officially
  documented or implementation-verified and recorded.

Worker execution plane:

- Keep Autorun's MCP control plane as the default MCP responsibility: plan
  creation, validation, batching, task lifecycle updates, and plan status.
- Use project-root `workplan.yaml` as the single durable plan state for both
  MCP-backed and direct-YAML workflows. Do not create repo-local
  `.autorun/mcp/plans/*.json` plan state.
- Require `repo_root` or explicit `workplan_path` for plan/status/lifecycle
  MCP calls. A packaged MCP server may run with the installed plugin directory
  as process cwd, so the server must not infer the user project from cwd.
- Keep core plan loading free of undeclared third-party dependencies. The
  bundled MCP server must be able to load Autorun's emitted workplan YAML with
  the Python standard library only.
- Store worker artifacts outside the repository by default. Prefer explicit
  `artifact_dir`, then `${CLAUDE_PLUGIN_DATA}` when available, then a platform
  user state directory. Treat Codex plugin data directory variables as
  undocumented unless later verified and recorded.
- Treat worker execution tools as an experimental adjunct. Worker start must
  return promptly with an identifier; status and collect calls own observation
  of long-running work.
- Start with Codex workers only. The runner can use documented `codex exec`
  automation behavior plus JSONL events, and current local implementation work
  can be verified against those semantics.
- Defer Claude workers. Claude headless mode is documented, but this change
  does not implement or verify a Claude worker runtime.
- The main session remains the orchestrator, reviewer, verifier, state owner,
  and committer. Workers must not commit. Workers must report changed paths and
  enough detail for the main session to verify results before task completion.

Fallback and control-plane-only contract:

- If MCP registration, startup, or tool exposure fails in either runtime, keep
  the existing skill-driven workflow available.
- The skill documentation must continue to describe direct root
  `workplan.yaml` editing as the fallback path.
- If worker execution tools are absent, failing, unsupported by the current
  runtime, or not explicitly requested through Autorun RUN mode, continue with
  control-plane-only Autorun: use MCP for planning/state when available, and
  use runtime-native delegation/subagents while keeping `workplan.yaml` as the
  durable state.
- Failure of the experimental worker execution plane must not invalidate the
  MCP control plane. Plan/state MCP tools may remain usable even when workers
  are disabled or failing.

## Verification Checklist

- Claude Code official scope is separated from OpenAI Codex official scope.
- Codex official documentation is separated from implementation-verified
  runtime behavior.
- Runtime-specific MCP source files and dist packaging behavior are explicit.
- Codex worker execution support is labeled experimental and
  implementation-backed.
- Claude headless support is documented but worker execution is deferred.
- Direct root `workplan.yaml` editing remains a documented fallback
  requirement.
