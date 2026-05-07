---
name: dpsir
display_name: DPSIR Framework
class: lens
underlying_class: native
domain: ecology
source: European Environment Agency (1994); formalized in environmental impact assessment and policy analysis
best_for:
  - Tracing root causes of environmental degradation from human activity through systemic impact
  - Structuring environmental policy responses around causal chains rather than isolated symptoms
  - Identifying intervention points in complex socio-ecological systems
one_liner: "Drivers-Pressures-State-Impact-Response — trace the causal chain from human activity to environmental change."
---

# DPSIR Framework

## Overview
DPSIR maps environmental problems as a causal chain: Drivers (human economic/social activity) create Pressures (emissions, resource extraction, habitat loss) that alter environmental State (water quality, species populations, climate), triggering Impacts (ecosystem collapse, human health effects, economic loss) that prompt Responses (regulation, technology, behavior change). Practitioners use it to avoid treating symptoms in isolation—a water quality problem traced backward reveals the pressures causing it, the drivers behind those pressures, and where policy can actually intervene. The discipline is completing the full chain; incomplete chains produce responses that fail.

## Analytical Procedure

### Phase 1 — Define the Environmental Problem

1. **State the observed environmental change in measurable terms.** Not "pollution is bad" but "nitrate concentration in the aquifer exceeded 50 mg/L in 2023, up from 15 mg/L in 2010." Include location, timeframe, and metric.

2. **Classify this change as State, Impact, or both.** 
   - **State** = the physical/chemical/biological condition of the environment (soil nitrogen, fish population, air particulates).
   - **Impact** = the consequence for human or ecosystem well-being (crop yield loss, species extinction, respiratory illness, economic loss).
   - Most observed problems are Impacts; Impacts rest on State changes.

### Phase 2 — Trace Pressures

3. **List all Pressures that could alter the State you identified.** Pressures are flows or forces applied to the environment:
   - Emissions (nitrogen fertilizer runoff, CO₂, methane)
   - Resource extraction (water withdrawal, timber harvest, mining)
   - Habitat destruction (land clearing, damming, fragmentation)
   - Invasive species introduction
   - Physical disturbance (trawling, dredging, plowing)
   
   Use your measured State change as a filter: which pressures, if intensified, would produce exactly that change? Be specific — "pollution" is not a pressure; "application of urea fertilizer at 200 kg/ha per year" is.

4. **For each Pressure, estimate the magnitude and trend.** What is the current rate? Has it increased, decreased, or stabilized over the period your State change covers? This step separates relevant pressures from background noise.

5. **Prioritize Pressures by contribution.** If multiple pressures could cause your State change, estimate which accounts for the largest share (use local data, modeling, literature, or expert judgment). Mark each as Primary, Secondary, or Tertiary.

### Phase 3 — Identify Drivers

6. **For each Primary Pressure, ask: What human activity generates this Pressure?** Drivers are the root economic, social, or behavioral forces:
   - Agricultural intensification (yield per hectare target drives fertilizer use)
   - Industrial production (output target drives emissions)
   - Population growth (demand for food/water/energy)
   - Consumer preference (demand for cheap animal protein, travel, goods)
   - Regulatory arbitrage (moving dirty production to regions with lax rules)
   - Technological lock-in (cheap coal power vs. renewable investment)
   
   Name the driver as a human choice or system incentive, not as a neutral trend. "Population growth" is weaker than "agricultural subsidies that incentivize monoculture over biodiversity" because the latter identifies a point of intervention.

7. **Verify the causal link.** For each Driver→Pressure→State chain, write out the mechanism. Example: "Agricultural subsidy → fertilizer use↑ → nitrogen runoff↑ → aquifer nitrate↑". If the link is weak or indirect, say so and note what assumption you're making.

### Phase 4 — Map Impacts and Current Responses

8. **List the human/ecosystem consequences of the State change.** Impacts are measurable harms:
   - Ecosystem: species loss, habitat degradation, nutrient cycling disruption
   - Human health: illness, mortality, reduced quality of life
   - Economic: crop loss, water treatment cost, lost tourism, property damage
   - Social: conflict over resource access, migration, inequality
   
   Quantify if possible (e.g., "drinking water treatment cost increased by $2M annually").

9. **Inventory existing Responses.** What policies, technologies, or behaviors are already in place to reduce the Pressure or mitigate the Impact? Examples:
   - Regulation: fertilizer application caps, emission limits
   - Technology: precision agriculture, water treatment, renewable energy
   - Individual action: dietary change, water conservation
   - Market mechanism: payment for ecosystem services, carbon pricing
   
   For each Response, note: Is it addressing the Driver, the Pressure, the State, or the Impact? Does it work? Is it at scale?

10. **Identify response gaps.** Which part of the chain has no response? Is the problem that Drivers are not addressed (only symptoms managed), or that responses exist but aren't implemented?

### Phase 5 — Synthesis and Intervention Design

11. **Map the complete chain for your problem.** Use the template below. A weak chain has gaps (e.g., Drivers identified but Pressures unmeasured, or Responses that don't address the Driver).

12. **Evaluate response leverage.** For each identified gap, design or propose a Response. Judge whether it:
   - Addresses the root Driver (highest leverage, slowest, hardest politically)
   - Reduces the Pressure (medium leverage, medium difficulty)
   - Remediates the State (lower leverage, faster, easier politically but may not prevent recurrence)
   - Adapts to Impacts (necessary but not preventive)
   
   Responses targeting Drivers are more durable; responses targeting Impacts alone are band-aids.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Environmental problem (State or Impact) is defined with specific metrics and timeframe | Y/N |
| At least one Primary Pressure is named with a quantified magnitude and trend | Y/N |
| Each Primary Pressure is linked to at least one Driver via a plausible mechanism | Y/N |
| Impacts are listed with at least one quantified consequence (ecosystem or human) | Y/N |
| At least one existing Response is identified and classified by causal stage | Y/N |
| At least one response gap is acknowledged (Driver, Pressure, or implementation) | Y/N |
| The chain contains no circular logic (e.g., "population growth causes population growth") | Y/N |

## Red Flags

- The chain starts at Pressure or State, skipping Drivers. This produces responses that fail because they don't address incentives.
- Drivers are stated as inevitable trends ("population will grow," "technology advances"). The strongest drivers are human choices embedded in policy and economics—find those, not excuses.
- Impacts are listed but not quantified. "Biodiversity loss" is vague; "three native fish species extirpated, species richness fell from 22 to 14" is measurable and actionable.
- Responses are all at the Adaptation or Impact stage (restoration, healthcare, insurance) with no effort to reduce the Pressure or address the Driver. The system is locked into treating symptoms.
- The chain is linear with no feedback. Real environmental systems have loops: agricultural runoff causes eutrophication, dead zones reduce fish, loss of protein source increases pressure for terrestrial protein, agricultural expansion increases runoff. Missing the loop means missing where intervention could break the cycle.
- "Nature" or "climate" is listed as a Driver. Natural variability is real, but it is not the same as a human Driver. Separate them.

## Output Format

```
## DPSIR Assessment

**Environmental Problem (State/Impact):**
- Metric: <measured quantity and unit>
- Location: <geographic scope>
- Timeframe: <period of observation>
- Magnitude of change: <quantified before/after or trend>

### Drivers (Human activities and incentives)
1. <Driver 1: e.g., "agricultural subsidy structure incentivizes monoculture">
   - Mechanism: <causal link to Pressure>
   - Evidence/assumption: <how confident in this link>

2. <Driver 2>
   ...

### Pressures (Environmental forces)
| Pressure | Magnitude | Trend | Primary/Secondary | Link to State |
|---|---|---|---|---|
| <e.g., nitrogen fertilizer runoff> | <quantity, e.g., 50 kg N/ha/year> | ↑ / ↓ / → | Primary | ↑ aquifer NO₃⁻ concentration |
| <...> | <...> | <...> | <...> | <...> |

### State Change (Environmental condition)
- Current: <measured state>
- Baseline: <reference state or time point>
- Mechanism of change: <how Pressures alter State>

### Impacts (Ecosystem and human consequences)
1. <Impact 1 with quantity: e.g., "three fish species extirpated; species richness fell from 22 to 14">
2. <Impact 2>
3. <...>

### Current Responses
| Response | Type (Regulation/Tech/Behavior/Market) | Causal stage targeted (Driver/Pressure/State/Impact) | Scale | Effectiveness |
|---|---|---|---|---|
| <e.g., fertilizer application cap> | Regulation | Pressure | Regional; partial coverage | Moderate (non-compliant farms remain) |
| <...> | <...> | <...> | <...> | <...> |

### Response Gaps
1. <Gap 1: e.g., "No response addresses the subsidy structure that incentivizes fertilizer use (Driver level)">
2. <Gap 2>

### Recommended Interventions
1. <Driver-level: e.g., "Reform agricultural subsidy to reward soil health metrics instead of yield volume">
   - Leverage: High (addresses root incentive)
   - Implementation barrier: High (political and economic)

2. <Pressure-level: e.g., "Mandate precision fertilizer application (variable-rate technology)">
   - Leverage: Medium
   - Implementation barrier: Medium (cost, training, monitoring)

3. <State-level: e.g., "Increase aquifer monitoring frequency to early-warn nitrate exceedances">
   - Leverage: Low (remedial, not preventive)
   - Implementation barrier: Low (technical feasibility)

### Confidence
<high/medium/low> — <justification: e.g., "High confidence in Pressure-State link (measured data). Medium confidence in Driver identification (based on regional literature, not site-specific study). Low confidence in Driver-Pressure mechanism (assumed but not quantified).">
```
