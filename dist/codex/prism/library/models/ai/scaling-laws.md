---
name: scaling-laws
display_name: Scaling Laws (Chinchilla, Kaplan)
class: model
underlying_class: native
domain: ai
source: Jared Kaplan et al., "Scaling Laws for Neural Language Models," arXiv:2001.08361, 2020; Hoffmann et al. (DeepMind), "Training Compute-Optimal Large Language Models," arXiv:2203.15556, 2022 (Chinchilla)
best_for:
  - Predicting loss and capability scaling as a function of model size, dataset size, and compute budget
  - Allocating training compute optimally between model parameters and training tokens
  - Planning infrastructure and budgets for large-scale AI training
one_liner: "Predict performance scalability via power-law relationships between model size, data, and compute."
---

# Scaling Laws (Chinchilla, Kaplan)

## Overview

Scaling Laws model the relationship between neural language model performance (measured as loss or downstream task accuracy) and the three primary resources that determine it: model size (parameters), dataset size (tokens), and total compute budget (FLOPs). The central claim is that loss follows a power-law relationship with each of these variables, and that these relationships are smooth and predictable across orders of magnitude. The model is empirical and predictive: it explains historical scaling trends and predicts the performance of larger, future models given specified resource allocations. Kaplan et al. (2020) established the basic power-law form; Hoffmann et al. (2022, Chinchilla) further refined the allocation problem, showing that most prior models were severely undertrained relative to their size, and that optimal compute allocation is roughly equal parts parameters and tokens.

## Core Variables and Relationships

The core scaling law relates loss to three variables:

1. **Model size (N)** — the number of parameters.
   - Loss decreases as N increases, following: **L(N) ≈ a · N^(−α)**
   - Empirical estimate: **α ≈ 0.07** (loss reduction per doubling of parameters ≈ 5%)
   - This relationship holds across scales from ~1M to ~175B+ parameters (GPT-3).

2. **Dataset size (D)** — the number of unique tokens in the training set.
   - Loss decreases as D increases, following: **L(D) ≈ b · D^(−β)**
   - Empirical estimate: **β ≈ 0.08** (loss reduction per doubling of tokens ≈ 5–6%)
   - This relationship holds over a wide range; data hunger scales roughly as N.

3. **Compute budget (C)** — the total number of floating-point operations (FLOPs) available.
   - Loss decreases with total compute: **L(C) ≈ c · C^(−γ)**
   - Empirical estimate: **γ ≈ 0.05–0.07** (loss reduction per doubling of compute ≈ 3–5%)

**Key relationship (Chinchilla):** The optimal allocation of compute C between parameters N and training tokens D is approximately **D ≈ 20N** — for a given compute budget, optimal models are undertrained (far more tokens than typical practice). In practice:
- Kaplan et al. (2020) under-estimated data requirements by ~4–10×.
- Chinchilla (2022) showed that a given compute budget should be split roughly equally between model scaling and data scaling (in FLOPs terms), with D ≈ 20N for optimal loss.

**Combined law:** 
    L(N, D) ≈ E · N^(−α) · D^(−β) + (residual)

where E is an empirical constant. The loss can also be expressed as a function of compute budget C alone, given an allocation strategy.

## Key Predictions

- **A model trained on compute-optimal allocation will outperform an under-trained larger model or an over-trained smaller model at the same total compute.** This was the central finding of Chinchilla — many models in 2020–2021 were 2–4× larger than optimal and undertrained by the same multiple.

- **Scaling laws remain smooth and predictable at least through 10^20–10^21 FLOPs.** There is no evidence of a "wall" or phase transition in the loss curves, suggesting that loss reductions continue at power-law rates at least to model scales beyond current practice.

- **The scaling exponents (α, β) are remarkably consistent across model architectures, datasets, and tasks.** A model trained on Wikipedia will follow nearly the same scaling curve as one trained on code or dialogue, within a constant offset. This suggests the laws capture something fundamental.

- **Loss improvements in pre-training transfer strongly to downstream task performance.** A 1-point reduction in pre-training loss translates to measurable gains on GLUE, SuperGLUE, and other benchmarks, though the transfer function is nonlinear and task-dependent.

- **Instruction-tuning, prompting, and in-context learning do not obviate scaling laws.** Even state-of-the-art few-shot or instruction-tuned models still improve steeply with scale, and their loss curves follow power laws.

- **For a fixed compute budget, the curve of "test loss vs. model size" shows a U-shape when data is held constant,** because if you fix D but increase N, you must reduce tokens-per-parameter and convergence worsens. The minimum of that U is where D ≈ 20N.

## Application Procedure

Instantiate the model to predict loss (or downstream accuracy) for a target model or to optimize compute allocation across model size and data size.

1. **Define the target model and scope.** What is the model architecture (Transformer, etc.)? What is the downstream task or task suite? What is the compute budget (in FLOPs, or equivalently, in GPU-hours with known hardware efficiency)? What is the time/resource constraint?

2. **Identify the constraint: is it model size, data size, or compute budget?**
   - If compute is fixed, you want to find optimal (N, D) such that D ≈ 20N and N · D · (constant) ≤ C.
   - If data is fixed (e.g., all available English text), you want to find the maximum N that minimizes L given C and D.
   - If model size is fixed, you solve for the minimum D to achieve a target loss.

3. **Gather or estimate empirical constants for your setting.**
   - Use published scaling curves (Kaplan et al., Hoffmann et al., or Chinchilla paper) to read off α, β, γ for your architecture / data mix.
   - Default: α ≈ 0.07, β ≈ 0.08, γ ≈ 0.06.
   - If applying to a domain outside LLMs (vision, speech, RL), the exponents may differ — use domain-specific estimates if available.

4. **Compute the predicted loss for candidate (N, D) pairs** using L(N, D) ≈ E · N^(−α) · D^(−β).
   - Use the empirical constant E from the literature or a reference model (e.g., GPT-3).
   - For each candidate, compute total FLOPs: C ≈ 6 · N · D (rough approximation; exact formula depends on architecture details).

5. **Select the (N, D) pair that minimizes loss for the available compute, or maximizes compute efficiency for a target loss.**
   - For fixed C, solve the optimization problem: minimize L(N, D) subject to 6ND ≤ C.
   - Chinchilla shows the solution is approximately N = (C / (6 · 20))^(1/2), D = 20N.

6. **Convert predicted loss to downstream task performance** (if needed).
   - Use a task-specific transfer function; these are nonlinear and task-dependent.
   - As a rough proxy: a 0.5-point reduction in pre-training loss often corresponds to a 2–5% improvement in GLUE average, but this varies widely.

7. **Check boundary conditions** (below). Flag conditions under which the law may not apply.

## Boundary Conditions

Scaling Laws are empirical and have known failure modes:

- **Below ~10B parameters or in extreme data-poor regimes.** The power law is well-established for "large" models but may not hold for small models (< 1B) or for models trained on tiny datasets. Empirical support is sparse below 10M parameters.

- **Domain shift from training data to deployment.** Scaling laws are measured on held-out test sets from the same distribution as training data. Performance on out-of-distribution tasks (e.g., a model trained on English text applied to code-generation) will not follow the same curve. The shift depends on semantic distance.

- **When inference or latency constraints are binding.** Scaling laws predict loss, not inference time. A larger model with lower loss may be too slow for deployment, and the optimal model under latency constraints is smaller and trained more. Quantization, distillation, and speculative decoding change the trade-off.

- **In few-shot or zero-shot settings at extreme scale.** While scaling laws hold for pre-training loss and general downstream performance, the behavior of models at 100B+ parameters in few-shot, in-context, and instruction-tuned settings is less well-characterized. Emergent capabilities and in-context learning may follow different scaling exponents.

- **When training data is non-independent or highly biased.** Scaling laws assume relatively diverse, independent training examples. If data has significant duplication, hard filtering, or systematic bias, the effective dataset size is smaller than the token count, and the law will overestimate performance.

- **At the compute budget boundary.** Scaling laws apply in the regime where compute is the binding constraint and both N and D can be scaled. If hardware cost per FLOP, not total FLOPs, is the actual constraint, or if data is exhausted, the predictions change qualitatively.

## Output Format

```
## Scaling Law Prediction: <model name / use case>

**Target model:** <architecture, estimated parameters>
**Constraint:** <fixed compute C / fixed data D / fixed model size N>
**Compute budget or data size:** <FLOPs or tokens available>

### Scaling exponents and constants
| Variable | Exponent | Coefficient | Source |
|---|---|---|---|
| Model size (N) | α ≈ 0.07 | E ≈ ... | Kaplan et al. / Chinchilla / domain-specific |
| Data size (D) | β ≈ 0.08 | (from α) | ... |
| Compute (C) | γ ≈ 0.06 | (derived) | ... |

### Optimal allocation (if compute is fixed)
- Optimal model size N: <parameter count>
- Optimal data size D: <token count>
- Ratio D/N: <check against ≈ 20>
- Total compute C: <FLOPs>

### Predicted loss and performance
- Pre-training loss: <value>
- Downstream task improvement (estimated): <e.g., GLUE, SuperGLUE, or domain-specific benchmark>
- Uncertainty / sensitivity: <which exponent or constant drives largest uncertainty>

### Boundary-condition check
- Domain shift risk: <applies / not applicable>
- Data independence: <potential duplication or bias>
- Inference constraints: <latency / memory constraints on model size>
- Regime: <are N, D, C in the well-characterized range>

### Confidence: high | medium | low
<reasoning: exponent certainty + empirical data quality + how closely the target setting matches published studies + boundary-condition fit>
```
