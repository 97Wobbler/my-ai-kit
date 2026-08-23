# Stochastic Comparison

Use this reference when outputs or evaluations can vary across runs. Its
purpose is to make uncertainty visible and match the strength of a conclusion
to the evidence. It does not prescribe one universal statistical test.

## Choose Rigor Before Execution

Use the lightest design that can support the user's decision.

### Exploratory comparison

Use when the request is broadly “make this better,” the decision is
reversible, or the budget is small.

- Establish an incumbent baseline and run repeated, comparable observations.
- Prefer paired observations on the same approved cases and conditions.
- Report score direction, effect size, dispersion, guardrails, cost, and
  obvious failure clusters.
- Treat a small or unstable lead as a signal for another experiment, not as
  established improvement.
- A candidate may be recommended provisionally when its advantage is material
  for the user's purpose and no guardrail regresses, but label the conclusion
  `exploratory_signal`.

### Confirmatory comparison

Use when the user requests a specific improvement, a consequential adoption,
or a defensible confidence level. Before execution, fix:

- primary outcome and direction;
- experimental unit and sampling frame;
- minimum effect worth adopting;
- guardrails and permitted regression margins;
- comparison method, sample or evaluation budget, and stopping rule;
- candidate count and any multiple-comparison handling;
- holdout or final whole-chain confirmation, when appropriate.

Select a method that fits the outcome, pairing, dependence, distribution, and
budget. Suitable methods can include confidence intervals, paired bootstrap or
randomization procedures, model-based intervals, or sequential designs. State
their assumptions and limitations. Do not choose a method merely because it is
familiar.

## Define The Experimental Unit

Name what one independent observation represents: for example, one approved
case-run, one user task, one conversation, or one whole-chain execution.
Distinguish variation across cases from repeated executions of the same case.
Do not count dependent retries, turns from one conversation, or correlated
judge calls as independent evidence without modeling or grouping that
dependence.

Record at least:

- sampling frame and exclusions;
- case identity or anonymized stable key;
- run conditions that should be held constant;
- number of distinct units and repeats per unit;
- known clustering, temporal drift, cache, model-version, and evaluator effects.

Also name the **analysis unit**, cluster key, distinct-cluster count, repeats
within each cluster, and effective sample basis. Repeated seeds or runs within
one case usually measure within-case variation; they do not create the same
amount of independent evidence as new cases. If the planned analysis ignores a
known dependence structure, stop and revise it rather than applying an
independent-unit bootstrap or test by convenience.

## Prefer Paired And Balanced Sampling

When feasible, run incumbent and candidates on the same units under comparable
conditions. Pairing removes some between-case variation and makes per-unit
differences inspectable. Randomize or counterbalance anonymized candidate
order when order, evaluator position, or shared external state could bias the
result.

Pairing is not automatically valid. Missing candidate outputs, changed inputs,
stateful chains, carry-over effects, or differently sampled cases can break the
pair. Record such observations and use a design that reflects them rather than
silently treating them as paired.

## Measure More Than The Mean

For every major criterion, report a useful effect estimate and uncertainty,
not only a point score. Depending on the data, inspect:

- mean or median paired difference;
- win, tie, and loss rates;
- quantiles, tails, or worst-case clusters;
- variance across cases, repeated runs, and evaluators;
- missing, invalid, timed-out, and safety-blocked observations;
- latency, token use, and other approved costs.

Separate process variance from evaluator variance when possible. An unstable
evaluator can dominate candidate differences; validate or repeat the evaluator
before interpreting small effects. Preserve raw-enough aggregate evidence to
recalculate decisions without exposing sealed cases to mutation work.

Treat evaluator readiness as a prerequisite, not merely a caveat after scores
exist. Compare evaluator disagreement and control drift with the minimum effect
that would change the decision. When disagreement is decision-reversing, use
anchors, paired preferences, repeated controls, human adjudication, or another
approved calibration step. If readiness remains insufficient, restrict the
result to exploratory diagnosis and do not apply the confirmatory adoption
threshold.

Measure cost with the same dictionary for incumbent and candidates. Prefer
wall time, actual model or evaluator calls, input and output units, retries,
discarded work, accepted outputs, and cost per accepted output. A precise ratio
is invalid when its numerator and denominator count different operations;
report the common measurements and the limitation instead.

## Minimum Effect And Confidence Intervals

For confirmatory work, agree on a minimum effect that is meaningful for the
user before seeing candidate results. A confidence interval should be
interpreted against both zero and this minimum effect:

- entirely beyond the minimum effect: evidence supports the specified gain;
- excludes meaningful harm but crosses the minimum effect: non-inferior or
  promising, not confirmed at the desired magnitude;
- spans meaningful benefit and harm: inconclusive;
- entirely on the harmful side or violates a guardrail: reject.

Confidence levels do not measure the probability that a particular candidate
is good. State the estimand, interval method, assumptions, and effective sample
size. Avoid false precision when observations or evaluator judgments are
coarse or dependent.

For noisy quality criteria and small effective samples, predefine three regions
when appropriate: pass, gray zone, and fail. A gray-zone result triggers the
approved additional-sampling or adjudication rule rather than an arbitrary
binary decision. Keep hard zero-tolerance thresholds for genuine safety,
validity, or explicit user requirements, not merely because a percentage is
easy to write.

## Sequential Testing

Sequential evaluation can save cost, but repeatedly checking an ordinary
fixed-sample result and stopping when it looks favorable inflates false
discoveries. If interim decisions are allowed, predefine a valid sequential
rule, such as spending boundaries, always-valid evidence, or a Bayesian rule
with explicit thresholds and priors.

The stopping rule must cover success, futility, harm, guardrail failure,
budget exhaustion, and evaluator instability. Log every look and why execution
stopped. Do not change thresholds after observing results without labeling the
next analysis exploratory.

Futility at one experiment path does not imply global futility. Apply the
approved futility boundary to the current hypothesis and intervention family,
then perform the contract's alternative-path review before ending the whole
investigation. A pivot starts a distinct, logged path and must not reuse interim
looks as if they were preregistered confirmatory evidence for the new path.

## Multiple Candidates And Criteria

Testing many mutations creates selection bias. In confirmatory work, limit the
candidate family or account for multiplicity with a method appropriate to the
decision. A common efficient pattern is:

1. screen several candidates on approved development evidence;
2. freeze the finalists and adoption rule;
3. compare only finalists on sealed evidence;
4. confirm the selected candidate on the whole target graph.

Never let an aggregate score conceal a prohibited regression. Apply guardrails
first. A safety or validity stop halts unusable evidence. An adoption gate
excludes a candidate from recommendation but may still allow safe, approved
diagnostic evaluation; record the full evidence and any eligible subset
without converting the candidate back to eligible. Diagnostic flags annotate
gray zones or weaknesses without deciding eligibility alone. Among eligible
candidates, prefer one that improves major criteria
together. If no candidate dominates the others, retain the Pareto set: a
candidate is non-dominated when no other eligible candidate is at least as
good on every relevant criterion and better on at least one. Recommend a
balanced default, explain trade-offs, and leave the final value judgment to
the user.

## Epistemic States

Use one of these states rather than overstating the result:

| State | Meaning |
|---|---|
| `confirmed` | The preapproved confirmatory rule was satisfied, including guardrails and final validation. |
| `likely` | Evidence is coherent and practically meaningful, but some confirmatory requirement remains unmet. |
| `exploratory_signal` | A useful direction appeared in exploratory evidence and merits confirmation. |
| `no_meaningful_change` | Evidence rules out, or does not reveal, an effect large enough to matter under the approved rule. |
| `inconclusive` | Evidence still permits materially different decisions. More or better evidence is needed. |
| `negative` | The candidate caused meaningful harm or failed an adoption threshold. |
| `invalid` | The experiment cannot answer the question because its contract, execution, evaluator, or data was compromised. |

A null or negative result is reusable knowledge. Record which hypothesis,
prediction, mutation, and conditions it bears on. `No meaningful change` is
not proof that all possible effects are zero; `inconclusive` is not evidence of
equivalence; a failed mutation does not by itself falsify every mechanism
behind its hypothesis.

## Analysis Checklist

- Compare against the approved incumbent and adoption rule.
- Confirm the unit, pairing, exclusions, and effective sample size.
- Inspect effect magnitude, uncertainty, dispersion, missingness, and cost.
- Check every guardrail before ranking candidates.
- Account for interim looks and candidate selection where the claim requires it.
- Revalidate partial-stage winners on the whole chain when product use depends
  on downstream behavior.
- Separate observations, inferences, unknowns, and next tests.
- Assign an epistemic state and state exactly what evidence would change it.
