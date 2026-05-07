---
name: feynman-technique
display_name: Feynman Technique
class: lens
underlying_class: native
domain: personal-knowledge-management-pkm
source: Richard Feynman (1918–1988); popularized in "Surely You're Joking, Mr. Feynman!" and physics pedagogy
best_for:
  - Testing depth of understanding by explaining to a non-expert
  - Identifying gaps in knowledge before teaching or publishing
  - Simplifying complex concepts for retention and clarity
one_liner: "Test understanding by checking whether you can explain a concept at a child's level."
---

# Feynman Technique

## Overview

The Feynman Technique exposes gaps in understanding by forcing you to explain a concept in plain language, as if to a bright child with no background. If you cannot explain it simply, you do not understand it deeply — you are either using jargon as a mask for incomplete knowledge or relying on memorization rather than intuition. Practitioners use this to audit their own learning before teaching others, publishing, or making decisions that depend on the concept.

## Analytical Procedure

### Phase 1 — Prepare and Select

1. **Choose a single concept or topic.** It must be concrete enough to fit in a few sentences but complex enough to deserve scrutiny. Bad targets: "leadership" (too vague). Good targets: "how photosynthesis converts light into glucose" or "why fractional reserve banking multiplies deposits."

2. **Gather your current understanding.** Write or speak aloud a 2-3 minute explanation of the concept as you currently understand it. Use whatever language comes naturally — jargon, equations, all of it. This is your baseline.

### Phase 2 — Explain to a Child

3. **Rewrite or re-explain the concept in language a 12-year-old would understand.** Rules:
   - No jargon. If you must use a technical term, define it in one sentence using only common words.
   - No equations. Use concrete examples instead.
   - No nested clauses. Short, clear sentences.
   - Use analogies sparingly and only if they actually clarify (not if they obscure).

4. **Read it aloud or teach it to an actual child, peer, or rubber duck.** A rubber duck method works: speak it aloud as if teaching. Pause when you get stuck. That pause is a gap.

5. **Record where you stalled or hedged.** Mark every moment where you:
   - Used a technical term you couldn't explain without that term
   - Said "it's complicated" or "basically" and moved on
   - Used an analogy that doesn't quite work
   - Realized you were repeating what you memorized, not explaining why

### Phase 3 — Identify and Close Gaps

6. **For each stall point, ask: What do I actually not know here?** Possible answers:
   - I don't know the mechanism (how it works)
   - I don't know the why (reason or cause)
   - I don't know a prerequisite concept I assumed was obvious
   - I can't distinguish this from a similar concept
   - I've never seen it applied to a real situation

7. **Go back to sources.** For each gap, read, ask, or experiment until you can explain that piece simply. Do not move on until the gap closes or you document exactly what remains uncertain.

### Phase 4 — Refine and Test

8. **Rewrite the explanation.** Incorporate what you learned in Phase 3. It should now be simpler and more honest about what you do and don't know.

9. **Test against edge cases.** Ask: Does this explanation hold up if someone asks:
   - When does this NOT work or apply?
   - What is the opposite or counterexample?
   - How do you know this is true?
   - How does this connect to something I already know?

10. **Rate your final explanation.** Does it now satisfy the standard: a literate 12-year-old or a peer in a different field could follow it and grasp the core idea?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Baseline explanation recorded (before simplification) | Y/N |
| Simplified explanation uses no unexplained jargon | Y/N |
| Simplified explanation avoids equations; uses examples instead | Y/N |
| At least one stall point identified and documented | Y/N |
| Gap analysis performed for each stall point (mechanism/why/prerequisite/distinction/application) | Y/N |
| Sources consulted to close gaps | Y/N |
| Refined explanation tested against 2+ edge cases | Y/N |
| Final explanation is shorter and clearer than baseline | Y/N |

## Red Flags

- No stall points identified. Either the concept is trivial or you are overconfident. Try explaining it to a real person; they will expose gaps.
- Gaps identified but not closed. "I don't understand why X works" is an honest start, but the phase ends when you've learned why, not when you've identified the question.
- The simplified explanation is nearly as long and complex as the baseline. Simplification failed — you are filtering jargon, not actually teaching understanding.
- Analogies are used repeatedly or are more complex than the concept itself. Analogies are bridges, not substitutes. If an analogy needs its own explanation, it is not helping.
- Final explanation appeals only to authority ("X works because physicists say so"). Authority is not understanding. Understanding predicts and explains.

## Output Format

```
## Feynman Technique Assessment

**Concept:**
<concept name and one-sentence scope>

### Phase 1 — Baseline Explanation
<Original explanation as written/spoken, including jargon and equations>

### Phase 2 — Simplified Explanation
<Rewritten explanation in child-accessible language>

### Stall Points Identified
| Where I stalled | Type of gap | What I didn't know |
|---|---|---|
| <phrase or moment> | mechanism/why/prerequisite/distinction/application | <specific unknown> |

### Phase 3 — Gap Closure
| Gap | Source consulted | What I learned |
|---|---|---|
| <...> | <source> | <resolution or remaining uncertainty> |

### Phase 4 — Refined Explanation
<Updated explanation incorporating Phase 3 learning>

### Edge Case Tests
1. When does this NOT apply? <answer>
2. What is a counterexample? <answer>
3. How do I verify this is true? <answer>
4. How does this connect to <prior knowledge>? <answer>

### Resilience Score
- Baseline jargon-free? yes/no
- All gaps closed? yes/partial/no
- Explanation passes edge cases? yes/some/no
- Verdict: <fully understood | partially understood | significant gaps remain>

### Confidence
<high/medium/low> — <justification (e.g., "high — explained to a peer and they understood; edge cases hold; sources align; no remaining gaps")>
```
