---
name: "lite"
description: "Lightweight Autorun workflow for small, clear coding tasks that need durable\nworkplan.yaml state, visible progress, verification, explicit path staging,\nand one commit per task without the Autorun MCP planning loop. Use when the\nuser asks for \"autorun lite\", \"autorun:lite\", \"lite workplan\", or a small\nautomatic task run. Do not use for broad, high-risk, security-sensitive, or\nunclear multi-surface work; escalate those to full Autorun."
---

# Lite

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `lite.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Delegate only when the runtime supports subagents and the task can run safely in parallel.
- Run the relevant validation checks before reporting completion.

Run small coding work through a direct `workplan.yaml` loop without Autorun MCP tools.

## Core Rules

1. **Lite does not use Autorun MCP tools.** Create, read, validate, and update the project-root `workplan.yaml` directly.
2. **Keep the plan small.** Lite is for one to five automatic tasks with obvious dependencies, narrow write surfaces, and clear verification.
3. **Escalate instead of stretching lite.** Switch to full Autorun when the active plan exceeds five tasks, dependencies become non-obvious, repeated splitting is needed, verification is unclear, write surfaces are broad, multiple human gates appear, or security, authorization, data integrity, compatibility, migration, public API, tokenized access, or execution-context behavior is central.
4. **Use `workplan.yaml` as the durable source of truth.** Task specs, dependencies, status, lifecycle timestamps, expected outputs, and verification checks live in the repository root until completion.
5. **Track visible progress.** Keep the runtime-visible task tracker aligned with unfinished `workplan.yaml` tasks.
6. **One task = one commit.** Stage explicit task output paths plus `workplan.yaml`. Do not use broad staging commands.
7. **Verify independently.** A worker or implementation self-check is not enough. Run the relevant project tests, targeted checks, or content review before marking a task verified.
8. **Acceptance criteria are verification checks.** Do not turn every acceptance criterion into a separate task unless it is independently commit-sized work.
9. **Preserve full Autorun compatibility.** Use the same broad schema fields as full Autorun where practical so full Autorun can later validate or refine the plan.

## PLAN Mode

Use PLAN mode when no current `workplan.yaml` exists and the user asks to prepare or start a lite run.

1. Confirm the current directory is inside a Git repository.
2. Read repository instructions before planning. Prefer the runtime's primary instruction file and also read the other runtime instruction file if it contains relevant project rules.
3. Gather only blocking clarification when the goal, success criteria, or constraints are materially ambiguous.
4. Inspect the current code enough to define the as-is and to-be states.
5. Write project-root `workplan.yaml` directly. Use this minimum shape:

```yaml
meta:
  created: YYYY-MM-DD
  spec_source: "<prompt, issue, or document>"
  as_is: "<current state>"
  to_be: "<verified target state>"

tasks:
  - id: T01
    name: "<short task name>"
    blocked_by: []
    human_gate: null
    done: false
    status: pending
    estimated_size: S
    spec: |
      Concrete implementation instructions for this task.
    output:
      - path/to/changed-file
    verify_checks:
      - "<test, command, or review criterion>"
    lifecycle:
      started_at: null
      verified_at: null
      committed_at: null
      worker_id: null
      commit: null
```

6. Keep optional `invariants`, `surfaces`, `criteria_map`, and `not_assessed` sections valid if they are useful, but do not require them for ordinary lite work.
7. If any `not_assessed` item is high-risk or blocks readiness, escalate to full Autorun before RUN.
8. Summarize task count, dependencies, gates, and checks. Ask before entering RUN unless the user already clearly asked to run.

On RUN approval, commit only `workplan.yaml`:

```bash
git add workplan.yaml
git commit -m "chore(autorun-lite): start workplan - <summary>"
```

## RUN Mode

Use RUN mode when `workplan.yaml` exists and the user asks to run, resume, or continue lite.

Preload:

1. Read repository instruction files.
2. Read the full `workplan.yaml`.
3. Inspect recent Git history.
4. Create or update the visible task tracker with all unfinished tasks.

Loop:

1. **Status:** Identify unfinished tasks, done blockers, ready human gates, and runnable automatic tasks.
2. **Human gates:** If a ready `human_gate` task exists, surface it before starting new automatic work.
3. **Escalation check:** Stop and recommend full Autorun if the work has outgrown lite by the Core Rules.
4. **Start:** Set the runnable task to `status: started` and write `lifecycle.started_at`.
5. **Execute:** Implement the task locally or delegate when delegation is useful and authorized. Keep the write scope to the task's `output` paths.
6. **Verify:** Run each `verify_checks` item or the closest available targeted validation. Add any extra relevant check discovered during implementation.
7. **Commit:** Set `status: verified`, then `status: committed`, `done: true`, and lifecycle timestamps before committing. Stage only the task output paths plus `workplan.yaml`.
8. **Repeat:** Continue until no automatic task is runnable.

Commit each completed task with:

```bash
git add <explicit-output-paths> workplan.yaml
git commit -m "<type>(autorun-lite): <task summary>"
```

Completion:

- If every task is done, remove `workplan.yaml` and commit only that removal:

```bash
git rm workplan.yaml
git commit -m "chore(autorun-lite): complete workplan - <summary>"
```

- If human gates, verification failures, resource limits, or user interruption remain, keep `workplan.yaml` for resume.

## Manual Validation

Before reporting completion, run the checks listed in the completed task's `verify_checks`. When the change affects shared behavior, also run the smallest relevant project-level test command. If a command cannot be run, record the blocker in the final summary and leave `workplan.yaml` available for resume when needed.

## Runtime Overrides

Codex invocation may appear as `$autorun:lite` for the plugin skill, or `$lite` when installed directly. Use Codex update_plan for RUN task tracking. Use spawn_agent only when the user has authorized delegation or when parallel delegation is explicitly part of the lite run. Read AGENTS.md first when present, and also read CLAUDE.md when the repository still uses it for useful project rules.
