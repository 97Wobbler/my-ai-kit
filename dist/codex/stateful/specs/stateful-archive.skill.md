---
name: "stateful-archive"
description: "Review completed Stateful workplan tasks and propose durable summaries, archive actions, or documentation cleanup. Use when the user asks to compact completed tasks, archive old workplan history, summarize finished work into stateful docs, or clean stale docs. Defaults to dry-run and requires user approval before editing or removing records."
targets:
  - codex
capabilities:
  user_questions: required
  file_edits: true
  subagents: none
  plan_mode: optional
  network: false
  validation: required
runtime_overrides:
  claude: |
    Ask for explicit approval before editing docs, archiving files, or removing records. If blocking clarification is required, use Claude Code native question flow.
  codex: |
    Ask for explicit approval before editing docs, archiving files, or removing records. In Plan Mode use structured user input when needed; in Default mode ask concise direct questions and wait.
outputs:
  codex: skills/stateful-archive/SKILL.md
---

# stateful-archive

Use this skill to move completed execution history into durable narrative state
without losing auditability.

## Workflow

1. Read `.stateful/workplan.yaml`, `.stateful/docs/status.md`,
   `.stateful/docs/decisions.md`, `.stateful/docs/risks.md`,
   `.stateful/docs/roadmap.md`, and `.stateful/session/handoff.md`.
2. Run the dry-run helper:

   ```bash
   python3 scripts/stateful/archive.py --dry-run
   ```

   If the target repository has not refreshed runtime scripts yet, run the
   plugin script directly from the installed plugin checkout.

3. Present recommendations to the user before writing:
   - which completed tasks should be summarized;
   - which target docs should receive the summary;
   - which docs appear stale, redundant, or historical;
   - whether anything should be archived or removed.
4. Require explicit user approval before editing docs, archiving files, or
   removing records.
5. After approved edits, run:

   ```bash
   python3 scripts/stateful/validate-workplan.py
   python3 scripts/stateful/sync-state.py
   python3 scripts/stateful/status.py --tool <runtime>
   ```

6. Commit archival or summary changes separately from feature work.

## Rules

- Default to dry-run. Never remove or rewrite historical documents without
  explicit approval.
- Preserve decision rationale in `.stateful/docs/decisions.md`.
- Preserve future work in `.stateful/docs/roadmap.md`.
- Use `.stateful/docs/status.md` for current position, not detailed transcripts.
- If completed tasks remain useful as machine history, keep them in workplan
  and summarize only the durable conclusions.
