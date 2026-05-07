---
name: fmo-theory
display_name: FMO Theory (Fukui)
class: model
underlying_class: native
domain: chemistry
source: Kenichi Fukui, "Theory of Orientation and Polarization for Electrophilic Substitution Reactions," Journal of Chemical Physics, 1952; expanded in Frontier Electrons in Chemical Reactions (1973)
best_for:
  - Predicting which site(s) in a molecule will undergo electrophilic or nucleophilic attack
  - Explaining regioselectivity and reactivity in organic reactions
  - Rationalizing reaction pathways without computing activation barriers
one_liner: "Frontier molecular orbital theory — reactive sites are set by the HOMO-LUMO gap and orbital overlap."
---

# FMO Theory (Fukui)

## Overview

Frontier Molecular Orbital (FMO) Theory claims that the reactivity and regioselectivity of organic reactions are governed primarily by the **interaction of the highest occupied molecular orbital (HOMO) of one reagent with the lowest unoccupied molecular orbital (LUMO) of the other** — rather than by the total electronic structure or by detailed calculations of transition states. The model is predictive: it allows chemists to identify which atoms or bonds in a molecule will react, and in what mode (electrophilic, nucleophilic, or cycloaddition), without solving the Schrödinger equation. The model is especially powerful for explaining *regioselectivity* — why a reaction occurs at one site rather than another — and for predicting stereochemical and regiochemical outcomes in organic synthesis.

## Core Variables and Relationships

FMO Theory operates on two key variables and their interaction:

1. **HOMO–LUMO energy gap (ΔE)** — the energy difference between the HOMO of the nucleophile and the LUMO of the electrophile (or vice versa for an electrophilic attack on a nucleophile).
   - Smaller ΔE → stronger interaction → faster reaction.
   - Expressed as: ΔE_rxn = E_LUMO(electrophile) − E_HOMO(nucleophile).
   - In nucleophilic attack, the nucleophile's HOMO donates electron density into the electrophile's LUMO.
   - In electrophilic attack, the electrophile's LUMO accepts electron density from the nucleophile's HOMO.

2. **Frontier orbital coefficients and symmetry overlap** — the magnitude and phase of the HOMO and LUMO wavefunctions at each atomic center.
   - Higher coefficient at a site → greater participation in the frontier orbital.
   - Sites with large, same-phase coefficients on both HOMO and LUMO of the reactants → strong orbital overlap → favored attack site.
   - Sites with opposite-phase coefficients (nodes) → poor overlap → disfavored.
   - Orbital symmetry matching is essential: if HOMO and LUMO phases are mismatched at a site, the interaction is antibonding and is disfavored.

3. **Fukui indices** (derived from frontier orbitals) — quantify the susceptibility of each atomic site:
   - f^+ (electrophilic Fukui index): probability that an atom accepts electron density in an electrophilic attack. Related to LUMO coefficient.
   - f^− (nucleophilic Fukui index): probability that an atom donates electron density in a nucleophilic attack. Related to HOMO coefficient.
   - Site with highest f^+ or f^− → most reactive site for that attack type.

4. **Orbital energy and reactivity hierarchy**:
   - **Electrophile-nucleophile pair**: For a given electrophile, nucleophiles with higher (less negative) HOMO energies react faster.
   - **Aromatic substitution**: Electron-donating substituents raise the HOMO energy of a benzene ring, increasing nucleophilicity and favoring electrophilic aromatic substitution. Electron-withdrawing groups lower the HOMO, deactivating the ring.
   - **Dienophile reactivity in Diels–Alder**: Electron-withdrawing groups lower the LUMO energy of the dienophile, making it more electron-deficient and more reactive toward the diene's HOMO.

## Key Predictions

- **Regioselectivity in electrophilic aromatic substitution:** The ortho/para ratio in electrophilic aromatic substitution is determined by the HOMO coefficients of the benzene ring at each position. Alkyl-substituted benzenes show HOMO density at the ortho and para positions, making them preferred attack sites; the meta position has a node and is disfavored.

- **Diels–Alder regioselectivity:** The endo/exo ratio and the regioselection in unsymmetrical Diels–Alder reactions are determined by the HOMO-LUMO overlap. Secondary orbital interactions (matching of the HOMO of one partner with the HOMO of the other, or LUMO-LUMO interaction) are weak but can break ties when the primary HOMO-LUMO gap is similar for two regioisomers.

- **Nucleophilicity trends:** Nucleophiles with higher HOMO energies (e.g., strong bases like alkoxides, or electron-rich heteroatoms like sulfur) react faster than those with lower HOMO energies (e.g., weak bases like carboxylic acids). This predicts order-of-reactivity without invoking charge or pKa alone.

- **Electrophile-promoted reactivity:** A highly electrophilic reagent (very low LUMO energy, e.g., strongly polarized C=O) reacts with a wider range of nucleophiles because the HOMO-LUMO gap is small even for weak nucleophiles. A weakly electrophilic reagent reacts only with strong nucleophiles.

- **Reaction mode selectivity:** The same nucleophile may undergo SN2, SN1, or elimination depending on the HOMO-LUMO energy levels of the substrate's C-X antibonding orbitals and the C=C π orbital. SN2 involves donation into an antibonding orbital of the C-X bond; elimination involves donation into the antibonding orbital of a C-H bond that is trans to the leaving group.

- **Pericyclic reaction selectivity:** Allowed pericyclic reactions (e.g., Diels–Alder, sigmatropic rearrangements) are those in which the HOMO and LUMO of the reactants have matching orbital symmetry (Woodward–Hoffmann rules as a consequence of FMO theory). Disallowed reactions proceed poorly or require much higher activation energy.

## Application Procedure

Instantiate FMO Theory against a concrete reaction or site-selectivity question.

1. **Identify the reaction type and the electrophile-nucleophile pair.**
   - Is this an electrophilic substitution, nucleophilic addition, Diels–Alder, or other reaction?
   - Which species acts as the nucleophile (donates electrons) and which as the electrophile (accepts electrons)?
   - Note: In some reactions, the roles may be unclear; sketch the mechanism to clarify.

2. **Identify the frontier orbitals of each partner.**
   - For the nucleophile: determine its HOMO (the occupied orbital with the lowest ionization energy).
   - For the electrophile: determine its LUMO (the unoccupied orbital with the lowest affinity for electrons).
   - If qualitative orbital energies are unknown, use empirical trends: electron-donating groups raise HOMO; electron-withdrawing groups lower LUMO.

3. **Estimate the HOMO-LUMO gap (ΔE).**
   - Qualitatively: is the nucleophile strong (high HOMO) and electrophile strong (low LUMO)? → small ΔE → fast reaction.
   - Weak nucleophile or weak electrophile? → larger ΔE → slower reaction.
   - This gap predicts *reaction rate* qualitatively.

4. **Map frontier orbital coefficients (or Fukui indices) onto the atoms.**
   - For each potential attack site in the electrophile, identify the LUMO coefficient (or f^+ Fukui index).
   - For aromatic or conjugated systems, draw the orbital diagram and note which atoms have large coefficients.
   - The site with the largest LUMO coefficient is the most electrophilic site for nucleophilic attack.
   - Similarly, for the nucleophile, the HOMO coefficient (or f^− index) identifies which atoms can donate most effectively.

5. **Check phase matching.**
   - Sketch a simple orbital overlap diagram between the HOMO of the nucleophile and the LUMO of the electrophile.
   - Ensure that at the proposed reaction site, the HOMO and LUMO phases are *in-phase* (same sign) so that overlap is bonding, not antibonding.
   - If phases are opposite, that site is disfavored.

6. **Consider secondary orbital interactions** if the primary HOMO-LUMO gap is similar for multiple regioisomers.
   - Secondary interactions include HOMO-HOMO and LUMO-LUMO interactions.
   - These are typically weaker but can predict endo vs. exo selectivity in cycloadditions.

7. **Check boundary conditions** (below). If any apply, flag that FMO is incomplete and note what additional analysis is needed.

8. **Generate the prediction:**
   - Which site(s) will react? (Identified by largest LUMO / HOMO coefficients and good phase overlap.)
   - How fast will the reaction be? (Smaller ΔE → faster.)
   - What is the regiochemical or regioelectronic outcome?
   - Compare prediction to known experimental regioselectivity if available.

## Boundary Conditions

FMO Theory assumes that the reaction is under orbital control and that the HOMO-LUMO interaction dominates. It is less reliable or incomplete under:

- **Thermodynamic (product) control.** FMO predicts the kinetically favored (lowest activation energy) product. If reaction conditions allow equilibration or if the reaction is reversible, the thermodynamically most stable product may dominate instead. Example: 1,2- vs. 1,4-addition to a diene depends on temperature and reversibility; FMO alone predicts kinetic regioselectivity.

- **Strong steric effects.** FMO assumes no steric clash. If a site has high LUMO coefficient but is sterically hindered, the reaction may be blocked or redirected. Steric effects must be assessed separately; FMO is blind to them.

- **Non-bonding orbital effects and strain.** Reactions involving very high-energy orbitals, or reactions that produce highly strained products, may not follow FMO predictions. FMO assumes normal bonding and antibonding patterns; extreme geometries can violate this.

- **Reactions involving transition-metal coordination or catalysis.** FMO Theory was developed for organic molecules. Transition metals have complex, multi-electron orbitals and often stabilize unusual reaction pathways not predicted by frontier orbitals of the organic substrate alone. Use organometallic or coordination theory alongside FMO.

- **Solvent effects and ion-pairing.** FMO is computed in the gas phase or in implicit solvent. Strong explicit solvation, hydrogen bonding, or ion-pairing can shift orbital energies significantly and change the HOMO-LUMO gap. FMO does not capture electrostatic pre-organization or explicit-solvent complexation.

- **Highly polar or highly ionic reactions.** In extremely ionic reactions (e.g., carbocation-anion combinations with very large charge separation), electrostatic attraction often dominates, and the orbital coefficients matter less. FMO assumes covalent character.

## Output Format

```
## FMO Analysis: <reaction type, substrate name>

**Reaction:** <nucleophile + electrophile → product(s)>
**Attack mode:** <electrophilic, nucleophilic, cycloaddition, etc.>
**Time snapshot:** <date>

### Frontier orbitals
| Reagent | FO | Orbital energy (eV, qualitative) | Remarks |
|---|---|---|---|
| Nucleophile | HOMO | <high / moderate / low> | <electron-donating / neutral / electron-withdrawing groups> |
| Electrophile | LUMO | <low / moderate / high> | <electron-withdrawing / neutral / electron-donating groups> |

### HOMO-LUMO gap and reactivity prediction
- ΔE_rxn: <small / medium / large> (qualitative)
- Expected reaction rate: <fast / moderate / slow>
- Reasoning: <summary of gap + conjugation effects>

### Regiochemistry analysis
| Potential site | LUMO/HOMO coefficient | Phase match | f^+ or f^− index | Predicted reactivity |
|---|---|---|---|---|
| ... | ... | In / Out | High / Low | Favored / Disfavored |

### Prediction
- Favored attack site(s): <which atom(s) and why>
- Regioselectivity: <which isomer, with HOMO-LUMO reasoning>
- Endo/exo or stereochemical outcome (if applicable): <prediction based on secondary interactions>

### Boundary-condition check
- Steric effects: <none / potential blocking at favored site / other>
- Thermodynamic vs. kinetic control: <kinetic (FMO applies) / reversible (may need thermodynamic analysis)>
- Solvent / ionic effects: <gas-phase assumption valid / explicit solvation may shift ΔE>
- Other: <metal catalysis / strain / ambiguity>

### Confidence: high | medium | low
<reasoning: orbital-energy estimates + coefficient clarity + boundary-condition fit + whether experimental regioselectivity data are available to validate>
```
---
