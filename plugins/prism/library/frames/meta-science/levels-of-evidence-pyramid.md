---
name: levels-of-evidence-pyramid
display_name: Levels of Evidence Pyramid
class: frame
underlying_class: native
domain: meta-science
source: origin uncertain; widely used in evidence-based medicine and systematic review methodology
best_for:
  - Sorting a claim or finding by the strength and type of evidence supporting it
  - Determining which response pattern (acceptance, skepticism, further investigation) is warranted
one_liner: "Hierarchy of evidence confidence based on type and quality."
---

# Levels of Evidence Pyramid

## Overview

The Levels of Evidence Pyramid sorts claims and findings into a hierarchy based on the **type and quality of evidence** that supports them. Its core claim is that different levels of evidence warrant **structurally different degrees of confidence and follow-up action** — and treating weak evidence as strong evidence (or vice versa) is a systematic source of misalignment between claim and justification. The pyramid reflects an epistemological ordering: evidence nearer the base (individual cases, mechanisms, expert opinion) is more abundant but more prone to bias and confounding; evidence nearer the apex (systematic reviews, meta-analyses) is rarer but more robust to alternative explanations.

## Categories

1. **Expert Opinion / Case Reports**
   - Single observations or the reasoned judgment of an authority without systematic comparison or quantification.
   - Discriminating criterion: the evidence is anecdotal, unsystematic, or derived from opinion rather than from a controlled comparison of outcomes.
   - Example: a clinician's report of an unusual adverse effect in a single patient; a domain expert's assertion based on experience.

2. **Observational Studies (Cohort, Case-Control)**
   - A study that **tracks outcomes in groups** without random assignment, or compares groups formed by exposure history rather than allocation.
   - Presence of comparison groups and measured outcomes, but **susceptible to confounding** (unmeasured or uncontrolled variables that explain the observed association).
   - Discriminating criterion: the study has a control arm and measures outcomes, but causality cannot be isolated because groups differ in ways other than the exposure.
   - Example: following smokers and non-smokers forward in time and measuring lung cancer incidence; comparing people who took a supplement to those who did not.

3. **Quasi-Experimental Studies (Before-After, Interrupted Time Series)**
   - Studies that measure an outcome **before and after** an intervention, often in real-world settings, without a concurrent control group.
   - Discriminating criterion: there is a measurable change, but alternative explanations (secular trends, regression to the mean, concurrent interventions) cannot be ruled out because there is no untreated comparison.
   - Example: measuring absenteeism before and after implementing a workplace wellness program in a single company; hospital readmission rates before and after a new discharge protocol.

4. **Randomized Controlled Trials (RCTs)**
   - A prospective study in which **participants are randomly assigned** to an intervention or control group, and outcomes are measured and compared.
   - Random assignment ensures groups are probabilistically equivalent on both measured and unmeasured confounders at baseline.
   - Discriminating criterion: the study has explicit random allocation, an untreated or standard-treatment control arm, and prospective outcome measurement.
   - Example: half the participants receive a drug, half receive placebo; neither knows which group they are in; both are followed and outcomes compared.

5. **Systematic Reviews and Meta-Analyses**
   - A **comprehensive, reproducible synthesis** of evidence from multiple studies, usually combined quantitatively, following a pre-specified protocol.
   - Discriminating criterion: the synthesis follows a transparent, pre-registered methodology; studies are searched exhaustively; inclusion/exclusion criteria are stated a priori; and results are pooled or synthesized with explicit handling of heterogeneity.
   - Example: a Cochrane review identifying all RCTs of a treatment, extracting data, assessing bias risk, and pooling effect sizes; a systematic review of observational studies on an environmental exposure.

## Classification Procedure

1. Identify the **claim or assertion** you are evaluating (e.g., "Drug X reduces mortality in condition Y").
2. Ask: **"Is this based on a synthesis of multiple studies using a pre-specified protocol?"**
   - If **yes** → Systematic Review / Meta-Analysis.
   - If **no**, go to step 3.
3. Ask: **"Is this based on a study in which people were randomly assigned to groups?"**
   - If **yes** → Randomized Controlled Trial.
   - If **no**, go to step 4.
4. Ask: **"Is this based on a study that measured outcomes in comparison groups (some exposed, some not)?"**
   - If **yes, with random assignment absent**, go to step 5.
   - If **no** (no control group at all), go to step 6.
5. Ask: **"Were the groups formed by tracking forward from exposure, or backward from outcome?"**
   - If **forward** → Cohort Study.
   - If **backward** → Case-Control Study.
   - (Both are Observational Studies.)
6. Ask: **"Is the evidence a measurement before and after an intervention in the same population, or a single observation?"**
   - If **before-and-after, no control** → Quasi-Experimental.
   - If **single case or expert opinion** → Expert Opinion / Case Report.

## Implications per Category

| Category | Confidence warranted | Follow-up action |
|---|---|---|
| **Expert Opinion / Case Report** | Low; prone to bias and chance. | Treat as a **signal** requiring confirmation; do not base policy or practice on single cases. Seek higher-level evidence before committing resources. |
| **Observational Studies** | Moderate; causality is suggested but not proven. | Examine **confounding and bias**; look for consistency across multiple observational studies; consider RCT if the observational signal is strong and the question is important. |
| **Quasi-Experimental** | Moderate-to-good; real-world relevance, but causality weakened by lack of control. | Check for **alternative explanations** (secular trends, concurrent events); consider repeating in a different setting or population to strengthen generalization. |
| **Randomized Controlled Trials** | Good-to-strong; causality is well-supported if conducted well. | Examine **implementation fidelity and generalizability**; pool with other RCTs for meta-analysis; consider applicability to the target population. |
| **Systematic Reviews / Meta-Analyses** | Strongest (if bias risk is low). | Treat as **guidance for practice or policy** unless the review identifies substantial heterogeneity or bias; re-assess periodically as new trials emerge. |

**Practical rule:** Use the **highest-level evidence available** for the question. If only expert opinion exists, acknowledge the weakness; do not cite it as though it were trial-level evidence. When multiple levels are available, weight them accordingly and note any discordance between them.

## Common Misclassifications

- **Case report mistaken for observational study.** A striking anecdote ("Patient reported relief after X") is treated as though it were a systematic observation of many cases. The tell is that the author is describing a single memorable case, not comparing frequencies across a series.
- **Observational study mistaken for RCT.** Treating a cohort study as if random assignment had occurred when only exposure was observed. The tell is the presence of uncontrolled confounders that plausibly explain the observed association (e.g., healthier people self-select into exercise).
- **Quasi-experimental mistaken for RCT.** A before-after comparison in the same population is stronger than a case report but weaker than an RCT because secular trends, regression to the mean, and concurrent interventions are not ruled out. The tell is the absence of a concurrent untreated control group.
- **Meta-analysis mistaken for systematic review.** A quantitative pooling of studies (meta-analysis) is not the same as a structured synthesis that may remain qualitative. A meta-analysis is a form of systematic review if it followed a protocol, but not all systematic reviews include meta-analysis.
- **Treating hierarchy as linear quality.** A well-conducted observational study may provide stronger evidence than a poorly designed RCT; the hierarchy reflects study design, not absolute truth. The tell is confusing "level of evidence" (study design) with "risk of bias" (study quality), which are separate dimensions.
