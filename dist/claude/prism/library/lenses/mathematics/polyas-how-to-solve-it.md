---
name: polyas-how-to-solve-it
display_name: Polya's How to Solve It
class: lens
underlying_class: native
domain: mathematics
source: George Pólya, "How to Solve It" (1945)
best_for:
  - Systematic problem-solving when you're stuck or unsure where to start
  - Structuring solutions to novel or unfamiliar problem types
  - Teaching problem-solving discipline to others
one_liner: "Four-phase iterative problem solving — understand, plan, execute, verify."
---

# Polya's How to Solve It

## Overview
A four-stage framework for attacking a mathematical (or any structured) problem: **Understand** the problem completely, **Plan** a solution strategy, **Carry out** the plan, and **Look back** to verify and extract generalizable lessons. Practitioners reach for this when facing an unfamiliar problem type, when an initial approach fails, or when teaching others to solve problems systematically rather than by lucky insight. The discipline is not cleverness — it is methodical interrogation of what you know, what you want, and what bridges them.

## Analytical Procedure

### Stage 1 — Understand the Problem

1. **Read the problem statement carefully.** Do not skim. Read it twice. Write it down in your own words — not a summary, but a restatement that uses different vocabulary. If you cannot restate it, you do not understand it yet.

2. **Identify and list the givens.** What information is explicitly provided? Write each down as a separate fact or constraint. Include numerical values, relationships, assumptions stated in the problem.

3. **Identify and list what you need to find.** What is the question asking for? Be precise: are you solving for a single number, a proof, a construction, a classification, or something else? Write it as a direct question.

4. **Check for ambiguity or missing information.** For each unknown in the problem, ask: "Is this given, directly or indirectly? Or is it something I need to determine?" If a critical piece is missing, state what assumption you are making to proceed.

5. **Represent the problem visually or symbolically.** Draw a diagram (if geometric), write equations (if algebraic), make a table (if combinatorial), or sketch a graph. External representation often exposes unstated structure.

6. **Restate the problem as a bridge question:** "Given [givens], find [unknown] such that [constraint]." This phrasing separates what you know from what you seek.

### Stage 2 — Devise a Plan

7. **Recall similar problems you have solved.** What problem from your past experience resembles this one? What was the solution method? Write the problem and method down, even if it's not a perfect match.

8. **List candidate strategies.** Common problem-solving strategies include:
   - **Work backward** from the desired answer to the givens
   - **Reduce to a simpler case** (fewer variables, smaller numbers, special case)
   - **Decompose** the problem into subproblems
   - **Use analogy** with a solved problem in a different domain
   - **Introduce new elements** (auxiliary variables, constructions, definitions) to make the structure visible
   - **Try a systematic search** or exhaustive enumeration
   - **Look for patterns** in small cases to guess the general form
   - **Assume the opposite** and derive a contradiction (proof by contradiction)

9. **Select the most promising strategy.** For each candidate, ask: "Is there evidence this strategy *could* work? What would I need to know to apply it?" Pick the one with the clearest path forward. If none feels certain, choose the simplest to attempt first.

10. **Outline the plan in pseudocode or rough steps.** Write a numbered outline of what you will do, without executing yet. If the plan is vague at any step (e.g., "then simplify"), refine it now. Vagueness at planning stage often means vagueness will hit you during execution.

### Stage 3 — Carry Out the Plan

11. **Execute each step of the plan in order.** As you work, check each calculation or logical move. Do not skip steps — even if a move seems obvious, write it down. This catches errors and allows you to retrace your steps if something goes wrong.

12. **If you get stuck on a step, pause and ask: "Did I misunderstand the problem in Stage 1? Did I choose a flawed strategy in Stage 2?"** Return to the relevant stage and revise. Do not grind on a single approach indefinitely.

13. **Verify each intermediate result.** After each meaningful calculation or proof move, ask: "Does this make sense? Is it consistent with the problem givens? Could I have made an error?" Spot-check with a concrete example if possible.

14. **When you reach a candidate answer, stop.** Do not assume it is correct yet.

### Stage 4 — Look Back

15. **Verify the answer.** Substitute it back into the original problem. Does it satisfy all constraints? If the problem asked for a proof, re-read your argument to ensure every step follows logically. If the problem asked for a construction, test it with the givens.

16. **Ask: "Is this answer reasonable?"** If the problem asks for a distance and you get a negative number, or a probability greater than 1, something is wrong. Compare the answer to analogous problems: is it the expected order of magnitude?

17. **Trace a different path to the answer.** If time permits, solve the problem using a different strategy. If you get the same answer, confidence rises. If you get a different answer, one of the methods contains an error.

18. **Extract the general principle.** Ask: "What was the key insight in this problem? Why did the chosen strategy work? What class of problems would benefit from the same approach?" Write this down — it becomes part of your problem-solving repertoire.

19. **Check your work for clarity and elegance.** Can the solution be written more concisely? Are there unnecessary steps? A well-organized solution is easier to verify and to teach.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem restated in own words | Y/N |
| All givens listed explicitly | Y/N |
| Unknown/goal stated as a precise question | Y/N |
| Visual or symbolic representation created | Y/N |
| At least 2 candidate strategies identified | Y/N |
| Plan outlined in pseudocode before execution | Y/N |
| Each step of execution recorded (not skipped) | Y/N |
| Candidate answer verified against original problem | Y/N |
| Reasonableness check performed (sign, magnitude, units) | Y/N |
| General principle extracted and recorded | Y/N |

## Red Flags

- Stage 1 is skipped or rushed; the solver jumps into algebraic manipulation without understanding the givens. This leads to solving the wrong problem.
- Stage 2 produces only one strategy, or strategies that are vague ("just try things"). Lack of planning discipline correlates with false starts and wasted effort.
- Execution (Stage 3) contains a "lucky guess" or unmotivated leap. If the solver cannot explain why a move was made, the plan was not clear enough.
- The answer is never verified in Stage 4; the solver assumes correctness. Verification finds errors that would be embarrassing later.
- The solver declares the problem solved but cannot extract or state what was learned. The framework becomes a checklist rather than a discipline.
- The solution is correct but opaque — steps are hard to follow. An unreadable solution cannot be taught or debugged.

## Output Format

```
## Polya's Problem-Solving Assessment

### Stage 1 — Understanding

**Problem (restated in own words):**
<restatement>

**Givens:**
- <fact 1>
- <fact 2>
...

**Unknown/Goal:**
<precise statement of what is to be found or proved>

**Bridge question:**
Given [givens], find [unknown] such that [constraints].

**Representation:**
<diagram, equation, table, or symbolic form>

### Stage 2 — Planning

**Similar problems recalled:**
- <problem and method>
...

**Candidate strategies:**
1. <strategy name and brief rationale>
2. ...

**Selected strategy:**
<strategy chosen and why>

**Plan outline (pseudocode):**
1. <step>
2. <step>
...

### Stage 3 — Execution

**Work:**
<step-by-step calculation or proof, with checkpoints>

**Intermediate result verification:**
- Step X: <check performed>
...

**Candidate answer:**
<result>

### Stage 4 — Verification

**Substitution check:**
<verification that answer satisfies original constraints>

**Reasonableness check:**
<magnitude, sign, units, comparison to analogous problems>

**Alternative path (if attempted):**
<result using different strategy; comparison to primary answer>

**General principle extracted:**
<key insight and class of problems it applies to>

### Confidence
<high | medium | low> — <justification>
```
