---
name: ecosystem-services
display_name: Ecosystem Services Valuation (TEEB/MA)
class: lens
underlying_class: native
domain: ecology
source: TEEB (The Economics of Ecosystems and Biodiversity, 2010) and Millennium Ecosystem Assessment (2005)
best_for:
  - Quantifying non-market benefits of natural systems for policy decisions
  - Comparing conservation investments across competing land uses
  - Identifying ecosystem dependencies in supply chains and infrastructure
one_liner: "Classify ecosystem services into four categories to quantify and value them."
---

# Ecosystem Services Valuation (TEEB/MA)

## Overview

Ecosystem services are the benefits humans derive from natural systems — pollination, water filtration, carbon sequestration, flood control, recreation. Rather than treating nature as free or infinite, this lens values these services in economic terms so they can be weighed against market-priced alternatives in policy and investment decisions. Practitioners use it when a development decision (dam, urbanization, agricultural conversion) requires comparing the cost of losing ecosystem functions against the benefit of the proposed use. The framework organizes services into four categories (provisioning, regulating, supporting, cultural), anchors each to measurable human outcomes, and assigns economic value through replacement cost, avoided cost, or market-derived methods.

## Analytical Procedure

### Phase 1 — Identify the Ecosystem and Boundary

1. **Define the physical system.** Name the specific ecosystem (wetland, forest patch, coral reef, agricultural landscape) and its geographic boundaries. Include elevation, climate, dominant species composition, and land tenure. Be precise enough that someone could visit the location.

2. **List all human populations within or downstream of the system.** Identify direct users (farmers, fishers, residents) and indirect beneficiaries (people breathing filtered air, using treated water, receiving flood protection). Note distances and dependency pathways.

3. **Establish the baseline and counterfactual.** What is the current state of the ecosystem? What is the plausible future state if the ecosystem is converted, degraded, or conserved? The comparison is always against the counterfactual, not against some pristine historical state.

### Phase 2 — Map Services to the Four Categories

For each service, assign it to exactly one category and specify the human outcome it produces:

**Provisioning Services** — direct extraction or harvest
- Food (fish, game, crops, forage)
- Water (for drinking, irrigation, industrial use)
- Fiber (timber, palm, cotton, wool)
- Genetic resources (pharmaceutical compounds, crop varieties)
- Biochemical compounds (natural pesticides, dyes)

**Regulating Services** — ecosystem processes that maintain livable conditions
- Climate regulation (carbon storage, temperature moderation)
- Water regulation (flood buffering, drought mitigation, aquifer recharge)
- Pollination (crop and wild plant reproduction)
- Pest and disease control (natural enemies, immune resistance in plants)
- Erosion control (soil stabilization, sedimentation prevention)
- Nutrient cycling (nitrogen fixation, phosphorus availability)
- Waste treatment (decomposition, filtering)

**Supporting Services** — ecosystem processes necessary for all other services
- Primary production (photosynthesis, biomass creation)
- Nutrient cycling (nutrient pathways through soil and water)
- Soil formation (weathering, organic matter accumulation)
- Habitat provision (breeding grounds, refugia, migration corridors)

**Cultural Services** — non-material human benefits
- Recreation (hiking, fishing, bird-watching, tourism)
- Aesthetic value (landscape beauty, visual amenity)
- Spiritual or religious significance (sacred sites, ceremonial use)
- Educational value (research sites, nature study, environmental awareness)
- Sense of place (cultural identity tied to landscape)

4. **For each service identified, answer:**
   - Who receives this service? (specific population, sector, distance)
   - What is the measurable outcome? (tons of fish, acre-feet of water, hectares protected from flooding, number of visitors)
   - If this service were lost, what would be the cost to replace it or do without it?

### Phase 3 — Quantify Service Flow

5. **Measure or model the quantity of each service under current and counterfactual conditions.**
   - For provisioning services: production per unit area per year (e.g., kg fish/hectare/year).
   - For regulating services: physical quantity of the regulating process (e.g., metric tons CO₂ sequestered, mm of storm water retained, percentage of pest pressure suppressed).
   - For cultural services: user numbers, visit frequency, or area accessible (e.g., 5,000 visitors/year, 200 hectares of accessible hiking).
   - Use primary data (field surveys, harvest records) if available; otherwise use published coefficients for comparable ecosystems.

6. **Calculate the difference (delta) between current and counterfactual.**
   - If the counterfactual is conversion to agriculture: "Current wetland sequesters 8 tons CO₂/hectare/year; drained corn field sequesters 0.5 tons/year — delta = 7.5 tons/hectare/year."
   - If the counterfactual is business-as-usual degradation: quantify the rate of decline and project it forward.

### Phase 4 — Assign Economic Value

7. **Choose a valuation method for each service.** Match the method to the service type and data availability:

| Service Category | Primary Methods | Notes |
|---|---|---|
| Provisioning | Market price, replacement cost, avoided cost | Use current market price for harvested goods; use substitute cost if markets don't exist |
| Regulating (climate) | Social cost of carbon ($/ton CO₂) | Standard: $50–200/ton in developed economies; vary by region and damage scenario |
| Regulating (water) | Replacement cost of treatment/infrastructure, avoided cost of flood damage | Cost to build/operate treatment plant, or expected damage from unregulated floods |
| Regulating (pollination) | Replacement cost of manual or mechanical pollination, lost crop value | Agricultural benefit attributable to wild pollinators |
| Regulating (pest control) | Replacement cost of pesticides + application, avoided crop loss | Cost of chemicals + labor + environmental remediation |
| Regulating (erosion, nutrients) | Replacement cost of fertilizers, avoided dredging, avoided eutrophication damage | Cost to replace lost soil fertility or downstream water quality |
| Cultural (recreation) | Travel cost method, hedonic property pricing, contingent valuation | Visitor spending + time value; property value premium from proximity; survey-based willingness to pay |
| Cultural (other) | Contingent valuation, benefit transfer from similar sites | Ask stakeholders willingness-to-pay; adapt values from comparable ecosystems |

8. **Assign unit values and calculate total value.**
   - Example: If the wetland sequesters 7.5 tons CO₂/hectare/year and the social cost is $100/ton, the climate value is $750/hectare/year.
   - If the wetland is 500 hectares, total annual climate value = $375,000.
   - Repeat for each service.

9. **Document all value assignments.** Record the source of each number (peer-reviewed study, government guidance, market price on date X, expert elicitation). Valuations are sensitive to methodological choice; transparency is non-negotiable.

### Phase 5 — Aggregate and Interpret

10. **Sum services to get total ecosystem value (TEV).**
    - TEV = Σ (quantity of service i) × (unit value of service i)
    - Present as annual value ($/year) and, if comparing to a development option, as net present value over a discount period (e.g., 50 years at 3% discount rate).

11. **Compare TEV to the counterfactual.**
    - If counterfactual is conversion: "Conserving the wetland yields $X/year in services; converting it to agriculture yields $Y/year in crops minus $Z/year in lost regulating services. Net benefit of conservation = $X - ($Y - $Z)."
    - If counterfactual is degradation: "Current ecosystem value is $X/year; business-as-usual degradation reduces it to $Y/year by year 20. Cost of degradation = $(X – Y)/year."

12. **Identify data gaps and sensitivity.**
    - Which services were not quantified and why? (data unavailable, service negligible, service not market-relevant)
    - Which valuations are most uncertain? Re-run the calculation with low and high estimates for those services.
    - Does the conclusion (conservation wins, conversion wins) hold across a range of discount rates and value assumptions?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Ecosystem boundaries are defined precisely (location, size, biophysical characteristics) | Y/N |
| Human beneficiaries are identified by population, sector, and distance | Y/N |
| Every identified service is assigned to one of four categories | Y/N |
| Service quantities are measured or modeled with cited sources | Y/N |
| Current and counterfactual quantities are compared (delta calculated) | Y/N |
| Each valuation method matches the service type and has a documented source | Y/N |
| Total ecosystem value is calculated as sum of all services | Y/N |
| Comparison to counterfactual is explicit (TEV vs. alternative use value) | Y/N |
| Data gaps and sources of uncertainty are documented | Y/N |
| Sensitivity analysis tested at least the two most uncertain valuations | Y/N |

## Red Flags

- Supporting services are valued independently. Supporting services enable other services; double-counting them inflates TEV. Value only provisioning, regulating, and cultural; note that supporting services are prerequisites.
- All services are assigned to the same valuation method (e.g., all "market price" or all "replacement cost"). Different services require different logic. Uniform methodology suggests template filling, not reasoning.
- Counterfactual is missing or vague ("what if the ecosystem disappears?"). Without a specific future state (conversion to agriculture, urbanization, managed degradation), the valuation is abstract and unactionable.
- Data sources are absent or circular (e.g., "pollination value from ecosystem services literature" without naming the study). Non-reproducible valuations cannot be defended in policy debates.
- Discount rate is not disclosed or is set at extreme values (0% or >10%). TEV is highly sensitive to discount rate. Burying this choice is a red flag for advocacy masquerading as analysis.
- Total value is presented without uncertainty bounds. Every valuation is an estimate; presenting a point value implies false precision.
- Cultural services are missing. Recreation and spiritual value are often large but are neglected because they resist market valuation. Omission biases the analysis toward extraction.

## Output Format

```
## Ecosystem Services Valuation

**Ecosystem:**
- Name and location: <...>
- Area: <...> hectares
- Dominant land cover and biophysical characteristics: <...>

**Beneficiary populations:**
- Direct users (distance, sector): <...>
- Indirect users (downstream, regional): <...>

**Baseline and counterfactual:**
- Current condition: <...>
- Alternative future (conversion/degradation): <...>
- Time horizon for comparison: <...> years

### Service Identification and Quantification

| Service | Category | Unit | Current | Counterfactual | Delta | Source |
|---|---|---|---|---|---|---|
| <e.g., Carbon storage> | Regulating | tons CO₂/hectare/year | <...> | <...> | <...> | <citation> |
| <e.g., Fish production> | Provisioning | kg/hectare/year | <...> | <...> | <...> | <citation> |
| <e.g., Recreation visits> | Cultural | visits/year | <...> | <...> | <...> | <citation> |

### Valuation

| Service | Valuation Method | Unit Value | Annual Value (Current) | Annual Value (Counterfactual) | Source |
|---|---|---|---|---|---|
| <...> | <Replacement cost / Market price / Social cost / Contingent valuation / ...> | $<...> | $<...> | $<...> | <citation> |

### Total Ecosystem Value (TEV)

- **Sum of current services:** $<...> / year
- **Sum of counterfactual services:** $<...> / year
- **Net annual benefit of conservation:** $<...> / year
- **50-year NPV (at 3% discount rate):** $<...>

### Data Gaps and Uncertainty

| Service | Status | Reason / Source |
|---|---|---|
| <...> | Quantified / Omitted / High uncertainty | <explanation> |

### Sensitivity Analysis

| Scenario | Discount Rate | Carbon Price | Recreation Value | TEV | Conclusion |
|---|---|---|---|---|---|
| Central | 3% | $100/ton | Base | $<...> | Conservation +$X |
| Low value | 5% | $50/ton | –30% | $<...> | Conservation +$Y |
| High value | 2% | $150/ton | +30% | $<...> | Conservation +$Z |

**Conclusion remains robust?** Yes / No — <if no, under which parameter ranges does the conclusion flip?>

### Confidence
<high | medium | low> — <justification citing data availability, methodological agreement with peer literature, discount rate sensitivity, stakeholder agreement on service identification>
```
