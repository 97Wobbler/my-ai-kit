---
name: causal-dag-for-ml
display_name: Causal DAG for ML
class: lens
underlying_class: native
domain: ai
source: Judea Pearl (Causality, 2009); applied in ML by Cunningham, Sekhon, and others (2020s)
best_for:
  - Identifying confounders before claiming causality from observational data
  - Documenting assumptions in a model's causal claims
  - Detecting when features are colliders or mediators, not confounders
one_liner: "Check for confounders when claiming causality from observational data in ML."
---

# Causal DAG for ML

## Overview
A Causal Directed Acyclic Graph (DAG) maps assumptions about which variables causally influence which others. Before claiming that a feature has a causal effect on an outcome, you must draw the DAG, identify confounders (common causes of both the feature and outcome), and either measure or control for them. Practitioners use this when they have observational data and are tempted to interpret correlations as causation — the DAG forces the assumptions into the open where they can be scrutinized.

## Analytical Procedure

### Phase 1 — Map the DAG

1. **List all variables in your analysis.** Include the treatment/feature (T), the outcome (Y), all measured confounders (C), and any unmeasured variables you suspect might matter.

2. **For each variable, ask: "What causes this variable?"** Draw an arrow from each cause to the variable it influences. Do NOT draw an arrow if you do not believe there is a causal relationship. If you are unsure, write the assumption down and mark it.

3. **Identify d-separation paths.** A path between T and Y exists if:
   - You can traverse arrows backward and forward (respecting direction except through open colliders)
   - No variable on the path blocks information flow between T and Y
   An unblocked path means a causal effect or confounding can exist. A blocked path means no causal association flows through it.

4. **For each unblocked path from T to Y, classify it as one of:**
   - **Causal** — goes directly T → Y or through mediators (variables Y depends on that T influences)
   - **Confounding** — goes T ← C → Y (C causes both T and Y)
   - **Collider bias** — goes through a variable Z where T → Z ← Y (if you condition on Z, you create spurious association)

### Phase 2 — Identify Confounders

5. **List all confounding paths (T ← C → Y).** These are the variables you must measure and control for to estimate the causal effect of T on Y.

6. **For each confounder, ask:**
   - Do we measure it? Y/N
   - Is it a parent of T (influences treatment assignment)? Y/N
   - Is it a parent of Y (influences outcome independent of T)? Y/N
   - Are there descendants of this confounder we've included in our analysis? (If yes, you may have blocked the confounder.)

7. **Identify unmeasured confounders.** Circle any variable on a confounding path that you do not measure. These cannot be controlled for in standard regression. You must either:
   - Measure the variable
   - Use instrumental variables (if available)
   - Use sensitivity analysis to show how much the unmeasured confounder would need to affect T and Y to change your conclusion
   - Acknowledge the limitation

### Phase 3 — Check for Collider Bias

8. **Identify all colliders on paths between T and Y.** A collider is a variable with two or more incoming arrows (T → Z ← Y). If you condition on a collider (include it as a control variable or filter the data by it), you open a spurious path.

9. **For each collider you included in your analysis, ask:**
   - Did we intentionally condition on this variable? Y/N
   - If yes, is there a good causal reason (e.g., it is part of the causal chain we want to measure)?
   - If no, remove it from your model.

### Phase 4 — Validate and Document

10. **Redraw the DAG after all edits.** Confirm that all confounders are either measured and controlled for or acknowledged as unmeasured.

11. **Write a causal assumptions statement.** List each edge in your DAG (each causal claim) and rate your confidence in that edge as `high` (backed by prior knowledge or experiments), `medium` (plausible but not directly tested), or `low` (speculative).

12. **Compare your DAG to existing domain knowledge.** Ask a domain expert: "Does this causal story match how you understand the system?" Iterate if needed.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All variables in the analysis are on the DAG | Y/N |
| Every arrow on the DAG represents a claimed causal relationship | Y/N |
| At least one confounding path (T ← C → Y) was identified | Y/N |
| All measured confounders are listed and justified | Y/N |
| Unmeasured confounders are explicitly acknowledged | Y/N |
| No colliders are being conditioned on without justification | Y/N |
| A domain expert has reviewed the causal assumptions | Y/N |
| Each causal claim is rated high/medium/low confidence | Y/N |

## Red Flags

- The DAG is absent or hand-wavy ("I'm pretty sure X causes Y"). A causal claim without a DAG is a guess dressed as analysis.
- Every variable is connected to every other variable. Either the system is genuinely fully connected (rare) or you are avoiding the discipline of specifying causal direction.
- A confounder is measured but not controlled for in the regression, and no reason is given. This is confounding bias waiting to happen.
- A collider is included as a control variable with no justification. This opens spurious paths and biases the estimate toward zero or can flip the sign.
- The DAG was drawn once and never revisited after the analyst saw the results. If results surprise you, the DAG assumptions should be questioned first.
- "Correlation is not causation" appears in the final write-up but the DAG is still absent. The statement is correct but useless without the DAG to show what causation claim is being made.

## Output Format

```
## Causal DAG Assessment

**System description:**
<Brief description of the treatment T, outcome Y, and measurement context>

### DAG Edges
| From | To | Causal claim | Confidence |
|---|---|---|---|
| <var1> | <var2> | <assumed mechanism> | high/medium/low |

### Confounding Paths
| Path | Confounder | Measured? | Control method |
|---|---|---|---|
| T ← C → Y | <C> | Y/N | <regression, matching, stratification, or "unmeasured"> |

### Unmeasured Confounders
- <Variable>: <Why it might confound> (Sensitivity analysis shows conclusion robust if confounder effect size < X)

### Colliders Identified
| Collider | Conditioned on? | Justification |
|---|---|---|
| <Z: T → Z ← Y> | Y/N | <reason or "removed"> |

### Causal Assumptions Statement
1. <Assumption and confidence level>
2. ...

### Domain Review
Reviewed by: <name/title or "not yet reviewed">
Feedback: <acceptance, disagreements, or requested modifications>

### Confidence
<high/medium/low> — <justification. Example: "high confidence if confounder X is measured and control method is defensible; medium if unmeasured confounder with plausible effect; low if multiple critical confounders suspected unmeasured">
```
