---
name: sequence-stratigraphy
display_name: Sequence Stratigraphy
class: lens
underlying_class: native
domain: geology
source: Exxon Production Research Company (1977, Vail et al.); refined by Posamentier, Jervey, Vail (1988)
best_for:
  - Correlating strata across basins using sea-level cycles
  - Predicting reservoir geometry in clastic and carbonate systems
  - Dating and subdividing sedimentary sequences without radiometric control
one_liner: "Use sea-level changes to delineate stratigraphic intervals and build predictive models."
---

# Sequence Stratigraphy

## Overview
Sequence stratigraphy interprets sedimentary strata as products of sea-level oscillation superimposed on subsidence and sediment supply. Rather than relying on chronostratigraphy (absolute dating) or lithostratigraphy (rock type alone), it groups beds into systems tracts — coherent depositional packages bounded by surfaces of relative change in sea level. Practitioners use this framework to predict facies patterns laterally, to correlate strata across structural highs and lows without gaps, and to estimate hydrocarbon trap geometry and fill. The discipline is precise surface recognition and the geometric logic that follows from sea-level position.

## Analytical Procedure

### Phase 1 — Define the stratigraphic section and time scale

1. **Establish well control and outcrop transects.** Collect gamma-ray logs, core descriptions, and measured sections oriented perpendicular to structural dip and across paleohighs. Include at least 3-5 closely spaced wells or outcrops spanning the area of interest (typically 10-100 km).

2. **Calibrate to a chronostratigraphic framework.** Assign absolute ages to key horizons using biostratigraphy (foraminifera, ostracods, palynomorphs), magnetostratigraphy, or radiometric dates. This establishes the duration of your section and the resolution at which you can resolve sea-level cycles.

3. **Determine subsidence and sediment-supply rates.** Calculate the ratio of accommodation (space created by subsidence + sea-level rise) to sediment flux. Express as: accommodation rate (mm/yr) ÷ sediment supply rate (mm/yr). Ratios > 1 are underfilled (accommodation exceeds supply); ratios < 1 are overfilled (supply exceeds accommodation).

### Phase 2 — Identify key stratigraphic surfaces

4. **Recognize sequence boundaries (SB).** These are unconformities or correlative conformities marking the maximum rate of relative sea-level fall. In logs and cores, look for:
   - Subaerial exposure (root traces, paleosols, cross-cutting channels)
   - Basal truncation (older strata cut out downdip)
   - Downlap of overlying strata onto the surface
   - Abrupt change from marine to nonmarine facies
   - When subsurface data are sparse, project the inferred fall using clinoform geometry from seismic data.

5. **Locate the transgressive surface (TS) and maximum flooding surface (MFS).** The TS marks the point of maximum relative sea-level rise following the preceding fall; it is often marked by ravinement (wave or current erosion) and the abrupt upward increase in water depth. The MFS occurs at the inflection point where accommodation stops increasing — strata above it show progradation. In logs, look for:
   - Maximum clay content (highest gamma-ray spike) for marine sections
   - Thickest benthonic foraminiferal assemblages in deep water
   - Lowest terrigenous input in carbonate sections
   - Steepest slope in bedding geometry on seismic profiles

6. **Link surfaces across the section.** Trace each surface (SB, TS, MFS) from well to well and from subsurface to outcrop, adjusting for structural dip and growth faults. Establish that surfaces are isochronous or near-isochronous (deposited at roughly the same time across your area). Use biostratigraphy to verify.

### Phase 3 — Subdivide into systems tracts

7. **Assign each stratigraphic package to one of four systems tracts:**

   - **Lowstand Systems Tract (LST).** Lies below the SB and above the preceding MFS. Characterized by offlap geometry (clinoforms dipping basinward), incised channels, and bypass of finer sediment to deeper water. Accommodation is low; sediment supply dominates. Typical facies: braided fluvial channels, shoreface sands, submarine fans.

   - **Transgressive Systems Tract (TST).** Lies between the SB (or TS) and the MFS. Accommodation increases; the shoreline retreats landward (onlap). Facies fine upward. Typical: estuarine/bay mudstones with thin storm sands, shelf mudstones, slope shales.

   - **Highstand Systems Tract (HST).** Lies between the MFS and the next SB (or the current/eroded top of section). Accommodation decreases; clinoforms prograde oceanward. Facies coarsen upward. Typical: deltaic progradation, prograding shelf-margin wedges, isolated reef development.

   - **Falling-Stage Systems Tract (FSST, optional).** Narrow interval of forced regression between peak sea-level and the SB. Accommodation decreases rapidly. Strata prograde rapidly; subaerial features appear on the shelf. Typical: delta-front sands with deltaic topset, shelf-margin fans.

8. **Verify systems-tract identity using stacking patterns.** Confirm that your assignment is internally consistent. Plot gamma-ray curves or grain-size trends for each systems tract. LST and HST should show net coarsening upward and basinward shift. TST should show net fining upward and landward shift.

### Phase 4 — Establish predictive architecture

9. **Map the lateral facies mosaic.** For each systems tract, create a facies cross-section showing how lithology, thickness, and geometry change from structural high to basin center. Use well log correlation to guide facies interpretation. Mark paleocurrent directions and paleobathymetry to confirm depositional dip.

10. **Quantify changes in accommodation and supply.** For each sequence, calculate:
    - Eustatic sea-level change magnitude (e.g., 50–150 m for a major cycle)
    - Subsidence-adjusted accommodation curve (plot cumulative accommodation vs. time)
    - Sediment supply rate and how it varied during the sequence

11. **Project facies into undrilled areas using clinoform geometry.** Use seismic-stratigraphic dip and seismic attribute maps (acoustic impedance, coherency) to predict where high-quality reservoir facies (sand) are likely to occur in downdip or updip areas. Estimate trap geometry and charge pathway.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All key surfaces (SB, TS, MFS) are identified and defined in one sentence each | Y/N |
| Surfaces are correlated across ≥3 data points (wells, outcrops, seismic lines) | Y/N |
| Each systems tract is assigned and justified with facies/log evidence | Y/N |
| Subsidence rate and sediment-supply rate are quantified | Y/N |
| At least one stacking pattern (fining or coarsening trend) confirms systems-tract assignment | Y/N |
| Facies predictions for undrilled areas are explicit and linked to accommodation/supply logic | Y/N |

## Red Flags

- All surfaces are claimed to be identified but no evidence (core, log signature, or seismic geometry) is cited. Surface recognition failure.
- Subsidence and sediment supply are not calculated; accommodation is assumed to be "high" or "low" without numbers. The quantitative discipline has been skipped.
- Systems tracts are assigned by thickness alone (e.g., "thick zone = HST"). Thickness is ambiguous; facies and geometry must drive the interpretation.
- The MFS is claimed but no maximum-flooding evidence (e.g., deepest water, highest clay content) is shown.
- Seismic data are not used to extend the interpretation beyond wells. The framework becomes local and non-predictive.
- Stacking patterns are ignored; systems tracts are treated as time slices rather than as genetically related packages. The sequence is not verified to behave as a coherent unit.

## Output Format

```
## Sequence-Stratigraphic Analysis

**Area and time interval:**
<geologic region, age range (e.g., "Cretaceous Eagle Ford Shale, central Texas")>

**Chronostratigraphic control:**
- Biostratigraphy: <zones/markers used>
- Absolute age calibration: <radiometric or tuning constraints>
- Duration of section: <Ma>

**Subsidence and sediment supply:**
- Mean subsidence rate: <mm/yr>
- Mean sediment-supply rate: <mm/yr>
- Accommodation ratio (high/medium/low): <>
- Interpretation: <is the basin under- or overfilled?>

### Key Stratigraphic Surfaces

| Surface | Depth (subsurface) or Elevation (outcrop) | Diagnostic Features | Age (estimated) |
|---|---|---|---|
| Sequence Boundary (SB) | <...> | <...> | <...> |
| Transgressive Surface (TS) | <...> | <...> | <...> |
| Maximum Flooding Surface (MFS) | <...> | <...> | <...> |

### Systems Tracts and Facies Architecture

| Systems Tract | Lateral Extent | Thickness Range | Dominant Facies | Geometry | Stacking Pattern |
|---|---|---|---|---|---|
| LST | <...> | <...> | <...> | <offlap / onlap / toplap> | <coarsens up / fines up> |
| TST | <...> | <...> | <...> | <...> | <...> |
| HST | <...> | <...> | <...> | <...> | <...> |

### Predictive Facies Model

**Updip (paleohigh, structural high):**
<expected facies, thickness, geometry in areas of high accommodation, low accommodation>

**Downdip (paleoslope, basin center):**
<expected facies, thickness, geometry; sand/shale distribution>

**Trap geometry and charge pathway:**
<predicted location and geometry of sand bodies; source rock position relative to sequence>

### Confidence
<high | medium | low> — <justification: e.g., "high — all surfaces tied to biostratigraphy and verified across 8 wells spanning 80 km" or "medium — MFS identified by log correlation only; no core or seismic calibration available">
```
