---
name: presupposition-analysis
display_name: Presupposition Analysis
class: lens
underlying_class: native
domain: philosophy
source: Philosophy of language and pragmatics — Frege on sense and reference (1892), Strawson on presupposition ("On Referring," 1950), Stalnaker on common ground and presupposition projection (1973, 1974). The lens synthesizes these into a workable checklist rather than tracking any single theorist.
best_for:
  - Claims that appear to assert one thing but silently depend on several contested background assumptions
  - Normative statements that smuggle value judgments into descriptive-sounding language
  - Policy and strategy arguments whose force collapses if a hidden structural or scope assumption fails
  - Feeding argument reconstruction by making implicit premises explicit before validity is tested
one_liner: "Surface every hidden assumption a claim requires across five categories (definitional, empirical, structural, normative, scope), judge each as strong/contested/weak, and state what the claim loses if it fails."
---

# Presupposition Analysis

## Overview

Every claim stands on a stack of things left unsaid. Some of those unsaid things are harmless — shared vocabulary, basic facts about the world — but others carry most of the claim's persuasive force while dodging inspection. This lens walks a claim through five presupposition categories, forces each hidden assumption into plain language, grades its plausibility, and says what happens to the claim if the assumption turns out to be false. The categories are chosen so that typical failure modes — equivocation (definitional), false-fact dependency (empirical), spurious binaries (structural), is-ought smuggling (normative), and overgeneralization (scope) — each have a dedicated inspection step.

## Analytical Procedure

1. **Walk the five categories in order.** For each category, ask the category-specific question of the claim. Produce zero or more presuppositions per category. Do not force a finding — if a category yields nothing, write "none identified" and move on.
   - **Definitional:** Does the claim assume that key terms have settled, shared meanings? (Does not duplicate conceptual-analysis; here, the question is specifically what the *sharedness* assumption is doing.)
   - **Empirical:** Does the claim assume facts about the world — causal regularities, base rates, historical events, technical feasibility — that are not stated?
   - **Structural:** Does the claim assume a particular structure of the domain (binary, spectrum, hierarchy, natural-kind category, discrete-state system) that might be arbitrary or contested?
   - **Normative:** Does the claim present as descriptive while relying on a value judgment — what counts as good, fair, acceptable, efficient, healthy?
   - **Scope:** Does the claim assume universal applicability when its warrant is context-dependent, or restricted applicability when its warrant would force a broader conclusion?

2. **State each presupposition explicitly.** For every presupposition found, write it as a standalone proposition in plain language — what must be true for the claim to be meaningful or true. Do not bury it inside conditional prose.

3. **Grade plausibility.** Assign each presupposition one of three grades, with a one-line basis:
   - **strong** — widely accepted within the claim's domain; the skeptic's burden would be to overturn it.
   - **contested** — serious reasons to accept it and serious reasons to doubt it; honest domain experts disagree.
   - **weak** — empirically doubtful, structurally arbitrary, or smuggles a value judgment with no defense. The claim relies on it, but it would not survive scrutiny.

4. **State failure impact per presupposition.** For each presupposition, describe what happens to the claim if that presupposition is false. Possibilities include: the claim becomes false; the claim becomes vacuous; the claim's scope shrinks dramatically; the claim flips into its opposite; the claim survives but loses rhetorical force. A presupposition whose failure has no impact is not load-bearing — either remove it or note why it was listed.

5. **Identify the weakest load-bearing presupposition.** Among presuppositions whose failure would materially damage the claim, name the one most likely to actually fail. This is the claim's primary attack surface.

6. **Summarize presuppositional load.** State the overall load as **light**, **moderate**, or **heavy**:
   - *light* — few presuppositions, most graded strong.
   - *moderate* — several presuppositions, a mix of strong and contested, at most one weak.
   - *heavy* — many presuppositions, or one or more weak-but-load-bearing. The claim is doing a lot of silent work.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All five categories (definitional / empirical / structural / normative / scope) are walked, even if empty | Y/N |
| Each presupposition is stated as a standalone proposition, not embedded in hedged prose | Y/N |
| Each presupposition has a plausibility grade with a one-line basis | Y/N |
| Each presupposition has a failure-impact statement | Y/N |
| The weakest load-bearing presupposition is named | Y/N |
| Presuppositional load is summarized (light / moderate / heavy) with justification | Y/N |

## Red Flags

- **Explicit-premise-only trap.** Only premises the claim actually states get listed; the silent ones (the point of this lens) are never surfaced. If every "presupposition" you found also appears on the face of the claim, you have not done presupposition analysis.
- **Category neglect.** Normative or structural presuppositions are skipped because the claim "looks descriptive" or "looks obvious." Is-ought smuggling and spurious binaries are the category's signature failure modes — they must be checked, not skipped.
- **Grade inflation.** Every presupposition is graded strong. Either the claim is astonishingly well-founded (rare) or the analyst refused to mark anything contested to avoid seeming tendentious.
- **Impact hand-waving.** Failure impact is written as "the claim would be weakened." Without specifying *how* — false, vacuous, narrower, reversed — the impact statement is decorative.
- **Load mismatch.** Presuppositional load is summarized as *light* despite multiple weak load-bearing presuppositions in the table. The summary must be consistent with the contents.
- **Category padding.** A category yields nothing but the analyst invents a presupposition to avoid an empty cell. An empty category is a legitimate finding; a fabricated one corrupts the load summary.

## Output Format

```
## Presupposition Analysis

**Input claim:**
<the claim being analyzed>

### Presupposition table

| # | Category | Presupposition (explicit) | Plausibility | Basis | Failure impact |
|---|---|---|---|---|---|
| 1 | definitional | <...> | strong / contested / weak | <one-line basis> | <what happens to the claim if this fails> |
| 2 | empirical | <...> | ... | ... | ... |
| 3 | structural | <...> | ... | ... | ... |
| 4 | normative | <...> | ... | ... | ... |
| 5 | scope | <...> | ... | ... | ... |
| ... | | | | | |

(If a category is empty, include a single row: `| — | <category> | none identified | — | — | — |`)

### Weakest load-bearing presupposition
<name it and state why it is most likely to fail and what the claim becomes if it does>

### Presuppositional load
[light | moderate | heavy] — <one-line justification referring to the table>

### Confidence
<high / medium / low> — <high when the five-category walk was exhaustive and every load-bearing presupposition has a grounded grade; medium when some categories required speculative reconstruction of context; low when the claim's context is opaque enough that multiple presuppositions could not be judged.>
```
