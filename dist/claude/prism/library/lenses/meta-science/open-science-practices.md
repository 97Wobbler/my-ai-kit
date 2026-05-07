---
name: open-science-practices
display_name: Open Science Practices
class: lens
underlying_class: native
domain: meta-science
source: Open Science Framework (OSF), Center for Open Science; preregistration methodology (Nosek & Ebersole, 2016); open data principles (Wilkinson et al., 2016)
best_for:
  - Assessing whether a research project follows reproducibility-enabling practices
  - Identifying which transparency mechanisms are absent or partial
  - Evaluating whether results can be independently verified
one_liner: "Assess research credibility and transparency through preregistration, open data, and replication."
---

# Open Science Practices

## Overview
Open Science Practices audit whether a research project has implemented mechanisms that make its methods, data, and findings independently verifiable and reproducible. The framework checks across four domains: preregistration (commitment to methods before data collection), open data (accessibility of raw data and materials), transparent reporting (disclosure of all analyses and results, including null findings), and reproducibility infrastructure (code availability, version control, computational documentation). Practitioners use this lens when evaluating published research, assessing internal research quality, or designing studies that need to withstand reproducibility scrutiny.

## Analytical Procedure

### Phase 1 — Identify Research Stage and Scope

1. **Determine what stage the research is in:**
   - Pre-data collection (design phase) — can assess preregistration
   - Post-data collection, pre-publication — can assess data documentation and analysis transparency
   - Published — can assess all four domains

2. **List the research claims or hypothesis groups.** For example: "We tested H1 (main effect), H2 (mediation pathway), H3 (moderation by treatment)." Each major claim gets evaluated separately.

### Phase 2 — Preregistration

3. **Check whether a preregistration document exists** (on OSF, AsPredicted, or discipline-specific registry).
   - If yes: Document the registry, registration date, and date of first data collection.
   - If no: Note that the research lacks prospective commitment.

4. **For each registered hypothesis or analysis plan:**
   - Does it specify the primary outcome variable *before* data collection?
   - Does it specify the analysis method and sample size calculation *before* data collection?
   - Does it distinguish between pre-specified (confirmatory) and exploratory analyses?
   - Are deviations from the pre-registration documented and justified?

5. **Score preregistration completeness:**
   - Full: Primary hypotheses, sample size, analysis plan, and outcome variables all preregistered before data collection.
   - Partial: Some elements specified in advance; others added post-hoc.
   - None: No prospective commitment document exists.

### Phase 3 — Open Data and Materials

6. **Check whether raw data is publicly available** (on OSF, GitHub, institutional repository, or discipline-specific archive).
   - Identify the location and access level (open, restricted with justification, or absent).
   - Note any anonymization, data safety, or privacy constraints that limit full release.

7. **For the available data, verify that it is machine-readable and documented:**
   - Are there codebooks describing every variable, its type, and valid range?
   - Are missing data patterns explained (e.g., "participant withdrew," "equipment failure")?
   - Are exclusion criteria and their frequency documented?

8. **Check whether analysis code is available:**
   - Is the code (R, Python, Stata, etc.) that produced the reported statistics provided?
   - Is the code version-controlled (git history available)?
   - Can someone unfamiliar with the research run the code and reproduce the numbers?

9. **Check whether materials are available:**
   - Are stimuli (images, texts, survey items) openly shared or available on request?
   - Are experimental protocols documented step-by-step?

### Phase 4 — Transparent Reporting

10. **Examine the reported results against the preregistration (if it exists):**
    - Were all preregistered analyses reported?
    - Are effect sizes, confidence intervals, and p-values reported for both significant and null findings?
    - Is the distinction between confirmatory and exploratory results clear in the text?

11. **Check whether null results and negative findings are reported:**
    - Are hypotheses that were not supported still described in the results?
    - Or do the results selectively report only significant findings?

12. **Verify statistical reporting standards:**
    - Are sample sizes reported for each analysis?
    - Are assumptions of statistical tests (normality, homogeneity of variance) checked and reported?
    - Are multiple comparison corrections applied if applicable?

### Phase 5 — Reproducibility Infrastructure

13. **Assess computational reproducibility:**
    - If computational work is involved, is the exact software version (including package/library versions) documented?
    - Are random seeds specified for stochastic analyses?
    - Is a dependency list provided (requirements.txt, environment.yml, Docker image)?

14. **Check for funding and conflict-of-interest disclosure:**
    - Are all funding sources listed?
    - Are conflicts of interest (financial or intellectual) disclosed?

## Evaluation Criteria

| Element | Full (2 pts) | Partial (1 pt) | Absent (0 pts) |
|---|---|---|---|
| Preregistration | Primary hypotheses & analysis plan registered before data collection | Some hypotheses or methods preregistered; others post-hoc | No prospective commitment document |
| Open Data | Raw data publicly available with codebook and exclusion criteria documented | Data available but with incomplete documentation; or restricted access with documented reason | Data not made available |
| Analysis Code | Complete code provided, version-controlled, executable | Code fragments or pseudocode provided; not version-controlled | No code available |
| Materials | All stimuli and protocols openly available | Some materials available; others on request | Materials not shared |
| Transparent Reporting | All preregistered analyses reported; null results included; distinction between confirmatory/exploratory clear | Most preregistered analyses reported; some null findings omitted | Selective reporting; no distinction between preregistered and exploratory |
| Computational Reproducibility | Software versions, random seeds, dependencies fully specified | Some version info provided; missing seeds or dependencies | No computational specification |

**Scoring:** Sum across all elements. 12 = high open science maturity; 6–11 = moderate transparency with gaps; 0–5 = minimal transparency.

## Red Flags

- Preregistration date is *after* data collection or very close to submission. A preregistration backdated or filed retroactively is not a real commitment.
- Data is "available on request" but requests are slow or denied without justification. Availability that requires gatekeeping is not genuinely open.
- Code runs but produces different numbers than the paper. Bugs or manual corrections were made post-hoc without explanation.
- Results section reports only p-values without effect sizes or confidence intervals. This obscures practical significance and enables p-hacking.
- A large gap between the number of analyses run (evident from code or appendix) and those reported in the main text. Missing analyses suggest selective reporting.
- Conflicting versions of "the analysis" in different places (preregistration, methods section, code, appendix). Changes are not justified or tracked.
- Raw data contains identifiable information, but no privacy or consent protocol is documented. This violates ethics even if the data is "open."

## Output Format

```
## Open Science Practices Assessment

**Research claims being evaluated:**
<List each hypothesis or major claim>

### Preregistration
- Registry and date: <location | "none">
- Preregistered before data collection: <yes | no | partial>
- Preregistered elements: <list: hypotheses, sample size, analysis plan, outcomes>
- Post-hoc deviations: <description and justification, or "none">
- Score: <full | partial | none>

### Open Data and Materials
- Raw data availability: <location | "none">
- Data documentation: <codebook exists | partially documented | not documented>
- Anonymization/restrictions: <none | justified privacy/ethical constraints>
- Analysis code availability: <location | "none">
- Code is version-controlled: <yes | no>
- Code is executable: <yes | no | untested>
- Materials (stimuli/protocols): <available | on-request | not shared>

### Transparent Reporting
- All preregistered analyses reported: <yes | no | partial>
- Null/negative results included: <yes | no>
- Distinction between confirmatory and exploratory: <explicit | implied | absent>
- Effect sizes and CIs reported: <all | most | few | none>
- Multiple comparisons correction applied (if applicable): <yes | no | N/A>

### Reproducibility Infrastructure
- Software versions documented: <yes | no>
- Random seeds/stochastic specifications: <yes | no | N/A>
- Dependency list (environment, packages): <yes | no>
- Funding and CoI disclosure: <complete | partial | absent>

### Strengths
<List 2–3 open science practices the research implements well>

### Gaps
<List 2–3 areas where transparency or reproducibility is limited>

### Recommendations
1. <Highest-impact transparency gap to address>
2. <Second priority>
3. <Third priority>

### Overall Score
<0–5 (minimal) | 6–11 (moderate) | 12+ (high)>

### Confidence
<high | medium | low> — <justification based on completeness of available documentation and accessibility of artifacts>
```
---
