---
name: source-sink-dynamics
display_name: Source-Sink Dynamics
class: model
underlying_class: native
domain: ecology
source: Levins, R., "Extinction," in Some Mathematical Questions in Biology, Lectures on Mathematics in the Life Sciences (1970); developed further by Hanski & Gilpin, "Metapopulation Dynamics: Brief History and Conceptual Domain," Biological Journal of the Linnean Society (1991)
best_for:
  - Predicting persistence and range shifts of species across fragmented habitat
  - Explaining why some populations collapse despite apparent refuge habitat
  - Designing reserve networks and connectivity corridors
one_liner: "Regional population dynamics and extinction risk driven by movement between source and sink habitats."
---

# Source-Sink Dynamics

## Overview

Source-Sink Dynamics models how populations persist across a landscape of
heterogeneous habitat patches, and predicts which patches sustain
populations (sources) versus where populations cannot maintain themselves
(sinks) and depend on continuous immigration. The model's central claim is
that a species' long-term survival is not determined by average habitat
quality alone, but by the **balance between birth/death rates within each
patch and movement flows between them**. A good-quality source patch can
sustain a sink patch indefinitely through emigration, but loss of that
source patch causes the sink to collapse regardless of its intrinsic
habitat quality. The model is predictive: it explains why reserves on
paper often fail in practice, and why habitat connectivity is as
load-bearing as habitat area. To apply it, use the procedure below.

## Core Variables and Relationships

The model operates on two dynamics running in parallel:

1. **Patch-level population dynamics** — within each patch, births and deaths:
   - **λ (lambda) = finite rate of increase.** λ = births / deaths per
     generation. λ > 1 = source patch (population growing despite emigration).
     λ < 1 = sink patch (population declining, sustained only by immigration).
   - Drivers of λ per patch:
     - Habitat quality (food, nesting sites, predation risk, disease)
     - Breeding season length or productivity
     - Mortality rate (age-structure, density dependence)
     - Migration cost (individuals leaving vs. staying)

2. **Movement between patches** — emigrants follow a dispersal rule:
   - **m (per-capita emigration rate).** What fraction of individuals
     leave the patch per generation? Drivers:
     - Density in the source (high density → higher emigration)
     - Patch connectivity (distance, barriers, corridors)
     - Behavioral dispersal propensity (species-specific)
   - **Immigration success.** What fraction of emigrants survive and
     reproduce in a new patch? Drivers:
     - Patch carrying capacity (how many can it support?)
     - Allee effects (small populations have lower λ)
     - Establishment cost (first few immigrants often fail)

3. **Source vs. Sink identity** — determined by the combined outcome:
   - Patch i is a **source** if: λᵢ(1 − m) + immigration > 1
     (i.e., it maintains local growth even after emigration).
   - Patch i is a **sink** if: λᵢ(1 − m) + immigration < 1
     (i.e., it depends on immigration to avoid collapse).
   - The identity is **not intrinsic**; it depends on (λ, m, and flow).
     A patch with λ = 0.8 can be a source if it receives large inflow
     from a stronger source. Same patch becomes a sink if the source dries up.

4. **Network-level dynamics:**
   - **Metapopulation capacity C.** Broadly, C = Σ pᵢ · λᵢ over all patches,
     weighted by connectivity and size. The system persists long-term if
     C > 1; collapses if C < 1, regardless of individual patch λ values.
   - **Critical connectivity threshold.** Below some level of inter-patch
     movement, sinks become true sinks and the metapopulation fragments.
     Above it, sources can rescue sinks.

## Key Predictions

- **Habitat loss is non-linear in effect.** Losing a single large source
  patch can collapse a metapopulation even if 80% of habitat remains,
  because the sinks can no longer be rescued. Conversely, protecting one
  source patch can sustain many sinks.

- **Connectivity is as or more important than total area.** A landscape
  with 100 small disconnected patches (m ≈ 0) will lose more species
  than one with 10 larger connected patches (same total area, higher m).
  The effect compounds for species with low dispersal ability.

- **Range shifts under climate change are slower through sink-dependent
  ranges.** A species' range may lag climate by decades because sinks at
  the trailing edge are still supported by source immigration, and
  leading-edge colonization happens only if sinks at the front can
  convert to sources.

- **Protected-area networks fail if they contain only sinks.** A reserve
  system covering 30% of habitat can still lose a species if all reserves
  are sink-quality and the few remaining sources lie outside.

- **Sink-source reversal under perturbation.** A drought, logging, or
  invasive species that reduces λ in a keystone source can flip the
  entire system from stable to collapsing within a few generations, even
  if it affects only 5% of landscape area, because sinks become
  unsupported.

- **Species-specific threshold effects.** A species with very high
  dispersal ability (m large) is less sensitive to patch isolation but
  more sensitive to total source-patch area. A species with low dispersal
  (m small) is highly sensitive to isolation but can persist in very
  small reserves if located within source habitat.

## Application Procedure

Instantiate the model against a specific species and landscape.

1. **Define the system boundary.** What is the focal species? What is
   the geographic extent of the landscape? What is the generation time
   (or time step)? State this in one sentence.

2. **Identify and map habitat patches.** Enumerate patches in the
   landscape (forest fragments, wetlands, etc.). For each patch, estimate
   or infer:
   - **Habitat quality score** (qualitative or quantitative measure of
     suitability: resources, predation risk, climate match). Use literature
     or field surveys.
   - **Patch size** (area or carrying capacity K).
   - **Isolation distance** to nearest patches.

3. **Estimate λ (finite rate of increase) per patch.** For each patch:
   - If you have time-series count data: λ = geometric mean of Nₜ₊₁/Nₜ.
   - If you have demographic data (fecundity, survival): construct a
     projection matrix and extract the dominant eigenvalue.
   - If you have habitat covariates only (no count data): use a habitat-suitability
     model or published species relationships to estimate λ(quality).
   - Mark each patch as λ > 1 (potential source) or λ < 1 (potential sink).

4. **Estimate movement parameters m and immigration success.**
   - **Emigration rate m:** Use published dispersal studies for the species,
     or empirical distance-decay models (# individuals recovered by distance).
     If unavailable, use trait-based estimates (body size, wing morphology).
   - **Immigration success:** What fraction of emigrants survive to
     reproduce in a sink patch? This is often lower for rare or specialized
     species; higher for generalists.

5. **Compute source-sink status for each patch** by checking whether, at
   equilibrium, population in each patch grows, shrinks, or stabilizes.
   - A rough qualitative check: if λᵢ > 1 and patch is not isolated, mark
     as source. If λᵢ < 1 and immigration inflow is present, mark as sink.

6. **Identify the load-bearing sources.** Which patches, if lost, would
   flip the metapopulation from stable to declining? Usually 1–3 patches
   carry most of the metapopulation capacity.

7. **Read off predictions.**
   - Will the species persist under current conditions (C > 1 or C < 1)?
   - Which patches are most critical to protect?
   - What connectivity threshold would allow range expansion (e.g., through
     corridors)?
   - What habitat loss would be tolerable without causing collapse?

8. **Check boundary conditions** (below). If any apply, note that
   source-sink structure alone may not capture the full dynamics.

## Boundary Conditions

Source-Sink Dynamics assumes simple directional flow (source → sink) and
discrete generation time. It breaks down or becomes misleading when:

- **Overlapping generations and age-structure are complex.** If a species
  has long generation time, multiple reproductive ages, and size-dependent
  survival, the simple λ model underestimates the impact of losing
  reproductive females. Use a stage-structured or size-structured model
  instead.

- **Feedback dynamics dominate (Allee effects, mate-finding limitation).** In
  very small sink populations, Allee effects cause λ to collapse
  nonlinearly as population drops. The model assumes λ is patch-intrinsic
  and independent of current population size; this can fail for species
  with strong Allee effects.

- **Predator or disease dynamics create spatial heterogeneity in λ.** If
  sinks are sinks because of a mobile predator or epidemic that moves
  between patches, the λ values are not independent; they couple together.
  This requires a multi-species or disease-structured model.

- **Rescue effects saturate.** The model assumes immigration rates are
  proportional to source population size. If sink patches fill up or
  develop behavioral territoriality, further immigration cannot increase
  the population. The rescue effect saturates and sinks can collapse even
  with nearby sources.

- **Human-modified landscapes with frequent disturbance.** If the landscape
  turns over (repeated habitat loss and recovery) on a timescale
  comparable to or faster than metapopulation generation time, the model's
  equilibrium assumption breaks. Use a dynamic/stochastic framework instead.

- **Very long-distance rare dispersal events are essential.** Some species
  (certain birds, plants with wind-dispersed seed) have occasional
  long-distance colonization that rescues distant patches. If these rare
  events are load-bearing, standard movement models underestimate
  connectivity and the system appears more fragile than it is.

## Output Format

```
## Source-Sink Analysis: <species name, landscape>

**Focal species:** <name, generation time>
**System boundary:** <geographic extent, time horizon>
**Landscape structure:** <# patches, total habitat, fragmentation index>

### Patch inventory
| Patch | Size | Habitat quality | Estimated λ | Source/Sink | Isolation |
|---|---|---|---|---|---|
| ... | ... | ... | >1 / <1 | ... | ... |

### Key drivers per patch
- λ drivers: <main factors supporting or limiting growth>
- Movement: <estimated m per patch, distances to neighbors>
- Immigration inflow: <likely source patches and flow magnitude>

### Source-Sink diagnosis
- Load-bearing source patch(es): <which patch(es) and why>
- Dependent sink patch(es): <which patches depend on which sources>
- Metapopulation capacity C: >1 (stable) / <1 (declining) / uncertain

### Predictions
- Will the species persist under current conditions? <yes / no / uncertain>
- Critical conservation priorities: <which patches if lost cause collapse>
- Connectivity threshold for expansion: <distance, corridor width, etc.>
- Tolerable habitat loss before C < 1: <% or area>

### Boundary-condition check
<which boundary conditions apply and whether the source-sink diagnosis
remains valid; what complementary analysis (age structure, Allee effects,
disturbance dynamics) is needed>

### Confidence: high | medium | low
<reasoning: data quality (λ estimates, movement data) + landscape
stability + whether critical boundary conditions apply>
```
