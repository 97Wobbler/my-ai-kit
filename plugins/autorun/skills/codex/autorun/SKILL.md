---
name: "autorun"
description: "Turn a broad coding request into a dependency-aware project-root workplan.yaml,\nthen run it as an orchestrated workflow using visible task tracking,\nmandatory subagent delegation, independent verification, and one commit per\ncompleted task. Use when the user asks \"autorun 시작\", \"일감 자동 진행\",\n\"워크플랜 돌려\", \"작업 스펙 줄게 알아서 진행해줘\", \"이 요구사항 자동으로 처리해줘\",\n\"태스크 분해하고 돌려\", or otherwise explicitly asks the agent to decompose\nand delegate a multi-step implementation. Supports PLAN mode (spec to\nworkplan) and RUN mode (execute an existing workplan.yaml)."
---

# Autorun

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: `plugins/autorun/specs/autorun.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Delegate only when the runtime supports subagents and the task can run safely in parallel.
- Run the relevant validation checks before reporting completion.

Convert a broad task into a dependency graph and execute it through a controlled orchestration loop.

## Core Rules

1. **Main session = orchestrator, verifier, committer, and state manager.** The main session owns discovery, planning, `workplan.yaml`, verification, commits, and user-facing status. In RUN mode, it must not directly implement workplan tasks. Implementation belongs to subagents.
2. **`workplan.yaml` is the source of truth.** Task specs, dependencies, state, expected outputs, and verification checks live in the project-root `workplan.yaml`.
3. **Track progress with the runtime's visible task tracker.** On RUN entry, create or update the visible task plan. Mark tasks in progress before delegation, and completed immediately after verification and commit.
4. **Autorun invocation authorizes subagent delegation.** When the user invokes autorun RUN mode, that is explicit permission to use subagents for the workplan. Delegate every automatic implementation task. If suitable delegation is unavailable, stop and report instead of implementing locally.
5. **Do not duplicate delegated work.** Once a task is delegated, the main session verifies and integrates the result instead of independently reimplementing the same change.
6. **Verify independently.** Treat a worker's self-check as useful but insufficient. The main session runs L2/L3 checks, and can use a separate read-only subagent for high-risk or large tasks.
7. **One task = one commit.** Include the task's outputs and the `workplan.yaml` state update in the same commit. Stage explicit paths only; never use `git add -A` or `git add .`.
8. **`workplan.yaml` lifecycle is fixed.** The file lives at the Git repository root. Commit it when RUN starts, update it per task, and remove it in a final completion commit only when every automatic task is done.

Main-session exceptions are limited to reading files, planning, updating `workplan.yaml`, running verification commands, applying narrow integration fixes required to reconcile a returned worker patch, and creating commits. Those exceptions do not permit implementing an undelegated workplan task locally.

## PLAN Mode

Use this when the user gives a broad spec and asks the agent to break it down or run it automatically.

1. Confirm the current directory is inside a Git repository with `git rev-parse --is-inside-work-tree`. If not, stop and explain that autorun requires Git.
2. Gather the spec. Ask at most 1-3 blocking questions if scope, success criteria, or constraints are materially ambiguous.
3. Analyze the as-is state with local search and file reads. For broad codebase questions, the autorun request authorizes bounded read-only subagents when they materially improve planning.
4. Write a concrete to-be state.
5. Split the gap into tasks that are suitable for one worker each. Add real dependencies in `blocked_by`; avoid artificial chains.
6. Create project-root `workplan.yaml` from `assets/workplan-template.yaml`. Use `references/workplan-schema.md` for the schema.
7. Summarize phases, task count, dependencies, and gates. Ask before entering RUN mode unless the user's prompt already clearly said to start running.
8. On RUN approval, commit only `workplan.yaml`:

```bash
git add workplan.yaml
git commit -m "chore(autorun): start workplan - <summary>"
```

See `references/planning.md` for detailed planning heuristics.

## RUN Mode

Use this when `workplan.yaml` exists and the user asks to run or resume it.

If `workplan.yaml` is found in a fresh session, do not auto-run. Ask whether to resume, discard, or ignore it.

Preload:

1. Read the runtime's primary project instruction file when present. Also read the other supported runtime instruction file if it exists and contains useful project rules.
2. Read the full `workplan.yaml`.
3. Inspect recent Git history with `git log --oneline -20`.
4. Create or update the visible task plan with all unfinished tasks.

Loop:

1. **SCAN**: Find tasks where `done: false`, every `blocked_by` task is done, and `human_gate: null`.
2. **DRAIN**: Collect completed background subagents, then verify and commit their outputs.
3. **PLAN**: Batch independent tasks that do not touch the same files. Keep dependent chains foreground.
4. **EXEC**: Mark tasks in progress. Delegate every runnable automatic implementation task. For dependency chains, delegate foreground and wait only when the result is needed for the next step. For independent tasks with disjoint write scopes, spawn workers in parallel. Tell each worker they are not alone in the codebase, not to revert others' edits, and to list changed paths. Do not implement the task locally if delegation is unavailable.
5. **VERIFY**: Run L2/L3 checks from `references/verification.md`. Use a separate read-only subagent for large or risky changes when useful.
6. **COMMIT**: Set the task `done: true` in `workplan.yaml`, stage explicit task output paths plus `workplan.yaml`, commit, then mark the plan item completed.
7. **LOOP**: Continue until no automatic task is runnable.

Completion:

- If every task is done, remove the workplan and commit only that removal:

```bash
git rm workplan.yaml
git commit -m "chore(autorun): complete workplan - <summary>"
```

- This deletion commit is part of normal autorun completion. Do it before the final user-facing summary. If the delete commit cannot be created, report the blocker and leave `workplan.yaml` in place for resume.
- If human gates, verification failures, resource limits, or user interruption remain, keep `workplan.yaml` for resume.

See `references/execution-loop.md` for the full loop.

## Subagent Prompting

Use `assets/subagent-prompt-template.md` as the worker prompt template.

- Workers must read the repository's relevant instruction files before editing.
- Workers must not commit.
- Workers must not revert unrelated changes.
- Workers should report changed file paths and a `self-check: PASS` or `self-check: WARN - ...` line.

## Reference Files

- `references/planning.md`: PLAN mode details.
- `references/execution-loop.md`: RUN loop, batching, stop conditions, resume behavior.
- `references/workplan-schema.md`: `workplan.yaml` schema and examples.
- `references/verification.md`: L1/L2/L3 verification protocol.

## Assets

- `assets/workplan-template.yaml`: Starting template for a new workplan.
- `assets/subagent-prompt-template.md`: Worker delegation prompt template.

## Runtime Overrides

Use Codex update_plan for RUN task tracking. Use spawn_agent and wait_agent for required implementation delegation. Read AGENTS.md first when present, and also read CLAUDE.md when the repository still uses it for useful project rules.
