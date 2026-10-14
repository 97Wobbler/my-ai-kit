# Strategy, Goals, and Purpose Reviews

Start with the observable user/product outcome, not the current implementation.
Keep multiple goals when appropriate; quantitative and qualitative success are
both valid. For goals record hierarchy, success criterion, priority, and whether
the goal is mandatory. Do not invent weights to hide quality/cost conflicts.

A milestone is an intermediate outcome, while a hypothesis is an uncertain
claim with predictions and conditions. "Usable images" is a milestone;
"reference images preserve shape" is a hypothesis. Several hypotheses can
support one milestone, and A-prime may replace A while preserving B–C–D.
Failure of A can block the current route without refuting B itself.

Before choosing a next experiment, answer:

1. Which important whole-goal uncertainty will this reduce?
2. Will different results change the next action?
3. Is refining this path more valuable than an alternative or downstream test?
4. What provisional sufficiency, cost and stopping criteria make this practical?

Compare cost among paths plausibly meeting the goal and mandatory conditions.
Start with a promising path or test independent paths in parallel inside the
same total budget. Weak cost/likelihood estimates should stay qualitative and
uncertain. Cheap but irrelevant paths are not optimal.

Use purpose, evidence/inference, and path/cost perspectives where useful.
At milestones, repeated failure, major strategy shifts or changed criteria,
give an independent reviewer current goals, selected paths, significant unknowns,
remaining budget and the latest decisions. Ask:

- Is this local problem important to the whole goal?
- Is evidence already practically sufficient to proceed?
- Would another path or the next milestone be more valuable?
- Are cost and stopping rules still respected?

Keep a purpose-review role available across relevant work, but reload files
instead of trusting long conversational memory. A fresh perspective may help
at a major pivot; do not require a new reviewer or review every model call.
If runtime/authority prevents delegation, disclose the host-only fallback.

Reviewers submit bounded artifacts; the main agent checks evidence,
counterexamples and applicability, then records accepted/rejected/deferred
opinions and reasons. Main owns total budget and final integration. Workers
do not all write the canonical file. Role separation alone is not secure
evaluator isolation; use `evaluation-and-isolation.md` for controlled comparisons.

Borrow useful elements of goal pathways/connection assumptions, sequential
experimentation, information value, exploratory vs confirmatory claims, and
alternative explanations. Do not impose one research school or statistical
confidence number on every problem. Interim criteria may adapt, but preserve
the original prediction, old/new criteria, and reason. For quantitative claims
read `stochastic-comparison.md`; fixed-sample intervals and repeated favorable
stopping cannot be treated as the same design merely by logging changes.

Success is less aimless refinement and more inspectable, useful next decisions.
Node counts, experiment counts, and pivot counts are not success metrics.
Observe actual user intervention and sufficient proceed/stop decisions during
longer dogfood; a well-rendered retrospective graph alone is not that evidence.
