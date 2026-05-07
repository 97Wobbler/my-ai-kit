---
name: trophic-cascade-analysis
display_name: Trophic Cascade Analysis
class: lens
underlying_class: native
domain: ecology
source: Estes & Palmisano (1974); formalized in community ecology by Paine (1980), Power (1990)
best_for:
  - Predicting ecosystem response to predator removal or reintroduction
  - Diagnosing unexpected community shifts after a single species intervention
  - Tracing indirect effects through food webs
one_liner: "Trace the downstream effects of predator removal or restoration on lower trophic levels."
---

# Trophic Cascade Analysis

## Overview

A trophic cascade is a top-down ecological effect: a change in predator abundance propagates downward through the food web, causing often-unexpected shifts in prey and plant communities far removed from the initial intervention. Rather than predicting ecosystem change from bottom-up (productivity, nutrient availability), this lens maps how a single apex predator removal or recovery can trigger a chain reaction across multiple trophic levels. Practitioners use it when a species intervention produces ecosystem-wide consequences that seem disproportionate to the species' direct abundance, or when an apparently isolated community shift has no obvious local cause.

## Analytical Procedure

### Phase 1 — Establish the Focal Predator and Baseline Food Web

1. **Identify the focal predator** (the species being removed, reintroduced, or whose abundance changed). If multiple species changed simultaneously, isolate one as the focal change; treat others as confounds to be noted.

2. **Map the direct food web around the focal predator.** For each prey species that the focal predator eats, list:
   - Prey species name
   - Proportion of focal predator's diet (% by biomass or frequency)
   - Functional role of that prey (e.g., herbivore, omnivore, scavenger)

3. **For each direct prey, list its own predators.** Include the focal predator and all others. Create a table:
   | Prey Species | Focal Predator Diet % | Other Predators | Abundance Control |
   |---|---|---|---|
   | <name> | <number> | <list> | <which predator is primary controller> |

4. **Identify plants or resources eaten by the direct prey.** For herbivorous prey, list the plant genera or functional groups (grasses, forbs, shrubs, algae, etc.). For omnivorous prey, list both animal prey and plant resources.

5. **Document the baseline state.** Before the focal predator change, record:
   - Focal predator abundance (density, biomass, or presence/absence)
   - Direct prey population sizes or densities
   - Plant/resource community composition (species list, cover %, or biomass)
   - Any measured predation rates (kills per predator per unit time)

### Phase 2 — Trace the Cascade

6. **Predict the immediate effect of the focal predator change.** If predator abundance increases, prey should decrease (release of predation). If predator abundance decreases, prey should increase (relaxation of predation). Write this prediction as a hypothesis:
   - "If focal predator increases, direct prey <X> will decrease by >20% within <timeframe>."

7. **For each direct prey species, ask: "Who else eats this prey, and how important is the focal predator in controlling it?"**
   - If the focal predator accounts for <20% of predation mortality on that prey, the prey may not respond to focal predator change. Mark as "weakly coupled."
   - If the focal predator accounts for >50% of predation mortality, that prey is "tightly coupled" and should respond strongly.
   - If multiple predators are roughly equal, the prey is "redundantly controlled" — predator release may be dampened by compensatory predation from other predators.

8. **For each prey that is tightly coupled, predict the second-order effect on its predators and food resources.**
   - If focal predator increases and tightly coupled prey decreases, then predators of that prey (other than the focal predator) will have less food. Those predators may decline or shift diet.
   - If focal predator decreases and tightly coupled prey increases, then plants eaten by that prey will experience more herbivory. Plant abundance or species composition may shift.

9. **Extend one more level.** For plants affected in step 8:
   - If herbivory increases on plant species A, does this suppress A? Does it release competitor species B? Does the shift in plant composition feed back to herbivore populations?
   - Document predicted changes in plant community structure, diversity, or dominance.

10. **Check for omnivory and loops.** If any species in the cascade is omnivorous (eats both herbivores and plants, or eats multiple trophic levels), note whether its response to prey change is ambiguous or self-dampening. Omnivory can suppress trophic cascades by creating alternative feeding routes.

### Phase 3 — Evaluate Cascade Strength and Resilience

11. **Classify the strength of each linkage in the cascade:**
    - **Strong**: Predator removal causes >40% change in prey within one generation; prey change causes >30% change in next trophic level.
    - **Moderate**: Changes in the 15–40% range.
    - **Weak**: Changes <15% or not detectably different from background noise.

12. **Identify potential stabilizers or suppressors:**
    - Compensatory predation (other predators increase when focal predator declines)
    - Dietary flexibility (prey switch to alternative food sources)
    - Spatial heterogeneity (some subpopulations escape the cascade due to refugia)
    - Lag effects (responses are delayed, allowing time-dependent interactions)

13. **For each trophic level affected, list alternative explanations for observed change:**
    - Is the change in abundance better explained by climate, nutrient availability, disease, or other simultaneous interventions?
    - Is the timing of the change consistent with a cascade (expected lag <2 generations) or does it suggest an independent driver?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Focal predator identified and baseline abundance documented | Y/N |
| Direct food web mapped (predator → prey → plants) with quantified diet % | Y/N |
| For each direct prey, primary predator(s) identified and coupling strength assessed | Y/N |
| Second-order and third-order trophic levels explicitly predicted | Y/N |
| Omnivory checked and its effect on cascade amplitude noted | Y/N |
| Each linkage in the predicted cascade classified as strong/moderate/weak | Y/N |
| At least one alternative non-cascade explanation for each observed change | Y/N |

## Red Flags

- Focal predator is identified but its diet composition is not quantified. Without knowing how much of the diet is each prey, you cannot weight which prey changes matter most.
- Prey response is assumed without checking for other predators. If three species predate the focal prey equally, removing one predator may produce no detectable effect.
- The cascade extends more than four trophic levels without evidence. Most cascades attenuate beyond trophic level +3; deeper predictions require empirical data on interaction strengths.
- Omnivorous species are mentioned but their response to prey change is not explicitly resolved. Omnivory muddies cascades by creating feedback loops that are difficult to predict.
- Alternative explanations (climate, nutrients, disease) are never considered. A correlation in time between predator change and ecosystem shift is not proof of causation.
- Resilience is not discussed. Even strong cascades can be dampened by refugia, migration, or resource subsidy from outside the study system.

## Output Format

```
## Trophic Cascade Analysis Report

**Focal predator:** <species name>
**Intervention:** <removal / reintroduction / abundance change> in <timeframe>
**Baseline abundance:** <density, biomass, or presence>
**Study system:** <ecosystem type, location, spatial extent>

### Direct Food Web
| Prey Species | % of Focal Predator Diet | Other Predators | Coupling Strength |
|---|---|---|---|
| <name> | <number> | <list> | strong / moderate / weak |

### Trophic Cascade Prediction

#### Level 1 → Level 2 (Direct Effect)
<If focal predator increases, then: ...>
<If focal predator decreases, then: ...>
Expected magnitude: strong / moderate / weak
Evidence of coupling: <% diet composition, predation rate, or field observation>

#### Level 2 → Level 3 (Second-order Effect)
Prey species affected: <name>
Downstream predators/resources: <list>
Predicted change: <increases / decreases / shifts composition>
Expected magnitude: strong / moderate / weak
Redundancy/compensatory effects: <noted if applicable>

#### Level 3 → Level 4 (Third-order Effect)
Plant or basal resource affected: <list>
Predicted change in dominance/diversity: <increases / decreases / switches to different species>
Expected magnitude: strong / moderate / weak

### Omnivory Check
Omnivorous species in cascade: <list or "none detected">
Effect on cascade attenuation: <describes feedback or stabilization>

### Alternative Explanations
| Observed Change | Cascade Explanation | Alternative (Climate / Nutrients / Disease / Spatial) |
|---|---|---|
| <trophic level affected> | <mechanism> | <rival hypothesis with likelihood> |

### Cascade Strength Summary
- Strong linkages (>40% change): <count and examples>
- Moderate linkages (15–40% change): <count and examples>
- Weak linkages (<15% change or non-detectable): <count and examples>
- Overall cascade amplitude: strong / moderate / attenuated

### Resilience Factors
1. <stabilizer or suppressor, with mechanism>
2. ...

### Confidence
<high / medium / low> — <justification: e.g., "high because diet proportions are quantified from >50 observations and other predators are well-documented; low because plant response lag is unknown">
```
