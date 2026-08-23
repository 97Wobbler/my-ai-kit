---
name: "experiment"
description: "Investigate and improve nondeterministic LLM prompts, skills, agent chains, loops, graphs, or evaluation and routing harnesses with an approval-gated scientific experiment. Use when the user asks to research why an LLM workflow behaves as it does, improve it through measured variants, compare stochastic candidates, optimize a prompt or agent workflow without overfitting its evaluator, or design and run a controlled experiment. Do not use for ordinary deterministic program or command optimization, a one-off edit with no investigation or comparison requested, or claims of causal certainty from an uncontrolled test."
---

# Experiment

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `experiment.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Use Claude Code's native blocking question flow when clarification is required.
- Follow repository edit instructions and preserve unrelated user changes.
- Delegate only when the runtime supports subagents and the task can run safely in parallel.
- Use network access only when current or external facts are required.
- Run the relevant validation checks before reporting completion.

## Purpose

Apply scientific-method discipline to investigating and improving a
nondeterministic LLM workflow. Keep the method portable across small prompts
and skills, agent chains, loops, dependency graphs, and their routing,
retrieval, context, evaluation, and post-processing harnesses. Scale the rigor
to the decision; do not turn the skill into a catalog of domain recipes.

Investigation is a valid outcome. Do not force an intervention when evidence
does not justify one, and do not claim causal certainty merely because an
experiment used scientific techniques.

## Resolve References

Resolve the installed Inquiry package root by walking upward from the
directory containing this `SKILL.md` until a directory contains all of:

```text
references/experiment-contract.md
references/evaluation-and-isolation.md
references/stochastic-comparison.md
references/artifact-schemas.md
```

Read references progressively:

- read `references/experiment-contract.md` while framing and approving work;
- read `references/evaluation-and-isolation.md` before designing disclosure,
  diagnosis, mutation, or evaluation roles;
- read `references/stochastic-comparison.md` before fixing the comparison
  design or analyzing results;
- read `references/artifact-schemas.md` only when drafting, recording, or
  handing off structured artifacts.

Do not assume a private source-checkout path or a particular runtime cache.

## Workflow

### 1. Resolve the target and provenance

Use an explicit user-supplied target and context first. Resolve references such
as "this skill" or "the chain above" from the current conversation. If no
target is explicit, infer the strongest candidate from the current
conversation and present it as a proposal. Label material context as
user-provided, conversation-inferred, workspace-observed, external evidence,
or experiment-observed.

Ask only when competing interpretations would materially change scope, cost,
scoring, or experiment design. Never broaden an explicit target silently.
Conversation examples may motivate hypotheses or scoring proposals, but do not
become evaluation truth, test cases, or holdout evidence without approval.

### 2. Align the problem and experiment direction

Before investigating or optimizing the current mechanism, perform a compact
problem-alignment check. Borrow the useful reasoning of restatement, XY
checking, and elegance review without requiring another skill or a second
approval ceremony:

- **Restate:** state the observed condition, underlying user or product goal,
  scope, constraints, and material assumptions in concrete language.
- **XY check:** separate observed evidence from inferred causes and proposed
  solutions. Name the uncertainty the experiment must reduce and verify that
  the proposed intervention actually tests it.
- **Efficiency check:** compare the current direction with a simpler or
  structurally different route. Prefer the smallest safe test with the highest
  expected learning value relative to cost, risk, and time.

Separate the user's observable goal and invariants from the implementation
that happens to produce them. Ask:

- what outcome must remain true from the user's or product's perspective;
- which current mechanisms are genuine constraints and which are assumptions;
- whether a simpler or structurally different mechanism can satisfy the same
  invariant;
- which smallest comparison would discriminate between those mechanisms.

Propose at least one materially different mechanism when evidence supports
one. Prefer the test with the highest expected learning value for its cost,
not the mutation closest to the incumbent implementation. If the user has
explicitly frozen a mechanism, preserve it, but make the resulting limitation
visible. Do not turn this checkpoint into generic brainstorming: alternatives
must be relevant, testable, and consistent with explicit constraints.

Record one alignment verdict: `aligned`, `simplify_first`, `reframe`, or
`investigate_first`. When the check changes the target, goal, or allowed
direction materially, resolve that choice with the user before completing the
contract. Otherwise include the check in the approval-ready contract and use
the existing single approval boundary.

### 3. Investigate before intervening

Inspect the target and available evidence without altering or evaluating it.
Separate:

- observations and their conditions;
- the observable question;
- falsifiable hypotheses;
- predictions and disconfirming results;
- proposed interventions with mutable and frozen surfaces.

Distinguish symptoms from possible mechanisms. A failed mutation does not by
itself falsify every mechanism behind a hypothesis. If the evidence supports
no useful intervention, propose further investigation or a null conclusion.

### 4. Propose and confirm goals and scoring

Preserve user-supplied goals, scores, and rubrics while surfacing ambiguities.
If the user asks only for something to be "better" or does not know how to
score it, propose criteria from the proposed target and context. Include the
primary criteria, their directions, strengths to preserve, prohibited
regressions, observation unit, cluster or dependence structure, evidence
source, evaluator, repetitions, comparable cost accounting, and adoption rule.

Classify guardrails before execution:

- **safety or validity stops** halt unsafe or uninterpretable work;
- **adoption gates** make a candidate ineligible but may still permit safe,
  budgeted diagnostic measurement;
- **diagnostic flags** annotate a weakness or gray zone without deciding
  eligibility by themselves.

Define evaluator-readiness evidence before candidate comparison. If evaluator
variation can reverse the minimum meaningful decision, calibrate with anchors,
paired preference, repeated controls, human review, or another approved method;
otherwise limit the claim to exploratory diagnosis. Use indifference or gray
zones for noisy quality criteria when a hard threshold would let one or two
observations flip the decision. Reserve zero-tolerance rules for genuinely
absolute safety, validity, or user requirements.

Operationalize every decision-relevant measure before execution. For each
metric, graph dimension, or qualitative judgment, define:

- the construct it represents and the observable signal used as its proxy;
- unit, direction, observation conditions, and evidence provenance;
- aggregation key and rule, including cluster or dependence handling;
- one concrete example and one counterexample at ambiguous boundaries;
- missing, invalid, tied, and gray-zone handling.

Use a small fixture, trace, rendered artifact, or worked example to validate
the semantics when an incorrect grouping or interpretation could change the
experiment or implementation. A label such as "generation", "depth",
"quality", or "success" is not an operational definition. If the measurement
cannot distinguish the approved alternatives, revise it before candidate
comparison rather than collecting precise-looking but irrelevant scores.

Recommend lightweight exploratory rigor for directional improvement with low
decision risk. Recommend confirmatory rigor for a specific improvement claim,
a consequential adoption, or a requested confidence level. Confirmation may
require a minimum meaningful effect, an appropriate interval or sequential
design, multiplicity handling, and sealed final evidence. Explain rigor as a
trade-off among cost, speed, and warranted confidence instead of requiring the
user to choose statistical jargon.

### 5. Choose the contract scope and map both graphs

For one bounded question, use one experiment contract. For a connected series
of hypotheses or factor combinations, prefer one **research program contract**
with a preapproved candidate envelope, factor axes, total budget, stage gates,
and explicit reapproval triggers. Do not create a new top-level contract for
every candidate when it stays inside that envelope. Record each candidate and
path as a compact parent reference plus its factor values and deltas; do not
copy the full parent contract. Use a contract amendment only when approved
scope actually changes.

Map the **target graph** as the workflow under study, including relevant stages
and dependencies. Mark the change boundary and downstream behavior that must
remain stable.

Map the **experiment graph** separately as hypotheses, interventions,
measurements, comparisons, validation steps, and prerequisites. Choose among
whole-chain, segmented, bottleneck-first, or partial-screening-then-whole-chain
designs according to observability, dependency, cost, and downstream
sensitivity. Do not infer whole-system improvement from a local-stage score;
plan whole-chain confirmation whenever adoption affects the product outcome.
Identify plausible alternative hypothesis, target-stage, and intervention
branches so exhausting one branch does not silently terminate the whole
investigation.

Run a capacity preflight over the proposed experiment graph before approval.
Estimate a plausible range, with assumptions, for model and evaluator calls,
branch or state growth, input and output units, wall time, memory, disk or
artifact growth, retries, external quotas, and cumulative work across resumed
runs. Detect multiplicative or combinatorial growth rather than extrapolating
only one loop in isolation. Distinguish per-run limits from whole-program
limits such as cumulative expansions or total retained artifacts.

Use a bounded pilot or instrumented dry run when the estimate is too uncertain
to support the requested scale. Set hard observable caps and a degradation or
checkpoint strategy before a large run. Report ranges and unknowns instead of
inventing false precision. If the approved question cannot receive a
meaningful observation within the feasible envelope, simplify, segment, or
request a material budget decision before execution.

Include a product-validity checkpoint in longer programs: after the approved
number of candidate paths or a major mechanism result, verify that the next
experiment still reduces an important uncertainty in the full target graph.
Do not indefinitely optimize a local proxy while a more consequential product
or integration risk remains untested.

### 6. Present the experiment contract and stop

Present an approval-ready contract containing:

- target interpretation, provenance, target graph, and observable question;
- problem-alignment verdict and its restatement, XY, and efficiency checks;
- observation, hypothesis, prediction, intervention, and disconfirming result;
- mutable and frozen surfaces;
- criteria, guardrails, experimental unit, evidence, evaluator, repetitions,
  measurement semantics, uncertainty method, and any holdout;
- achieved information boundary and known leakage channels;
- contract scope and any preapproved factor or candidate envelope;
- experiment graph, staged execution gates, dependencies, per-loop bounds,
  capacity preflight, whole-program bounds, operational stopping rules,
  alternative-path review, and adoption rule.

Mark inferred assumptions and proposed scores explicitly. **Stop after
presenting the contract. Do not create candidates, alter the target, run a
baseline, run an evaluator, or spend experiment budget until the user approves
the contract.** Approval must be an explicit user response, not inferred from
the original request.

If approval changes the target, evidence, scoring, disclosure, mutation scope,
material budget, dependencies, or adoption rule, revise the contract and ask
again. Candidate additions, harness repairs, and execution details already
inside an approved research-program envelope do not require a new top-level
contract; record them and remain within their stage and budget limits. After
approval, execute only the approved scope.

### 7. Execute through staged gates

Use the cheapest stage that can invalidate a candidate before spending the
full experiment budget. Unless a stage is genuinely inapplicable, progress
through:

1. deterministic harness, schema, or fake-model checks;
2. tokenizer, prompt-template, tool, or interface inspection where relevant;
3. one minimal real execution that proves the candidate reaches the intended
   mechanism;
4. a small development screen across distinct cases and a few repeats;
5. the full approved development comparison only for survivors;
6. diagnostic evaluation, including ineligible candidates when it is safe,
   useful, and approved;
7. sealed or otherwise stronger confirmation for adoption candidates;
8. whole-target or product-validity confirmation when local results are not
   sufficient.

Define promotion and failure rules for every stage. A failed harness check is
`invalid`, not negative evidence about the hypothesis. Do not start a full
block merely because it fits the total budget. If a stage is skipped, record
why it could not reduce risk or cost.

### 8. Execute with bounded role separation

Separate planning, diagnosis, mutation, evaluation, and adjudication roles to
the degree the approved environment supports. Give mutation work the goal,
public criteria, weakness cards, strengths to preserve, allowed surfaces, and
cost limits. Withhold exact evaluator instructions, hidden weights, item-level
answers, candidate identity signals, and sealed evidence where feasible.

Use weakness cards to communicate aggregate symptoms and desired direction
without teaching hidden cases. Anonymize frozen candidates and randomize or
counterbalance their evaluation order when feasible. Hold approved inputs,
budgets, tools, and conditions comparable, and record deviations.

Name the achieved boundary accurately: procedural blindness, context
isolation, or technically enforced secrecy. Different role labels in one
context are only procedural blindness. Never describe prompt-only separation
as secure or sealed. If the approved isolation cannot be achieved, disclose
the degraded boundary and pause for renewed approval when it materially
changes the contract.

### 9. Compare stochastic evidence

Define what one independent observation means. Distinguish different cases
from repeated runs of one case, and do not count correlated retries, turns, or
judge calls as independent without grouping or modeling that dependence.
Name the analysis unit, cluster key, distinct-cluster count, repeats within
cluster, and effective sample basis before analysis. Treat a mismatch between
the approved dependence structure and the analysis as a protocol error rather
than silently applying an independent-sample method.

Prefer paired, balanced comparisons on the same approved units when valid.
Measure effect magnitude, uncertainty, dispersion, evaluator variation,
missing or invalid runs, guardrails, and approved costs rather than only the
mean. Follow the preapproved sequential and stopping rules; do not repeatedly
peek at an ordinary fixed-sample test and stop on a favorable result.

Use the same cost definitions for incumbent and candidates: record wall time,
actual model or evaluator calls, prompt and generated units when available,
retries, discarded work, and cost per accepted output. If instrumentation is
not comparable, report only conclusions supported by the common measurements
and do not present a precise ratio from unlike counters.

Validate partial-stage survivors on the whole target graph when downstream
behavior matters. Quarantine contaminated or protocol-invalid evidence rather
than silently lowering the standard after results are known.

### 10. Review progress and dead ends before ending the investigation

Treat repeated failure or futility as exhaustion of the **current experiment
path**, not proof that the entire improvement space is exhausted. Before a
futility decision ends the whole investigation, perform an alternative-path
review over:

- untested or unresolved hypotheses supported by current evidence;
- other approved mutable stages or bottlenecks in the target graph;
- materially different intervention families, not cosmetic variants of the
  failed approach;
- experiment-graph branches unblocked by completed results;
- the evidence, isolation, and remaining budget needed for a meaningful test.

Continue with a viable alternative already covered by the approved contract.
If the best alternative changes scope, evidence, disclosure, dependencies, or
material budget, pause and request a revised contract. End the whole
investigation for futility only when no relevant, non-duplicative, feasible
alternative remains within the overall stopping policy. Do not prolong work by
inventing unsupported possibilities merely to avoid a null result.

Record each exhausted path, why it failed, what alternatives were reviewed,
and whether the result caused a pivot, reapproval request, or whole-
investigation stop.

At the approved product-validity checkpoint, also review whether continued
proxy improvement is more valuable than testing an unresolved downstream,
integration, or whole-graph risk. A pivot to that risk is not failure; it is a
better allocation of the remaining research budget.

### 11. Analyze, record, and recommend

Apply guardrails before ranking candidates. Use one calibrated epistemic
state: `confirmed`, `likely`, `exploratory_signal`,
`no_meaningful_change`, `inconclusive`, `negative`, or `invalid`. Separate
observations, inferences, unknowns, and next tests, and state what evidence
would change the conclusion.

An adoption-gate failure prevents recommendation but does not erase diagnostic
learning. When safe and approved, report both the full candidate evidence and
the eligible subset, keeping the candidate ineligible. A safety or validity
stop still takes precedence and may prohibit further measurement.

Record every successful, negative, null, inconclusive, and invalid experiment
in the ledger. Preserve preregistered predictions separately from post-result
interpretation so failed paths remain reusable knowledge.

Among eligible candidates, recommend the option that improves major criteria
together without a prohibited regression. If candidates trade off, retain the
non-dominated Pareto set, explain each trade-off, recommend a balanced default,
and ask the user for the final adoption choice. Do not force a winner when the
evidence is inconclusive and do not adopt or overwrite the incumbent without
the user's choice.

## Operational Rules

- Keep the experiment proportional: the smallest design that can answer the
  approved question is preferred.
- Treat the experiment contract as the scope and cost boundary, not as
  optional documentation.
- Preserve unrelated user work and never use destructive rollback as a
  generic candidate-management strategy.
- Keep sealed evidence and evaluator internals outside artifacts visible to
  mutation work.
- Report protocol deviations, leakage risk, evaluator instability, and weak
  isolation as limitations on the conclusion.
- `No meaningful change`, `inconclusive`, `negative`, and `invalid` are valid
  outcomes, not reasons to invent a winner.
- A path-level dead end is not a whole-investigation stopping condition until
  the required alternative-path review finds no viable approved branch.
- Run the validations required by the approved target and experiment contract
  before reporting completion.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Use the runtime's native blocking-question flow for experiment-contract approval when available. Use fresh, separate agent contexts for mutator, evaluator, or adjudicator roles only when the approved design benefits from context isolation and the runtime supports it; otherwise report procedural blindness and its limitations.
