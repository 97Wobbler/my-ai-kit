# my-ai-kit

`my-ai-kit` is a personal Claude Code and Codex CLI plugin marketplace. It is
for versioning and reinstalling the AI workflows, repo state tools, and future
MCP-backed utilities I use across machines.

This repository is private-first. The goal is repeatable personal setup, not a
general public framework.

## Current Contents

The repository currently contains six installable plugins.

The `stateful` plugin installs a repository-local state system based on the pattern
documented in
[`repo-stateful-harness-report.md`](repo-stateful-harness-report.md): keep
agent session state in the repository, not in chat memory.

The selected future plugin names are:

| Plugin | Purpose | Status |
|---|---|---|
| `stateful` | Install and operate repo-local workplan, handoff, roadmap, and recovery state | Available |
| `restate` | Restate and verify user intent before execution | Available |
| `autorun` | Run dependency-aware workplans with bounded autonomous execution | Available |
| `skill-forge` | Author one Skill Forge spec and compile Claude/Codex runtime skills | Available |
| `studycoach` | Coach project-local self-study roadmaps and Rumsfeld Known/Unknown matrices | Available |
| `prism` | Discover and compose analytical instruments for multi-perspective analysis | Available |

MCP plugin work is intentionally deferred until there is a concrete MCP server
to package.

## Repository Direction

The target layout is a marketplace monorepo:

```text
my-ai-kit/
├── .claude-plugin/
│   └── marketplace.json
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── plugins/
│   ├── stateful/
│   ├── restate/
│   ├── autorun/
│   ├── skill-forge/
│   ├── studycoach/
│   └── prism/
└── docs/
```

The original root-level `harness` plugin has been moved into
`plugins/stateful/`.

## Install The Marketplace

Install from GitHub:

```bash
claude plugin marketplace add 97Wobbler/my-ai-kit
codex plugin marketplace add 97Wobbler/my-ai-kit
```

Local checkout alternative:

```bash
claude plugin marketplace add /path/to/my-ai-kit
codex plugin marketplace add /path/to/my-ai-kit
```

## Stateful Plugin Usage

The stateful plugin is installed from the `my-ai-kit` marketplace.

Claude Code:

```bash
claude plugin install stateful@my-ai-kit
```

Codex CLI:

```bash
codex
/plugins
```

In the Codex plugin browser, choose the `my-ai-kit` marketplace and install
`stateful`.

## Install Stateful Workflow Into A Repository

From any target repository, run the current installer from this checkout:

```bash
python3 /path/to/my-ai-kit/plugins/stateful/scripts/stateful_init.py --root . --skill repo
```

Inside Claude Code, the current plugin also exposes:

```bash
stateful-init --root . --skill repo
```

In Codex, use the installed plugin skill:

```text
@stateful-init
```

Use a different `--skill` value if you want another repo-local skill name:

```bash
python3 /path/to/my-ai-kit/plugins/stateful/scripts/stateful_init.py --root . --skill stateful
```

The installer is conservative. Existing scaffold files are left untouched
unless `--force` is passed.

## Daily Commands In an Installed Repo

```bash
python3 scripts/stateful/validate-workplan.py
python3 scripts/stateful/sync-state.py
python3 scripts/stateful/status.py --tool codex
python3 scripts/stateful/task.py claim R002 --tool codex --summary "Implementing R002"
python3 scripts/stateful/plan.py --dry-run
python3 scripts/stateful/archive.py --dry-run
python3 scripts/stateful/close-session.py --tool codex --handoff-to claude --summary "Where to continue"
```

Fresh agent sessions should start with the generated repo-local skill:

```text
Claude Code: /repo
Codex: $repo or "use repo skill"
```

## Project State

This repository now dogfoods its own stateful workflow.

Start future sessions by reading:

1. `AGENTS.md` or `CLAUDE.md`
2. `.stateful/config.yaml`
3. `.stateful/workplan.yaml`
4. `.stateful/session/handoff.md`

Then run:

```bash
python3 scripts/stateful/status.py --tool codex
```

## Development Checks

Validate the current plugin files:

```bash
claude plugin validate .
python3 -m py_compile plugins/stateful/scripts/*.py scripts/stateful/*.py
python3 scripts/plugins/check-codex-installed-drift.py
```

`check-codex-installed-drift.py` is a local guardrail for Codex: it compares
the rebuilt `dist/codex` plugins with the copies currently installed under
`~/.codex`. If it reports stale files, refresh the Codex plugin installation
before relying on local skill behavior.

Validate the stateful workplan:

```bash
python3 scripts/stateful/validate-workplan.py
python3 scripts/stateful/sync-state.py --check
```
