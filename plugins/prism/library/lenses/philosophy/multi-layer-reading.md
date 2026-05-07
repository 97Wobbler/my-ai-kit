---
name: multi-layer-reading
display_name: Multi-Layer Reading
class: lens
underlying_class: stance
domain: philosophy
source: Composite of hermeneutic and pragmatic traditions — Ricoeur (Interpretation Theory, 1976) and Gadamer (Truth and Method, 1960) on meaning and interpretation, Grice ("Logic and Conversation," 1975) and Austin (How to Do Things with Words, 1962) on pragmatic and performative layers. No single author; an operationalized synthesis of these traditions.
best_for:
  - Analyzing claims whose literal reading is likely incomplete (metaphor, irony, speech-act, hedge)
  - Short utterances where the same sentence can sustain multiple defensible interpretations
  - Feeding a downstream critical pipeline that needs interpretation branches explicitly labeled
  - Preventing premature closure on a single reading before conceptual or presuppositional work begins
one_liner: "Generate and label multiple defensible readings of a short claim across semantic, pragmatic, performative, and contextual layers, each tagged with plausibility."
---

# Multi-Layer Reading

## Overview

A claim rarely has only one meaning. The same short sentence can be read literally, figuratively, performatively (as an act, not a description), or as context-dependent implicature. This lens operationalizes the hermeneutic insight that interpretation precedes evaluation: before you argue about whether a claim is *true*, you first have to pin down *which* claim is on the table. The procedure forces the analyst to enumerate candidate readings explicitly, tag them by layer, and attach evidence and plausibility to each — so downstream lenses (conceptual analysis, presupposition analysis, argument reconstruction) can be applied either to a single converged Reading or in parallel across multiple surviving ones.

## Analytical Procedure

1. **Capture the literal surface.** Restate the input in the plainest language you can. Strip hedging, metaphor, and tone. If the input is already literal and unambiguous, say so explicitly and move to step 5 — do not invent readings where none exist.
   - Example input: "The market has spoken."
   - Literal surface: "Aggregate purchasing behavior has produced an outcome."

2. **Generate candidate readings across four layers.** For each layer below, ask whether the input supports a reading at that layer. If yes, produce a candidate labeled Reading A, Reading B, Reading C, … Use at most one candidate per layer unless the layer itself sustains two genuinely different readings.
   - **Semantic (literal):** the compositional meaning of the words as written.
   - **Figurative:** metaphor, metonymy, analogy, idiom — what the expression stands in for.
   - **Performative:** what the utterance *does* rather than *says* (declaring, ordering, endorsing, distancing, warning).
   - **Contextual / implicature:** what the utterance conversationally implies given the likely speaker, audience, and setting.

3. **Gather layer-specific evidence for each Reading.** For every candidate, list the features of the input that support locating it on that layer: lexical choice, syntactic mood, register, genre cues, likely speaker-audience relation. Evidence must be inspectable in the text or in a stated contextual assumption — not a private intuition.

4. **Test cross-compatibility.** For each pair of surviving Readings, ask: can both hold simultaneously, or are they mutually exclusive? Readings that are mutually exclusive will be analyzed separately downstream. Readings that are compatible (e.g., a sentence can be both literally meaningful and performatively an endorsement) are kept together and marked as co-holding.

5. **Finalize the Reading set and tag plausibility.** For each surviving Reading, assign plausibility as **high**, **medium**, or **low** based on: (a) strength of the layer-specific evidence gathered in step 3, (b) whether the Reading requires contested contextual assumptions, (c) whether the Reading is what the input most naturally invites versus a strained alternative. If a single Reading dominates and others are weak, mark the dominant one high and the others low but retain them for red-team purposes. If two or more Readings are roughly equal, flag the input as **interpretively underdetermined** — downstream lenses should run on each in parallel.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Literal surface is extracted in plain language without hedging | Y/N |
| Each layer (semantic / figurative / performative / contextual) is considered, even if dismissed in one line | Y/N |
| Each Reading is labeled A, B, C, … and tagged with its layer | Y/N |
| Each Reading has layer-specific evidence that is inspectable | Y/N |
| Cross-compatibility between Readings is checked, not assumed | Y/N |
| Plausibility is assigned per Reading with an explicit basis | Y/N |
| Interpretive underdetermination is flagged when Readings tie | Y/N |

## Red Flags

- **Forced metaphorical reading.** Every utterance gets pushed into a figurative or performative layer even when the literal reading is clearly primary. If the speaker plainly meant what they said, do not invent depth.
- **Authorial-intent collapse.** Treating "what the author probably meant" as the only legitimate Reading. The lens surfaces what the text *can* sustain, not what the author *had in mind*. Attribution is separate from interpretation.
- **Evidence-free Readings.** A Reading is proposed but no text-level or context-level feature supports its layer placement. This is interpretation by vibe, not by analysis.
- **Uniform plausibility.** All Readings are tagged medium with no basis given. Plausibility is a ranking signal — if everything is medium, the analyst refused to discriminate.
- **Reading inflation.** Producing five Readings to appear thorough when only two are genuinely distinct. Readings must differ in layer *or* in substantive content, not in phrasing.
- **Premature collapse.** Declaring a single Reading before any layer beyond semantic has been checked. If no other layer was considered, the "single Reading" conclusion is a default, not a finding.

## Output Format

```
## Multi-Layer Reading

**Input:**
<the original claim or utterance, verbatim>

**Literal surface:**
<plain-language restatement, hedging and figuration stripped>

### Readings

**Reading A — <layer>**
- Content: <one-sentence restatement of what this Reading takes the input to mean/do>
- Layer: [semantic | figurative | performative | contextual]
- Evidence: <inspectable features of the input or stated context supporting this Reading>
- Plausibility: [high | medium | low]
- Basis: <why this plausibility, not another>

**Reading B — <layer>**
- Content: <...>
- Layer: <...>
- Evidence: <...>
- Plausibility: <...>
- Basis: <...>

(repeat as needed; do not invent Readings past what the input sustains)

### Cross-compatibility
| Pair | Relation |
|---|---|
| A ↔ B | co-holding / mutually exclusive / partially overlapping |
| A ↔ C | ... |

### Interpretive status
[converged on Reading <X> | underdetermined between <list>]
<If underdetermined, name which Readings should be carried forward into downstream analysis in parallel.>

### Confidence
<high / medium / low> — <high if one Reading dominates with strong evidence; medium if two Readings co-hold or if the dominant Reading rests on contested context; low if the input is genuinely underdetermined or context-starved.>
```
