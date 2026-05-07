---
name: niche-analysis
display_name: Niche Analysis
class: frame
underlying_class: native
domain: ecology
source: G. Evelyn Hutchinson, Yale University, 1957 ("Concluding Remarks")
best_for:
  - Distinguishing between the theoretical space of resources available to an organism and the actual subset it occupies
  - Predicting whether a species' range is limited by environment, competition, or realized behavior
  - Understanding why a population may persist in a subset of seemingly suitable habitat
one_liner: "Distinguish the fundamental (possible) niche from the realized (occupied) niche."
---

# Niche Analysis

## Overview

Niche Analysis sorts the habitat or resource space available to an organism
into two conceptually distinct categories: **fundamental niche** (the full
range of conditions and resources where an organism could theoretically
survive and reproduce) and **realized niche** (the actual subset it occupies
in practice). The core claim is that the difference between these two is
**not random** — it reveals the primary limiting factor: abiotic constraint,
interspecific competition, predation, or behavioral choice. Recognizing which
mechanism explains the gap changes what field observations to collect and
what interventions are ecologically sound.

## Categories

1. **Fundamental Niche**
   - The **theoretical maximum extent** of habitat space — defined by
     physiological tolerances, metabolic requirements, and food-web
     prerequisites alone.
   - Estimated by laboratory experiments, comparative physiology, and
     absence of observed interspecific competitors or predators.
   - Discriminating criterion: the organism can survive and complete its
     lifecycle under these conditions when isolated or removed from
     competing/predating species.
   - Example: a fish species survives in laboratory tanks across a pH range
     of 5.5–8.0 and temperatures 10–28°C; these bounds define its
     fundamental niche for those axes.

2. **Realized Niche**
   - The **actual subset of habitat space** the organism occupies in nature,
     observed through field survey, occupancy mapping, and resource-use
     telemetry.
   - Constrained by the fundamental niche *plus* all biotic and behavioral
     factors: competition, predation, parasitism, dispersal limitation,
     and microhabitat preference.
   - Discriminating criterion: the organism is observed or sampled within
     these bounds; outside them, it is absent even if the abiotic
     conditions fall within its tolerance range.
   - Example: the same fish species occupies only pH 6.5–7.5 and 15–22°C in
     the river, where it competes with a congener that dominates the
     extremes and avoids shallow, predator-rich zones.

## Classification Procedure

1. **Define the environmental axis or resource category** in question (e.g.,
   temperature, pH, food type, vertical strata, time-of-activity).

2. **Determine the fundamental niche bounds** for that axis:
   - Consult published physiological tolerance data, or
   - Run or review laboratory experiments on the species in isolation, or
   - Infer from phylogenetic context (sister species' ranges often bound
     tolerance).
   - Record the upper and lower limits.

3. **Map the realized niche** for the same axis:
   - Conduct field surveys (net samples, transects, occupancy records) in
     the region where the species is believed to occur.
   - Record all locations where the species is observed and all where it is
     absent but conditions fall within the fundamental range.
   - Plot the observed distribution against the environmental axis.

4. **Compare realized to fundamental:**
   - If realized ≈ fundamental, the species is **abiotic-limited** (the
     environment is the primary constraint).
   - If realized ≪ fundamental, the gap is explained by competition,
     predation, dispersal, or behavior; proceed to step 5.

5. **Diagnose the limiting factor** for the gap (optional but informative):
   - **Competition:** Introduce a competitor to an unused portion of the
     fundamental niche and observe whether the species retreats or
     partitions the resource.
   - **Predation:** Remove the predator and observe niche expansion.
   - **Dispersal:** Check for propagules (larvae, seeds, migrants) arriving
     in unoccupied suitable habitat; absence suggests the barrier is
     dispersal, not environment or interaction.
   - **Behavioral avoidance:** Observe movement and habitat selection; if
     the species avoids suitable habitat for non-obvious reasons, behavior
     may be the primary constraint.

6. **Classify and document** which niche (fundamental, realized) is in
   question and what the primary limiting mechanism is.

## Implications per Category

| Niche type | What it reveals | Ecological implication | Management response |
|---|---|---|---|
| **Fundamental ≈ Realized** | The environment is the primary constraint. | The species is close to its physiological limits; further range expansion requires conditions to change. | Monitor climate/water chemistry; predict vulnerability to abiotic shift. |
| **Realized ≪ Fundamental (competition)** | A competitor is excluding the species from otherwise suitable habitat. | The species is competitively subordinate on that axis. | Remove or control the competitor; or restore the species to a refuge niche. |
| **Realized ≪ Fundamental (predation)** | A predator or parasite limits the species' expansion into suitable habitat. | The species exists in a predation-risk balance. | Reduce predator pressure; or restore predator-sparse refugia. |
| **Realized ≪ Fundamental (dispersal)** | The species has not reached all suitable habitat. | The species is dispersal-limited; it could expand if barriers (geographic, connectivity) are removed. | Create dispersal corridors; translocate individuals to suitable unoccupied habitat; restore stepping-stone habitat. |
| **Realized ≪ Fundamental (behavior)** | The species avoids suitable habitat for reasons not explained by competition or predation. | The species may have culturally mediated or learned habitat preference; rapid evolution may be possible. | Investigate preference mechanisms; consider soft reintroduction to restore lost preferences. |

The practical implication is that **knowing which category applies determines
what data to collect and what conservation or restoration action is
ecologically justified**. Restoring a competitively displaced species without
removing or managing the competitor is futile; expanding habitat without
addressing a dispersal barrier is wasted effort.

## Common Misclassifications

- **Confusing realized with fundamental under incomplete sampling.** A
  species appears absent from suitable habitat because the survey was
  underpowered or timed poorly (wrong season, wrong time of day). The tell
  is that intensive re-sampling or occupancy modeling shows the species
  present; the niche was not actually contracted, just unobserved. Solution:
  pilot the survey design before concluding the realized niche is truly
  smaller.

- **Assuming realized niche = occupied habitat.** A species may be present
  but in low density or temporary use; absence of active breeding or
  permanent settlement in a habitat indicates a realized niche boundary even
  if the organism is occasionally detected. The tell is that the species
  does not sustain a population in that habitat without recolonization from
  outside.

- **Mistaking a shifted fundamental niche (due to local adaptation) for
  realized niche contraction.** A population may have evolved narrower
  tolerance in response to strong selection, making its fundamental niche
  smaller than the species-wide estimate. The tell is that transplant
  experiments show poor survival relative to published tolerance ranges,
  and genetic structure explains the difference. Solution: distinguish
  genotype-specific tolerance from environmental constraint.

- **Attributing realized niche contraction to abiotic limits when the
  mechanism is biotic.** A species absent from the thermal optimum is often
  assumed to be thermally limited; closer inspection reveals a competitor
  dominates that zone. The tell is that the species can survive those
  temperatures in lab or when the competitor is absent. Solution: remove the
  competitor experimentally and re-assess occupancy.

- **Ignoring temporal variation in realized niche.** A species' realized
  niche can contract and expand seasonally, annually (dry/wet years), or
  over decadal cycles. Classifying based on a single snapshot or year is
  misleading. The tell is that occupancy surveys in different years or
  seasons reveal different boundaries. Solution: repeat surveys across
  multiple years and seasons before concluding niche shape is stable.
