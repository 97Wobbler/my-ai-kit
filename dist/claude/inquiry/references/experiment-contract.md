# Experiment Contract

Use this contract to turn the current request into an approval-ready scientific
investigation. It applies to prompts, skills, agent chains, loops, graphs, and
their routing, retrieval, context, evaluation, and post-processing harnesses.
Keep the contract proportional to the work: a small prompt experiment can be a
short checklist, while a dependent product graph needs explicit nodes and
dependencies.

## Resolve The Target And Context

Choose the target with this precedence:

1. Use the target, artifact, and context the user explicitly supplies.
2. Resolve direct references such as "this skill" or "the chain above" against
   the current conversation.
3. If no target is explicit, infer the strongest candidate from the current
   conversation and present it as a proposal.
4. If competing interpretations would materially change scope, cost, scoring,
   or the experiment design, ask the user instead of silently choosing.

Explicit user direction overrides inferred context. Do not broaden an explicit
target merely because related artifacts are visible. Conversation examples can
motivate a target, weakness, or scoring proposal, but they do not become
evaluation truth, test cases, or holdout evidence without approval.

Label material context with one of these provenance values:

- `user_explicit`: directly supplied or confirmed by the user;
- `conversation_inferred`: inferred from the current conversation;
- `workspace_observed`: read from the target or its surrounding workspace;
- `external_evidence`: obtained from an identified external source;
- `experiment_observed`: produced by an approved experiment.

For inferred claims, record the inference and its supporting context separately.
An inference becomes approved contract content only when the user approves the
plan; it does not become historical fact or evaluation evidence by approval
alone.

## Align The Problem And Direction Before Designing The Experiment

Perform one compact preflight that combines three questions without requiring
another skill dependency or a separate approval ceremony:

1. **Restate:** What was observed, what outcome does the user or product need,
   what is in scope, and which constraints or assumptions matter?
2. **XY check:** Which parts are observations, inferred causes, and proposed
   solutions? What uncertainty must actually be reduced, and does the proposed
   experiment test it?
3. **Efficiency check:** Is there a simpler, safer, or structurally different
   test that yields more useful information per unit of cost, time, and risk?

Record the verdict as `aligned`, `simplify_first`, `reframe`, or
`investigate_first`. If the answer materially changes the target, goal, or
allowed direction, resolve that decision with the user before completing the
contract. Otherwise carry the result into the contract and keep one approval
boundary.

Separate the observable goal from the incumbent mechanism. Record the user- or
product-visible invariant, explicitly frozen implementation constraints, and
implementation details that are merely current assumptions. When evidence
supports one, include at least one materially different mechanism and the
smallest comparison that can distinguish the leading mechanisms.

Rank first tests by expected learning value relative to cost and risk. Do not
automatically begin with the mutation closest to the current code. If only the
incumbent mechanism is allowed, state that constraint and which questions it
prevents the experiment from answering. Alternatives must remain relevant,
testable, and consistent with explicit user constraints.

## Frame The Scientific Question

Do not collapse investigation into a proposed edit. Record these elements
before execution:

- **Observation:** what was seen, under which conditions, and from which
  provenance-labeled evidence.
- **Question:** the uncertainty the experiment should reduce.
- **Hypothesis:** a falsifiable explanation of the observation.
- **Prediction:** what measurable difference should occur if the hypothesis is
  useful, including its expected direction and affected criteria.
- **Intervention:** the bounded mutation or comparison that tests the
  prediction. List mutable and frozen surfaces.
- **Falsification condition:** a result that would disconfirm the prediction or
  leave the hypothesis unresolved. Include prohibited regressions.

An unsuccessful intervention does not automatically falsify its underlying
hypothesis. Record whether the result supports, challenges, or leaves the
hypothesis unresolved, and distinguish an invalid experiment from a negative
result.

## Keep The Two Graphs Separate

The **target graph** describes the system under study: relevant prompts, skills,
agents, loops, routing, retrieval, context, evaluators, post-processing stages,
and their data or control dependencies. Mark the proposed change boundary and
the stages whose behavior must remain stable.

The **experiment graph** describes the investigation: hypotheses,
interventions, measurements, comparisons, validation steps, and their
prerequisites. For example, evaluator stability may need validation before
candidate comparison, and partial-stage screening may precede whole-chain
confirmation.

Do not treat a locally improved target node as a whole-system improvement.
State how surviving partial candidates will be checked against downstream and
whole-chain outcomes.

For connected experiments, define a **research program contract** rather than
starting a new top-level contract for every candidate. It may preapprove factor
axes, candidate families, mutable surfaces, development evidence, total budget,
and stage gates. Candidate runs and bounded harness repairs inside that
envelope are ledger entries. Require an amendment or new approval only when the
target, evidence, scoring, disclosure, mutation boundary, dependency, material
budget, or adoption rule changes.

Keep child records compact: reference the approved parent and record only the
candidate's factor values, intervention delta, stage, evidence, and decision.
Do not restate the entire program contract for each candidate.

Add a product-validity checkpoint to a longer program. Fix when the program
will reconsider whether another proxy candidate is more valuable than testing
an unresolved downstream, integration, or whole-target risk.

## Propose And Confirm Scoring

If the user supplies a score or rubric, preserve it and surface ambiguities. If
the user asks only for improvement or does not know how to score it, infer a
proposal from the goal and context. The proposal must identify:

- primary criteria and whether higher or lower is better;
- strengths to preserve and guardrail thresholds;
- observation and analysis units, cluster key, distinct clusters, repeats
  within cluster, effective sample basis, evidence set, evaluator, and
  aggregation;
- cost, latency, or complexity constraints when relevant;
- exploratory or confirmatory rigor;
- adoption rule, including how ties and non-dominated alternatives are handled.

Mark proposed criteria and weights as `conversation_inferred` until approved.
Do not hide a major-criterion regression inside an aggregate score. Prefer
balanced improvement across major criteria; retain Pareto alternatives when no
candidate dominates, and leave the final value trade-off to the user.

For exploratory work, a bounded repeated comparison and an uncertainty label
may be sufficient. For a specific or high-confidence claim, propose an
appropriate minimum effect, sample plan, interval or sequential method, and
sealed confirmation. Never treat one stochastic score increase as established
improvement.

Define evaluator readiness before candidate comparison. State the controls,
anchors, repeated judgments, paired preferences, human review, or other
evidence used to show that evaluator variation is small enough for the
decision. If disagreement can reverse the minimum meaningful effect, pause for
calibration or restrict the result to exploratory diagnosis.

Classify every guardrail as one of:

- `safety_or_validity_stop`: halt because continued work is unsafe or cannot
  answer the question;
- `adoption_gate`: exclude the candidate from adoption while allowing safe,
  approved diagnostic measurement;
- `diagnostic_flag`: record a concern or gray zone without deciding
  eligibility alone.

For noisy quality measures, prefer pass, gray-zone, and fail regions with an
approved additional-sampling rule. Use zero-tolerance thresholds only for
requirements that are genuinely absolute.

## Validate Measurement Meaning

Operationalize every decision-relevant metric, graph dimension, and
qualitative judgment. Record:

- construct and observable proxy;
- unit, direction, conditions, and evidence provenance;
- aggregation key and rule, including dependence or clustering;
- a concrete positive example and boundary counterexample;
- missing, invalid, tied, and gray-zone behavior.

Validate ambiguous meanings with a small fixture, trace, rendered artifact, or
worked example before mutation. Terms such as `generation`, `depth`,
`quality`, and `success` are labels, not definitions. If a measurement cannot
distinguish the mechanisms or candidates under study, repair the measurement
or reframe the question before spending comparison budget.

## Run A Capacity Preflight

Before approving execution, estimate a plausible range and state assumptions
for model and evaluator calls, branch or state growth, input and output units,
wall time, memory, disk or artifact growth, retries, external quotas, and
cumulative work across resumed runs. Inspect the whole experiment graph for
multiplicative or combinatorial growth. Do not mistake a per-run limit for a
whole-program bound.

When uncertainty is material, first run a bounded pilot or instrumented dry
run and use it to set observable hard caps, checkpoint or retention policy,
and a degradation action. Prefer ranges to false precision. If no feasible
capacity envelope can produce a meaningful observation, simplify or segment
the design, or ask the user to approve a material budget change.

## Stage Execution Before Full Comparison

Use a staged funnel appropriate to the target:

1. deterministic harness, schema, or fake-model validation;
2. tokenizer, template, interface, or tool inspection;
3. one minimal real execution;
4. a cheap screen across distinct cases and limited repeats;
5. full development comparison for survivors;
6. diagnostic evaluation, including ineligible candidates when safe and useful;
7. stronger or sealed survivor confirmation;
8. whole-target or product-validity confirmation.

For each applicable stage, define its budget, promotion rule, failure state,
and artifact. A harness failure is `invalid`, not negative hypothesis evidence.
Do not spend a full comparison block before the candidate has demonstrated
that it reaches the intended mechanism. Record why any stage is skipped.

Before execution, define a common cost dictionary for incumbent and candidates.
Prefer wall time, actual model or evaluator calls, input and output units,
retries, discarded work, accepted outputs, and cost per accepted output. If a
metric cannot be measured symmetrically, mark it non-comparable and do not use
it for a precise ratio.

## Fix Budget, Dependencies, And Stopping

State the budget in observable units such as candidate count, evaluator calls,
tokens, time, or monetary cost. Record experiment-graph dependencies and define
stopping rules before execution. Make every rule operational by naming its
signal, threshold, observation window, action, and resulting epistemic state.
Give every repeated experiment-graph node a maximum iteration or resource
bound and an exit condition.

Cover at least:

- budget exhaustion;
- sufficient evidence for the approved adoption rule;
- futility or repeated non-improvement;
- guardrail failure or unsafe behavior;
- evaluator instability, contamination, or unavailable isolation;
- a prerequisite failure that invalidates downstream experiments;
- user-requested stop.

Separate a **path stop** from a **whole-investigation stop**. Repeated
non-improvement normally exhausts the current hypothesis, target stage, or
intervention family. It does not establish that every useful route is
exhausted. Before whole-investigation futility, review untested or unresolved
hypotheses, other approved target stages, materially different interventions,
and unblocked experiment-graph branches. A viable alternative must be relevant
to the approved goal, supported enough to test, non-duplicative, permitted by
the mutation boundary, and affordable enough for a meaningful observation.

Pivot to a viable alternative already inside the approved contract. Pause for
reapproval when the alternative needs a new target, mutation surface, evidence
source, disclosure boundary, dependency, or material budget. Stop the whole
investigation only when an overall stop applies or no viable alternative
remains. Do not keep generating speculative alternatives merely to avoid a
null result.

Stopping without a winner is valid. Report `no change`, `inconclusive`, or
`invalid` when that is what the evidence supports, and record which paths were
exhausted and which alternatives were considered.

## Approval Boundary

Present the completed contract and experiment graph to the user before any
mutation or evaluation. Approval must cover the target interpretation,
objective, scoring and guardrails, mutable and frozen surfaces, evidence and
observation unit, information boundaries, budget, dependencies, stopping rule,
and adoption rule.

Do not create candidates, alter the target, run baseline or candidate
evaluations, or spend the experiment budget before approval. Read-only
inspection needed to draft the plan is allowed, but label its observations and
do not promote them to evaluation evidence without approval.

After approval, execute only within the agreed contract. Pause for renewed
approval if a new target, criterion, evidence source, mutation surface,
dependency, material budget increase, disclosure change, or adoption rule is
needed. Ordinary execution details that do not change the contract do not
require another approval.

## Compact Contract Shape

```yaml
target:
  description: ""
  provenance: user_explicit | conversation_inferred
  context_sources: []
  target_graph: []
problem_framing:
  restated_problem: ""
  observed_vs_inferred: []
  observable_invariant: ""
  explicit_constraints: []
  incumbent_assumptions: []
  alternative_mechanisms: []
  cheapest_discriminating_test: ""
  alignment_verdict: aligned | simplify_first | reframe | investigate_first
question: ""
observation:
  statement: ""
  provenance: ""
hypothesis: ""
prediction: ""
falsification_condition: ""
intervention:
  mutable_surfaces: []
  frozen_surfaces: []
program:
  scope: single_experiment | research_program
  factor_axes: {}
  candidate_envelope: []
  amendment_triggers: []
evaluation:
  rigor: exploratory | confirmatory
  primary_criteria: []
  guardrails:
    safety_or_validity_stops: []
    adoption_gates: []
    diagnostic_flags: []
  observation_unit: ""
  analysis_unit: ""
  cluster_key: ""
  distinct_clusters: ""
  repeats_within_cluster: ""
  effective_sample_basis: ""
  evidence: []
  evaluator: ""
  evaluator_readiness: ""
  repetitions: ""
  cost_dictionary: []
  adoption_rule: ""
measurement_semantics:
  - name: ""
    construct: ""
    observable_proxy: ""
    unit: ""
    direction: ""
    conditions: ""
    provenance: ""
    aggregation_key: ""
    aggregation_rule: ""
    positive_example: ""
    boundary_counterexample: ""
    missing_invalid_tie_gray_zone: ""
information_boundaries:
  mutation_visible: []
  mutation_hidden: []
experiment_graph: []
execution:
  contract_scope: single_experiment | research_program
  candidate_envelope: []
  stage_gates: []
  budget: ""
  loop_bounds: []
  capacity_preflight:
    assumptions: []
    estimated_range: {}
    growth_shape: linear | multiplicative | combinatorial | unknown
    whole_program_caps: []
    pilot_or_dry_run: ""
    checkpoint_or_retention: ""
    degradation_action: ""
  stopping_rules:
    - scope: path | whole_investigation
      signal: ""
      threshold: ""
      observation_window: ""
      action: continue | pivot | pause_for_reapproval | stop
      outcome: ""
  alternative_path_review:
    required_before_whole_futility: true
    viability_criteria: [relevant, evidence_supported, non_duplicative, in_scope, affordable]
  product_validity_checkpoint: ""
  dependencies: []
approval:
  status: proposed | approved
  approved_scope: ""
```
