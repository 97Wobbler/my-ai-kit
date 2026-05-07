---
name: triz
display_name: TRIZ (Theory of Inventive Problem Solving)
class: lens
underlying_class: native
domain: manufacturing
source: Genrich Altshuller, 1956–1985; systematized in *The Innovation Algorithm* (2000)
best_for:
  - Breaking deadlocked design trade-offs by mapping to solved analogies
  - Identifying the actual contradiction blocking progress
  - Generating non-obvious solutions from 40 inventive principles
one_liner: "Break design deadlocks via the contradiction matrix and 40 inventive principles."
---

# TRIZ (Theory of Inventive Problem Solving)

## Overview
TRIZ assumes that inventive problems are not unique — the same contradictions recur across industries. By mapping your specific contradiction onto Altshuller's 39×39 contradiction matrix, you retrieve the 40 inventive principles that have solved it elsewhere. The lens is powerful only when the contradiction is stated precisely; vague problems yield vague principles. Practitioners reach for TRIZ when conventional trade-offs feel mandatory ("lighter but more fragile," "faster but less precise") and they suspect a non-obvious solution exists in the patent literature or adjacent domains.

## Analytical Procedure

### Phase 1 — Define the Technical Contradiction

1. **Identify the parameter being improved.** Choose one of the 39 engineering parameters Altshuller identified (e.g., weight, speed, precision, cost, reliability, complexity). Write it plainly.

2. **Identify the parameter being worsened.** As you improve the first parameter, what else gets worse as a side effect? Also choose from the 39 parameters. Do not say "cost increases" vaguely — be specific: does manufacturing cost increase? Material cost? Maintenance cost? These map to different cells.

3. **Quantify the contradiction if possible.** "Lighter AND faster" is not a contradiction. "Lighter (target: 20% weight reduction) AND stronger (tensile strength ≥500 MPa)" is. Specificity determines whether the matrix lookup is accurate.

4. **Test the direction.** You should be unable to improve parameter A without degrading parameter B using conventional methods (materials, geometry, processes). If you can improve both, this is not a contradiction — solve it directly without TRIZ.

### Phase 2 — Consult the Contradiction Matrix

5. **Locate the row and column.** Find your "Improving" parameter on the rows and your "Worsening" parameter on the columns of the 39×39 matrix. The cell intersection lists 1–4 inventive principles (numbered 1–40).

6. **Retrieve the principles.** Look up each recommended principle number in the reference table. Each principle is a brief statement (e.g., "Principle 1: Segmentation," "Principle 14: Spheroidality," "Principle 35: Parameter Changes").

7. **Interpret each principle in your domain.** The principles are stated abstractly. Your job is to translate them into concrete experiments or design moves specific to your problem. For example:
   - **Segmentation** applied to a bridge cable could mean braiding instead of solid wire, or modular sections that decouple.
   - **Local quality** applied to machining could mean varying the cutting angle per zone instead of uniform geometry.
   - **Dynamism** applied to a plastic mold could mean hydraulic flexibility at squeeze points instead of rigid steel.

### Phase 3 — Generate and Screen Solutions

8. **Generate at least one concrete design for each principle.** Do not stay abstract. Draw, describe, or prototype the idea enough that an engineer could evaluate it. "Apply segmentation" is not a solution; "replace solid steel shaft with braided strands in a composite tube" is.

9. **Screen for physical feasibility.** Does the solution violate materials science, manufacturing capability, or physics? For each solution, mark it as:
   - **Feasible now** — can be built with existing tooling and materials.
   - **Feasible with investment** — requires tooling or new materials but is not speculative.
   - **Speculative** — requires materials or processes that don't yet exist reliably.

10. **Screen for contradiction resolution.** For each solution, verify that it actually improves the target parameter without degrading the opposing parameter. Do not accept solutions that merely shift the trade-off.

11. **Rank by implementation cost and novelty.** Feasible-now solutions that competitors haven't adopted yet are highest value.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Improving parameter is one of Altshuller's 39 (e.g., weight, speed, precision, cost) | Y/N |
| Worsening parameter is one of the 39 and distinct from improving parameter | Y/N |
| Contradiction is stated with quantified targets, not vague trade-off language | Y/N |
| Matrix lookup completed and principles identified | Y/N |
| Each principle is translated to ≥1 concrete design idea, not abstract | Y/N |
| All generated solutions are marked feasible/investment/speculative | Y/N |
| At least one solution improves both parameters or removes the contradiction entirely | Y/N |

## Red Flags

- Contradiction is phrased as "we want X but it's hard" instead of "improving X worsens Y." TRIZ works on contradictions, not difficulties.
- Matrix lookup returns only Principle 1 (Segmentation) or only Principle 35 (Parameter Changes). These are common fallback recommendations; if that's the only result, the parameters may be mis-mapped to the matrix.
- All generated solutions are feasible-now and well-known. Either the contradiction isn't genuine or the translation of principles is shallow. Go deeper into each principle.
- A solution improves both parameters but was obvious to the design team already. TRIZ's value is in non-obvious solutions; if nothing is surprising, question whether the principles were fully explored.
- Costs and effort to implement are not estimated. Without implementation realism, recommendations stay academic.

## Output Format

```
## TRIZ Analysis

**Technical Contradiction:**
- Improving parameter: <name> (Altshuller #<nn>)
- Worsening parameter: <name> (Altshuller #<nn>)
- Quantified targets: <specific values or thresholds>

**Contradiction Matrix Lookup:**
- Matrix cell intersection (row × column): 
- Recommended principles: <#, #, #, #>

**Principle Translations & Solutions:**

### Principle <#>: <Name>
Domain translation: <how this principle applies to your problem>
Concrete design: <specific design move, not abstract>
Feasibility: feasible now | investment | speculative
Resolves contradiction: yes | no
Confidence: high | medium | low — <why>

[Repeat for each recommended principle]

**Solution Ranking**
| Design | Feasibility | Novelty (industry aware) | Implementation cost | Resolves contradiction | Rank |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | yes/no | 1 |

**Recommended Approach**
<Top-ranked solution(s) with rationale>

### Confidence
<high/medium/low> — <justification: Did the matrix lookup feel accurate? Are solutions genuinely non-obvious? How much domain expertise was required to translate principles?>
```
