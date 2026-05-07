---
name: gagnes-9-events-of-instruction
display_name: Gagne's 9 Events of Instruction
class: lens
underlying_class: native
domain: education
source: Robert M. Gagné (1965, refined through 1985); foundational in instructional design
best_for:
  - Designing a complete instructional sequence from attention to transfer
  - Auditing existing instruction for gaps in cognitive support
  - Ensuring each learning objective receives the events it requires
one_liner: "Sequence nine cognitive events to reliably drive a learning objective home."
---

# Gagne's 9 Events of Instruction

## Overview

Gagné's 9 Events is a prescriptive framework for structuring instruction around how the human brain processes new information. Each event addresses a specific cognitive need — from capturing attention to enabling transfer of learning to new contexts. Instructional designers use this lens to audit whether a course, lesson, or training program provides the cognitive scaffolding learners need at each stage, or whether it assumes prerequisites that should be explicitly taught.

## Analytical Procedure

### Phase 1 — Map the Instruction to the 9 Events

1. **Obtain the instructional artifact.** This is typically a lesson plan, course syllabus, training module, tutorial, or onboarding sequence. Extract the sequence of activities, media, assessments, and interactions as they are actually presented to the learner (not as designed, but as experienced).

2. **For each of the 9 Events listed below, read through the artifact and identify where (if at all) that event occurs.** Write down the exact step or activity in the instruction that corresponds to each event. If an event is absent, write "absent."

The 9 Events of Instruction are:

| Event | Cognitive Purpose | What it must do |
|---|---|---|
| 1. Gain Attention | Activate receptivity | Trigger interest; break routines; pose a problem or question |
| 2. Inform Learners of Objectives | Set expectations | State what the learner will be able to do after instruction |
| 3. Stimulate Recall of Prior Knowledge | Activate existing schema | Connect new learning to concepts or skills already in memory |
| 4. Present the Content | Deliver new information | Explain, demonstrate, or model the skill or concept; use multiple modalities |
| 5. Provide Learning Guidance | Support encoding | Give examples, analogies, mnemonics, or scaffolds that aid understanding |
| 6. Elicit Performance | Force retrieval | Ask learner to produce, recall, or apply; do not just read/watch |
| 7. Provide Feedback | Correct and reinforce | Tell learner if response was correct and why; explain errors |
| 8. Assess Performance | Verify mastery | Measure whether the learning objective was met; provide summative evidence |
| 9. Enhance Retention and Transfer | Ensure durability | Provide variety of contexts, practice over time, or real-world scenarios |

3. **Note the order.** Gagné's sequence is prescriptive: events earlier in the list must occur before events later. For example, Event 6 (Elicit Performance) cannot work if Event 5 (Learning Guidance) has not yet occurred. Mark any violations of this order (e.g., "assessment occurs in Event 4" or "objectives stated after content presentation").

### Phase 2 — Evaluate Coverage and Depth

4. **For each event that is present, grade its execution:**
   - **Present and explicit:** The event happens and is clearly intentional (e.g., "Learning objective is stated at the start of the module").
   - **Present but weak:** The event happens but superficially (e.g., "There is a brief attention-getter, but it is generic and unrelated to the topic").
   - **Absent:** The event does not occur.

5. **For each event that is absent, diagnose why.** Is it:
   - Genuinely unnecessary for this learning objective (rare; justify why)?
   - Assumed to happen outside the instruction (e.g., "Prior knowledge is built in a prerequisite course")?
   - Forgotten or overlooked (likely candidate for improvement)?

### Phase 3 — Identify Gaps and Sequence Violations

6. **List all absent or weak events.** These are your primary findings.

7. **Check for sequence violations.** If Event 8 (Assess Performance) occurs before Event 6 (Elicit Performance), flag it. If Event 2 (Inform Objectives) is stated after content has already been presented, flag it.

8. **Estimate the cognitive impact of each gap.** Ask: "If this event is missing, what will the learner struggle with?"
   - Missing Event 1 → Learner may not engage
   - Missing Event 2 → Learner does not know what success looks like
   - Missing Event 3 → New content may not connect to memory; encoding fails
   - Missing Event 5 → Content is presented but learner cannot retrieve it or apply it
   - Missing Event 6 → No opportunity to practice; learner has false confidence
   - Missing Event 7 → Learner has no way to correct errors
   - Missing Event 9 → Learner forgets content or cannot apply it in new contexts

## Evaluation Criteria

| Check | Pass |
|---|---|
| All 9 events identified and located (or marked absent) in the artifact | Y/N |
| Order of events matches Gagné's prescriptive sequence | Y/N |
| Each present event is graded as explicit, weak, or absent | Y/N |
| For each absent event, a reason (unnecessary/assumed/overlooked) is stated | Y/N |
| Cognitive impact of gaps is diagnosed (not just listed) | Y/N |
| At least one recommendation is concrete (e.g., "Add a worked example in Event 5") | Y/N |

## Red Flags

- All 9 events are marked "present and explicit." Instruction is rarely this complete; recheck that weak or implicit events were not mislabeled.
- Events 1-3 are absent or weak. Learners typically disengage before content presentation, making the rest of the instruction ineffective.
- Event 5 (Learning Guidance) is absent but Event 6 (Elicit Performance) is present. Learners are asked to perform before they have been shown how; expect high failure rates.
- Events 7 and 8 are absent. Learners have no feedback and no summative assessment; you cannot measure whether the instruction worked.
- Event 9 is absent and the instruction is described as a "one-off course" with no follow-up. Learners will forget within days.
- Events are present but in the wrong order (e.g., assessment before practice, or objectives stated after examples).

## Output Format

```
## Gagne's 9 Events Assessment

**Instructional artifact:**
<title, type, duration, audience>

### Event Mapping
| Event | Purpose | Where Found | Grade |
|---|---|---|---|
| 1. Gain Attention | <...> | <...> | Explicit / Weak / Absent |
| 2. Inform Objectives | <...> | <...> | <...> |
| 3. Recall Prior Knowledge | <...> | <...> | <...> |
| 4. Present Content | <...> | <...> | <...> |
| 5. Learning Guidance | <...> | <...> | <...> |
| 6. Elicit Performance | <...> | <...> | <...> |
| 7. Provide Feedback | <...> | <...> | <...> |
| 8. Assess Performance | <...> | <...> | <...> |
| 9. Enhance Retention/Transfer | <...> | <...> | <...> |

### Sequence Violations
<List any departures from the prescribed order, e.g., "Assessment (Event 8) occurs before Practice (Event 6).">

### Absent or Weak Events
| Event | Status | Reason (unnecessary / assumed / overlooked) | Cognitive Impact |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

### Recommendations
1. <Concrete action to address the highest-impact gap>
2. <Concrete action to address the next gap>
...

### Confidence
<high/medium/low> — <justification: e.g., "High — all 9 events were independently located in the artifact with clear timestamps. Cognitive impact diagnosis is based on learning science consensus.">
```
