---
name: stereonet-analysis
display_name: Stereonet Analysis
class: lens
underlying_class: native
domain: geology
source: Wulff (1902); Schmidt (1924); modern structural geology practice standardized in 1960s–present
best_for:
  - Analyzing orientations of planar and linear features in rock
  - Identifying fold axes, fault planes, and fracture sets
  - Detecting structural patterns and kinematic indicators
one_liner: "Quantify planar and linear rock structures via spherical projection to extract geometric patterns."
---

# Stereonet Analysis

## Overview

A stereonet is a circular projection of a sphere (typically the lower hemisphere) onto a flat plane, allowing three-dimensional orientations of planar and linear features to be plotted, measured, and analyzed simultaneously. Geologists use stereonets to visualize strike and dip of bedding, foliation, fault planes, and lineations; to detect preferred orientations that indicate stress regimes or kinematic history; and to solve spatial problems (e.g., finding the acute angle between two planes, or the orientation of a pole perpendicular to a plane). The discipline is translating field measurements into stereographic coordinates and reading geometric clusters, concentrations, and girdles.

## Analytical Procedure

### Phase 1 — Data Preparation and Plotting

1. **Collect orientation measurements from the field.** Record strike and dip (or trend and plunge) for each feature. Strike runs horizontally along the feature; dip is the acute angle from horizontal, measured perpendicular to strike. Lineations are described by trend (compass direction of plunge) and plunge (angle below horizontal). Use standard geology notation: strike is 000–180°, dip is 0–90°, trend is 000–360°, plunge is 0–90°.

2. **Select a stereonet projection.** Use **equal-area (Schmidt) projection** for statistical work (density contouring, statistical tests). Use **equal-angle (Wulff) projection** for angular measurements. Most structural geologists default to equal-area. Confirm which your data require.

3. **Plot planes as poles.** A plane is plotted as a single point (pole) perpendicular to it. For each measurement (strike/dip), find the pole by rotating your tracing paper over the stereonet grid until the strike line aligns with a stereonet meridian, then mark the point at a distance from the center equal to 90° minus the dip value. Alternatively, use stereonet software (Stereowin, OpenStereo, Netplotter) to automate this step.

4. **Plot linear features as points.** Lineations (trend/plunge) are plotted directly as points on the stereonet at the position corresponding to their direction and angle of descent.

5. **Document all plotted points.** Record sample ID, feature type (bedding, fault, fracture, lineation), and original field measurement alongside each point. This is essential for later phase revisits.

### Phase 2 — Cluster and Pattern Recognition

6. **Visually scan for clusters.** Look for concentrations of poles in small regions of the stereonet. Tight clusters indicate a preferred orientation (e.g., a single bedding attitude affecting many samples). Scattered distributions indicate variable orientations (e.g., open folds or high strain).

7. **Apply density contouring (if sample size ≥20).** Use equal-area projection software to generate a density contour map. Typical procedure:
   - Divide the stereonet into counting nets (typically 1% area cells).
   - Count poles in each cell.
   - Assign contours at density intervals (e.g., 1%, 2%, 3% per cell).
   - Contours peaking above background indicate clusters; their position reveals the mean attitude.

8. **Identify geometric patterns:**
   - **Single cluster (girdle absent):** Suggests a single dominant attitude or event (e.g., unfolded bedding).
   - **Girdle pattern:** A distribution of poles along a great circle (curve on the stereonet) suggests folding — the girdle axis (center of the curve) is the fold axis.
   - **Bimodal distribution:** Two clusters 180° apart suggest refraction across a competency contrast or two superimposed structures.
   - **Random scatter:** Suggests no preferred orientation, high noise, or need to subset the data (e.g., separate by layer thickness or fault type).

9. **Measure axes and angles if patterns are ambiguous.** Use stereonet grid:
   - To find the mean orientation of a cluster, plot it and estimate its centroid.
   - To find the fold axis from a girdle, draw the best-fit great circle through the poles and find its pole (the axis).
   - To measure the angle between two planes or lineations, plot both and read the angular distance on the net (in degrees of arc).

### Phase 3 — Interpretation and Kinematic Analysis

10. **Relate clusters to structural features.** Assign each cluster a structural interpretation:
    - Is it bedding? (Usually girdles in refolded terranes; single cluster in unfolded areas.)
    - Is it a fault or fracture set? (Compare to known orientations triggered by regional stress.)
    - Is it a lineation? (Does it trend parallel to fold axes or downdip on faults?)

11. **Apply kinematic indicators.** If data include fault striations (slickenlines) or mineral lineations, use the stereonet to deduce slip direction and sense of shear:
    - Plot the fault plane as a pole.
    - Plot the striation (trend/plunge) as a point on the stereonet.
    - The striation must lie on the fault plane (if not, field measurement error or lab miscalculation).
    - The position on the plane relative to dip direction indicates rake angle and slip sense (normal, reverse, or strike-slip).

12. **Compare to stress inversion (optional).** If multiple fault planes with slickenlines are present, use stereonet software (e.g., Fry analysis, Angelier-Mechler method) to invert for the best-fit principal stress orientations (σ1, σ2, σ3). Plot stress axes on the same stereonet for cross-check.

### Phase 4 — Quality Control and Documentation

13. **Check for outliers and errors.** Reexamine any pole far from the main cluster: Is it a measurement error, a different structural generation, or a real outlier worth documenting?

14. **Reproject or subset the data if interpretation requires it.** For example:
    - If different lithologies show different orientations, replot by rock type.
    - If the site has multiple fold generations, plot and analyze each generation separately.
    - If paleomagnetic or other auxiliary data exist, use them to constrain age or kinematics.

15. **Document the stereonet in the final report.** Include:
    - Title and sample source.
    - Total number of measurements and any filtering applied.
    - Projection type (equal-area or equal-angle).
    - Interpretation (fold axis, stress regime, fault family) and confidence.
    - Any overlays (e.g., stress axes, π-poles from refolding).

## Evaluation Criteria

| Check | Pass |
|---|---|
| All field measurements are recorded with strike/dip or trend/plunge | Y/N |
| Projection type (equal-area or equal-angle) is justified for the question asked | Y/N |
| At least 10 plotted points on the stereonet (more for density contouring) | Y/N |
| Clusters and girdles visually identified and described qualitatively | Y/N |
| If sample size ≥20, density contours are applied | Y/N |
| Fold axes, fault families, or stress orientations are explicitly labeled on the plot | Y/N |
| Geometric patterns (single cluster, girdle, bimodal, scatter) are named and linked to structure | Y/N |
| Outliers are examined and explained or removed with justification | Y/N |

## Red Flags

- Plot contains >50% scatter with no clusters or girdles. Either the site is genuinely homogeneous (rare in tectonically active areas) or the data mix unrelated structures (e.g., bedding and unrelated joint sets) — subset and replot.
- A girdle is claimed but no axis is calculated or named. Girdle patterns require you to extract the fold axis; eyeballing a curve is not enough.
- Density contours peak at multiple unrelated positions (>3 separate peaks far apart) without explanation. This usually means different structural generations or lithologies are mixed; separate them and replot.
- Fault striations do not lie on their plotted fault planes. Check field measurements and plotting — if error is real, discard the striation.
- No distinction is made between primary structures (e.g., bedding) and secondary structures (e.g., cleavage). The two often plot at different positions; conflating them corrupts the interpretation.
- Confidence in fold axis or stress direction is stated without having tested it against independent data (e.g., crosscutting relationships, paleomagnetic poles, other fault sets).

## Output Format

```
## Stereonet Analysis Report

**Site/Sample identifier:**
<name, location, rock type>

**Data summary:**
- Total measurements: <N>
- Feature types: <bedding, faults, lineations, etc.>
- Projection: <equal-area (Schmidt) | equal-angle (Wulff)>
- Filtering applied: <none | by lithology | by age | etc.>

### Plotted Clusters and Patterns
| Cluster ID | Pole count | Pattern type | Mean orientation (strike/dip or trend/plunge) | Interpretation |
|---|---|---|---|---|
| 1 | <N> | Single / Girdle / Bimodal / Scatter | <e.g., 045/30> | <e.g., bedding in Fm X> |
| 2 | <N> | ... | ... | ... |

### Girdles and Fold Axes (if present)
| Girdle ID | Pole count | Fold axis (trend/plunge) | Implied fold type | Confidence |
|---|---|---|---|---|
| ... | ... | ... | ... | high/medium/low |

### Fault/Fracture Families (if analyzed)
| Family ID | Mean pole (strike/dip) | Count | Striation trend/rake | Inferred slip | Stress regime |
|---|---|---|---|---|---|
| ... | ... | ... | ... | normal/reverse/sinistral/dextral | ... |

### Kinematic/Stress Interpretation
<Paragraph describing principal stress orientations (σ1, σ2, σ3 if inferred), slip sense, and structural history implied by the stereonet pattern.>

### Outliers and Caveats
<List any data points removed, sites with mixed generations, or assumptions made. E.g., "Sample 5 rejected: 120° from cluster; resampled, no error found — likely pre-fold tilting.">

### Stereonet Image
<Embedded or referenced plot showing all plotted points, contours (if density map), labeled axes, and interpreted structures.>

### Confidence
<high | medium | low> — <Justification based on sample size, cluster tightness, agreement with regional structures, and independent corroboration.>
```
