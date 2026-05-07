---
name: island-biogeography
display_name: Island Biogeography
class: model
underlying_class: native
domain: ecology
source: Robert H. MacArthur & Edward O. Wilson, "An Equilibrium Theory of Insular Zoogeography," Evolution, 1963; extended in The Theory of Island Biogeography (1967)
best_for:
  - Predicting species richness on islands as a function of area and isolation
  - Understanding colonization-extinction dynamics in fragmented habitats
  - Explaining why larger, closer islands harbor more species
one_liner: "Island size and distance set the equilibrium point of species diversity."
---

# Island Biogeography

## Overview

The Island Biogeography model claims that the number of species on an island
is determined by a **dynamic equilibrium between colonization and extinction
rates**, both of which are predictable functions of island area and isolation
from the mainland (or source pool). The model is predictive: given an island's
size and distance from the source, one can estimate the steady-state species
count without invoking historical accident or dispersal capability. The
central insight is that large islands near the mainland will reach
equilibrium at higher species richness than small islands far away because
they enjoy high colonization rates and low extinction rates; the reverse is
true for small, distant islands. The model is descriptive of the forces
at play, and its application lets an ecologist read off the equilibrium
species number for any island in a given taxon.

## Core Variables and Relationships

The model rests on two core rate functions and one equilibrium concept:

1. **Colonization rate C(S)** — the rate at which new species arrive at the
   island as a function of the number of species already present:
   - Decreases with S (as S increases, fewer mainland species remain
     unrepresented on the island; fewer arrivals are "new").
   - Increases with **island area A** (larger islands intercept more
     colonists from the mainland dispersal stream).
   - Increases with **proximity to mainland** / decreases with distance D
     (shorter distance = higher arrival rate of propagules; isolation
     reduces colonization rate steeply, often ~exponentially with D).
   - At S = 0 (empty island), C is at its maximum; C approaches 0 as S
     approaches the mainland species pool.

2. **Extinction rate E(S)** — the rate at which species disappear from the
   island as a function of the number of species present:
   - Increases with S (more species → higher chance that some will go
     extinct; this is sometimes called the "stochastic extinction" effect,
     though the model allows both stochastic and deterministic mechanisms).
   - Decreases with **island area A** (larger islands support larger
     populations; smaller populations are more vulnerable to random
     environmental fluctuations and demographic drift).
   - Relatively independent of distance D (distance affects arrival, not
     survival once present).
   - At S = 0, E = 0 (no species to go extinct); E increases roughly
     linearly (or sublinearly) with S for typical taxa.

3. **Equilibrium species number S\*:**
   The model predicts that colonization and extinction rates will intersect at
   an equilibrium. At S\*, arrivals = departures, and the island maintains a
   stable species count. This equilibrium is:
   - **Higher on large islands** (because large islands have lower extinction
     rates; the E(S) curve shifts downward).
   - **Higher on islands near the mainland** (because near islands have higher
     colonization rates; the C(S) curve shifts rightward).
   - **Lower on small, distant islands** (because both C is low and E is high).

   The relationship is often expressed as:
   ```
   S* ∝ A^z · exp(−kD)
   ```
   where z ≈ 0.2–0.35 (the "species-area exponent") and k is a distance
   decay constant. Doubling island area increases equilibrium species by ~15–25%;
   doubling distance may halve the colonization rate, shifting S\* downward
   significantly.

## Key Predictions

- **Larger islands harbor more species** at equilibrium, all else equal.
  The effect is sublinear: doubling area does not double species count, but
  increases it by a measurable fraction. This gives rise to the canonical
  "species-area curve," observed across taxa (birds, insects, plants) and
  geographies (Caribbean islands, Pacific atolls, habitat fragments).

- **Isolated islands harbor fewer species** than nearby islands of the same
  area. The effect of distance is often steeper than area: moving an island
  from 100 km to 1,000 km from the mainland may reduce S\* by 50% or more,
  whereas the same relative change in area (10×) reduces it by ~30%.

- **Species turnover (beta diversity) is higher on small, distant islands**
  because both colonization and extinction rates are high in absolute terms.
  A small island far from the mainland is a "revolving door" — species arrive
  and disappear rapidly, but the count fluctuates around a lower mean. Large,
  near islands have high immigration (high absolute C) and low extinction
  (low absolute E), so the standing stock is stable and large.

- **Species composition on islands is not deterministic** — the model predicts
  *number*, not *which* species. Two islands of the same area and distance
  will reach the same S\* but may contain different species, depending on
  stochastic arrival order (the "assembly history"). This is a non-obvious
  prediction that challenges a purely deterministic view of ecology.

- **Habitat area loss in fragmented ecosystems mimics island isolation.** A
  mainland patch of forest surrounded by cleared land behaves like an island.
  The model predicts that reducing patch area will lower the equilibrium
  species count and increase turnover, independent of how the forest was
  cleared. This is a major application to conservation biology.

- **Adding area to an island yields diminishing returns in species gain**, due
  to the sublinear exponent. The first doubling of area yields more new
  species than the second doubling. This has practical implications for
  reserve design: a single large reserve captures more species than multiple
  small reserves of the same total area (the SLOSS debate).

## Application Procedure

Instantiate the model against a concrete island, archipelago, or fragmented
habitat system.

1. **Define the island(s) and source pool.** What is the island or habitat
   patch? What is the geographic "mainland" or source of colonists (e.g.,
   adjacent forest, river network, regional pool)? Define the taxon of
   interest (birds, small mammals, plants, insects, etc.).

2. **Measure or estimate island area A and distance D** (or isolation metric,
   e.g., connectivity to nearest source). Area in km²; distance in km to the
   nearest point on the mainland or largest island in the archipelago.

3. **Obtain (or infer) the species-area exponent z and distance-decay
   constant k** from the literature for your taxon and region. These are
   empirically fitted to local or regional data. For birds in the Caribbean,
   z ≈ 0.24; for insects, z ≈ 0.30. k varies widely (0.01–0.1 per km,
   depending on dispersal ability).

4. **Estimate the regional species pool size** P (the number of species
   in the source area, or the largest nearby island). This sets the
   ceiling — S\* ≤ P.

5. **Calculate predicted S\*** using the power-law relationship:
   ```
   S* = c · A^z · exp(−kD)
   ```
   where c is a fitted constant from regional data. Alternatively, estimate
   S\* graphically by plotting C(S) and E(S) curves and finding their
   intersection. The qualitative result (large + near = high S; small + far =
   low S) requires no fitting — it is the model's core claim.

6. **Observe the actual species count S_obs** on the island.

7. **Compare S\* to S_obs.** Is the island below, at, or above equilibrium?
   - If S_obs < S\*, the island is undersaturated (likely because it was
     recently isolated, or colonization is slow). Prediction: species will
     accumulate over time.
   - If S_obs ≈ S\*, the island is at equilibrium (steady state).
   - If S_obs > S\*, the island is oversaturated (rare; suggests either the
     model's assumptions are violated, or S_obs includes recently extinct
     species not yet removed from the biota).

8. **Check boundary conditions** (below). If any apply strongly, flag that
   the prediction may be qualitatively correct but quantitatively off.

## Boundary Conditions

The Island Biogeography model applies best to **real islands or habitat
islands in a relatively stable region over timescales of centuries to low
thousands of years**. It breaks down or becomes incomplete under several
conditions:

- **Very recent isolation or recolonization.** The model assumes species
  counts have had time to reach equilibrium (often 1,000–10,000 years for
  birds and mammals). Islands that were underwater until 100 years ago
  (e.g., new volcanic islands) are far below equilibrium; the model's
  prediction for S\* is correct, but the trajectory to reach it may be slow
  and path-dependent. Use the model to predict the *eventual* state, not
  the current one.

- **Habitat heterogeneity and niche structure.** The model treats area as
  a proxy for resource diversity and carrying capacity, but does not
  explicitly account for habitat type. An island with diverse habitats
  (forest + wetland + rocky shore) may exceed predictions based on area
  alone. Conversely, a large homogeneous island (monoculture sand, uniform
  grassland) may fall short. Supplement with explicit habitat-diversity
  metrics if heterogeneity is high.

- **Endemism and in-situ speciation.** The model assumes all species come
  from the mainland source pool. Islands with high endemism (species found
  nowhere else, evolved on the island itself) violate this assumption. The
  equilibrium number will be higher than the model predicts if speciation
  has occurred. Very old, large islands (e.g., Madagascar, Hawaiian
  Islands) are driven as much by *in situ* evolution as by colonization-
  extinction balance; the simple MacArthur-Wilson model is descriptive but
  incomplete.

- **Trophic structure and interaction effects.** The model treats extinction
  as a species-level rate independent of community composition. In reality,
  the loss of a keystone predator or pollinator may trigger cascades. The
  model does not capture these second-order effects; it predicts number, not
  composition or stability.

- **Anthropogenic disturbance and non-equilibrium dynamics.** Modern islands
  are often subject to rapid environmental change (climate, invasive species,
  direct habitat loss). These can shift the location of equilibrium faster
  than the biota can respond. The model is less useful in predicting transient
  dynamics during rapid change.

- **Dispersal limitation for very poor dispersers.** The model implicitly
  assumes colonization is determined by area and distance alone. For
  organisms with extremely limited dispersal (flightless insects, small
  mammals with no over-water capacity), even "nearby" islands may be
  unreachable, and the model predicts higher S\* than is ever realized.
  Distance decay k may be much steeper than the literature average.

## Output Format

```
## Island Biogeography Analysis: <island or system name>

**Island(s):** <name(s)>
**Taxon:** <birds, small mammals, plants, insects, etc.>
**Area A:** <km²>
**Distance D:** <km from mainland / source>
**Regional species pool P:** <estimated count>

### Model parameters
| Parameter | Value | Source / note |
|---|---|---|
| Species-area exponent z | <0.2–0.35> | <literature or fit> |
| Distance-decay constant k | <per km> | <literature or fit> |
| Fitted constant c | <from data> | <regional study> |

### Predicted vs. observed
| Metric | Value |
|---|---|
| S* (predicted equilibrium) | <species count> |
| S_obs (observed) | <species count> |
| Saturation status | <undersaturated / equilibrium / oversaturated> |

### Interpretation
- **Large-area effect:** <area contribution to S\*>
- **Distance effect:** <isolation contribution to S\*>
- **Dominant factor:** <which of area or distance more strongly limits S\*>
- **Turnover expectation:** <high / moderate / low, with reasoning>

### Trajectory prediction
- If undersaturated: <expected accumulation path and timescale>
- If at equilibrium: <stability and species composition fluidity>

### Boundary-condition check
<which boundary conditions apply (recent isolation, endemism,
anthropogenic disturbance, etc.) and whether the prediction is robust
to those conditions>

### Confidence: high | medium | low
<reasoning: availability of local z and k estimates + age of island +
habitat homogeneity + presence of significant endemism or in-situ
speciation + data quality on current species count>
```
```
