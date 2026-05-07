---
name: perturbation-theory
display_name: Perturbation Theory
class: lens
underlying_class: native
domain: physics
source: Rayleigh (1873); formalized by Schrödinger (1926) in quantum mechanics; generalized across physics
best_for:
  - Approximating solutions to complex systems when an exact solution is intractable
  - Validating whether small changes to a known system preserve qualitative behavior
  - Deciding whether to solve a problem exactly or accept an approximate solution
one_liner: "Approximation technique that starts from a solvable base and expands via small correction terms."
---

# Perturbation Theory

## Overview
Perturbation theory solves difficult problems by breaking them into a solved or simple part (the unperturbed system) plus a small correction (the perturbation). Instead of solving the full, intractable equation, you solve the simple one exactly, then compute successive corrections as series expansions. Practitioners use this when the exact system is too complex to solve analytically but behaves *nearly like* something simpler. The discipline is deciding what counts as "small" and detecting when the expansion breaks down.

## Analytical Procedure

### Phase 1 — Identify the Unperturbed System and Perturbation

1. **State the full problem.** Write the complete equation, Hamiltonian, differential equation, or system of interest. This is the target.

2. **Identify a solvable reference system.** Find a simpler problem that:
   - Has a known, exact solution
   - Resembles the full problem structurally (same type of equation, same degrees of freedom)
   - Differs by terms you can isolate as "small"
   Write the exact solution of the reference system explicitly.

3. **Isolate the perturbation.** Rewrite the full problem as:
   ```
   Full System = Unperturbed System + Perturbation
   ```
   The perturbation should be all the terms you dropped to get from full to unperturbed. Write it symbolically.

4. **Quantify "smallness."** Define a dimensionless parameter λ (lambda) such that:
   - When λ = 0, the full system reduces exactly to the unperturbed system
   - The perturbation scales as λ × (something with units matching the unperturbed system)
   - 0 < λ ≪ 1 in the regime of interest
   
   Examples:
   - Gravity near Earth's surface: λ = g·L / v² (where L is scale, v is velocity)
   - Atomic fine structure: λ = α² ≈ 1/137² (fine structure constant squared)
   - Weakly nonlinear oscillation: λ = amplitude of nonlinear term / amplitude of linear term

### Phase 2 — Expand the Solution

5. **Assume a power-series ansatz.** Suppose the solution can be written as:
   ```
   Solution = Solution₀ + λ·Solution₁ + λ²·Solution₂ + ...
   ```
   where Solution₀ is the unperturbed solution (known), and Solution₁, Solution₂, ... are corrections to be found.

6. **Substitute into the full equation.** Plug the ansatz above into the original problem. Group terms by powers of λ.

7. **Solve order by order.**
   - **Order λ⁰** (zeroth order): You should recover the unperturbed equation. Verify this — if you don't, the decomposition is wrong.
   - **Order λ¹** (first order): Solve for Solution₁. This will be an inhomogeneous equation whose source term depends on Solution₀ (known). Solve it.
   - **Order λ²** (second order): Solve for Solution₂. Source term depends on Solution₀ and Solution₁. Continue as needed.
   
   Each order is linear in the new unknown (even if the original is nonlinear), because you're treating the perturbation as small.

### Phase 3 — Validate and Interpret

8. **Check convergence.** Compare successive approximations:
   - Calculate |Solution₁| / |Solution₀| and |Solution₂| / |Solution₁|.
   - If both ratios are ≪ 1, the series is converging and truncating after a few terms is justified.
   - If ratios approach 1 or grow, the series diverges and the approximation is unreliable in this regime.

9. **Verify against known limits.** 
   - Set λ = 0 explicitly: does your zeroth-order solution recover exactly?
   - If possible, compare to exact solution or high-fidelity numerical result at small λ: is the error consistent with λ²-scaling (for second-order accuracy)?

10. **Assess the domain of validity.** Perturbation solutions are local: they're accurate near λ = 0 but can fail at larger λ. Determine the practical boundary:
    - The point where truncation error (term you dropped) becomes comparable to the last term you kept
    - The point where a physical quantity (energy, amplitude, decay rate) becomes unphysical (negative, infinite, etc.)
    Write this as: "Valid for λ < λ_max ≈ ___."

## Evaluation Criteria

| Check | Pass |
|---|---|
| Unperturbed system is solvable exactly (solution written down) | Y/N |
| Perturbation is isolated and λ is defined as a dimensionless quantity | Y/N |
| Ansatz is written as a power series in λ | Y/N |
| Zeroth-order equation is verified to match unperturbed problem | Y/N |
| At least first-order correction is computed (not just stated) | Y/N |
| Convergence is checked by comparing ratio of successive terms | Y/N |
| Domain of validity (maximum λ) is estimated | Y/N |

## Red Flags

- The "unperturbed system" has no known solution, only a numerical approximation. Then you're not using perturbation theory; you're perturbing numerics.
- λ is defined as a dimensional quantity or its value in the regime of interest is not ≪ 1. The whole method rests on λ being small; if it's order 1, the expansion doesn't converge.
- Zeroth-order equation does not match the unperturbed problem when λ is set to 0. The decomposition is inconsistent.
- Successive terms grow in magnitude rather than shrink. The series is diverging — truncation at any order gives wrong answer.
- The "domain of validity" is missing or vague ("valid for small perturbations"). Without an upper bound on λ, the reader doesn't know when to trust the result.
- First-order correction is stated without showing the work. Readers cannot verify it or adapt the method to similar problems.

## Output Format

```
## Perturbation Analysis

**Target system (full equation):**
<Write the equation or system to be solved>

**Unperturbed system:**
<Write the simplified reference problem>
<Exact solution: ...>

**Perturbation:**
<Decomposition: Full = Unperturbed + Perturbation>
<Perturbation term explicitly>

**Small parameter:**
λ = <definition>
λ_value ≈ <numerical value in regime of interest>

### Zeroth-Order Solution
Solution₀ = <exact solution of unperturbed system>
<Verification: Substituting back recovers unperturbed equation ✓>

### First-Order Solution
<Equation for Solution₁>
<Solution₁ = ...>

### Second-Order Solution (if needed)
<Equation for Solution₂>
<Solution₂ = ...>

### Convergence Check
|Solution₁| / |Solution₀| ≈ <ratio>
|Solution₂| / |Solution₁| ≈ <ratio>
<Series is converging / diverging / marginal>

### Domain of Validity
Truncation error becomes comparable to kept terms when λ ≈ <threshold>
**Valid for:** λ < λ_max ≈ <numerical bound>

### Approximate Solution (final)
Solution ≈ Solution₀ + λ·Solution₁ + λ²·Solution₂
= <explicit formula>

### Confidence
<high | medium | low> — <Justification: degree of convergence, how close λ is to its maximum, and whether exact solution or numerical check was available for validation>
```
