# Artifact Schemas

These compact, runtime-neutral YAML shapes are contracts for reasoning and
handoff, not a required storage engine. Add fields when the approved experiment
needs them; do not silently omit fields that determine scope, isolation,
budget, or adoption. Keep sealed evidence and evaluator internals outside any
artifact visible to mutation work.

## Experiment Plan

Create this plan from explicit user context when provided; otherwise propose a
provenance-labeled interpretation from the conversation. It remains
`proposed` until the user approves it. Conversation examples do not become
evaluation truth or holdout data without explicit approval.

```yaml
schema: experiment-plan/v1
id: exp-short-label
status: proposed # proposed | approved | superseded | completed
context:
  source: user_provided # user_provided | conversation_inferred | workspace_observed | external_evidence
  inferred: false
  summary: "What context defines this investigation"
question: "The observable question"
problem_framing:
  restated_problem: "Observable condition, underlying goal, scope, constraints, and assumptions"
  observed_vs_inferred:
    observations: []
    inferred_causes: []
    proposed_solutions: []
    uncertainty_to_reduce: ""
  observable_invariant: "What must remain true for the user or product"
  explicit_constraints: []
  incumbent_assumptions: []
  alternative_mechanisms: []
  cheapest_discriminating_test: ""
  alignment_verdict: aligned # aligned | simplify_first | reframe | investigate_first
target:
  description: "What is investigated or improved"
  graph:
    nodes: [stage_a, stage_b]
    dependencies: ["stage_a -> stage_b"]
  mutable_surfaces: ["stage_a prompt"]
  frozen_surfaces: ["approved evaluator", "sealed cases"]
hypothesis:
  statement: "A falsifiable explanation"
  prediction: "Expected observable change under the mutation"
  disconfirming_result: "Outcome that counts against the prediction"
program:
  scope: single_experiment # single_experiment | research_program
  factor_axes: {}
  candidate_envelope: []
  amendment_triggers: [new_target, new_evidence, scoring_change, disclosure_change, material_budget_change]
evaluation:
  rigor: exploratory # exploratory | confirmatory
  experimental_unit: "one approved case-run paired across candidates"
  analysis_unit: "one distinct approved case"
  cluster_key: "case_id"
  distinct_clusters: 12
  repeats_within_cluster: 2
  effective_sample_basis: "distinct cases, with within-case repeats grouped"
  sampling_frame: "approved development cases"
  primary_criteria:
    - name: quality
      direction: maximize
      minimum_effect: null # required when the approved claim needs it
  guardrails:
    safety_or_validity_stops:
      - {name: unsafe_behavior, rule: "halt immediately"}
    adoption_gates:
      - {name: prohibited_regression, rule: "candidate remains ineligible; diagnostic evaluation may continue if approved"}
    diagnostic_flags:
      - {name: quality_gray_zone, rule: "collect approved additional evidence"}
  evaluator: "approved evaluator description"
  evaluator_readiness:
    evidence: "anchors, repeated controls, paired preference, or human review"
    decision_rule: "disagreement cannot reverse the minimum meaningful decision"
    failure_action: "calibrate, use a stronger evaluator, or limit the claim to exploratory diagnosis"
  repetitions: "planned units and repeats, or adaptive rule"
  uncertainty_method: "chosen after checking outcome and dependence"
  holdout: "none, or sealed final evidence"
  cost_dictionary: [wall_time, model_calls, evaluator_calls, input_units, output_units, retries, discarded_work, accepted_outputs]
measurement_semantics:
  - name: path_depth
    construct: "Distance from the approved root state"
    observable_proxy: "Number of traversed logical edges"
    unit: edges
    direction: descriptive
    conditions: "Measured on the approved logical graph before visual aggregation"
    provenance: workspace_observed
    aggregation_key: [display_token, path_depth]
    aggregation_rule: "Merge equal display tokens only at equal path depth"
    positive_example: "The same token observed twice at depth 2 is one displayed node"
    boundary_counterexample: "The same token at depth 2 and depth 3 remains two displayed nodes"
    missing_invalid_tie_gray_zone: "Missing depth is invalid and excluded with a count"
isolation:
  level: weak # weak | contextual | strong
  mutator_can_see: [goal, weakness_cards, strengths_to_preserve]
  hidden_from_mutator: [exact_evaluator_prompt, hidden_weights, item_answers, holdout]
experiment_graph:
  nodes:
    - id: validate_harness
      depends_on: []
    - id: minimal_real_run
      depends_on: [validate_harness]
    - id: validate_evaluator
      depends_on: [minimal_real_run]
    - id: screen_candidates
      depends_on: [validate_evaluator]
    - id: full_development
      depends_on: [screen_candidates]
    - id: confirm_whole_chain
      depends_on: [full_development]
execution:
  candidate_limit: 3
  budget: "approved time, calls, tokens, or cost"
  capacity_preflight:
    assumptions: ["branching estimate and average output length"]
    estimated_range:
      model_calls: "low..high"
      evaluator_calls: "low..high"
      wall_time: "low..high"
      memory: "low..high"
      disk_or_artifacts: "low..high"
    growth_shape: multiplicative # linear | multiplicative | combinatorial | unknown
    cumulative_across_resumes: "whole-program estimate"
    whole_program_caps: [max_total_expansions, max_model_calls, max_artifact_bytes]
    pilot_or_dry_run: "bounded run used when estimates are uncertain"
    checkpoint_or_retention: "how resumability and artifact growth are bounded"
    degradation_action: "pause, sample, segment, or request reapproval"
  stage_gates:
    - {stage: deterministic_validation, promotion: "harness and schema pass", failure: invalid}
    - {stage: minimal_real_run, promotion: "intended mechanism reached", failure: invalid}
    - {stage: cheap_screen, promotion: "approved screen criteria pass", failure: negative_or_ineligible}
    - {stage: full_development, promotion: "adoption candidate survives", failure: negative_or_inconclusive}
    - {stage: confirmation, promotion: "approved adoption evidence passes", failure: negative_or_inconclusive}
  loop_bounds:
    - node: screen_candidates
      max_iterations: 3
      max_cost: "approved bound"
      exit_condition: "operational success, futility, harm, or invalidity rule"
  stopping_policy:
    - scope: path # path | whole_investigation
      signal: "three consecutive candidates below the minimum useful effect"
      threshold: 3
      observation_window: "three completed comparable candidate evaluations"
      action: alternative_path_review # continue | pivot | pause_for_reapproval | stop
      outcome: "current path exhausted"
  alternative_path_review:
    required_before_whole_futility: true
    consider: [unresolved_hypotheses, other_mutable_stages, different_intervention_families, unblocked_branches]
    viability: [relevant, evidence_supported, non_duplicative, in_scope, affordable]
  product_validity_checkpoint:
    after: "approved number of candidate paths or one major mechanism result"
    question: "Is another proxy candidate more valuable than testing a downstream or whole-target risk?"
  adoption_rule: "guardrails first; then balanced or Pareto comparison"
approval:
  approved_by_user: false
  approved_at: null
  approved_scope_hash_or_summary: null
```

## Weakness Card

The diagnosis role creates this bounded handoff. It gives mutation work enough
information to address a weakness and preserve strengths without revealing
sealed scoring mechanics or item-level answers.

```yaml
schema: weakness-card/v1
id: weak-constraint-retention
observation:
  category: constraint_retention
  symptom: "Constraints are lost in longer contexts"
  frequency: "observed in several approved development units"
  severity: high
  affected_stage: stage_a
diagnosis:
  confidence: tentative # tentative | supported | unresolved
  possible_mechanism: "Constraints compete with unstructured context"
desired_direction: "Improve retention without adding unsupported content"
strengths_to_preserve: [accuracy, concise_output]
allowed_scope: ["stage_a prompt structure"]
excluded_information: [item_answers, exact_judge_prompt, hidden_weights, holdout]
evidence_reference: "non-sealed aggregate or redacted trace reference"
```

Do not present a possible mechanism as an observed fact. One weakness may
support several competing hypotheses and mutations.

## Experiment Ledger Entry

Append an entry for every successful, negative, null, inconclusive, or invalid
experiment. Preserve preregistered statements separately from interpretations
made after observing results.

```yaml
schema: experiment-ledger/v1
experiment_id: exp-short-label
run_id: run-001
plan_version: "approved plan reference"
candidate_ids: [incumbent, candidate_anon_b]
candidate_delta:
  parent_contract: exp-short-label
  factors: {prompt_structure: structured}
  intervention_delta: "Only what differs from the approved parent"
execution:
  started_at: "RFC3339 timestamp"
  completed_at: "RFC3339 timestamp"
  actual_units: 24
  actual_repeats: 2
  stage_reached: full_development
  analysis_unit: approved_case
  cluster_key: case_id
  distinct_clusters: 12
  effective_sample_size: "reported under the approved dependence model"
  cost:
    wall_time: ""
    model_calls: ""
    evaluator_calls: ""
    input_units: ""
    output_units: ""
    retries: ""
    discarded_work: ""
    accepted_outputs: ""
    comparability: comparable # comparable | partial | non_comparable
  deviations: []
path_result:
  path_id: prompt-structure
  status: exhausted # active | succeeded | exhausted | invalid
  reason: "Approved path-level stopping rule that fired"
alternative_path_review:
  alternatives_considered: [context-routing]
  decision: pivot # pivot | request_reapproval | stop_investigation
  rationale: "Why a viable branch remains or why none remains"
observations:
  primary_effect: "estimate with unit and direction"
  uncertainty: "interval, posterior, or other approved summary"
  dispersion: "case/run/evaluator variation summary"
  guardrails:
    safety_or_validity_stops: "pass, fail, or uncertain"
    adoption_gates: "eligible or ineligible per gate"
    diagnostic_flags: "clear, gray-zone, or triggered"
  cost: "latency, tokens, calls, or money when approved"
  missing_invalid: "counts and reasons"
inference:
  epistemic_state: exploratory_signal # confirmed | likely | exploratory_signal | no_meaningful_change | inconclusive | negative | invalid
  hypothesis_status: unresolved # supported | challenged | unresolved | not_tested
  interpretation: "What the observations support and do not support"
unknowns: ["What remains unresolved"]
decision:
  status: hold # recommend | hold | reject | invalid
  reason: "Rule and evidence behind the status"
next_tests: ["A bounded follow-up, or none"]
```

## Candidate Decision

Use anonymized candidate IDs during evaluation where feasible. Apply
guardrails before ranking. Keep non-dominated alternatives when values trade
off, and ask the user to make the final adoption choice.

```yaml
schema: candidate-decision/v1
experiment_id: exp-short-label
incumbent_id: incumbent
eligible_candidates:
  - id: candidate_anon_b
    epistemic_state: likely
    effects:
      quality: "+5 percentage points"
      concision: "+2 percentage points"
      cost: "no material change"
    uncertainty: "approved comparison summary"
    guardrails: pass
    pareto_status: non_dominated
ineligible_candidates:
  - id: candidate_anon_c
    reason: "approved adoption gate failed; diagnostic evidence remains labeled"
recommendation:
  balanced_default: candidate_anon_b
  rationale: "Improves major criteria together with no prohibited regression"
  alternatives: []
  user_choice_required: true
adoption:
  selected_by_user: null
  selected_at: null
  required_follow_up: "whole-chain or post-adoption check, if approved"
```

If evidence cannot distinguish candidates, keep the decision unresolved. Do
not force a winner, average away a prohibited regression, or translate
`inconclusive` into `no change`.
