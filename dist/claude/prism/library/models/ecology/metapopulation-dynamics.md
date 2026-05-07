---
name: metapopulation-dynamics
display_name: Metapopulation Dynamics (Levins)
class: model
underlying_class: native
domain: ecology
source: Richard Levins, "Some Demographic and Genetic Consequences of Environmental Heterogeneity for Biological Control," Bulletin of the Entomological Society of America, 1969
best_for:
  - Predicting persistence or extinction of species in fragmented habitats
  - Understanding how patch connectivity and extinction rates interact to determine regional survival
  - Evaluating conservation strategies that trade off habitat area against patch isolation
one_liner: "In fragmented habitat, the balance of local extinction and recolonization drives persistence of the whole species."
---

# Metapopulation Dynamics (Levins)

## Overview

Levins' metapopulation model claims that **a fragmented population persists not through high survival in any single patch, but through a dynamic balance between local extinction and recolonization across the patch network**. The model predicts that even if patches are small and local populations are short-lived, the species survives at the regional level if patches are sufficiently abundant and well-connected. The core intuition is that rapid turnover within patches is tolerable if immigration from occupied patches refills empty ones fast enough. The model is predictive — it generates equilibrium extinction risk as a function of landscape structure (patch number, isolation) and species traits (colonization ability, local extinction rate). It applies when populations are fragmented into discrete patches with limited dispersal between them.

## Core Variables and Relationships

The metapopulation state is tracked by **p(t)**, the fraction of patches occupied at time t. The rate of change in occupancy is governed by two opposing flows:

1. **Colonization rate (immigration)** — patches become occupied.
   - Proportion of occupied patches p(t) at time t
   - Proportion of unoccupied patches (1 − p(t))
   - Colonization ability per occupied patch (rate c, assumed constant per occupied patch in simple form)
   - Patch isolation / connectivity (higher isolation → lower effective colonization rate)
   - **Direction:** Higher p and higher connectivity increase colonization flow.

2. **Extinction rate (local loss)** — occupied patches lose their population.
   - Local population size within a patch (smaller patches → higher extinction probability)
   - Temporal stochasticity and local environmental variance
   - Species intrinsic extinction risk (baseline for the species, e.g., reproductive variance)
   - **Direction:** Larger patches and less variable environments reduce extinction rate.

The **core equation** (simplified, assuming homogeneous patches):

    dp/dt = c · p · (1 − p) − e · p

where:
- **c · p · (1 − p)** is colonization (colonization rate × occupied patches × unoccupied patches)
- **e · p** is extinction (extinction rate × currently occupied patches)

The model reaches **equilibrium occupancy p\*** when dp/dt = 0:

    p* = 1 − (e / c)

This equation reveals the central prediction: **occupancy depends only on the ratio e/c, not on absolute patch number or area.** If c > e, the metapopulation persists (p\* > 0); if e ≥ c, it goes extinct (p\* ≤ 0).

## Key Predictions

- **Threshold for persistence:** A metapopulation persists if and only if the colonization rate c exceeds the extinction rate e. Below this threshold, the network-scale extinction is inevitable, regardless of patch restoration efforts that do not increase c relative to e.

- **Occupancy at equilibrium p\* = 1 − (e/c) depends only on the ratio, not on patch number or total area.** A landscape with 100 large patches has the same predicted equilibrium occupancy as one with 10,000 small patches *if the colonization and extinction rates are identical*. This counterintuitive prediction—that raw habitat area is not a direct predictor—is one of the model's defining insights.

- **Connectivity matters more than patch size when the ratio e/c is near the extinction threshold.** If extinction is driven by demographic stochasticity in small patches, increasing patch isolation (reducing c) destabilizes the metapopulation faster than increasing local extinction risk alone.

- **Rescue effect:** Patches that would otherwise go extinct are "rescued" by immigration from occupied patches. The strength of rescue depends on the immigration rate and the number of occupied source patches; high c relative to e makes the metapopulation resistant to localized disturbance.

- **Lag-time extinction:** If connectivity or colonization ability declines suddenly (e.g., habitat fragmentation), the metapopulation does not immediately collapse. Occupancy decays exponentially toward the new equilibrium; during the lag phase, patches remain occupied even though the system is no longer at equilibrium. This predicts a window in which conservation intervention can be effective.

- **Amplified sensitivity near the critical threshold e = c:** Small changes in colonization ability or extinction rate near p\* ≈ 0.5 produce large changes in occupancy; the system is unstable and can flip from persistence to extinction with slight parameter shifts.

## Application Procedure

Instantiate the model against a concrete fragmented population or habitat system.

1. **Define the spatial and temporal scope.** What is the species or population? What is the geographic region? What is the time horizon over which you are predicting (years, decades)? Write it in one sentence. Clarify the boundaries of "patches" — are they distinct habitat fragments, subpopulations, or breeding colonies?

2. **Identify occupied and unoccupied patches.** Count or estimate the number of habitat patches and the fraction currently occupied p(t). If exact count is infeasible, estimate from survey data or expert judgment.

3. **Estimate or infer the extinction rate e.** This is the rate at which an occupied patch loses its population.
   - Use local population time-series data if available (how many patches turned over empty in a fixed period?).
   - Alternatively, infer from patch size: smaller patches → higher e. Use rules of thumb from the literature (e.g., extinction probability per unit time as a function of patch area: e ~ A^−z, where z ≈ 0.1–0.3 for many taxa).
   - Account for temporal variance and environmental stochasticity; e is always positive.

4. **Estimate or infer the colonization rate c.** This is the rate at which an occupied patch successfully colonizes an unoccupied patch per unit occupancy.
   - Use dispersal data (how far does the species travel?), landscape connectivity indices (habitat availability within dispersal range), and recolonization records (how fast does an empty patch fill after nearby reoccupancy?).
   - Alternatively, calibrate from observed occupancy changes: if you have p(t) data over time, infer c and e by fitting the differential equation.
   - c is reduced by patch isolation; connectivity indices (like the incidence function J) can modify c.

5. **Compute the equilibrium occupancy p\* = 1 − (e/c).** If e/c > 1, predict extinction (p\* ≤ 0). If e/c < 1, predict persistence at the fractional occupancy p\*.

6. **Identify which parameter (c or e) is the bottleneck.** Is the metapopulation near the extinction threshold because extinction is very high, or because colonization is very limited? This determines which conservation lever (reduce fragmentation / increase connectivity vs. increase patch quality / reduce local extinction) is most effective.

7. **Check boundary conditions** (below). If any apply, note that the simple Levins model is incomplete and flag complementary analysis.

8. **Generate the prediction:** Given the estimated parameters, will the metapopulation persist or go extinct over the time horizon? If persisting, what is the expected regional occupancy?

## Boundary Conditions

The Levins metapopulation model assumes **identical homogeneous patches**, **linear colonization and extinction dynamics**, and **no internal population structure within patches**. It breaks down when:

- **Patches are highly heterogeneous in size, quality, or isolation.** The model treats all patches identically; if source patches are much larger or better-connected than sink patches, the actual occupancy and persistence can deviate significantly from p\*. Supplement with a spatial analysis or a source-sink model (Pulliam).

- **Colonization or extinction dynamics are nonlinear or density-dependent.** Real populations have Allee effects (mating failure at low density), demographic stochasticity that depends on local patch size, and immigration that saturates or is blocked by distance thresholds. Levins' linear model may overpredict persistence in very small or very isolated patches.

- **Spatial autocorrelation is strong** (all patches are in one cluster, or extinction/colonization events are spatially correlated). The model assumes events in one patch are independent; if a disturbance (e.g., fire, disease, environmental stress) affects multiple patches simultaneously, the effective e and c are confounded, invalidating the simple rate estimates.

- **The species has complex life history** (long-lived organisms with overlapping generations, seed banks, dormancy). The model treats occupancy as a binary (occupied / empty) state; it does not track population structure within patches or age-stage dynamics. Use a structured metapopulation model (e.g., matrix models) if age or stage is critical.

- **Evolutionary rescue or rapid adaptation occurs.** The model assumes c and e are fixed; if dispersal ability or extinction risk evolves quickly (e.g., over 10–20 generations in a fast-reproducing species), the parameters shift and the prediction becomes outdated.

- **External forcing or stochasticity is extreme.** The model predicts long-term equilibrium; if the system experiences rare catastrophic events, rapid climate shifts, or habitat loss during the planning horizon, the equilibrium assumption is violated and a transient or stochastic analysis is needed.

## Output Format

```
## Metapopulation Persistence Analysis: <species, region>

**System:** <one sentence: species, geographic extent, patch definition, time horizon>
**Patches:** <total number, current occupancy p(t), geographic distribution notes>

### Parameter estimates
| Parameter | Estimate | Data source / method | Uncertainty |
|---|---|---|---|
| Extinction rate e | <per patch per year> | <survey / literature / inferred from area> | <high / medium / low> |
| Colonization rate c | <per occupied patch per year> | <dispersal / connectivity data / recolonization records> | <high / medium / low> |
| Patch connectivity | <isolated / moderate / well-connected> | <geographic analysis / dispersal range vs. inter-patch distance> | ... |

### Equilibrium prediction
- **e/c ratio:** <value>
- **Equilibrium occupancy p\*:** <value or range>
- **Persistence threshold:** <metapopulation will persist (e < c) / is at risk (e ≈ c) / will go extinct (e > c)>

### Critical bottleneck
<Is extinction rate too high, or colonization rate too low? Which conservation lever is most important?>

### Transient dynamics
- **Current state vs. equilibrium:** <is the system oversaturated, undersaturated, or at equilibrium?>
- **Time to equilibrium:** <approximate lag time to reach p\* at current trajectory>
- **Lag-time extinction risk:** <is there a window for intervention before obligate local extinctions accumulate?>

### Conservation implications
- To increase p\*, should we prioritize: <connectivity (increase c) / patch quality or size (decrease e) / increase total patch number / restore dispersal corridors>
- Estimated change in p\* if c increases by X% or e decreases by Y%

### Boundary-condition check
<Which assumptions (homogeneous patches, linear dynamics, independence, constant parameters) are violated? What complementary analysis is needed?>

### Confidence: high | medium | low
<Reasoning: quality of e and c estimates + landscape homogeneity + fit to Levins assumptions + time horizon relative to generation time>
```
---
