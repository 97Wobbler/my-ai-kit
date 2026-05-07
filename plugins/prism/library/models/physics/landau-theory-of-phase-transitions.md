---
name: landau-theory-of-phase-transitions
display_name: Landau Theory of Phase Transitions
class: model
underlying_class: native
domain: physics
source: Lev Landau, "On the Theory of Phase Transitions," Journal of Experimental and Theoretical Physics, 1937; extended by Landau & Lifshitz in Statistical Physics (1958)
best_for:
  - Predicting critical behavior and phase-transition properties near equilibrium critical points
  - Explaining symmetry breaking and universality in continuous phase transitions
  - Calculating critical exponents and phase diagrams from minimal microscopic information
one_liner: "Explain phase transitions through symmetry breaking and free-energy expansion in the order parameter."
---

# Landau Theory of Phase Transitions

## Overview

Landau Theory is a phenomenological framework that explains continuous phase transitions by expanding the free energy as a power series in an **order parameter** — a variable that is zero in the high-symmetry phase and nonzero in the low-symmetry phase. The theory's central claim is that near a critical point, the free energy can be reliably approximated by keeping only the first few terms of this expansion, ordered by symmetry and powers of the order parameter. This minimalist approach yields non-obvious predictions: critical exponents, the shape of phase diagrams, the nature of stable vs. unstable phases, and why certain transitions are continuous while others are discontinuous. The theory is predictive for temperatures and fields near the critical point; it fails far from criticality. It is explanatory in the sense that it reveals the *logical structure* of phase transitions once symmetry is invoked, but it does not derive that structure from microscopic first principles.

## Core Variables and Relationships

**Order parameter η:** A scalar (or tensor) quantity that measures the degree of broken symmetry. η = 0 in the disordered (high-temperature) phase; η ≠ 0 in the ordered (low-temperature) phase. For a ferromagnet, η is magnetization; for a liquid–gas transition, η is related to density difference. The choice of η encodes the physical symmetry breaking.

**Free energy (Landau free energy):**
$$F(η, T, h) = F_0(T) + a(T)η^2 + b(T)η^4 + c(T)η^6 + … − hη$$

where:
- **a(T)** is the quadratic coefficient, taken to vanish at the critical temperature: a(T) ≈ a′(T − T_c) near T_c (a′ > 0).
- **b(T)** is the quartic coefficient; for a continuous (second-order) transition, b > 0 is assumed; b < 0 leads to first-order transitions or instability.
- **c(T), higher terms** capture higher-order constraints; often negligible very close to T_c.
- **h** is an external field conjugate to η (magnetic field, chemical potential difference, etc.).
- **F_0(T)** is a non-singular background free energy; its exact form does not affect phase stability.

**Equilibrium condition:** The system minimizes F, so the stable order parameter satisfies ∂F/∂η = 0, which yields:

$$2a(T)η + 4b(T)η^3 + … = h$$

**Critical exponents (defined near T_c):**
- **β**: order parameter vanishes as η ∝ (T_c − T)^β; Landau predicts **β = 1/2**.
- **α**: heat capacity diverges as C_v ∝ |T − T_c|^{−α}; Landau predicts **α = 0** (a logarithmic divergence or cusp).
- **γ**: susceptibility χ = ∂η/∂h diverges as χ ∝ |T − T_c|^{−γ}; Landau predicts **γ = 1**.
- **δ**: isotherm exponent η ∝ h^{1/δ} at T = T_c; Landau predicts **δ = 3**.

## Key Predictions

- **Universality of critical exponents below T_c.** All second-order phase transitions with the same symmetry (same dimensionality of order parameter, same spatial dimensionality) have the same critical exponents to leading order, regardless of microscopic details. This is a profound prediction: ferromagnets, liquid–gas transitions, and superfluid helium should have measurably different exponents if their symmetries differ — and they do, in the way Landau's symmetry classes predict.

- **Phase diagram structure.** The phase boundary (coexistence curve) near T_c is determined solely by a(T) and b(T): above T_c, η = 0 (disordered phase) is stable; below T_c, the equilibrium η is nonzero and symmetric (|η| is the same for +η and −η if h = 0). The phase diagram widens as one moves away from T_c, and the width is proportional to |T − T_c|^{β}.

- **Discontinuity at the transition.** At the transition (h = 0, T = T_c), the order parameter η jumps discontinuously from 0 to ±√(−a/2b) as T crosses below T_c. This discontinuity is *second-order* in the thermodynamic sense (first derivative of F is continuous, but second derivatives—entropy, heat capacity—are discontinuous), consistent with experiments on ferromagnets near T_c.

- **Field-dependent suppression of order.** In the presence of a non-zero field h (e.g., external magnetic field), the transition is rounded: the order parameter rises continuously, and the discontinuity in entropy at T_c is suppressed. The phase diagram acquires a critical end point if h crosses zero.

- **Tricritical and multicritical points.** If b(T) is allowed to vanish at some T = T_tri < T_c, the critical exponent β changes discontinuously; β = 1/4 near a tricritical point. This predicts that certain materials with competing interactions should show anomalous critical behavior—a prediction borne out in some magnetic systems.

- **Scaling laws.** Near T_c, all thermodynamic functions scale as powers of the same two variables: the reduced temperature |T − T_c|/T_c and the reduced field h/|T − T_c|^{βδ}. This scaling prediction is non-obvious from the Landau expansion alone, but follows from dimensional analysis on the theory and is supported by experiments (e.g., ferromagnetic susceptibility data collapse onto a universal curve when plotted in scaled variables).

## Application Procedure

Instantiate Landau Theory against a phase transition you wish to explain or predict.

1. **Identify the phase transition and the symmetry breaking.** What is the high-symmetry (disordered) phase? What is the low-symmetry (ordered) phase? What symmetry is broken (rotational, translational, gauge)? Write a one-sentence description of the symmetry change.

2. **Identify the order parameter η.** What quantity is zero in the disordered phase and nonzero in the ordered phase? Is it a scalar (e.g., magnetization M, density difference ρ_liquid − ρ_gas) or a vector (e.g., three-component magnetization in a ferromagnet)? The dimensionality of η determines the symmetry class and, in principle, the critical exponents.

3. **Identify the control parameters.** What external variables tune the transition? Typically temperature T; sometimes pressure, magnetic field h, or chemical potential. Write them explicitly.

4. **Construct the Landau free energy.** Write down the free-energy expansion F(η, T, h) to quartic order (higher powers are rarely needed near T_c). Use symmetry to decide which terms are allowed:
   - If η is a scalar, both η^2 and η^4 terms are allowed; odd powers (η, η^3) are forbidden unless h breaks the symmetry.
   - If η is a vector of n components, write η² = Σ_i η_i², and construct invariants: η^2, (η^2)^2, etc.
   - Temperature dependence: assume a(T) ≈ a′(T − T_c) and b(T) ≈ const. > 0 (or investigate if b changes sign).

5. **Locate the critical point.** Set ∂F/∂η = 0 and solve for the equilibrium order parameter η_eq(T, h). At the critical point (T = T_c, h = 0), the condition ∂²F/∂η² = 0 must also hold; this fixes T_c in terms of the microscopic parameters.

6. **Compute critical behavior near T_c.**
   - Below T_c at h = 0: η_eq ∝ (T_c − T)^{1/2} (the β = 1/2 prediction).
   - Susceptibility χ ≡ ∂η/∂h ∝ |T − T_c|^{−1} (the γ = 1 prediction).
   - At T = T_c: η ∝ h^{1/3} (the δ = 3 prediction).

7. **Check boundary conditions** (below). Note whether the theory applies at the transition itself, far below T_c, or only in a narrow window near T_c.

8. **Generate predictions.**
   - What is the shape of the phase boundary?
   - What are the predicted critical exponents?
   - How should thermodynamic data collapse under the scaling variables defined by Landau?
   - Where does the theory fail (and what complementary model is needed)?

## Boundary Conditions

Landau Theory is a leading-order expansion near the critical point and breaks down or becomes misleading in several regimes:

- **Far from criticality (|T − T_c| ≫ T_c).** The free-energy expansion diverges; higher-order terms and non-analytic contributions (e.g., latent heat in first-order transitions) dominate. Landau is reliable only in a window of order ∼0.1 T_c or smaller around T_c. For phase diagrams spanning wide temperature ranges, use equation-of-state data or simulation.

- **Three-dimensional critical exponents do not match Landau's predictions.** Experiments on ferromagnets, liquids, and superfluids show β ≈ 0.3 (not 0.5), α ≈ 0.1 (not 0), γ ≈ 1.2 (not 1), and δ ≈ 4.8 (not 3). This is the **failure of mean-field theory**: Landau neglects thermal fluctuations and correlations that become long-ranged at the critical point. Near criticality in 3D, use renormalization-group results or experimental data; Landau's exponents are qualitatively correct only in high dimensions (d > 4) or for very special systems.

- **First-order transitions (b(T) < 0 or b(T) = 0).** If the quartic coefficient is negative or vanishes, the free energy has a different structure: the phase transition becomes discontinuous (first-order), and Landau's predictions for continuous transitions do not apply. Detect this by examining whether b(T) changes sign; if so, invoke a more general theory or data.

- **Strong fluctuations (near-zero stiffness or soft order parameter).** Superconductors with low superfluid stiffness or systems with very weak restoring forces (e.g., smectic ordering in liquid crystals) are dominated by topological defects and fluctuations; Landau is insufficient. Supplement with a defect-based or fluctuation-based theory.

- **Competition between order parameters.** If two or more order parameters (e.g., charge and spin density waves) are nearly degenerate in energy, the Landau expansion must include their cross-coupling. Single-order-parameter Landau becomes inaccurate; use a multi-component theory.

- **Time-dependent or driven systems.** Landau is an equilibrium theory. Non-equilibrium phase transitions (e.g., jamming, active matter) have a different phenomenology; equilibrium Landau does not apply.

## Output Format

```
## Landau Theory Analysis: <phase transition name>

**Transition:** <disordered → ordered phase, one sentence>
**Order parameter η:** <scalar / vector, physical interpretation>
**Critical point:** T_c = <value or expression>; h_c = <value or expression>
**Symmetry broken:** <which symmetry>

### Landau free energy
F(η, T, h) = a(T)η² + b(T)η⁴ + ... − hη

where:
- a(T) ≈ a′(T − T_c), a′ = <value or sign>
- b(T) ≈ <const or T-dependent expression>
- higher terms: <kept or neglected>

### Equilibrium order parameter
Below T_c at h = 0: η_eq = <expression in T, T_c>
Susceptibility: χ = ∂η/∂h ∝ |T − T_c|^<exponent>

### Predicted critical exponents
| Exponent | Prediction | Experiment (if known) |
|---|---|---|
| β | 0.5 | <value or "not measured"> |
| α | 0 (log divergence) | ... |
| γ | 1 | ... |
| δ | 3 | ... |

### Phase diagram sketch
<qualitative description: phase boundary shape, stable vs. unstable regions, field dependence>

### Scaling prediction
Near T_c, all thermodynamic functions depend only on the scaled variables: (T − T_c)/T_c and h/|T − T_c|^<exponent>. Data should collapse.

### Boundary-condition notes
- Applicable regime: <e.g., "|T − T_c|/T_c ≲ 0.1">
- Fails if: <which of the boundary conditions above are violated>
- Complementary model needed: <renormalization group, simulation, etc., if applicable>

### Confidence: high | medium | low
<reasoning: how close is the system to the critical point, dimensionality, presence of competing order parameters, availability of data to test predictions>
```
---
