---
name: stable-isotope-analysis
display_name: Stable Isotope Analysis
class: lens
underlying_class: native
domain: geology
source: Urey, H. C. (1947); developed in paleoclimatology by Emiliani (1950s) and Shackleton (1970s)
best_for:
  - Reconstructing paleotemperature and paleoenvironment from skeletal carbonate
  - Tracing water and organic matter provenance in sediments
  - Detecting diagenetic alteration in fossil records
one_liner: "Reconstruct past climate and environment from oxygen and carbon isotope ratios in carbonates and biogenic skeletons."
---

# Stable Isotope Analysis

## Overview
Stable isotope ratios (δ¹⁸O and δ¹³C) in carbonate minerals and organic matter encode information about temperature, water source, and depositional chemistry at the time of formation. The practitioner measures these ratios in fossil shells, foraminifera, or bulk sediment, then interprets them against a calibration framework to infer paleotemperature, paleosalinity, and paleoproductivity. Geologists and paleoclimatologists use this lens when sedimentary records lack other chronological or environmental constraints and need sub-meter or sub-millennial resolution.

## Analytical Procedure

### Phase 1 — Sample Selection and Documentation

1. **Identify the target material.** Specify whether you are analyzing skeletal carbonate (foraminifera, ostracod, mollusc shell), bulk sediment, tooth enamel, or organic matter. Record the taxon, horizon, depth in core, and stratigraphic age estimate.

2. **Assess preservation state.** Examine the sample under a binocular microscope or SEM for:
   - Recrystallization (loss of fine structure, frosted appearance in SEM)
   - Infilling by secondary calcite or clay
   - Breakage or fragmentation beyond depositional transport
   - Visible alteration films or Fe-Mn coatings
   - For foraminifera: test color (should be translucent white/amber; brown or dark gray signals burning or diagenesis)
   
   Rank preservation on a scale: **pristine** (no alteration visible), **good** (minor surface etching), **moderate** (obvious recrystallization, <20% infilling), **poor** (heavy recrystallization, >20% void space filled).

3. **Select material for analysis.** Pick specimens of the same taxon and size class if possible. For foraminifera, choose 10–50 individuals of the same species. For bulk sediment, homogenize and subsample. Avoid specimens with visible coatings or infilling; if none are pristine, document the compromise.

4. **Prepare the sample for isotope measurement.** 
   - For carbonate: acid-leach in dilute HCl (0.1 M) for 30 seconds to remove surface clay, then rinse and dry. Weigh into a vial (2–10 mg of carbonate). 
   - For organic matter: isolate the target fraction (e.g., humic acid, kerogen, specific amino acids) using chemical or physical separation. 
   - Record sample weight, vial ID, and any chemical pretreatment applied.

### Phase 2 — Measurement and Standardization

5. **Conduct isotope ratio mass spectrometry (IRMS).** Run samples on a carbonate-handling device coupled to a continuous-flow or dual-inlet IRMS. Record raw voltage ratios for both ¹⁸O/¹⁶O and ¹³C/¹²C. Inject a working standard (e.g., NBS 19, VPDB calcite) every 5–10 samples to monitor instrumental drift.

6. **Calculate delta values.** For each sample, compute:
   - δ¹⁸O (‰) = [(Rsample / Rstandard) − 1] × 1000
   - δ¹³C (‰) = [(Rsample / Rstandard) − 1] × 1000
   
   where R is the ¹⁸O/¹⁶O or ¹³C/¹²C ratio and the standard is VPDB (Vienna Pee Dee Belemnite). Corrections for non-linearity and drift are automatic in modern instrument software. **Document the standard used and the calibration curve applied.**

7. **Assess measurement uncertainty.** Record the standard deviation of replicate analyses (typically ±0.1–0.2‰ for carbonate). If a sample was run more than once, report the mean and 1σ. Samples with SD > 0.3‰ between replicates flag inconsistent measurement or sample heterogeneity and should be rerun or flagged in the final report.

### Phase 3 — Interpretation and Calibration

8. **Select appropriate temperature and environment calibrations.** 
   - For **foraminifera δ¹⁸O**: apply a species-specific calibration equation (e.g., Bemis et al. 1998 for planktonic species; Shackleton 1974 for benthic species). The equation typically has the form: T(°C) = a × (δ¹⁸Ocarbonate − δ¹⁸Owater) + b
   - For **bulk sediment or mixed assemblages**: use a general benthic calibration or acknowledge that the temperature estimate is a mixture of multiple taxa.
   - Confirm that the calibration was developed using the same analytical method (IRMS, clumped isotope, etc.) and a similar time period/oceanographic regime.

9. **Constrain δ¹⁸O of the ambient water.** Estimate δ¹⁸Owater from:
   - Modern analogs (if the sample age is <10 ka, assume modern oceanographic conditions and apply VSMOW-corrected δ¹⁸Owater for that latitude and depth)
   - Paired benthic–planktonic foraminifera (if both are available, depth-corrected)
   - Ice volume correction (for pre-Holocene: δ¹⁸Owater rises ~0.1‰ per 10 m of sea-level drop, a well-established late Quaternary relationship)
   - Sensitivity testing: vary δ¹⁸Owater by ±0.5‰ and report the resulting temperature range
   
   **Document your assumption about δ¹⁸Owater explicitly** — it is the largest source of uncertainty in the calculation.

10. **Interpret δ¹³C in context.** δ¹³C in foraminifera records the δ¹³C of dissolved inorganic carbon (DIC) in the ambient water, modulated by vital effects (species-dependent fractionation during calcification). Use δ¹³C to infer:
    - **Paleoproductivity** (higher δ¹³C in surface sediments correlates with more photosynthetic removal of ¹²C and higher nutrient utilization)
    - **Water mass identity** (deeper, older water masses have lower δ¹³C because of remineralization of organic matter)
    - **Diagenetic alteration** (δ¹³C that is 1–3‰ lower than expected for the environment flags bacterial decomposition or methanogenesis in pore water)
    
    Do not interpret δ¹³C in isolation; compare it to modern analogs from the same depth and latitude.

11. **Check for diagenetic overprint.** Cross-check your temperature and environmental reconstructions against independent proxies:
    - **Comparison to coexisting records**: if δ¹⁸O paleotemperatures are 10°C warmer than clay mineralogy or alkenone paleothermometry suggest, diagenesis may be the culprit.
    - **Down-core trends**: if δ¹⁸O and δ¹³C become progressively lighter with burial depth at a single site (excluding primary environmental change), diagenesis is active.
    - **Replication across taxa**: if different species or different size fractions of the same species yield conflicting δ¹⁸O values, selective recrystallization of one fraction is likely.
    - **Petrographic evidence**: compare SEM observations (recrystallization, infilling) to isotopic data. If preservation is "poor" but δ¹⁸O is plausible, note the conflict.

### Phase 4 — Reporting and Uncertainty Quantification

12. **Quantify total uncertainty.** Calculate or estimate the combined uncertainty in your final result by propagating:
    - Measurement uncertainty (SD from replicates or instrumental precision)
    - Calibration equation uncertainty (typically ±1–2°C for temperature equations)
    - δ¹⁸Owater uncertainty (sensitivity test result)
    - Vital effect uncertainty (for species where vital fractionation is poorly constrained)
    
    Report the result as: **T = X ± Y°C (1σ combined)** or **δ¹³C = Z ± W‰**.

13. **Document all assumptions and limitations in a methods note.** State:
    - Species analyzed, sample size, stratigraphic position
    - Preservation ranking (pristine / good / moderate / poor)
    - IRMS standard and calibration equation used
    - Assumed δ¹⁸Owater value and justification
    - Whether diagenetic screens were applied and the outcome
    - Any replicate analyses and their agreement

## Evaluation Criteria

| Check | Pass |
|---|---|
| Sample preservation assessed and ranked (pristine–poor) | Y/N |
| IRMS measurements include standard data and drift corrections | Y/N |
| Species or material type specified; vital effect bias acknowledged if present | Y/N |
| δ¹⁸Owater value documented and justified (not assumed) | Y/N |
| δ¹⁸O paleotemperature cross-checked against at least one independent proxy | Y/N |
| Measurement + calibration + δ¹⁸Owater uncertainty propagated to final result | Y/N |
| Diagenetic alternative (recrystallization, infilling) ruled out or noted as caveat | Y/N |

## Red Flags

- Preservation ranking is not recorded. Without it, readers cannot judge the credibility of the interpretation.
- δ¹⁸Owater is assumed from a generic salinity–δ¹⁸O relationship without local oceanographic justification. In estuaries, upwelling zones, or ice-proximal settings, this assumption fails catastrophically.
- δ¹⁸O temperature is reported to ±0.5°C precision, but the total uncertainty budget is ±2°C or not calculated. False precision invites misuse.
- δ¹³C is interpreted as a productivity signal without comparison to modern analogs. Low δ¹³C in sediments can reflect local anoxia, methane seepage, or diagenesis, not just productivity.
- The sample underwent recrystallization (SEM shows frosted texture, heavy infilling) but the interpretation is treated as unambiguous. Recrystallized carbonate may have lost primary isotopic signature.
- No replicates or duplicate analyses. A one-off measurement has no attached uncertainty.
- Vital effect is ignored for a taxon known to have high vital fractionation (e.g., planktonic foraminifera can fractionate ¹⁸O by 1–2‰ relative to equilibrium).

## Output Format

```
## Stable Isotope Analysis Report

**Sample:** <taxon/material, horizon, depth, age estimate>

**Preservation:** <pristine | good | moderate | poor> — <description of SEM/microscopic observations>

### Raw Isotopic Data
| Sample ID | δ¹⁸O (‰ VPDB) | δ¹³C (‰ VPDB) | n replicates | SD |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

### Assumptions and Calibrations
- **IRMS Standard:** <NBS 19, VPDB, etc.>
- **Temperature calibration:** <citation, equation>
- **Assumed δ¹⁸Owater:** <value, unit, justification>
- **Vital effect correction (if applied):** <species-specific offset, citation>

### Paleotemperature Estimate
T = **X ± Y°C** (combined 1σ: measurement ± Z, calibration ± A, δ¹⁸Owater sensitivity ±B)

*Confidence: [high | medium | low] — <if preservation is pristine and cross-checked with independent proxy, high; if moderate preservation and single-proxy basis, medium; if poor preservation or conflicting proxies, low>*

### Paleoenvironmental Interpretation
- **δ¹³C inference:** <paleoproductivity, water mass identity, or diagenetic signal as inferred>
- **Cross-checks:** <comparison to independent proxies (clay mineralogy, alkenones, Mg/Ca); agreement or conflict noted>
- **Diagenetic risk:** <assessment of recrystallization, infilling, or down-core alteration trends; ruled in or out>

### Limitations and Caveats
<Explicit statement of model assumptions, taxa-specific biases, and scenarios where the interpretation breaks down.>

### Confidence
<high | medium | low> — <brief justification drawing on preservation, replication, cross-validation, and absence of contradictory proxies>
```
---
