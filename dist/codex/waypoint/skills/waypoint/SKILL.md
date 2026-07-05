---
name: "waypoint"
description: "Router and explainer for the Waypoint docs-first repository harness. Use when the user asks what Waypoint is, wants a repo recovery waypoint, wants to initialize, audit, deep-audit, organize, or validate a docs harness, or mentions waypoint init, audit, deep-audit, or doctor."
---

# Waypoint

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `waypoint.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.

## Purpose

Waypoint is a docs-first repository recovery harness. Its job is to make a
repository easy for a later agent or human session to resume from visible files:

- `AGENTS.md` as the always-loaded router;
- optional thin runtime wrappers such as `CLAUDE.md`;
- focused `docs/*.md` files for purpose, terms, architecture, workflows,
  decisions, plans, optional tracks, todos, ideas, and workbench notes;
- `.waypoint/config.yaml` only as a locator, not as the source of truth.

Waypoint must not recreate the retired `stateful` model. It does not introduce a
custom workplan engine, hidden primary state, mandatory hooks, or generated task
graphs.

## Route Requests

Classify the user's request and route to the smallest shipped workflow:

| Request | Route |
|---|---|
| "What is Waypoint?", "explain waypoint", "should I use it?" | Explain the docs-first harness and shipped MVP. |
| "initialize", "install docs harness", "create AGENTS/docs" | Use `init`. |
| "audit this repo", "brownfield", "what docs exist?" | Use `init` in brownfield audit-only mode or `doctor` if validation is requested. |
| "audit docs", "find bloat", "organize docs", "dry-run cleanup", "consolidate decisions" | Use `audit`; it is dry-run by default and applies edits only after explicit approval. |
| "deep audit", "docs consistency sweep", "big docs cleanup after a large work phase", "multi-perspective docs check", "did the cleanup lose anything" | Use `deep-audit`; it fans out read-only lens subagents, adjudicates their findings, and applies edits only after explicit approval. |
| "doctor", "validate", "check routing", "broken docs links" | Use `doctor`. |
| "tracks", "work items", "epic/story alternative", "larger than todos" | Use `tracks`; it is an optional documentation layer, not a task engine. |
| "close session", "brief next session" | Say these are planned but out of the MVP; offer to run `doctor` or produce a manual summary without claiming Waypoint has shipped close/brief skills. |

## Explanation Points

When explaining Waypoint, keep it concrete:

- It creates a visible documentation harness for greenfield repositories.
- It audits brownfield repositories before suggesting writes.
- It can run a dry-run documentation audit for bloat, routing drift, role
  mixing, stale plans, and decision consolidation candidates.
- It can run a deeper multi-perspective consistency sweep with read-only lens
  subagents after large work phases, including a post-cleanup over-deletion
  check.
- It can optionally add `docs/tracks.md` for larger active work tracks when
  plan/todo alone is not enough.
- It keeps human-readable state in visible docs, not hidden tool-owned state.
- Its MCP tools are read-only inspectors; the skill owns judgment and user
  interaction.
- Hooks, closeout automation, and recovery briefs are future work.

## Safety Boundaries

- Do not overwrite existing repository instructions.
- Do not weaken existing safety, privacy, release, ownership, or test rules.
- Treat brownfield repositories as audit-only in the MVP unless a future shipped
  skill explicitly adds write/adopt behavior.
- Treat `audit` and `deep-audit` apply modes as approval-bound document
  editing, not automatic normalization.
- Ask before making durable naming, taxonomy, public documentation, security,
  privacy, release, or irreversible migration decisions.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Users may call this skill as `$waypoint` or by saying `use waypoint`.
Use `request_user_input` only in Plan Mode. In Default mode, ask a concise direct question only when the target repository or requested workflow is blocking.
