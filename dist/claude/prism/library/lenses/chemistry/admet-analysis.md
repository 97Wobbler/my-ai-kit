---
name: admet-analysis
display_name: ADMET Analysis
class: lens
underlying_class: native
domain: chemistry
source: Lipinski et al. (1997); standardized in computational drug discovery; origin in oral bioavailability screening
best_for:
  - Predicting whether a small molecule will make a viable drug candidate
  - Early-stage compound filtering before synthesis or animal testing
  - Identifying which molecular properties to optimize in lead compounds
one_liner: "Screen drug candidates for clinical viability across absorption, distribution, metabolism, excretion, and toxicity."
---

# ADMET Analysis

## Overview
ADMET analysis predicts five physicochemical and pharmacokinetic properties that determine whether a molecule can be absorbed, distributed, metabolized, and eliminated safely by a human body. Rather than synthesizing and testing thousands of compounds, practitioners apply ADMET as a computational filter early in drug discovery to reject molecules likely to fail in vivo before resources are committed to chemistry, animal testing, or trials. The lens operates on chemical structures (as SMILES strings or 2D/3D models) and produces a binary pass/fail verdict plus quantitative scores on each axis.

## Analytical Procedure

### Phase 1 — Prepare the Molecule

1. **Obtain the chemical structure** in a machine-readable format: SMILES string, SDF file, or molfile. If given only a name, convert it using ChemDraw, RDKit, or a chemical database (PubChem, ChemSpider).

2. **Normalize the structure:**
   - Add or verify hydrogens for the predominant ionization state at physiological pH 7.4.
   - Resolve salt forms to the free base or acid.
   - Remove counter-ions and crystallographic water molecules.
   - Check for valence errors or unusual oxidation states. If present, document them and note that the structure may be ambiguous.

3. **Calculate molecular weight (MW).**
   - Record the exact mass (sum of atomic weights).
   - Flag if MW > 500 Da; this predicts poor oral absorption.

### Phase 2 — Apply the Five ADMET Axes

#### **Axis 1 — Absorption (A)**

4. **Calculate lipophilicity (LogP).**
   - Use an established partition coefficient predictor (Wildman-Crippen LogP, Moriguchi LogP, or consensus).
   - Record the LogP value.
   - **Pass criterion:** −1 ≤ LogP ≤ 5. Values outside this range predict poor oral bioavailability or excessive off-target binding.

5. **Count hydrogen bond donors (HBD) and acceptors (HBA).**
   - HBD: N–H and O–H groups.
   - HBA: N and O atoms (not N/O themselves, but the atoms serving as acceptors).
   - **Pass criteria:** HBD ≤ 5, HBA ≤ 10 (Lipinski's Rule of Five thresholds).
   - Compounds exceeding these are predicted to have low oral absorption due to poor membrane permeability.

6. **Estimate topological polar surface area (TPSA).**
   - TPSA is the surface sum of all polar atoms (typically N and O).
   - **Pass criterion:** TPSA ≤ 140 Ų. Higher values predict poor cell membrane penetration.

#### **Axis 2 — Distribution (D)**

7. **Predict blood-brain barrier (BBB) penetration (if relevant).**
   - Use TPSA and MW as proxies: molecules with TPSA < 60 Ų and MW < 400 Da are likely to cross BBB.
   - Note: BBB penetration is desirable for CNS drugs but undesirable for non-CNS drugs (off-target neurotoxicity risk).
   - Record whether BBB penetration is expected and whether it is desired for the therapeutic indication.

8. **Estimate plasma protein binding (PPB).**
   - High PPB (>90%) reduces free drug concentration and efficacy; it also increases drug-drug interaction risk.
   - Use LogP as a surrogate: LogP > 5 predicts high PPB.
   - **Flag if PPB is predicted to be >90%.**

#### **Axis 3 — Metabolism (M)**

9. **Identify sites of metabolic attack.**
   - Search the structure for common metabolic hotspots: aromatic C–H, aliphatic C–H, N–H, O–H, sulfur, and heteroaromatic N.
   - Use a metabolism predictor tool (MetaDrug, Meteor, Sybyl) or manual inspection.
   - List the top 3 predicted metabolic sites.

10. **Assess metabolic stability.**
    - If structural analogs are available, record their known clearance rates (low, moderate, high).
    - Estimate clearance category (fast, moderate, slow) based on the number and reactivity of metabolic sites.
    - Slow metabolism (low clearance) is generally favorable for oral drugs (longer half-life, better PK).
    - Very fast metabolism (high clearance) may result in insufficient exposure unless dosed frequently.

#### **Axis 4 — Excretion (E)**

11. **Estimate renal clearance.**
    - Molecules with MW < 500 Da and low plasma protein binding are predicted to be renally cleared.
    - Highly polar molecules (TPSA > 140 Ų) or zwitterionic molecules are excreted unchanged via the kidney.
    - Record whether the compound is expected to be renally cleared (Y/N).

12. **Check for biliary excretion risk factors.**
    - Compounds with MW > 400 Da and high lipophilicity (LogP > 3) may be excreted via the bile duct, which can increase liver exposure and hepatotoxicity risk.
    - **Flag if MW > 400 and LogP > 3.**

#### **Axis 5 — Toxicity (T)**

13. **Screen for structural alerts (SAs).**
    - Compare the structure against known toxicophores (PAINS filters, Brenk filters, or in-house proprietary lists).
    - Toxicophores include: Michael acceptors, aromatic nitros, free radicals, alkylating agents, acyl halides, etc.
    - Record all SA matches and their severity (high-concern, moderate, informational).

14. **Estimate hepatotoxicity risk.**
    - Compounds with high metabolic instability and high liver exposure (MW > 400, high LogP, biliary excretion predicted) carry elevated hepatotoxicity risk.
    - Record risk level: low, moderate, high.

15. **Check hERG inhibition liability.**
    - Compounds with aromatic rings, basic nitrogens, and planar geometry are prone to hERG (cardiac potassium channel) inhibition.
    - Use an hERG predictor or chemical rules (aromatic ring + basic N + planar).
    - If hERG inhibition is predicted, record as a cardiac liability.

### Phase 3 — Synthesize and Score

16. **Compile ADMET profile:**
    - For each axis, record: status (PASS/FAIL/FLAG), principal metrics, and caveats.

17. **Assign overall pass/fail verdict:**
    - **PASS:** No FAIL on any axis; ≤1 FLAG across all axes.
    - **FLAG:** One axis is FAIL or ≥2 FLAGs across axes. Compound is viable but requires optimization.
    - **FAIL:** ≥2 axes are FAIL. Compound is predicted to have poor in vivo properties; recommend redesign.

18. **Rank priority for optimization** (if FLAG or FAIL):
    - Identify which axis is the bottleneck (e.g., poor absorption, high metabolism).
    - Suggest a chemical modification strategy (e.g., reduce MW to improve absorption; add metabolic blockers to slow clearance).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Molecular structure is normalized and valence-checked | Y/N |
| All five axes are scored with quantitative metrics | Y/N |
| MW, LogP, HBD, HBA, TPSA are reported with values | Y/N |
| Metabolic sites and structural alerts are explicitly listed | Y/N |
| BBB, hERG, and biliary excretion risks are flagged where relevant | Y/N |
| Overall verdict (PASS/FLAG/FAIL) is justified by the axis scores | Y/N |
| At least one optimization recommendation is provided for FLAG/FAIL cases | Y/N |

## Red Flags

- TPSA or LogP calculated but thresholds never stated; the analyst cannot defend the pass/fail boundary.
- Structural alerts identified but severity not ranked; high-concern toxicophores are not distinguished from informational ones.
- BBB penetration is predicted but the therapeutic indication is not checked (e.g., BBB penetration predicted but the drug is for a non-CNS disease, raising off-target risk).
- Metabolism assessed only by hotspot count, without consulting analogs or reference data; no comparative context for "fast" vs. "slow."
- hERG risk ignored entirely; cardiac toxicity is a leading cause of post-marketing drug withdrawal.
- Overall verdict assigned but not traceable to the five axis scores; reviewer cannot validate the decision.

## Output Format

```
## ADMET Assessment

**Molecule:**
SMILES: <...>
Molecular Weight: ___ Da

### Axis 1 — Absorption (A)
| Property | Value | Threshold | Status |
|---|---|---|---|
| LogP | ___ | −1 to 5 | PASS / FAIL |
| HBD | ___ | ≤ 5 | PASS / FAIL |
| HBA | ___ | ≤ 10 | PASS / FAIL |
| TPSA | ___ Ų | ≤ 140 | PASS / FAIL |
| **Absorption verdict** | | | **PASS / FLAG / FAIL** |

### Axis 2 — Distribution (D)
| Property | Prediction | Flag |
|---|---|---|
| BBB penetration | Yes / No | N/A if non-CNS drug |
| Plasma protein binding >90% | Yes / No | <-- if Yes, FLAG |
| **Distribution verdict** | | **PASS / FLAG** |

### Axis 3 — Metabolism (M)
Top metabolic sites: <...>, <...>, <...>
Predicted clearance rate: Fast / Moderate / Slow
Analogs with known clearance: <...>
**Metabolism verdict:** **PASS / FLAG / FAIL**

### Axis 4 — Excretion (E)
Renal clearance expected: Yes / No
Biliary excretion risk (MW > 400 + LogP > 3): <-- if Yes, FLAG
**Excretion verdict:** **PASS / FLAG**

### Axis 5 — Toxicity (T)
| Structural Alert | Severity | Flag |
|---|---|---|
| <...> | High / Moderate / Info | <-- |
| hERG inhibition risk | Yes / No | <-- if Yes, FLAG |
| Hepatotoxicity risk | Low / Moderate / High | <-- if High, FLAG |
| **Toxicity verdict** | | **PASS / FLAG / FAIL** |

### Overall ADMET Profile
| Axis | Verdict |
|---|---|
| Absorption | PASS / FLAG / FAIL |
| Distribution | PASS / FLAG |
| Metabolism | PASS / FLAG / FAIL |
| Excretion | PASS / FLAG |
| Toxicity | PASS / FLAG / FAIL |

**Overall recommendation:** PASS / FLAG / FAIL

**Rationale:** <one sentence explaining the bottleneck or the all-clear>

**Optimization priority (if FLAG or FAIL):** <axis and suggested chemical modification>

### Confidence
<high/medium/low> — <justification: predicted values are in silico and should be validated by wet assays; confidence increases with structural similarity to analogs with known ADMET data>
```
---
