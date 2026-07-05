# Deep-Audit Lenses

Use this reference for `waypoint:deep-audit` lens selection, subagent prompt
construction, adjudication, and post-apply reverse checks.

## Lens Selection

Start from the three core lenses. Add optional lenses only when their signal
condition is present. Do not run more than six lenses in one sweep.

| Lens | Tier | Run when |
|---|---|---|
| `conflict` | core | Always. |
| `role-mixing` | core | The doc set has more than one live document. |
| `freshness` | core | Always. |
| `diet` | optional | Long commit streak since the last cleanup, or documents near or past ~500 lines, or the user mentions bloat, diet, or oversized docs. |
| `code-drift` | optional | The repository contains implementation code whose behavior the docs describe. |
| `cold-start` | optional | The doc set claims to support session recovery (routers, status, handoff, plan documents), or the user asks whether a fresh session could resume correctly. |

If the inventory is small — roughly under 10 documents and under ~2,000 total
lines — a multi-agent sweep is usually overkill. Say so, offer the single-pass
`audit` skill instead, and continue with `deep-audit` only if the user insists.

## Lens Catalog

### `conflict` — cross-document factual conflict

Find statements that cannot all be true at once: contradictory scope, numbers,
dates, or terminology across documents; items marked resolved in one place but
still listed as open elsewhere; the same decision recorded with different
outcomes in different homes.

### `role-mixing` — duplication and role integrity

Find content recorded in more than one live document, and documents doing
another document's job: status history inside a recovery/handoff doc, plans
inside todo lists, decisions embedded in reports without promotion, routing
tables bypassed by direct cross-references.

### `freshness` — canonical-versus-stale clarity

Find places where a reader cannot tell which document is the current basis:
archived or superseded material referenced as if live, missing superseded
markers, draft documents treated as decisions, stale claims contradicted by
newer documents, and unclear precedence when two documents overlap.

### `diet` — bloat and dead weight

Find documents that grew past their role: oversized documents (already large
or clearly still growing), completed-work history cluttering live documents,
add-then-revert pairs that cancel out and teach nothing durable, and split or
archive candidates. Size alone is not a finding; size must harm routing,
recovery, or editability.

### `code-drift` — implementation versus documentation

Compare documented behavior against the actual implementation: commands,
configuration keys, defaults, file layouts, feature claims, and test claims.
Report only concrete mismatches with evidence on both sides.

### `cold-start` — recovery simulation

Read only what a fresh session would read (router, then the core documents it
routes to). Then state, from those documents alone: what work is active, what
happens next, and which decisions govern it. Report where the reconstruction
was wrong, ambiguous, or required guessing. The adjudicator compares this
reconstruction against the main session's actual knowledge.

## Subagent Prompt Contract

Every lens subagent prompt must contain:

- the absolute target repository path;
- the explicit document list for this lens, taken from the inventory (plus
  implementation paths for `code-drift`);
- the single lens charter, copied or adapted from the catalog above — one lens
  per subagent;
- a read-only statement: inspect only, never edit files;
- an anti-summary instruction: do not summarize document contents; report only
  problems;
- the report format: for each finding give evidence as `path:line`, why it is
  a problem, severity (`high`/`medium`/`low`), confidence
  (`high`/`medium`/`low`), and a recommended cleanup direction;
- noise suppression: avoid broad catch-all comments likely to duplicate other
  lenses, report only defensible items, and reply exactly
  `no actionable findings` when nothing qualifies.

## Adjudication Rules

Apply these in the main session after all lens reports return:

- Deduplicate findings that point at the same file and the same underlying
  claim, keeping the best-evidenced copy.
- Judge each finding against main-session context. A finding that merely
  restates intentional history, intentional repository policy, or an accepted
  trade-off is not actionable.
- Prefer findings whose fix can be applied mechanically after approval; mark
  the rest as judgment items.
- Keep a short rejected-with-reason list in the briefing so the user can
  override the adjudication.

## Reverse Check

After apply-mode edits, run an over-deletion check before reporting success:

- Give one or two fresh read-only subagents the applied diff (or the changed
  file list plus repository access).
- Charter: find removed or rewritten content whose loss breaks live guidance,
  links, or routing, or silently changes meaning; check that moved content
  actually arrived at its destination.
- Report format: `PASS` or `FAIL`, an issue list with `path:line` evidence,
  and at most 200 words.

A `FAIL` verdict means the cleanup plan missed something: report it to the
user as follow-up findings instead of silently re-editing.
