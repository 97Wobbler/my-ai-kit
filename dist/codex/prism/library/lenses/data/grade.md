---
name: grade
display_name: GRADE
class: lens
underlying_class: native
domain: data
source: Shea & Amobi (evidence-based medicine); adapted for data quality assessment
best_for:
  - Assessing credibility of empirical claims and research findings
  - Ranking evidence strength in data-driven decision-making
  - Identifying gaps in supporting evidence for analytical conclusions
one_liner: "Systematically rate evidence quality to quantify confidence in conclusions."
---

# GRADE

## Overview
GRADE (Grading of Recommendations Assessment, Development and Evaluation) evaluates the quality of evidence underpinning a claim by examining study design, consistency, directness, precision, and risk of bias. Instead of treating all data sources as equivalent, it assigns each piece of evidence a quality tier from high (confidence in true effect) to very low (little confidence). Practitioners use it when a conclusion rests on mixed or imperfect evidence and stakeholders need to know whether to act decisively or with caution.

## Analytical Procedure

1. **State the claim and its evidence set.** Write the analytical claim in one sentence. List all sources of evidence cited to support it (datasets, studies, analyses, prior work). Number them for reference.

2. **For each evidence source, identify the study design (or data collection method):**
   - Randomized controlled trial / experimental design with random assignment
   - Prospective cohort study / time-series analysis with pre-specified outcomes
   - Case-control or retrospective cohort study
   - Observational data without controls / cross-sectional analysis
   - Case reports, anecdotes, or expert opinion
   Mark the baseline quality tier:
     - **High:** RCTs or equivalent experiments
     - **Moderate:** Well-executed prospective studies without randomization
     - **Low:** Retrospective or observational studies
     - **Very Low:** Case reports, expertise, or unvalidated sources

3. **Downgrade each source for risk of bias.** For the evidence at hand, check:
   - **Selection bias:** Were cases chosen to represent the full population, or filtered for particular outcomes?
   - **Measurement bias:** Were outcomes assessed consistently and without knowledge of group assignment? Could the analyst have unconsciously favored one result?
   - **Confounding:** Could an unmeasured or uncontrolled variable explain the observed effect instead of the causal claim?
   - **Reporting bias:** Was the analysis plan registered before analysis began, or was it adjusted based on results observed?
   If any are present, downgrade one tier. If multiple are present, downgrade up to two tiers total.

4. **Assess consistency across sources.** Compare the direction and magnitude of effects across all evidence:
   - **Consistent:** All sources point the same direction; effect sizes are similar
   - **Inconsistent:** Some sources point opposite directions, or effect sizes vary widely
   If inconsistent, downgrade the overall evidence one tier. If consistency cannot be assessed (only one source), note it.

5. **Check directness.** Does the evidence directly measure the outcome claimed, or does it infer it?
   - **Direct:** The evidence measures the exact quantity or outcome stated in the claim
   - **Indirect:** The evidence measures a proxy, surrogate, or related outcome
   If indirect, downgrade one tier. If partially indirect (some sources direct, some not), apply half a tier where possible.

6. **Examine precision.** Does the evidence narrow the plausible range of the effect, or is the range too wide to be useful?
   - Count the number of observations (rows in datasets, participants in studies).
   - Calculate or identify the confidence interval (CI) or margin of error around the claimed effect.
   - If the CI spans zero or a range wide enough to flip the decision (e.g., "could be harmful or beneficial"), downgrade one tier.
   - If precision is high (CI is narrow), no downgrade.

7. **Check for publication or analysis bias.** Is there evidence that negative or null results were suppressed?
   - Look for asymmetry: many small positive studies but few negative ones (funnel plot analysis if multiple sources).
   - Ask: would a null result have been published or analyzed?
   - Ask: was the analysis hypothesis pre-registered?
   If strong suspicion of suppression, downgrade one tier.

8. **Assign final quality rating to the body of evidence:**
   - **High:** Effect is true; further research is unlikely to change confidence.
   - **Moderate:** Effect is likely true; further research may change confidence.
   - **Low:** Effect may be true; further research is likely to change confidence.
   - **Very Low:** Very uncertain; further research will very likely change confidence.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Claim and all evidence sources are explicitly listed | Y/N |
| Each source assigned initial quality tier based on study design | Y/N |
| Bias assessment performed for each source (at least 2 dimensions checked) | Y/N |
| Consistency across sources evaluated and documented | Y/N |
| Directness of evidence explicitly addressed | Y/N |
| Precision (sample size and CI) examined for each source | Y/N |
| Publication bias assessed or reasoning for why it is not a concern | Y/N |
| Final overall quality rating assigned (High/Moderate/Low/Very Low) | Y/N |

## Red Flags

- All evidence is rated "High" quality. Real-world claims rarely rest on perfect evidence; this suggests the bias assessment was lenient or the analyst has confirmation bias.
- No source was downgraded for bias. Every study has limitations; missing bias is a sign the method wasn't applied rigorously.
- Consistency is "inconsistent" but no downgrade was applied, or the downgrade was not justified. Contradictory evidence must move the needle.
- Precision is not calculated. Statements like "the study had many participants" are not sufficient; confidence intervals must be examined.
- The final rating contradicts the intermediate findings. If sources are mostly Low quality with bias issues, the overall rating cannot be Moderate.
- Directness was not assessed. Proxies and surrogates are common in data work; overlooking them inflates confidence.

## Output Format

```
## GRADE Evidence Assessment

**Claim:**
<one sentence>

### Evidence Inventory
| # | Source | Study Design | Baseline Tier |
|---|---|---|---|
| 1 | <...> | <RCT / Cohort / Observational / Other> | <High/Moderate/Low/Very Low> |
| 2 | ... | ... | ... |

### Bias Assessment
| Source | Selection Bias | Measurement Bias | Confounding | Reporting Bias | Downgrade | Final Tier |
|---|---|---|---|---|---|---|
| 1 | <Yes/No, detail> | <Yes/No, detail> | <Yes/No, detail> | <Yes/No, detail> | <0–2 tiers> | <Tier> |
| 2 | ... | ... | ... | ... | ... | ... |

### Consistency
**Finding:** <Consistent / Inconsistent / Not assessed>
**Detail:** <direction and magnitude of effects across sources>
**Downgrade applied:** <Yes/No, justify>

### Directness
**Finding:** <Direct / Indirect / Mixed>
**Detail:** <does evidence measure the exact outcome, or infer it?>
**Downgrade applied:** <Yes/No, justify>

### Precision
| Source | N | Confidence Interval / Margin of Error | Sufficient? | Downgrade? |
|---|---|---|---|---|
| 1 | <...> | <...> | <Yes/No> | <Yes/No> |
| 2 | ... | ... | ... | ... |

### Publication Bias
**Assessment:** <Suspected / Not suspected / Unclear>
**Reasoning:** <evidence of asymmetry, pre-registration, publication history>
**Downgrade applied:** <Yes/No>

### Overall Evidence Quality

**Final Rating:** <High | Moderate | Low | Very Low>

**Justification:**
- Baseline design quality: <...>
- Bias and downgrade summary: <...>
- Consistency: <...>
- Directness: <...>
- Precision: <...>
- Publication bias: <...>

### Confidence
<high/medium/low> — <justification. E.g., "High: all sources are prospective with low bias, narrow CI, and consistent effect direction. Low: only retrospective data, wide CI, and contradictory results across analyses.">
```
