# Repository Instructions

This repository uses a Waypoint docs-first recovery harness.

## Always-Loaded Rules

- Treat `AGENTS.md` as the authoritative router for repository work.
- Preserve unrelated user or agent edits.
- Keep durable project knowledge in visible repository docs.
- Treat `.waypoint/config.yaml` as a locator only, not as primary project state.
- Do not hide human-readable planning, decisions, or recovery notes in tool
  cache directories.

## Document Map

- Project purpose and non-goals: `docs/vision.md`.
- Shared vocabulary: `docs/ontology.md`.
- Architecture and ownership boundaries: `docs/architecture.md`.
- Repeatable procedures: `docs/workflows.md`.
- Durable decisions: `docs/decisions.md`.
- Current roadmap and active work: `docs/plan.md`.
- Short task queue: `docs/todo.md`.
- Exploratory ideas: `docs/ideas.md`.
- Scratch notes before promotion: `docs/workbench/`.

## Read And Update Routing

| Work type | Read before work | Update after work |
|---|---|---|
| Change purpose, scope, or non-goals | `docs/vision.md`, `docs/decisions.md` | `docs/vision.md`, `docs/decisions.md` |
| Add or change architecture | `docs/architecture.md`, `docs/decisions.md` | `docs/architecture.md`, `docs/decisions.md` |
| Add or change procedures | `docs/workflows.md` | `docs/workflows.md` |
| Record durable terminology | `docs/ontology.md` | `docs/ontology.md` |
| Plan committed work | `docs/plan.md`, `docs/todo.md` | `docs/plan.md`, `docs/todo.md` |
| Capture exploratory ideas | `docs/ideas.md`, `docs/workbench/` | `docs/ideas.md` |
| Finish meaningful work | Relevant docs above | Update changed authority homes and record validation gaps |

## Session Bootstrap

1. Read this file first.
2. Use the routing table to load only the docs needed for the work.
3. Check repository status before editing.
4. Preserve unrelated edits.
5. Clarify only when a wrong assumption would be costly or irreversible.

## Session Closeout

Before ending meaningful work, check:

- Did the plan or todo change?
- Did a durable decision happen?
- Did a new term, state, or relationship appear?
- Did architecture or workflow change?
- Did an exploratory idea emerge?
- Do workbench notes need promotion or cleanup?
- Were validation commands and known gaps recorded?

## Decision Authority Levels

| Level | Agent behavior |
|---|---|
| Reversible technical implementation | Agent may decide and record rationale when useful. |
| Naming, taxonomy, ontology, or public docs | Agent may propose; user approval is recommended before durable change. |
| Product direction, public release, security, privacy, irreversible migration | User approval is required. |
| Unclear or conflicting evidence | Ask a focused question before writing durable docs. |

## Archive And Report Boundary

Reports, archives, and workbench notes are evidence. They are not live policy
unless this file, `docs/plan.md`, `docs/workflows.md`, or `docs/decisions.md`
explicitly promotes them.

<!-- waypoint:start -->
## Waypoint

Existing repository-specific rules above take precedence. Waypoint only defines
recovery, document routing, and closeout behavior.

Document homes:

- Router: `AGENTS.md`
- Claude wrapper: `{{CLAUDE_PATH}}`
- Vision: `docs/vision.md`
- Ontology: `docs/ontology.md`
- Architecture: `docs/architecture.md`
- Workflows: `docs/workflows.md`
- Decisions: `docs/decisions.md`
- Plan: `docs/plan.md`
- Todo: `docs/todo.md`
- Ideas: `docs/ideas.md`
- Workbench: `docs/workbench/`

Before work, read the relevant document homes. After work, update the document
home whose authority changed.
<!-- waypoint:end -->
