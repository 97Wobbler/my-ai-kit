---
name: hammett-equation
display_name: Hammett Equation
class: lens
underlying_class: native
domain: chemistry
source: Louis P. Hammett, 1937; extended by Taft, Hansch, and others
best_for:
  - Predicting how molecular substituents affect reaction rates or equilibria
  - Comparing reactivity trends across structural analogues
  - Screening substituent effects before synthesis
one_liner: "Quantify reactivity through the substituent σ × ρ linear free-energy relationship."
---

# Hammett Equation

## Overview

The Hammett Equation quantifies how electron-donating or electron-withdrawing substituents on a benzene ring influence the rate or equilibrium of a chemical reaction. It relates observed reactivity (log k or log K) to two parameters: the Hammett constant σ (a measure of the substituent's electronic effect) and the reaction sensitivity ρ (rho, a measure of how sensitive the reaction is to electronic changes). Practitioners use this framework to predict reactivity trends without running every experiment, to compare mechanisms across similar reactions, and to rank substituents by their probable effects. The power lies in separating the intrinsic property of the substituent (σ) from the context-dependent response of the reaction (ρ).

## Analytical Procedure

### Phase 1 — Define the Reaction and Baseline

1. **Identify the reference reaction and reference data.** Choose a single reaction for which you have quantitative kinetic or equilibrium data (rate constants k, equilibrium constants K, or their logarithms). This reaction serves as the baseline. Record the structure, conditions (solvent, temperature, pH if applicable), and all measured rate or equilibrium constants.

2. **List all substituents of interest.** For each substituent (e.g., H, Me, Cl, NO₂, OMe), document its position on the ring (ortho, meta, para if on benzene) and the raw kinetic/equilibrium data for that variant.

3. **Check reaction scope.** Hammett's equation assumes the mechanism is constant across substituent variants—only electronic effects change. If you suspect steric effects dominate, bond rotations change, or the mechanism shifts with substituent, note this as a scope limit. Hammett works best for meta and para substituents on benzene; ortho is complicated by steric effects.

### Phase 2 — Extract or Obtain Hammett Constants (σ)

4. **Source σ values for each substituent.** Use published tables (Hansch, Leo, and Taft compilations; modern databases like ChemSpider or Pubchem). Record the σ value and its source for each substituent. If σ is not published, note whether you will use: (a) experimental data from a reference reaction, or (b) computational estimates (e.g., HOMO/LUMO difference, NBO charge).

5. **Distinguish σ variants if needed.** Hammett's original σ is for ionizable reactions; Taft's σ* is for unsubstituted aryl systems; Hansch introduced σ⁺ (for carbocation intermediates) and σ⁻ (for carbanion intermediates). Check whether the reaction fits the standard σ or requires a variant. If the reference literature uses a different variant for your reaction class, use that.

6. **Verify σ consistency.** If using published values, ensure they are from the same source or carefully reconciled. A single inconsistent σ can skew the correlation.

### Phase 3 — Construct and Evaluate the Linear Regression

7. **Calculate log(k/k₀) or log(K/K₀) for each substituent.** Here, k or K is the rate or equilibrium constant for the substituted variant, and k₀ or K₀ is the rate or equilibrium constant for the unsubstituted (H) reference. This is the dependent variable, y.

8. **Perform a linear least-squares regression of y against σ.** Plot log(k/k₀) on the y-axis, σ on the x-axis. The slope is ρ, the intercept is 0 by construction. Generate the regression line, residuals, and R² (coefficient of determination).

9. **Evaluate the goodness of fit.**
   - **R² ≥ 0.95:** excellent fit; the linear model captures the data.
   - **0.90 ≤ R² < 0.95:** good fit; minor scatter, likely experimental noise.
   - **0.85 ≤ R² < 0.90:** acceptable fit; some deviations present, investigate outliers.
   - **R² < 0.85:** poor fit; the Hammett model does not describe this reaction well. Steric effects, multiple mechanisms, or non-electronic factors are likely at play.

10. **Identify and examine outliers.** Plot residuals vs. substituent type. If H, Me, Cl, etc. systematically deviate, note which ones and hypothesize why (e.g., ortho substituents, hydrogen bonding, steric clash). Do not remove outliers without explanation.

### Phase 4 — Interpret ρ and Predict

11. **Interpret the sign and magnitude of ρ.**
   - **ρ > 0:** electron-withdrawing substituents (positive σ) increase reaction rate/equilibrium; the transition state or intermediate is stabilized by electron withdrawal (e.g., SN2, nucleophilic aromatic substitution, reactions building positive charge).
   - **ρ < 0:** electron-donating substituents (negative σ) increase rate/equilibrium; the transition state benefits from electron donation (e.g., electrophilic aromatic substitution, reactions building negative charge or aryl radical formation).
   - **|ρ| large (>2):** the reaction is very sensitive to electronic effects; small changes in σ cause large changes in rate or equilibrium.
   - **|ρ| small (<0.5):** the reaction is insensitive to electronic effects; steric factors or other mechanisms dominate.

12. **Use the regression equation to predict unmeasured substituents.** For a new substituent with a known σ, plug σ into the fitted line: log(k_new/k₀) = ρ × σ. Solve for k_new. This is valid only if the new substituent fits the scope of the fit (para or meta, no ortho effects, etc.).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Reference reaction is fully specified (structure, conditions, mechanism) | Y/N |
| All substituents have tabulated or experimentally-derived σ values | Y/N |
| log(k/k₀) or log(K/K₀) is correctly calculated for each substituent | Y/N |
| Linear regression is performed and R² is reported | Y/N |
| Outliers are identified and explained (not silently removed) | Y/N |
| ρ is interpreted in terms of the proposed mechanism | Y/N |
| Scope limitations (ortho effects, mechanism shifts, steric interference) are documented | Y/N |

## Red Flags

- **R² < 0.85 without explanation.** The Hammett model is failing; the reaction likely involves steric bulk, multiple competing mechanisms, or non-electronic effects. Do not proceed to predictions.
- **Substituents include significant ortho effects (o-Me, o-Cl, etc.) but are treated as equivalent to meta/para.** Ortho introduces steric strain and can corrupt σ values. Exclude ortho or use a separate ortho-specific constant.
- **σ values are drawn from multiple sources with no reconciliation.** Different compilations can differ slightly (±0.05 units); mixing them introduces noise. Use one source or explicitly justify differences.
- **ρ is interpreted without reference to the proposed mechanism.** A negative ρ makes chemical sense only if you can explain why electron donation helps the reaction—if you cannot, the mechanism hypothesis is weak.
- **Predictions are made for substituents far outside the range of the fit** (e.g., fitting on small groups like Me, Cl but predicting for NO₂). Extrapolation beyond the data range is unreliable.
- **No residual plot is shown or discussed.** If residuals are not randomly scattered (e.g., show a curve or a systematic pattern), the linear model is inadequate.

## Output Format

```
## Hammett Equation Analysis

**Reaction:** <structure or SMILES/name>
**Conditions:** <solvent, temperature, mechanism type>
**Reference data:** <list of substituent → k or K values>

### Phase 1 — Baseline & Scope
- Reference reaction (H variant): k₀ = <value>, units <...>
- Mechanism: <proposed, e.g., SN2, EAS, carbocation formation>
- Scope limitations: <ortho effects, steric factors, pH sensitivity, etc.>

### Phase 2 — Hammett Constants (σ)
| Substituent | σ value | Source |
|---|---|---|
| H | 0.00 | (reference) |
| <...> | <...> | <...> |

### Phase 3 — Linear Regression

| Substituent | k or K | log(k/k₀) | σ | Residual |
|---|---|---|---|---|
| H | <...> | 0.00 | 0.00 | <...> |
| <...> | <...> | <...> | <...> | <...> |

**Regression line:** log(k/k₀) = ρ × σ
**ρ (slope):** <value with 95% confidence interval>
**R²:** <value>
**Interpretation:** [Fit quality and residual pattern; identify outliers and propose explanations]

### Phase 4 — Interpretation & Prediction

**ρ sign and magnitude:**
- ρ > 0 / ρ < 0: <electron withdrawal / donation> favors reaction
- |ρ| = <magnitude>: reaction is [sensitive / insensitive] to electronic effects

**Mechanism consistency:** <Does the sign of ρ match the proposed mechanism? If not, what does it imply?>

**Example prediction:**
- Proposed new substituent: <name, σ value>
- Predicted log(k_new/k₀): <value>
- Predicted k_new: <value with uncertainty>
- Validity: [Is this substituent within scope? Are there concerns?]

### Confidence
<high | medium | low> — <Justification based on R², outlier count, mechanism clarity, and scope adherence.>
```
---
