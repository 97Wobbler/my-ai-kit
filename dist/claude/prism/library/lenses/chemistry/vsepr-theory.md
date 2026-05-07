---
name: vsepr-theory
display_name: VSEPR Theory
class: lens
underlying_class: native
domain: chemistry
source: Ronald Gillespie and Ronald Nyholm, 1957
best_for:
  - Predicting molecular geometry from electron-pair repulsion
  - Explaining bond angles and molecular shape
  - Rationalizing chemical reactivity based on steric arrangement
one_liner: "Predict molecular geometry from valence shell electron-pair repulsion."
---

# VSEPR Theory

## Overview
Valence Shell Electron Pair Repulsion (VSEPR) Theory predicts the three-dimensional shape of a molecule by minimizing electrostatic repulsion between electron pairs (bonding and non-bonding) around a central atom. The artifact is a molecular structure or Lewis dot formula; the lens systematically applies electron-pair geometry rules to infer the actual spatial arrangement and resulting bond angles. Practitioners use this when needing to explain or predict molecular shape, polarity, reactivity, or spectroscopic properties without computational methods.

## Analytical Procedure

### Step 1 — Parse the Lewis Structure

1. **Identify the central atom.** This is the atom with the lowest electronegativity (usually not hydrogen or halogen). If multiple atoms are candidates, select the one bonded to the most other atoms.

2. **Count valence electrons on the central atom.** Use the group number (main group) or standard rules (transition metals). Write down the number.

3. **Determine bonding pairs.** Count the number of bonds (single = 1 pair, double = 2 pairs, triple = 3 pairs) to all neighboring atoms. Record as a count.

4. **Calculate lone pairs.** Lone pairs = (valence electrons − bonding electrons) ÷ 2. Round down if the result suggests fractional pairs; this indicates an error in the Lewis structure. Record as a count.

5. **Sum electron groups.** Total electron groups = bonding pairs + lone pairs. This total determines the electron-pair geometry (step 3 below).

### Step 2 — Apply Electron-Pair Geometry

6. **Match electron-group count to geometry type:**
   - 2 groups → linear
   - 3 groups → trigonal planar
   - 4 groups → tetrahedral
   - 5 groups → trigonal bipyramidal
   - 6 groups → octahedral

   Write the electron-pair geometry explicitly.

7. **Apply the repulsion hierarchy.** Rank repulsion strength:
   - Lone pair–lone pair (strongest)
   - Lone pair–bonding pair (medium)
   - Bonding pair–bonding pair (weakest)

   This hierarchy is used to determine positions in step 4 below.

### Step 3 — Determine Molecular Geometry

8. **Subtract lone pairs from electron-pair geometry.** The molecular geometry is the spatial arrangement of *atoms only* (not electron pairs). Use the repulsion hierarchy to place lone pairs in positions that minimize their repulsive effect.

   For example:
   - Tetrahedral (4 groups) with 1 lone pair → trigonal pyramidal (3 atoms, 1 lone pair in position that spreads it farthest from bonding pairs)
   - Tetrahedral (4 groups) with 2 lone pairs → bent (2 atoms, 2 lone pairs in equatorial positions)
   - Trigonal bipyramidal (5 groups) with 1 lone pair → seesaw (4 atoms, 1 lone pair in equatorial position)
   - Trigonal bipyramidal (5 groups) with 2 lone pairs → linear (2 atoms, 2 lone pairs in equatorial positions)
   - Octahedral (6 groups) with 1 lone pair → square pyramidal (5 atoms, 1 lone pair opposite one apex)
   - Octahedral (6 groups) with 2 lone pairs → square planar (4 atoms, 2 lone pairs opposite each other)

9. **Name the molecular geometry.** Record the name (e.g., "tetrahedral," "trigonal pyramidal").

### Step 4 — Predict Bond Angles

10. **Use the electron-pair geometry to estimate ideal angles:**
    - Linear: 180°
    - Trigonal planar: 120°
    - Tetrahedral: 109.5°
    - Trigonal bipyramidal: 120° (equatorial-central-equatorial), 90° (axial-central-equatorial)
    - Octahedral: 90°

11. **Apply compression rules.** Lone pairs repel more strongly than bonding pairs, so bond angles involving lone pairs are compressed (smaller than ideal):
    - Each lone pair compresses bonding pair–bonding pair angles by ~2–4°.
    - Lone pair–lone pair repulsion compresses the geometry around the lone pairs.

    For example, ammonia (NH₃) has a tetrahedral electron-pair geometry (ideal 109.5°) but only 3 bonding pairs. The lone pair compresses the H–N–H angles to ~107°.

12. **Record predicted and observed angles.** If experimental data is available, note the difference and attribute it to lone-pair compression or other effects (e.g., electronegativity differences in polar molecules).

### Step 5 — Verify and Explain Properties

13. **Assess molecular polarity.** A molecule is nonpolar if all bond dipoles cancel (symmetric geometry). It is polar if bond dipoles do not cancel (asymmetric geometry or different atoms). Assign polar or nonpolar.

14. **Connect geometry to reactivity.** Note whether the molecular shape allows for steric hindrance, nucleophilic approach, or orbital overlap. This explains selectivity in chemical reactions.

15. **Cross-check with experimental bond angles.** If literature values are available, compare. Deviations >5° may indicate resonance, hypervalency, or other effects beyond simple VSEPR.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Central atom correctly identified | Y/N |
| Valence electron count is correct | Y/N |
| Bonding and lone pair counts match the Lewis structure | Y/N |
| Electron-pair geometry matches the total electron group count | Y/N |
| Molecular geometry correctly subtracts lone pairs and applies repulsion hierarchy | Y/N |
| Bond angles are estimated with lone-pair compression applied | Y/N |
| Polarity assignment (polar/nonpolar) is consistent with geometry | Y/N |

## Red Flags

- Valence electron count does not match the periodic table group. Recalculate or verify the Lewis structure.
- Total electron groups is odd (e.g., 5.5). This indicates a counting error; each pair is an integer.
- Molecular geometry is stated as the same as electron-pair geometry when lone pairs are present. Lone pairs must reduce the geometric name (e.g., "tetrahedral with 1 lone pair" should be "trigonal pyramidal," not "tetrahedral").
- Bond angles are all stated as ideal values with no compression. If lone pairs are present, angles should deviate from ideals.
- Polarity is assigned as "nonpolar" for an asymmetric geometry (e.g., trigonal pyramidal NH₃ is polar, not nonpolar).
- Experimental bond angles differ by >8° from predictions without explanation. Consider resonance, electronegativity effects, or hypervalency.

## Output Format

```
## VSEPR Analysis

**Molecule:** <formula>

### Electron-Pair Geometry
- Central atom: <atom>
- Valence electrons: <number>
- Bonding pairs: <number>
- Lone pairs: <number>
- Total electron groups: <number>
- **Electron-pair geometry:** <name>

### Molecular Geometry
- **Geometry:** <name>
- **Geometry sketch:**
  ```
  <ASCII or textual description of 3D arrangement>
  ```

### Bond Angles
| Bond | Ideal angle | Predicted angle | Experimental angle | Deviation |
|---|---|---|---|---|
| <atom>–<central>–<atom> | <>° | <>° | <>° | <>° |

### Molecular Polarity
- **Polarity:** <polar | nonpolar>
- **Justification:** <whether bond dipoles cancel or reinforce>

### Reactivity Implications
- <steric or electronic property affecting reactivity>

### Confidence
<high | medium | low> — <Because the Lewis structure is unambiguous and VSEPR rules are deterministic, confidence is high. Confidence is medium if experimental bond angles deviate significantly from predictions, indicating additional effects not captured by simple repulsion. Confidence is low if the Lewis structure is uncertain (e.g., resonance structures, formal charges ambiguous).>
```
---
