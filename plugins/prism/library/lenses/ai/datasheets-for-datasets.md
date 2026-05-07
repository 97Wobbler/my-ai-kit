---
name: datasheets-for-datasets
display_name: Datasheets for Datasets
class: lens
underlying_class: native
domain: ai
source: Timnit Gebru, Jamie Buolamwini, et al. (arXiv:1803.09010, 2018)
best_for:
  - Documenting dataset provenance, composition, and limitations before use
  - Identifying potential harms and biases embedded in training data
  - Enabling reproducibility and informed consent in ML projects
one_liner: "Systematic dataset documentation (provenance, composition, constraints) to surface risk and bias early."
---

# Datasheets for Datasets

## Overview
A datasheet is a structured document that records the motivation, composition, collection process, labeling, uses, and limitations of a dataset. It operates on any dataset intended for machine learning, from raw collection through deployment. Practitioners use it to surface hidden assumptions about how data was gathered, who it represents, and what harms or biases it may encode — information typically locked in researchers' heads or scattered across lab notebooks. The discipline is completeness: skipping a section means a critical risk went undocumented.

## Analytical Procedure

### Section 1 — Motivation

1. **Document why the dataset was created.** Write the original research question or business objective. If motivation evolved, record the original and current versions.

2. **Record who created the dataset and when.** Names, institutions, funding sources, and date ranges. Include anyone who made decisions about what to collect.

3. **Identify if the dataset was created in response to a perceived need.** Was there a gap in existing datasets? Was the existing data biased or inadequate? Write the specific gap or limitation the dataset was meant to address.

### Section 2 — Composition

4. **Count instances.** Total number of datapoints, broken down by major categories (e.g., number of images per class, documents per language, records per time period).

5. **Describe the composition by demographic, geographic, or other salient axes.** For each axis, state the granularity of the breakdown:
   - Example: "Images annotated by gender presentation: 45% male-presenting, 48% female-presenting, 7% non-binary or unclear. Gender inferred visually by annotators, not self-reported."
   - Flag any axis where you *cannot* provide a breakdown — this is itself informative (a blank spot).

6. **Document what is NOT in the dataset.** Explicitly state populations, geographies, time periods, or phenomena excluded from collection. Do not assume this will be obvious to future users.

7. **List all label classes and their frequencies.** For multi-label or hierarchical labels, show the structure and frequency of each label type.

### Section 3 — Collection Process

8. **Describe the data collection mechanism.** Was it automated (sensor, API, scrape)? Manual (annotators, crowdsourced, interview)? A mix? Write who did the collection and under what constraints (time pressure, location, incentives).

9. **Document the sampling strategy.** How were instances selected for inclusion?
   - Stratified by category? Random? Convenience sample? Biased by availability?
   - If crowdsourced: how many annotators per instance, how were annotators recruited, what were they paid, what expertise was required?

10. **Record all preprocessing and filtering steps.** Each step that removed or transformed data should be explicit:
    - "Deleted images smaller than 100×100 pixels" — now 12% of raw captures are gone.
    - "Deduplicated using MD5 hash" — 3% of raw instances were removed.
    - Each deletion changes what the dataset represents.

### Section 4 — Annotation and Labeling

11. **For human-annotated data: document the annotation process.**
    - Instructions given to annotators (verbatim or summary).
    - Annotation interface and tool.
    - Inter-annotator agreement score (Cohen's kappa, Fleiss' kappa, or equivalent).
    - Number of rounds of annotation (if multiple).
    - Any disagreement resolution process (voting, arbitration, deletion).

12. **Document annotator demographics and incentives if known.**
    - Age range, location, native language, prior experience with the task.
    - Payment per annotation, total compensation.
    - Whether annotators knew the intended use of the data.

13. **If labels came from automated sources (e.g., user behavior, metadata, model predictions), describe the labeling function.**
    - What proxy was used to infer the true label?
    - How reliable is that proxy?
    - Has the proxy been validated against ground truth?

### Section 5 — Uses and Misuses

14. **Document the intended use(s) of the dataset.** What tasks, domains, or populations is this dataset designed for? Write concretely: "training a medical imaging classifier for detecting pneumonia in chest X-rays of adult patients in the US."

15. **Explicitly anticipate misuses.** What harmful, unintended, or out-of-distribution uses might someone attempt?
    - Example: Dataset built for classifying plant disease should be flagged if someone might use it to identify non-native or protected species.
    - Example: A dataset of mugshots should be flagged for risk of use in biased surveillance systems.
    - Example: A dataset of customer behavior should be flagged if de-anonymization or re-identification is possible.

16. **Document any known limitations on future use.** Regulatory, ethical, or technical constraints:
    - Can the dataset be commercialized?
    - Does it contain personally identifiable information (PII)?
    - Are there licensing restrictions on derived works?

### Section 6 — Maintenance, Distribution, and Limitations

17. **Describe how the dataset will be maintained.** Will it be updated? Deprecated? If updated, what is the versioning scheme? Record date of last update.

18. **Document how the dataset is distributed.** Is it public, requires registration, access-controlled, or proprietary? What are the terms of use?

19. **Record all known limitations and failure modes.** Be specific:
    - "The dataset underrepresents rural areas" (not "geographic bias").
    - "Annotations by non-expert workers had 0.63 agreement; expert-only subset had 0.89" (not "some annotations are unreliable").
    - "All data collected in winter months; seasonal variation in X is not represented" (not "temporal bias").

20. **Document any ethical considerations or potential harms.** Has the dataset been flagged for reproducing historical biases? Could the dataset enable surveillance, discrimination, or other harms? Record the concern and any mitigation.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Sections 1–6 each have entries; no section is empty | Y/N |
| Composition includes at least one demographic or salient axis with granular breakdown | Y/N |
| All preprocessing/filtering steps that removed data are documented | Y/N |
| For human-annotated data: inter-annotator agreement is reported | Y/N |
| Intended use is concrete (not generic "machine learning") | Y/N |
| At least two potential misuses are explicitly anticipated | Y/N |
| Limitations are stated with specificity, not vague hedging | Y/N |
| Ethical considerations or known harms are recorded | Y/N |

## Red Flags

- Composition section has no demographic or geographic breakdown. This indicates the creators did not examine representativeness — a critical gap.
- "No preprocessing" or "raw data." Every dataset has preprocessing; if none is documented, it either wasn't tracked or is being hidden.
- Inter-annotator agreement missing or not calculated. Label quality is unknowable without it.
- "Intended use: general machine learning" or "any classification task." This is too broad and suggests the creators did not think carefully about downstream impact.
- Misuses section is absent or says "none known." Every dataset has misuse risks; absence suggests the creators did not interrogate them.
- Limitations section is generic ("some bias," "limited diversity"). Specific, measurable limitations are required to be actionable.
- No record of who made collection decisions or annotation decisions. Accountability requires knowing who chose what and when.

## Output Format

```
## Datasheets for Datasets Assessment

### Section 1 — Motivation
**Research question / objective:**
<...>

**Creators and timeline:**
<...>

**Gap this dataset addresses:**
<...>

### Section 2 — Composition
**Instance counts:**
- Total: <number>
- Breakdown by category:
  - <category>: <count> (<percentage>)
  - <category>: <count> (<percentage>)

**Composition by salient axis:**
| Axis | Category | Count | Percentage | Notes |
|---|---|---|---|---|
| <axis> | <category> | <n> | <%> | <method of collection/known gaps> |

**What is NOT in this dataset:**
- <population / geography / time period / phenomenon>
- <...>

**Label classes and frequencies:**
| Label | Count | Percentage |
|---|---|---|
| <...> | <n> | <%> |

### Section 3 — Collection Process
**Collection mechanism:**
<automated / manual / mixed — describe who, constraints>

**Sampling strategy:**
<stratified / random / convenience — describe how instances were chosen>

**Preprocessing and filtering steps:**
| Step | Instances removed | Percentage | Rationale |
|---|---|---|---|
| <description> | <number> | <%> | <why> |

### Section 4 — Annotation and Labeling
**Annotation process (if human-labeled):**
- Instructions: <summary or verbatim>
- Interface: <tool name or description>
- Inter-annotator agreement: <metric and score>
- Rounds: <number>
- Disagreement resolution: <voting / arbitration / deletion>

**Annotator profile (if known):**
- Demographics: <age, location, language, experience>
- Incentives: <payment per annotation, total compensation>
- Awareness of downstream use: <yes / no / unknown>

**Automated labeling function (if applicable):**
- Proxy used: <...>
- Validation against ground truth: <...>

### Section 5 — Uses and Misuses
**Intended use:**
<concrete task, domain, population — be specific>

**Anticipated misuses:**
1. <risk and why>
2. <risk and why>

**Constraints on future use:**
- Commercialization: <allowed / restricted / prohibited>
- PII: <present / redacted / none>
- Licensing: <terms>

### Section 6 — Maintenance, Distribution, Limitations
**Maintenance and versioning:**
<update policy, version scheme, last update date>

**Distribution:**
<public / registered access / proprietary — terms of use>

**Known limitations:**
| Limitation | Impact | Affected populations / domains |
|---|---|---|
| <specific limitation, not vague> | <consequence> | <who is affected> |

**Ethical considerations and potential harms:**
- <harm or bias and mitigation (if any)>
- <...>

### Confidence
<high/medium/low> — <justification (e.g., "high — all six sections completed with granular demographic breakdown and explicit anticipation of misuses"; "medium — composition lacks geographic axis; inter-annotator agreement not calculated"; "low — significant sections empty; ethical considerations unaddressed")>
```
---
