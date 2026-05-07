---
name: conceptual-analysis
display_name: Conceptual Analysis
class: lens
underlying_class: native
domain: philosophy
source: Analytic philosophy tradition, from G. E. Moore (Principia Ethica, 1903) through later Wittgenstein's language-games (Philosophical Investigations, 1953) and into contemporary experimental philosophy (X-phi). Not attributable to a single author — a method refined across a century of analytic practice.
best_for:
  - Claims whose argumentative weight rests on a single contested or ambiguous term
  - Policy, ethics, and social-science statements where the same word does different work across contexts
  - Preparing an argument for presupposition analysis or reconstruction by fixing what the words are doing first
  - Detecting unfalsifiable claims hiding behind a definition that can be shifted on demand
one_liner: "Extract each key concept in a claim, state charitable and critical definitions as a pair, map the concept's scope and edge cases, and judge whether it can be operationalized."
---

# Conceptual Analysis

## Overview

Most arguments that look substantive are actually arguments about which definition of a key term is in force. Before a claim can be evaluated as true, false, or well-supported, the concepts inside it have to be pinned down. This lens forces the analyst to surface every load-bearing concept, produce both the most charitable definition (the one the claim's defender would accept) and the most critical definition (the one a skeptic would impose), map the concept's boundary against edge cases, and decide whether the concept can be operationalized at all. Concepts that cannot be operationalized, or whose meaning slides under pressure, are flagged as vulnerabilities; downstream analysis can then target the slippage rather than the surface claim.

## Analytical Procedure

1. **Extract key concepts.** Read the claim and list every term whose meaning materially affects whether the claim holds. Skip function words (articles, conjunctions), indexicals with no dispute, and terms whose meaning is technical and uncontested in the claim's domain. A concept is "key" if replacing it with a different definition would change what the claim is asserting.

2. **For each concept, produce a paired definition.**
   - **Charitable definition:** the most defensible, well-formed meaning that a reasonable defender of the claim would offer. This is not the weakest definition — it is the one that gives the claim its best shot at being true.
   - **Critical definition:** the meaning that a skeptic or adversarial reader would assign. This is not a strawman — it is a definition that the term can sustain in ordinary usage but that makes the claim's burden heavier.
   - The two definitions must genuinely differ. If you cannot produce a critical definition, mark the concept `pinned` and move on — but make the failure to find one explicit, not silent.

3. **Map the boundary.** For each concept, state where its scope begins and ends under each definition. Then produce at least two edge cases: one that is plainly inside the concept and one that plausibly tests the boundary. If an edge case survives under the charitable definition but collapses under the critical one, record that divergence — it is the analytically load-bearing gap.

4. **Assess operationalizability.** For each concept, ask: is there any procedure — measurement, observation, test — that could in principle determine whether the concept applies to a particular instance? Rate:
   - **operationalizable** — there is a workable measurement or criterion, even if expensive.
   - **partially operationalizable** — some instances can be decided, but core cases remain judgment calls.
   - **unfalsifiable** — no conceivable observation would settle whether the concept applies; the concept's scope can be revised post-hoc to include or exclude any case. Flag this explicitly.

5. **Identify fragile concepts.** Rank the extracted concepts. Concepts that are `slippery` (definitions diverge and boundary is unstable) or `unfalsifiable` are the weakest links — name them and indicate which part of the claim would fail if the skeptic's definition prevails.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Every key concept in the claim is extracted (function words excluded) | Y/N |
| Each concept has both a charitable and a critical definition, genuinely different | Y/N |
| Each concept has a boundary statement and at least two edge cases | Y/N |
| Operationalizability is rated explicitly, including unfalsifiable flags | Y/N |
| Divergence between charitable and critical Readings (if any) is named, not hidden | Y/N |
| Fragile concepts are ranked and the analytical consequence is stated | Y/N |

## Red Flags

- **Single-definition dismissal.** Only one definition is offered per concept ("the dictionary says …"). A dictionary entry is a starting point, not an analysis. Without the adversarial definition, the concept has not been tested.
- **Strawman critical definition.** The critical definition is deliberately uncharitable — a version no one would actually assert — so the claim wins by default. The critical definition must be one a serious skeptic could defend.
- **No edge cases.** The concept's boundary is described abstractly but never tested against specific cases. Boundary claims that cannot be checked are not boundary claims.
- **Unfalsifiable-but-assumed.** The concept is clearly unfalsifiable (e.g., "authentic," "emergent," "systemic") and the analyst moves on without flagging it. Unfalsifiability changes the entire burden of the surrounding argument.
- **Slippery concepts treated as pinned.** The definition is said to be settled but the analyst shifts between slightly different uses across the analysis. If the meaning moved during the analysis itself, the concept is contested, not pinned.
- **Concept inflation.** Every noun in the claim is flagged as a key concept, burying the two or three that actually carry load. Pick the concepts that change the claim when redefined; ignore the rest.

## Output Format

```
## Conceptual Analysis

**Input claim:**
<the claim or short argument being analyzed>

### Per-concept table

| Concept | Charitable definition | Critical definition | Boundary & edge cases | Operationalizability | Verdict |
|---|---|---|---|---|---|
| <term 1> | <defender's definition> | <skeptic's definition> | <scope; in-case / edge-case> | operationalizable / partial / unfalsifiable | pinned / contested / slippery |
| <term 2> | ... | ... | ... | ... | ... |
| ... | | | | | |

### Divergence summary
<For each concept where charitable and critical definitions disagree in a way that affects the claim: name the divergence and state what the claim looks like under each.>

### Fragile concepts (ranked)
1. <concept> — <slippery / unfalsifiable> — <what fails in the claim if the skeptic's definition prevails>
2. <...>

### Confidence
<high / medium / low> — <high when every key concept is pinned or cleanly contested with a named verdict; medium when one or more concepts are slippery but downstream argument can still be evaluated; low when core concepts are unfalsifiable or the claim is fundamentally under-defined.>
```
