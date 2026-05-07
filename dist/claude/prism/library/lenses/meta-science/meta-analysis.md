---
name: meta-analysis
display_name: Meta-analysis (Cochrane)
class: lens
underlying_class: native
domain: meta-science
source: Cochrane Collaboration (established 1993); methodological consensus from Higgins & Green (Cochrane Handbook)
best_for:
  - Synthesizing effect sizes across multiple independent studies
  - Quantifying heterogeneity and detecting publication bias
  - Producing a single estimate of treatment effect with confidence bounds
one_liner: "Integrate effect sizes across studies via weighted averaging and quantify heterogeneity."
---

# Meta-analysis (Cochrane)

## Overview
Meta-analysis combines effect sizes from multiple independent studies into a single pooled estimate, weighted by study precision (sample size and variance). It surfaces heterogeneity — variation in effects that cannot be explained by sampling error alone — and flags publication bias, which distorts the aggregate effect when small, negative studies go unpublished. Practitioners reach for this lens when a question is addressed by many studies but no single study is definitive, and when understanding *why* studies disagree matters as much as the pooled number.

## Analytical Procedure

### Phase 1 — Specification and Study Identification

1. **Define the research question in PICO format:**
   - **Population** — who are the subjects?
   - **Intervention** — what is being tested?
   - **Comparison** — what is the control or alternative?
   - **Outcome** — what is measured, and how (mortality, symptom score, etc.)?
   Write each element plainly. Vague definitions lead to vague inclusions.

2. **Establish inclusion and exclusion criteria before searching.** Write criteria that a trained rater could apply consistently without judgment. Example: "RCTs only" vs. "RCTs and quasi-RCTs"; "English-language publications only" vs. "all languages"; "published 2000 onward" vs. "no date limit."

3. **Search the literature systematically.** Use at least two databases (MEDLINE, Embase, PubMed, CINAHL, etc.) with identical search strings. Document the exact search query, date range, and number of results before and after deduplication. Do not rely on a single database or hand-picked papers.

4. **Screen titles and abstracts against criteria.** Have at least two raters screen independently, then reconcile disagreements. Document reasons for exclusion (e.g., "study population does not match PICO").

5. **Retrieve full texts and apply detailed eligibility screening.** Again, use ≥2 raters. Document every exclusion reason. If >10% of full texts are excluded at this stage without a clear reason (e.g., "full text not found"), investigate — it signals poor initial screening or a shifting definition of eligibility.

### Phase 2 — Data Extraction and Effect Size Calculation

6. **Create a data extraction form.** Fields must include: study ID, year, population size (n per arm), intervention and comparison details (dose, duration, method), outcome definition, follow-up duration, and outcome data (events/totals for dichotomous outcomes; mean, SD, n per arm for continuous outcomes). Pilot the form on 3 studies and revise if instructions are unclear.

7. **Extract data independently from each study.** Two raters extract in parallel. Resolve discrepancies by discussion or by consulting the original paper; do not average disagreements.

8. **Calculate the effect size for each study.** Choose the effect size metric in advance:
   - **Dichotomous outcomes** (event/no event): use risk ratio (RR), odds ratio (OR), or risk difference (RD). Prefer RR or OR; they are invariant to baseline risk.
   - **Continuous outcomes** (measurements on a scale): use mean difference (MD) if all studies use the same scale; use standardized mean difference (SMD, Cohen's d) if scales differ.
   - **Time-to-event** (survival): use log hazard ratio (log HR).
   Calculate 95% confidence intervals (CIs) for each effect size. If a study reports only p-values or t-statistics, back-calculate the effect size and CI from those.

9. **Flag zero-event studies.** If a study reports zero events in one or both arms, effect size calculation requires a continuity correction (typically 0.5 added to all cells). Document which studies received this correction.

### Phase 3 — Heterogeneity Assessment

10. **Calculate Q-statistic and I² heterogeneity index.**
    - **Q-statistic**: sum of squared weighted deviations of each study's effect from the pooled effect. Q follows a chi-squared distribution with k−1 degrees of freedom (k = number of studies). p-value > 0.10 suggests homogeneity; p ≤ 0.10 suggests heterogeneity.
    - **I²** = (Q − (k−1)) / Q × 100%. Interpretation: <25% = low, 25–75% = moderate, >75% = high heterogeneity.
    Calculate both; they convey different information. Q is sample-size dependent (large k inflates Q even with small true differences), while I² is not.

11. **Conduct univariate meta-regression or subgroup analysis on hypothesized sources of heterogeneity.** Sources often include:
    - Study design (RCT vs. quasi-RCT)
    - Population characteristics (age, disease severity, baseline risk)
    - Intervention details (dose, duration, mode of delivery)
    - Outcome definition (proxy vs. clinical endpoint)
    - Geographic region or publication year
    Stratify the dataset and recalculate pooled effects and I² within each stratum. Report which variables explain heterogeneity (i.e., reduce I² substantially).

### Phase 4 — Pooled Effect Estimation

12. **Choose a statistical model: fixed-effect or random-effects.**
    - **Fixed-effect model** assumes all studies estimate the same true effect; variation is due to sampling error only. Use this if I² < 25% or if there is a strong *a priori* reason to believe effect homogeneity.
    - **Random-effects model** (DerSimonian & Laird, or more modern estimators) assumes each study estimates a different true effect drawn from a distribution. Use this if I² ≥ 25% or if heterogeneity is expected.
    For most real data, random-effects is more defensible because it accounts for between-study variance.

13. **Calculate the pooled effect size and 95% CI** using the chosen model. Report the point estimate, CI, and p-value (though p-value is less informative than the CI).

14. **Assess the precision of the pooled estimate.** If the 95% CI is wide (e.g., includes both clinically meaningful benefit and harm), the pooled estimate is too imprecise to guide decision-making, even if p < 0.05.

### Phase 5 — Publication Bias and Sensitivity

15. **Construct a funnel plot:** x-axis = effect size, y-axis = study size (or precision). Expect a symmetric, inverted funnel if studies are unbiased. Asymmetry suggests small studies with null or opposite effects were not published. Perform Egger's regression test (p < 0.10 indicates asymmetry).

16. **Apply Duval & Tweedie's trim-and-fill method** (optional but recommended): estimate how many small, unpublished studies might be "missing" and recalculate the pooled effect with those studies imputed. If the trimmed-and-filled effect differs substantially from the observed pooled effect, publication bias is likely inflating the result.

17. **Conduct sensitivity analysis:** Repeat the pooled effect calculation:
    - Excluding the largest study (to check whether one large trial dominates)
    - Excluding studies at high risk of bias (see Phase 6)
    - Using fixed-effect model if random-effects was used (and vice versa)
    If the pooled effect is robust, these variations will yield similar results. Large swings signal fragility.

### Phase 6 — Risk of Bias Assessment

18. **Assess bias in each study using a standard tool:**
    - **Cochrane Risk of Bias tool (RoB 2)** for RCTs: evaluate selection bias (randomization process), performance bias (blinding of participants/personnel), detection bias (blinding of outcome assessor), attrition bias (completeness of follow-up), and reporting bias (selective outcome reporting).
    - **ROBINS-I** for observational studies: add confounding and selection bias domains.
    Rate each domain as "low," "some concerns," or "high" risk. Two raters assess independently; reconcile disagreements.

19. **Summarize risk of bias across studies.** Create a "traffic light" plot (green/yellow/red for low/some concerns/high) and a summary table. Note whether bias patterns cluster (e.g., all older studies are at high risk).

20. **In the sensitivity analysis (Step 17), exclude studies at high risk of bias and recalculate the pooled effect.** If removal of biased studies materially changes the conclusion, report both estimates and note the dependence on study quality.

## Evaluation Criteria

| Check | Pass |
|---|---|
| PICO elements are defined plainly before screening | Y/N |
| Inclusion/exclusion criteria are written precisely (not subjective) | Y/N |
| ≥2 independent raters screened and extracted data | Y/N |
| Search strategy documented with database names, queries, date ranges | Y/N |
| Effect size metric chosen and calculated consistently for all studies | Y/N |
| Both Q-statistic and I² reported (not just one) | Y/N |
| Heterogeneity sources examined via subgroup analysis or meta-regression | Y/N |
| Funnel plot and Egger's test performed | Y/N |
| Risk of bias assessed independently by ≥2 raters | Y/N |
| Sensitivity analysis includes removal of high-bias studies | Y/N |
| Pooled effect reported with 95% CI and sample size (not just p-value) | Y/N |

## Red Flags

- Search strategy is undocumented or limited to one database. Conclusions are then specific to that database's coverage, not to the question.
- Inclusion criteria were applied inconsistently or changed mid-analysis ("we added quasi-RCTs after seeing the data"). This is p-hacking at the study level.
- All studies are small, or all are from a single country/institution. Extreme heterogeneity or undisclosed bias is likely.
- I² is >75% but no heterogeneity analysis was performed. The pooled effect is uninterpretable — you are averaging apples and oranges.
- Funnel plot is absent or asymmetric but publication bias was not investigated. The aggregate effect may be inflated.
- Risk of bias assessment shows all studies as "low risk." Real studies have flaws. Uniformly positive assessments signal inadequate scrutiny or conflicts of interest.
- Sensitivity analysis was not performed, or results changed materially when high-bias studies were excluded but this was not reported prominently.
- The pooled estimate has a 95% CI so wide it spans both clinical benefit and harm. Precision is insufficient for recommendations.

## Output Format

```
## Meta-analysis Summary

**Research question (PICO):**
Population: ...
Intervention: ...
Comparison: ...
Outcome: ...

**Search and Screening:**
- Databases searched: [list]
- Search date range: [dates]
- Initial results: [n] | Deduplicated: [n]
- Title/abstract screening: [n] included, [n] excluded
- Full-text review: [n] included, [n] excluded (reasons: ...)
- Final sample: [n] studies, [n] participants

**Included Studies:**
| Study (Year) | Design | N | Intervention | Comparison | Effect size (95% CI) | Risk of bias |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

**Heterogeneity:**
- Q-statistic: [value] (p = [p-value], [homogeneous | heterogeneous])
- I²: [value]% ([low | moderate | high])
- Sources examined: [e.g., age, baseline risk, intervention dose]

**Pooled Effect ([Fixed-effect | Random-effects] model):**
Effect size: [point estimate] (95% CI: [lower]–[upper])
p-value: [value]
Interpretation: [clinically meaningful or not, precise or imprecise]

**Publication Bias:**
- Funnel plot: [symmetric | asymmetric]
- Egger's test: p = [value] ([no bias | evidence of bias])
- Trim-and-fill estimate (if performed): [new pooled effect], suggesting bias of approximately [n] studies

**Sensitivity Analysis:**
| Variant | Pooled effect (95% CI) | Change from main |
|---|---|---|
| Exclude largest study | ... | ... |
| Exclude high-risk bias studies | ... | ... |
| Fixed-effect model | ... | ... |

**Risk of Bias Summary:**
[Traffic light table or narrative summary of bias domains and patterns]

**Confidence**
<high | medium | low> — <justification: e.g., "high: large sample, low I², no publication bias detected"; "low: high heterogeneity unexplained, multiple high-bias studies, asymmetric funnel">
```
