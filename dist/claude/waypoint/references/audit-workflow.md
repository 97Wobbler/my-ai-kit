# Waypoint Audit Workflow

Use this reference for normal `waypoint:audit` runs.

## Default Posture

Audit is read-only by default. The skill may inspect files, run read-only
scripts or MCP tools, and report a proposed cleanup plan. It must not edit files
unless the user explicitly approves an apply scope.

## Dry-Run Steps

1. Identify the target repository.
2. Read the top-level router first:
   - `AGENTS.md` when present;
   - `CLAUDE.md` only as a runtime wrapper unless it clearly contains project
     rules not delegated to `AGENTS.md`.
3. Run `waypoint_audit` or the fallback script to get deterministic inventory.
4. Inspect only the documents needed to verify the inventory:
   - likely routers;
   - docs called out by findings;
   - configured homes from `.waypoint/config.yaml`;
   - decisions docs when consolidation is requested or signaled.
5. Group findings by outcome:
   - fix routing or SSOT drift;
   - split or move mixed content;
   - archive stale detail;
   - consolidate decision history;
   - no action.

## Finding Quality

A useful finding includes:

- evidence path and short reason;
- why the current document role is wrong or overloaded;
- recommended target home;
- confidence and expected risk;
- whether it can be applied mechanically after approval.

Do not present raw size thresholds as final truth. Large documents are only a
problem when size harms routing, recovery, or editability.

## Apply Plan Shape

When the user asks to apply, first reduce the dry-run findings into a bounded
plan:

- exact paths to edit;
- exact sections to move, summarize, archive, or consolidate;
- links and routing entries that must change;
- validation to run afterward.

Apply only that plan. If new issues appear, report them as follow-up findings
instead of expanding scope silently.
