---
name: hr-diagram
display_name: HR Diagram
class: lens
underlying_class: native
domain: astronomy
source: Ejnar Hertzsprung (1911) and Henry Norris Russell (1913)
best_for:
  - Classifying stars by their physical properties
  - Identifying stellar evolutionary stages
  - Predicting stellar lifespans and fates
one_liner: "Classify stellar evolution stages and properties via the luminosity-temperature relation."
---

# HR Diagram

## Overview
The Hertzsprung-Russell diagram plots stars by two observables — absolute brightness (luminosity) on the vertical axis and surface temperature (spectral class) on the horizontal axis — to reveal the underlying physical states and evolutionary paths of stars. Most stars cluster into predictable regions (the main sequence, giants, white dwarfs) that expose the link between mass, age, and fate. Practitioners use it to infer a star's internal composition, remaining fuel, and ultimate destiny without direct observation, and to anchor stellar populations within galactic and cosmic timescales.

## Analytical Procedure

### Phase 1 — Data Collection and Transformation

1. **Obtain the star's apparent magnitude (m) and distance (d in parsecs).** Gather from catalogs (Gaia, Hipparcos, etc.) or measure via parallax. If distance is unavailable, note the star as unclassifiable on the diagram; do not interpolate.

2. **Calculate absolute magnitude (M).** Apply the distance modulus formula:
   $$M = m - 5 \log_{10}(d) + 5$$
   This normalizes brightness to a standard reference distance (10 pc).

3. **Convert absolute magnitude to luminosity (L in solar units).** Use:
   $$\log_{10}(L/L_{\odot}) = -0.4(M - M_{\odot})$$
   where $M_{\odot} = 4.83$. Plot this on the vertical axis (logarithmic scale, brightest at top).

4. **Obtain the star's effective surface temperature (T in Kelvin).** Measure from spectral type (O, B, A, F, G, K, M) using standard calibration tables, or derive from broadband photometry (color indices) using color-temperature relations. Typical ranges: O-stars ~30,000 K, M-stars ~3,000 K.

5. **Convert temperature to spectral class or color index if only one is available.** Plot temperature on the horizontal axis (decreasing left to right; hottest stars on the left). Use a logarithmic scale if spanning >1000 K range.

### Phase 2 — Positioning and Regional Classification

6. **Mark each star on the diagram** using (T, L) coordinates. Use distinct symbols if comparing multiple populations (clusters, galaxies).

7. **Identify the region each star occupies.** Cross-reference with the standard HR diagram template:
   - **Main Sequence** (diagonal band, lower-left to upper-right): ~90% of stars, fusing hydrogen in the core. Tighter on this band = more uniform properties.
   - **Giant Branch** (upper-right): Cool, highly luminous stars; thin outer envelope, inert core. Red Giants (RGB) and Asymptotic Giant Branch (AGB) stars.
   - **White Dwarf region** (lower-left): Hot, dim remnants; no fusion; cooling slowly. Typically < 0.01 $L_{\odot}$.
   - **Supergiant region** (upper-left): Rare, very luminous, short-lived. Hot supergiants (blue) or cool supergiants (red).
   - **Subdwarfs** (below main sequence): Metal-poor, older Population II stars.

8. **For each star, estimate its mass and age range** using standard models:
   - Main Sequence luminosity correlates with mass (~$L \propto M^{3.5}$). Use published mass-luminosity relations.
   - Position on main sequence approximates age: upper-left = young, lower-right = old (age depends on mass and evolutionary stage).
   - Giants have exhausted core hydrogen; red giants are typically billions of years old.

### Phase 3 — Population and Evolutionary Inference

9. **If multiple stars are plotted (cluster, galaxy), examine the distribution:**
   - Clustered main sequence with short upper envelope → young, coeval population (age = turn-off point age).
   - Main sequence extending to low luminosity only → old population.
   - Populated giant branches → intermediate age.
   - All regions populated → composite population (multiple ages).

10. **Estimate the age of a star cluster** using the "main sequence turn-off" method: the luminosity at which stars have just exhausted core hydrogen. Cross-reference with isochrones (evolutionary tracks of constant age) to read the cluster's age in Gyr.

11. **Infer the endpoint** of each star's evolution:
    - Main Sequence stars < 0.5 $M_{\odot}$ → Red Dwarf, then White Dwarf (after many Gyr).
    - Main Sequence stars 0.5–8 $M_{\odot}$ → Red Giant, then White Dwarf.
    - Main Sequence stars 8–20 $M_{\odot}$ → Red Supergiant, then Core-Collapse Supernova, Neutron Star.
    - Main Sequence stars > 20 $M_{\odot}$ → Blue Supergiant, then Core-Collapse Supernova, Black Hole or Neutron Star.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Distance data (or parallax) provided for each star, or absence noted | Y/N |
| Absolute magnitude (M) or luminosity (L) calculated from apparent magnitude and distance | Y/N |
| Effective temperature (T) measured or derived from spectral type or color | Y/N |
| Each star positioned on diagram with correct axes (L vertical, T horizontal, decreasing right) | Y/N |
| Regional classification assigned (Main Seq, Giant, White Dwarf, etc.) for each star | Y/N |
| For clusters: turn-off point identified and cross-referenced with isochrone model | Y/N |
| Mass and age estimates provided with justification (e.g., mass-luminosity relation, isochrone) | Y/N |

## Red Flags

- Temperature and luminosity are plotted but distance is missing or unknown; star cannot be placed reliably without absolute magnitude.
- Stars plotted at spectral class (B, A, F, etc.) instead of numerical temperature; loss of quantitative power.
- Multiple stars clustered in a narrow region of the diagram with no age spread; either a genuine coeval population (acceptable) or improper uncertainty handling (suspect).
- Estimated age of a main-sequence star is shorter than the main-sequence lifetime at its mass (e.g., a 1 $M_{\odot}$ star called "10 Gyr old" when its total MS life is ~10 Gyr — timing OK, but confidence should be low).
- White dwarf region populated but no mention of cooling models or age estimates; white dwarf ages require additional data (cooling rate, composition).
- No isochrones or theoretical models cited; diagram becomes a taxonomic tool without predictive power.

## Output Format

```
## HR Diagram Analysis

**Population / Object:**
<name of star, cluster, or sample>

### Data Summary
| Star | Distance (pc) | Apparent Mag | Absolute Mag | Temperature (K) | Luminosity ($L_{\odot}$) |
|---|---|---|---|---|---|
| <name> | <value> | <value> | <value> | <value> | <value> |

### Positioning and Regional Classification
| Star | Region | Estimated Mass ($M_{\odot}$) | Evolutionary Stage | Remarks |
|---|---|---|---|---|
| <name> | Main Seq / Giant / WD / Supergiant | <range> | <core H burning / core He burning / white dwarf / etc.> | <e.g., young, metal-poor, ...> |

### Population Age and Composition
- **Cluster Age (if applicable):** <age in Gyr, or range>
- **Turn-off point:** <luminosity, mass, or spectral type>
- **Population type:** <coeval / composite / old halo / young disk / ...>
- **Key isochrone(s):** <model and age>

### Evolutionary Endpoint Forecast
| Star | Final State | Timescale to Endpoint |
|---|---|---|
| <name> | White Dwarf / Neutron Star / Black Hole / Red Dwarf | <Gyr, or "ongoing"> |

### Confidence
<high | medium | low> — <justification. E.g., "high: Gaia parallax, coeval cluster with tight isochrone fit"; "medium: spectral type estimated from photometry, age depends on model choice"; "low: distance uncertain, no distance modulus applied">
```
