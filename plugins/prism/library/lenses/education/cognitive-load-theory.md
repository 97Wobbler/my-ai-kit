---
name: Cognitive Load Theory
domain: education
source: John Sweller (1988), with extensions by Paas, van Merriënboer, Kirschner, and others
underlying_class: model
best_for: Diagnosing why a lesson, learning material, or interface is harder to learn from than it should be
one_liner: "Decompose learning material into intrinsic / extraneous / germane load and check seven sources of extraneous load."
---

# Cognitive Load Theory

## Overview
Working memory is small — roughly 4 independent chunks at a time. Learning happens when those limited slots are used on the material itself, not on decoding the presentation or managing incidental complexity. Cognitive Load Theory partitions the load into three types (intrinsic, extraneous, germane) and asks which type is dominant in a given learning experience. Practitioners use it to redesign lessons, textbooks, UIs, and instructional videos that "feel hard" without being deep. The diagnostic question is: "What is the student's working memory being spent on right now?"

## Analytical Procedure

### Step 1 — Identify the learning target

1. **State the target concept or skill in one sentence.** Without this, you can't separate essential complexity from noise.

2. **Identify the learner's prior knowledge level.** Intrinsic load is relative: what's simple for an expert is overwhelming for a novice. Specify: absolute novice / some exposure / intermediate / near-expert.

### Step 2 — Score each type of load

#### Intrinsic Load (내재적 부하) — the inherent difficulty of the material
Intrinsic load is set by two factors:
- **Element interactivity** — how many elements must be held in mind simultaneously to understand the concept. Solving a single arithmetic fact is low-interactivity. Balancing a chemical equation is high-interactivity.
- **Learner expertise** — more expertise = more elements chunked = less effective load from the same material.

Score intrinsic load: **Low / Medium / High** for the specified learner level. Justify with element count.

**Intrinsic load cannot be reduced by instructional design, only by sequencing** — break the content into smaller element sets, teach prerequisites first, or use worked examples.

#### Extraneous Load (외재적 부하) — load from how the material is presented
Extraneous load is pure waste — it consumes working memory without contributing to learning. Check for each of these known sources:

- **Split attention** — the learner must integrate information across two separated places (a diagram on one page, labels on another). FIX: co-locate.
- **Redundancy** — the same information is presented twice (on-screen text + narration reading the same text verbatim). FIX: remove one.
- **Modality overload** — too much visual information with no auditory channel (or vice versa) when dual-channel would distribute load. FIX: rebalance.
- **Transient information** — information that disappears before the learner can use it (fast video, unpausable animations). FIX: allow pause/replay or provide static reference.
- **Seductive details** — interesting but off-target content (fun facts, decorative images, entertaining tangents) that competes for attention. FIX: cut.
- **Poor signaling** — important parts are not visually or structurally distinguished from unimportant parts. FIX: add headings, bolding, arrows.
- **Unfamiliar notation or jargon** without introduction. FIX: introduce or link to a glossary.

Score extraneous load: **Low / Medium / High**. For each source found, record the specific instance and a proposed fix.

#### Germane Load (본유적 부하) — load used for actual schema construction
Germane load is "good load" — working memory effort that goes into building and refining the mental schema. It shows up as:
- Self-explanation prompts ("why does this step work?")
- Worked example pairs followed by matched problems
- Variability across examples (same concept applied to surface-different situations)
- Retrieval practice (recalling what was learned)
- Elaboration (linking new material to prior knowledge)

Score germane load: **Low / Medium / High**. Unlike extraneous load, you want this to be as high as the total load budget allows.

### Step 3 — Total load check

3. **Compute total effective load** as (Intrinsic + Extraneous + Germane), capped by working memory capacity (~4 elements).
4. **If total > capacity**, learning fails. Reduce extraneous load first (it's always waste), then reduce intrinsic load via sequencing.
5. **If total < capacity and germane is low**, the material is under-challenging — the learner is bored rather than overloaded.

### Step 4 — Diagnose and recommend

6. **Name the dominant load type.** Most failing learning materials are extraneous-dominant. Germane-dominant failures are rare and usually mean the material is too advanced.
7. **Produce at least one concrete redesign recommendation per extraneous load source found.** Recommendations must point to a specific element of the material, not "improve clarity."

## Evaluation Criteria

| Check | Pass |
|---|---|
| Learning target is stated in one sentence | Y/N |
| Learner expertise level is specified | Y/N |
| Element interactivity is actually counted (not estimated by feel) | Y/N |
| All 7 extraneous load sources were checked (not just the obvious ones) | Y/N |
| Each extraneous finding has a specific instance and a specific fix | Y/N |
| Germane load is scored, not just intrinsic + extraneous | Y/N |

## Red Flags

- Intrinsic load is labeled High without counting elements. Without a count, it's a feeling, not a diagnosis.
- Only split attention and redundancy were checked. Transient info and seductive details are the sneaky ones; missing them is a sign of incomplete review.
- Recommendations are of the form "simplify the language." Vague. Name which sentence, which word, which image.
- Germane load is assumed to be whatever's left after removing extraneous. Germane is its own kind of design (worked examples, self-explanation) and must be added deliberately.
- The learner profile is "students." CLT depends on expertise level — without it, the load score is meaningless.
- Load is scored but no capacity check is done. The whole point of CLT is that working memory has a ceiling; omitting the ceiling check skips the central insight.

## Output Format

```
## Cognitive Load Assessment

**Learning target:**
<one sentence>

**Learner profile:**
<absolute novice | some exposure | intermediate | near-expert>

### Intrinsic Load
- Element count (for target learner): _
- Score: Low / Medium / High
- Justification: <...>
- Sequencing recommendation (if High): <...>

### Extraneous Load
| Source | Found? | Instance | Fix |
|--------|--------|----------|-----|
| Split attention       | Y/N | <where> | <how> |
| Redundancy            | Y/N | <...>   | <...> |
| Modality overload     | Y/N | <...>   | <...> |
| Transient information | Y/N | <...>   | <...> |
| Seductive details     | Y/N | <...>   | <...> |
| Poor signaling        | Y/N | <...>   | <...> |
| Unfamiliar notation   | Y/N | <...>   | <...> |

Score: Low / Medium / High

### Germane Load
- Techniques present: <worked examples / self-explanation / variability / retrieval / elaboration>
- Techniques missing: <...>
- Score: Low / Medium / High

### Capacity Check
- Total (Intrinsic + Extraneous + Germane): _ / ~4
- Verdict: <overloaded | balanced | under-challenging>

### Dominant Problem
<extraneous-dominant | intrinsic-dominant | germane-starved | balanced-needs-progression>

### Redesign Recommendations
1. <specific change to specific element>
2. ...

### Confidence
<high/medium/low> — <justification>
```
