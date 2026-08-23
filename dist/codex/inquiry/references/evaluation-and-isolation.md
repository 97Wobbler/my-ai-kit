# Evaluation and Isolation

Use information boundaries to make mutation purposeful without letting it optimize directly against evaluator internals. Isolation reduces leakage and rubric overfitting; it does not prove that an evaluator is valid or that a result generalizes.

## Choose and Report the Isolation Level

Distinguish these levels explicitly in the experiment contract and result:

- **Procedural blindness:** roles receive different instructions or context views, but run in the same session or in an environment where prior content may already be known. This is useful process discipline, not enforced secrecy.
- **Context isolation:** mutator and evaluator run in fresh, separate contexts with only their declared inputs. This limits accidental carryover, but shared files, logs, tools, or operator messages can still leak information.
- **Enforced secrecy:** access controls or separate environments prevent the mutator from reading sealed evidence, evaluator instructions, item-level results, and hidden weights. Claim this only when the boundary is technically enforced and checked.

Never describe prompt-only role separation as secure, sealed, or strongly isolated. If the requested level is unavailable, name the achieved level, list the exposed channels, explain how confidence is reduced, and let the user approve the degraded design before execution.

## Disclosure by Role

Apply least disclosure while giving each role enough information to do its job.

| Role | May receive | Withhold where feasible |
|---|---|---|
| Planner | target and experiment graphs, user goal, candidate evaluation dimensions, budget, dependencies, proposed boundaries | sealed items and answers unless needed to construct the evaluation; final hidden weights need not be exposed |
| Diagnostician | baseline outputs, criterion-level patterns, stage traces needed for attribution, strengths and failures | mutation proposals; unnecessary item answers; sealed confirmation set |
| Mutator | approved target, mutable and frozen surfaces, weakness cards, strengths to preserve, public criteria, cost limits | exact evaluator prompts, hidden weights and thresholds, item-level scores or answers, candidate identities during evaluation, sealed holdouts |
| Evaluator | approved rubric and evidence, anonymized candidate outputs, guardrails, repetition protocol | candidate authorship, mutation rationale and expected winner, prior rankings when not required |
| Adjudicator | anonymized measurements, uncertainty, guardrail results, cost and complexity, protocol deviations | candidate identity until the recommendation is formed; do not expose mutation narratives that invite post-hoc preference |

One agent may fill multiple roles only when the contract records the resulting loss of isolation. Do not imply independence merely because roles have different names.

## Weakness Cards

A weakness card is diagnostic feedback for mutation, not a copy of the evaluator. Prefer aggregate patterns and observable symptoms over item-level teaching signals.

```yaml
weakness_id: W1
observation: "What repeatedly went wrong"
evidence_scope: "approved source and observation range"
provenance: user-supplied | experiment-observed | conversation-inferred | workspace-inferred
contamination_risk: none | low | medium | high
frequency: "count, rate, or qualitative estimate"
severity: low | medium | high
affected_stage: "target-graph node or whole chain"
desired_direction: "observable improvement, not evaluator wording"
strengths_to_preserve:
  - "current behavior that must remain"
guardrails:
  - "prohibited regression and tolerance"
allowed_scope:
  - "surfaces the mutator may change"
confidence: low | medium | high
unknowns:
  - "unresolved cause or attribution"
```

Label conversation- or workspace-derived claims as inference, not clean evaluation evidence. A weakness card may describe a symptom without asserting its cause. Do not include exact hidden prompts, answer keys, hidden weights, sealed examples, or instructions that reveal how to trigger a score.

## Preserve Strengths Deliberately

Before mutation, identify strengths from baseline evidence and user priorities. Convert critical strengths into guardrails with observable checks and tolerances; retain softer strengths as comparison criteria. Evaluate every candidate against both the targeted weakness and preserved strengths.

A higher aggregate score does not override a prohibited regression. When trade-offs remain within approved tolerances, preserve non-dominated candidates and recommend the candidate that improves major criteria most evenly. Leave value-dependent adoption to the user.

Classify guardrails by consequence before execution:

- a **safety or validity stop** halts work because continuing is unsafe or the
  resulting evidence cannot answer the question;
- an **adoption gate** keeps a candidate ineligible but does not automatically
  erase safe diagnostic learning from it;
- a **diagnostic flag** marks a weakness or gray zone for analysis without
  deciding eligibility alone.

Do not expose sealed evidence merely to diagnose an ineligible candidate. When
diagnostic evaluation is safe, useful, budgeted, and uses approved development
evidence, report both the full candidate pattern and the eligible subset while
keeping the adoption decision failed. A safety or validity stop always takes
precedence.

## Anonymous, Randomized Comparison

When feasible:

1. Freeze candidate artifacts before evaluation.
2. Assign opaque identifiers unrelated to origin, version, or expected quality.
3. Randomize presentation order per evaluation unit; counterbalance order when repeated comparisons are practical.
4. Give all candidates the same approved inputs, tool access, budgets, stopping rules, and environmental conditions.
5. Keep evaluator instructions and scoring scales stable during a comparison block.
6. Reveal identities only after measurements and the adjudicator's provisional recommendation are recorded.

Before the first candidate comparison, run the approved evaluator-readiness
gate. Use controls, anchors, repeated judgments, paired preferences, human
review, or another appropriate check. Compare evaluator disagreement with the
minimum effect that would change adoption. If disagreement can reverse the
decision, calibrate, replace or supplement the evaluator, or limit the work to
exploratory diagnosis; do not merely average unstable evaluators and proceed as
if the threshold remained confirmatory.

Record deviations such as failed runs, retries, unequal latency limits, evaluator drift, or stateful tool effects. Randomization reduces order and identity bias; it does not correct invalid samples, leakage, or an unreliable evaluator.

## Hidden Weights and Holdouts

Public criteria should be meaningful enough to guide improvement. Hidden material should test generalization, not introduce undisclosed objectives.

- Hide exact weights, thresholds, evaluator prompts, item-level answers, and sealed confirmation examples from the mutator where feasible.
- Keep every safety or adoption-blocking guardrail visible at the policy level. Do not surprise candidates with a secret normative requirement.
- Separate exploratory evidence from a sealed holdout before candidate development. Do not use holdout failures to iteratively tune the same candidate and still call the set sealed.
- If the holdout is opened, log when, why, by whom or which role, and what was revealed. Retire or refresh it before further confirmation.
- Validate evaluator stability and rubric relevance independently; secrecy cannot repair a poor measurement system.

## Leakage and Contamination Checks

Run these checks before evaluation and again before final adoption:

- Search mutator inputs, candidate artifacts, shared files, traces, and tool outputs for evaluator text, hidden item content, answer keys, weights, thresholds, or holdout identifiers.
- Check whether the same session, agent context, persistent memory, cache, retrieval index, or workspace previously exposed sealed material.
- Verify that diagnostic summaries cannot be joined with other available data to reconstruct item-level answers.
- Check candidate names, ordering, metadata, path names, timestamps, and formatting for identity or expected-rank signals.
- Confirm that evaluators did not see mutation rationales, expected effects, prior winners, or user preferences before scoring.
- Detect evaluator drift by repeating controls or known anchors when the approved design requires it.
- Record provenance for every non-observed diagnostic claim and rate contamination risk as `none`, `low`, `medium`, or `high`.

Treat suspected leakage as a protocol deviation. Quarantine affected measurements, determine whether clean re-evaluation is possible, and otherwise report the outcome as exploratory or inconclusive rather than silently accepting it.

## Degraded-Isolation Report

When ideal isolation is not possible, include a compact disclosure:

```yaml
isolation_claim: procedural_blindness | context_isolation | enforced_secrecy
intended_boundary: "what was meant to remain hidden"
actual_exposure:
  - "known or plausible leakage channel"
checks_performed:
  - "verification completed"
residual_risk: low | medium | high
impact_on_conclusion: "how confidence or allowed wording changes"
mitigation: "fresh context, re-randomization, new holdout, or none available"
```

Use calibrated language: `exploratory signal`, `likely improvement`, `confirmation passed`, or `inconclusive` as supported by the approved design. Isolation is one property of the evidence, not a license to claim certainty.
