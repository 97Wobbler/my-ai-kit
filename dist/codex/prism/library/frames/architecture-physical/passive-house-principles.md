---
name: passive-house-principles
display_name: Passive House Principles
class: frame
underlying_class: native
domain: architecture-physical
source: Bo Adamson and Rolf Feist, Thermal Technology Institute / Swedish University of Lund, 1988
best_for:
  - Classifying building design and envelope performance against Passive House certification criteria
  - Determining which thermal and air-tightness strategies are load-bearing vs. decorative
one_liner: "Building standard requiring almost no heating via airtightness, insulation, heat recovery, and rigorous calculation."
---

# Passive House Principles

## Overview

Passive House (Passivhaus) is a performance-based frame that sorts building design strategies and envelope attributes into categories based on their **necessity and sufficiency for achieving sub-5 kWh/m²/year heating demand**. Its core claim is that different thermal and air-tightness interventions are **not equally load-bearing**: some are mandatory prerequisites, others are secondary optimizations, and some are decorative if the core four principles are met. Sorting a strategy into the right category prevents two systematic errors: over-engineering non-critical details while under-specifying critical ones, and mistaking incremental improvements for fundamental shifts in energy behavior.

## Categories

1. **Airtightness (Air Sealing)**
   - The building envelope must achieve **≤0.6 air changes per hour at 50 Pa pressure** (n₅₀ ≤ 0.6).
   - Absence of airtightness undermines all other strategies through uncontrolled infiltration.
   - Discriminating criterion: airtightness cannot be compensated by insulation or recovery; it is a strict pass/fail threshold below which the other three principles cannot deliver the target.
   - Example: sealing around electrical outlets, window frames, roof-wall junctions with careful detailing and tape; third-party blower-door testing to verify.

2. **Insulation (Thermal Envelope)**
   - The building envelope must provide **U-values ≤0.15 W/m²K** on walls, roofs, and foundations (typical thickness 200–400 mm depending on climate and material).
   - Sufficient insulation reduces the rate of heat loss; without it, no recovery strategy can offset the load.
   - Discriminating criterion: insulation level is sized by heating degree-days and acceptable indoor–outdoor temperature differential; undersizing insulation forces unrealistic recovery equipment or heating load.
   - Example: continuous exterior insulation on all opaque surfaces, triple-glazed windows (U ≤ 0.8 W/m²K), thermal breaks in all penetrations.

3. **Heat Recovery (Ventilation System)**
   - A **controlled mechanical ventilation system with heat recovery efficiency ≥75–80%** is required to capture warmth from exhaust air and pre-heat supply air.
   - Without recovery, ventilating a well-sealed house loses heat; without sealing, ventilation cannot be controlled.
   - Discriminating criterion: heat recovery is only effective in a sealed envelope; it presupposes airtightness and works *with* insulation, not instead of it.
   - Example: ERV (energy recovery ventilator) with enthalpy core, crossflow plate heat exchanger, ducted supply and exhaust paths.

4. **Thermal Bridge Avoidance**
   - **All structural and penetration thermal bridges must be minimized** (linear transmittance ψ ≤ 0.01 W/mK); avoidable bridges must be eliminated.
   - Thermal bridges are localized high-conductivity paths that create cold spots, condensation risk, and heat loss disproportionate to their area.
   - Discriminating criterion: the presence of unaddressed thermal bridges (e.g., uninsulated cantilevers, metal studs bridging the envelope) defeats the benefit of high-level envelope insulation by creating fail points.
   - Example: fully insulated balcony connections, continuous exterior insulation wrapping structural columns, elimination of exposed concrete lintels.

5. **Design Verification (Computational Modeling)**
   - The design must be **modeled and verified** using standardized tools (PHPP — Passive House Planning Package, or equivalent) to confirm the heating demand ≤5 kWh/m²/year and domestic hot water ≤2 kWh/m²/year.
   - Design without verified calculation is speculation; the four physical principles above are necessary but not sufficient without proof.
   - Discriminating criterion: if modeled demand exceeds 5 kWh/m²/year, the design does not qualify; the calculation step is the gate, not the physical strategies.
   - Example: PHPP input of geometry, U-values, airtightness target, window orientation, occupancy, ventilation strategy; output identifies which strategy is undersized.

## Classification Procedure

1. Identify the element or strategy under review: Is it a physical intervention (window, insulation layer, air seal) or a performance attribute (modeled heating load)?
2. Ask **"Is this a mandatory threshold or an optimization?"**
   - If the answer is "it must be below/above a specific number to qualify," go to step 3.
   - If the answer is "it improves performance but the design can work without it," it is **decorative** (not a Passive House Principle).
3. Ask **"Does this strategy depend on one or more of the other four principles to work?"**
   - If **yes**, identify which ones — it is either Heat Recovery (depends on Airtightness and Insulation), Thermal Bridge Avoidance (improves all three), or Design Verification (gate for all).
   - If **no**, it is likely Airtightness or Insulation (foundational).
4. Cross-check against the PHPP model: if the element is sized or credited in the standard calculation, it is one of the five. If it is not, it is decorative.
5. State the category and note its relationship to the others: **"This is a [Category]; it is [mandatory threshold / optimization] and [depends on / independent of] [other categories]."**

## Implications per Category

| Category | Role | What the designer must do |
|---|---|---|
| **Airtightness** | Foundational gate | Achieve ≤0.6 n₅₀ through continuous detail, third-party blower-door testing. Non-negotiable; all other strategies fail without it. |
| **Insulation** | Load-bearing | Size by climate and modeling; typical U ≤ 0.15 W/m²K opaque, ≤ 0.8 W/m²K windows. Undersizing forces unrealistic ventilation recovery or heating. |
| **Heat Recovery** | Essential complement | Install ERV/HRV sized to ventilation flow; depends on Airtightness to control air path. Provides 60–80% of heating in cold climates. |
| **Thermal Bridges** | Verification lever | Identify and eliminate or minimize all bridges; unaddressed bridges create cold spots and defeat insulation investment. |
| **Design Verification** | Proof gate | Model every design iteration in PHPP or equivalent; if calculated demand > 5 kWh/m²/year, the design fails, regardless of on-site quality. |

Implicit sequencing rule: **Verify design in PHPP first (step 5), then specify Airtightness (step 1), then Insulation (step 2) sized by the model, then eliminate Thermal Bridges (step 4), then select Heat Recovery (step 3) sized by ventilation need and heating load residual.**

## Common Misclassifications

- **Treating Insulation as Airtightness.** Specifying very high R-value insulation while ignoring air sealing. The tell is that blower-door testing fails despite thick insulation; insulation does not prevent infiltration.
- **Installing Heat Recovery without Airtightness.** An ERV in a leaky house delivers minimal benefit — much of the supply air leaks out, uncontrolled. The tell is that ventilation noise and draft complaints arise because air is not controlled.
- **Ignoring Thermal Bridges as "minor."** A single exposed concrete lintel or uninsulated cantilconnection can reduce overall envelope performance by 10–15% and create a cold-condensation failure point. The tell is mold at a specific junction year after year.
- **Skipping Design Verification or relying on intuition.** A design that "looks efficient" may fail modeling because of window area, orientation, or ventilation sizing. The tell is on-site heating demand much higher than the designer expected.
- **Confusing "efficient" insulation (decorative add-ons) with Passive House Principles.** Extra cork panels or specialized "energy-saving" coatings outside the five categories do not move the needle if the core five are mis-specified. The tell is the PHPP model unchanged despite the add-on cost.
