---
name: structural-geology
display_name: Structural Geology
class: lens
underlying_class: native
domain: geology
source: Turner & Weiss (Structural Analysis of Metamorphic Tectonites, 1963); modernized framework in Passchier & Trouw (Microtectonics, 2005)
best_for:
  - Deciphering deformation history from fold and fault geometry
  - Reconstructing strain magnitude and stress orientation in rock bodies
  - Distinguishing syn-kinematic from post-kinematic structures
one_liner: "Reconstruct crustal stress fields and deformation history from the geometry and kinematics of rock deformation."
---

# Structural Geology

## Overview
Structural geology reconstructs the motion history of rock masses by reading the geometric and kinematic signals encoded in folds, faults, and mineral fabrics. Rather than inferring stress from surface earthquakes or modeled loads, practitioners extract strain magnitude (how much the rock was squeezed or stretched) and stress direction (which way the force pointed) directly from deformed rock bodies. The discipline is pattern recognition: a fold's limb dip, an offset mineral lineation, a slickenline striation all point to a specific moment in deformation. Practitioners use this when they need to know not just that a region deformed, but *how*, *when*, and *in what order*.

## Analytical Procedure

### Phase 1 — Geometric Survey

1. **Map the structural elements in the outcrop or section.** For each visible structure, record:
   - **Type:** fold, fault, shear zone, or foliation (list all four even if only one is present)
   - **Orientation:** strike and dip (or plunge and trend) of the structure itself, not the rock layers
   - **Sense of shear (if applicable):** dextral/sinistral for faults; Z-fold vs S-fold for folds
   - **Relative age:** which structure cuts which (cross-cutting relationships)

   Use a stereonet (equal-area projection) to plot all orientations. Do not skip structures that seem "small" — minor faults and foliation kinks often reveal the strain field more clearly than large folds.

2. **Identify the foliation and lineation pair.** Every deformed rock has a preferred orientation:
   - **Foliation:** the planar fabric (e.g., metamorphic banding, cleavage, bedding)
   - **Lineation:** the linear fabric (e.g., mineral alignment, fold axis, stretching direction)
   
   On a stereonet, plot foliation as a great circle and lineation as a point. The angle between them constrains the deformation style (see Phase 2).

3. **For each fault, measure slickenline striation and measure or infer the slip vector.** The striation direction shows the direction of motion, not necessarily the sense. Use the surrounding rock geometry (displaced markers, asymmetric pressure shadows) to assign sense. Record:
   - Angle between striation and fold axis
   - Sense (arrows on the fault surface or inferred from dip-slip vs strike-slip displacement)

4. **Document any syn-kinematic indicators.** These structures formed *during* deformation and are therefore markers of when that deformation happened:
   - Minerals that grew while shearing (check for bent or kinked crystal faces)
   - Foliation curves that spiral into fault surfaces (drag folds)
   - Porphyroblasts with internal foliation different from external foliation (rotated during growth)
   
   Mark these explicitly — they are temporal anchors.

### Phase 2 — Strain and Stress Interpretation

5. **Estimate strain magnitude from fold geometry.** Use one or more of these methods:
   - **Interlimb angle:** Tight folds (≤30° between limbs) imply higher strain than open folds (>90°)
   - **Axial plane angle:** If the fold is asymmetric, measure the acute angle between the two limbs' dips; deviation from 180° tracks progressive shortening
   - **Aspect ratio (length:thickness) of folded layers:** A layer shortened to 1/3 its original thickness shows ~66% strain

   For faults, estimate displacement using offset of recognizable markers (veins, contacts, fossiliferous beds). Displacement magnitude divided by fault length gives a rough strain estimate for that structure.

6. **Infer the strain ellipsoid from the foliation-lineation pair.** On a stereonet:
   - The lineation points in the direction of *maximum stretching* (the long axis of the strain ellipsoid)
   - The foliation is perpendicular to the direction of *maximum shortening* (the short axis)
   - The intermediate axis is perpendicular to both
   
   This three-axis model tells you whether deformation was dominated by shortening (flattening) or stretching (constriction). Check: do folds have their axes parallel to the lineation? (They usually do.)

7. **Extract the stress direction from fault geometry and subsidiary structures.** Use the four-quadrant method:
   - On a stereonet, plot the fault plane as a great circle and the slip vector as a point on that circle
   - Bisect the acute angle between the two principal stresses — this bisector should point toward the slip direction (or opposite to it)
   - Stress axes are perpendicular and parallel to the fault; the largest (σ₁) points toward the hanging wall if the fault is a thrust
   
   Compare this inferred stress direction to the strain directions from Phase 2, step 6. Do they align? If not, the deformation may have occurred in two phases, or the stress field rotated during deformation.

### Phase 3 — Temporal Sequence and Kinematics

8. **Establish a relative chronology using cross-cutting and syn-kinematic relationships.** Create a table:

   | Structure | Age Relative to Others | Syn-kinematic? | Timing Anchor |
   |---|---|---|---|
   | Foliation A | Earlier | No | Bedding pre-dates it |
   | Fault B | Later | Yes | Fault grew during foliation A |
   | Fold C | Latest | No | Folds both A and B |

   Younger structures cut older ones. Syn-kinematic structures date the deformation that created them.

9. **Identify kinematic phases.** Group structures by similar stress orientation and deformation style:
   - **Phase 1:** all structures indicating shortening from the same direction (e.g., north-south compression)
   - **Phase 2:** a later set of structures indicating rotation or new stress (e.g., east-west extension)
   
   Do not assume only two phases exist. Some deformed terranes record four or more kinematic events. Look for evidence: do younger structures systematically reorient older ones? Do fault striations change direction?

10. **Link each kinematic phase to a tectonic context.** Using your relative chronology and the stress/strain directions:
    - Is there evidence of collision (coaxial shortening, thickened crust)?
    - Is there evidence of rifting (biaxial extension, normal faults)?
    - Is there evidence of strike-slip motion (simple shear, offset markers)?
    
    Each context produces characteristic fault angles, fold orientations, and lineation trends. Mismatch here signals either data error or an unexpected tectonic event.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All structural elements (fold, fault, foliation, lineation) were inventoried | Y/N |
| Every element was oriented and plotted on stereonet | Y/N |
| At least one syn-kinematic indicator was identified and dated | Y/N |
| Strain magnitude was estimated using at least one quantitative method | Y/N |
| Stress direction was inferred using fault geometry and slip vector | Y/N |
| Stress direction aligns with strain direction (or misalignment is noted) | Y/N |
| A relative chronology was established with at least two phases | Y/N |
| Each phase is linked to a tectonic context (collision, rifting, or strike-slip) | Y/N |

## Red Flags

- All folds are the same size and symmetry, all faults have the same angle. Sampling bias — you are missing the smaller structures that often drive the kinematic story.
- Foliation and lineation are parallel or perpendicular. This is geologically unlikely and usually indicates measurement error. Re-measure or re-check the stereonet plot.
- Strain magnitude and stress direction point in opposite directions (e.g., maximum strain to the north, maximum compression to the west). This is possible but rare — it implies the stress field rotated during deformation. If you see it, slow down and verify the data.
- No syn-kinematic structures identified. Without temporal anchors, you cannot distinguish structures that formed together from structures that formed millions of years apart. The relative chronology collapses.
- Only one kinematic phase. Complex terranes rarely show a single deformation event. If everything points to one phase, either the terrane is genuinely young and simple (possible) or you have lumped structures of different ages (common).
- Tectonic context assigned without evidence. "This must be collision-related" is speculation. Only assign a context if the stress/strain indicators match known patterns for that regime.

## Output Format

```
## Structural Geology Assessment

### Phase 1 — Geometric Inventory
| Structure | Type | Strike/Dip | Sense/Orientation | Syn-kinematic? |
|---|---|---|---|---|
| <...> | fold/fault/foliation/lineation | <...>° | <...> | Y/N |

### Phase 2 — Strain and Stress
**Strain magnitude estimate:**
- Method: <aspect ratio / interlimb angle / displacement>
- Result: <% shortening or extension>

**Strain ellipsoid:**
- Maximum extension direction: <plunge/trend>
- Maximum shortening direction: <plunge/trend>
- Deformation style: <flattening / constriction / coaxial>

**Stress direction (inferred):**
- σ₁ (maximum compression): <plunge/trend>
- σ₃ (maximum extension): <plunge/trend>
- Alignment with strain: <yes / no — explain misalignment>

### Phase 3 — Kinematic History

**Relative chronology:**
| Phase | Key structures | Age order | Stress regime | Tectonic context |
|---|---|---|---|---|
| 1 | <...> | <...> | <...> | collision / rifting / strike-slip |
| 2 | <...> | <...> | <...> | <...> |

**Evidence for each phase:**
- Phase 1: <cross-cutting, syn-kinematic, or other relationship>
- Phase 2: <...>

**Confidence**
<high/medium/low> — <justification based on:
  - density and consistency of structural data
  - clarity of syn-kinematic indicators
  - alignment of stress and strain
  - robustness of relative chronology>
```
---
