---
name: bibliometric-analysis
display_name: Bibliometric Analysis
class: lens
underlying_class: native
domain: meta-science
source: Garfield, E. (1955, Citation Indexes); Hirsch, H. (2005, h-index); modern practice across meta-research and research evaluation
best_for:
  - Measuring research impact and influence through citation patterns
  - Identifying seminal works and research clusters in a field
  - Comparing researcher productivity and visibility across disciplines
one_liner: "Quantify research impact and field structure via citation networks and the h-index."
---

# Bibliometric Analysis

## Overview
Bibliometric analysis quantifies research impact and structure by measuring citation patterns, author productivity, and knowledge diffusion across a field or researcher cohort. Instead of reading each paper, you extract numerical signals from citation metadata (who cites whom, how often, when) to infer influence, community boundaries, and research momentum. Practitioners use it when they need to survey a large literature quickly, validate intuitions about which work shaped a field, or benchmark a researcher's standing relative to peers.

## Analytical Procedure

### Phase 1 — Data Assembly

1. **Define the scope.** Specify:
   - The field, subfield, or research question (e.g., "machine learning for medical diagnosis 2015–2025")
   - The publication types to include (journals, conferences, preprints, books)
   - The date range
   - Any inclusion/exclusion rules (e.g., exclude self-citations, exclude papers with fewer than 2 citations)
   
   Document these rules; they affect all downstream results.

2. **Select a bibliographic source.** Choose one:
   - **Web of Science** — comprehensive, strict indexing, proprietary
   - **Scopus** — broad coverage, consistent metadata
   - **Google Scholar** — largest coverage, noisier metadata
   - **PubMed** (for biomedical) — specialized, clean
   - **arXiv / discipline-specific preprint servers** — if your field publishes preprints
   
   Note the source; results are not directly comparable across databases.

3. **Execute the search query.** Use field-specific syntax (title, abstract, keywords) to retrieve papers matching your scope. Export the result set as a structured file (CSV, RIS, or the database's native format) including: author names, publication year, citation count, referenced papers, and subject categories.

4. **Validate the result set.** Spot-check 10–20 random papers. Confirm they match your scope. If >10% are off-topic, refine the query and re-run. Document how many papers were retrieved and how many passed validation.

### Phase 2 — Calculate Core Metrics

5. **Compute the h-index for the corpus or each author.** 
   - Sort papers by citation count (descending).
   - Find the largest number *h* such that at least *h* papers have ≥*h* citations.
   - Example: If 15 papers have ≥15 citations, 12 papers have ≥16 citations, then h = 15.
   - Interpret: An h-index of 15 means the researcher/corpus has 15 highly-cited works; it ignores outliers and low-cited papers.

6. **Calculate aggregate metrics per author (if author-level analysis):**
   - **Total citations:** Sum of all citations to the author's papers.
   - **Average citations per paper:** Total / number of papers.
   - **Publication rate:** Number of papers / years active.
   - **Citation trajectory:** Citations per year over time (reveals momentum or decline).

7. **Calculate aggregate metrics per year or time window (if field-level analysis):**
   - **Papers published per year:** Track growth or contraction of the field.
   - **Average citations per paper per year:** Measures how fast papers accumulate citations.
   - **Median citation count:** Resistant to outliers; complements the mean.

8. **Identify top cited papers and authors.** List the top 10 papers by citation count and the top 10 authors by h-index or total citations. These are the field's anchors.

### Phase 3 — Citation Network Analysis

9. **Build the citation graph.** For each paper in your corpus, record:
   - Which other papers in the corpus it cites (in-edges)
   - Which other papers in the corpus cite it (out-edges)
   
   Represent as a directed acyclic graph (DAG): an edge from A → B means "A cites B."

10. **Detect clusters.** Use a community detection algorithm (e.g., Louvain, modularity optimization) or hierarchical clustering on the citation graph to partition papers into research clusters or subtopics. Document the algorithm and any parameters (e.g., resolution, minimum cluster size). Interpret clusters by reading titles and abstracts of papers in each.

11. **Trace influence flow.** Identify:
    - **Seminal papers:** Papers cited by many others but cite few (high out-degree, low in-degree). These are foundational.
    - **Synthesis papers:** Papers that cite many others and are cited by many (high in- and out-degree). These integrate across clusters.
    - **Emerging topics:** Papers published recently with high citation velocity (citations accumulated quickly after publication).

12. **Assess temporal dynamics.** Plot cumulative citations over time for the top 5–10 papers. Papers that plateau early peaked in influence; papers still rising are sustained or growing in impact.

### Phase 4 — Validation and Interpretation

13. **Sanity-check the results.** Ask:
    - Do the top papers match your expert knowledge of the field? If the top-cited paper is unknown to domain experts, the corpus may be misaligned with the actual research community.
    - Are clusters interpretable? If a cluster is a grab-bag of unrelated topics, the algorithm may have failed or the corpus is too heterogeneous.
    - Does the citation trajectory match the field's history? (E.g., a new subfield should show rising publication rates in the past 5 years.)

14. **Document limitations.** Note:
    - Self-citations (inflated by authors citing their own work)
    - Missing citations (papers indexed late or with indexing errors)
    - Gaming or anomalies (e.g., one paper cited 10,000 times, others <5; suggests potential mass citations or database errors)
    - Disciplinary biases (some fields cite more than others; citation counts are not normalized across domains)

## Evaluation Criteria

| Check | Pass |
|---|---|
| Scope (field, date range, publication types) is explicit | Y/N |
| Bibliographic source is named and justified | Y/N |
| Search query is reproducible (exact keywords or boolean logic documented) | Y/N |
| Result set size and validation notes are present | Y/N |
| h-index is calculated correctly (sortable list of papers × citation counts provided) | Y/N |
| Top papers and authors are listed and interpreted | Y/N |
| Citation network has been visualized or described (not just tabulated) | Y/N |
| At least one cluster or seminal/synthesis paper has been identified | Y/N |
| Temporal dynamics (publication rate, citation velocity) are addressed | Y/N |
| Limitations (self-citations, missing papers, gaming) are acknowledged | Y/N |

## Red Flags

- The h-index is presented without showing the underlying citation distribution. Without the full ranked list, the h-index is uninterpretable.
- Top papers are unrecognized by domain experts or contradict established history of the field. Suspect corpus misalignment or database error.
- All papers have similar citation counts (flat distribution). Either the field is very new, the corpus is too narrow, or the indexing is incomplete.
- No mention of self-citations. Authors and research groups often cite each other strategically; uncontrolled self-citation inflates apparent influence.
- Clusters do not make semantic sense when you read the paper titles. The algorithm detected statistical patterns but not meaningful research subcommunities.
- Citation velocity is not examined. A paper with 1000 citations accumulated over 20 years is not the same as 1000 citations in 2 years; momentum matters.
- Temporal dynamics are ignored. A corpus frozen at one point in time misses the field's trajectory and emerging areas.

## Output Format

```
## Bibliometric Analysis Report

**Scope:**
- Field: <field or research question>
- Date range: <YYYY–YYYY>
- Publication types: <journals, conferences, preprints, etc.>
- Inclusion/exclusion rules: <rules applied>

**Data Source:**
- Database: <Web of Science | Scopus | Google Scholar | other>
- Search query: <exact query or keyword string>
- Result set size: <N papers>
- Validation: <N papers spot-checked; X% match scope>

### Core Metrics (Corpus or Author Level)

**h-index:** <N>
- Definition: <N> papers have ≥<N> citations.

**Total citations:** <N>
**Average citations per paper:** <N>
**Publication rate:** <N> papers/year
**Citation trajectory:** <description of trend over time>

### Top Papers
| Rank | Title | Author(s) | Year | Citations |
|---|---|---|---|---|
| 1 | <...> | <...> | <...> | <...> |
| ... |

### Top Authors (if author-level analysis)
| Rank | Author | h-index | Total citations | Papers |
|---|---|---|---|---|
| 1 | <...> | <...> | <...> | <...> |
| ... |

### Citation Network & Clusters

**Network statistics:**
- Total papers: <N>
- Total citations (edges): <N>
- Average citations per paper: <N>

**Detected clusters (communities):** <N clusters>
| Cluster | Size (papers) | Interpretable topic | Example papers |
|---|---|---|---|
| 1 | <N> | <topic> | <paper 1>, <paper 2>, ... |
| ... |

**Seminal papers** (high out-degree, low in-degree):
- <Paper title (Year)>: <brief interpretation>

**Synthesis papers** (high in- and out-degree):
- <Paper title (Year)>: <brief interpretation>

**Emerging topics** (recent, high citation velocity):
- <Paper title (Year)>: <N citations in past Y years>

### Temporal Dynamics

**Publication rate:** <trend: rising | stable | declining | bifurcated, with description>
**Citation velocity:** <top papers' citation accumulation rates over time>
**Field momentum:** <Interpretation of whether the field is growing, maturing, or contracting>

### Limitations & Caveats
- Self-citations: <% of total, or "not separated">
- Indexing lag: <description of any recent papers with low citation counts>
- Database bias: <any known gaps in this database for your field>
- Gaming risk: <any anomalies detected>

### Interpretation Summary
<2–4 sentences synthesizing what the metrics reveal about the field or author's influence, the structure of the research landscape, and key insights that wouldn't be obvious from reading papers individually.>

### Confidence
<high | medium | low> — <justification based on data completeness, alignment with expert knowledge, temporal coverage, and limitations noted above>
```
---
