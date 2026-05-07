---
name: natural-selection
display_name: Natural Selection
class: model
underlying_class: native
domain: biology
source: Charles Darwin, "On the Origin of Species by Means of Natural Selection," 1859
best_for:
  - Explaining evolutionary change in populations over time
  - Predicting which traits will increase or decrease in frequency
  - Understanding how heritable variation and differential reproduction interact to drive adaptation
one_liner: "Variation + heritability + differential reproduction = evolutionary change."
---

# Natural Selection

## Overview

Natural Selection claims that **heritable variation in a population, combined with differential reproduction tied to that variation, produces cumulative change in trait frequencies over generations**. The model explains how adaptation emerges without intentional design — not through the inheritance of acquired characteristics, but through the systematic filtering of reproductive success. The mechanism is mechanical: if a trait is heritable, if it varies across individuals, and if individuals carrying different variants have different reproductive outputs, then the trait's frequency in the population must shift. The model is explanatory and predictive; it does not require knowledge of the underlying genetics (which Darwin lacked) to apply. Applying it to a concrete population requires the procedure below.

## Core Variables and Relationships

Natural Selection operates through three necessary conditions and their interaction:

1. **Variation within the population** — individuals differ in measurable traits.
   - Phenotypic variance: observed differences in morphology, behavior, physiology
   - Heritable component of variance: the fraction of observed variation that is *not* due to environmental plasticity alone
   - Without heritable variation, no evolutionary change is possible; environmental plasticity is not transmitted

2. **Differential reproduction** — some individuals produce more surviving offspring than others, and this difference correlates with trait values.
   - Survival to reproductive maturity (viability selection)
   - Mating success / reproductive access (sexual selection)
   - Fecundity conditional on mating (number of offspring per individual)
   - Offspring survival to independence (parental investment, habitat quality)
   - The correlation between trait and reproductive output is the **selection differential**: strength of selection depends on how tightly reproduction tracks the trait

3. **Heritability h²** — the proportion of phenotypic variance that is transmitted parent-to-offspring; equivalently, the resemblance between parent and offspring for the trait in question.
   - h² = (Var_genetic) / (Var_phenotypic)
   - h² ranges from 0 (no heritable component; no parent-offspring resemblance) to 1 (purely genetic, no environmental variance)
   - Intermediate h² is typical: height h² ≈ 0.7, intelligence h² ≈ 0.5, many behavioral traits h² ≈ 0.3–0.5

**The core equation** (breeder's equation):

    R = h² · S

where R is the response to selection (change in mean trait value per generation), S is the selection differential (difference between mean trait in reproducing individuals vs. population mean), and h² is heritability.

**Directional prediction**: if heritable variation exists and differential reproduction is correlated with that variation, the mean trait value will shift toward higher-fitness phenotypes each generation. The rate depends jointly on heritability and selection strength.

## Key Predictions

- **Trait frequencies shift in the direction of the selection differential, by an amount proportional to h² and S.** A trait that increases reproductive success will increase in frequency *if and only if* it is heritable. A trait tied to fitness but not heritable (e.g., a scar from injury) will not spread.

- **Populations under consistent directional selection can exhibit large morphological changes in timescales much shorter than previously thought** (decades to centuries, not geological ages), provided mutation or migration introduces sufficient variation.

- **In the absence of continued directional selection, trait frequencies stabilize or drift slowly.** Once an allele reaches fixation or is lost, no further directional change is possible without new mutation or immigration. Populations under no consistent selection show variation but not cumulative directional change.

- **When selection favors intermediate phenotypes (stabilizing selection), variance in the population decreases while the mean shifts or stays steady.** Extreme phenotypes are filtered out each generation; populations become phenotypically more uniform.

- **Conflicting selection pressures (e.g., males compete fiercely for mates, favoring large size, while heavy males suffer higher mortality in harsh winters) produce equilibrium trait distributions**, not monotonic change. The equilibrium depends on the relative strength of the competing forces.

- **Heritable variation and reproductive output are both population-specific and environment-dependent.** The same trait may be under strong positive selection in one population / generation and negative selection in another; h² varies across populations and can change over time as genetic architecture shifts.

## Application Procedure

Instantiate the model against a concrete population and trait you are trying to explain or predict.

1. **Define the population and trait precisely.**
   - What species, population, and generation(s) are you analyzing?
   - What is the trait (morphological, behavioral, physiological)? How is it measured?
   - Over what timescale? (one generation, ten generations, 100 years?)

2. **Establish baseline variation and heritability.**
   - Is the trait variable in the population? Estimate or measure phenotypic variance or range.
   - Is that variation heritable, or is it purely environmental? Consult pedigree data, twin studies, or parent-offspring correlations to estimate h². If h² is near zero, stop: Natural Selection will not change the trait's frequency.
   - Note the source of heritable variation: Are alleles at known loci responsible, or is the genetic basis unknown? (The model works without knowing genetics, but genetic details help predict future variation.)

3. **Quantify survival and reproduction by trait value.**
   - Measure or estimate which individuals (partitioned by trait value) survive to reproductive age.
   - Measure or estimate the number of offspring per individual, by trait value.
   - Compute the selection differential S: difference between mean trait in reproducing individuals vs. the population mean before selection.
   - Note whether selection is directional, stabilizing, disruptive, or sexually antagonistic (males selected for one phenotype, females for another).

4. **Apply the breeder's equation or qualitative reasoning.**
   - Compute R = h² · S, or qualitatively estimate: high h², high S → large R; low h², weak S → R ≈ 0.
   - Predict the mean trait value in the next generation: mean_new = mean_old + R.

5. **Check for mutation, migration, or linkage.**
   - Is new genetic variation entering the population (mutation, migration from another population)? If so, h² and S may change over time.
   - Are the alleles underlying the trait in linkage disequilibrium with deleterious mutations? If so, selection on the focal trait may drag along harmful alleles, weakening the response.
   - These factors modify the simple prediction but do not negate it.

6. **Generate the prediction and identify the load-bearing assumption.**
   - Predict the trait's mean value one or more generations forward.
   - State which condition is most uncertain: variation, heritability, or selection differential? The prediction is only as strong as the weakest link.
   - If variation is absent, no change. If h² is unmeasured, the direction is known but not the rate. If selection intensity is environment-dependent (e.g., harsh winter, abundant food), the magnitude is uncertain.

7. **Check boundary conditions** (below). If any apply, flag limitations on the prediction.

## Boundary Conditions

Natural Selection predicts trait frequency change in populations with heritable variation under consistent directional selection. It breaks down or requires supplementation when:

- **Heritability is zero or unmeasured.** If the trait is wholly environmental (e.g., scars, learned behavior) or if h² cannot be estimated, the model is inapplicable. Supplement with models of cultural or behavioral transmission if h² < 0.1.

- **Selection is weak relative to drift.** In very small populations (N_e < 50), random sampling of gametes (genetic drift) overwhelms weak selection, so trait frequencies change unpredictably. The model predicts direction but not probability of fixation.

- **Selection changes direction or magnitude across generations** (variable environment). If favorable conditions return only every 10 years, mean selection S is weak; if selection alternates (e.g., directional one decade, stabilizing the next), the long-term prediction requires integrating over the environment's cycle, not a single R.

- **Inbreeding or population bottlenecks occur.** These reduce effective population size and increase drift, also potentially increasing mutation load. The model's predictions become noisier.

- **Pleiotropy or linkage disequilibrium causes indirect selection.** A trait may have low direct selection but be genetically linked to a trait under strong selection. The focal trait then changes even if selection on it is weak or absent. Requires genetic mapping to predict accurately.

- **The trait affects mate choice (sexual selection).** If the trait itself determines who mates with whom (e.g., bright plumage in birds), evolution can accelerate or reverse independently of survival-based selection. Requires explicit sexual selection modeling.

- **Very long timescales (millions of years).** Speciation, extinction, and macroevolutionary processes become dominant. The model predicts change within a species but not speciation rates or large morphological transitions.

## Output Format

```
## Natural Selection Analysis: <population and trait>

**Population:** <species, geography, generation(s)>
**Trait:** <name, measurement unit, baseline mean and variance>
**Timescale:** <one generation, multiple generations, years>

### Variation and heritability
- Phenotypic variance (SD, range, or categorical frequency): <value>
- Heritability h²: <estimate, with source (pedigree, twin study, etc.)>
- Genetic basis: <known loci, or unknown>

### Reproduction by trait
| Trait value | Viability (survival to maturity) | Fecundity | Reproductive output |
|---|---|---|---|
| ... | ... | ... | ... |

### Selection differential
- Mean trait in reproducing cohort: <value>
- Mean trait in population (all): <value>
- Selection differential S (difference): <value>
- Direction of selection: <directional (positive/negative), stabilizing, disruptive, sexual>

### Prediction
- Predicted response R = h² · S: <value or qualitative>
- Mean trait in next generation: <value>
- Expected trajectory (stabilize, increase, decrease, fluctuate): <description>

### Boundary-condition check
<which of the boundary conditions apply; whether the prediction is robust or uncertain>

### Confidence: high | medium | low
<reasoning: heritability estimate quality + stability of selection + population size + generation count + whether any boundary conditions undermine the prediction>
```
