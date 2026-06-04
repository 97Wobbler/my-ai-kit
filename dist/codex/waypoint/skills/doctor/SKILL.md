---
name: "doctor"
description: "Inspect a repository's Waypoint docs harness health. Use when the user asks to validate Waypoint, check AGENTS.md routing, detect missing configured docs, find duplicate waypoint marker blocks, inspect brownfield docs, or run waypoint doctor."
---

# Doctor

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `doctor.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill to inspect whether a repository has a healthy docs-first recovery
harness. Doctor is read-only. It reports findings; it does not make durable
policy decisions or edit files.

## What Doctor Checks

Doctor checks for:

- `AGENTS.md` presence and basic routing sections;
- `.waypoint/config.yaml` presence and configured document homes;
- missing configured docs;
- duplicate or mismatched `<!-- waypoint:start -->` and
  `<!-- waypoint:end -->` marker blocks;
- `CLAUDE.md` wrapper delegation to `AGENTS.md` when present;
- `.waypoint/cache/` Git ignore coverage when the cache directory exists;
- broken local Markdown links in repository docs.

Findings use `pass`, `warn`, and `fail` levels. A warning is not a policy
decision; it is a prompt for agent judgment.

## Workflow

1. Resolve the target repository from the user's request or use the current
   working directory.
2. Prefer the MCP tool when available:

```text
waypoint_doctor(repo_root=<target-repo>)
```

3. If the MCP tool is not available, resolve the installed Waypoint plugin root
   by walking up from this `SKILL.md` until you find `scripts/` and run:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_doctor.py --repo-root <target-repo>
```

4. Present findings ordered by severity: `fail`, then `warn`, then notable
   `pass` summary. Keep the response concise.
5. If the user asks for fixes, explain that the MVP supports greenfield writes
   and brownfield audit-only behavior. For existing repositories, propose a
   patch plan rather than editing unless a future shipped Waypoint workflow
   supports adoption writes.

## Output Shape

Use this structure:

```markdown
**Waypoint Doctor**
Status: <pass|warn|fail>

Findings:
- <level> <code>: <message> (<path if available>)

Next action:
<one or two concrete next steps>
```

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Users may call this skill as `$doctor` when unambiguous, or by saying `use waypoint:doctor`.
Use `request_user_input` only in Plan Mode. In Default mode, ask a concise direct question only when the target repository is unclear.
Use the `waypoint_doctor` MCP tool when it is available; otherwise use the bundled fallback script.
