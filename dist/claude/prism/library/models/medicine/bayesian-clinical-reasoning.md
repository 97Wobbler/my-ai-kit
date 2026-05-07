---
name: bayesian-clinical-reasoning
display_name: Bayesian Clinical Reasoning
class: model
underlying_class: native
domain: medicine
source: Thomas Bayes, "An Essay towards solving a Problem in the Doctrine of Chances," 1763; modern medical applications developed by Sackett et al., Evidence-Based Medicine (1996) and Pauker & Kassirer (1975)
best_for:
  - Updating disease probability after a test result using pretest probability and test accuracy
  - Deciding whether a diagnostic test changes clinical action
  - Explaining why test results mean different things in different populations
one_liner: "Pre-test probability × likelihood ratio → post-test probability."
---

# Bayesian Clinical Reasoning

## Overview

Bayesian Clinical Reasoning claims that the **posterior probability of disease after a test result is determined entirely by three inputs**: the pretest probability of disease in the patient, the sensitivity and specificity of the test (encoded as likelihood ratios), and Bayes' rule. The model is predictive — it tells you what the true probability of disease is after a test, correcting for the common cognitive error of treating test results as if they carry fixed meaning independent of context. It explains why a positive test means something very different in a high-prevalence population than in a low-prevalence one, and why many clinicians misinterpret test results by ignoring the pretest probability. This is a mechanistic model: apply the procedure below to a concrete patient and test.

## Core Variables and Relationships

Three variables determine the posttest probability:

1. **Pretest probability (prior)** — the probability of disease in the
   patient *before* the test result.
   - Established by patient history, physical exam, prevalence in the
     population, clinical presentation
   - Is the patient symptomatic? Do they match the disease profile?
   - What is the base rate of disease in this setting?
   - Higher pretest probability → higher posttest probability for a
     given test result

2. **Sensitivity** — the probability of a positive test given the patient
   has disease: P(T+ | D+).
   - Also called the true positive rate
   - Feeds into the likelihood ratio: LR+ = Sensitivity / (1 − Specificity)
   - Higher sensitivity → LR+ closer to 1 (test less discriminating)
   - Lower sensitivity → LR+ closer to 0

3. **Specificity** — the probability of a negative test given the patient
   does not have disease: P(T− | D−).
   - Also called the true negative rate
   - Feeds into the likelihood ratio: LR− = (1 − Sensitivity) / Specificity
   - Higher specificity → LR− closer to 0 (negative test rules out disease)
   - Lower specificity → LR− closer to 1

4. **Likelihood ratio (LR)** — the key quantity that updates probability.
   - LR+ = Sensitivity / (1 − Specificity) : how much does a positive test
     increase the odds of disease?
   - LR− = (1 − Sensitivity) / Specificity : how much does a negative test
     decrease the odds of disease?
   - LR > 1 increases suspicion of disease; LR < 1 decreases it
   - LR = 1 provides no information

The core relationship is **odds form of Bayes' rule**:

    Posttest odds = Pretest odds × Likelihood ratio

Or equivalently:

    Posttest probability = Pretest odds × LR / (1 + Pretest odds × LR)

where pretest odds = pretest probability / (1 − pretest probability).

## Key Predictions

- **A positive test in a low-pretest-probability setting may still leave
  the patient's probability of disease below the "treat" threshold.** If
  pretest probability is 5%, specificity 95%, and sensitivity 90%, a
  positive test raises probability to ~49%, often still below where
  treatment is warranted. The test is not useless but is misinterpreted if
  treated as confirming disease.

- **A negative test with high sensitivity and high pretest probability can
  confidently rule out disease.** If pretest probability is 70%, sensitivity
  95%, and specificity 90%, a negative test drops probability to ~8%. High
  sensitivity makes negative results strong evidence.

- **A positive test with high specificity in a high-pretest-probability
  setting is nearly decisive.** If pretest probability is 70%, specificity
  95%, and sensitivity 90%, a positive test raises probability to ~95%. The
  test confirms what clinical judgment already suggested.

- **Sensitivity and specificity alone do not determine the utility of a test.**
  A test with 90% sensitivity and 90% specificity (LR+ ≈ 9, LR− ≈ 0.11) is
  helpful in a 50% pretest setting (posttest ~90% or ~10%) but misleading in a
  5% setting (posttest ~32% or <1%). Context is load-bearing.

- **Clinicians systematically overestimate the posttest probability of disease
  after a positive test**, especially when pretest probability is low. This is
  the conjunction fallacy: high sensitivity is misread as high posterior
  probability. Quantitative reasoning prevents this error.

- **Sequential testing amplifies the effect of likelihood ratios.** A first
  negative test (LR− = 0.1) drops 50% → 9%; a second negative test drops
  9% → 0.9%. Two independent tests with even modest LRs can move probability
  decisively. Conversely, a sequence of weak positive tests (LR+ = 2) is much
  slower to accumulate evidence.

## Application Procedure

Instantiate the model against a concrete patient, test, and clinical
decision.

1. **Define the patient and disease in question.** Who is the patient? What
   specific disease or condition are you testing for? (Not "infection" but
   "streptococcal pharyngitis.") Write it in one sentence.

2. **Establish the pretest probability.** Estimate the probability of disease
   in *this patient* before the test result, drawing on:
   - Patient symptoms, signs, and risk factors
   - Prevalence of disease in the relevant population
   - How closely the patient matches the typical presentation
   - If necessary, use published pretest probability estimates for the
     clinical presentation (e.g., "chest pain with X characteristics has
     10% pretest probability of MI").
   - Write the pretest probability as a percentage or odds ratio.

3. **Identify the test and look up its sensitivity and specificity.** From
   the literature (or the test manufacturer), obtain P(T+ | D+) and P(T− |
   D−). Note the population and setting in which the test was validated —
   can differ materially.

4. **Calculate the likelihood ratio for the observed test result.**
   - If test is positive: LR+ = Sensitivity / (1 − Specificity)
   - If test is negative: LR− = (1 − Sensitivity) / Specificity
   - Qualitatively: LR > 10 is strong evidence for disease; LR < 0.1 is
     strong evidence against it; 2 ≤ LR ≤ 5 is moderate.

5. **Apply Bayes' rule to compute posttest probability.** Convert pretest
   probability to odds, multiply by LR, convert back to probability.
   - Pretest odds = P / (1 − P)
   - Posttest odds = Pretest odds × LR
   - Posttest probability = Posttest odds / (1 + Posttest odds)
   - Or use a nomogram or calculator if numeric precision is not required.

6. **Compare posttest probability to clinical thresholds.**
   - Probability below which you would not treat (treat threshold)
   - Probability above which you would treat (test threshold)
   - Is the posttest probability above the test threshold, below the treat
     threshold, or in between?
   - If in between, consider whether further testing is warranted.

7. **Check boundary conditions** (below). If any apply, note that Bayes' rule
   still applies but additional reasoning is needed.

8. **Generate the clinical prediction.** Does the test result change your
   management of the patient? By how much?

## Boundary Conditions

Bayesian Clinical Reasoning assumes the test result is conditionally
independent of disease status given the patient's true disease state, and
that sensitivity and specificity are known and stable. The model is partial
or breaks down when:

- **Sensitivity or specificity is unknown or population-dependent.** Published
  values from a screened, tertiary-referral population may not generalize to
  your primary-care cohort. The model's output is only as accurate as the
  input numbers.

- **The test result is not binary or is ambiguous.** Many imaging tests and
  pathology results admit degrees of suspicion, not a clean positive/negative.
  For ordinal results, Bayes' rule applies to each threshold, but you must
  recalibrate the LR for the specific cutoff.

- **The disease has multiple phenotypes or severity states.** Pretest
  probability of "infection" conflates bacterial infection (needs antibiotics),
  viral infection (does not), and non-infectious inflammation. If the test is
  sensitive to one phenotype but not others, the LR is mismeasured for your
  clinical question.

- **The test is conditionally dependent on other findings** (the patient had
  prior test X, which already moved probability). The LR of test Y should be
  computed *given* the patient's current (posttest from X) probability, not
  the original pretest. Sequential testing is easier to reason about when
  tests are assumed independent.

- **Pretest probability is not a fixed number but is poorly quantified or
  contested among clinicians.** If you and a colleague disagree on the pretest
  probability by a factor of 3, the posttest probability will also diverge. In
  low-pretest settings, small changes in pretest assumption swing the posttest
  widely.

- **The test is extremely expensive, invasive, or rare, and the decision is
  not isolated.** Bayes' rule tells you the probability of disease, not whether
  you should order the test. A separate utility analysis (cost, risk, benefit)
  is needed to decide whether testing is worthwhile.

## Output Format

```
## Bayesian Clinical Reasoning: <patient / disease / test>

**Patient:** <age, sex, key clinical features>
**Disease in question:** <specific diagnosis>
**Test:** <name, modality>

### Inputs
| Input | Value | Source / Notes |
|---|---|---|
| Pretest probability | __% | <reasoning from history, exam, prevalence> |
| Sensitivity | __% | <source, population> |
| Specificity | __% | <source, population> |
| Observed result | Positive / Negative | |
| Likelihood ratio | __  | <LR+ or LR− from sensitivity/specificity> |

### Bayesian calculation
| Step | Calculation | Result |
|---|---|---|
| Pretest odds | P / (1−P) | __ |
| Posttest odds | Pretest odds × LR | __ |
| Posttest probability | Posttest odds / (1 + Posttest odds) | __% |

### Clinical interpretation
- Posttest probability: __% (was __% before test)
- Probability change: <up / down> by __ percentage points
- Clinical threshold (treat if >__%): <above / below / at threshold>
- Does the result change management? <yes / no, and how>

### Boundary-condition check
<which of the boundary conditions apply and whether the LR and posttest
probability are still reliable guides to clinical action>

### Confidence: high | medium | low
<reasoning: pretest probability clarity + sensitivity/specificity
stability in this population + test independence + whether threshold
decision is clear-cut>
```
