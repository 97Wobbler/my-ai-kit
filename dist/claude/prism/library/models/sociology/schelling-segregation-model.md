---
name: schelling-segregation-model
display_name: Schelling Segregation Model
class: model
underlying_class: native
domain: sociology
source: Thomas C. Schelling, "Dynamic Models of Segregation," Journal of Mathematical Sociology, 1971; extended in Micromotives and Macrobehavior (1978)
best_for:
  - Predicting emergent segregation patterns from weak individual preferences
  - Explaining how tolerance thresholds at the individual level produce homogeneous neighborhoods
  - Understanding tipping points and path dependence in residential integration
one_liner: "Weak individual preferences → strong aggregate segregation."
---

# Schelling Segregation Model

## Overview

Schelling's Segregation Model claims that **even when individuals hold only mild preferences for living near their own group**, the iterative process of local relocation decisions produces highly segregated, homogeneous neighborhoods at the macro level. The model is purely descriptive and mechanistic: it does not require malice, explicit discrimination, or strong preference intensity to generate the observed outcome. Instead, it shows how individual rationality (moving when dissatisfied with local composition) operating on spatial neighborhoods produces emergent segregation as a system-level property. The model is both explanatory and predictive — it illuminates why segregation persists even when median preferences are integrationist, and it predicts how sensitive the system is to initial conditions and threshold parameters.

## Core Variables and Relationships

1. **Individual tolerance threshold (τ)** — the maximum percentage of neighbors from a different group an agent will accept before relocating.
   - Measured as a fraction: τ ∈ [0, 1]. Example: τ = 0.3 means an agent will tolerate up to 30% of neighbors from another group.
   - Lower τ → more segregation pressure; higher τ → more tolerance for diversity.
   - Empirically, survey data suggests median τ ≈ 0.3–0.4 in U.S. contexts (majority prefer not to be a minority in their immediate neighborhood).

2. **Local neighborhood composition** — the fraction of neighbors of each group in an agent's immediate spatial vicinity.
   - Defined at small scale: typically the 8 adjacent cells in a grid model, or the k nearest neighbors in a continuous model.
   - Composition changes as agents relocate.

3. **Vacant sites and relocation mechanics** — where agents can move when dissatisfied.
   - Availability and distribution of vacant housing.
   - Relocation rule: dissatisfied agents (composition exceeds threshold) move to a random vacant site.
   - Order of moves: simultaneous or sequential updates produce different dynamic trajectories.

4. **Initial distribution** — the starting configuration of the two (or more) groups in space.
   - Random scatter, clustered, mixed, homogeneous.
   - Initial distribution strongly influences convergence time and final segregation level.

5. **Segregation index (measurable outcome)** — quantifies final spatial homogeneity.
   - Dissimilarity index D: fraction of agents that would have to move to achieve perfect integration.
   - D ∈ [0, 1]. D = 0 (perfect integration); D = 1 (perfect segregation).

**Core relationship:**
- **Even weak individual preferences (τ = 0.3–0.4) → high macro segregation (D = 0.7–0.8).**
- The gap between individual tolerance and macro segregation is the model's central insight.

## Key Predictions

- **Tipping points are sharp, not smooth.** As neighborhood composition moves toward an agent's threshold, relocation accelerates nonlinearly. A small shift in initial conditions can flip a neighborhood from integrated to nearly homogeneous.

- **Segregation emerges from relocation dynamics even if no agent has a strong preference for homogeneity.** A tolerance of "I'll move if more than 40% of my neighbors are different" is not a strong preference for segregation, yet it produces it.

- **Path dependence and lock-in.** Once a neighborhood tips toward one group, the negative feedback loop (agents of the minority group leave, reducing diversity further, accelerating departures) is self-reinforcing. Reversing segregation once established is much harder than preventing it.

- **Spatial scale matters.** If tolerance thresholds are defined relative to small neighborhoods (8 neighbors), segregation is severe; if relative to larger neighborhoods (100+ people), segregation is less pronounced. The "neighborhood" definition is not objective — it is endogenously formed through social interaction distance.

- **Cluster formation precedes full separation.** Segregation does not distribute uniformly; agents of the same group cluster first, then expand, leaving the other group in isolated pockets — this intermediate stage is an attractor.

- **The level of segregation is insensitive to small preference shifts near the threshold but highly sensitive to threshold crossing.** Moving τ from 0.35 to 0.45 produces little macro change; moving from 0.45 to 0.55 produces a discontinuous drop in segregation.

## Application Procedure

Instantiate the model against a concrete residential context or policy scenario.

1. **Define the spatial domain and agents.** What is the geographic area (a city block, neighborhood, metropolitan area)? How many agents of each group? Is the population fixed or growing?

2. **Establish individual tolerance thresholds (τ).** Survey data or ethnographic accounts often provide bounds. If unavailable, test sensitivity across a plausible range: 0.2, 0.3, 0.4, 0.5.
   - Write down the assumption explicitly: "We assume the median agent will tolerate up to 35% of their immediate neighbors from the other group."

3. **Define "neighborhood" and local composition metric.** Is it the k nearest spatial neighbors, or the inhabitants of a bounded region (e.g., the 8 adjacent grid cells)? Clearly state the radius or count, as the choice drives segregation sensitivity.

4. **Initialize the spatial distribution.** Document the starting configuration: random, clustered, segregated, or mixed. Run sensitivity tests on initial conditions if possible.

5. **Run the relocation dynamics (conceptually or computationally).**
   - Iterate: for each agent, measure local composition; if composition exceeds τ, mark for relocation.
   - Move dissatisfied agents to random vacant sites (or to the nearest vacant site if bounded search is more realistic).
   - Repeat until no agent is dissatisfied (convergence) or a maximum iteration count is reached.

6. **Measure the final segregation index (D or similar).** Quantify the gap between initial and final composition diversity.

7. **Check sensitivity.**
   - How much does segregation level change if τ increases by ±0.05?
   - How sensitive is the outcome to initial distribution, neighborhood radius, or order-of-moves (simultaneous vs. sequential)?

8. **Check boundary conditions** (below). If any apply, note what additional mechanisms or constraints are needed.

9. **Generate the prediction.**
   - What segregation index is predicted for the given τ and neighborhood definition?
   - How long is the convergence timescale (measured in relocation rounds)?
   - What is the robustness of the final state to small perturbations?

## Boundary Conditions

Schelling's model applies cleanly to voluntary relocation driven by local composition. It breaks down or requires modification under:

- **Constrained housing supply and costs.** The model assumes vacant sites are freely available everywhere. In reality, agents cannot move freely due to affordability, discrimination, or shortage. The model predicts higher segregation than actually observed when housing is scarce but does not explain *which* groups get locked into poor neighborhoods — that requires a model of income, pricing, and credit.

- **Multi-group settings with hierarchies.** The classic model uses two groups with symmetric preferences. When there are more than two groups or when group preferences are asymmetric (e.g., one group actively excludes, another is indifferent), the equilibrium structure differs and is not fully characterized by Schelling's framework.

- **Institutional and legal discrimination.** Redlining, discriminatory lending, zoning laws, and explicit exclusion override pure preference-driven segregation. Schelling's model captures preference-driven segregation; it does not account for structural discrimination, which can produce segregation even with integrationist preferences.

- **Endogenous preference formation.** The model takes τ as exogenous. In reality, preferences are shaped by experience, peer effects, and media narratives. If living in a segregated neighborhood *increases* preference for segregation (or integration), the fixed-τ assumption breaks down and a dynamic preference model is needed.

- **Income and class as confounds.** If group differences correlate with income, the model conflates preference-driven segregation with economic segregation (affording different neighborhoods). Disentangling the two requires explicit income or wealth stratification.

- **Network effects and social-identity dynamics.** If agents care not only about the racial/ethnic composition of their neighborhood but also about status, peer approval, or identity signaling, the dynamics are richer and the relocation threshold becomes endogenous to social proof.

## Output Format

```
## Schelling Segregation Analysis: <context name>

**Domain:** <residential area, city, region>
**Agent groups:** <Group A, Group B> (and relative population sizes)
**Tolerance threshold τ:** <value, with justification or sensitivity range>
**Neighborhood definition:** <k nearest neighbors, or grid radius, or distance>

### Initial distribution
| Group | Count | Spatial pattern |
|---|---|---|
| Group A | n | <clustered / random / segregated> |
| Group B | m | <clustered / random / segregated> |

### Relocation dynamics
- Move rule: <agents exceeding τ move to random/nearest vacant site>
- Order: <simultaneous or sequential updates>
- Convergence criterion: <all satisfied, or max iterations>

### Predicted outcome
- Final segregation index D: <estimated value, with reasoning>
- Convergence time: <number of rounds or estimate>
- Equilibrium structure: <which areas integrate, which segregate, why>

### Sensitivity
- τ ± 0.05: <does segregation change, how sharply>
- Initial distribution: <which starting patterns converge to the same D, which diverge>

### Policy implications
- Interventions that would lower final D (e.g., subsidized mixed-income housing, quota targets)
- Why raising average tolerance τ alone is a weak lever (mechanical: it is not the mean, but the distribution of thresholds, that matters)

### Boundary-condition check
<which conditions apply: housing constraints, multi-group asymmetries, discrimination, preference endogeneity, income confounds, identity dynamics. Note what additional model components are needed.>

### Confidence: high | medium | low
<reasoning: clarity of τ estimation from data + fit of neighborhood definition to actual social distance + whether the population is fixed and voluntary-relocation-driven + applicability of boundary conditions>
```
