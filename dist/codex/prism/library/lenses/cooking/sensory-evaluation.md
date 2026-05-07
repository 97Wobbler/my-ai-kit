---
name: sensory-evaluation
display_name: Sensory Evaluation
class: lens
underlying_class: native
domain: cooking
source: ISO 13299 (Sensory analysis — Methodology for establishing a sensory profile); triangle test (ISO 4120); descriptive analysis and hedonic scaling in food science
best_for:
  - Standardizing taste, aroma, texture assessments across batches or recipes
  - Detecting small differences between two products (triangle test)
  - Building a detailed sensory vocabulary for a dish or ingredient
  - Measuring consumer preference or acceptance
one_liner: "Systematic sensory measurement via triangle tests, descriptive analysis, and preference testing."
---

# Sensory Evaluation

## Overview

Sensory Evaluation is a structured methodology for quantifying and documenting the sensory attributes of food—appearance, aroma, flavor, texture, and mouthfeel. Rather than relying on intuition or informal tasting notes, the lens operationalizes perception through three distinct protocols: the triangle test (detecting differences), descriptive analysis (building sensory profiles), and hedonic scales (measuring preference). Practitioners use it when product consistency must be verified, when a recipe iteration needs objective feedback, or when communicating flavor/texture to others requires a shared vocabulary.

## Analytical Procedure

### Phase 1 — Define the Evaluation Objective

1. **Specify what you are assessing.** Are you detecting a difference between two products (triangle test)? Documenting the sensory profile of a single product (descriptive)? Or measuring how much people like something (hedonic)?

2. **Choose the protocol:**
   - **Triangle Test:** Use when you need to answer: "Are Product A and Product B detectably different?" (Go to Phase 2a)
   - **Descriptive Analysis:** Use when you need to document: "What are all the sensory attributes of this product and how intense is each?" (Go to Phase 2b)
   - **Hedonic Scale:** Use when you need to measure: "How much do people like this product?" (Go to Phase 2c)

### Phase 2a — Triangle Test (Difference Detection)

Applicable only if your objective is to detect whether two products are perceptibly different.

3. **Prepare three samples:** Two identical samples (let's call them AA) and one different sample (B). Arrange them in random order (e.g., AAB, ABA, BAA, etc.) so the evaluator does not know which is the odd one out.

4. **Brief the evaluator:** "You will taste three samples. Two are identical, one is different. Which one is the odd one out?"

5. **Record the response:** Note whether the evaluator correctly identified the odd sample or guessed.

6. **Repeat with multiple evaluators** (at least 8–12 for statistical validity).

7. **Calculate the result:**
   - Count correct identifications.
   - Compare to chance (1 in 3 = 33%).
   - If significantly more than 33% are correct (consult a triangle test statistical table for your sample size), the products are detectably different.

### Phase 2b — Descriptive Analysis (Sensory Profiling)

Applicable only if your objective is to document the full sensory profile of a product.

8. **Build or select a sensory vocabulary** for the product category. For example, a beef broth might include: "beefy," "salty," "umami," "meaty," "mineral," "warming," "clear," "translucent." Each term should be concrete and scorable (not subjective like "good" or "complex").

9. **Define reference standards for each attribute.** For "salty," agree that a sample with 1% salt is a 3/10 and a sample with 3% salt is an 8/10. Reference standards anchor the scale across evaluators and sessions.

10. **Prepare the product sample** at serving temperature and portion size (e.g., 30 mL broth in a white cup, at 60°C).

11. **Have each evaluator score each attribute on a 0–10 or 0–15 scale** against the reference standards. Use a scoresheet (see Output Format) to record all scores simultaneously.

12. **Repeat with 8–12 trained evaluators** (training = multiple sessions where evaluators calibrate against standards and discuss results together).

13. **Average the scores across evaluators** for each attribute. This is your sensory profile.

### Phase 2c — Hedonic Scale (Preference Measurement)

Applicable only if your objective is to measure how much people like a product.

14. **Choose a hedonic scale.** Common options:
    - **9-point scale:** 1 = "Dislike extremely" → 5 = "Neither like nor dislike" → 9 = "Like extremely"
    - **5-point scale:** 1 = "Dislike very much" → 3 = "Neither" → 5 = "Like very much"
    - **Labeled Affective Magnitude (LAM) scale:** More sensitive to small differences in preference (uses visual magnitude estimation).

15. **Prepare the sample** at serving temperature and portion size. Ensure all samples are identical in presentation.

16. **Brief the evaluator:** "Please taste this sample and indicate how much you like it using this scale."

17. **Record the response.** Optionally, ask a follow-up: "What did you like or dislike about this?"

18. **Repeat with 30–100+ naïve evaluators** (consumers, not trained assessors). Larger n increases statistical power.

19. **Analyze the results:**
    - Calculate the mean and standard deviation of scores.
    - If comparing two products, use a paired t-test or Wilcoxon signed-rank test to check if the difference in mean preference is statistically significant.

### Phase 3 — Quality Control and Consistency

20. **If running multiple sessions or batches:** Repeat the same evaluation (triangle, descriptive, or hedonic) on a new batch of the product at a later date. Compare results to the first session. High consistency across sessions = reliable product or method. Large drift = batch variation or evaluator drift.

21. **If using trained evaluators (descriptive analysis):** Periodically re-evaluate reference standards and check for rater drift (i.e., one evaluator's scores shifting over time). If drift is detected, conduct a retraining session.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Objective clearly stated (difference / profile / preference) | Y/N |
| Correct protocol chosen for the objective | Y/N |
| Samples prepared and presented identically (except where difference is intended) | Y/N |
| Sample size adequate for protocol (≥8 for triangle, ≥8–12 for descriptive, ≥30 for hedonic) | Y/N |
| For descriptive: sensory vocabulary is concrete and unambiguous | Y/N |
| For descriptive: reference standards are defined and communicated to evaluators | Y/N |
| For hedonic: scale and instructions are communicated clearly | Y/N |
| Results recorded on a standardized scoresheet | Y/N |
| Analysis (averaging, statistical test) performed and documented | Y/N |

## Red Flags

- Evaluators are not blinded or samples are not randomized. Bias will contaminate results.
- Sensory vocabulary (descriptive) is vague: "tasty," "good," "weird." These are preferences, not attributes. Reject and redefine.
- Reference standards are missing or not communicated. Evaluators are scoring against their own internal scales, not a shared standard.
- Sample size is very small (e.g., 3 evaluators for triangle test). Chance will dominate the result.
- Results from descriptive analysis show extreme agreement (all evaluators gave identical scores). Either the product is uniform to the point of blandness or evaluators copied each other instead of evaluating independently.
- Hedonic scale results have a bimodal or heavily skewed distribution (e.g., all 1s and 9s, few in the middle). This may indicate that the product is polarizing or that the scale does not match the product.
- No repeat or consistency check across batches or time. A single evaluation is a snapshot, not evidence of a stable product.

## Output Format

```
## Sensory Evaluation Report

**Objective:**
[Difference detection / Sensory profiling / Preference measurement]

**Protocol Used:**
[Triangle test / Descriptive analysis / Hedonic scale]

**Sample Description:**
- Product: <name or batch ID>
- Portion size and temperature: <e.g., 30 mL at 60°C>
- Number of evaluators: <n>
- Evaluator type: [Trained / Naïve / Mixed]

### Results

#### For Triangle Test:
| Evaluator | Response | Correct? |
|---|---|---|
| 1 | [Sample A / B / C] | Y/N |
| 2 | ... | ... |

Correct responses: _ out of _
Percentage: _%
**Verdict:** [Significantly different / Not detectably different]

#### For Descriptive Analysis:
| Sensory Attribute | Mean Score | Std Dev | Reference |
|---|---|---|---|
| Aroma: Meaty | 6.2 | 1.1 | Ref std = 6 |
| Aroma: Salty | 4.8 | 1.5 | Ref std = 5 |
| Taste: Umami | 7.1 | 0.9 | Ref std = 7 |
| ... | ... | ... | ... |

**Sensory Profile:**
[Narrative summary of the product's dominant attributes and intensities]

#### For Hedonic Scale:
| Scale Used | Mean | Std Dev | Median | Mode |
|---|---|---|---|---|
| <9-point / 5-point / LAM> | 6.8 | 1.4 | 7 | 7 |

**Distribution:** <e.g., 15 responses at 9, 20 at 8, 12 at 7, 8 at 6, 5 at 5, 0 at 4–1>
**Interpretation:** [e.g., "Strong preference" / "Mixed but leaning positive" / "No clear consensus"]

If comparing two products: 
- Product A mean: 6.8; Product B mean: 5.1
- t-test p-value: 0.003 (significant at α=0.05)
- **Verdict:** Product A is significantly more preferred.

### Confidence
<high/medium/low> — <Justification. Examples: "High — protocol followed, n=40 evaluators, consistent across two sessions." Or "Medium — small sample size (n=6) and no reference standards defined." Or "Low — evaluator instructions were ambiguous and no quantitative analysis performed.">
```
