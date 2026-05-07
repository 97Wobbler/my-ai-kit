---
name: lipinskis-rule-of-five
display_name: Lipinski's Rule of Five
class: frame
underlying_class: native
domain: chemistry
source: Christopher A. Lipinski, Pfizer Inc., 1997 ("Drug-like Properties and Their Relationship to In Vitro Toxicology Assays")
best_for:
  - Sorting a drug candidate by oral bioavailability likelihood
  - Filtering chemical libraries for drug-likeness
  - Early-stage compound screening before expensive in vivo testing
one_liner: "Oral drug-likeness — judge druggability via five simple physicochemical rules."
---

# Lipinski's Rule of Five

## Overview

Lipinski's Rule of Five sorts a small-molecule compound into one of two categories — drug-like or not drug-like — based on five molecular property thresholds. The core claim is that compounds violating *more than one* of these rules have poor oral bioavailability and are unlikely to become successful oral drugs, even if they are biologically active. The frame is used early in drug discovery to filter large chemical libraries and avoid investing development effort in compounds that will fail at the pharmacokinetics stage.

## Categories

1. **Drug-like (Compliant)**
   - A compound that **violates zero or one** of the five Lipinski criteria.
   - Such compounds have a high probability of acceptable oral bioavailability when tested in vivo.
   - Discriminating criterion: meets at least four of the five property thresholds.
   - Example: aspirin (MW 180, LogP 1.2, 1 H-bond donor, 3 H-bond acceptors, 1 rotatable bond — fully compliant).

2. **Not Drug-like (Non-compliant)**
   - A compound that **violates two or more** of the five Lipinski criteria.
   - Such compounds are statistically unlikely to have adequate oral absorption or distribution, making them poor candidates for oral drug development.
   - Discriminating criterion: fails two or more property thresholds.
   - Example: rifampicin (MW 823, LogP 4.9, 3 H-bond donors, 12 H-bond acceptors, >10 rotatable bonds — violates MW, LogP, H-bond donor, and rotatable bond limits).

## The Five Criteria

For reference, the five molecular properties and their thresholds are:

1. **Molecular Weight (MW)** ≤ 500 Daltons
2. **Lipophilicity (LogP)** ≤ 5 (partition coefficient between octanol and water)
3. **Hydrogen Bond Donors (HBD)** ≤ 5 (NH and OH groups)
4. **Hydrogen Bond Acceptors (HBA)** ≤ 10 (N and O atoms)
5. **Rotatable Bonds** ≤ 10 (single bonds not in rings)

## Classification Procedure

1. Obtain or calculate the five molecular properties for the candidate compound: MW, LogP, HBD, HBA, and rotatable bond count.
2. Compare each property to its Lipinski threshold.
3. Count the **number of violations** (properties exceeding the threshold).
4. If violations ≤ 1 → **Drug-like**. Proceed with further development.
5. If violations ≥ 2 → **Not Drug-like**. Consider de-prioritizing or redesigning the compound.
6. Record the violation count and which specific properties exceed threshold; this informs chemical structure modifications if the compound is to be revisited.

## Implications per Category

| Category | Implication | Next step |
|---|---|---|
| **Drug-like** | Oral bioavailability is likely acceptable; compound merits progression to in vitro and in vivo testing. | Advance to ADME (absorption, distribution, metabolism, excretion) screening and animal pharmacokinetics. |
| **Not Drug-like** | Oral bioavailability is unlikely; compound will likely fail in vivo testing. Heavy resources required to achieve absorption and/or distribution. | Either de-prioritize and screen other compounds, or if the compound has exceptional biological activity, invest in chemical redesign to reduce MW, LogP, or H-bond count. |

## Common Misclassifications

- **Single violation mistaken for non-compliance.** A compound violating only one criterion (e.g., MW = 510) is still classified as drug-like. The tell is counting violations; Lipinski's threshold is *two or more*, not one.
- **Confusing LogP with other lipophilicity measures.** LogP specifically is the octanol–water partition coefficient. Other scales (e.g., MLOGP, XLOGP) may give slightly different values. Verify the metric used.
- **Applying Lipinski to non-oral routes.** Lipinski's Rule predicts oral bioavailability. A compound that fails Lipinski may still work as an intravenous or topical drug. The frame assumes oral administration.
- **Ignoring the rule of one violation.** Designers sometimes treat any violation as immediate disqualification, when in fact one violation is acceptable per Lipinski. This unnecessarily narrows the design space.
- **Over-reliance without considering biology.** A drug-like compound is not guaranteed to be effective — Lipinski addresses pharmacokinetics, not pharmacodynamics. Conversely, a non-compliant compound *might* work if it has exceptional potency or special transport mechanisms (e.g., active uptake). Lipinski is a screening filter, not a veto.
