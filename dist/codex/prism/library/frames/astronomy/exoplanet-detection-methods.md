---
name: exoplanet-detection-methods
display_name: Exoplanet Detection Methods
class: frame
underlying_class: native
domain: astronomy
source: origin uncertain
best_for:
  - Sorting an exoplanet discovery by observational method to understand detection sensitivity and bias
  - Choosing which method is best suited to find planets in a given orbital or stellar regime
one_liner: "Classify exoplanet detection methods by sensitivity, bias, and accessible planetary properties."
---

# Exoplanet Detection Methods

## Overview

This frame sorts an exoplanet discovery or search strategy by the physical method used to detect the planet's presence. Its core claim is that each detection method is **sensitive to different planetary and orbital parameters** — and the same planet in different orbital configurations will be detectable by one method but not another. Sorting a discovery or a survey by method reveals which kinds of planets populate the known sample, which are systematically missed, and which method is most practical for a given scientific question. The method chosen also determines observational bias: transit surveys find planets close to their stars; radial-velocity surveys miss edge-on orbits; imaging finds only young, hot planets far from their host.

## Categories

1. **Transit Method** (also "photometry" or "transit photometry")
   - Detection via **periodic dips in stellar brightness** as the planet passes in front of the star.
   - Sensitivity: highest for planets in short-period, edge-on orbits around bright stars.
   - Discriminating criterion: requires orbital inclination near 90°; sensitive to planetary radius and orbital period, not stellar orbital motion.
   - Example: the vast majority of exoplanets discovered by Kepler, TESS, and ground-based surveys; directly measures planet radius and orbit.
   - Observable bias: strongly favors short-period planets and edge-on systems; misses planets in wide orbits or at high inclinations.

2. **Radial Velocity Method** (also "spectroscopy" or "Doppler method")
   - Detection via **periodic shifts in the star's motion along the line of sight**, measured via Doppler shift of stellar spectral lines.
   - Sensitivity: highest for massive planets at any orbital distance; independent of inclination (though minimum mass is inclination-dependent).
   - Discriminating criterion: detects cumulative gravitational pull on the star; measures minimum mass, not radius; works for any inclination.
   - Example: 51 Pegasi b (first exoplanet); planets around M dwarfs found by HARPS and similar high-precision spectrographs.
   - Observable bias: favors massive planets and wide orbits; less sensitive to low-mass planets; inclination unknown unless supplemented by other methods.

3. **Direct Imaging**
   - Detection via **direct photographic observation of reflected or emitted light** from the planet itself, spatially separated from the star.
   - Sensitivity: highest for young, hot planets far from the star (wide orbits, high temperature, recent formation).
   - Discriminating criterion: requires high contrast and angular separation; works only for massive, young planets that emit thermal radiation; typically requires infrared.
   - Example: HR 8799 system (multiple planets imaged in mid-infrared); β Pic b; most young association planets.
   - Observable bias: strongly biased toward young systems and wide, massive orbits; nearly impossible for planets closer than ~10 AU or older than ~100 Myr.

4. **Gravitational Microlensing**
   - Detection via **light amplification from a chance alignment** in which the planetary system acts as a gravitational lens for a more-distant background star.
   - Sensitivity: unique ability to find planets at solar system scales and beyond, and to find planets around very distant stars; sensitive to planets regardless of orbital inclination.
   - Discriminating criterion: event-driven and not repeatable for the same planet; requires a fortuitous alignment; independent of planet luminosity.
   - Example: planets in the Galactic Bulge; planetary-mass ratio and separation measurable from the light curve; candidate exomoons detected this way.
   - Observable bias: probes outer solar system analogs; insensitive to stellar distance (can detect planets light-years away); mass ratio measurable but absolute mass and luminosity not.

5. **Astrometry**
   - Detection via **periodic shifts in the star's position on the sky** caused by the planet's gravitational pull (distinct from parallax).
   - Sensitivity: most practical for massive planets at wide orbits; enhanced by long baseline measurements (space-based required for small amplitudes).
   - Discriminating criterion: measures absolute mass and full 3D orbit; works at any distance if instrumentation is precise enough; independent of orbital inclination.
   - Example: Gaia mission candidate detections; potential future detections of Jupiter-mass planets at solar system scales.
   - Observable bias: currently limited to nearby stars and massive planets; historically underutilized due to instrumental precision requirements.

6. **Timing Variations** (also "pulsar timing" or "transit timing variations")
   - Detection via **subtle periodic changes in arrival time** of a pulse (pulsar) or transit (planet+planet system) caused by gravitational perturbation.
   - Sensitivity: exquisite for small-mass planets in multi-planet systems or around millisecond pulsars; can detect Earth-mass planets.
   - Discriminating criterion: requires a high-precision clock (pulsar) or a high-cadence photometric time series (TTV); indirectly measures planet mass via perturbation.
   - Example: planets around pulsars; planets in the Kepler multi-planet systems detected via transit-timing variations.
   - Observable bias: limited to systems with multiple planets or pulsars; requires very long baseline of observations; excellent for detecting low-mass planets in compact systems.

## Classification Procedure

1. **Describe the discovery or survey goal.** State what is observed (e.g., photometry time series, radial velocity spectrum, direct image, event light curve, positional measurements, or transit-time residuals) and what celestial object is being monitored.

2. **Ask: What observable quantity reveals the planet?**
   - Periodic dimming of light → **Transit**.
   - Periodic wavelength shift of stellar spectrum → **Radial Velocity**.
   - Direct photon collection from the planet in the imaging plane → **Direct Imaging**.
   - Amplified light from a background star via gravitational lensing → **Microlensing**.
   - Shifting position of the star on the sky → **Astrometry**.
   - Perturbations in pulse arrival or transit timing → **Timing Variations**.

3. **Cross-check against orbital constraints.** If the discriminating criterion of the candidate method (e.g., edge-on for transit, high contrast for imaging) is not satisfied or is not observed, revisit the answer to step 2.

4. **State the method and note the key sensitivity/bias.** Example: "This is a transit discovery; the system is edge-on, so we measure radius and orbital period but not the planet's true mass; planets in wide orbits are not detectable this way."

## Implications per Category

| Category | Measured quantities | Blind spots | Next-step analysis |
|---|---|---|---|
| **Transit** | Planet radius, orbital period, orbital inclination, atmosphere (via transmission spectroscopy) | True mass (inclination-dependent), planets in wide orbits | Combine with RV to break inclination degeneracy; search for TTV in multi-planet systems. |
| **Radial Velocity** | Minimum mass, orbital period, orbital eccentricity, long-term trends (wide planets) | Planet radius, planets at high inclinations, long-period planets (require years of data) | Combine with transit for true mass; use direct imaging or astrometry for visual confirmation. |
| **Direct Imaging** | Planet luminosity, atmospheric composition, orbital motion (relative position over years), age constraints | Planet mass (without additional dynamics), planets not yet cooled | Combine with RV for absolute mass; use Gaia parallax for distance refinement. |
| **Microlensing** | Planet-star mass ratio, planetary-mass companions, planets far from their stars | Absolute masses, planet luminosity, orbital inclination | Requires follow-up imaging or RV in favorable cases; targets galaxies and Galactic Bulge. |
| **Astrometry** | Absolute planet mass, full 3D orbital elements, planets at any inclination | Rapid follow-up characterization (requires long baseline) | Extremely powerful for orbit reconstruction; emerging from Gaia and future missions. |
| **Timing Variations** | Planet masses in multi-planet systems, Earth-mass planets in compact orbits | Single-planet systems, planets in isolated orbits | Essential for constraining system architecture and planet-planet interactions. |

For a lenslab agent analyzing an exoplanet survey or discovery: choose the method first to understand which population you can detect, then apply method-specific lenses (e.g., TTV dynamics for Timing, contrast limits for Imaging, Doppler precision for RV) to refine the physical interpretation.

## Common Misclassifications

- **Transit mistaken for Radial Velocity.** Both produce periodic signals; the tell is the observable. Transits show brightness dips; RV shows wavelength shifts. Consequence: wrong planet mass, wrong orbital inclination inference.
  
- **Direct Imaging mistaken for Astrometry.** Both show spatial information; the tell is whether you see photons from the planet itself (imaging) or only the star's position shifts (astrometry). Consequence: false candidate confirmations in direct imaging when the companion is stellar or substellar, not planetary.

- **Microlensing mistaken for Astrometry.** Both are geometry-sensitive; the tell is whether the event is transient and amplifying (microlensing) or periodic and astrometric (astrometry). Consequence: misidentifying planets at different distances or orbits.

- **Timing Variations mistaken for a Single Method.** TTV is always *subsidiary* to either Transit or pulsar observations; the primary method is transit photometry or pulsar timing, and the planet is detected via perturbation. Classifying TTV as its own discovery method obscures the underlying observable.

- **Ignoring inclination degeneracy in Radial Velocity.** RV yields minimum mass (M sin i), not true mass. Mistaking minimum mass for true mass is rampant; the tell is whether an independent inclination measurement (transit, astrometry, imaging) exists. Consequence: overestimating planet mass by up to a factor of ~57 in extreme cases.
