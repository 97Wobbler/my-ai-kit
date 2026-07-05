---
name: "audit"
description: "Audit a Waypoint-style docs harness for document bloat, SSOT routing drift, role mixing, stale plans, and decision-consolidation candidates. Use when the user asks to dry-run docs cleanup, find oversized docs, check AGENTS.md or CLAUDE.md governance, consolidate reverted decisions, or organize repository docs."
---

# Audit

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `audit.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.
- Follow repository edit instructions and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill to review a Waypoint-style documentation harness as an editor,
not as an automatic document manager.

Audit finds:

- document bloat and sections that should be split or archived;
- content that conflicts with the `AGENTS.md` or `CLAUDE.md` source of truth;
- role mixing across plans, decisions, workflows, ideas, reports, and archives;
- optional track/work-item needs when active work has outgrown the plan/todo
  split;
- stale work queues or recommendations that were never promoted into live docs;
- decision records that may be consolidated after a later reversal or correction.

The default mode is always dry-run. Do not edit files unless the user explicitly
asks to apply a specific audit plan or patch.

`audit` is the fast single-pass review. For a post-milestone multi-perspective
sweep that fans out read-only lens subagents and reverse-checks applied cleanup
for over-deletion, route to the `deep-audit` skill instead.

## Inputs

Use the current working directory as the target repository unless the user
provides a path. If the target path is unclear or does not exist, ask one
concise question before continuing.

Classify the request into one of these modes:

| Request | Mode | Writes |
|---|---|---|
| "audit docs", "find bloat", "dry-run cleanup", "check document governance" | `dry-run` | No |
| "show what you would change", "propose organization" | `dry-run` | No |
| "apply this audit plan", "make the approved cleanup" | `apply` | Only approved edits |

If the user asks to "organize" or "clean up" without explicitly approving
edits, run dry-run first and present a proposed plan.

## Reference Files

Resolve the installed Waypoint plugin root by walking up from this `SKILL.md`
until you find `references/`, `scripts/`, and `skills/`.

Read only the reference files needed for the request:

- `references/audit-workflow.md` for the main dry-run and apply flow.
- `references/ssot-rules.md` when checking `AGENTS.md`, `CLAUDE.md`, routing
  tables, document maps, or locator behavior.
- `references/document-bloat.md` when judging oversized documents, role mixing,
  stale plans, or split/archive candidates.
- `references/decision-consolidation.md` when judging reversed, superseded, or
  duplicate decisions.
- `references/apply-safety.md` before making any file edits.

For a normal dry-run audit, read the first four reference files. For apply mode,
read all five.

## Workflow

1. Resolve the target repository and the Waypoint plugin root.
2. Run the read-only audit inventory. Prefer the MCP tool when available:

```text
waypoint_audit(repo_root=<target-repo>)
```

3. If the MCP tool is not available, run the fallback script:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_audit.py --repo-root <target-repo>
```

4. Read the relevant reference files and inspect the repository docs needed to
   verify the inventory findings. Treat script findings as heuristic signals,
   not final judgment.
5. For dry-run mode, report findings with:
   - severity: `high`, `medium`, or `low`;
   - confidence: `high`, `medium`, or `low`;
   - evidence path;
   - recommended action;
   - whether the action is safe to apply automatically after approval.
6. For decision consolidation, distinguish:
   - "preserve both" when the reversal teaches durable context;
   - "consolidate" when the pair was a simple mistaken path with no current
     effect;
   - "archive" when the detail is useful evidence but not live guidance.
7. For apply mode, edit only the user-approved findings. Do not invent new
   migrations while applying. Preserve document meaning, update links and
   routing maps, and keep `.waypoint/config.yaml` as a locator only.
8. Run validation after edits:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_doctor.py --repo-root <target-repo>
python3 <waypoint-plugin-root>/scripts/waypoint_audit.py --repo-root <target-repo>
```

9. Report edited paths, skipped findings, validation status, and remaining
   risks.

## Output Shape

Use this structure for dry-run:

```markdown
**Waypoint Audit**
Mode: dry-run
Status: <clean|findings>

Findings:
- <severity> <code> (<confidence>): <summary> [<path>]
  Recommendation: <action>

Apply candidates:
- <small approved-scope candidate or "None">

Not applied:
No files were changed.
```

Use this structure for apply:

```markdown
**Waypoint Audit**
Mode: apply
Status: <completed|partial>

Changed:
- <path>: <what changed>

Validation:
- doctor: <pass|warn|fail>
- audit: <remaining summary>

Skipped:
- <finding or "None">
```

## Safety Boundaries

- Dry-run means no file edits.
- Do not weaken repository safety, privacy, ownership, release, or test rules.
- Do not delete decision history solely because it is old or inconvenient.
- Do not remove historical reports or archives unless the user explicitly asks
  and the repository router allows it.
- Do not turn `.waypoint/config.yaml` into primary state.
- Ask before making durable naming, taxonomy, public documentation, security,
  privacy, release, or irreversible migration decisions.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Claude Code plugin skills are namespaced. Users may call `/waypoint:audit`.
Use the `waypoint_audit` MCP tool when it is available; otherwise use the bundled fallback script.
Apply mode must use normal repository edit safeguards and preserve unrelated user changes.
