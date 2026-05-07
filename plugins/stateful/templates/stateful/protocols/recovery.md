# Recovery Protocol

When a fresh session starts, do not trust chat memory. Recover from files and
git history.

## Checks

1. Run `git status --short --branch`.
2. Run `git log --oneline -10`.
3. Run `python3 scripts/stateful/status.py --tool <claude|codex>`.
4. Inspect tasks with `wip.active: true`.
5. Read `.stateful/session/handoff.md` before choosing work.

## Three-way Recovery

For a pending task that appears partially executed or has active WIP:

1. **Active WIP from current tool**: continue only after checking git status,
   task spec, and handoff.
2. **Active WIP from another tool**: treat it as a handoff, not as a fresh
   task. Read `wip.summary`, inspect uncommitted files, then either continue
   the same task or ask before replacing the WIP claim.
3. **Outputs exist, no commit**: verify outputs, then ask before marking done.
4. **No outputs, no commit**: clean abort; run
   `python3 scripts/stateful/task.py clear <task-id>` if the WIP is stale.
5. **Outputs exist, commit exists**: likely done flag drift; report and patch
   workplan.

Never overwrite expensive generated outputs during recovery without checking
whether they are the only evidence of prior work.

## Cross-tool Handoff

Claude Code and Codex share the same state files. Tool-specific instructions
may differ, but task ownership must move through `.stateful/workplan.yaml` and
`.stateful/session/handoff.md`.

- Before pausing mid-task, keep `wip.active: true` and update the handoff with
  the current tool and intended next tool.
- When resuming in the other tool, run status with `--tool`, inspect the active
  WIP, and continue that task before selecting unrelated runnable work.
- Use `--force` on `task.py claim` only after recovery proves the previous WIP
  is stale or intentionally abandoned.
