---
name: pixar-formula
display_name: Pixar Formula
class: lens
underlying_class: native
domain: storytelling
source: Andrew Stanton (Pixar storyteller); formalized in "The Art of Storytelling" talks and "Narrative Structures in Animation"
best_for:
  - Diagnosing narrative momentum loss in screenplays and scripts
  - Testing whether a story premise has genuine conflict and stakes
  - Identifying underexplored consequences in plot sequences
one_liner: "One event at a time, 'because of that' next, and again — when the causal chain breaks, the story dies."
---

# Pixar Formula

## Overview
The Pixar Formula is a narrative diagnostic that checks whether a story's causality chain is intact. It operationalizes the principle: *Once upon a time...* (setup) → *One day...* (inciting incident) → *Because of that...* (first consequence) → *And because of that...* (escalating cascade) → *Until finally...* (climax). The discipline is tracing causality — most stories break because a plot point happens for external reasons (pacing, subplot convenience) rather than because the preceding event made it inevitable. Practitioners use this when a screenplay feels loose, when beats feel planted rather than earned, or when characters seem to act against established logic.

## Analytical Procedure

### Phase 1 — Extract the Causality Chain

1. **Identify the story's inciting incident.** This is the single event that makes the protagonist's world unsustainable as it was. Write it in one sentence. It must involve the protagonist or their immediate circle directly, not abstract backstory.

2. **Trace forward from the inciting incident.** For each major plot beat that follows, ask: *Did this event happen because of what came before, or did it happen because the story needed it to happen?* Write the answer plainly.

3. **For each beat, write the causal chain in this form:**
   - **Beat A:** <what happened>
   - **Direct consequence of A:** <what logically results>
   - **Beat B (planned):** <what the story moves toward>
   - **Match?** Yes / No / Partial

   If Match = No, the beat is externally motivated. Flag it.

4. **Map the full sequence.** Using the form above, create a numbered list of 5–8 major story turns from inciting incident to climax. Show the causality claim for each.

### Phase 2 — Stress-Test Causality

5. **For each flagged beat (Match = No), ask three pressure questions:**
   - *What would a character with the goals established so far actually do at this moment?*
   - *What would naturally happen if no one intervened to steer the plot?*
   - *Is there a more direct path to this plot point from the preceding beat?*
   
   Write honest answers. If the story's beat is less logical than the natural outcome, note the gap.

6. **Check for consequence denial.** After each major beat, does the story adequately show the consequences of that beat — for the protagonist, for allies, for the world? Or does the story skip past the fallout to get to the next plot point? Mark each beat "Consequence shown / Consequence compressed / Consequence ignored."

7. **Examine the midpoint.** The midpoint (roughly 50% through) should be where the protagonist's plan or understanding is fundamentally wrong, forcing them to take a different approach. If the midpoint is a surprise or a plot twist *about* the world rather than a reversal of *the protagonist's strategy*, it is not a true midpoint — flag it.

### Phase 3 — Identify Causality Breaks

8. **Compile the breaks.** For each beat where causality is weak (Match = No or Consequence is denied/ignored), write:
   - **Beat:** <what happens>
   - **Causal weakness:** <why it doesn't flow from what came before>
   - **Cost to narrative:** Does this break momentum, confuse motivation, or require suspension of disbelief?
   - **Repair path:** What would need to change in preceding beats to make this beat inevitable?

9. **Calculate the causality ratio.** Count beats with Match = Yes and full Consequence shown. Divide by total major beats (excluding epilogue). A ratio below 0.6 indicates significant causality loss; below 0.4 indicates structural failure.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Inciting incident identified and stated in one sentence | Y/N |
| Every major beat (5–8) mapped with causal claim (A → B) | Y/N |
| At least one beat flagged as externally motivated (Match = No) | Y/N |
| Consequences explicitly marked Shown/Compressed/Ignored for each beat | Y/N |
| Midpoint identified and tested against reversal definition | Y/N |
| Causality ratio calculated (major beats with Match=Yes / total beats) | Y/N |
| Repair paths proposed for each causality break | Y/N |

## Red Flags

- Every beat has Match = Yes. Either the story has no structural problems (rare) or the causality test was applied generously. Re-interrogate beats where the protagonist's action feels forced or where external plot pressure is visible.
- Midpoint is missing or is a surprise about the world (villain's hidden plan revealed, magic system explained) rather than a reversal of the protagonist's approach. The story lacks a true turning point.
- Consequences column is all "Compressed" or "Ignored." The story moves fast but doesn't breathe — characters don't grapple with what their choices cost them.
- Causality breaks cluster in the second half. This often means the climax was written first and earlier beats were installed to lead to it, rather than emerging naturally from character choice and consequence.
- A beat requires a character to act against their established motives or knowledge. This is causality failure masquerading as plot twist.

## Output Format

```
## Pixar Formula Assessment

**Story:** <title>
**Inciting incident:** <one sentence>

### Causality Chain

| # | Beat | Direct consequence of prior | Planned beat | Match? | Consequence shown? |
|---|---|---|---|---|---|
| 1 | <...> | <...> | <...> | Yes/No | Shown/Compressed/Ignored |
| 2 | <...> | <...> | <...> | <...> | <...> |

### Flagged Beats (Match = No)

**Beat:** <...>
- What would the character logically do? <...>
- What would naturally happen? <...>
- Is there a more direct path? <...>

### Causality Breaks

| Beat | Causal weakness | Cost to narrative | Repair path |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

### Midpoint Check
**Identified at:** <beat #, timing>
**Type:** World reveal / Protagonist strategy reversal / other
**Verdict:** True turning point / Not a reversal / Missing

### Causality Ratio
- Beats with Match = Yes and full Consequence: _
- Total major beats: _
- Ratio: __% (above 60% = healthy)

### Confidence
<high/medium/low> — <justification based on causality ratio and break severity>
```
