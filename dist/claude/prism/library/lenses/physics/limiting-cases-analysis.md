---
name: limiting-cases-analysis
display_name: Limiting Cases Analysis
class: lens
underlying_class: native
domain: physics
source: George Pólya (How to Solve It, 1945); standard technique in mathematical physics and engineering validation
best_for:
  - Validating formulas and models by testing behavior at extremes
  - Catching sign errors, missing factors, and conceptual inconsistencies
  - Building confidence in derived equations before full implementation
one_liner: "Probe formulas at extreme values to catch derivation errors and physical inconsistencies."
---

# Limiting Cases Analysis

## Overview
A formula or model derived from first principles is only as good as the cases where its behavior is obviously correct. Limiting Cases Analysis tests a derived expression by evaluating it at extreme values of its parameters — boundary conditions where the answer is known or physically intuitive — to catch algebraic errors, missing factors, sign flips, and conceptual inconsistencies before the formula is used in design or simulation. Practitioners use this when a derivation is complete but not yet trusted, or when comparing a new formula to an existing one.

## Analytical Procedure

### Phase 1 — Identify Limiting Cases

1. **List all parameters in the formula.** Include both the variables (things that change during use) and the constants or material properties (things that are fixed for a given system).

2. **For each parameter, identify the physically natural limits:**
   - **Zero limit:** What should happen if this parameter becomes zero or vanishes?
   - **Infinity limit:** What should happen if this parameter grows without bound?
   - **Boundary/symmetry case:** Are there special values (e.g., 90°, 1, exact balance) where physical intuition or a simpler law gives the answer directly?
   
   Write down the physical intuition for each case. Do not yet evaluate the formula.

3. **Choose the 3–5 most revealing cases.** Prioritize:
   - Cases where a parameter completely dominates or disappears, isolating a single effect.
   - Cases where you can compare against a well-known special case (e.g., circular symmetry reduces to 2π; frictionless motion becomes conservation of energy).
   - Cases where dimensional analysis or a simpler model gives a known answer.

### Phase 2 — Evaluate the Formula at Limits

4. **Substitute each limiting case into the formula algebraically.** Simplify completely. Do not use numerical approximation here — work symbolically so errors are visible.

5. **Check the simplified result against your physical intuition from Step 2.** Does the formula give the expected behavior?
   - **Match:** The formula simplifies to the expected result (or a multiple of it, or the reciprocal — note the difference).
   - **Mismatch:** The formula does not simplify to the expected result.
   - **Indeterminate:** The simplified form is ambiguous (e.g., 0/0, ∞/∞). Apply L'Hôpital's rule or re-examine the derivation.

6. **If there is a mismatch, do NOT assume the formula is wrong.** Instead:
   - Check whether your physical intuition for that limit is actually correct. (You may be wrong.)
   - Re-derive the formula to find where the unexpected term originated.
   - Check units and dimensional consistency (a separate lens).
   - If the formula is indeed in error, identify the step in the derivation where the error entered.

### Phase 3 — Document and Assess Confidence

7. **For each limiting case, record:**
   - The case (parameter values or ratio).
   - Your pre-evaluation physical expectation.
   - The formula's simplified result.
   - Match/Mismatch/Indeterminate.
   - Any resolution or caveats.

8. **Assign a confidence level to the formula:**
   - **High:** All limiting cases matched intuition; formula is dimensionally sound; result is consistent with known special cases.
   - **Medium:** Most limits matched; one or two required deeper investigation but were resolved; no outstanding contradictions.
   - **Low:** Multiple limits either mismatched or remain unexplained; formula's behavior at extremes is counterintuitive and unresolved.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All parameters of the formula identified | Y/N |
| At least 3 limiting cases identified (zero, infinity, boundary, or symmetry) | Y/N |
| Physical intuition for each case stated before evaluation | Y/N |
| Formula algebraically simplified at each limit (symbolic, not numerical) | Y/N |
| Each result compared to intuition and tagged Match/Mismatch/Indeterminate | Y/N |
| All mismatches investigated and resolved or documented | Y/N |
| Confidence level assigned with explicit justification | Y/N |

## Red Flags

- A limiting case is skipped or deflected ("that case never occurs in practice"). If it never occurs, it's safe to test; if it does occur, it must be understood.
- The simplified form at a limit is stated without showing algebraic steps. Errors often hide in the simplification.
- A mismatch is acknowledged but not investigated — the formula is called "good enough" without resolution. This defers the error to later, more expensive stages.
- All cases "match" but the formula is counterintuitive or differs from a published reference. Suspect that intuition was retrofitted to match the result rather than independently formed.
- Confidence is assigned as "high" without any mismatch investigation or dimensional analysis performed.
- The formula is compared only to itself (e.g., "this simplified form matches the formula"). Compare to known physical laws or simpler models.

## Output Format

```
## Limiting Cases Assessment

**Formula:**
<equation or expression under test>

**Parameters:**
- <parameter name> (type, units)
- <parameter name> (type, units)
...

### Limiting Cases Evaluated

| Case | Parameter/Ratio | Physical Intuition | Formula Simplified | Match? | Notes |
|---|---|---|---|---|---|
| Zero limit of <param> | <param> → 0 | <expected behavior> | <simplified result> | Y/N/Indet | <resolution or caveat> |
| Infinity limit of <param> | <param> → ∞ | <expected behavior> | <simplified result> | Y/N/Indet | <...> |
| Boundary: <condition> | <values> | <expected behavior> | <simplified result> | Y/N/Indet | <...> |

### Dimensional Analysis
- Expected dimensions (from physics/engineering principle): <...>
- Formula dimensions: <...>
- Match: Y/N

### Known Special Cases
| Special Case | Expected Result | Formula Gives | Status |
|---|---|---|---|
| <e.g., circular symmetry> | <known answer> | <formula output> | Match/Mismatch |

### Summary of Findings
<List any mismatches or unresolved indeterminate forms. If all cases matched, state that.>

### Confidence
<high | medium | low> — <justification: cite which cases matched, which required investigation, any outstanding concerns>
```
---
