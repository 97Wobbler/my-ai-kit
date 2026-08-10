---
name: "context-bridge"
description: "Edit an existing plan, policy, report, summary, or handoff so readers without its creation context can understand and investigate it independently. Use when a document relies on hidden background, internal terms, prior decisions, or inaccessible references."
---

# Context Bridge

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `context-bridge.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

# Context Bridge

Repair the boundary around an existing document while keeping it as the single source of truth.

1. Read the whole document and infer its intended reader from the request and content.
2. Find material gaps in background, consequential terms, prior decisions, existing behavior, or investigative trailheads. Unfamiliarity alone is not a gap.
3. Add the minimum supported context needed for independent entry. Explain a term at first meaningful use or use one compact terms section when several concepts need a shared home.
4. When deeper evidence belongs elsewhere, leave a concrete trailhead such as a document, decision, ticket, pull request, meeting note, repository path, symbol, owner, or exact search term.
5. Preserve the document's decisions, logic, scope, detail, and voice. Do not create a separate simplified copy or expand into a general document review.
6. Remove drafting-only exclusions, inaccessible internal references, and unexplained private taxonomy. Keep negative constraints when they materially affect the reader's interpretation, behavior, safety, or scope.
7. Verify that every addition closes a real gap and the original remains the source of truth. Summarize the bridges added and report unresolved material gaps separately.

Do not invent context or references. Ask only when a missing fact blocks a responsible edit.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit` with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Read the full target document before editing. Use `apply_patch` for manual edits and preserve unrelated changes.
