---
name: shannon-simpson-diversity
display_name: Shannon / Simpson Diversity
class: lens
underlying_class: native
domain: ecology
source: Claude Shannon (Information Theory, 1948); Edward Simpson (Concentration of Measure, 1949); popularized in ecology by Simpson (1949) and Shannon (1948)
best_for:
  - Quantifying species richness and evenness in ecological communities
  - Comparing biodiversity across sites or time periods
  - Detecting dominance patterns that affect ecosystem function
one_liner: "Quantify species diversity to assess ecosystem health and stability."
---

# Shannon / Simpson Diversity

## Overview
Shannon and Simpson diversity indices measure both how many species are present (richness) and how evenly their abundances are distributed (evenness) in a community. Shannon's index weights rare species more heavily; Simpson's index weights abundant species more heavily. Practitioners use these metrics to compare ecological communities, track changes over time, and detect whether a system is dominated by one or two species (a red flag for ecosystem stress or recent disturbance).

## Analytical Procedure

### Phase 1 — Data Preparation

1. **Obtain the species abundance data.** This is a count or biomass table where each row is a site/sample and each column is a species, with cell values as abundance (number of individuals, biomass, or relative abundance). Verify that:
   - All entries are non-negative integers or proportions.
   - The data includes all species observed in the sample, not just rare or dominant ones.
   - Sampling effort is consistent across samples if comparing multiple sites (note any differences for later interpretation).

2. **Choose a rarefaction baseline if comparing samples with unequal sizes.** If two samples differ in total count (e.g., 100 vs. 500 individuals), diversity indices will be artificially inflated for the larger sample. Decide whether to:
   - Rarefy to the smallest sample size (removes bias but loses data).
   - Use richness-corrected measures.
   - Report both raw and rarefied indices and document the choice.

### Phase 2 — Shannon Index Calculation

3. **Calculate Shannon index (H) for each sample:**
   - For each species *i*, compute the proportion of the community it comprises: p_i = (count of species i) / (total count in sample).
   - For each species, compute: p_i × ln(p_i). (Use natural log; some sources use log₁₀ — document which.)
   - Sum across all species and negate: H = −Σ(p_i × ln(p_i)).
   - **Interpretation:** H ranges roughly from 0 (one species dominates) to 4–5 (highly diverse, even community). An increase of 0.5 is meaningful; of 0.1 is noise-level.

4. **Convert Shannon to "Shannon evenness" (J) to isolate evenness from richness:**
   - J = H / ln(S), where S is the number of species observed.
   - J ranges from 0 to 1. J near 0.5 suggests one or two dominants; J > 0.8 suggests near-equal abundances.

### Phase 3 — Simpson Index Calculation

5. **Calculate Simpson index (λ or D) for each sample:**
   - For each species *i*, compute: λ = Σ(p_i²).
   - λ ranges from (1/S) to 1. Low λ (near 1/S) indicates high diversity; high λ (near 1) indicates dominance by few species.
   - **Interpretation:** Some sources report 1 − λ (Simpson's diversity) or 1/λ (reciprocal Simpson), which increase with diversity. Document which version you use.

6. **Compare Shannon and Simpson indices side by side.** Shannon "sees" rare species more clearly; Simpson focuses on the dominant species. If the two indices rank sites differently, it signals that dominance structure varies (e.g., Site A has many rare species, Site B has two or three dominants).

### Phase 4 — Cross-Site or Temporal Comparison

7. **If comparing multiple samples (sites or time points):**
   - Create a summary table with Shannon, Simpson, and richness (S) for each sample.
   - Identify the highest and lowest values for each metric. High Shannon with low richness suggests one or two abundant species and many rare ones (common in early succession or disturbed sites). High Shannon with high richness and high evenness suggests a mature, stable community.

8. **Check for statistical significance.** Calculate standard error or bootstrapped confidence intervals for each index if sample sizes are small (< 50 individuals per species, on average). Indices from samples with <20 total individuals are unreliable.

### Phase 5 — Interpretation and Context

9. **Map findings to ecological hypotheses:**
   - **High diversity + high evenness** → stable, mature, or climax community; low external stress.
   - **High diversity + low evenness** → early succession, high resource heterogeneity, or niche partitioning by rare specialists.
   - **Low diversity + dominance (λ near 1)** → recent disturbance, harsh environment, or early primary succession.
   - **Decreasing diversity over time** → habitat degradation, invasive species, or overharvesting.
   - **Increasing diversity over time** → recovery, restoration success, or loss of a dominant.

10. **Note confounding factors:** Sampling method, season, spatial scale, and observer skill all affect observed diversity. Document these so readers can contextualize the indices.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Abundance data is complete (all species, all samples) and verified for quality | Y/N |
| Rarefaction baseline (if needed) is stated explicitly | Y/N |
| Shannon index calculated correctly for at least one sample (spot-check the math) | Y/N |
| Shannon evenness (J) is reported alongside Shannon index | Y/N |
| Simpson index calculated and documented (clarify if λ, 1−λ, or 1/λ is used) | Y/N |
| Indices from samples with <20 individuals are flagged as unreliable or excluded | Y/N |
| Summary table includes Shannon, Simpson, richness, and evenness for all samples | Y/N |
| Findings mapped to at least two ecological hypotheses (succession, stress, stability) | Y/N |
| Confounding factors (sampling method, season, spatial scale) are documented | Y/N |

## Red Flags

- All samples have identical Shannon values across a gradient of richness. The calculation is likely wrong; re-check the formula and logarithm base.
- Richness (S) is very high (>100 species) but Shannon and Simpson are low (H < 1.5, λ > 0.5). This often means most species are singletons or doubletons (sampling artifact); consider whether the true community is inflated by rare vagrants or whether sampling effort was insufficient.
- Shannon and Simpson indices rank sites in opposite order (highest Shannon = lowest Simpson and vice versa). This is plausible if sites differ in dominance structure, but verify it reflects real biology, not a calculation error.
- Evenness (J) is very high (>0.95) in a natural community. While possible, this is rare; check whether all species are being counted or whether the data is artificially smoothed.
- Temporal trend shows oscillating diversity with no net direction over years. If the oscillation is seasonal, this is expected; if not, it may signal unstable sampling or real but unexplained environmental noise.
- No comparison group or baseline. An isolated Shannon value is uninterpretable — always report it relative to a reference (other sites, historical data, or published norms for the ecosystem type).

## Output Format

```
## Shannon / Simpson Diversity Assessment

### Input Data Summary
- Number of samples: _
- Total species observed: _
- Sample sizes (individuals): min _, max _, mean _
- Rarefaction applied: Yes/No (if Yes, to _)

### Results Table
| Sample | Richness (S) | Shannon (H) | Evenness (J) | Simpson (λ) | Interpretation |
|---|---|---|---|---|---|
| Site A | _ | _ | _ | _ | <dominance pattern or community type> |
| Site B | _ | _ | _ | _ | ... |

### Shannon Index Details
- Logarithm base used: natural log / log₁₀
- H range observed: _ to _
- Sample with highest diversity: _; lowest: _

### Simpson Index Details
- Variant reported: λ / (1 − λ) / (1/λ)
- λ range observed: _ to _
- Sample with most dominance: _; most evenness: _

### Comparative Analysis
**Shannon vs. Simpson rank order:**
- Sites ranked by Shannon (high to low): _
- Sites ranked by Simpson (low λ to high λ): _
- Agreement: high / partial / low. [If partial/low, explain difference.]

### Ecological Interpretation
1. <Finding 1: community type, stress signal, or successional stage>
2. <Finding 2: comparison between sites or time periods>
3. <Finding 3: dominant species effect or richness-evenness trade-off>

### Caveats & Confounds
- Sampling method: <method>
- Temporal context: <season, year, or "temporal series from _ to _">
- Spatial scale: <plot size, area, or transect length>
- Known biases: <e.g., "rare species undersampled," "seasonal variation," "observer expertise varies">

### Confidence
<high | medium | low> — <justification, e.g., "high: large sample sizes, complete species list, replicate sites; medium: small samples, possible rare-species undersampling; low: <20 individuals, indices unreliable">
```
