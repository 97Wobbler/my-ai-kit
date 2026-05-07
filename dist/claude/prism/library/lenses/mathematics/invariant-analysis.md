---
name: invariant-analysis
display_name: Invariant Analysis
class: lens
underlying_class: native
domain: mathematics
source: Emmy Noether (Noether's Theorem, 1915); formalized in physics, computer science, and constraint solving
best_for:
  - Finding hidden structure in dynamic systems
  - Proving properties that hold regardless of execution path
  - Simplifying proofs by identifying what cannot change
one_liner: "Find quantities that do not change to reveal the essential structure of a problem."
---

# Invariant Analysis

## Overview
An invariant is a quantity, property, or relationship that remains true before, after, or throughout some process. Instead of tracking every state transition (which grows combinatorially), identify what *cannot* change and use it to constrain the solution space. Practitioners use this lens when a problem's state space is too large to enumerate, when a direct proof feels brittle, or when they suspect the system's real degrees of freedom are fewer than apparent.

## Analytical Procedure

### Phase 1 — Identify Candidate Invariants

1. **State the system and its transitions.** Write:
   - Initial state (or initial condition)
   - All operations/transformations that change the state
   - Final state (or goal condition)
   - Example: "Sorting: array of n integers → swap adjacent elements → array in ascending order"

2. **List quantities that *appear* to be preserved.** For each operation, ask: "What about the state stayed the same?" Write down everything you notice, including the obvious (e.g., "the number of elements," "the set of elements"). Do not filter yet.
   - Example for sorting: number of elements, multiset of values, some partial orderings

3. **For each candidate, run it through the full sequence of operations.** Trace at least one concrete example by hand. If the quantity changes during any operation, cross it off. If it holds through the full sequence, mark it as a **confirmed invariant**.
   - Example: "number of elements" — stays same through swaps ✓. "array is sorted" — false initially, true at end, so NOT an invariant.

4. **Separate strong invariants from weak ones:**
   - **Strong:** True at every intermediate step, including before and after each single operation
   - **Weak:** True before and after a *sequence* of operations but may be violated in between
   Only strong invariants are usually useful for proofs; weak invariants can guide algorithm design.

### Phase 2 — Prove Invariant Preservation

5. **For each strong invariant, prove it is preserved by each operation.** Structure: "If the invariant holds before operation X, does it hold after?" Write a short logical argument (2-4 sentences). This is the crux.
   - Example: "If the multiset of values is S before a swap, and we exchange two elements, the multiset S is unchanged after. Therefore, multiset preservation is invariant under swaps."

6. **Prove the invariant holds initially.** Verify the invariant is true in the starting state (or initial condition). If it isn't, it's not a valid invariant for this system.

7. **Trace through one non-trivial execution path.** Pick a realistic sequence of operations and verify the invariant at each step. This catches logical errors in the preservation proof.

### Phase 3 — Exploit the Invariant

8. **State what the invariant implies about the final state.** Combine:
   - The invariant (what must be true)
   - The termination condition (when operations stop)
   - → What can you conclude about the result?
   - Example: "Multiset invariant + 'no more swaps possible' → the array contains the same elements but now sorted."

9. **Identify what the invariant rules out.** What states are *impossible* given the invariant? This constrains the search space and can eliminate wrong approaches.
   - Example: "If the multiset invariant holds, it's impossible for the algorithm to create or destroy elements, so we can't 'fix' a sort by ignoring outliers."

10. **Check for auxiliary invariants that strengthen the result.** Are there secondary quantities that, together with the main invariant, narrow the solution further?
    - Example in sorting: multiset invariant + "at each step, the rightmost k elements are ≥ all others" → stronger bound on progress.

## Evaluation Criteria

| Check | Pass |
|---|---|
| System and its operations are stated precisely | Y/N |
| At least 3 candidate invariants were identified | Y/N |
| Each confirmed invariant was traced through a concrete example | Y/N |
| Each strong invariant has a preservation proof for every operation | Y/N |
| Invariant holds in the initial state | Y/N |
| At least one auxiliary or secondary invariant was identified | Y/N |
| Final state implications follow logically from the invariant | Y/N |

## Red Flags

- All candidates turn out to be trivial (e.g., "the algorithm terminates"). The invariant was too weak to guide reasoning.
- Preservation proofs are hand-wavy ("it seems like it should stay true"). Vague means the invariant may not actually hold under all operations.
- The invariant is defined *in terms of* the solution (e.g., "the array remains closer to sorted"). That's circular — the invariant should be independent of what we're trying to prove.
- No weak invariants emerged, only strong ones. This can indicate the system is simpler than suspected, but also that the search for structure was shallow.
- The invariant is true but tells you nothing new about the final state. If the implication in Phase 3 is empty, the invariant is decorative.
- Termination condition is unstated. An invariant without a stopping rule doesn't guarantee the process finishes or reaches the goal.

## Output Format

```
## Invariant Analysis

**System description:**
- Initial state: <...>
- Operations: <...>
- Goal/final state: <...>

### Phase 1 — Candidate Invariants
| Candidate | Holds through sequence? | Strong or weak? |
|---|---|---|
| <...> | Yes/No | Strong/Weak/N/A |

### Phase 2 — Preservation Proofs
**Invariant 1: <statement>**
- Preserved by operation A: <argument>
- Preserved by operation B: <argument>
- Holds initially: <verification>

### Phase 3 — Exploitation
**What the invariant(s) imply:**
- About final state: <...>
- Impossible states ruled out: <...>
- Auxiliary invariants: <...>

### Key Insight
<One sentence connecting the invariant to the problem's solution or structure.>

### Confidence
<high/medium/low> — <justification>
```
