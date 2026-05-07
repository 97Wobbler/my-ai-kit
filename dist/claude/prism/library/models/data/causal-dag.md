---
name: causal-dag
display_name: Causal DAG (Pearl)
class: model
underlying_class: native
domain: data
source: Judea Pearl, "Causality: Models, Reasoning, and Inference," 2nd ed., 2009; foundational work on causal graphical models
best_for:
  - Identifying confounders and causal paths in observational data
  - Distinguishing association from causation using graphical criteria
  - Determining what variables must be controlled for to estimate causal effects
one_liner: "Causal identification and confounder diagnosis via graph structure."
---

# Causal DAG (Pearl)

## Overview

The Causal DAG (Directed Acyclic Graph) model claims that causal relationships in a system can be encoded as a directed graph where nodes represent variables and edges represent direct causal influences, and that this graph structure alone determines which statistical associations are causal and which are spurious. The model is diagnostic: given a proposed DAG, it reveals whether observed associations reflect causal effects, confounding, selection bias, or collider bias. Crucially, it answers the question "which variables must I control for to estimate a causal effect?" — a question correlation alone cannot answer. The model is both descriptive (encodes causal assumptions) and prescriptive (points to identification strategies). It applies whenever you have observational data and need to distinguish causation from association.

## Core Variables and Relationships

A causal DAG encodes three primitive concepts:

1. **Nodes** — each variable in the system (treatment, outcome, confounders, mediators, colliders).

2. **Edges** — a directed edge X → Y means X is a direct cause of Y (all other paths from X to Y are blocked by conditioning).

3. **Paths** — sequences of edges connecting two variables. A path is **open** (transmits association) or **closed** (blocks association) depending on the conditioning set and the structure of the path.

Key relationships:

- **Confounding path:** X ← C → Y. The common cause C opens an association between X and Y that is not causal. Conditioning on C closes this path and reveals the causal effect of X on Y.

- **Causal path:** X → Y (possibly through mediators). All edges point in the same direction toward Y.

- **Collider:** X → C ← Y. The two variables X and Y are *unconditionally* independent (no open path). But conditioning on the collider C *opens* a spurious association between X and Y — this is called collider bias or Berkson's paradox.

- **Mediator:** X → M → Y. The path is causal; M transmits the effect of X on Y. If you condition on M, you block the indirect (mediated) effect.

- **d-separation (d = directional-separation):** A pair of variables is d-separated in a DAG given a conditioning set Z if all paths between them are blocked. D-separated variables are statistically independent given Z. This criterion automatically generates the control-variable strategy.

The **identification criterion (Pearl's back-door criterion):** The causal effect of X on Y is identifiable from observational data if there exists a conditioning set Z such that:
1. No element of Z is a descendant of X.
2. Z blocks all "back-door" paths from X to Y (paths that enter X from the left via common causes).

If such a Z exists, conditioning on Z yields an unbiased causal estimate.

## Key Predictions

- **Conditioning on a confounder reduces bias.** If C confounds X → Y, then the association X ∼ Y is inflated by C's correlation with both. Conditioning on C reveals the true causal effect of X on Y.

- **Conditioning on a collider introduces spurious association.** If X → C ← Y (and X and Y have no other path), then unconditionally X ⊥ Y. But conditioning on C opens a path and induces correlation between X and Y. This is collider bias: including variables that have no causal role but receive influence from multiple sources of error.

- **Not all confounders must be conditioned on.** If a confounder C is not on any back-door path from X to Y (e.g., C affects X but not Y), conditioning on C does not reduce bias and may introduce variance.

- **Conditioning on a mediator masks the causal effect.** If X → M → Y and you condition on M, you block the causal path from X to Y, making X appear uncaused even though it causally affects Y through M.

- **Causal effects are not identifiable from the DAG alone if back-door paths remain open.** If all confounders are unmeasured, no conditioning set can close the back-door; the causal effect is unidentifiable even if the DAG is correctly specified.

- **Different DAGs imply different conditioning strategies.** Two observationally indistinguishable datasets (same marginal and conditional distributions) may require opposite conditioning sets depending on the true causal structure.

## Application Procedure

Instantiate the model against a causal inference problem in observational data.

1. **Specify the causal question precisely.** What is the treatment X? What is the outcome Y? Write the causal question: "What is the causal effect of X on Y?"

2. **Draw the DAG.** List all variables you believe are in the system (including unobserved confounders, mediators, colliders). Encode each direct causal relationship as an edge. A variable should have an edge to another only if you believe the first *directly* causes the second (not merely associated).

3. **Identify all paths from X to Y.**
   - Causal paths: all edges point from X toward Y.
   - Back-door paths: paths that enter X from the left (X ← ... → Y). These represent confounding.
   - Check for colliders on each path (→ C ←); they block the path unless you condition on C.

4. **Apply the back-door criterion.** Find a conditioning set Z such that:
   - Z blocks all back-door paths (using d-separation rules).
   - Z contains no descendants of X (to avoid post-treatment bias).
   - If no such set exists, state that the causal effect is unidentifiable from this DAG.

5. **Propose the control strategy.** Condition on Z (via regression, matching, or stratification). Report the causal effect of X on Y within strata of Z.

6. **Check for collider bias.** Scan the DAG for colliders on the causal path or confounding paths. If you condition on a collider, explicitly flag that you are introducing collider bias.

7. **Check boundary conditions** (below). If any apply, note that the identification strategy may not be valid.

8. **Report the identification status:**
   - Identifiable: Z exists and satisfies back-door criterion; state what to condition on.
   - Unidentifiable: unmeasured confounder blocks all back-door sets; state what would need to be measured or argue for a sensitivity analysis.
   - Sensitive to DAG misspecification: flag if changing one edge changes the conditioning strategy dramatically.

## Boundary Conditions

The Causal DAG model assumes a directed acyclic structure and breaks down or becomes misleading under several conditions:

- **Cycles and feedback.** The model assumes no cycles (X causes Y causes X). In systems with feedback loops (e.g., treatment affects outcome affects future treatment), a DAG cannot represent the structure. Extend to Structural Causal Models (SCMs) or dynamic models.

- **Unmeasured and unmeasurable confounders.** The back-door criterion assumes all confounders are either measured or irrelevant. If a critical confounder is unmeasured (e.g., genetic predisposition in an observational study), the causal effect is unidentifiable. Use sensitivity analysis to bound the bias.

- **Specification error in the DAG.** The identification strategy is only valid if the DAG is correctly specified. Misspecifying edges (adding or removing causal relationships) changes the conditioning set. The model gives no guidance on verifying the DAG from data alone.

- **Interference / spillovers.** The model assumes that the treatment X on one unit does not affect the outcome Y of other units (SUTVA). In networks, markets, or clusters, this breaks down. Extend to network causal models.

- **Discrete / categorical outcomes with non-collapsibility.** For odds ratios and relative risks (not differences), conditioning on a variable can change the causal effect even if the variable is not a confounder. The back-door criterion applies cleanly only to linear or difference-based effects.

- **Time-varying treatments and confounding.** If treatment is applied in stages and later confounders depend on earlier treatment, standard DAG analysis requires special handling (g-methods, marginal structural models). A static DAG misses the temporal dynamics.

## Output Format

```
## Causal DAG Analysis: <treatment → outcome>

**Causal question:** What is the causal effect of <X> on <Y>?
**Variables in system:** <list all nodes: treatments, outcomes, confounders, mediators, colliders, unobserved>

### DAG sketch
<text description of edges and paths, or ASCII / structured description>

### Paths from X to Y
| Path | Type | Open/Closed? | Notes |
|---|---|---|---|
| X → Y | Causal | Open | Direct effect |
| X ← C → Y | Back-door | <Open if C unconditioned> | Confounder |
| X → M → Y | Causal + Mediated | Open | Indirect effect |
| X → C ← Y | Collider | <Closed if C unconditioned> | Collider bias if conditioned |

### Back-door paths and confounders
<which variables confound X → Y, which open back-door paths>

### Identification status
- **Identifiable:** Yes / No / Partially
- **Conditioning set Z:** <variables to condition on per back-door criterion>
- **Justification:** <d-separation argument showing Z blocks all back-door paths>

### Causal effect estimate
- **Target:** causal effect of X on Y
- **Strategy:** <condition on Z via regression / matching / stratification>
- **Sensitivity:** <if Z is incomplete or unmeasured confounder present, note required for validity>

### Collider bias check
<whether conditioning on any collider would introduce bias; flag if applicable>

### Boundary-condition notes
<which boundary conditions apply: unmeasured confounding, cycles, interference, time-varying treatment, etc.>

### Confidence: high | medium | low
<reasoning: clarity of DAG specification + completeness of measured variables + robustness to plausible DAG changes + whether back-door criterion yields a clean control set>
```
