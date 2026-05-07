---
name: dan-harmons-story-circle
display_name: Dan Harmon's Story Circle
class: lens
underlying_class: native
domain: storytelling
source: Dan Harmon (Community, 2011); based on Joseph Campbell's Monomyth (The Hero with a Thousand Faces, 1949)
best_for:
  - Diagnosing structural weakness in TV episodes, screenplays, or narrative arcs
  - Identifying where a story loses audience engagement or emotional coherence
  - Debugging why a story feels "off" even when individual scenes work
one_liner: "Eight-stage cyclical structure that tracks a story's emotional arc."
---

# Dan Harmon's Story Circle

## Overview

The Story Circle is a simplified, cyclical version of the Hero's Journey that traces an emotional arc through eight concrete stages. Instead of a linear quest, it models a character entering an unfamiliar world, adapting, and returning changed. Practitioners use this to audit whether a story maintains forward momentum, whether emotional stakes are clear at each turn, and whether the ending resolves what the opening promised. The discipline is tracing the audience's emotional journey, not just the plot's logical sequence.

## Analytical Procedure

### Phase 1 — Extract the Eight Stages

1. **Identify the protagonist and their starting state.** Write down who the story is *about* (not necessarily the most prominent character) and what their normal world looks like before disruption. This is Stage 1: **You.**

2. **Find the inciting incident.** What happens that pulls the protagonist out of their routine? This must be external and specific ("the villain arrives," "the job offer comes," "the loved one vanishes") — not vague ("things get complicated"). This is Stage 2: **Need.**

3. **Locate the threshold or commitment point.** Where does the protagonist commit to action, cross into a new world (literal or metaphorical), or say "yes" to the challenge? This is Stage 3: **Go.** Do not confuse this with the inciting incident; there is always a gap between being called and accepting.

4. **Identify the series of small wins, lessons, or adaptations.** What does the protagonist learn or master in the unfamiliar world? What allies or tools do they acquire? Trace at least 2-3 concrete moments of growth or adjustment. This is Stage 4: **Search.** (Often the longest stage in TV—the "exploring and learning" middle.)

5. **Find the point where the protagonist has what they think they need.** They have the McGuffin, they've mastered the skill, they believe they've solved the problem. This is Stage 5: **Find.** It is often a false victory.

6. **Locate the moment of greatest jeopardy or truth.** What goes wrong? What do they discover about themselves or the world that shatters their illusion? This must be worse than the problem in Stage 2. This is Stage 6: **Take.** (The "inversion" — the character is brought low.)

7. **Identify the climactic decision or action.** How does the protagonist use what they learned to confront the real problem? What do they *actually* do in the moment of maximum stakes? This is Stage 7: **Break.** (The protagonist breaks their old patterns or breaks the antagonistic force.)

8. **Describe the new normal.** What is the protagonist's state at the end? How are they different from Stage 1? What has been gained or lost? This is Stage 8: **Return.** The audience should feel that the protagonist has genuinely changed.

### Phase 2 — Evaluate Emotional Continuity

9. **For each stage transition, ask: "Does the audience understand why the protagonist does this next thing?"** Weak stories have stage breaks where the character's action is unmotivated or felt (to the viewer) like the writer's forcing it. Mark each transition as `clear` (emotionally inevitable), `plausible` (understandable but not inevitable), or `forced` (requires suspension of disbelief or feels arbitrary).

10. **Measure emotional stakes.** At each stage, the audience should know what the protagonist *wants* (external goal) and what they *fear* (internal stake). Write down both for Stages 2–7. If either is missing or unclear, mark the stage as `low stakes`. If both are vivid and in tension, mark as `high stakes`.

11. **Check for symmetry.** Compare the protagonist's state at Stage 1 (You) and Stage 8 (Return). The most common failure is Stage 8 being identical to Stage 1 (no change) or being so extreme that it severs the character from their former life (unearned catharsis). A strong Return shows change that is *earned and ambiguous* — the character has learned something that costs them.

### Phase 3 — Diagnose Failure Points

12. **If the story loses energy in Stage 4 (Search), check for:**
    - Are the lessons being *shown* in conflict or *told* in exposition?
    - Is each small win raising the stakes of the next challenge?
    - Is the protagonist discovering something about the *world* or just about the *task*?

13. **If the story feels unearned at Stage 6 (Take) or Stage 7 (Break), check for:**
    - Did the protagonist encounter the knowledge or tool they use in Break during Search?
    - Is the Take truly worse than the Need, or is it a repeat?
    - Does the Break use something learned, or does it pull a power from nowhere?

14. **If the audience doesn't believe the Return (Stage 8), check for:**
    - Does the ending address the original fear stated in Stage 2?
    - Is the change visible in concrete behavior, not just stated?
    - Does the Return contradict anything established in Stages 1–3?

## Evaluation Criteria

| Check | Pass |
|---|---|
| All eight stages are identified with concrete story moments, not abstract summaries | Y/N |
| Stage 2 (Need) and Stage 6 (Take) are distinct; Take is not a repeat of Need | Y/N |
| Stage 3 (Go) is separated from Stage 2; protagonist consciously chooses to enter the new world | Y/N |
| Stage 5 (Find) shows what the protagonist *thinks* they need, not what they actually need | Y/N |
| All transitions (1→2, 2→3, etc.) are marked as clear, plausible, or forced | Y/N |
| Stages 2–7 have both an external goal and an internal fear articulated | Y/N |
| Stage 8 shows specific change in the protagonist's belief, relationship, or behavior | Y/N |

## Red Flags

- Stages 4 and 5 are described as a sequence of plot events rather than a sequence of *what the protagonist learns.* (Example: "They fight five bad guys" vs. "They discover that speed doesn't solve the problem; they need patience." The latter is structural; the former is just action.)
- Stage 6 (Take) is softer than Stage 2 (Need). The story's emotional low point should be lower than its opening disruption, not equal or higher.
- The Return is described as a summary ("and they lived happily") rather than as a *specific moment showing the character behaving differently.* Stage 8 must be shown, not reported.
- All transitions are marked `clear`. Either the story is genuinely coherent (possible but rare) or the evaluator is not interrogating whether the audience actually buys each moment.
- Stages 1 and 8 are identical. The character learned nothing, which makes the story feel like a waste of time to the audience even if the plot is entertaining.
- Protagonist acquires a crucial skill or tool in Stage 7 (Break) that was never mentioned before. This is called "armoring" — the writer gave the protagonist what they needed to win, but the audience doesn't believe they earned it.

## Output Format

```
## Story Circle Assessment

**Story/Episode:** <title>
**Protagonist:** <character name and starting condition>

### The Eight Stages

| Stage | Label | Story Moment | Internal/External Stakes | Transition | Transition Quality |
|---|---|---|---|---|---|
| 1 | You | <description> | <wants/fears> | N/A | N/A |
| 2 | Need | <description> | <wants/fears> | Stage 1→2 | clear / plausible / forced |
| 3 | Go | <description> | <wants/fears> | Stage 2→3 | clear / plausible / forced |
| 4 | Search | <description> | <wants/fears> | Stage 3→4 | clear / plausible / forced |
| 5 | Find | <description> | <wants/fears> | Stage 4→5 | clear / plausible / forced |
| 6 | Take | <description> | <wants/fears> | Stage 5→6 | clear / plausible / forced |
| 7 | Break | <description> | <wants/fears> | Stage 6→7 | clear / plausible / forced |
| 8 | Return | <description> | <change from Stage 1> | Stage 7→8 | clear / plausible / forced |

### Emotional Stakes Summary
- Clearest stakes: <stage and why>
- Weakest stakes: <stage and why>
- Overall stakes consistency: high / medium / low

### Key Findings

1. <Finding about narrative structure, emotional coherence, or earned vs. unearned moments>
2. <Finding>
3. <Finding>

### Diagnosis (if story falters)
- **If energy drops in Stage 4:** <specific observation about Search pacing or revelation>
- **If Take/Break feel unearned:** <specific observation about knowledge transfer or tool introduction>
- **If Return feels hollow:** <specific observation about change or closure>

### Confidence
<high/medium/low> — <justification based on clarity of stage identification, quality of moment-by-moment evidence, and consistency of stakes>
```
