---
name: woodward-hoffmann-rules
display_name: Woodward-Hoffmann Rules
class: lens
underlying_class: native
domain: chemistry
source: Woodward & Hoffmann, 1965 (Conservation of Orbital Symmetry)
best_for:
  - Predicting which pericyclic reactions proceed thermally vs. photochemically
  - Rationalizing unexpected selectivity or reaction barriers in cycloadditions and rearrangements
  - Designing synthetic routes that avoid symmetry-forbidden pathways
one_liner: "Decide whether a pericyclic reaction is allowed or forbidden via orbital symmetry."
---

# Woodward-Hoffmann Rules

## Overview

Pericyclic reactions (cycloadditions, sigmatropic shifts, electrocyclic reactions, and others) are allowed or forbidden based on whether the highest occupied molecular orbital (HOMO) of one reactant can interact constructively with the lowest unoccupied molecular orbital (LUMO) of another. Practitioners use this lens to predict reaction feasibility, understand why a synthetic route fails or succeeds, and choose between thermal and photochemical conditions. Rather than memorizing allowed/forbidden lists, the lens teaches the underlying orbital logic so that new reactions can be assessed without prior precedent.

## Analytical Procedure

### Phase 1 — Classify the Reaction

1. **Identify the reaction type.** Determine which category applies:
   - **Cycloaddition** — two π-systems combine to form a ring (e.g., Diels-Alder, [2+2])
   - **Electrocyclic** — a single conjugated π-system opens or closes (e.g., ring-opening of cyclobutene)
   - **Sigmatropic shift** — a σ-bond migrates across a conjugated system (e.g., [1,5]-H shift, [3,3]-Cope rearrangement)
   - **Cheletropic reaction** — a single atom forms/breaks two σ-bonds simultaneously
   If the reaction does not fit these categories, the Woodward-Hoffmann framework does not apply.

2. **Count π-electrons in each system.** For cycloadditions, count electrons in each reacting component separately. For electrocyclic reactions and sigmatropic shifts, count electrons in the conjugated chain. Record as 2, 4, 6, 8, etc. (always even for these reactions).

3. **Determine the mechanism: concerted or stepwise?** If the reaction is known to proceed via an intermediate (carbocation, radical, carbanion, etc.), it is *not* pericyclic and Woodward-Hoffmann does not apply. If there is no intermediate and all bonds form/break in a single transition state, proceed.

### Phase 2 — Assess Orbital Symmetry

4. **Draw or visualize the HOMO of the electron-rich system.** For a cycloaddition, identify which reactant is the electron donor (usually lower ionization energy, or explicitly nucleophilic). For electrocyclic/sigmatropic, there is only one system. Draw the HOMO as a sequence of lobes (positive and negative phases) around the conjugated chain.
   - Tip: For a conjugated diene (4 electrons), the HOMO has two bonding internuclear regions and two antibonding (nodal planes). For a dienophile (2 electrons), the HOMO is a single π-bond.

5. **Draw or visualize the LUMO of the electron-poor system.** (For cycloadditions only; for other pericyclics, the LUMO is of the same system, but shifted by one node.) The LUMO is the same system with one fewer node than the HOMO.
   - Tip: A diene LUMO has one bonding and one antibonding internuclear region.

6. **Test orbital overlap at the reaction sites.** Imagine the two orbitals approaching in the reactive geometry (usually the geometry that brings the atoms closest together without steric clash). 
   - **Allowed** — lobes of the same sign (both positive or both negative) come together at *both* reactive bond-forming sites simultaneously.
   - **Forbidden** — lobes of opposite signs meet at one or both sites, or there is significant orbital mismatch.
   Record the result as "thermally allowed" or "thermally forbidden."

7. **Repeat the assessment for photochemical conditions (excited state).** Photoexcitation of the electron-rich system promotes one electron from HOMO to LUMO, flipping the symmetry pattern. Redo steps 4–6 using the excited-state orbital of the donor. Record as "photochemically allowed" or "photochemically forbidden."

### Phase 3 — Reconcile with Experimental Behavior

8. **Check the prediction against known outcomes.** Literature or experimental data should show:
   - Thermally allowed reactions proceed readily at mild temperatures (ΔG ‡ typically < 25 kcal/mol).
   - Thermally forbidden reactions either do not occur at practical temperatures or require very high heat (> 100°C, often > 200°C).
   - Photochemically allowed reactions proceed under UV light even if thermally forbidden.
   - If the prediction matches the known behavior, the framework is correctly applied.

9. **If prediction and experiment conflict,** interrogate:
   - Is the mechanism truly concerted, or does an intermediate form (making it stepwise, not pericyclic)?
   - Are there competing non-pericyclic pathways (polar, radical-based)?
   - Is steric hindrance or orbital mismatch beyond symmetry blocking the reaction?
   - Record the conflict and do not claim symmetry is the limiting factor without ruling out alternatives.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Reaction is correctly classified (cycloaddition, electrocyclic, sigmatropic, or cheletropic) | Y/N |
| π-electron count is accurate for each system | Y/N |
| Reaction is concerted; no intermediate postulated | Y/N |
| HOMO of donor and LUMO of acceptor are correctly drawn with phases | Y/N |
| Overlap test is applied at *both* bond-forming sites | Y/N |
| Thermal and photochemical predictions are both stated | Y/N |
| Prediction is tested against literature or experimental data | Y/N |

## Red Flags

- Electron count is odd. Pericyclic reactions always involve even numbers of π-electrons.
- HOMO and LUMO are not drawn with explicit phase labels. Without phases, overlap cannot be assessed.
- Overlap test applies symmetry at only one reactive site. Pericyclic reactions form two (or more) bonds simultaneously; both must have favorable overlap.
- Thermal prediction is stated without acknowledging the photochemical outcome. These are different and both are predictable.
- The reaction is known to be stepwise (polar, radical, involving an isolable intermediate), yet Woodward-Hoffmann is still invoked. This mechanism category is outside the scope.
- Very high activation energy is observed experimentally (ΔG ‡ > 30 kcal/mol for a "forbidden" reaction at room temperature), yet no steric or polar explanation is considered. True symmetry forbiddance is usually hard kinetic forbiddance, not just slow.

## Output Format

```
## Woodward-Hoffmann Assessment

**Reaction type:** <cycloaddition / electrocyclic / sigmatropic / cheletropic>

**π-electron count:**
- System 1: _
- System 2: _ (if applicable)

**Mechanism:** Concerted (pericyclic) [Y/N]

### HOMO–LUMO Analysis

**HOMO (donor or single system):**
<description or ASCII diagram of phases>

**LUMO (acceptor or excited state):**
<description or ASCII diagram of phases>

### Symmetry Prediction

**Thermal reaction:** [Allowed / Forbidden]
- Overlap at site 1: <same sign / opposite sign>
- Overlap at site 2: <same sign / opposite sign>

**Photochemical reaction:** [Allowed / Forbidden]
- Excited-state HOMO: <modified phase pattern>
- Overlap at site 1: <same sign / opposite sign>
- Overlap at site 2: <same sign / opposite sign>

### Experimental Reconciliation

**Known behavior:** <reaction outcome, temperature, yield>

**Predicted outcome:** <matches / conflicts>

**Confidence:** <high/medium/low> — <if thermal allowed, expect facile reaction; if forbidden, expect very high ΔG ‡ or competing pathway; photochemical flips prediction; conflict suggests non-pericyclic mechanism or steric/polar dominance>
```
