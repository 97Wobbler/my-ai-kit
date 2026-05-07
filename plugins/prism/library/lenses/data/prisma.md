---
name: prisma
display_name: PRISMA Checklist
class: lens
underlying_class: native
domain: data
source: Moher, Liberati, Tetzlaff, Altman; Preferred Reporting Items for Systematic Reviews and Meta-Analyses (2009)
best_for:
  - Validating completeness of systematic review reporting
  - Identifying gaps in transparency before publication
  - Benchmarking review quality against reporting standards
one_liner: "27-item reporting standard for systematic literature reviews."
---

# PRISMA Checklist

## Overview

PRISMA is a 27-item checklist that enforces transparent, complete reporting of systematic reviews and meta-analyses. It operates on the written manuscript (or pre-submission draft) of a review. Practitioners use it to audit whether the review is reproducible — that readers have enough detail to understand what was searched, who decided what to include, and how data were synthesized. Missing items are not flaws in the *research*; they are flaws in *communication* of the research.

## Analytical Procedure

### Phase 1 — Locate and Extract Each Section

1. **Obtain the manuscript.** Work from the most recent version, ideally as a single document with visible section headers (Abstract, Introduction, Methods, Results, Discussion).

2. **Skim for the major sections.** Identify where Title, Abstract, Introduction, Methods, Results, Discussion, and Funding disclosure appear. Note page/paragraph numbers. If a section is missing, mark it as "not found" — this is data.

3. **Create a PRISMA item tracker.** Use the 27-item list below. For each item, you will record: (a) whether it is present, (b) where it appears (section, paragraph), (c) how thoroughly it is addressed.

### Phase 2 — Check Each PRISMA Item

For each of the 27 items below, apply the following procedure:

4. **Read the item definition carefully.** PRISMA items are often misunderstood because they use precise language. For example, "reporting the protocol registration" does not mean mentioning that a protocol existed; it means stating the specific registry and registration ID.

5. **Search the manuscript for the item.** Use keyword matching first (e.g., search for "registration," "PROSPERO," "protocol"), then read the relevant section to verify the content matches the item requirement.

6. **Score as Present (✓), Partial (◐), or Absent (✗):**
   - **Present (✓):** The item requirement is explicitly stated or directly evident.
   - **Partial (◐):** The item is mentioned but lacks critical detail (e.g., the protocol is mentioned but not registered, or inclusion criteria are vague).
   - **Absent (✗):** The item is not addressed or is addressed too briefly to evaluate.

7. **Cite the exact location.** Record the section and paragraph where evidence for the item appears. If absent, write "not found."

### The 27 PRISMA Items

**Title & Abstract**
1. Title: Identifies the report as a systematic review and meta-analysis
2. Structured abstract: Reports background, objectives, data sources, study eligibility, study selection/data extraction, risk of bias assessment, synthesis methods, results, limitations, conclusions, and registration

**Introduction**
3. Rationale: Describes the rationale for the review in the context of what is already known
4. Objectives: Provides explicit statement of questions being addressed with reference to PICO (Population, Intervention, Comparison, Outcome)

**Methods**
5. Protocol registration: States whether a protocol was registered and where (registry name + registration ID)
6. Eligibility criteria: Specifies study characteristics (PICO, follow-up length, study design) and report characteristics (publication status, language, date) that determine inclusion/exclusion
7. Information sources: Lists databases, registers, websites, grey literature sources, and hand-search strategies with date ranges for each
8. Search strategy: Presents the full search strategy for at least one database, including all keywords and operators
9. Study selection process: Describes the process for screening records and full texts, including how many reviewers performed each step and how disagreements were resolved
10. Data extraction: Describes the data extracted, how data were extracted from each study, who extracted them, and how disagreements were resolved
11. Study characteristics: Lists the characteristics extracted from each study (e.g., funding source, trial registration, baseline balance)
12. Risk of bias assessment: Specifies the tool(s) used, the domains assessed, how judgments were made, and whether assessments were done by one or two reviewers
13. Effect measures: Defines the primary effect measure (e.g., relative risk, mean difference) and secondary measures
14. Synthesis methods: Describes whether meta-analysis was planned, the effect measure used, methods for combining results, handling of heterogeneity, subgroup analysis plans, sensitivity analysis plans, and any meta-regression
15. Reporting bias assessment: States how assessment of reporting bias was conducted (funnel plot, regression tests, etc.)
16. Certainty assessment: Describes the approach to assessing the certainty of evidence (e.g., GRADE)

**Results**
17. Study selection: Provides numbers of records identified, screened, excluded, and assessed for eligibility, with reasons for exclusion at full-text stage (flow diagram required)
18. Study characteristics: Presents characteristics of included studies (e.g., study design, population, sample size, duration) — use table or text
19. Risk of bias summary: Presents results of risk of bias assessment for all studies, presented as summary table or graph
20. Effect estimates: For each outcome, presents results for all included studies (effect estimate and 95% confidence interval, ideally in a table or forest plot)
21. Heterogeneity results: Presents statistical heterogeneity measures (I², τ²) and interpretation
22. Meta-analysis results: Presents summary effect estimate and confidence interval for the primary outcome (if meta-analysis performed)
23. Subgroup/sensitivity analyses: Presents results of any subgroup or sensitivity analyses conducted
24. Reporting bias results: Presents results of reporting bias assessment (e.g., funnel plot, test statistics)
25. Certainty of evidence: Presents certainty judgments (e.g., GRADE summary of findings table)

**Discussion & Closing**
26. Discussion: Interprets the results, discusses limitations (study limitations, outcome measurement, missing data, study design, directness, precision), compares findings to other reviews, and addresses practical applicability
27. Funding/conflicts: States sources of funding and any competing interests for all authors

### Phase 3 — Aggregate and Interpret

8. **Count the results.** Tally Present (✓), Partial (◐), and Absent (✗) items. Calculate the PRISMA Adherence Score: (Present + 0.5×Partial) / 27 × 100%.

9. **Identify clusters of missing items.** Group absences by section (e.g., "Methods section has 4 absences, mostly in synthesis methods"). This reveals where transparency broke down.

10. **Produce the summary.** List the absent and partial items with their locations (or "not found"). For each, note what information is missing and where it should appear.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All 27 items were evaluated (none skipped) | Y/N |
| Each absent/partial item has a specific location cited or marked "not found" | Y/N |
| PRISMA Adherence Score is calculated | Y/N |
| Clusters of missing items are identified by section | Y/N |
| Recommendations for revision point to concrete sections | Y/N |

## Red Flags

- Reviewer marked all items as Present without reading the full manuscript. PRISMA items require specific language and completeness; spot-checking is insufficient.
- The "risk of bias" section cites a tool name (e.g., "Cochrane ROB 2") but does not show the results (table, graph, or summary). Item 19 requires *presentation* of results, not just methodology.
- Protocol registration is claimed but the review ID and registry name are not stated. Item 5 requires explicit identification.
- Search strategy is listed as "databases searched" with no keywords or operators shown. Item 8 requires the full strategy from at least one database.
- Eligibility criteria are buried in prose without clear structure. Item 6 requires explicit PICO statements and date/design limits.
- Meta-analysis results are presented without heterogeneity measures (I², τ²). Item 21 and 22 must both be present if synthesis occurred.

## Output Format

```
## PRISMA Assessment

**Manuscript:** <title, authors, submission date>
**Review date:** <date of assessment>
**Reviewer:** <name>

### Item Checklist

| # | Item | Status | Location | Notes |
|---|---|---|---|---|
| 1 | Title identifies as systematic review/meta-analysis | ✓/◐/✗ | <section, para> | <detail> |
| 2 | Structured abstract with required elements | ✓/◐/✗ | Abstract | <missing elements, if any> |
| ... | ... | ... | ... | ... |
| 27 | Funding and conflicts disclosed | ✓/◐/✗ | <section> | <detail> |

### Summary by Section

**Title & Abstract:** 2/2 present
**Introduction:** 2/2 present
**Methods:** 10/12 present, 1 partial, 1 absent
**Results:** 7/9 present, 2 partial
**Discussion & Closing:** 1/2 present, 1 absent

### Missing & Partial Items (Priority Order)

1. **Item 8 (Search strategy):** Absent. Methods section names PubMed and Cochrane but does not provide keywords or search operators. Recommendation: Add full search string with Boolean operators for at least PubMed.

2. **Item 14 (Synthesis methods):** Partial. Meta-analysis approach described but heterogeneity handling not specified. Recommendation: State a priori plan for detecting and handling I² > 75%.

3. **Item 26 (Discussion limitations):** Partial. Discusses study heterogeneity but does not address missing data handling or measurement error. Recommendation: Add paragraph addressing outcome measurement and completeness of follow-up.

### Cluster Analysis

- **Methods transparency gap:** Items 5, 8, 9, 12 collectively weak — protocol details and selection process opaque. High priority for revision.
- **Results presentation adequate:** Items 17–25 largely present; flow diagram, tables, and heterogeneity clearly shown.

### PRISMA Adherence Score

- Present: 22
- Partial: 3
- Absent: 2
- **Adherence: (22 + 1.5) / 27 = 87%**

### Confidence

<high/medium/low> — <Justification: e.g., "High — all 27 items checked against manuscript text; gaps are specific and actionable. Reviewer familiar with PRISMA 2020 update." OR "Medium — search strategy section unavailable in submitted version; score provisional pending full Methods appendix.">
```
---
