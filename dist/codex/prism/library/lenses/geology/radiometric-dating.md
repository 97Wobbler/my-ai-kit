---
name: radiometric-dating
display_name: Radiometric Dating
class: lens
underlying_class: native
domain: geology
source: Rutherford and Soddy (1902); standardized methods in Faure (2nd ed., 1986) and McDougall & Harrison (1999)
best_for:
  - Establishing absolute ages of rock and mineral samples
  - Constraining geological timescales and depositional sequences
  - Validating relative dating frameworks with numeric calibration
one_liner: "Determine absolute rock age via radioactive decay curves."
---

# Radiometric Dating

## Overview
Radiometric dating measures the decay of unstable isotopes in minerals and rocks to assign an absolute age in years (or millions/billions of years). The method rests on three assumptions: the initial isotope ratio is known, the decay rate (half-life) is constant, and the closed system has remained unaltered since mineral crystallization. Practitioners use this lens when relative stratigraphic order is established but numeric calibration is needed, or when dating volcanic ash, basalt flows, or metamorphic minerals that reset their isotopic clocks during thermal events.

## Analytical Procedure

### Phase 1 — Sample Selection and Documentation

1. **Identify the target mineral or rock phase.** Specify which mineral (feldspar, mica, zircon, whole-rock) will be dated and why it is appropriate. Not all minerals retain radiogenic isotopes equally — zircon (U-Pb) is far more resistant to argon loss than plagioclase.

2. **Document the geological context.** Write down:
   - Stratigraphic position and lithology (basalt, granite, ash fall, etc.)
   - Field relationships to dated horizons or paleontological markers
   - Any evidence of post-crystallization heating, weathering, or alteration
   - Location and sample number

3. **Select the isotope system.** Choose based on expected age and mineral composition:
   - **U-Pb (Uranium-Lead):** Zircon, baddeleyite; best for ages >5 Ma; least susceptible to disturbance
   - **K-Ar (Potassium-Argon):** Whole-rock basalt, feldspar, mica; ages 10 ka to 4 Ga; argon may escape during heating
   - **Rb-Sr (Rubidium-Strontium):** Feldspar, biotite; ages >10 Ma; sensitive to alteration
   - **Sm-Nd (Samarium-Neodymium):** Whole-rock, garnet; ages >10 Ma; closed system, less mobile
   - **C-14 (Carbon-14):** Organic matter, carbonate; ages <50 ka; only for Quaternary materials

### Phase 2 — Laboratory Measurement

4. **Measure the parent and daughter isotope concentrations.** Use mass spectrometry (thermal ionization MS, inductively coupled plasma MS, or accelerator MS for C-14) to determine:
   - Amount of parent isotope remaining (e.g., K-40, U-235, U-238, Rb-87)
   - Amount of radiogenic daughter isotope produced (e.g., Ar-40, Pb-207, Sr-87)
   - Ratio of daughter to parent isotope
   - Standard error or uncertainty on each measurement

5. **Measure or assume the initial daughter isotope ratio.** For U-Pb and Rb-Sr, measure the non-radiogenic isotope ratio in the sample. For K-Ar, assume all Ar-40 is radiogenic (atmospheric Ar-40 is negligible in some cases but not all). Document this assumption explicitly.

6. **Apply instrumental corrections.** Account for:
   - Mass fractionation during measurement
   - Blank (machine background) subtraction
   - Decay constant uncertainty (use current IUGS standard values; note that half-lives are known to 0.1–0.5% precision)

### Phase 3 — Age Calculation

7. **Calculate the age using the decay equation.** For a simple system:
   - N(t) = N₀ × e^(−λt), where λ is decay constant, t is time elapsed, N₀ is initial parent, N(t) is parent remaining
   - Rearrange: t = (1/λ) × ln[(N₀ / N(t)) + 1]
   - The daughter/parent ratio can be inverted to solve for t

   For multi-system dating (e.g., U-Pb with U-235 and U-238 both decaying in parallel), use concordia methods: plot the ratio of Pb-207/U-235 against Pb-206/U-238; concordant ages lie on the concordia curve.

8. **Calculate propagated uncertainty.** Combine measurement errors in parent, daughter, and isotope ratios using standard error propagation. Report age ± 1σ (68% confidence) or ± 2σ (95% confidence). For U-Pb concordia, report both concordia age and weighted mean age if concordant.

### Phase 4 — Interpretation and Validation

9. **Check the closed-system assumption.** Examine whether:
   - The mineral phase has remained unheated or unaltered since crystallization (visual inspection, microscopy, microprobe trace elements)
   - Argon loss (for K-Ar) would be expected given burial depth and thermal history
   - Pb loss (for U-Pb) would alter the ratio (common in surface samples, uncommon in fresh zircon)
   - Whole-rock isochron plots align (for Rb-Sr and Sm-Nd)

   If the sample shows evidence of argon diffusion, radiation damage, or chemical alteration, flag it as potentially disturbed.

10. **Compare ages from multiple mineral phases or isotope systems in the same sample.** If zircon and feldspar from the same granite yield concordant K-Ar and U-Pb ages, confidence rises. If they differ by >10%, investigate: different closure temperatures (zircon closes ~900 K, feldspar ~500 K), resetting of one phase, or analytical error.

11. **Place the age in stratigraphic and paleontological context.** Does the radiometric age agree with the relative age inferred from fossils or superposition? If a dated volcanic ash in a sedimentary sequence is younger than underlying fossils, or older than overlying fossils, either:
    - The sample was recycled (reworked ash incorporated from an older unit — common in fluvial settings)
    - The age is spurious (contamination, open-system behavior)
    - The fossil correlation is wrong

12. **Estimate the closure temperature for the dating system.** This is the temperature below which the mineral retains daughter isotope product. K-Ar in feldspar closes ~500 K; U-Pb in zircon closes ~900 K. If the sample cooled slowly, the age records cooling rather than crystallization. Combine with thermochronologic constraints (apatite fission track, (U-Th)/He) if available.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Sample location, lithology, and stratigraphic context documented | Y/N |
| Mineral phase and isotope system chosen are appropriate for expected age range | Y/N |
| Parent and daughter isotope concentrations measured with <5% analytical error | Y/N |
| Initial daughter isotope ratio stated (measured or assumed) | Y/N |
| Decay constant used is current IUGS standard (or justification given if not) | Y/N |
| Age calculated with propagated uncertainty reported as ±σ | Y/N |
| Closed-system assumption evaluated (not assumed) | Y/N |
| Age compared to other mineral phases or isotope systems from same sample | Y/N |
| Radiometric age reconciled with stratigraphic/paleontological constraints | Y/N |
| Closure temperature context noted for interpretation | Y/N |

## Red Flags

- Decay constant is outdated or non-standard. Age uncertainty cannot be estimated without it.
- Initial daughter isotope ratio is unknown or assumed without justification. For U-Pb, unmeasured initial Pb ratios introduce 1–5 Ma scatter in Archean samples.
- No error bars or uncertainty on age. A single number ("342 Ma") without ±σ is not a measurement.
- Sample shows visible alteration (weathering, staining, veining) under the microscope but is dated anyway. Alteration may open the system to isotope loss or gain.
- Age contradicts fossils or field superposition by >10%, but no reworking, contamination, or resetting is addressed. Either the age is wrong or the stratigraphic interpretation is.
- All mineral phases in a sample yield identical ages. If zircon, feldspar, and biotite all agree, either they cooled together (plausible) or one or more closed systems were violated and the ages are erroneously concordant (less common but possible in high-strain zones).
- C-14 age on material >50 ka. Half-life of C-14 is 5,730 yr; beyond ~10 half-lives, activity is unmeasurable by decay counting. Radiocarbon dating of very old samples requires exceptional care and is often unreliable.

## Output Format

```
## Radiometric Dating Assessment

**Sample identification:**
- Location: <lat, long, locality name>
- Lithology: <rock type>
- Stratigraphic context: <unit, position relative to markers>

**Dating parameters:**
- Mineral phase: <zircon, feldspar, whole-rock, etc.>
- Isotope system: <U-Pb, K-Ar, Rb-Sr, Sm-Nd, C-14>
- Parent isotope measured: <X> with error <±%>
- Daughter isotope measured: <Y> with error <±%>
- Initial daughter ratio: <measured / assumed>, justification: <reason>
- Decay constant (λ): <value>, reference: <citation>

**Age calculation:**
- Calculated age: <X> Ma (or ka, Ga as appropriate)
- ±1σ uncertainty: <±Y>
- ±2σ uncertainty: <±2Y>
- Method: <simple age equation / concordia / isochron regression>

**Closed-system assessment:**
- Visual alteration: <none / minor / severe>
- Cooling history: <rapid / slow>, closure temperature ≈ <K>
- Comparison to other phases: <mineral, age, agreement Y/N>
- Evidence of post-crystallization disturbance: <none observed / possible argon loss / Pb loss / heating event>

**Stratigraphic validation:**
- Relative age (fossils, superposition): <younger / same / older> than radiometric age
- Agreement: <concordant / discordant / unexplained>
- Interpretation: <primary crystallization / cooling age / inheritance / reworking / resetting>

**Confidence
<high/medium/low> — <justification: closed system secure, concordant with other data, stratigraphically consistent, etc. — or — weak: open-system evidence, isolated analysis, stratigraphic conflict>
```
---
