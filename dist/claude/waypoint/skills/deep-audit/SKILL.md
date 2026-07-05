---
name: "deep-audit"
description: "Multi-perspective documentation consistency sweep using read-only lens subagents. Use after a large work phase, pivot, or long commit streak when the user asks for a docs consistency review, big docs cleanup, docs diet, stale-doc sweep, cross-document conflict check, code-versus-docs drift check, or a post-cleanup over-deletion check."
---

# Deep Audit

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `deep-audit.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.
- Follow repository edit instructions and preserve unrelated user changes.
- This skill requires subagent delegation for workflow steps that call for it; the main session orchestrates and verifies instead of doing delegated work locally.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill for a post-milestone documentation consistency sweep: several
read-only lens subagents inspect the doc set from different perspectives, the
main session adjudicates their findings, and cleanup is applied only after the
user approves a bounded plan.

`deep-audit` complements `audit`. `audit` is the fast single-pass dry-run
review backed by deterministic inventory heuristics. `deep-audit` is for the
bigger moments — after a large work phase, a direction pivot, or a long commit
streak — when one pass and one perspective are not enough and over-deletion
risk matters.

The default mode is always dry-run. Do not edit files unless the user
explicitly approves a specific cleanup plan.

## Inputs

Use the current working directory as the target repository unless the user
provides a path. If the target path is unclear or does not exist, ask one
concise question before continuing.

Classify the request into one of these modes:

| Request | Mode | Writes |
|---|---|---|
| "deep audit", "docs consistency sweep", "big docs cleanup", "docs diet", "stale docs sweep" | `dry-run` | No |
| "apply the deep-audit plan", "make the approved cleanup" | `apply` | Only approved edits |
| "check the recent docs cleanup for over-deletion", "did the cleanup lose anything" | `verify-cleanup` | No |

If the user asks to "clean up" without explicitly approving edits, run dry-run
first and present a proposed plan.

The doc scope may be a Waypoint harness, but does not have to be. When the
repository has no `AGENTS.md` and no `.waypoint/config.yaml`, treat it as a
brownfield doc set: infer the documentation roots (for example `docs/`,
`branch-docs/`, or a work-scoped docs directory), confirm them with the user
if ambiguous, and preserve the existing document names and homes. Do not
normalize a coherent brownfield documentation system into Waypoint defaults.

## Reference Files

Resolve the installed Waypoint plugin root by walking up from this `SKILL.md`
until you find `references/`, `scripts/`, and `skills/`.

Read only the reference files needed for the request:

- `references/deep-audit-lenses.md` always: lens catalog, subagent prompt
  contract, adjudication rules, and the reverse check.
- `references/audit-workflow.md` for the shared dry-run posture and finding
  quality bar.
- `references/ssot-rules.md` when routing, routers, or document maps are in
  scope.
- `references/document-bloat.md` when the `diet` lens runs.
- `references/decision-consolidation.md` when decision records are in scope.
- `references/apply-safety.md` before any apply-mode edit.

## Workflow

1. Resolve the target repository, the Waypoint plugin root, and the mode.
2. Preflight repository hygiene: check version-control status. If unrelated
   uncommitted changes exist, recommend that the user commit or stash them
   first so cleanup edits stay separable; do not commit for the user. If the
   repository has no version control, warn that the reverse check will be
   weaker.
3. Build the document inventory. Prefer the `waypoint_audit` MCP tool:

```text
waypoint_audit(repo_root=<target-repo>)
```

   If the MCP tool is not available, run the fallback script:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_audit.py --repo-root <target-repo>
```

   For a brownfield doc set without a Waypoint harness, list the Markdown
   documents under the confirmed doc roots with their sizes instead, and treat
   that listing as the inventory.
4. Check scale. For a small inventory, offer the single-pass `audit` skill
   instead, as described in `references/deep-audit-lenses.md`.
5. Select lenses per `references/deep-audit-lenses.md` and tell the user in
   one line which lenses will run. This is not a blocking question unless the
   scope is genuinely ambiguous.
6. Fan out one read-only subagent per selected lens, following the subagent
   prompt contract in `references/deep-audit-lenses.md`. Launch independent
   lenses concurrently when the runtime allows it. Subagents inspect and
   report only; they never edit files.
7. Adjudicate the returned findings in the main session using the
   adjudication rules: deduplicate, judge validity against main-session
   context, rank by severity, and keep a rejected-with-reason list.
8. Brief the user: accepted findings, rejected findings with reasons, and a
   bounded cleanup plan with exact paths, moves, archives, link updates, and
   the validation to run. Dry-run mode stops here; no files were changed.
9. For apply mode, read `references/apply-safety.md` and apply only the
   user-approved plan. Do not invent new migrations while applying. Preserve
   document meaning, move content before deleting it, and update links and
   routing maps.
10. Validate after edits. When a Waypoint harness is present:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_doctor.py --repo-root <target-repo>
python3 <waypoint-plugin-root>/scripts/waypoint_audit.py --repo-root <target-repo>
```

    For a brownfield doc set, verify local Markdown links and routing
    references touched by the edits.
11. Run the reverse check from `references/deep-audit-lenses.md`: fresh
    read-only subagents inspect the applied diff for over-deletion and broken
    routing, returning `PASS` or `FAIL`. Report a `FAIL` as follow-up
    findings; do not silently re-edit.
12. Report edited paths, skipped findings, validation status, the reverse
    check verdict, and remaining risks. Suggest committing the cleanup
    separately from unrelated work; commit only if the user asks.

For `verify-cleanup` mode, skip steps 4–9: identify the cleanup commits or
diff range with the user, then run steps 11–12 against that diff.

## Output Shape

Use this structure for dry-run:

```markdown
**Waypoint Deep-Audit**
Mode: dry-run
Lenses: <lens list>
Status: <clean|findings>

Findings:
- <severity> <lens> (<confidence>): <summary> [<path>]
  Recommendation: <action>

Rejected:
- <finding>: <reason> (or "None")

Proposed plan:
- <bounded step or "No action needed">

Not applied:
No files were changed.
```

Use this structure for apply:

```markdown
**Waypoint Deep-Audit**
Mode: apply
Status: <completed|partial>

Changed:
- <path>: <what changed>

Validation:
- doctor: <pass|warn|fail|n/a>
- audit: <remaining summary|n/a>

Reverse check:
- <PASS|FAIL>: <summary>

Skipped:
- <finding or "None">
```

For `verify-cleanup`, report only the reverse-check block plus follow-up
findings.

## Safety Boundaries

- Dry-run and verify-cleanup mean no file edits.
- Lens subagents are read-only; never delegate edits to a subagent.
- Do not run more than six lens subagents in one sweep.
- Do not weaken repository safety, privacy, ownership, release, or test rules.
- Do not delete decision history solely because it is old or inconvenient.
- Do not remove historical reports or archives unless the user explicitly asks
  and the repository router allows it.
- Do not normalize a coherent brownfield documentation system into Waypoint
  defaults, and do not turn `.waypoint/config.yaml` into primary state.
- Ask before making durable naming, taxonomy, public documentation, security,
  privacy, release, or irreversible migration decisions.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Claude Code plugin skills are namespaced. Users may call `/waypoint:deep-audit`.
Spawn lens subagents with the native subagent primitive, launching independent lenses in one parallel batch. Prefer the built-in read-only exploration agent type for lens subagents.
Use the `waypoint_audit` MCP tool for the inventory when it is available; otherwise use the bundled fallback script.
Apply mode must use normal repository edit safeguards and preserve unrelated user changes.
