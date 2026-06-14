# Document Bloat And Role Mixing

Use this reference when judging whether a document has outgrown its role.

## Heuristics

Size is a signal, not a verdict. Treat these as prompts for inspection:

- router docs over roughly 250 lines;
- thin runtime wrappers over roughly 80 lines;
- focused docs over roughly 400 lines;
- docs with many unrelated top-level headings;
- live docs that include long historical narratives or obsolete batches;
- repeated sections with similar names across multiple docs.

## Role Smells

Flag likely role mixing when:

- `docs/plan.md` contains durable decisions, release policy, or historical
  evidence;
- `docs/decisions.md` contains active TODO queues or implementation batches;
- `docs/workflows.md` contains one-off session notes or speculative ideas;
- `docs/ideas.md` contains committed roadmap items;
- `docs/reports/` or `docs/archives/` are treated as live instructions without
  promotion through the router;
- `README.md` carries private operational process that belongs in internal docs.

## Recommended Actions

Use the smallest useful action:

- summarize a long obsolete section in place and move detail to an archive;
- split a document only when it has two durable audiences or update paths;
- move active work into the live plan;
- move durable policy into workflows or the router;
- move durable choices into decisions;
- leave large docs alone when they are cohesive and easy to scan.

## Reporting

Report document bloat with:

- current role;
- observed overload;
- recommended destination;
- expected benefit;
- risk of losing context.

Do not optimize for shortness alone. Optimize for recovery: a future session
should know what to read, what is current, and what can be ignored.
