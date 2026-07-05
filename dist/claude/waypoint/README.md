# Waypoint

Waypoint installs and inspects a lightweight docs-first repository recovery
harness.

The MVP has six user-facing skills:

- `waypoint`: route or explain Waypoint workflows.
- `init`: run preflight, create a greenfield docs harness when safe, or return
  repair/adopt/no-op guidance without writing.
- `audit`: dry-run documentation bloat, SSOT drift, role mixing, stale-plan,
  and decision-consolidation findings; applies edits only after explicit
  approval.
- `deep-audit`: run a post-milestone multi-perspective docs consistency sweep
  with read-only lens subagents and a post-cleanup over-deletion check.
- `doctor`: inspect document routing, configured homes, marker blocks,
  and local Markdown links.
- `tracks`: enable or maintain the optional `docs/tracks.md` active work layer
  for work that is larger than todos but should not become a hidden task graph.

The MCP server is read-only. It exposes deterministic inspectors:

- `waypoint_discover`
- `waypoint_audit`
- `waypoint_doctor`

Durable project state belongs in visible repository docs. `.waypoint/config.yaml`
is only a locator for document homes and install options.
