---
name: light-curve-analysis
display_name: Light Curve Analysis
class: lens
underlying_class: native
domain: astronomy
source: Developed from observational astronomy practice; formalized in variable star photometry (Hipparcos, TESS missions)
best_for:
  - Characterizing periodic and non-periodic brightness variations in stars
  - Detecting exoplanets via transit photometry
  - Identifying stellar activity, pulsations, and eruptions
one_liner: "Decompose brightness versus time to infer the physical properties of a celestial object."
---

# Light Curve Analysis

## Overview
A light curve is a time series of brightness measurements from an astronomical object. Light Curve Analysis decomposes this series into constituent signals—periodic oscillations, long-term trends, noise, and transient events—each linked to a physical mechanism (rotation, pulsation, eclipses, accretion, explosions). Practitioners use this lens to move from raw photometry to physical interpretation: identifying the source of variation, measuring its amplitude and frequency, constraining object parameters (mass, radius, activity state), and assessing data quality. The discipline is systematic decomposition and signal attribution.

## Analytical Procedure

### Phase 1 — Prepare and Validate

1. **Document the observational context.** Record: instrument/telescope, wavelength band(s), exposure time, cadence (time between measurements), observation duration, photometric precision (in magnitudes or fractional flux), and any known systematic errors (atmospheric effects, instrument drift, detector noise).

2. **Inspect the raw light curve.** Plot brightness vs. time. Visually scan for:
   - **Outliers**: Single measurements >3σ from the local median. Mark as potential cosmic rays, satellite trails, or bad pixels.
   - **Gaps**: Intervals with missing data. Record their duration and whether they correlate with instrument state changes.
   - **Trends**: Slow brightness drift over the observation window. Note if it's monotonic, cyclical (daily/seasonal), or step-like.
   - **Noise floor**: Typical scatter in the measurements when the object is not varying intrinsically.

3. **Detrend if necessary.** If the data show instrumental trends (e.g., atmospheric extinction over a night, detector cooling), fit and subtract a low-order polynomial (typically linear or quadratic) to the data outside of known variable regions. Document the polynomial coefficients. Do not over-fit; if detrending removes more variance than it explains, revert.

4. **Normalize to zero mean or unit flux.** Subtract the median brightness (or divide by the mean, depending on convention). This allows comparison across objects and wavelengths.

### Phase 2 — Identify Periodicities

5. **Compute a periodogram.** Use Fourier (FFT or Lomb-Scargle if data are unevenly sampled) or wavelet methods to identify dominant frequencies/periods. If using Lomb-Scargle, set frequency grid to at least 10 points per cycle across the full range from 1/T_obs (where T_obs is total observation time) to the Nyquist frequency (1 / 2Δt, where Δt is median cadence).

6. **Identify peaks in the periodogram.** For each peak:
   - Record its frequency/period and power (amplitude squared or spectral density).
   - Check if it is a harmonic of a lower-frequency peak (e.g., twice the main period). If so, label it as a harmonic and do not count as independent.
   - Assess false-alarm probability: use the peak's power relative to the noise floor (estimated from the periodogram away from strong peaks). A peak is significant if its power exceeds the noise floor by ≥4σ.
   - If multiple periods are present, test for beat frequencies (amplitude modulation). If periods p₁ and p₂ are close, a beat at frequency |1/p₁ − 1/p₂| may emerge.

7. **Assess period stability.** Divide the light curve into 3-5 equal time segments and compute the periodogram for each. Do the dominant periods shift or remain constant? If periods shift, the signal is not strictly periodic (e.g., differential rotation, stochastic variability).

### Phase 3 — Decompose Signal Components

8. **For each significant period, fold the light curve.** Take the period and phase the data by t_phase = (t − t₀) mod P, where P is the period and t₀ is an arbitrary reference time. Plot brightness vs. phase to produce a phase-folded light curve (or phase diagram). If the period is correct, all cycles will overlap coherently and reveal the intrinsic shape.

9. **Measure the amplitude and profile.** For the phase-folded curve:
   - Measure peak-to-peak amplitude: max brightness − min brightness.
   - Describe the shape: sinusoidal, sawtooth, multi-peaked, eclipsing (flat-bottomed dip), or irregular.
   - If applicable (e.g., eclipsing binaries), measure the duration and depth of eclipses.
   - Quantify how well the data scatter around the phase curve using the reduced χ² or RMS deviation.

10. **Identify non-periodic and aperiodic signals.** After subtracting out the phased periodic components, examine residuals. Look for:
    - **Long-term trends**: monotonic drift or multi-cycle sinusoids. Fit a low-order function and measure its amplitude and timescale.
    - **Flares or transients**: sudden, asymmetric brightenings or fadings. Record arrival time, rise time, decay time, and total energy (integrated above the baseline).
    - **Stochastic variations**: red noise or "flickering." Estimate the power spectral density at low frequencies (flicker noise exponent α in P(f) ∝ f^−α).

11. **Attribute each signal to a physical mechanism.** For each identified component, propose a source:
    - Periodic: rotation (spot-modulated), pulsation (radial or non-radial), eclipses (binary), or orbital motion.
    - Trend: magnetic activity cycle, orbital decay, or secular cooling/heating.
    - Flares: magnetic reconnection events (stellar, accretion-related).
    - Stochastic: turbulent accretion, convection, or instrumental noise.

### Phase 4 — Validate and Report

12. **Cross-check with ancillary data.** If available, compare:
    - Period to spectroscopic measurements (e.g., rotation period from Doppler shift, pulsation frequencies from radial velocity).
    - Amplitude to color variations (multiband photometry). Some mechanisms (e.g., starspots) produce color-dependent amplitudes.
    - Timing of flares to contemporaneous X-ray, radio, or spectroscopic observations.

13. **Assess goodness of fit.** Compare the model light curve (sum of all fitted periodic and aperiodic components) to the observed data. Compute the reduced χ² or Akaike information criterion (AIC) to check if model complexity is justified.

14. **Document limitations and caveats.** Note: observational window bias (aliasing if observation duration is comparable to a suspected period), sensitivity to detrending choices, dependence on assumed period for phasing, and any periods that could not be resolved or distinguished.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Observational metadata (instrument, cadence, precision, duration) are recorded | Y/N |
| Raw light curve was visually inspected and outliers/gaps/trends noted | Y/N |
| Periodogram was computed using an appropriate method for the data sampling | Y/N |
| All significant peaks (≥4σ) were identified and tested for harmonics | Y/N |
| Period stability was assessed across multiple time segments | Y/N |
| Phase-folded light curves were produced for each period | Y/N |
| Amplitude, profile shape, and fit quality (χ²) are reported for each periodic component | Y/N |
| Residuals were examined for non-periodic signals (trends, flares, stochastic noise) | Y/N |
| Each signal component was attributed to a plausible physical mechanism | Y/N |
| Results were cross-checked against ancillary data (if available) | Y/N |

## Red Flags

- Periodogram shows a forest of peaks all above the noise floor with no dominant signal. Either the object is genuinely stochastic (legitimate) or the data are noisy and period-finding is unreliable (investigate data quality).
- Phase-folded light curve shows scatter far exceeding the measurement error. Either the period is wrong, the signal is not strictly periodic, or there are unresolved multiple periods.
- A significant period is claimed but was not tested for aliasing or observational window effects. Observation duration equal to a suspect period can create false peaks via spectral leakage.
- Detrending removed more variance than it should have. If the detrended light curve shows unphysical behavior (e.g., a previously smooth object now has sharp features), the detrending polynomial was over-fit.
- A signal was attributed to a mechanism without ruling out alternatives. For example, a period could come from rotation *or* pulsation *or* an orbital companion. Ambiguity should be stated.
- Reduced χ² >> 1 on the phased light curve. This indicates either underestimated uncertainties, unresolved sub-periods, or a genuinely incoherent signal. Do not report results as "periodic" if fit quality is poor.

## Output Format

```
## Light Curve Analysis Report

**Object:** <name/designation>
**Instrument/Band:** <telescope, filter, cadence, duration>
**Photometric precision:** <typical error in magnitudes or flux>

### Phase 1 — Data Quality
- Outliers removed: <count and criteria>
- Data gaps: <number, total duration>
- Detrending applied: <polynomial order or method, or "none">
- Remaining noise floor: <σ in magnitudes or fractional flux>

### Phase 2 — Periodogram Results
| Period (days) | Frequency (day⁻¹) | Power | Sig (σ) | Harmonic? | Stable? |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | Y/N | Y/N |

(Only report periods significant at ≥4σ)

### Phase 3 — Periodic Components
For each significant period:

**Period P = <value> days**
- Amplitude: <peak-to-peak in mag or % flux>
- Profile: <sinusoidal / sawtooth / eclipsing / etc.>
- Phase fit χ²_red: <value>
- Attributed to: <rotation / pulsation / eclipses / other>
- Cross-checks: <spectroscopy / multiband / other data, if available>

### Phase 4 — Non-Periodic Components
- Long-term trend: <none / present; amplitude and timescale if present>
- Flares/transients: <count, energies, rise/decay times if present>
- Stochastic noise: <power-law exponent α if applicable, or RMS amplitude>

### Residual Quality
- χ²_red (full model vs. data): <value>
- Unexplained variance: <% of total>
- Likely sources: <instrumental / genuinely aperiodic / unresolved periods / measurement error>

### Caveats and Limitations
- Aliasing risk: <none / possible at [frequencies]; mitigation taken/needed>
- Detrending sensitivity: <results robust / moderately / highly dependent on detrending choice>
- Period resolution limit (1/T_obs): <value>
- Unresolved periods or ambiguities: <list if any>

### Confidence
<high | medium | low> — <justification: e.g., "high: strong peaks well above noise, multi-segment period stability confirmed, phase profile coherent to χ² = 1.2"; or "medium: one marginal period, poor phase coherence, no ancillary data for cross-check"; or "low: data too noisy, period aliases with observation window, detrending unstable">
```
---
