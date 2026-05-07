---
name: phylogenetic-reconstruction
display_name: Phylogenetic Reconstruction
class: lens
underlying_class: native
domain: biology
source: Felsenstein (1981, Maximum Likelihood); Swofford et al. (1996, Phylogenetic Inference); Ronquist & Huelsenbeck (2003, Bayesian methods)
best_for:
  - Inferring evolutionary relationships from sequence or morphological data
  - Choosing between parsimony, maximum likelihood, and Bayesian tree-building methods
  - Evaluating tree quality and confidence in inferred relationships
one_liner: "Pick and validate the right tree-building method for the data when inferring evolutionary relationships."
---

# Phylogenetic Reconstruction

## Overview

Phylogenetic reconstruction infers evolutionary relationships (a tree) from observed character data—typically DNA/protein sequences or morphological traits. The analyst's core task is selecting an inference method (parsimony, maximum likelihood, or Bayesian) appropriate to the data and biological question, building the tree, and assessing confidence in the topology. Practitioners use this when evolutionary history is unknown and sequence or trait divergence must be converted into a branching diagram representing common ancestry.

## Analytical Procedure

### Phase 1 — Data Characterization

1. **Describe the dataset in quantitative terms.**
   - Number of taxa (species/sequences)
   - Number of characters (sequence length, morphological traits)
   - Character type: DNA nucleotides, amino acids, discrete morphological states, or mixed
   - Missing data prevalence (percentage of cells with ambiguous or absent values)
   - Sequence alignment quality: are homologous sites clearly aligned? Are there insertion/deletion regions (gaps)?

2. **Assess divergence depth.**
   - Do the sequences show saturation? (i.e., do distant pairs have multiple substitutions at the same site, obscuring the original state?)
   - Calculate pairwise sequence identity: high identity (>90%) suggests recent divergence; low identity (<50%) suggests deep divergence.
   - Note whether taxa span a narrow clade or represent major evolutionary distances.

3. **Check for model assumptions violation.**
   - Are substitution rates clock-like (approximately constant across lineages)? If not, Bayesian relaxed-clock models or outgroup rooting may be needed.
   - Is there strong compositional bias (e.g., GC-rich vs. AT-rich sequences)? This violates standard substitution models.
   - Is there evidence of selection (non-random change patterns) or primarily neutral drift?

### Phase 2 — Method Selection

4. **Select parsimony if:**
   - Dataset is small (<50 taxa, <1000 characters) AND divergence is shallow (recent common ancestors).
   - You need interpretability: each step in the tree reconstruction maps to specific mutations.
   - Computational speed is critical (parsimony is fastest).
   - Caveat: parsimony can recover incorrect trees under scenarios of asymmetric change rates or long branches.

5. **Select maximum likelihood (ML) if:**
   - Dataset is medium to large (50–500 taxa) AND you have a reasonable substitution model.
   - Divergence is moderate to deep (clock-like assumption can be relaxed).
   - You want to compare trees formally using likelihood ratio tests or AIC/BIC.
   - Computational resources allow iterative search (ML is slower than parsimony).

6. **Select Bayesian inference if:**
   - You want posterior probability distributions on tree topology (credibility intervals on splits).
   - You have prior knowledge about divergence times or substitution rates you wish to incorporate.
   - Dataset is large and you can tolerate long computation (MCMC sampling is slow but thorough).
   - You need to integrate over model uncertainty (different substitution models simultaneously).

### Phase 3 — Tree Construction

7. **Prepare the alignment or character matrix.**
   - If sequencing: ensure all sequences are aligned to the same reference or using a multiple alignment tool (MAFFT, MUSCLE, ClustalW).
   - Remove highly ambiguous columns (>30% gaps or Ns).
   - If morphological: verify character coding (binary, multistate, ordered vs. unordered).
   - Designate an outgroup (if known) to root the tree and orient evolutionary direction.

8. **Run the chosen inference method with appropriate parameters.**
   - **Parsimony:** Use exhaustive search for <10 taxa; branch-and-bound or heuristic search for larger datasets.
   - **ML:** Perform model selection (AIC/BIC) before searching tree space. Use hill-climbing search (e.g., nearest-neighbor interchange, subtree pruning-regrafting). Run multiple starting trees and compare likelihoods.
   - **Bayesian:** Choose a substitution model (GTR+Γ for DNA is standard). Set priors on model parameters and topology. Run two independent MCMC chains for ≥10 million generations. Check convergence (ESS >200 for key parameters, potential scale reduction factor <1.01).

9. **Assess tree convergence and sampling adequacy.**
   - For ML: confirm that multiple independent searches converge on the same tree topology and nearly identical log-likelihood values.
   - For Bayesian: plot trace plots (chain values over generations). Look for "hairy caterpillar" appearance (no drift, good mixing). Discard first 20% of generations as burn-in. Check that posterior probabilities stabilize after burn-in.

### Phase 4 — Confidence Assessment

10. **Calculate node support for the inferred tree.**
    - **Bootstrap** (parsimony, ML): resample characters with replacement 100–1000 times; run inference on each pseudo-dataset; count how often each split appears. Splits present in >70% of replicates are considered supported.
    - **Posterior probability** (Bayesian): proportion of post-burn-in MCMC samples in which a given split appears. Values >0.95 indicate strong support; 0.50–0.95 are uncertain.
    - **Likelihood ratio test** (ML): compare likelihood of two competing trees using a chi-squared test; p <0.05 means trees are significantly different.

11. **Evaluate tree robustness to method and data perturbation.**
    - Compare trees from two different inference methods. If major clades differ, the data may be ambiguous or model assumptions violated.
    - Repeat inference excluding putatively problematic taxa (e.g., sequences with many gaps, fast-evolving lineages). If the tree topology changes markedly, that taxon is influential but may be phylogenetically unstable.
    - If available, add independent data (different gene, morphological traits) and compare tree congruence.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Dataset is quantified: taxa count, character count, type, and missing-data percentage documented | Y/N |
| Divergence depth assessed and method selection justified against data properties | Y/N |
| Alignment (if DNA) quality verified; outgroup designated | Y/N |
| Tree inference ran to convergence (bootstrap reps completed, MCMC ESS sufficient, ML searches consistent) | Y/N |
| All nodes in final tree have support values (bootstrap %, posterior probability, or p-value) | Y/N |
| Robustness checked: tree topology stable across method/data variants OR instability documented | Y/N |

## Red Flags

- Tree topology differs radically between parsimony and ML/Bayesian. This suggests the data violates one method's assumptions (e.g., strong rate heterogeneity misleading parsimony) — investigate before reporting.
- Bootstrap values or posterior probabilities are uniformly high (>95% on nearly all nodes) across a large dataset. Either the data is extremely informative (rare) or support values are inflated due to model misspecification.
- The inferred tree contradicts known organismal relationships by orders of magnitude (e.g., placing a human within non-mammalian clades). Check for contamination, erroneous alignment, or outgroup choice.
- Burn-in period was not set or is very short (<10% of MCMC). Posterior estimates will be biased by starting conditions.
- Conflicting splits (e.g., taxon A groups with B, but A also groups with C in different trees) are present with equal support. Data are insufficient to resolve that region; report both topologies and their frequencies instead of choosing one.
- No convergence diagnostics (trace plots, ESS, PSRF) are reported for Bayesian inference. The chain may not have sampled the posterior adequately.

## Output Format

```
## Phylogenetic Reconstruction Report

### Data Summary
- Sequences: N taxa, M bp/characters
- Missing data: X%
- Sequence divergence: min–max pairwise identity
- Divergence depth category: [shallow | moderate | deep]

### Method Selection Rationale
- Chosen method: [Parsimony | ML | Bayesian]
- Justification: <why this method fits the data>
- Model (if ML/Bayesian): <substitution model, clock model>

### Inferred Tree
- Tree topology: [Newick format or text description of major clades]
- Log-likelihood (ML) or posterior probability (Bayesian): <value>
- Number of trees found with same score: [one | multiple — list or sample]

### Node Support
| Clade | Support Value | Method | Interpretation |
|---|---|---|---|
| (A, B) | XX% | Bootstrap | Supported / Uncertain / Unsupported |
| (C, (A, B)) | 0.98 | Posterior probability | Strongly supported |

### Robustness Assessment
- Bootstrap/MCMC convergence: [adequate | inadequate — specify diagnostic]
- Consistency across methods: [all methods agree | some disagreement in clades X, Y, Z]
- Stability when taxa removed: [stable | unstable — specify which taxa if removals change topology]

### Caveats and Limitations
<e.g., high saturation at third codon position; uneven taxon sampling; possible horizontal gene transfer in taxon X>

### Confidence
[High | Medium | Low] — <e.g., "High: tree topology consistent across methods and taxa, bootstrap support >80% for major clades. Medium: node X has support 60–75%, indicates minor topological uncertainty. Low: severe saturation or conflicting support across independent data; topology unreliable.">
```
