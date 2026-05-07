---
name: {{SKILL_NAME}}
description: >
  Codex repository-local Stateful entry point. Use this skill at the start of a
  fresh Codex session to recover state, inspect the workplan, and continue the
  next runnable task. Trigger on "${{SKILL_NAME}}", "use {{SKILL_NAME}}",
  "resume this repo", "continue the workplan", "repo status".
---

# {{SKILL_NAME}}

This repository uses Stateful for stateful Codex work.

## Required Context Loading

Read these files in order:

1. `AGENTS.md`
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
python3 scripts/stateful/status.py --tool codex
git log --oneline -10
```

## Modes

- `${{SKILL_NAME}}` or "use {{SKILL_NAME}}": recover context and proceed with
  the next automatic task when safe.
- "use {{SKILL_NAME}} status": report workplan status only.
- "use {{SKILL_NAME}} doctor": validate/sync/status only.
- "use {{SKILL_NAME}} close": update `.stateful/session/handoff.md`.
- "use {{SKILL_NAME}} plan": dry-run roadmap-to-workplan proposals with
  `python3 scripts/stateful/plan.py --dry-run`.
- "use {{SKILL_NAME}} archive": dry-run completed-task archival review with
  `python3 scripts/stateful/archive.py --dry-run`.
- "use {{SKILL_NAME}} batch": consider `execution_gate: batch` tasks only when
  the user explicitly asks.

## Rules

- `.stateful/workplan.yaml` is the machine-readable source of truth.
- `.stateful/docs/*` are the human-readable source of truth.
- Treat `.stateful/docs/roadmap.md` as future intent, not as automatically
  executable work.
- Do not mark a task done before outputs and `verify_checks` pass.
- Do not auto-complete `approve`, `execute`, or `review` tasks.
- Before editing files for a task, claim it with
  `python3 scripts/stateful/task.py claim <task-id> --tool codex --summary "<work>"`.
- If stopping mid-task, keep the WIP active and run
  `python3 scripts/stateful/close-session.py --tool codex --handoff-to claude --summary "<handoff>"`.
- If resuming WIP from Claude Code, inspect `wip.summary`, `git status`, and
  the handoff before changing unrelated files.
- Regenerate `.stateful/state.json` after workplan edits.
