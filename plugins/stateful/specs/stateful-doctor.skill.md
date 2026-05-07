---
name: "stateful-doctor"
description: "Workflow for validating an installed Stateful state system. Checks workplan schema, DAG safety, stale generated state, gate consistency, and current runnable tasks. Trigger on \"stateful doctor\", \"validate stateful\", \"check workplan\", \"하네스 검사\", \"워크플랜 검증\"."
targets:
  - claude
  - codex
capabilities:
  user_questions: none
  file_edits: true
  subagents: none
  plan_mode: none
  network: false
  validation: required
runtime_overrides:
  claude: |
    Run status with --tool claude when the target script accepts a tool argument.
  codex: |
    Run status with --tool codex when the target script accepts a tool argument.
outputs:
  claude: plugins/stateful/skills/claude/stateful-doctor/SKILL.md
  codex: plugins/stateful/skills/codex/stateful-doctor/SKILL.md
---

# stateful-doctor

Run from the target repository root.

## Procedure

1. Confirm `.stateful/workplan.yaml` exists.
2. Run:

```bash
python3 scripts/stateful/validate-workplan.py
python3 scripts/stateful/sync-state.py --check
python3 scripts/stateful/status.py --tool <runtime>
```

3. If `sync-state.py --check` reports stale state, run:

```bash
python3 scripts/stateful/sync-state.py
```

4. Report:
   - validation result
   - task count and done count
   - runnable automatic tasks
   - blocked human/review/batch tasks
   - active WIP claims, especially claims started by another runtime
   - stale state or recovery warnings

## Failure Handling

- Unknown gate values, duplicate ids, dangling blockers, cycles, and retired id
  reuse are hard failures.
- Missing outputs for done tasks are warnings by default because older projects
  may adopt Stateful retroactively.
