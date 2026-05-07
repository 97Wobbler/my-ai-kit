---
name: life-cycle-assessment
display_name: Life Cycle Assessment
class: lens
underlying_class: native
domain: ecology
source: ISO 14040/14044 (International Organization for Standardization); origins in industrial ecology (1969–1990s)
best_for:
  - Quantifying total environmental cost of a product or service from extraction through disposal
  - Comparing two designs, materials, or processes on environmental impact, not just operational phase
  - Identifying which stage of production or use causes the most damage
one_liner: "Quantify environmental impact across a product's full life cycle and identify stage-level hotspots."
---

# Life Cycle Assessment

## Overview

Life Cycle Assessment (LCA) quantifies the environmental impact of a product, service, or process across its entire lifecycle — from raw material extraction through manufacturing, transport, use, and end-of-life disposal or recycling. Rather than optimizing a single phase (e.g., reducing operational emissions), LCA reveals whether improvements in one stage create larger burdens elsewhere (e.g., a lighter car uses less fuel but requires energy-intensive materials). Practitioners use this when a product's environmental story feels incomplete or when marketing claims focus on one phase while the full picture is unknown.

## Analytical Procedure

### Phase 1 — Define Goal and Scope

1. **State the product or service clearly.** Include its functional unit — the basis of comparison. Not "a plastic bag" but "a bag that holds 10 kg of groceries for one trip to the store." Functional unit must be measurable and consistent across alternatives being compared.

2. **Set system boundaries.** Decide what stages to include:
   - **Cradle-to-gate:** extraction and manufacturing only (excludes transport, use, disposal).
   - **Cradle-to-grave:** extraction through disposal, but excludes user phase.
   - **Cradle-to-cradle:** includes recycling loops and assumes closed-loop recovery.
   - **Gate-to-gate:** one process segment only (e.g., injection molding step in a factory).
   
   Document what you are *excluding* and why (e.g., capital equipment amortized separately, or administrative overhead below 1% of mass).

3. **Define the time horizon and geography.** LCA results vary by region (electricity grid carbon intensity, distance to recycling, local regulations). State the baseline year and location.

4. **Identify impact categories to assess.** Standard ones include:
   - Global warming potential (kg CO₂ equivalent)
   - Acidification potential
   - Eutrophication potential
   - Water consumption
   - Primary energy demand
   - Hazardous waste generation
   
   Do not assess all categories — pick 3–5 material to your product.

### Phase 2 — Life Cycle Inventory (LCI)

5. **Map all process steps from raw material through end-of-life.** Draw a flowchart showing inputs (energy, water, materials) and outputs (product, emissions, waste) at each stage. For a manufactured good, this typically includes:
   - Extraction of raw materials (mining, harvesting, drilling)
   - Transportation of feedstock
   - Manufacturing and assembly
   - Packaging and distribution
   - Use phase (if applicable; e.g., fuel burned by a car)
   - End-of-life (landfill, incineration, recycling)

6. **Quantify material and energy flows.** For each process step, record:
   - **Input:** kg of raw material, MJ of electricity, liters of water, etc.
   - **Output:** kg of product, kg of emissions (CO₂, NOx, etc.), kg of waste by type.
   
   Use industry data (e.g., ecoinvent, US Life Cycle Inventory Database, product-specific Environmental Product Declarations) when primary data is unavailable. Document the source and year for every input.

7. **Account for recycling and co-products.** If a process yields multiple outputs or material is recycled:
   - Use the **cut-off rule:** exclude recycled material as input; count recovery at end-of-life as an output credit.
   - Or use **substitution:** subtract the environmental burden of the virgin material the recycled material displaces.
   
   State which method you used; results differ significantly.

8. **Calculate totals by impact category.** Sum all emissions (e.g., CO₂ from energy, transportation, chemical reactions) across all stages. Multiply quantities by characterization factors (e.g., 1 kg of methane = 28 kg CO₂ equivalent over 100 years) to express in common units.

### Phase 3 — Impact Assessment and Sensitivity

9. **Identify hotspots — stages or inputs causing >20% of total impact.** For example:
   - Material extraction (energy-intensive aluminum smelting)
   - Manufacturing (solvent emissions)
   - Use phase (fuel burned; electricity consumed)
   - Transportation (distance and modal choice)
   
   Rank stages by impact magnitude. Note which stages have highest data uncertainty.

10. **Run sensitivity analysis.** Vary key assumptions (e.g., end-of-life recovery rate, electricity grid carbon intensity, recycling rate) by ±20% and recalculate. If results change dramatically, those assumptions drive the conclusion and must be validated.

11. **Normalize and weight if comparing alternatives.** If assessing two designs:
    - Express both in the same functional unit.
    - Calculate the percentage difference in each impact category.
    - If weighting categories, document the weighting scheme (e.g., equal weight, expert judgment, stakeholder consensus). Weighting is subjective — always show unweighted results first.

### Phase 4 — Interpretation and Uncertainty

12. **Assess data quality.** For each major input, score quality as:
    - **High:** primary measured data, recent, location-specific
    - **Medium:** industry average, ≤5 years old, plausible range documented
    - **Low:** proxy or estimate, age unknown, wide uncertainty range
    
    Report the proportion of your model built on high-, medium-, and low-quality data.

13. **List assumptions explicitly.** Examples:
    - Electricity grid carbon intensity assumed constant over product lifetime.
    - 80% of plastic waste goes to landfill; 20% is recycled (varies by jurisdiction).
    - Transport distance assumed average for the region.
    - End-of-life process energy not included (often 2–5% of total).

14. **State what you cannot conclude from this LCA.** Do NOT claim:
    - This product is "green" or "sustainable" without defining those terms.
    - This design is "better" if impacts are mixed (lower carbon but higher water use).
    - Results apply to regions or time periods outside your scope.
    - Quantitative certainty beyond ±15–20% (typical LCA precision).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Functional unit is specific, measurable, and consistent across alternatives | Y/N |
| System boundaries (cradle-to-X) are explicitly stated and justified | Y/N |
| Time horizon and geography are declared | Y/N |
| ≥3 impact categories are assessed | Y/N |
| All lifecycle stages are mapped and quantified (or marked "excluded" with reason) | Y/N |
| Data sources and years are documented for ≥80% of inputs | Y/N |
| At least one hotspot (>20% of total impact) is identified | Y/N |
| Sensitivity analysis varies key assumptions and reports outcome changes | Y/N |
| Recycling/co-products are handled with one stated method (cut-off or substitution) | Y/N |
| Data quality scored (high/medium/low) and proportions reported | Y/N |
| Assumptions explicitly listed; limits of the study stated | Y/N |
| No marketing claims ("green," "sustainable") made without definition | Y/N |

## Red Flags

- Functional unit is vague ("one product," "per year") or differs between alternatives being compared. Comparison becomes meaningless.
- System boundary is drawn around the manufacturing stage only, excluding use and disposal. Misleading if the product's main impact is in operation (e.g., a vehicle).
- No hotspot analysis. Recommendations are made without knowing where the impact actually concentrates.
- Sensitivity analysis is absent or claims "robust" without testing assumptions. If recycling rate, electricity grid, or transport distance changes, does the conclusion reverse?
- Data quality is undeclared or mixed (60% estimated, 40% measured) but treated as certain. Precision claimed exceeds data quality.
- Comparison of two products uses different system boundaries (one includes use, the other doesn't). Unfair by design.
- End-of-life modeled as 100% landfill or 100% recycling, with no regional or realistic distribution.
- Conclusions overstated: "This material is better" when the LCA shows lower carbon but higher water use — a trade-off, not a victory.

## Output Format

```
## Life Cycle Assessment Report

**Product/Service:**
<name and functional unit, e.g., "Plastic water bottle (500 mL, single-trip use)">

**System Boundary:**
<Cradle-to-gate / Cradle-to-grave / Cradle-to-cradle; time horizon; geography; exclusions and justification>

**Impact Categories Assessed:**
1. <category> (unit)
2. <category> (unit)
3. ...

### Life Cycle Inventory Summary

| Stage | Material Input | Energy Input | Key Emissions | Data Quality |
|---|---|---|---|---|
| Raw material extraction | <...> | <...> | <...> | High/Medium/Low |
| Manufacturing | <...> | <...> | <...> | <...> |
| Transport | <...> | <...> | <...> | <...> |
| Use (if applicable) | <...> | <...> | <...> | <...> |
| End-of-life | <...> | <...> | <...> | <...> |

### Impact Results (by category)

| Impact Category | Total | Hotspot Stage | % of Total |
|---|---|---|---|
| Global warming (kg CO₂-eq) | <...> | <...> | <...> |
| <...> | <...> | <...> | <...> |

### Hotspot Analysis
1. <Stage>: <magnitude> <unit>, reason: <dominant input or process>
2. <Stage>: ...

### Sensitivity Analysis
- Varying recycling rate (0% → 80%): impact changes by ±__%
- Varying electricity grid intensity (±20%): impact changes by ±__%
- Varying end-of-life process: impact changes from <low> to <high>

**Conclusion:** <Most sensitive parameter is...>

### Key Assumptions & Limitations
- <Assumption 1>
- <Assumption 2>
- Excluded: <reason>
- Precision: ±15–20% (typical for LCA)
- Results do NOT apply to: <regions, time periods, or contexts outside scope>

### Comparison (if applicable)
| Alternative | Global Warming (kg CO₂-eq) | Water Use (L) | Difference vs. Baseline |
|---|---|---|---|
| Baseline design | <...> | <...> | — |
| Alternative A | <...> | <...> | <+/–__% GWP, <+/–__% water> |

**Trade-off noted:** <Lower carbon but higher water use, etc.>

### Confidence
<high | medium | low> — <Justification: e.g., "Medium—primary data available for manufacturing (70% of impact) but use-phase assumptions span ±30%; end-of-life recovery rates vary by jurisdiction.">
```
---
