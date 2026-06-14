# SSOT Rules

Use this reference when comparing repository docs to the routing rules in
`AGENTS.md` or a thin runtime wrapper such as `CLAUDE.md`.

## Source Of Truth

Treat `AGENTS.md` as the primary always-loaded router when present. Treat
`CLAUDE.md` as a wrapper unless it explicitly defines project rules that are not
delegated to `AGENTS.md`.

`.waypoint/config.yaml` is a locator for document homes and install options. It
is not a source of project policy, task state, release state, or decisions.

## Routing Drift

Flag likely drift when:

- `CLAUDE.md` contains project safety or workflow rules that conflict with or
  duplicate `AGENTS.md`;
- `AGENTS.md` names a document home that does not exist;
- important docs exist but are absent from the Document Map;
- the Read/Update routing table sends a work type to a missing or mismatched
  document;
- a lower document defines governance rules that should be in `AGENTS.md`;
- `.waypoint/config.yaml` contains narrative policy or task state.

## Wrapper Drift

A healthy runtime wrapper should be short and should point back to `AGENTS.md`
for durable rules. Flag wrapper drift when `CLAUDE.md` starts carrying:

- release policy;
- privacy or safety policy;
- document governance;
- task routing;
- durable decisions;
- long project background.

## Reporting

For each SSOT finding, report:

- the rule source;
- the conflicting or misplaced content;
- the least disruptive fix;
- whether the fix needs a human decision.

Prefer "move this rule to the router" or "replace duplicate text with a
delegation" over deleting content outright.
