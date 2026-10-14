# Research Record v1

Use `research-schema.json` as the structural schema. Both the Python writer and
packaged TypeScript viewer validate it plus references, goal ancestry and hard
dependency cycles. This is one workspace JSON file outside the plugin cache.
JSON is the initial canonical format; YAML import is not implemented.

| Section | Meaning |
|---|---|
| authority | A/B/C, approved scope, referenced experiment contracts and their approval provenance |
| budget | One explicit unit, whole-program limit and cumulative spent; use linked ledgers for other units |
| nodes | goal, milestone, hypothesis, experiment, decision; state and evidence state are separate |
| edges | contributes_to, requires, supports, challenges, tests, informs, supersedes |
| prerequisites | ALL/ANY members for a target; multiple incoming lines alone cannot express this |
| paths | branch/rejoin node IDs, goal IDs, draft/adopted/paused/exhausted/superseded, rationale and uncertain cost/likelihood |
| decisions | timestamp, mode_at_decision, actor, action, rationale, alternatives, source versions and reviews with dispositions |
| recoveries | failed premise, path, original adoption decision, append-only reviewed upper points, limits/counters; linked resets cite prior_episode_id, reset_evidence_refs and a new reset_decision_id |
| documents | immutable source reference, version and summary as read at the decision, not a new purpose SSOT |
| evidence | artifact reference, conditions, summary and provenance; no sealed evaluator content |

Hypotheses need `evidence_state`: `not_tested`, `inconclusive`, `supported`,
`challenged`, or `mixed`. Include conditions and relevant evidence. Null/boolean
cannot distinguish untested, inconclusive and missing data. Supported does not
mean universal proof; proceeding is an explicit decision.

`requires` is a hard prerequisite, `supports` may be replaceable rationale.
Never mechanically propagate a failed support into downstream refutation.
AND groups and unconditional required edges must be acyclic. ANY alternatives
are not all mandatory edges. The file represents claims/criteria; validation
does not infer proof, causal validity or successful execution from labels.

Begin with important hypotheses, experiments, results and changes. Keep detailed
logs as references; promote details when they affect the next action. Evidence
can stay attached to an experiment until reused or conflicting. No per-image
node requirement. Keep contemporaneous reasons distinct from later reconstruction.

Commands use `<package-root>` resolved from the installed skill:

```sh
python3 <package-root>/scripts/research_store.py init /workspace/research.json --id image-study --title "Image study" --mode B --budget-unit calls --budget-limit 30
python3 <package-root>/scripts/research_store.py validate /workspace/research.json
python3 <package-root>/scripts/research_store.py save /workspace/research.json --proposal /workspace/proposal.json --expected-revision 0
```

The `init` default scope is design-only. Replace it with actual agreed scope
and contract references before experiments; creating a record is not approval.
Use the synthetic `examples/research-demo.json` to inspect a complete shape,
not as approved data or a scoring truth set.

For saves, main reads current revision, integrates worker artifacts, writes a
complete proposal to a separate workspace file, validates, then saves against
that revision. Writers use an exclusive sibling `.lock` and atomic replacement.
On conflict re-read/reconcile; do not automatically retry an uncertain write.
Lock existence requires inspection; the tool does not delete another writer's lock.
Prior decisions/doc snapshots/evidence entries are immutable: append a version.
Record the mode at each decision so a later mode change does not rewrite the
authority under which historical choices were made.
Preserve node/edge/path IDs and use supersession states/relationships rather
than deleting history. Cumulative spent and episode counters cannot decrease.
This is single-writer cooperation, not a multi-client database or an ACL.

Changes to scope, modes, budgets or scientific criteria still need their actual
authority basis. Tools validate recorded assertions, not human identity or
semantic sufficiency. They do not launch models or validate experiment outcomes.

The viewer accepts files up to 5 MiB, at most 500 nodes and 3,000 edges. These
are interface bounds, not evidence or scientific stopping rules. For a larger
program link a bounded sub-study rather than deleting history to satisfy a limit.
