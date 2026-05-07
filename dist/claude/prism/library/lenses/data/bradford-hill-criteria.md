---
name: bradford-hill-criteria
display_name: Bradford Hill Criteria
class: lens
underlying_class: native
domain: data
source: Austin Bradford Hill, 1965 (British Medical Journal); epidemiological causal inference standard
best_for:
  - Evaluating whether an observed association is causal or confounded
  - Pressure-testing causal claims in observational data
  - Structuring disagreement about causation between domain experts
one_liner: "Nine-point checklist for assessing causal inference reliability from observational data."
---

# Bradford Hill Criteria

## Overview
When two variables move together in data, it may be causation, confounding, reverse causation, or noise. The Bradford Hill Criteria are nine checkpoints that distinguish real causal signals from artifacts of measurement, selection, or hidden variables. Practitioners use this lens when an association is statistically significant but causation is still ambiguous—especially in observational studies where randomization is impossible or unethical. The framework does not prove causation but systematically raises the bar for claiming it.

## Analytical Procedure

### Setup
1. **State the proposed association clearly.** Write: "Exposure X is associated with outcome Y" with the direction and magnitude (e.g., "smoking increases lung cancer risk 10-fold"). Include the population, time window, and measurement method for both X and Y.

2. **Verify the association is real.** Confirm that the correlation or effect size is statistically significant and reproducible across at least two independent datasets or populations. If the association is absent or reverses in replication, stop—it is likely noise or publication bias.

### Nine Criteria Evaluation

Apply each criterion below. For each, answer: **Does this association *strengthen* the case for causation (✓), *weaken* it (✗), or *remain neutral* (?)**

**Criterion 1 — Strength of association**
- How large is the effect size or relative risk? Larger effects are less likely to be explained by unmeasured confounding.
- Rule of thumb: RR > 3 or odds ratio > 3 substantially strengthens the case. RR = 1.1 weakens it (easily explained by bias).
- Answer: Is the effect size large enough to be hard to dismiss as confounding? ✓ / ✗ / ?

**Criterion 2 — Consistency (replicability)**
- Has the association been observed across different populations, settings, measurement methods, or time periods?
- Consistency across *at least three independent studies* with different designs (cohort, case-control, cross-sectional) strengthens the case.
- Answer: Has the association been replicated in populations or contexts that differ from the primary study? ✓ / ✗ / ?

**Criterion 3 — Specificity**
- Does the exposure affect *only* this outcome, or does it affect many outcomes?
- Specificity (one exposure → one outcome) strengthens causation; non-specificity (one exposure → many unrelated outcomes) suggests confounding or bias.
- Answer: Is the exposure's effect on this outcome narrower and stronger than its effects on other outcomes? ✓ / ✗ / ?

**Criterion 4 — Temporality**
- Did the exposure precede the outcome in time?
- If outcome preceded exposure, causation is impossible. If timing is unclear, causal inference is severely weakened.
- Answer: Is there clear evidence that exposure occurred *before* outcome onset? ✓ / ✗ / ?
- Note: This is not optional. Reverse temporality is a fatal flaw.

**Criterion 5 — Biological gradient (dose-response)**
- As exposure increases, does the risk increase monotonically (or for a threshold exposure, does risk jump then plateau)?
- Lack of a dose-response does not rule out causation (thresholds exist), but a clear dose-response strengthens it.
- Answer: Is there a dose-response relationship, or does the mechanism predict one that we can measure? ✓ / ✗ / ?

**Criterion 6 — Plausibility**
- Is there a known or proposed biological, chemical, or physical mechanism linking exposure to outcome?
- Plausibility is subjective—what is "plausible" depends on current knowledge and can be wrong. But mechanism absence or incoherence with known biology weakens the case.
- Answer: Can we describe a causal pathway from X to Y that does not contradict known physiology or biochemistry? ✓ / ✗ / ?

**Criterion 7 — Coherence**
- Does the association cohere with what is already known about the exposure, outcome, and related systems?
- Incoherence with established knowledge does not prove the association is wrong, but it raises skepticism.
- Answer: Does this association fit with the existing body of knowledge in the field, or does it contradict established findings? ✓ / ✗ / ?

**Criterion 8 — Experiment**
- Can the association be tested experimentally (e.g., randomized trial, crossover, lab manipulation)?
- If experiments exist and confirm the association, this is the strongest evidence. If experiments contradict it, causation is unlikely.
- Answer: Have controlled experiments or trials replicated the association, or would they be impossible/unethical? ✓ / ✗ / ?

**Criterion 9 — Analogy**
- Are there known causal associations of a similar type (exposure, outcome, mechanism) that support the plausibility of this one?
- Analogies are weak evidence but can support a causal inference if the analogue is well-established.
- Answer: Does a similar exposure cause a similar outcome elsewhere, providing precedent? ✓ / ✗ / ?

### Synthesis

3. **Count the checks.** Tally ✓, ✗, and ? for all nine criteria. Record the results in a table.

4. **Identify the critical gaps.** If Criterion 4 (temporality) is ✗, stop—causation is ruled out. If Criteria 1, 2, or 4 are ✗, causation is unlikely without additional evidence. If Criteria 1, 2, 4, and 5 are all ✓, causation is more plausible.

5. **Evaluate robustness to unmeasured confounding.** For each ✓ criterion, ask: "Could this be explained by a hidden variable we haven't measured?" Criteria 3, 5, and 6 are relatively resistant to unmeasured confounding. Criteria 1 and 2 alone are not.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Association is clearly stated with effect size and population | Y/N |
| Association is verified as statistically significant and replicated ≥1 time | Y/N |
| All nine criteria are evaluated (none skipped) | Y/N |
| Each criterion is marked ✓, ✗, or ? with brief justification | Y/N |
| Temporality (Criterion 4) is explicitly addressed | Y/N |
| Critical gaps (✗ in Criteria 1, 2, 4, or 5) are flagged | Y/N |
| Unmeasured confounding vulnerability is discussed | Y/N |

## Red Flags

- Temporality (Criterion 4) is ✓ but the data is cross-sectional. Cross-sectional data cannot establish temporality. This is a fatal flaw for causal inference.
- All nine criteria are ✓. Either the association is extraordinarily well-established (rare) or the evaluation was lenient. Re-check Criterion 6 (plausibility)—if the mechanism is unknown or speculative, Criterion 6 should be ✗ or ?.
- Criterion 8 (experiment) was marked ✓ but the experiment was observational, not truly controlled. RCTs are experiments; observational studies are not.
- Criterion 3 (specificity) was marked ✓ but the exposure affects many unrelated outcomes. Specificity was not met; mark it ✗.
- No discussion of unmeasured confounding. Every observational study is vulnerable to unmeasured confounding. Absence of discussion suggests the analysis stopped too early.
- Criterion 5 (dose-response) was marked ✗ and cited as evidence against causation. Causation without a dose-response is uncommon but possible (thresholds, rare exposures). Mark ✗ only if a dose-response is theoretically expected and absent.

## Output Format

```
## Bradford Hill Assessment

**Association under evaluation:**
<exposure X → outcome Y, with effect size and population>

### Criterion Scores
| Criterion | Score | Justification |
|---|---|---|
| 1. Strength | ✓/✗/? | <effect size and threshold reasoning> |
| 2. Consistency | ✓/✗/? | <number of replications and contexts> |
| 3. Specificity | ✓/✗/? | <exposure effect on this vs. other outcomes> |
| 4. Temporality | ✓/✗/? | <sequence of exposure and outcome> |
| 5. Dose-response | ✓/✗/? | <monotonic or threshold gradient> |
| 6. Plausibility | ✓/✗/? | <proposed mechanism> |
| 7. Coherence | ✓/✗/? | <alignment with existing knowledge> |
| 8. Experiment | ✓/✗/? | <controlled trials or feasibility> |
| 9. Analogy | ✓/✗/? | <precedent from similar associations> |

**Summary:** ✓ = <count>  |  ✗ = <count>  |  ? = <count>

### Critical Gaps
<List any ✗ in Criteria 1, 2, 4, or 5. If Criterion 4 is ✗, causation is ruled out.>

### Unmeasured Confounding Vulnerability
<For each ✓ criterion, assess: could this be explained by a hidden variable?
Identify the most plausible unmeasured confounders and estimate their impact if possible.>

### Causal Inference Verdict
<Based on the profile above, is causation:>
- **Established**: ≥7 criteria are ✓, Criterion 4 is ✓, and experiments (Criterion 8) confirm or Criterion 1 and 5 are strong.
- **Plausible**: ≥5 criteria are ✓, Criterion 4 is ✓, no fatal flaws in unmeasured confounding analysis.
- **Uncertain**: 3–4 criteria are ✓, or gaps in Criteria 1, 2, or 5.
- **Unlikely**: Criterion 4 is ✗, or ≥2 of Criteria 1, 2, 5 are ✗.

### Confidence
<high/medium/low> — <justification: which criteria are most robust; which most vulnerable to unmeasured confounding>
```
