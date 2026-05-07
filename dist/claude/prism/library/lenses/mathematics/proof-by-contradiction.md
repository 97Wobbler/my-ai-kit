---
name: proof-by-contradiction
display_name: Proof by Contradiction
class: lens
underlying_class: native
domain: mathematics
source: Aristotle (Prior Analytics); formalized in classical logic; foundational in mathematical proof
best_for:
  - Proving statements when direct construction is intractable
  - Establishing impossibility or necessity results
  - Testing whether a claim is internally consistent
one_liner: "Prove a proposition by assuming its negation and deriving a contradiction."
---

# Proof by Contradiction

## Overview
To prove a claim *P* true, assume *P* is false and derive a logical contradiction. The contradiction forces *P* to be true, since the alternative is impossible. The discipline is rigorous tracking of what you've assumed, what follows necessarily from those assumptions, and where exactly the contradiction arises. Practitioners use this when a direct proof feels elusive and they suspect the negation of the claim admits a simpler path to absurdity.

## Analytical Procedure

### Phase 1 — Setup

1. **State the claim *P* in one sentence with no ambiguity.** Identify what exactly you are trying to prove. If the claim has quantifiers ("for all *x*..." or "there exists *y*..."), write them explicitly. Use logical notation if needed.

2. **State the negation ¬*P* explicitly.** If *P* is "all primes greater than 2 are odd," then ¬*P* is "at least one prime greater than 2 is even." Write both versions in plain language to confirm they are genuine opposites.

3. **List all premises, axioms, and background facts you are allowed to use.** These are your fixed assumptions — you will add ¬*P* temporarily, but these background facts stay throughout. Mark any premise you are uncertain about as "assumed but unverified."

### Phase 2 — Derivation

4. **Add ¬*P* to your list of working assumptions.** You now have: {background facts} ∪ {¬*P*}.

5. **Derive consequences step by step.** For each step, write:
   - The new statement you derive
   - Which prior statements (or background fact) you used to derive it
   - Which logical rule (modus ponens, universal instantiation, algebraic manipulation, etc.) you applied
   
   This is not a sketch — each step must be justified. If you write "it follows that X," go back and show *why* it follows.

6. **Track the logical chain.** Keep a running list of statements you have now established:
   - Statement 1 (derived from ___)
   - Statement 2 (derived from ___)
   - ... and so on

7. **Continue until you reach a contradiction.** A contradiction is one of:
   - A statement *Q* and its negation ¬*Q* both derived (explicit contradiction)
   - A statement that violates a background axiom (e.g., deriving 1=0 when working in a field)
   - A statement that contradicts a premise you listed in Phase 1 (violation of background facts)

   Mark the exact line where contradiction appears.

### Phase 3 — Validation

8. **Verify no logical errors in the chain.** Go back through your derivation. At each step, ask: "Is this step valid in the logical system I'm working in?" If you used algebra, did you apply the rules correctly? If you used set theory, did you respect the axioms of your set theory?

9. **Check that ¬*P* was genuinely necessary to the contradiction.** Remove ¬*P* from your list of working assumptions and ask: "Would this contradiction arise without it?" If yes, then the contradiction doesn't depend on ¬*P*, and your proof is broken. If no, then ¬*P* caused the contradiction, which means *P* must be true.

10. **Confirm the contradiction is non-recoverable.** A contradiction in classical logic cannot be resolved by weakening premises or reinterpreting terms — it signals fundamental incompatibility. If there is any way to revise ¬*P* slightly and avoid the contradiction, you have not actually derived a contradiction; you have derived a constraint.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Claim *P* and its negation ¬*P* are both stated explicitly and are genuine opposites | Y/N |
| All background axioms, premises, and definitions are listed | Y/N |
| Every derivation step cites the prior statement(s) and the logical rule applied | Y/N |
| The chain of reasoning contains no gaps (no "obviously follows" without justification) | Y/N |
| A contradiction is explicitly identified | Y/N |
| Removing ¬*P* eliminates the contradiction (proof that ¬*P* was essential) | Y/N |
| No unintended background assumptions were introduced mid-derivation | Y/N |

## Red Flags

- The contradiction is vague ("this leads to weird results") rather than formal. A valid contradiction is precise and checkable.
- The derivation feels long and indirect. Some proofs by contradiction are necessarily long, but if each step feels arbitrary or unmotivated, the proof may be straining against a better direct approach.
- The statement ¬*P* is asymmetrical to *P* — they are not true opposites. For example, proving "*x* is positive" by deriving a contradiction from "*x* is negative" works only if those are the only options; if *x* could be zero, the proof is incomplete.
- Multiple contradictions are derived but appear in different branches of the reasoning. This suggests the derivation is not cleanly controlled; a single unified contradiction is the standard.
- The "background facts" section is vague or was added mid-proof. This is often a sign that unstated assumptions are doing work. Make them explicit.
- No attempt to verify that ¬*P* was necessary (Phase 3, step 9). Without this check, the contradiction may have arisen from a background fact alone, not from ¬*P*.

## Output Format

```
## Proof by Contradiction Assessment

**Claim (*P*):**
<one sentence, no ambiguity>

**Negation (¬*P*):**
<explicit negation in plain language>

### Background Facts & Axioms
- <fact or axiom>
- <fact or axiom>
- ...

### Derivation Chain (with *P* assumed false)

**Working assumptions:** {background facts} ∪ {¬*P*}

1. <statement 1> [from <prior> via <rule>]
2. <statement 2> [from <prior> via <rule>]
3. ...
N. <contradiction: *Q* and ¬*Q*> [from <prior> via <rule>]

### Validation

**Contradiction type:** <explicit contradiction | axiom violation | premise violation>

**Is ¬*P* essential to the contradiction?** 
Yes — removing ¬*P* eliminates statement N above. [or: No — <explain>; proof is invalid]

**Logical system used:** <classical logic | intuitionistic logic | set theory (specify axioms) | other>

### Confidence
<high | medium | low> — <justification: e.g., "high — each step is justified in standard first-order logic and the contradiction is formal, not semantic" or "medium — the derivation is correct but assumes the axiom of choice, which some mathematicians reject">
```
