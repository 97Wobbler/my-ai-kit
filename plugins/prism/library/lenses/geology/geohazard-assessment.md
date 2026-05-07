---
name: geohazard-assessment
display_name: Geohazard Assessment
class: lens
underlying_class: native
domain: geology
source: USGS Hazards Program, International Association of Engineering Geologists (IAEG), UNESCO; synthesized from seismic, volcanic, and mass-movement standards
best_for:
  - Evaluating site or regional vulnerability to earthquakes, volcanic activity, landslides, or tsunamis
  - Prioritizing mitigation investments across multiple hazard types
  - Screening new development sites for acceptable risk
one_liner: "Multi-hazard framework that systematically ranks earthquake, volcano, landslide, and tsunami risks."
---

# Geohazard Assessment

## Overview

Geohazard Assessment is a systematic procedure for identifying, characterizing, and ranking natural ground-based hazards across four primary categories: seismic (earthquakes), volcanic (eruptions and lahars), mass movement (landslides and debris flows), and tsunami (wave inundation). Practitioners apply this lens when deciding where to build, whether to occupy an existing structure, or where to invest in early-warning systems. The discipline is treating all four hazards as competing risks in a single framework, rather than assessing them in isolation.

## Analytical Procedure

### Phase 1 — Hazard Identification and Inventory

1. **Define the study area.** Mark the boundary on a map. Note latitude, longitude, elevation range, and primary land uses (urban, agricultural, industrial, infrastructure corridors).

2. **Compile historical hazard records for the past 500 years** (or all available). For each hazard type, list:
   - **Seismic:** Documented earthquakes (magnitude, epicenter, felt intensity, damage reports, year).
   - **Volcanic:** Eruptions, lahars, ashfall zones, pyroclastic flows, lava flows (volume, extent, date).
   - **Mass movement:** Landslides, debris flows, rockfalls (type, area, depth, trigger, date, casualties if any).
   - **Tsunami:** Historical wave heights, inundation extent, sources (distant earthquakes, local submarine slides, year).
   
   Use USGS, national geological surveys, local universities, and colonial-era records where available.

3. **Map active geologic structures and features.** Plot:
   - Faults (confirmed active, potentially active, historical rupture segments, dip angle, slip rate if known).
   - Volcanic centers (calderas, cones, vents, extent of historical lava and pyroclastic deposits).
   - Steep slopes (>30°), historic landslide scars, debris fan deposits, zones of deep weathering or previous failure.
   - Submarine trenches, offshore fault zones, and coastal geometry (depth profile, strait width, beach slope).

4. **Assess data gaps.** For each hazard type, mark whether records are continuous, sparse, incomplete, or absent. Note where instrumental records are too short to capture the full hazard spectrum (e.g., seismometers <50 years old in a region with rupture intervals >200 years).

### Phase 2 — Hazard Characterization

5. **For each hazard type, estimate recurrence intervals and magnitude/extent parameters:**
   - **Seismic:** Estimate the Maximum Credible Earthquake (MCE) magnitude from paleoseismic studies or fault geometry. Calculate recurrence interval from slip rate (if known) or from historical frequency. Identify the largest historic shock and the interval since it occurred.
   - **Volcanic:** Determine eruption frequency (if the volcano is active), typical eruption size (Volcanic Explosivity Index range), and the extent of historically documented deposits. Mark the date of the last eruption and any unrest signals (gas emissions, deformation, seismicity).
   - **Mass movement:** For each major slope or gully, estimate the critical rainfall threshold (mm/day or antecedent moisture), typical volume, and runout distance. Identify whether failures are primarily soil or bedrock, single-event or ongoing.
   - **Tsunami:** For distant sources (subduction zones, mid-ocean ridges), estimate travel time and maximum wave height at the coast. For local sources (submarine landslides, earthquake-triggered seafloor displacement), estimate wave generation time and near-field amplification.

6. **Assign a probability category for each hazard in the next 50 years:**
   - **Very high (>50%):** Recurrence interval <50 years and no current quiet period known.
   - **High (20–50%):** Recurrence interval 50–150 years.
   - **Moderate (5–20%):** Recurrence interval 150–500 years.
   - **Low (1–5%):** Recurrence interval 500–2000 years.
   - **Very low (<1%):** Recurrence interval >2000 years or no historical record.

### Phase 3 — Exposure and Vulnerability Assessment

7. **Map exposure for each hazard.** Identify:
   - **Buildings and infrastructure** in high-hazard zones (count, use type, occupancy density, construction year and likely seismic/volcanic resistance).
   - **Population at risk** (full-time residents, workers, daytime visitors, nighttime population).
   - **Critical facilities** (hospitals, fire stations, water treatment, power stations, emergency response centers).
   - **Economic assets** (agricultural land value, industrial zones, transportation corridors, mining operations).

8. **Estimate vulnerability for each building type and hazard:**
   - **Seismic:** Use building code era and material (unreinforced masonry, concrete frame, steel, timber). Apply standard damage curves (USGS or European standards) to estimate collapse probability or loss given a specified ground motion (PGA, spectral acceleration).
   - **Volcanic:** Assess roof load capacity relative to likely ashfall depth; estimate ignition risk for lahars; map lava flow paths and building thermal exposure.
   - **Mass movement:** Estimate impact force from debris; identify buildings on steeper slopes or directly downslope.
   - **Tsunami:** Calculate wave force and bore depth for buildings in inundation zones; assess vertical evacuation feasibility.

9. **Calculate annualized risk for each hazard type:**
   Risk = Probability × Exposure × Vulnerability (in units of expected annual loss in dollars or lives per year).
   
   Tabulate all four hazards for the same study area using the same economic or population baseline.

### Phase 4 — Comparative Ranking and Synthesis

10. **Rank all four hazards in order of annualized risk.** Note where hazards overlap spatially (e.g., seismic and tsunami, or volcanic and mass movement triggered by ash load).

11. **Identify hazard hotspots:** Zones where two or more hazards converge and combined risk exceeds any single hazard. These are priority areas for mitigation or development restrictions.

12. **Document assumptions and uncertainty.** For each major estimate (recurrence interval, magnitude, extent), state the data source, confidence level, and sensitivity (how much would the rank change if this parameter were revised by ±50%?).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Historical record spans at least 200 years (or all available) for each hazard | Y/N |
| All four hazard types explicitly addressed in the study area | Y/N |
| Recurrence intervals derived from paleoseismic, paleontologic, or archival evidence, not assumption | Y/N |
| Probability categories justified by time since last event and known/estimated intervals | Y/N |
| Exposure and vulnerability quantified in the same metric (USD or lives) for all hazards | Y/N |
| Annualized risk compared across all four hazards on the same axis | Y/N |
| Data gaps and uncertainties explicitly documented with sensitivity ranges | Y/N |

## Red Flags

- Only one or two hazards are assessed; the others are mentioned but not characterized. This is selective omission and defeats the purpose of the framework.
- Probability categories are assigned by visual inspection of a map with no recurrence interval calculation. Stating "high hazard" without a number is circular reasoning.
- Exposure and vulnerability for different hazards are expressed in different units (e.g., seismic in USD, volcanic in number of buildings) and therefore cannot be ranked.
- The last major event for a hazard was >500 years ago and the study concludes "low risk" without justification. Many great earthquakes and eruptions have intervals >500 years.
- Critical facilities (hospitals, power plants) are mentioned but no separate risk calculation is done for them. They often dictate policy even if overall population risk is moderate.
- Uncertainty ranges are not provided. A rank order that collapses when a key parameter is varied ±50% is brittle and unreliable for decision-making.

## Output Format

```
## Geohazard Assessment Report

**Study area:**
<Name, location, size, primary land use>

**Assessment period:** <Start year to end year of historical record reviewed>

### Phase 1 — Hazard Identification

**Hazards present (in order of historical impact):**
1. <Hazard type; brief characterization of recent activity>
2. ...

**Data completeness:**
| Hazard | Record span | Quality | Gaps |
|---|---|---|---|
| Seismic | <years> | <good/moderate/poor> | <...> |
| Volcanic | | | |
| Mass movement | | | |
| Tsunami | | | |

### Phase 2 — Hazard Characterization

| Hazard | Max magnitude/extent | Recurrence interval | Last event (year) | Probability next 50 yr |
|---|---|---|---|---|
| Seismic | M___ | ___ years | ___ | <Very High / High / Moderate / Low / Very Low> |
| Volcanic | VEI ___ | ___ years | ___ | <...> |
| Mass movement | Area ___ km², depth ___ m | ___ years | ___ | <...> |
| Tsunami | Wave height ___ m | ___ years | ___ | <...> |

**Key assumptions and data sources:**
- <Assumption 1: source, confidence>
- ...

### Phase 3 — Exposure & Vulnerability

**Population at risk:** <total number, distribution across hazard zones>

**Critical facilities in high-hazard zones:**
- <Facility type, number, hazard exposure>

**Annualized risk (expected annual loss):**
| Hazard | Probability | Exposed value ($) | Vulnerability factor | Annual loss ($) | % of total |
|---|---|---|---|---|---|
| Seismic | | | | | |
| Volcanic | | | | | |
| Mass movement | | | | | |
| Tsunami | | | | | |
| **Total** | | | | | 100% |

### Phase 4 — Hazard Hotspots and Ranking

**Ranking by annualized risk:**
1. <Hazard 1>: $___ per year
2. <Hazard 2>: $___
3. ...

**Overlapping hazard zones:**
- <Location, hazards present, combined annual loss>

**Key uncertainties and sensitivity:**
- Parameter: <X>. Current estimate: <Y>. If revised ±50%, rank would shift by <Z positions>.
- ...

### Confidence
<high | medium | low> — <justification: e.g., "High: 350+ year record, paleoseismic constraints on recurrence, and instrumental data all align." or "Low: volcanic record incomplete prior to 1800; last eruption 180 years ago makes interval estimation speculative.">
```
