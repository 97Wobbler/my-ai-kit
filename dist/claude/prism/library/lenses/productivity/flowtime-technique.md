---
name: flowtime-technique
display_name: Flowtime Technique
class: lens
underlying_class: native
domain: productivity
source: Soren Bjornstad; popularized in focus and attention research
best_for:
  - Uninterrupted deep work sessions when task boundaries are unclear
  - Protecting flow state from artificial time boundaries
one_liner: "Work without interruption until the task is complete — the time-unbounded alternative to Pomodoro."
---

# Flowtime Technique

## Overview
Flowtime abandons fixed time intervals (like Pomodoro's 25 minutes) and instead works in uninterrupted blocks until a natural stopping point emerges—task completion, energy depletion, or a genuine external constraint. The discipline is recognizing when the work is *actually done*, not when the timer fires. Practitioners use this when deep focus matters more than consistency, when tasks have irregular completion times, and when interrupting flow to restart a timer adds friction rather than structure.

## Analytical Procedure

### Phase 1 — Pre-session Setup

1. **Define the work unit clearly.** Write what "done" looks like for this session in one sentence. Not vague ("work on the report") but observable: "complete the first draft of Section 3 with all citations checked" or "fix the authentication bug and verify it passes the test suite."

2. **Remove or silence interruptions.** Phone away, email client closed, Slack status set to unavailable, browser notifications off. Document what you're protecting against so you can evaluate later whether the barriers worked.

3. **Set a soft minimum duration.** Write down a realistic floor—the earliest point where you'd consider stopping if energy crashes (e.g., "at least 45 minutes, no stopping before"). This prevents premature exit due to minor friction.

### Phase 2 — Active Session

4. **Start the work.** Begin immediately; do not set a timer. Log the start time.

5. **Notice your state continuously.** As you work, track three signals:
   - **Momentum:** Are you making progress? Is the next step obvious? (Yes = continue)
   - **Energy:** Can you still think clearly and make good decisions? (Yes = continue)
   - **Completion proximity:** Is the work unit actually done, or is there meaningful remainder? (Done = stop; remainder = continue)

6. **Watch for false endings.** When you feel the urge to stop, pause and ask: "Is the work unit actually done, or am I hitting a hard part and seeking escape?" If it's a hard part, push through 5–10 more minutes. If it's genuine completion, stop.

7. **Log the stop time and reason.** Write down why you stopped: "Completed the first draft," "Energy crashed after 110 minutes," "Got interrupted by a hard-stop meeting," etc.

### Phase 3 — Post-session Reflection

8. **Measure the session.** Duration, actual work output (lines of code, words written, bugs fixed—whatever is countable), stopping reason, whether the work unit was actually complete.

9. **Note state changes.** How did your focus, energy, and clarity evolve over time? Did a 45-minute session feel different from a 120-minute one? Did specific stopping reasons correlate with quality or completion?

10. **Track the accuracy of your pre-session "done" definition.** Did you stop exactly where you said "done" was, or did scope creep extend it? If scope creep happened, was it legitimate (discovered necessary work) or avoidable (poor planning)?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Work unit is defined with a concrete, observable stopping criterion | Y/N |
| Interruptions were actively removed or silenced before the session | Y/N |
| A soft minimum duration was set and logged | Y/N |
| Session was timed (start and stop recorded) | Y/N |
| Stopping reason is documented and truthful | Y/N |
| Work unit completion matches the pre-session definition (or reason for mismatch is noted) | Y/N |
| At least 3 sessions completed to establish a pattern | Y/N |

## Red Flags

- Every session ends exactly at the soft minimum or a round number (60, 90 minutes). You're drifting back to time-boxing; the technique isn't being applied.
- Stopping reason is always vague ("felt like a good time to stop") or untruthful ("got bored" when the actual work was incomplete). This prevents learning when Flowtime is actually working.
- Work units are not actually complete; sessions end before "done" was achieved. This suggests either over-ambitious pre-session definitions or poor energy/focus management.
- No pattern emerges across 3+ sessions. Different work types may need different timings, but if *every* session is chaotic and unpredictable, Flowtime isn't matching your actual work rhythm.
- The soft minimum is never reached in any session. Either it's set too high or Flowtime doesn't suit your work type (return to time-boxing).

## Output Format

```
## Flowtime Session Log

**Work unit:** <one sentence defining "done">

**Pre-session setup:**
- Interruptions removed: <list>
- Soft minimum duration: <minutes>
- Start time: <HH:MM>

**Session activity:**
- Stop time: <HH:MM>
- Total duration: <minutes>
- Stopping reason: <completed | energy crash | external interrupt | other>

**Work output:**
- Quantified output: <units delivered — lines, words, bugs fixed, etc.>
- Work unit status: <complete | incomplete — specify remainder if incomplete>

**State observations:**
- Focus trajectory: <how focus evolved over the session>
- Energy trajectory: <when did energy peak or crash?>
- Clarity at stopping point: <high | medium | low — can you make good decisions right now?>

**Post-session reflection:**
- Was the "done" definition accurate? <yes | no — explain>
- Legitimate scope creep or avoidable? <or N/A if no creep>
- Key insight: <one observation about your work rhythm from this session>

**Confidence:** <high | medium | low> — <justification based on completeness of logging and clarity of stopping reason>
```
---

## Meta-note for practitioners

Flowtime is not "work until you collapse." The soft minimum prevents quitting at the first sign of discomfort, but continuous logging of stopping reasons reveals whether you're actually hitting natural completion or just running out of focus discipline. Three to five logged sessions usually show whether this technique matches your work style; if sessions are chaotic and stopping reasons are never truthful, Pomodoro or another fixed-interval method may be more honest for your brain.
