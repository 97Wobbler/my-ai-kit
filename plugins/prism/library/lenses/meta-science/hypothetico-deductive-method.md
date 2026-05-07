---
name: hypothetico-deductive-method
display_name: Hypothetico-Deductive Method
class: lens
underlying_class: native
domain: meta-science
source: Karl Popper (The Logic of Scientific Discovery, 1934); foundational to modern empirical methodology
best_for:
  - Validating or falsifying a theoretical claim through systematic observation
  - Designing experiments that can produce conclusive results
  - Detecting when an explanation is unfalsifiable or circular
one_liner: "Scientific reasoning cycle — hypothesize, derive predictions, test by observation or experiment."
---

# Hypothetico-Deductive Method

## Overview
The hypothetico-deductive method tests a theoretical claim by deriving predictions from it, then exposing those predictions to observation or experiment. If observations contradict predictions, the hypothesis is falsified. If observations confirm predictions, the hypothesis survives (but is never "proven" — only not-yet-falsified). Practitioners use this to distinguish genuine explanations from post-hoc narratives, and to design experiments that can actually settle a disagreement rather than accumulate ambiguous data.

## Analytical Procedure

### Phase 1 — State the Hypothesis

1. **Write the hypothesis as a causal or relational claim.** Use this structure: "If [condition], then [outcome] because [mechanism]." The mechanism is the explanatory heart — it's what makes the claim falsifiable. Without it, you have only a correlation prediction, not an explanation.
   - Weak: "Rain increases crop yield."
   - Strong: "Rain increases soil moisture, which increases nutrient availability to roots, which increases crop yield."

2. **Check that the hypothesis is falsifiable.** Ask: "What observation would prove this wrong?" If the answer is "nothing — it's always true," the hypothesis is unfalsifiable and cannot be tested with this method. If the answer is "well, if it failed, we'd say X interfered," you have an escape clause — the hypothesis is protected from falsification, not testable.

3. **List the components of the mechanism explicitly.** Each step from condition to outcome should be stated. Missing steps hide assumptions that later become problems.

### Phase 2 — Derive Predictions

4. **From the hypothesis, derive at least 3 specific, testable predictions.** Each prediction must:
   - State a measurable quantity (not "more" but "15% more")
   - Specify a condition or population under which it applies
   - Be logically entailed by the hypothesis (not just consistent with it)

   Example: If "rain → soil moisture → nutrient availability → yield" is your hypothesis, then predictions might include:
   - "Soil moisture will increase within 12 hours of rainfall at depths 0–30cm in sandy loam"
   - "Plant nitrogen uptake will increase within 48 hours in plots that received >5mm rain"
   - "Yield will be 20% higher in years with above-median rainfall vs. below-median"

5. **For each prediction, specify its logical status relative to the hypothesis:**
   - **Necessary consequence** — the hypothesis requires this to be true. If it fails, the hypothesis is falsified.
   - **Sufficient but not necessary** — the hypothesis predicts this, but the hypothesis could be true without it. If it fails, the hypothesis survives; if it succeeds, it gains support.
   - **Correlated but not entailed** — this would be true if the hypothesis is true, but other hypotheses might also predict it. If it fails, falsification is ambiguous.

   Only necessary consequences can actually falsify the hypothesis. Sufficient-but-not-necessary predictions strengthen support but don't rule it out when they fail.

6. **Design the observation or experiment to test the necessary predictions.** Write the protocol explicitly: What will you measure? How? Under what conditions? What is the threshold for confirming vs. falsifying each prediction?

### Phase 3 — Conduct Observation or Experiment

7. **Carry out the observation or experiment as designed.** Record the results without post-hoc modification of the protocol. If you change the protocol mid-experiment, flag it and note that the test is now testing a different hypothesis.

8. **For each necessary prediction, state whether it was confirmed or falsified.**
   - **Confirmed:** The observation matches the prediction within the stated tolerance.
   - **Falsified:** The observation contradicts the prediction.
   - **Ambiguous:** The observation is inconclusive (e.g., measurement error, confounding variables, or the protocol was not followed).

   Do not grade-curve ambiguous results. Name them as ambiguous and design a follow-up test.

### Phase 4 — Evaluate and Revise

9. **Assess the hypothesis's status:**
   - **Falsified:** At least one necessary prediction failed. The hypothesis as stated is wrong.
   - **Survives:** All necessary predictions were confirmed. The hypothesis has not been falsified (but note: this does not prove it true — other hypotheses might also explain the data).
   - **Ambiguous:** Some necessary predictions were ambiguous. Design a follow-up test to resolve the ambiguity before concluding.

10. **If falsified, analyze the failure mode.** Which part of the mechanism broke? The condition wasn't met? The outcome didn't follow? The mechanism itself was wrong? This guides revision.

11. **If survives, list alternative hypotheses that would make the same predictions.** Can you think of a competing explanation that would also predict the results? If yes, design a new experiment that differentiates between them.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Hypothesis includes a causal mechanism, not just correlation | Y/N |
| Falsifiability test passed — at least one observation could prove it wrong | Y/N |
| At least 3 specific, measurable predictions derived | Y/N |
| Each prediction marked as necessary/sufficient/correlated | Y/N |
| At least one necessary prediction is included | Y/N |
| Experiment/observation protocol written before data collection | Y/N |
| Each result classified as confirmed/falsified/ambiguous | Y/N |
| Alternative hypotheses considered (if hypothesis survived) | Y/N |

## Red Flags

- Hypothesis is unfalsifiable ("this is always true, but sometimes other things interfere"). If every possible outcome is compatible with the hypothesis, it predicts nothing and cannot be tested.
- All derived predictions are sufficient-but-not-necessary. A hypothesis that can explain anything explains nothing. At least one prediction must be necessary.
- Protocol is vague ("we'll measure growth" without specifying how, when, or what counts as a change). Vague protocols allow post-hoc rationalization of ambiguous results.
- Prediction is confirmed, and no alternative hypotheses are considered. A single test that succeeds does not distinguish between competing explanations.
- Results are ambiguous, but the hypothesis is declared "survived" anyway. Ambiguity is not confirmation. It is a signal to run a more precise test.
- Mechanism contains untested sub-claims. "Rain → nutrient availability" is itself a mini-hypothesis that needs its own test. Naming it doesn't validate it.

## Output Format

```
## Hypothetico-Deductive Assessment

**Hypothesis:**
> <statement with mechanism>

**Falsifiability check:**
- Observation that would falsify it: <...>
- Is hypothesis protected from falsification? Y/N
- Status: Falsifiable | Unfalsifiable

### Phase 1 — Mechanism Components
1. <component>
2. <component>
3. ...

### Phase 2 — Derived Predictions
| Prediction | Logical Status | Measurement Protocol |
|---|---|---|
| <...> | Necessary/Sufficient/Correlated | <...> |

### Phase 3 — Results
| Prediction | Outcome | Observation |
|---|---|---|
| <...> | Confirmed/Falsified/Ambiguous | <...> |

### Phase 4 — Evaluation

**Hypothesis status:** Falsified | Survives | Ambiguous

**Analysis:**
<If falsified: which part of mechanism broke? If survives: what alternative hypotheses predict the same results? If ambiguous: what follow-up test is needed?>

**Alternative hypotheses considered:**
1. <...> — differentiable by: <test>
2. <...>

### Confidence
<high/medium/low> — <justification. High confidence: all necessary predictions confirmed and alternatives ruled out. Medium: necessary predictions confirmed but alternatives remain or follow-up needed. Low: results ambiguous or falsified.>
```
