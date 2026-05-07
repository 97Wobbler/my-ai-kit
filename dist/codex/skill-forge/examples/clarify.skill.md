---
name: clarify-example
description: "Create or refine requirements by asking targeted clarification questions before implementation."
targets:
  - claude
  - codex
capabilities:
  user_questions: required
  file_edits: false
  subagents: none
  plan_mode: optional
  network: false
  validation: optional
runtime_overrides:
  claude: |
    Use Claude Code's native question flow for blocking clarification.
  codex: |
    In Plan Mode use request_user_input; in Default mode ask concise text questions.
---

# Clarify Example

When the user's request is ambiguous, restate the goal, identify the decisions
that affect implementation, and ask only the questions needed to make the
request actionable.

Do not implement the original request during clarification.

After the user answers, summarize the confirmed requirement, assumptions, and
remaining risks.
