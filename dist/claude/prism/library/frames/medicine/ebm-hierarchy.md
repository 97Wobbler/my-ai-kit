---
name: ebm-hierarchy
display_name: EBM Hierarchy
class: frame
underlying_class: native
domain: medicine
source: David Sackett et al., Centre for Evidence-Based Medicine, Oxford, 1990s
best_for:
  - Sorting medical evidence by methodological rigor and susceptibility to bias
  - Deciding which evidence base is sufficient to support a clinical decision
  - Identifying gaps when lower-level evidence dominates a question
one_liner: "Evidence-pyramid that tiers clinical evidence by methodological rigor."
---

# EBM Hierarchy

## Overview

The EBM Hierarchy sorts medical evidence into a ranked pyramid based on
methodological design and exposure to bias. Its core claim is that **not all
evidence contributes equally to clinical truth** — and different hierarchical
levels demand structurally different interpretations and thresholds for
action. A randomized controlled trial conducted in your patient population
carries more weight than a case series, not because researchers prefer
experiments, but because the design itself constrains the kinds of error that
can masquerade as signal. Sorting the evidence base by hierarchy prevents two
systematic failures: over-confident action on anecdote, and paralysis
waiting for a trial that will never come.

## Categories

1. **Case Report / Case Series**
   - Uncontrolled observation of one or a small number of individual patients, often with a specific outcome of interest.
   - No comparison group; outcome may have occurred regardless of intervention.
   - Discriminating criterion: the study involves no control arm and no randomization; observations are entirely confounded with natural history and secular trends.
   - Example: a report of five patients with pulmonary embolism who received a new anticoagulant and survived; a single case of an unexpected drug reaction.
   - Typical bias exposure: selection bias (only interesting cases reported), publication bias (failures unreported), natural history mistaken for treatment effect.

2. **Cohort Study**
   - Observational follow-up of exposed and unexposed (or more-vs-less exposed) groups, measured forward in time.
   - Patients are grouped by exposure or intervention status *after the fact*, then outcomes are compared.
   - Discriminating criterion: there is a comparison group defined by exposure level, and outcomes are tracked prospectively, but assignment to exposure is not randomized.
   - Example: comparing lung cancer risk in smokers vs. nonsmokers followed over a decade; comparing outcomes in patients who received a drug vs. those who did not, when clinicians chose treatment based on severity.
   - Typical bias exposure: confounding (sicker patients choose or receive the intervention), selection bias (loss to follow-up differs by group).

3. **Randomized Controlled Trial (RCT)**
   - Prospective comparison of randomly assigned groups, where one receives the intervention and the other receives control (placebo, standard care, or alternative).
   - Randomization breaks the link between patient characteristics and intervention assignment.
   - Discriminating criterion: patients are assigned to groups by chance, not by choice or clinical judgment.
   - Example: a trial where patients with hypertension are randomly assigned to a new drug or placebo, and blood pressure reduction is compared; a surgical trial where patients are randomly assigned to approach A or approach B.
   - Typical bias exposure: much lower than observational studies, but not zero (crossover, loss to follow-up, publication bias for positive results).

4. **Systematic Review (of RCTs or cohorts)**
   - Structured synthesis of multiple studies addressing the same question, using explicit criteria for inclusion and often pooling results.
   - A good systematic review includes a pre-registered protocol, searches multiple databases, assesses bias risk in each study, and is transparent about heterogeneity.
   - Discriminating criterion: the review applies systematic methods to multiple independent studies rather than relying on a single study or narrative judgment.
   - Example: a Cochrane review of all RCTs comparing beta-blockers to placebo for heart attack prevention; a meta-analysis of cohort studies on hormone replacement therapy and cardiovascular risk.
   - Typical bias exposure: lower than any single study (aggregates reduce random error), but vulnerable to publication bias (missing negative studies) and heterogeneity (studies may not be measuring the same thing).

5. **Meta-Analysis**
   - Statistical pooling of results from multiple studies, usually using standardized effect sizes and weighting.
   - A meta-analysis is often the analytical engine within a systematic review, but can also stand alone.
   - Discriminating criterion: results are combined quantitatively and reported as a single pooled estimate with confidence interval.
   - Example: a meta-analysis combining data from ten RCTs of aspirin for primary prevention, yielding a single pooled risk ratio; a meta-analysis of observational studies on coffee consumption and mortality.
   - Typical bias exposure: same as systematic review, plus the additional assumption that studies are similar enough to pool meaningfully (if heterogeneity is high, pooling can obscure truth rather than reveal it).

## Classification Procedure

1. Identify the clinical question and locate the evidence base addressing it.
2. For each study or summary, ask: **"Is there a comparison group (exposed vs. unexposed or intervention vs. control)?"**
   - If **no** → the evidence is a **Case Report / Case Series**.
   - If **yes**, go to step 3.
3. Ask: **"Was the assignment to intervention or exposure determined by randomization (chance)?"**
   - If **yes** → the evidence is an **RCT** (go to step 5).
   - If **no** → the evidence is a **Cohort Study** (go to step 5).
4. If you are reviewing a summary or synthesis of multiple studies, ask: **"Are results combined statistically into a single pooled estimate?"**
   - If **yes** → classify as **Meta-Analysis**.
   - If **no** (structured narrative synthesis only) → classify as **Systematic Review**.
5. Record the classification and note the number of studies of each type that address your question. If a lower-level evidence type dominates, flag this gap explicitly.

## Implications per Category

| Category | Evidence strength | What the clinician should do |
|---|---|---|
| **Case Report / Case Series** | Hypothesis-generating; high bias risk. | Use to **identify rare outcomes or unexpected signals**. Do not use alone to guide treatment decisions. Escalate to cohort/RCT before acting. |
| **Cohort Study** | Moderate; confounding and selection bias remain plausible. | Use when **RCTs are unavailable or unethical**. Adjust reasoning for unmeasured confounders. Stronger if exposure is early in life and outcome is distal. |
| **RCT** | High; randomization removes confounding. | Use as **gold standard for efficacy and safety**. Generalizability to your patient still requires judgment (trial population vs. your patient). |
| **Systematic Review** | Depends on included studies; reduces random error and publication bias. | Use to **synthesize the totality of evidence** and identify heterogeneity. Check for missing studies and risk-of-bias assessment. |
| **Meta-Analysis** | Highest statistical power; pooled estimates are precise. | Use for **final quantification** of effect, but only if heterogeneity is low or explained. Beware false precision if studies are not truly comparable. |

For a clinical agent, the practical implication is which **confidence threshold**
is defensible:
- Case Series alone → hypothesis only; do not recommend.
- Cohorts + case series → consider, with caution around confounding.
- Single RCT → recommend if consistent with pre-specified outcome and population-relevant.
- Multiple RCTs (or Systematic Review) → strong recommendation unless subgroup contradicts.
- Meta-Analysis of high-quality RCTs → highest confidence.

## Common Misclassifications

- **Case series mistaken for cohort.** A report of "all patients treated with X in our clinic" lacks a comparison group and is therefore a case series, not a cohort study, even if outcomes are tracked forward. The tell is the absence of a control or comparison arm defined by exposure level.
- **Confounded cohort mistaken for RCT.** A study with comparison groups but where sicker patients received the intervention has all the structure of a cohort study but none of the causal inference of an RCT. The tell is that the two groups differ at baseline on prognostically important variables.
- **Narrative review mistaken for systematic review.** A narrative summary of "the literature on X" is not a systematic review unless it used explicit inclusion criteria, searched multiple databases, and assessed bias risk. The tell is the absence of a protocol and transparent search strategy.
- **Meta-analysis of poor-quality studies mistaken for meta-analysis of RCTs.** Pooling five confounded cohort studies into a single meta-analysis gives the appearance of high evidence (a single forest plot with a narrow confidence interval) but does not resolve the underlying confounding. The tell is checking the source studies and finding they lack randomization.
- **Heterogeneous meta-analysis mistaken for homogeneous.** A pooled estimate from studies with widely different patient populations, interventions, or outcomes is precise but not meaningful — the "average" effect may not apply to anyone. The tell is an I² statistic above 75% combined with inability to explain the variation by subgroup.
