---
name: {{SKILL_NAME}}
description: >
  Claude Code repository-local Stateful entry point. Use this skill at the
  start of a fresh Claude Code session to recover state, inspect the workplan,
  and continue the next runnable task. Trigger on "/{{SKILL_NAME}}", "resume
  this repo", "continue the workplan", "repo status".
---

# {{SKILL_NAME}}

This repository uses Stateful for stateful Claude Code work.

## Required Context Loading

Read these files in order:

1. `CLAUDE.md`
2. `.stateful/config.yaml`
3. `.stateful/workplan.yaml`
4. `.stateful/protocols/autorun.md`
5. `.stateful/protocols/gates.md`
6. `.stateful/protocols/recovery.md`
7. `.stateful/docs/status.md`
8. `.stateful/session/handoff.md`
9. `.stateful/docs/roadmap.md` if it exists

Then run:

```bash
python3 scripts/stateful/validate-workplan.py
python3 scripts/stateful/sync-state.py
python3 scripts/stateful/status.py --tool claude
git log --oneline -10
```

## Modes

- `/{{SKILL_NAME}}`: recover context and proceed with the next automatic task
  when safe.
- `/{{SKILL_NAME}} status`: report workplan status only.
- `/{{SKILL_NAME}} doctor`: validate/sync/status only.
- `/{{SKILL_NAME}} close`: update `.stateful/session/handoff.md`.
- `/{{SKILL_NAME}} plan`: dry-run roadmap-to-workplan proposals with
  `python3 scripts/stateful/plan.py --dry-run`.
- `/{{SKILL_NAME}} archive`: dry-run completed-task archival review with
  `python3 scripts/stateful/archive.py --dry-run`.
- `/{{SKILL_NAME}} batch`: consider `execution_gate: batch` tasks only when
  the user explicitly asks.

## Rules

- `.stateful/workplan.yaml` is the machine-readable source of truth.
- `.stateful/docs/*` are the human-readable source of truth.
- Treat `.stateful/docs/roadmap.md` as future intent, not as automatically
  executable work.
- Do not mark a task done before outputs and `verify_checks` pass.
- Do not auto-complete `approve`, `execute`, or `review` tasks.
- Before editing files for a task, claim it with
  `python3 scripts/stateful/task.py claim <task-id> --tool claude --summary "<work>"`.
- If stopping mid-task, keep the WIP active and run
  `python3 scripts/stateful/close-session.py --tool claude --handoff-to codex --summary "<handoff>"`.
- If resuming WIP from Codex, inspect `wip.summary`, `git status`, and the
  handoff before changing unrelated files.
- Regenerate `.stateful/state.json` after workplan edits.
