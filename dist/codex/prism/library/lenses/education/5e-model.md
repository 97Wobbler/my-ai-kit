---
name: 5e-model
display_name: 5E Model
class: lens
underlying_class: native
domain: education
source: Bybee et al. (Biological Sciences Curriculum Study, 1989); refined in science education (NGSS, 2013)
best_for:
  - Designing coherent lesson sequences that move students from curiosity to mastery
  - Diagnosing where a lesson unit breaks down in student engagement or understanding
  - Auditing curriculum materials for pedagogical completeness
one_liner: "Five-phase cyclical instructional design — Engage, Explore, Explain, Elaborate, Evaluate."
---

# 5E Model

## Overview

The 5E Model sequences a learning experience through five phases: Engage (activate prior knowledge and interest), Explore (hands-on investigation), Explain (structured interpretation), Elaborate (extend and apply), and Evaluate (assess understanding and metacognition). It is cyclical, not linear — the output of Evaluate often feeds back into a new Engage. Practitioners use it to design lessons that build conceptual understanding incrementally and to diagnose why a lesson failed (Did students never engage? Did they explore but not explain?). The model is agnostic to subject; it works equally in science, mathematics, literacy, and social studies.

## Analytical Procedure

### Phase 1 — Map the Current Lesson

1. **Extract the learning objective.** Write what students should be able to do or understand by the end. Avoid vague terms like "understand" or "learn about" — use action verbs: "identify," "calculate," "explain the relationship between," "predict."

2. **List every activity currently in the lesson.** Write 1-2 sentences per activity. Include timing, materials, and grouping (individual, pair, whole class).

3. **Classify each activity by the 5E it primarily serves.** If an activity spans multiple phases, assign it to the dominant one. If an activity doesn't fit any phase, flag it separately.

### Phase 2 — Evaluate Each Phase

For **Engage**, assess whether the opening:
- Activates at least one piece of students' prior knowledge relevant to the objective
- Surfaces a question, curiosity gap, or real-world connection that students recognize as *their* problem, not the teacher's
- Takes no more than 10–15% of lesson time
- Does NOT teach the answer (common error: overexplaining upfront)

For **Explore**, assess whether students:
- Manipulate physical or digital materials, gather data, or conduct an investigation
- Work collaboratively at least some of the time
- Make observations and predictions *before* being told the answer
- Encounter phenomena that are puzzling or surprising (if everything works as expected, there is little to explore)
- Are not given the procedure step-by-step; instead, they design or adapt an approach

For **Explain**, assess whether:
- Students articulate their findings in their own words first (misconceptions surfaced early are correctable)
- The teacher or text introduces vocabulary, principles, or models *after* students have tried to explain
- Explanations connect directly to what students observed in Explore
- The explanation is not a 20-minute lecture; dialogue and evidence-checking break it up

For **Elaborate**, assess whether students:
- Apply the concept to a new or more complex context
- Revisit the Engage question (or a variant) and now can answer or predict correctly
- Extend the concept to adjacent ideas (transfer, not mere repetition)
- Have scaffolds that allow independent or small-group work, not just teacher direction

For **Evaluate**, assess whether:
- Students demonstrate understanding of the objective through multiple modes (drawing, writing, verbal explanation, problem-solving)
- Evaluation includes *both* formative (ongoing, mid-lesson) and summative (end-of-lesson) components
- Students reflect on *how* they learned, not just *what* they learned (metacognition)
- Results are used to inform the next cycle (If students scored poorly, what gets re-taught in the next Engage/Explore?)

### Phase 3 — Identify Gaps and Overloads

4. **Count the phases.** Tally how many substantial activities serve each E. A well-balanced 5E unit typically has:
   - 1 Engage (or fewer if the unit spans multiple days and re-engages partway)
   - 2–4 Explore activities (investigation is where most time lives)
   - 1–2 Explain sessions
   - 1–2 Elaborate activities
   - 1 Evaluate (may be distributed across the unit)

5. **Spot missing phases.** If Explore is absent or cursory, students skip the productive struggle. If Explain is missing, students rely on intuition without formal concepts. If Elaborate is absent, transfer is unlikely.

6. **Spot overloads.** If Engage takes 30 minutes and Explore takes 10, engagement isn't buying time for discovery. If Evaluate is one quiz and no reflection, you've measured but not taught metacognition.

7. **Check for dead time.** Any activity that doesn't serve one of the five Es (e.g., "students copy the diagram into their notebooks") should be eliminated or bundled into an E phase.

### Phase 4 — Trace Conceptual Coherence

8. **Reread the Explore section.** What phenomenon or pattern did students actually encounter? Write it in one sentence.

9. **Reread the Explain section.** What principle or model does the teacher introduce? Write it in one sentence.

10. **Check the alignment.** Does the principle explain the phenomenon? If the student explored a water cycle diagram but the lesson explains the hydrologic cycle in abstract terms, there is a mismatch — the concrete and abstract don't meet.

11. **Trace the Elaborate forward.** When students apply the concept in Elaborate, do they apply it to the *same phenomenon in a new context* (strong), or to an entirely different phenomenon (risky — students may not see the connection)?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Learning objective is written with an action verb (not "understand") | Y/N |
| All activities in the lesson are classified into one of the five Es | Y/N |
| Engage activates prior knowledge and surfaces a genuine question | Y/N |
| Explore includes hands-on investigation, not just observation | Y/N |
| Explain introduces vocabulary/models *after* student sense-making | Y/N |
| Elaborate applies the concept in a new context, not repetition | Y/N |
| Evaluate includes both formative and metacognitive components | Y/N |
| The phenomenon in Explore is explained (not just described) in Explain | Y/N |
| No phase is missing entirely | Y/N |
| No phase consumes more than 50% of lesson time | Y/N |

## Red Flags

- Engage is a lecture that teaches the answer upfront. Students have no space to wonder.
- Explore is a worksheet with blanks to fill in, not a real investigation. The procedure is given; no design or prediction required.
- Explain comes before Explore. This breaks the model and makes Explore confirmatory, not exploratory.
- Elaborate is identical in context to Explore (same problem, same conditions). There is no transfer, just repetition.
- Evaluate is a single summative quiz with no formative feedback or student reflection during the unit.
- The concept introduced in Explain has no visible connection to what students explored. Alignment is broken.
- One phase (usually Explore) takes 80% of time while others are rushed. A balanced lesson distributes time across all five.
- Students are told the answer in Engage, explore to confirm it in Explore, and explain it back to the teacher in Explain. The cycle has no genuine discovery.

## Output Format

```
## 5E Lesson Audit

**Learning Objective:**
<action verb + what students will do/understand>

### Phase Inventory
| Phase | Activity | Time | Meets Phase Criteria? |
|---|---|---|---|
| Engage | <...> | <...> | Y/N |
| Explore | <...> | <...> | Y/N |
| Explain | <...> | <...> | Y/N |
| Elaborate | <...> | <...> | Y/N |
| Evaluate | <...> | <...> | Y/N |

### Phase-by-Phase Assessment
**Engage:** <Y/N — explain why or why not>
**Explore:** <Y/N — explain>
**Explain:** <Y/N — explain>
**Elaborate:** <Y/N — explain>
**Evaluate:** <Y/N — explain>

### Conceptual Alignment
**Phenomenon from Explore:** <one sentence>
**Principle introduced in Explain:** <one sentence>
**Alignment:** <Strong / Weak / Broken — explanation>

### Missing or Overloaded Phases
<List any gaps (e.g., "Elaborate is absent") or imbalances (e.g., "Explore claims 70% of time").>

### Recommended Changes
1. <Specific change and why>
2. <...>

### Confidence
<high/medium/low> — <justification (e.g., "High: all five phases present with clear alignment; Medium: Elaborate is weak but fixable; Low: Engage and Explain are out of sequence, requiring structural redesign")>
```
