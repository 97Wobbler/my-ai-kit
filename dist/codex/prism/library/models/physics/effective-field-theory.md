---
name: effective-field-theory
display_name: Effective Field Theory
class: model
underlying_class: native
domain: physics
source: Steven Weinberg, "Phenomenology, Astrophysics and Cosmology," 1979; Kenneth G. Wilson, "The Renormalization Group and Critical Phenomena," 1971; systematized in modern form across quantum field theory and condensed-matter physics
best_for:
  - Predicting the behavior of a system at one energy scale given knowledge of a different scale
  - Identifying which degrees of freedom matter for a given physical question
  - Reducing a complex many-body or high-energy system to a simpler effective model
one_liner: "Simplify and predict complex systems by separating energy scales."
---

# Effective Field Theory

## Overview

Effective Field Theory (EFT) claims that physical systems with **widely separated energy or length scales** can be understood by focusing only on the degrees of freedom relevant to the scale of interest, discarding microscopic details that decouple at higher energies. The model is predictive: given measurements or constraints at one energy scale, EFT predicts observable quantities at lower energies without needing to solve the full microscopic theory. The central intuition is that low-energy phenomena depend on high-energy physics only through a small set of **coupling constants** (coefficients) whose values must be measured or inferred, not derived from first principles within the low-energy theory. EFT is diagnostic in the sense that it reveals which operators and scales are load-bearing for a given question, and predictive in that it reduces an intractable problem to a tractable one.

## Core Variables and Relationships

An effective field theory is built on the following structure:

1. **Energy scales and their separation.** 
   - Microscopic / UV scale Λ: the scale at which the full theory is valid (e.g., the electroweak scale ~246 GeV, or a lattice spacing in condensed matter).
   - Low-energy / IR scale E: the scale of the phenomena we want to predict.
   - **Scale hierarchy:** Λ ≫ E (typically Λ/E > 10). The larger the separation, the more decoupling occurs and the simpler the effective theory.

2. **Effective Lagrangian / Hamiltonian at scale E.**
   - Contains only **light degrees of freedom** (particles or excitations with mass < E).
   - Heavy degrees of freedom (mass > E) are integrated out and their effects appear as **operators** in the effective action.
   - The effective Lagrangian is a **power-series expansion in E/Λ**:
     
     $$L_{\text{eff}} = L_{\text{renormalizable}} + \sum_{n > 4} c_n \frac{(E/\Lambda)^{n-4}}{M^{n-4}} O_n$$
     
     where O_n are operators of dimension n, and c_n are **Wilson coefficients** (measured, not predicted in the EFT).

3. **Decoupling principle.**
   - Particles or degrees of freedom with mass M ≫ E contribute only through their **coupling constants** (or equivalently, through Wilson coefficients of higher-dimension operators).
   - The detailed structure of the heavy sector becomes irrelevant; only its effect on the light sector matters.

4. **Renormalizability and naturalness.**
   - Operators of dimension 4 (renormalizable in 4D spacetime) contribute at leading order in E/Λ.
   - Operators of dimension > 4 are suppressed by powers of E/Λ and are small when E ≪ Λ.
   - **Naturalness assumption:** Wilson coefficients of high-dimension operators are not accidentally tuned to be large; they are order 1 unless there is a reason (e.g., a symmetry) to suppress them.

5. **Running and scale dependence.**
   - Coupling constants and masses in the effective theory depend on the energy scale at which they are measured (via the **renormalization group**).
   - This scale dependence is **calculable** within EFT from the beta functions of the light degrees of freedom.
   - It allows the theory to be self-consistent across scales E₁ and E₂ if boundary conditions are matched at a reference scale.

## Key Predictions

- **Heavy particles decouple.** Once E drops below the mass of a particle, that particle's direct effects vanish (exponentially suppressed); only its "footprints" (effective couplings) remain. Example: W and Z bosons decouple below the electroweak scale, leaving only the four-fermi interaction of the Fermi theory.

- **Predictions are exponentially accurate when E/Λ is small.** If E/Λ ~ 0.01, then neglected operators of dimension 6 contribute effects ~ (E/Λ)² ~ 10⁻⁴ relative to dimension-4 terms. This makes EFT a controlled approximation: you can quantify the error.

- **Predictions become unreliable when approaching the UV scale.** As E → Λ, higher-dimension operators grow in relative importance; the expansion in E/Λ breaks down, and you must use the full theory. EFT is valid in a "window" E ≪ Λ; trying to use it to describe physics at E ~ 0.5Λ is a boundary-condition violation.

- **Matching conditions at a reference scale pin down the Wilson coefficients.** You cannot predict the coupling constants of the EFT from EFT alone; they must be extracted from:
   - Measurements at the reference scale, or
   - Integration of the full high-energy theory (if known).
   Once matched, the EFT makes predictions at all lower scales via renormalization-group evolution.

- **Model-independence below the matching scale.** Different UV completions (e.g., different grand unified theories, or different lattice models in condensed matter) that have the same symmetries and the same low-energy spectrum will give the same EFT at E ≪ Λ. This means low-energy predictions are robust across microscopic details.

## Application Procedure

Instantiate EFT against a concrete physical system and a specific low-energy question.

1. **Identify the energy scale E of the question.** What is the typical energy, momentum transfer, or excitation energy of the phenomenon you want to predict or explain? Write it down in absolute units (eV, Hz, etc.).

2. **Identify the UV scale Λ where the full theory is valid.** This is often a scale where new physics enters, or where symmetries break, or where the approximations underlying your description change. Confirm that E ≪ Λ (at least by a factor of 3–10).

3. **List the light degrees of freedom at scale E.** Which particles, excitations, or fields are kinematically accessible (mass or energy threshold below E)? Which are decoupled? This distinction is the core of EFT model selection.

4. **Write down the leading effective Lagrangian or Hamiltonian.** Include:
   - All renormalizable (dimension ≤ 4) operators of the light fields.
   - One or two operators of dimension > 4 if they are phenomenologically relevant (i.e., if their Wilson coefficient times (E/Λ)^(dim−4) is not negligibly small).
   - Leave the Wilson coefficients as unknowns to be measured or matched.

5. **Match to data or boundary conditions at a reference scale E₀.** 
   - Measure or infer the Wilson coefficients from experiments or simulations at E₀.
   - Alternatively, if the UV theory is known, integrate out the heavy degrees of freedom to compute the Wilson coefficients (this is technically involved but in principle deterministic).

6. **Use the renormalization group to evolve the couplings to the scale E of interest.** Compute the running of the couplings from E₀ to E using the beta functions of the light degrees of freedom. This step accounts for how the effective theory changes as you move to a different scale.

7. **Make the prediction.** Compute the observable of interest (e.g., a scattering cross section, a decay width, a correlation function) using the evolved couplings. The result is a prediction that is exact up to corrections of order (E/Λ)^(dim−4) for the first neglected operator.

8. **Check boundary conditions** (below). Does the scale separation hold? Are you in the decoupling regime? Will threshold effects become important? Do you have enough data to match Wilson coefficients reliably?

## Boundary Conditions

Effective Field Theory is a controlled approximation valid in a specific regime. It breaks down or becomes misleading when:

- **Scale separation is poor** (E ~ 0.3Λ or larger). The expansion in E/Λ no longer converges, and higher-dimension operators become numerically important. The EFT loses its predictive power; you must use the full theory. Example: trying to apply the Fermi theory to describe W/Z boson production near the electroweak scale.

- **New light degrees of freedom emerge near E.** If a resonance, phase transition, or symmetry change occurs at a scale close to E, particles thought to be "heavy" may suddenly become light, violating the decoupling assumption. Example: near a critical point in condensed matter, length scales diverge and the effective degrees of freedom shift.

- **Threshold effects are large.** When E is close to a particle mass threshold (e.g., E ~ m_top in electroweak physics), the approximation that the particle is either fully on-shell or fully decoupled fails. A full calculation accounting for the threshold is needed.

- **No measured boundary condition is available.** Wilson coefficients must be extracted from experiments or known input. If the reference scale is far from E and the renormalization-group flow is steep, small errors in the Wilson coefficients can amplify into large errors at E. Conversely, if you have no direct measurement of a Wilson coefficient at any accessible scale, the prediction is speculative.

- **Symmetry breaking at a scale between E and Λ.** If the symmetry structure of the EFT changes between E and Λ (e.g., a spontaneous symmetry breaking), the set of allowed operators changes discontinuously. The EFT above and below the breaking scale are formally different, and you cannot directly use renormalization-group running across the breaking point without explicit matching.

- **Non-perturbative or strongly coupled regimes.** EFT is built on perturbation theory and a power-series expansion in E/Λ. If the coupling constant at scale E is large (α > 0.1), perturbation theory fails, and the loop expansions and beta functions are unreliable. Example: the effective theory of strong-interaction hadrons at low energies (chiral perturbation theory) requires explicit input from lattice QCD or experiment because the coupling is not small.

## Output Format

```
## Effective Field Theory Analysis: <system and question>

**System:** <what physical system>
**Energy scale of interest E:** <absolute scale, units>
**UV scale Λ:** <where full theory takes over, units>
**Scale ratio E/Λ:** <numerical value>

### Light and heavy degrees of freedom
| Degree of freedom | Mass / Energy scale | Light (E > threshold)? | Decoupling status |
|---|---|---|---|
| ... | ... | Yes/No | ... |

### Effective Lagrangian / Hamiltonian
**Renormalizable terms (dimension ≤ 4):**
- <list operators and their physical meaning>

**Higher-dimension operators (if relevant):**
- <dimension, operator form, Wilson coefficient (measured or to be determined)>

### Matching and boundary conditions
- **Reference scale for Wilson coefficient measurement:** E₀ = <scale>
- **Wilson coefficients (measured or inferred):**
  - <operator>: c = <value or "to be determined">
  - ...
- **Symmetries protecting small Wilson coefficients:** <if any>

### Renormalization-group evolution
- **Beta functions of light degrees of freedom:** <direction and magnitude of coupling running>
- **Couplings at scale E (evolved from E₀):** <list>

### Prediction
- <Observable of interest>: <predicted value with uncertainty>
- **Dominant operator contributions:** <which dimension-4 or dimension-6 terms drive the result>
- **Neglected operator corrections:** <estimated size of next-order terms, (E/Λ)^(dim−4)>

### Boundary-condition check
- Scale separation adequate? Yes/No — <reasoning>
- Threshold effects important? Yes/No — <which particle/scale>
- Symmetry changes between E and Λ? Yes/No — <if yes, matching required>
- Coupling constant regime? Perturbative / marginal / non-perturbative — <consequence for reliability>

### Confidence: high | medium | low
<Reasoning: (1) How cleanly separated are E and Λ? (2) How well are Wilson coefficients measured or constrained? (3) Are any boundary conditions violated? (4) How large are the neglected-operator corrections? Confidence is high when E/Λ < 0.1, Wilson coefficients are precisely known from data, and no boundary conditions apply.>
```
