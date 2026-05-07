---
name: connectome-mapping
display_name: Connectome Mapping
class: lens
underlying_class: native
domain: neuroscience
source: Olaf Sporns (Indiana University); Human Connectome Project (Van Essen et al., 2013)
best_for:
  - Mapping whole-brain functional or structural connectivity patterns
  - Identifying network disruptions in neurological or psychiatric disease
  - Quantifying graph-theoretic properties of brain organization
one_liner: "Parcellate brain regions, measure pairwise connectivity, compute graph metrics, and detect disrupted network patterns."
---

# Connectome Mapping

## Overview
A connectome is the complete map of neural connections in a brain. Connectome Mapping operationalizes this by partitioning the brain into regions (parcellation), measuring connectivity strength between every pair of regions, computing graph-theoretic properties of the resulting network, and comparing against normative baselines to identify disruptions. Practitioners use it to quantify how disease, development, or intervention rewires the brain and to test hypotheses about which network properties explain behavioral or cognitive symptoms.

## Analytical Procedure

### Phase 1 — Parcellation and Data Acquisition

1. **Choose a parcellation scheme.** Decide whether to use:
   - **Anatomical** (e.g., AAL-90, Brainnetome) — regions defined by histology or structural landmarks
   - **Functional** (e.g., Yeo 7-network, Power 264) — regions defined by intrinsic functional connectivity
   - **Multimodal** (e.g., HCP-MMP1.0) — regions informed by multiple imaging modalities
   
   Document the number of regions, the source (citation and version), and why this choice matches your research question. If you are comparing to prior work, use their parcellation if possible.

2. **Acquire and preprocess imaging data.**
   - For **structural connectivity**: obtain diffusion tensor imaging (DTI) or diffusion spectrum imaging (DSI) scans. Run preprocessing: eddy current correction, motion correction, skull stripping, tensor fitting.
   - For **functional connectivity**: obtain resting-state fMRI scans (at least 5–10 minutes per subject, TR ≤ 3s). Run preprocessing: slice timing correction, motion correction, spatial normalization to standard space, registration to parcellation template. Regress out motion, white matter, and CSF signals.
   - Document preprocessing software (FSL, SPM, AFNI, fMRIPrep), parameters, and quality control steps.

3. **Extract time series or streamlines for each region.**
   - **Functional**: extract mean BOLD signal for each parcel across all time points, producing a time series of length T (number of volumes) × R (number of regions).
   - **Structural**: use deterministic or probabilistic fiber tracking to count streamlines connecting each pair of regions. Normalize by tract length or by total streamline count to control for distance bias.

### Phase 2 — Connectivity Matrix Computation

4. **Compute the connectivity matrix.** For each pair of regions (i, j):
   - **Functional**: Pearson correlation of the time series (or partial correlation to remove indirect influences). Optionally apply Fisher z-transform.
   - **Structural**: streamline count (raw or normalized), connection probability, or tract density.
   
   Result: an R × R symmetric matrix C where C[i,j] represents the strength of connection between regions i and j.

5. **Threshold or weight the matrix.**
   - **Weighted**: retain all connections, scaled by strength. This preserves nuanced information but is sensitive to noise.
   - **Thresholded**: retain only connections above a strength cutoff (e.g., top 10% or r > 0.3) and set others to zero. This increases signal-to-noise but discards information.
   
   If thresholding, justify the choice (e.g., expected sparsity, prior literature, statistical significance).

### Phase 3 — Graph Metric Computation

6. **Compute network-level metrics:**
   - **Density**: proportion of possible connections that are present (for thresholded networks).
   - **Average strength**: mean connection weight across all edges.
   - **Global efficiency**: inverse of average shortest path length; measures how efficiently information flows across the network.
   - **Clustering coefficient**: local cliquishness; average proportion of a region's neighbors that are also connected to each other.
   - **Modularity**: strength of division into communities (densely connected subnetworks); computed via community detection algorithm (e.g., Louvain).
   - **Small-world index**: ratio of actual clustering to path length, normalized against random networks; high values indicate efficient local and long-range connectivity.

7. **Compute node-level metrics for each region:**
   - **Degree** (functional) or **strength** (weighted): total number or weight of connections to that node.
   - **Betweenness centrality**: how many shortest paths pass through this node; high values indicate "hub" status.
   - **Eigenvector centrality**: influence based on connections to other influential nodes.
   - **Clustering coefficient (local)**: cliquishness of that region's neighborhood.
   - **Participation coefficient**: how evenly this region connects across different modules (0 = within-module only; 1 = balanced across modules).

8. **Compute edge-level metrics (optional):**
   - **Edge betweenness**: how many shortest paths use this edge.
   - **Edge weight distribution**: histogram of all connection strengths (assess bimodality, outliers).

### Phase 4 — Comparison and Statistical Testing

9. **Establish a normative baseline.** Compute the same metrics for a control group (age- and sex-matched healthy subjects) or use published norms. Record mean and standard deviation for each metric.

10. **Compare the patient/treatment group to baseline.**
    - **Group-level**: use t-tests, Mann-Whitney U tests, or permutation tests to compare group means. Apply multiple comparison correction (Bonferroni, FDR) if testing many metrics.
    - **Individual-level**: for single-subject or clinical interpretation, compute z-scores: (patient_value − control_mean) / control_SD. Values beyond ±2 SD are flagged as abnormal.
    - **Longitudinal**: if the same subject is scanned multiple times, test whether metrics change over time; use linear mixed models or ANCOVA controlling for scanner drift and head motion.

11. **Identify disrupted regions and edges.**
    - **Node disruption**: which regions show abnormal degree, centrality, or module participation?
    - **Edge disruption**: which connections are significantly stronger or weaker than expected?
    - **Network disruption**: are global metrics (efficiency, modularity, small-world index) shifted?
    
    Generate a brain map highlighting disrupted regions and overlay significant edges.

### Phase 5 — Validation and Interpretation

12. **Test robustness across parcellations.** Repeat the analysis with 2–3 alternative parcellation schemes. If findings persist across parcellations, they are more robust.

13. **Check motion and artifact confounds.** Regress out framewise displacement (head motion), in-scanner movement, and scanner-related artifacts. Recompute metrics to confirm findings are not driven by motion.

14. **Correlate network metrics with clinical or behavioral outcomes.** If available, compute correlations between disrupted network properties and symptom severity, cognitive scores, or treatment response. Report correlation strength, p-value, and effect size.

15. **Interpret in biological context.** Link disrupted regions and networks to known neuroanatomy and function:
    - Which resting-state networks (default mode, salience, executive) are affected?
    - Which neurotransmitter systems or brain regions are implicated?
    - Are the disruptions consistent with the disease mechanism or clinical presentation?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Parcellation scheme is named and justified | Y/N |
| Preprocessing pipeline is fully documented with software and parameters | Y/N |
| Connectivity matrix construction method (Pearson, streamline count, etc.) is explicit | Y/N |
| Thresholding (if used) is justified; weighted alternative is considered | Y/N |
| At least 4 network-level and 4 node-level metrics are computed | Y/N |
| Control group or normative baseline is defined | Y/N |
| Multiple comparison correction is applied to group statistics | Y/N |
| Robustness check (alternative parcellation or artifact control) is reported | Y/N |
| Disrupted regions/edges are linked back to neuroanatomy and clinical context | Y/N |

## Red Flags

- Parcellation is unspecified or arbitrary. ("We used the standard atlas.") Without reproducible parcellation, the analysis cannot be replicated.
- Preprocessing is under-documented or uses default parameters without checking quality. Motion, distortion, and normalization errors propagate into the connectome.
- Connectivity matrix is thresholded without justification or sensitivity analysis. Findings are often sensitive to the threshold; report results across multiple thresholds.
- No control group or normative baseline. Without comparison, you cannot distinguish abnormal from normal variation.
- Multiple metrics are computed but not corrected for multiple comparisons. Many false positives are likely.
- Disrupted regions are reported with no reference to anatomy or function. ("Node 47 is disrupted.") Raw indices are meaningless without interpretation.
- Findings are not validated across parcellations or do not persist after motion correction. Suggests artifacts or overfitting rather than true disruption.
- Correlation with clinical outcomes is missing. Even if the connectome is disrupted, if it doesn't relate to behavior or symptoms, the clinical relevance is unclear.

## Output Format

```
## Connectome Mapping Report

**Subject(s):** <ID, group, or population>
**Imaging modality:** <resting fMRI | DTI | DSI | multimodal>
**Parcellation:** <name, number of regions, citation>
**Preprocessing:** <software, version, QC checks>

### Connectivity Matrix
- **Construction method:** <Pearson correlation | partial correlation | streamline count | etc.>
- **Thresholding:** <none (weighted) | top 10% | r > 0.3 | other>
- **Matrix sparsity:** _%
- **Average connection strength:** <value>

### Network-Level Metrics (vs. control baseline)

| Metric | Value | Control mean ± SD | Z-score | Abnormal? |
|---|---|---|---|---|
| Global efficiency | <...> | <...> | <...> | Y/N |
| Clustering coefficient | <...> | <...> | <...> | Y/N |
| Modularity | <...> | <...> | <...> | Y/N |
| Small-world index | <...> | <...> | <...> | Y/N |

### Node-Level Disruptions
Top 5 most disrupted regions (ranked by z-score magnitude):

| Region | Metric | Value | Control mean | Z-score | Interpretation |
|---|---|---|---|---|---|
| <name/index> | degree/strength | <...> | <...> | <...> | <hub loss / hub gain / ...> |

### Edge-Level Disruptions
Top 5 strongest or most disrupted connections:

| Region A | Region B | Strength | Control mean | Status | Network |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | stronger / weaker | <default mode / salience / ...> |

### Validation Across Parcellations
| Parcellation | Global efficiency | Modularity | Top disrupted regions overlap | Robust? |
|---|---|---|---|---|
| <scheme 1> | <...> | <...> | <yes/no> | <...> |
| <scheme 2> | <...> | <...> | <yes/no> | <...> |

### Motion and Artifact Control
- **Mean framewise displacement (FD):** <value> mm
- **Volumes censored (>0.5mm FD):** _%
- **Metrics after FD regression:** <persist / attenuate / disappear>

### Clinical Correlation
| Network metric | Outcome | Correlation | p-value | 95% CI | Effect size |
|---|---|---|---|---|---|
| <efficiency / modularity / etc.> | <symptom / score> | <r or ρ> | <...> | <...> | <...> |

### Interpretation
<2-3 sentences summarizing which networks or regions are disrupted, how this relates to known neuroanatomy and the disease/condition, and what the disruption implies functionally.>

### Confidence
<high | medium | low> — <justification, e.g., "high: findings robust across 3 parcellations, FD-corrected, significant clinical correlation. low: small N, motion artifacts remain, threshold-sensitive.">
```
---
