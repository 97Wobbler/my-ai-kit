---
name: dimensional-analysis
display_name: Dimensional Analysis
class: lens
underlying_class: native
domain: physics
source: Joseph Fourier (1822); formalized by Edgar Buckingham (1914); widely adopted in engineering and physics
best_for:
  - Detecting algebraic errors in equations before computation
  - Validating model structure against physical constraints
  - Inferring functional relationships when data or first principles are incomplete
one_liner: "Check equation structure via dimensional consistency of physical quantities."
---

# Dimensional Analysis

## Overview
Dimensional analysis checks whether an equation, formula, or relationship is dimensionally consistent — that is, whether the units on both sides of an equals sign (or within a function) match in a way that respects the structure of physical reality. Practitioners reach for it when they want to catch algebraic typos before running experiments, when they need to infer the form of a relationship from incomplete information, or when they suspect a model violates conservation laws. The discipline is systematic reduction to fundamental dimensions (length, mass, time, temperature, etc.) and relentless consistency checking.

## Analytical Procedure

### Phase 1 — Identify all quantities and their dimensions

1. **List every variable and constant in the equation or relationship.** Include units and, if not obvious, the physical meaning.
   - Example: `v = √(2gh)` → variables are v (velocity), g (gravitational acceleration), h (height).

2. **Reduce each quantity to fundamental dimensions.** Use the standard fundamental set: **L** (length), **M** (mass), **T** (time), **Θ** (temperature), **I** (electric current), **N** (amount of substance), **J** (luminous intensity). For most physics and engineering problems, L, M, and T suffice.
   - `v` (velocity) = L·T⁻¹
   - `g` (acceleration) = L·T⁻²
   - `h` (length) = L
   - Numerical constants (π, 2, e) have dimension **1** (dimensionless).

3. **Record the dimension of each side of the equation separately.** Do not simplify yet — keep the expression in factored form.
   - Left side: `[v]` = L·T⁻¹
   - Right side: `[√(2gh)]` = (L·T⁻²·L)^(1/2) = (L²·T⁻²)^(1/2) = L·T⁻¹

### Phase 2 — Check dimensional balance

4. **Compare the dimensions on both sides.** They must match exactly — same exponents on every fundamental dimension.
   - Left: L¹·T⁻¹
   - Right: L¹·T⁻¹
   - **Match: ✓**

5. **If dimensions do not match, flag the equation as either:**
   - **Dimensionally inconsistent** (error in algebra, typo, or physical misunderstanding)
   - **Mixing incompatible operations** (e.g., adding 5 meters to 3 seconds; adding L to T in an exponent)

6. **For compound expressions (products, quotients, exponents), apply these rules:**
   - **Multiplication:** multiply dimension exponents → `[A·B]` = `[A]`·`[B]`
   - **Division:** subtract exponents → `[A/B]` = `[A]`/`[B]`
   - **Exponentiation:** multiply exponents → `[A^n]` = `[A]^n` (n must be dimensionless)
   - **Addition/subtraction:** both operands must have identical dimensions → `[A + B]` requires `[A]` = `[B]`
   - **Logarithm, sine, cosine, etc.:** argument must be dimensionless → `[ln(A)]` requires `[A]` = **1**

### Phase 3 — Infer or validate functional form (optional advanced use)

7. **If you have an incomplete equation, use dimensional analysis to constrain its structure.** Write the suspected functional form as a product of power laws:
   - Hypothesis: `F = C·v^a·ρ^b·A^c` where C is a dimensionless constant, v is velocity (L·T⁻¹), ρ is density (M·L⁻³), A is area (L²), and F is force (M·L·T⁻²).
   - Set up dimensional equations: `M·L·T⁻²` = `(L·T⁻¹)^a·(M·L⁻³)^b·(L²)^c`
   - Separate by fundamental dimension:
     - M: 1 = b
     - L: 1 = a − 3b + 2c
     - T: −2 = −a
   - Solve the system: a = 2, b = 1, c = 1 → `F = C·v²·ρ·A` (drag force formula).

8. **Mark the result as a dimensional constraint, not a complete theory.** The form is valid; the dimensionless constant C is not determined by dimensional analysis alone and must be found by experiment or calculation.

### Phase 4 — Document findings

9. **State whether the equation passes or fails dimensional consistency.** If it fails, identify which terms or sub-expressions are problematic.

10. **For equations that pass, note any assumptions or caveats.** Are all exponents integers, or are fractional/negative exponents used? Do logarithms or trig functions appear (which require dimensionless arguments)? Are there implicit unit conversions?

## Evaluation Criteria

| Check | Pass |
|---|---|
| All variables and constants identified with explicit units | Y/N |
| Each quantity reduced to fundamental dimensions (L, M, T, etc.) | Y/N |
| Dimensions on both sides of the equation calculated separately | Y/N |
| Dimensional balance verified (exponents match on both sides) | Y/N |
| All compound operations (products, quotients, exponents) treated correctly | Y/N |
| Dimensionless operations (ln, sin, etc.) have dimensionless arguments | Y/N |
| Addition/subtraction operands have identical dimensions | Y/N |
| If inferring functional form, dimensional constraints are solved algebraically | Y/N |

## Red Flags

- A quantity is listed as "unitless" without justification. Most unitless quantities are implicitly ratios (e.g., strain, efficiency) and must be checked for hidden dimensions.
- Exponents on fundamental dimensions are left unsimplified (e.g., M^(1/2)·L^(3/2)·T⁻¹ vs. √(M·L³)·T⁻¹). Simplify before comparing sides.
- Logarithm or trigonometric function of a quantity with dimensions (e.g., `ln(5 meters)`, `sin(force)`). These are physically meaningless and indicate a modeling error.
- Dimensions balance but the equation looks physically implausible (e.g., force proportional to 1/velocity). Dimensional consistency is necessary but not sufficient; always sanity-check against physics.
- Constants introduced without declaring their dimensions (e.g., "assume k = 0.5"). If k is meant to be dimensionless, state it. If it has units, those units must be specified and included in the analysis.
- Equation involves a sum of terms with different dimensions (e.g., `E = ½mv² + mgh + F·x` has terms with dimension M·L²·T⁻² throughout, so this is fine; but `E = ½mv² + 5 seconds` would be invalid).

## Output Format

```
## Dimensional Analysis Report

**Equation or relationship:**
<verbatim statement being analyzed>

### Phase 1 — Quantities and Dimensions
| Variable | Physical Meaning | Dimension |
|---|---|---|
| <symbol> | <meaning> | <e.g., L·T⁻¹> |

### Phase 2 — Dimensional Balance
**Left side:** <dimensions>
**Right side:** <dimensions>
**Match:** <Yes / No>

### Detailed Analysis
<For each term or sub-expression, show the dimensional calculation step-by-step.>

### Findings
- **Status:** dimensionally consistent / **inconsistent** (specify which terms fail)
- **Issues (if any):** <list any dimensional violations>
- **Inferred form (if applicable):** <dimensionally constrained functional relationship>

### Confidence
<high | medium | low> — <justification. High confidence if all checks pass and calculation is straightforward. Medium if equation is complex or non-standard operations (fractional exponents, embedded functions) require extra scrutiny. Low if inconsistency is found or assumptions about unit conversions are unclear.>
```
