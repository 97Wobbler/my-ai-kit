---
name: "research"
description: "Plan, track, resume, and inspect a research strategy across multiple experiments, hypotheses, milestones, and alternative paths. Use when the user wants a research graph, contemporaneous decision records, practical stopping or recovery rules, a view of the whole goal while selecting the next experiment, or to prevent local optimization from consuming a research program. Supports LLM and image-generation research without requiring every investigation to be an LLM candidate comparison. Use experiment for a single controlled stochastic comparison. Do not activate for every routine code edit."
---

# Research

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `research.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.
- Follow repository edit instructions and preserve unrelated user changes.
- Delegate only when the runtime supports subagents and the task can run safely in parallel.
- Run the relevant validation checks before reporting completion.

## Purpose

Keep the next research action connected to the whole user or product goal.
Preserve the evidence, alternatives, and reasons stated at important decisions
so the user can intervene. Reduce endless local refinement; a graph's size or
number of experiments is not a success metric.

## Resolve Resources Progressively

Walk upward from this `SKILL.md` to the package containing
`references/research-schema.json` and `scripts/research_store.py`.
Use that package root for commands and sibling resources; do not rely on
runtime cache names or private checkout paths.

- Read `research-strategy.md` and `research-modes.md` when starting or choosing
  a next action.
- Read `research-records.md` before creating, validating, or saving records.
- Read `research-recovery.md` when a path fails or a loop repeats without value.
- Read `research-viewer.md` only when opening or connecting the viewer.
- Read `research-connection.md` only for a requested project connection.

All references above live under package-root `references/`.

## Workflow

1. **Find the goal and existing record.** Read existing project instructions,
   document conventions, goal sources, and any research routing first. Reuse
   their locations and lifecycle; do not impose a new Markdown hierarchy or
   require Waypoint. Distinguish explicit context, observations, inference,
   and retrospective reconstruction. Ask only if uncertainty materially
   changes goals, scope, costs, authority, or success. If creating a record,
   use the user-selected location or propose a reversible workspace location
   outside the installed plugin. Default to mode B unless another mode is agreed.
2. **Map a small strategy.** Separate goals, intermediate milestone outcomes,
   uncertain hypotheses, experiments, and decisions. Permit multiple goals,
   branching paths, parallel work and rejoining an existing milestone.
   Mark mandatory prerequisites versus replaceable support; express ALL/ANY
   groups explicitly. Keep evidence as linked artifacts until it merits its
   own reusable entry. Do not make every run or image a graph node.
3. **Select a bounded next action.** Compare only paths plausibly satisfying
   the goal and mandatory conditions. Consider learning value, likely progress,
   costs, remaining budget, and simpler mechanisms. Label uncertain estimates.
   Set provisional sufficiency, stopping and recovery limits. Explain which
   important uncertainty this test reduces and what action its outcomes change.
4. **Apply one authority boundary.** Mode A advises; B drafts alternatives and
   awaits user strategy adoption; C may change paths and advance experiments
   inside an explicitly approved scope. Recording and viewing do not authorize
   execution. For controlled comparisons, use the existing `experiment` contract:
   explicit initial approval, autonomous work inside its program envelope,
   reapproval for material amendments, and user final candidate adoption.
   Do not create duplicate approvals for already authorized internal steps.
5. **Check purpose at important transitions.** At a milestone, repeated failure,
   strategy change, or criterion change, obtain a bounded independent purpose
   review when authorized and supported. Reuse its role but reload current
   goals and records; optionally add a fresh perspective for a major pivot.
   The main agent validates claims, counterexamples and scope, records why
   opinions were accepted/rejected/deferred, and integrates results as one writer.
   No vote or agent count establishes correctness or evaluator independence.
6. **Record and execute only authorized work.** Append the contemporaneous
   decision, compared alternatives, criteria, evidence and source versions.
   Keep observations and interpretations distinct. Call an approved experiment
   or existing harness where appropriate; this skill supplies no model runner,
   daemon, or external scheduler. Preserve failed, invalid and inconclusive
   outcomes. Do not interpret tool failure as a falsified hypothesis.
7. **Recover proportionally.** First seek a useful alternative rejoining the
   next milestone; then revise milestones while preserving the goal; then
   reconsider the upper decision that adopted the failed premise in this path.
   Apply both backtrack and local exploration limits. Two upper backtracks are
   the initial bound; stop before a third. Keep counters across resumes/name
   changes/new A-prime candidates. Start a new episode only for recorded
   meaningful progress or premise-changing evidence, without resetting total cost.
   Report untested alternatives and resume conditions; a resource stop is not
   global refutation. Apply A/B/C and the overall stopping policy afterward.
8. **Verify, show, and resume.** Validate the JSON and use revision-aware saving;
   never overwrite unrelated edits or rewrite prior decisions. Show the
   packaged read-only viewer when useful. Its focused view and expanded view
   use the same data. Report current goals, important unknowns, next decision,
   limits and evidence gaps. Distinguish functional checks from long-term
   dogfood evidence that research behavior actually improved.

## Operational Rules

- Evidence state and proceed/hold/stop decisions are separate axes. Supported
  evidence is conditional; an inconclusive low-cost path can still be tried.
- Keep quantitative and qualitative goals; expose quality/cost trade-offs
  instead of inventing a weighted score or confidence percentage.
- Adapt practical criteria visibly, but do not attach fixed-sample statistical
  guarantees to adaptively selected favorable results. Use the existing
  stochastic-comparison reference when a quantitative claim is required.
- Record public reasons and evidence references, not hidden internal reasoning
  or sealed evaluator contents. A source snapshot is context, not a new goal SSOT.
- Detailed work can be promoted into the graph if it changes the next decision.
  Avoid per-call paperwork and reviews that themselves create an endless loop.
- Connect a thin project routing point only within authorized installation or
  connection scope. Preserve existing instructions and document lifecycle.
- Run record, tool, and relevant target validations before reporting completion.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Use native questions for material user decisions when available. Resolve the installed package from this skill, not from a private repository path. Use separate agent contexts for bounded purpose or evidence reviews when delegation is authorized and supported. Return review artifacts to the main writer instead of concurrent record edits. Invoke the experiment skill in this Inquiry package when a controlled comparison is needed.
