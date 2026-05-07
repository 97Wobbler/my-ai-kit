---
name: habitable-zone-analysis
display_name: Habitable Zone Analysis
class: lens
underlying_class: native
domain: astronomy
source: Kasting, Whitmire, Ray (1993); refined by Kopparapu et al. (2013)
best_for:
  - Assessing whether an exoplanet could sustain liquid water
  - Evaluating stellar habitability for biosignature searches
  - Constraining system-wide orbital parameters for life-bearing planets
one_liner: "Define and test the orbital range around a star where liquid water can exist."
---

# Habitable Zone Analysis

## Overview

The habitable zone (HZ) is the range of orbital distances around a star where a rocky planet with an appropriate atmosphere could maintain liquid water on its surface. This lens operationalizes the concept by translating stellar properties into concrete orbital bounds and evaluating whether a candidate exoplanet falls within them. Practitioners apply this when screening exoplanet candidates for biosignature observations or when modeling which planets in a multi-body system could plausibly harbor life.

## Analytical Procedure

### Phase 1 — Establish Stellar Properties

1. **Obtain the star's effective temperature (T_eff).** Use spectroscopic classification or direct measurement. If unavailable, estimate from color index (B-V) using a standard calibration table. Record the uncertainty (±K).

2. **Measure or estimate the star's luminosity (L_★).** Preferred: direct parallax + flux measurement. Alternative: Use the Stefan-Boltzmann relation L = 4πR²σT_eff⁴ if radius and temperature are known. Record in solar luminosities (L_☉). Uncertainty should be ±5–10%.

3. **Verify the star is on the main sequence** (for single-star HZ calculations). If it is a red giant, subgiant, or binary, note this — the HZ calculation method may differ. Record the star's age if available (affects HZ width for young systems with reduced atmospheric escape).

### Phase 2 — Calculate HZ Boundaries

4. **Choose the HZ model.** The field uses two standard models:
   - **Conservative HZ**: Inner boundary where a runaway greenhouse begins (water vapor photolysis); outer boundary where CO₂ freezes out. Use this if uncertainty tolerates a narrower zone.
   - **Optimistic (Extended) HZ**: Inner boundary assumes a high-albedo planet or partial CO₂ cloudiness; outer boundary includes subsurface habitability or transient liquid water. Use this if looking for marginal candidates.
   Record which model you chose and why.

5. **Apply the empirical boundary formulas** (Kopparapu et al. 2013 or updated coefficients):
   - **Inner boundary:** d_inner = √(L_★ / S_inner), where S_inner is the solar constant for HZ inner edge (≈1.077 W/m² for conservative; ≈1.107 W/m² for optimistic).
   - **Outer boundary:** d_outer = √(L_★ / S_outer), where S_outer ≈ 0.322 W/m² (conservative) or ≈ 0.356 W/m² (optimistic).
   - If T_eff differs significantly from 5778 K (Sun), apply the polynomial correction factor for stellar temperature. Record the coefficients used.
   
   Result: two AU distances defining the HZ.

6. **Calculate absolute errors.** Propagate uncertainties from L_★ and T_eff through the boundary equations. Report ±AU on each boundary.

### Phase 3 — Evaluate Candidate Planet

7. **Obtain the planet's orbital semi-major axis (a).** From radial velocity, transit timing, or direct imaging. Record in AU and include measurement uncertainty.

8. **Check containment.** Does a fall within [d_inner, d_outer]?
   - If yes: planet is **in the HZ**. Note how far from the center (in AU and as a percentage of zone width).
   - If no: planet is **outside the HZ**. Record which boundary it exceeds and by how much. Note whether it is in the "hot inner region" or "cold outer region."

9. **Assess habitability constraints beyond orbital position.** (These do NOT change HZ membership but inform likelihood of actual habitability):
   - **Atmosphere retention:** Is the planet's escape velocity (from mass + radius) sufficient to retain a thick atmosphere at its equilibrium temperature? Hydrogen escapes readily; nitrogen and oxygen are retained at most HZ locations.
   - **Tidal locking:** Is the orbital period short enough that the planet is tidally locked to the star? (If a < ~0.1 AU and M_planet is Earth-like, likely yes.) Tidal locking does not exclude habitability but concentrates liquid water regionally.
   - **Stellar stability:** Is the star variable (flare stars, long-period variables)? Extreme variability can destabilize atmospheres.
   - **System age:** Is the system young enough that planets retain primordial atmospheres, or old enough for long-term biological evolution? (Age constraints apply separately from HZ position.)

### Phase 4 — Synthesize the Verdict

10. **Produce a habitability summary.** Distinguish between:
    - **Orbital habitability**: Is the planet in the HZ? Yes/No, with quantitative margin.
    - **Conditional habitability**: Is the planet's mass, composition, and age consistent with retaining a life-supporting atmosphere? (Often uncertain for exoplanets.)
    - **Observational priority**: Does the planet merit biosignature observation? Rank among candidates by combination of HZ position (tighter constraints = higher priority) and observability (brightness, transit depth, etc.).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Star's effective temperature is documented with uncertainty | Y/N |
| Star's luminosity is documented and sourced (measurement or estimation method noted) | Y/N |
| HZ model (conservative or optimistic) is selected and justified | Y/N |
| Inner and outer HZ boundaries are calculated with propagated errors | Y/N |
| Planet's orbital semi-major axis is obtained with measurement uncertainty | Y/N |
| Containment check explicitly answers whether planet is in, inside, or outside HZ | Y/N |
| Tidal locking, atmosphere retention, and stellar stability are assessed | Y/N |
| Habitability summary distinguishes orbital vs. conditional habitability | Y/N |

## Red Flags

- **No luminosity error bar.** Habitability conclusions are sensitive to L_★; an unquantified uncertainty makes the verdict unreliable.
- **HZ boundaries calculated without temperature correction.** If T_eff ≠ 5778 K and no polynomial adjustment is applied, the boundaries are systematically biased.
- **Planet containment reported vaguely** (e.g., "probably in the HZ" without numbers). Record the numerical margin: the planet is X AU from the nearest boundary.
- **Tidal locking or atmosphere loss noted but not integrated into the verdict.** If the planet is in the HZ but tidally locked or too light to retain an atmosphere, the conditional habitability is low — the summary must say so.
- **HZ calculation uses outdated coefficients** (pre-2013). The Kopparapu formulas are the community standard; older Kasting coefficients are less accurate for T_eff > 4000 K.
- **No acknowledgment of the "Habitable Zone Paradox"** (faint young Sun, but early Earth was warm). If the system is young or the star is in an unusual evolutionary state, note that the static HZ snapshot may not capture transient habitability.

## Output Format

```
## Habitable Zone Assessment

### Stellar Parameters
- Effective temperature: _____ K (±_____ K)
- Luminosity: _____ L_☉ (±__%)
- HZ Model: [Conservative | Optimistic]
- Justification for model choice: _____

### HZ Boundaries
- Inner boundary: _____ AU (±_____ AU)
  - Derivation: √(L_★ / S_inner) with T_eff correction applied [Y|N]
- Outer boundary: _____ AU (±_____ AU)
  - Derivation: √(L_★ / S_outer) with T_eff correction applied [Y|N]
- HZ width: _____ AU

### Planet Assessment
- Orbital semi-major axis: _____ AU (±_____ AU)
- **Containment verdict**: [In HZ | Inside (too hot) | Outside (too cold)]
- Margin from nearest boundary: _____ AU

### Habitability Constraints
| Factor | Status | Notes |
|---|---|---|
| Tidal locking | [Yes/No/Likely] | Orbital period _____ ; lock threshold ~0.1 AU for Earth-like |
| Atmosphere retention | [Likely/Marginal/Unlikely] | Escape velocity vs. RMS velocity at HZ equilibrium temp |
| Stellar variability | [Stable/Moderate/High] | Type: _____ |
| System age | _____ Gyr | Sufficient for abiogenesis? [Yes/No/Unknown] |

### Habitability Summary
- **Orbital habitability**: Planet [is / is not] in the HZ.
- **Conditional habitability**: Given mass, radius, and stellar context, atmosphere retention is [likely / marginal / unlikely].
- **Overall assessment**: This planet [merits / does not merit] biosignature observation within this survey. Rank among candidates: [#1 / #2 / ...].

### Confidence
[High | Medium | Low] — <justification: e.g., "High: L_★ measured to ±3%, planet mass/radius constrained, no tidal locking.">
```
