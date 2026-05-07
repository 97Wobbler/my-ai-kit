---
name: "stateful-plan"
description: "Convert Stateful roadmap material into proposed workplan tasks. Use when the user asks to turn .stateful/docs/roadmap.md into executable work, promote roadmap items into .stateful/workplan.yaml, or plan the next stateful tasks. Defaults to dry-run and requires user approval before applying changes."
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
    Ask for explicit approval before applying roadmap-to-workplan changes. If blocking clarification is required, use Claude Code native question flow.
  codex: |
    Ask for explicit approval before applying roadmap-to-workplan changes. In Plan Mode use structured user input when needed; in Default mode ask concise direct questions and wait.
outputs:
  codex: skills/stateful-plan/SKILL.md
---

# stateful-plan

Use this skill to bridge future-oriented roadmap notes into executable
`.stateful/workplan.yaml` tasks.

## Workflow

1. Read `.stateful/config.yaml`, `.stateful/docs/roadmap.md`, and
   `.stateful/workplan.yaml`.
2. Run the dry-run helper:

   ```bash
   python3 scripts/stateful/plan.py --dry-run
   ```

   If the target repository has not refreshed runtime scripts yet, run the
   plugin script directly from the installed plugin checkout.

3. Review each proposed task for:
   - concrete output paths;
   - meaningful `verify_checks`;
   - correct dependencies;
   - correct gates.
4. Ask for explicit user approval before appending tasks.
5. After approval, either:
   - run `python3 scripts/stateful/plan.py --apply` and then refine the new
     tasks manually, or
   - edit `.stateful/workplan.yaml` directly when the proposals need
     substantial judgment.
6. Run:

   ```bash
   python3 scripts/stateful/validate-workplan.py
   python3 scripts/stateful/sync-state.py
   python3 scripts/stateful/status.py --tool <runtime>
   ```

7. Commit the roadmap-to-workplan update separately from implementation work.

## Rules

- Do not treat roadmap prose as automatically executable.
- Prefer `human_gate: approve` for newly promoted tasks until outputs and
  verification checks are concrete.
- Do not delete roadmap entries while promoting them; preserve durable intent.
- If there are no roadmap candidates, report that clearly and stop.
