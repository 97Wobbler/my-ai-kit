---
name: mathematical-induction
display_name: Mathematical Induction
class: lens
underlying_class: native
domain: mathematics
source: Origin uncertain; formalized by Peano (1889), foundational in proof theory
best_for:
  - Proving statements that hold for all natural numbers
  - Verifying recursive algorithms and data structures
  - Establishing properties of sequences and series
one_liner: "Prove a proposition for all natural numbers via base case and inductive step."
---

# Mathematical Induction

## Overview
Mathematical induction is a proof technique for establishing that a statement holds for all natural numbers (or elements in any well-ordered set). The method consists of two parts: proving the statement is true for a base case (usually n=1 or n=0), then proving that if it holds for an arbitrary value k, it must also hold for k+1. Practitioners use induction to prove properties of algorithms, closed-form formulas for sums, divisibility rules, and structural properties of recursive objects. The discipline is ensuring both the base case is genuine and the inductive step does not smuggle in assumptions.

## Analytical Procedure

### Phase 1 — Formulate the Claim

1. **State the claim as a predicate P(n).** Write it in the form "For all n ≥ n₀, P(n) is true." If the claim is stated informally (e.g., "the sum of the first n numbers"), translate it to a mathematical equation:
   - Bad: "Adding up the numbers 1 to n gives something."
   - Good: "For all n ≥ 1, 1 + 2 + ... + n = n(n+1)/2."

2. **Identify the base case value n₀.** This is usually 1 or 0, but could be any integer. Verify that the claim makes sense at this value — the claim must not be undefined or nonsensical at n₀.

### Phase 2 — Prove the Base Case

3. **Substitute n = n₀ into P(n) and verify the statement is true.** Show all arithmetic or algebraic steps. The base case is a direct computation, not a proof sketch.
   - If P(n₀) is false, the induction fails immediately. Stop and reconsider the claim.
   - If P(n₀) depends on another unproven claim, note this as a dependency.

### Phase 3 — Prove the Inductive Step

4. **State the inductive hypothesis (IH) explicitly:** "Assume P(k) is true for some arbitrary k ≥ n₀."

5. **Write down what P(k) says (the IH) and what you must prove: P(k+1).** Keep both visible; do not lose track of the target.
   - IH: P(k) = <statement substituting k for n>
   - Goal: P(k+1) = <statement substituting k+1 for n>

6. **Derive P(k+1) from P(k) step by step.** Each step must be justified:
   - Algebraic manipulation (name the rule: distributive, commutative, etc.)
   - Arithmetic simplification
   - Application of a previously proven lemma or theorem
   - Application of the inductive hypothesis
   - **Do NOT assume P(k+1) or any intermediate claim without justification.** This is where circular reasoning hides.

7. **Mark every use of the inductive hypothesis with a comment.** If the proof reaches the end without using the IH, the inductive step is vacuous — likely the claim is false or the proof is actually just a base case.

8. **Verify the algebraic or logical chain is continuous.** There should be no gaps between "we have X" and "therefore Y."

### Phase 4 — Closure and Scope

9. **State the conclusion:** "By mathematical induction, P(n) is true for all n ≥ n₀."

10. **Check scope:** Does the proof work only for positive integers, or does it extend to negative integers, real numbers, or other domains? If the claim involves divisibility, use of the Well-Ordering Principle, or strong induction (assuming P(j) for *all* j ≤ k, not just k), note this explicitly.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Claim P(n) is stated as a precise mathematical predicate | Y/N |
| Base case n₀ is identified and P(n₀) is computed (not left symbolic) | Y/N |
| Base case is verified to be true | Y/N |
| Inductive hypothesis is stated as a separate assumption | Y/N |
| Goal P(k+1) is explicitly written before the proof | Y/N |
| Every step in deriving P(k+1) from P(k) is justified | Y/N |
| The inductive hypothesis is used at least once | Y/N |
| No circular reasoning or unjustified leaps appear in the inductive step | Y/N |
| Conclusion restates the result with the correct scope | Y/N |

## Red Flags

- The base case is symbolic (e.g., "P(1) holds by assumption"). It must be computed concretely.
- The inductive hypothesis is never used in the inductive step. This means the step is not actually inductive — it is a universal proof that works for all n, making induction unnecessary (and suspicious).
- The inductive step assumes P(k+1) anywhere in the proof. This is circular reasoning.
- The proof uses "and so on" or "similarly" without showing the algebra. Induction proofs require every step.
- The claim is false for some value, but the "proof" proceeds anyway. (For example, proving "2^n > n^2 for all n ≥ 1" will fail at n=2, but careless induction might hide this.)
- The scope is never clarified. Does the proof work for negative integers? Reals? Only positive integers?
- The inductive step works only under an extra assumption not mentioned in P(n) (e.g., "assuming the next term is positive"). This assumption must appear in P(n) itself.

## Output Format

```
## Mathematical Induction Proof

**Claim P(n):**
For all n ≥ <n₀>, <state predicate>

### Base Case (n = n₀)
<Substitute n = n₀ into P(n) and verify.>
Result: <P(n₀) is true.>

### Inductive Step

**Inductive Hypothesis (IH):**
Assume P(k) = <statement with k>

**Goal:**
Prove P(k+1) = <statement with k+1>

**Proof:**
1. <Start from P(k) or a known result.>
2. <Apply algebra/logic with justification.>
3. [Apply IH: <how the hypothesis is used>]
4. <Continue derivation.>
...
n. <Conclude P(k+1).>

### Conclusion
By mathematical induction, P(n) is true for all n ≥ n₀.

**Scope notes:** <Clarify domain: positive integers only, or broader?>

### Confidence
<high | medium | low> — <justification: e.g., "high — base case verified, IH correctly applied, no gaps in algebra"; "medium — inductive step uses a lemma not proven in this document"; "low — circular reasoning detected in step 5">
```
