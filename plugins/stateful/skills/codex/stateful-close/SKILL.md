---
name: "stateful-close"
description: "Workflow for closing a working session by updating Stateful handoff state. Summarizes current git/workplan status, next actions, decisions, and risks into .stateful/session/handoff.md. Trigger on \"close session\", \"handoff\", \"세션 인계\", \"세션 종료\", \"다음 세션\"."
---

# Stateful Close

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: `plugins/stateful/specs/stateful-close.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

# stateful-close

Run from the target repository root.

## Procedure

1. Inspect current git state:

```bash
git status --short --branch
git log --oneline -5
```

2. Inspect Stateful state:

```bash
python3 scripts/stateful/status.py
```

3. Update handoff:

```bash
python3 scripts/stateful/close-session.py --summary "<brief session summary>"
```

If the user gave a specific summary, use it. Otherwise derive a concise
summary from the session and git diff.

If the user is pausing so another runtime can continue, include the transition:

```bash
python3 scripts/stateful/close-session.py --tool <runtime> --handoff-to <other-runtime> --summary "<brief session summary>"
```

4. Run validation:

```bash
python3 scripts/stateful/validate-workplan.py
python3 scripts/stateful/sync-state.py
```

5. Report the updated handoff path and whether there are uncommitted changes.

## Rules

- Do not mark tasks done unless outputs and verification are complete.
- Keep active WIP claims when intentionally handing unfinished work to another
  runtime.
- Put durable decisions in `.stateful/docs/decisions.md`, not only in the
  handoff.
- Keep handoff concise enough for a fresh agent session to read first.

## Runtime Overrides

Use --tool codex by default and hand off to claude only when the user asks for a Claude Code continuation.
