# Autorun MCP Runtime Support Decision

Status: accepted for implementation planning.

Official documentation checked: 2026-05-10.

## Scope

This note records the runtime MCP contract to use before implementing Autorun
MCP support. It separates officially documented behavior from behavior that
must be verified against the installed runtime.

## Documentation Basis

Claude Code official docs checked:

- `https://code.claude.com/docs/en/plugins`
- `https://code.claude.com/docs/en/plugins-reference`

Claude Code documentation explicitly supports plugin-provided MCP servers via
plugin root `.mcp.json` or inline manifest `mcpServers`. The plugin reference
also documents `${CLAUDE_PLUGIN_ROOT}` for plugin-relative paths and
`${CLAUDE_PLUGIN_DATA}` for plugin data storage.

OpenAI Codex official docs and repository examples checked:

- `https://developers.openai.com/codex/mcp`
- `https://developers.openai.com/codex/plugins/build`
- `https://github.com/openai/plugins`

OpenAI Codex documentation supports general MCP configuration through
`codex mcp` commands and `config.toml` entries such as
`[mcp_servers.<server-name>]` in `~/.codex/config.toml` or trusted
project-scoped `.codex/config.toml`. Current Codex plugin docs also document a
plugin manifest `mcpServers` field pointing to plugin root `.mcp.json`, and the
OpenAI plugin examples repository uses companion files next to
`.codex-plugin/plugin.json`, including `.mcp.json`.

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

## Decisions

Source layout:

- Keep runtime-specific source MCP config files:
  - `plugins/autorun/.mcp.claude.json`
  - `plugins/autorun/.mcp.codex.json`
- During dist build, normalize the selected runtime config to package root
  `.mcp.json`:
  - `dist/claude/autorun/.mcp.json`
  - `dist/codex/autorun/.mcp.json`

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

Fallback:

- If MCP registration, startup, or tool exposure fails in either runtime, keep
  the existing skill-driven workflow available.
- The skill documentation must continue to describe the root `workplan.yaml`
  workflow as the fallback path.

## Verification Checklist

- Claude Code official scope is separated from OpenAI Codex official scope.
- Codex official documentation is separated from implementation-verified
  runtime behavior.
- Runtime-specific MCP source files and dist `.mcp.json` normalization are
  explicit.
- The fallback to skill plus root `workplan.yaml` remains a documented
  requirement.
