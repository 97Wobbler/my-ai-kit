# Autorun Protocol

This protocol defines how an agent resumes and advances work in this
repository.

## Boot Order

1. Read `CLAUDE.md` or `AGENTS.md`.
2. Read `.stateful/config.yaml`.
3. Read `.stateful/workplan.yaml`.
4. Read `.stateful/docs/status.md`.
5. Read `.stateful/docs/decisions.md`.
6. Read `.stateful/session/handoff.md`.
7. Check `git log --oneline -10`.

## Loop

1. **Validate**: run `python3 scripts/stateful/validate-workplan.py`.
2. **Sync**: run `python3 scripts/stateful/sync-state.py`.
3. **Scan**: find tasks with `done: false` and all `blocked_by` tasks done.
4. **WIP check**: if a task has `wip.active: true`, do not start another
   task on top of it. Recover the partial work first, especially when
   `wip.tool` differs from the current tool.
5. **Gate**: skip `human_gate: approve|execute|review` and
   `execution_gate: batch` unless the user explicitly asks.
6. **Claim**: before changing files for a task, run
   `python3 scripts/stateful/task.py claim <task-id> --tool <claude|codex> --summary "<what is being attempted>"`.
7. **Execute**: make the code/doc/data changes required by `spec`.
8. **Verify**: check outputs and task-specific `verify_checks`.
9. **Update**: mark done only after verification; update status/todo/decisions.
10. **Clear or hand off**: after completion, run
   `python3 scripts/stateful/task.py clear <task-id>`. If stopping mid-task,
   keep the WIP active and run `python3 scripts/stateful/close-session.py --tool <claude|codex> --handoff-to <claude|codex> --summary "<handoff>"`.
11. **Sync again**: regenerate `.stateful/state.json`.
12. **Commit**: one completed task per commit when practical.

## Default Stop Conditions

- Only human-gated tasks remain.
- A `review` task is ready.
- A batch task is ready but the user did not ask for batch execution.
- Workplan validation fails.
- A task spec is too ambiguous to execute safely.
- A task has active WIP from another tool and the partial outputs cannot be
  confidently recovered from files and git status.
