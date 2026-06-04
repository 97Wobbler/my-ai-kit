---
name: "init"
description: "Create a Waypoint docs-first harness for a greenfield repository or run a brownfield audit-only discovery. Use when the user asks to initialize Waypoint, install a docs harness, create AGENTS.md and docs, adopt existing repo docs, or audit a repo before adding Waypoint."
---

# Init

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `init.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.
- Follow repository edit instructions and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill to set a repository waypoint: a visible set of files that tells a
future session what to read, where durable knowledge lives, and what to update
after work.

The MVP supports:

- greenfield creation of the standard docs harness;
- brownfield audit-only discovery and validation;
- read-only preflight classification before deciding what to do.

The MVP does not support brownfield writes, document moves, hook installation,
or future `audit`, `organize`, `close`, and `brief` skills.

## Resolve Inputs

Use the current working directory as the target repository unless the user
provides a path. If the target path is unclear or does not exist, ask one
concise question before continuing.

Run preflight before writing. The default script mode is `auto`, which classifies
the repository into one of four states:

| Detected state | Mode | Behavior |
|---|---|---|
| No Waypoint and weak docs | `greenfield-create` | Create the standard harness. |
| Waypoint present but docs/config/routing are broken | `repair` | Report findings and propose repairs; do not overwrite existing docs. |
| No Waypoint but coherent existing docs | `brownfield-adopt` | Preserve existing homes and propose locator plus minimal routing later. |
| Waypoint present and docs are healthy | `no-op` | Create nothing and report already initialized. |

Use explicit `greenfield` only when the repository has no meaningful existing
`AGENTS.md`, `CLAUDE.md`, or docs harness, or when the user explicitly asks to
create a new harness in a disposable/new repository. Use explicit
`brownfield-audit` when the user wants a read-only report regardless of the
auto recommendation.

`CLAUDE.md` is optional. Generate it only when the user asks for Claude Code
support, asks for both Claude and Codex wrappers, or the target repository
already uses Claude Code.

## Workflow

1. Resolve the installed Waypoint plugin root by walking up from this `SKILL.md`
   until you find `templates/`, `scripts/`, and `mcp/`.
2. Run auto preflight before writing:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_init.py --repo-root <target-repo>
```

3. Read the JSON output:
   - `mode=greenfield` means the script created the standard harness.
   - `mode=repair`, `mode=brownfield-adopt`, or `mode=no-op` means the script
     made no writes and returned `preflight` findings plus a message.
4. If the user explicitly asked for greenfield creation after reviewing
   preflight, run:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_init.py --repo-root <target-repo> --mode greenfield
```

   Add `--with-claude` when a thin `CLAUDE.md` wrapper should be generated.
5. For explicit brownfield audit-only mode, run:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_init.py --repo-root <target-repo> --mode brownfield-audit
```

6. Report created, unchanged, and conflicting paths. If conflicts are reported,
   do not overwrite them; recommend audit/adoption as future work.
7. Run `doctor` or the fallback doctor script after greenfield creation when
   the auto result did not already include doctor output:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_doctor.py --repo-root <target-repo>
```

8. End with the target repository path, generated files, doctor status, and any
   remaining warnings.

## Greenfield Output

The greenfield template creates visible state:

```text
AGENTS.md
docs/
  vision.md
  ontology.md
  architecture.md
  workflows.md
  decisions.md
  plan.md
  todo.md
  ideas.md
  workbench/README.md
.waypoint/config.yaml
```

When requested, it also creates:

```text
CLAUDE.md
```

`.waypoint/cache/` is non-authoritative and should be ignored by Git.

## Brownfield Boundary

For brownfield repositories in the MVP:

- inspect existing docs and routers;
- report likely document homes and gaps;
- do not write `AGENTS.md`, `CLAUDE.md`, `.waypoint/config.yaml`, or moved docs;
- do not normalize names;
- do not weaken existing repository rules.

When auto mode returns `brownfield-adopt`, treat it as a proposal, not an
implemented adoption. When auto mode returns `repair`, propose missing-file or
routing fixes, but ask before changing existing durable docs.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Claude Code plugin skills are namespaced. Users may call `/waypoint:init`.
Prefer the bundled script under the installed plugin root for greenfield file generation.
