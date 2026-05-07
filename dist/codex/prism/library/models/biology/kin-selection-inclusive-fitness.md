---
name: kin-selection-inclusive-fitness
display_name: Kin Selection / Inclusive Fitness
class: model
underlying_class: native
domain: biology
source: William D. Hamilton, "The Genetical Evolution of Social Behaviour," Journal of Theoretical Biology, 1964
best_for:
  - Predicting when organisms will sacrifice fitness for relatives
  - Explaining the evolution of altruism and cooperation in family groups
  - Analyzing inclusive fitness payoffs across genealogical relationships
one_liner: "Altruism evolves when relatedness × benefit exceeds individual cost."
---

# Kin Selection / Inclusive Fitness

## Overview

Hamilton's Kin Selection model claims that an organism's evolutionary fitness is not limited to direct reproduction (offspring) but extends to **all copies of its genes in existence**, weighted by the probability that relatives carry those same genes by descent. This reframes altruism and cooperation: a gene for self-sacrifice can spread if the recipients of that sacrifice are sufficiently close relatives and the fitness gains to them are large enough. The model is both descriptive and predictive — it explains why organisms bias their behavior toward kin, and it predicts the threshold at which altruistic behavior becomes evolutionary stable. The core insight is captured in the inequality **rB > C**: a behavior spreads if the genetic relatedness (r) to the recipient times the fitness benefit (B) to the recipient exceeds the fitness cost (C) to the actor.

## Core Variables and Relationships

1. **Relatedness (r)** — the probability that a relative carries a copy of the actor's gene by descent.
   - Parent to offspring: r = 0.5
   - Full sibling to sibling: r = 0.5
   - Grandparent to grandchild: r = 0.25
   - Aunt/uncle to niece/nephew: r = 0.25
   - First cousin to first cousin: r = 0.125
   - Unrelated individuals: r = 0
   - Relatedness decreases by half with each generational step

2. **Fitness Benefit (B)** — the gain in reproductive success (offspring produced, or increased survival-to-reproduction) experienced by the recipient of an altruistic act, relative to the counterfactual.
   - Measured in change in expected offspring count or survival probability
   - Higher when the recipient is young (more reproductive future) or in severe need
   - Must be discounted by the probability that the benefit actually reaches the recipient

3. **Fitness Cost (C)** — the loss in reproductive success (reduction in offspring or survival) borne by the altruist as a result of the act.
   - Measured in the same currency as B (expected offspring or survival)
   - Higher when the act diverts resources from the actor's own reproduction
   - Must account for opportunity costs

4. **Inclusive Fitness (W)** — the total evolutionary fitness of an organism, combining:
   - Direct fitness: reproduction and survival of the organism's own offspring (weighted 1.0)
   - Indirect fitness: reproduction and survival of relatives (weighted by r)
   - Formula: W = B_direct + Σ(r_i × B_indirect_i) − C_total
   - An altruistic act increases inclusive fitness if rB > C

5. **Evolutionary Stability** — a behavior (altruistic or otherwise) can spread in a population if:
   - Organisms carrying the allele for that behavior have higher inclusive fitness than those without it
   - The behavior persists once established, resisting invasion by alternative behaviors
   - This is stricter than "rB > C" alone — the cost and benefit must also not create incentives for cheating or defection

## Key Predictions

- **Altruism is strongest toward close relatives.** An organism will sacrifice more for a sibling (r=0.5) than for a grandchild (r=0.25) even if the absolute benefit to the grandchild is identical, because the genetic overlap is lower.

- **The "family circle" of altruism shrinks with distance.** Grandparents may provide substantial help to grandchildren, but great-aunts may provide none. The boundary tracks the r threshold where rB can no longer exceed the cost of help.

- **Altruism is conditional on the recipient's need and potential.** An organism will invest heavily in rescuing a young, healthy relative (high B, long reproductive future) but little in a very old or sterile one (low B, even if r is high).

- **Nepotism in resource allocation is adaptive, not a moral failure.** Parents bias resources toward biological children (and sometimes genetic relatives) at the expense of unrelated orphans or peers. The model predicts this pattern across all social mammals.

- **Kin recognition mechanisms evolve.** If altruism toward relatives is favored, selection also favors cognitive and behavioral mechanisms to identify and locate kin (smell, appearance, spatial proximity, learned association), because random altruism is a losing strategy.

- **Kin-biased conflict resolution.** Organisms will invest in mediating conflicts between their own kin (where inclusive fitness is shared) but not between unrelated parties. Family feuds are mitigated differently than disputes between strangers.

## Application Procedure

Instantiate the model against a concrete social behavior or allocation of resources you are trying to explain or predict.

1. **Define the actor, the recipient, and the context.** Who is making the choice or exhibiting the behavior? Who stands to benefit or suffer? What is the constraint or trade-off (time, energy, risk)?

2. **Identify the coefficient of relatedness (r) between actor and recipient.** Use the genealogical table above. If the relationship is traced through multiple lineages or is uncertain, estimate conservatively (e.g., for half-siblings, r = 0.25 if only one parent is shared).

3. **Quantify or estimate the fitness benefit B to the recipient.** In what form? (survival gains, fecundity gains, parental effort, protection, shared resources?) Estimate the marginal reproductive impact relative to the no-help counterfactual. For humans or long-lived organisms, consider both immediate and lifetime effects.

4. **Quantify or estimate the fitness cost C to the actor.** Is the cost in lost mating opportunities, reduced offspring quality, increased injury risk, reduced foraging time? Measure in the same units as B. Include opportunity costs — if the actor spends time helping a sibling, that is time not spent on own reproduction.

5. **Calculate or compare rB against C.** If rB > C, the model predicts the behavior will be stable and observed. If rB < C, the model predicts the behavior should be rare or absent (unless confounded by other motives). If rB ≈ C, the outcome is on the margin — small errors in estimation flip the prediction.

6. **Check whether the actor has kin-recognition capability.** Can the actor reliably identify the recipient as a relative, or is there information asymmetry (e.g., the actor does not know the recipient's true genetic relatedness)? If recognition is costly or unreliable, the threshold for behavior to spread may not be met.

7. **Evaluate boundary conditions** (below). If any apply, flag whether the model is incomplete.

8. **Generate the prediction:**
   - Will the behavior occur, and with what frequency or intensity?
   - What is the predicted rank-ordering of altruism (self > full sibling > half-sibling > cousin > unrelated)?
   - What would disconfirm the model (e.g., equal altruism toward kin and nonkin, or altruism that violates the r-weighting)?

## Boundary Conditions

Hamilton's Kin Selection model applies well to behavior in small, kinship-structured populations and to allocative decisions among relatives. It is less reliable when:

- **Reciprocal altruism dominates.** In large, anonymous societies (modern cities), altruism toward unrelated individuals is common and sometimes strong. Reciprocal-altruism and reputation models (Trivers, 1971) are necessary complements to kin selection.

- **Adoption, step-kinship, and social kinship complicate relatedness.** A step-parent or adopted child has r=0 genetically but may be treated with high-r investment. The model requires updating r to account for the actor's *subjective or behavioral* kinship, not just genealogical relatedness — this introduces measurement error.

- **Kin competition and conflict.** Parent-offspring conflicts (Trivers, 1974) and sibling rivalry can erase altruism despite high r. The model assumes costless cooperation among kin; in reality, kin often compete for resources, and the net inclusive-fitness benefit can flip sign.

- **Inbreeding and population structure.** In small populations, altruism toward kin increases inbreeding, which reduces offspring fitness through genetic load. The cost of inbreeding depression can dominate the benefit of kin cooperation, especially over multiple generations.

- **Externalities and group-selection effects.** If altruism toward kin creates positive spillovers (e.g., better family coordination, reduced family conflict, collective defense) that benefit the group, group-selection dynamics interact with kin selection. Kin Selection alone misses this amplification.

- **Dishonesty about kinship.** In species where paternity uncertainty is high (many birds and mammals), the *effective* r is lower than the nominal genealogical r, because the actor may not father offspring he believes are his. The model predicts behavior based on *perceived* kinship, not true kinship, which creates systematic errors when paternity is uncertain.

## Output Format

```
## Kin Selection Analysis: <behavior or allocation>

**Actor:** <organism or individual>
**Recipient:** <relative or group>
**Context:** <resource, behavior, or trade-off at stake>

### Relatedness and fitness parameters
| Parameter | Value | Basis |
|---|---|---|
| Relatedness (r) | <0.5, 0.25, 0.125, etc.> | <genealogy> |
| Fitness benefit B | <high / medium / low> | <specific gain to recipient> |
| Fitness cost C | <high / medium / low> | <specific cost to actor> |
| rB vs C | <rB > C / rB < C / rB ≈ C> | <calculation or comparison> |

### Kin-recognition capability
- Can the actor identify the recipient as kin? <yes / no / with error>
- Information available to the actor: <appearance, proximity, behavioral cues, explicit knowledge>

### Prediction
- Expected behavior (Kin Selection model): <behavior will be X with frequency/intensity Y>
- Rank-ordering of altruism by relatedness: <self > sibling > cousin > unrelated>
- Disconfirming observations: <what would falsify the prediction>

### Competing mechanisms
- Reciprocal altruism: <if applicable>
- Group selection / family-level cooperation: <if applicable>
- Sexual selection or mate choice: <if applicable>

### Boundary-condition check
<which boundary conditions apply and whether they weaken the model's predictive power>

### Confidence: high | medium | low
<reasoning: precision of r estimation + availability of B and C data + kin-recognition reliability + population structure and paternity certainty>
```
