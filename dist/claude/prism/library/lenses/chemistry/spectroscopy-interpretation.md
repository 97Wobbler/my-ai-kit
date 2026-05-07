---
name: spectroscopy-interpretation
display_name: Spectroscopy Interpretation (NMR/IR/MS)
class: lens
underlying_class: native
domain: chemistry
source: Standard analytical chemistry practice; systematized in Silverstein & Webster (Spectrometric Identification of Organic Compounds, 2014)
best_for:
  - Deducing molecular structure from spectroscopic data
  - Assigning functional groups and connectivity patterns
  - Validating proposed structures against experimental evidence
one_liner: "Determine molecular structure by systematically interpreting spectroscopic signals."
---

# Spectroscopy Interpretation (NMR/IR/MS)

## Overview
Spectroscopy captures the interaction of molecules with electromagnetic radiation across different wavelengths. NMR (nuclear magnetic resonance), IR (infrared), and MS (mass spectrometry) each report on different molecular properties—connectivity and environment, functional groups, and fragmentation pattern—and together they constrain the structure uniquely. Practitioners use this lens when integrating multiple spectra to assign a structure, when an observed spectrum contradicts an expected one, or when validating a synthetic intermediate. The discipline is systematic cross-referencing: no single spectrum is interpreted in isolation.

## Analytical Procedure

### Phase 1 — Data Collection and Baseline Checks

1. **Gather all available spectra.** For a complete structural investigation, obtain:
   - Molecular formula (from high-resolution MS or elemental analysis)
   - Degree of unsaturation (DBE = (2C + 2 - H + N) / 2)
   - IR spectrum (2500–4000 cm⁻¹ and 500–1500 cm⁻¹ regions)
   - ¹H NMR (integration, multiplicity, chemical shift)
   - ¹³C NMR (or DEPT for CH/CH₂/CH₃ distinction)
   - MS data (molecular ion peak [M]⁺, major fragments, base peak)
   - For complex structures: COSY, HSQC, HMBC, or other 2D NMR if available.

2. **Validate the molecular formula.** Check that the molecular weight from MS matches the calculated mass from the formula. If discrepant by >5 ppm, recheck the formula or MS calibration.

3. **Calculate degree of unsaturation.** DBE predicts the number of rings and double bonds combined. Compare DBE to the IR evidence:
   - DBE = 0: no rings or unsaturations (saturated alkane).
   - DBE = 1: one double bond or one ring.
   - DBE = 4+: likely aromatic ring (contributes 4 to DBE).
   High DBE with no IR carbonyl or aromatic signals is a red flag.

### Phase 2 — IR Interpretation

4. **Scan the IR in order of diagnostic frequency ranges.** Use the table below:

| Wavenumber (cm⁻¹) | Functional Group | Appearance | Intensity |
|---|---|---|---|
| 3200–3600 | O–H stretch | Sharp (alcohol) or broad (carboxylic acid) | Strong |
| 3000–3100 | N–H stretch | Sharp peaks, often paired | Medium |
| 2800–3000 | C–H stretch | Multiple peaks | Medium–Strong |
| 1650–1750 | C=O stretch (carbonyl) | Sharp, intense | Very Strong |
| 1600–1680 | Aromatic C=C stretch | Multiple peaks | Medium |
| 1000–1300 | C–O stretch (alcohol, ether) | Broad, multiple | Medium–Strong |
| 600–900 | Out-of-plane C–H bending (aromatic) | Multiple peaks | Medium |

5. **Note what is ABSENT.** If DBE ≥ 4 and there is no aromatic absorption around 1600 cm⁻¹, or if the formula suggests a carbonyl but no C=O peak appears, document the anomaly—it constrains interpretation.

6. **Identify functional group families:**
   - Carboxylic acid: broad O–H + C=O around 1700 cm⁻¹.
   - Ester: C=O around 1735 cm⁻¹ + strong C–O stretch.
   - Ketone or aldehyde: C=O around 1715 cm⁻¹.
   - Alcohol: O–H stretch + C–O stretch.
   - Aromatic: C–H bending in the 600–900 cm⁻¹ region + aromatic C=C stretches.

### Phase 3 — Molecular Ion and Fragmentation (MS)

7. **Locate the molecular ion peak [M]⁺.** This is usually the rightmost peak in the spectrum (highest m/z). Confirm it matches your calculated molecular weight.

8. **Examine prominent fragments.** For each major peak, calculate the mass loss from [M]⁺:
   - Loss of 15 (CH₃): typical of alkyl compounds.
   - Loss of 18 (H₂O): typical of alcohols or compounds with OH.
   - Loss of 28 (CO): typical of carbonyl compounds.
   - Loss of 44 (CO₂): typical of carboxylic acids or esters.
   Record these losses and infer functional groups.

9. **Use the base peak (most intense) and fragmentation logic.** The base peak often represents the most stable cation. For example:
   - Tertiary carbocation is more stable than secondary, which is more stable than primary.
   - Resonance-stabilized cations (e.g., allyl, benzyl) are very stable.
   If a base peak at m/z = 91 appears with DBE ≥ 4, suspect a benzyl (C₇H₇⁺) group.

### Phase 4 — ¹H NMR Interpretation

10. **Assign each peak to a proton environment.** For each ¹H NMR signal, record:
    - Chemical shift (δ in ppm).
    - Integration (number of equivalent protons).
    - Multiplicity (singlet, doublet, triplet, quartet, multiplet).

11. **Use the chemical shift table to infer local environment:**

| δ range (ppm) | Environment | Example |
|---|---|---|
| 0.8–1.5 | Alkyl C–H | CH₃, CH₂ remote from electronegative atoms |
| 1.5–2.5 | C–H α to carbonyl | CH₂ in ketone or aldehyde |
| 2.0–3.0 | C–H α to heteroatom (O, N) | –OCH₃, –NCH₃, –OH |
| 3.3–4.3 | C–H on carbon bearing O | Alcohols, ethers, esters |
| 5.0–6.0 | Vinyl protons (C=C) | Alkene |
| 7.0–8.0 | Aromatic protons | Benzene and derivatives |
| 9–13 | Exchangeable protons | Carboxylic acid –COOH, phenolic –OH |

12. **Use multiplicity to infer coupling.** Apply the n+1 rule: a proton coupled to *n* equivalent neighboring protons appears as *n*+1 peaks (doublet, triplet, quartet, etc.). Use this to map connectivity:
    - Triplet in ¹H NMR usually indicates –CH₂– adjacent to –CH₃.
    - Quartet usually indicates –CH₃ adjacent to –CH₂–.
    - Doublet usually indicates –CH₃ or –CH– adjacent to another –CH–.

13. **Check integration consistency.** The total integration should equal the number of protons in the molecular formula. If it does not, recount or suspect overlapping signals.

### Phase 5 — ¹³C NMR and 2D NMR (if available)

14. **Map ¹³C signals to functional groups.** Use this approximate table:

| δ range (ppm) | Environment |
|---|---|
| 10–50 | Alkyl carbons |
| 50–100 | Carbons bearing O or N |
| 100–150 | Aromatic or vinyl carbons |
| 150–220 | Carbonyl carbons (C=O) |

15. **Use DEPT (Distortionless Enhancement by Polarization Transfer) if available.** DEPT distinguishes CH₃ (pointing up), CH₂ (pointing down), and CH (pointing up) from quaternary carbons (absent in DEPT). This resolves ambiguity in ¹³C NMR.

16. **Apply 2D correlations to confirm connectivity (if available):**
    - **COSY (correlation spectroscopy):** Shows which ¹H nuclei are coupled (J-coupled neighbors). Use this to trace spin systems.
    - **HSQC (heteronuclear single quantum coherence):** Correlates each ¹H to the ¹³C it is directly attached to. Confirms C–H connectivity.
    - **HMBC (heteronuclear multiple bond coherence):** Correlates ¹H to ¹³C atoms 2–4 bonds away. Use to infer longer-range connectivity and quaternary carbon placement.

### Phase 6 — Structure Assembly and Validation

17. **Propose a structure.** Using all the constraints from Phases 1–5, draw a structure that accounts for:
    - The molecular formula and DBE.
    - All IR functional groups.
    - The MS fragmentation pattern (especially base peak and characteristic losses).
    - The ¹H NMR shifts, integrations, and multiplicities.
    - The ¹³C NMR shifts and connectivity (from 2D NMR if available).

18. **Test the proposed structure against the data.** For each key observation, confirm that your structure predicts it:
    - Does the aromatic C–H bending pattern in IR match the substitution pattern (ortho, meta, para) inferred from ¹H NMR?
    - Does a loss of 18 (H₂O) in the MS match the presence of an OH group?
    - Does the ¹H NMR splitting pattern match expected coupling through your proposed bonds?
    - Does the ¹³C NMR peak count match the number of unique carbons in your structure (accounting for symmetry)?

19. **Iterate if anomalies emerge.** If the proposed structure does not explain an observation, return to the spectra and reconsider:
    - Overlapping ¹H signals?
    - Unexpected chemical shifts (e.g., a proton far downfield when the structure predicts it should be upfield)?
    - A ¹³C peak count mismatch (too many or too few peaks)?
    Adjust the structure and re-test.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Molecular formula verified against MS; DBE calculated | Y/N |
| All IR diagnostic regions scanned; functional groups assigned | Y/N |
| Molecular ion and major MS fragments identified and explained | Y/N |
| Each ¹H NMR peak assigned a chemical shift, integration, multiplicity | Y/N |
| ¹H NMR chemical shifts match expected environments for proposed structure | Y/N |
| Multiplicity (n+1 rule) confirms proposed connectivity | Y/N |
| ¹³C NMR peak count matches number of unique carbons (accounting for symmetry) | Y/N |
| Proposed structure accounts for all major spectroscopic observations | Y/N |
| No unexplained anomalies remain (or anomalies explicitly noted and rationalized) | Y/N |

## Red Flags

- Molecular weight from MS does not match the proposed formula. Stop and recheck calibration or formula.
- IR shows a carbonyl peak but ¹H and ¹³C NMR show no evidence of a proton or carbon in the carbonyl region (δ ~9–13 ppm for ¹H, δ ~150–220 ppm for ¹³C). This is a fundamental contradiction.
- ¹H NMR integration does not sum to the number of protons in the molecular formula. Either signals are overlapping, or the formula is wrong.
- ¹³C NMR peak count is far greater than the number of unique carbons predicted (no peak should appear twice unless there is accidental equivalence). Suggests impurity or re-check peak assignment.
- A large doublet in ¹H NMR (expected for –CH₃ adjacent to –CH–) appears with no corresponding triplet for the –CH– group. This violates the n+1 rule and suggests either overlap or misassignment.
- Proposed structure contains functional groups not evident in IR (e.g., a ketone with no C=O stretch, or an alcohol with no O–H stretch). Re-examine.
- MS base peak is at m/z much lower than [M]⁺ but with no obvious fragmentation path from your proposed structure. Consider rearrangement or alternative isomers.

## Output Format

```
## Spectroscopy Interpretation Report

**Molecular Formula:** <formula>
**Molecular Weight:** <MW in Da>
**Degree of Unsaturation:** <DBE>

### IR Analysis
| Functional Group | Diagnostic Peak(s) (cm⁻¹) | Observed? | Notes |
|---|---|---|---|
| ... | ... | Yes/No | ... |

### Mass Spectrometry
| Fragment | m/z | Interpretation |
|---|---|---|
| [M]⁺ | <m/z> | Molecular ion |
| [M–X]⁺ | <m/z> | Loss of <X> |
| Base peak | <m/z> | <Identity, e.g., C₇H₇⁺ (benzyl)> |

### ¹H NMR Assignments
| δ (ppm) | Integration | Multiplicity | Environment | Assignment |
|---|---|---|---|---|
| <δ> | <n>H | <s/d/t/q/m> | <e.g., aromatic, alkyl α to C=O> | <proton(s) in structure> |

### ¹³C NMR Assignments
| δ (ppm) | DEPT | Count | Assignment |
|---|---|---|---|
| <δ> | CH₃/CH₂/CH/Q | <number of equivalent carbons> | <carbon(s) in structure> |

### Proposed Structure
<Structure drawn or described in IUPAC or systematic name>

### Structure Validation
- IR predictions: <Brief check — does the structure explain the functional groups observed?>
- MS predictions: <Do the major fragments and base peak make sense for this structure?>
- ¹H NMR predictions: <Do the shifts, integrations, and multiplicities match?>
- ¹³C NMR predictions: <Does the peak count and shift range match?>

### Anomalies or Uncertainties
<List any spectroscopic observations not fully explained, or areas where alternative isomers remain possible.>

### Confidence
<high | medium | low> — <justification, e.g., "All major spectra are consistent with the proposed structure and no unexplained peaks remain. Confidence is high." Or: "¹H NMR multiplets are overlapping in the aromatic region, preventing definitive assignment of substitution pattern. Confidence is medium.">
```
---
