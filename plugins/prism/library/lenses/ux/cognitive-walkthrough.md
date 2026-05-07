---
name: cognitive-walkthrough
display_name: Cognitive Walkthrough
class: lens
underlying_class: native
domain: ux
source: Wharton, Lewis, Polson (1994); extended in HCI by John Spencer
best_for:
  - Evaluating UI clarity for first-time users
  - Identifying gaps between designer intent and user mental model
  - Catching task-blocking friction before testing
one_liner: "Walk systematically through the cognitive steps a new user will actually face."
---

# Cognitive Walkthrough

## Overview
A Cognitive Walkthrough simulates a plausible user stepping through a UI for the first time, asking at each action whether the user would know what to do next, whether they would recognize the correct action, and whether they would interpret the feedback correctly. Unlike usability testing, which observes real users, the walkthrough is a structured interrogation performed by the design team — it catches friction at the design table before involving participants. Practitioners use it to audit interfaces for clarity, especially when redesigning task flows or onboarding.

## Analytical Procedure

### Phase 1 — Prepare the Scenario

1. **Define the user persona.** Write a one-sentence description: background, goal clarity, prior experience with the domain. Example: "Accountant with no prior SaaS experience, needs to record a transaction." This persona anchors every question.

2. **Select a single, discrete task.** Not "use the app," but "create and save an invoice." The task should complete in 3–8 steps. If it's longer, break it and walkthrough each segment separately.

3. **List the sequence of steps the UI *expects* the user to follow.** This is the "happy path." Write them as actions: "Click 'New Invoice' → Enter amount → Select customer → Click 'Save.'" Do not paraphrase; be literal about UI affordances.

4. **For each step, note the UI state (what the user sees).** Screenshot or describe: button labels, colors, visibility of controls, presence of hints or errors. This is the ground truth the user will evaluate.

### Phase 2 — Walk Through Each Step

For each step in the happy path, answer all four questions below. Be honest — the user *might* fail. That's the point.

5. **Question 1: Will the user know what to do?**
   - Has the previous screen explained or implied what action comes next?
   - Is there a logical connection between the current state and the next action?
   - Write: <clear / unclear / needs domain knowledge>
   - If unclear, note why: missing label, ambiguous icon, hidden affordance.

6. **Question 2: Will the user recognize the correct action on screen?**
   - Among all visible controls, will the user's eye land on the correct one?
   - Is it labeled with familiar language?
   - Does it look clickable / interactive?
   - Write: <recognizable / missed / confused with something else>
   - If missed, note: is it below the fold? Color too close to background? Competing visual weight?

7. **Question 3: After acting, will the user understand the feedback?**
   - Does the screen change in an expected way?
   - Is the new state obviously different from the old one?
   - Is progress toward the goal visible (e.g., "Step 2 of 5")?
   - Write: <understood / ambiguous / contradicts expectation>
   - If ambiguous, describe: no confirmation, confusing redirect, error message too cryptic.

8. **Question 4: Will the user interpret feedback correctly in context of their goal?**
   - Does the feedback feel like progress or a dead end?
   - If an error occurred, will the user know how to fix it?
   - Will the user believe they're on track?
   - Write: <confident / uncertain / lost>
   - If lost, note: error doesn't explain the cause, undo isn't obvious, too many steps to recover.

### Phase 3 — Synthesize Findings

9. **Tally the responses.** Count how many steps had all four questions answered as "clear / recognizable / understood / confident." Divide by total steps. This is your *clarity score*.

10. **Identify primary blockers.** Which steps had 2+ weak answers? These are the moments users are most likely to abandon the task. Rank them by position (earlier = higher priority).

11. **Separate "mental model mismatch" from "visual design."** Some failures are because the user won't think of the next action (design flaw). Others are because the right action exists but isn't visible (UI flaw). Flag each separately — they have different remedies.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Persona is specific (background + goal + experience level stated) | Y/N |
| Task is single, discrete, completable in 3–8 steps | Y/N |
| Happy path is written as literal UI actions, not abstractions | Y/N |
| All four questions answered for every step | Y/N |
| At least 1 blockers identified (step with 2+ weak answers) | Y/N |
| Blockers labeled as "mental model" or "visual design" | Y/N |
| No step was answered with pure speculation (all answers grounded in UI state) | Y/N |

## Red Flags

- All four questions answered "clear / recognizable / understood / confident" for every step. Either the interface is near-perfect (rare) or the walkthrough was lenient — re-run with a less familiar persona.
- Questions 1 and 2 pass but Question 3 fails repeatedly. The UI is invisible to the user even when they do the right thing; visual feedback is broken.
- The persona is generic ("typical user"). A Walkthrough depends entirely on specificity. Redo with a real user archetype in mind.
- No distinction made between mental model failures and visual design failures. You've identified problems but not where to fix them.
- Steps 7–8 fail but steps 1–3 pass. The user gets lost mid-task; this often signals missing progress indicators or unclear state transitions.
- Feedback for Question 4 is "uncertain but they'll figure it out." That's a walkthrough failure, not a user strength. If they have to figure it out, the design didn't work.

## Output Format

```
## Cognitive Walkthrough Report

**Persona:**
<Background, goal, prior experience — one sentence>

**Task:**
<Single, discrete task in plain language>

**Happy Path:**
1. <UI action>
2. <UI action>
3. ...

### Step-by-Step Analysis

#### Step 1: <action>
**UI State:** <description or screenshot reference>

1. Will user know what to do? **<clear/unclear/needs domain knowledge>** — <explanation>
2. Will user recognize correct action? **<recognizable/missed/confused>** — <explanation>
3. Will user understand feedback? **<understood/ambiguous/contradicts>** — <explanation>
4. Will user interpret correctly in goal context? **<confident/uncertain/lost>** — <explanation>

#### Step 2: <action>
...

### Synthesis

**Clarity Score:** _/_ steps passed all four questions = _%

**Primary Blockers:**
1. Step <N>: <problem> [mental model / visual design]
2. Step <N>: <problem> [mental model / visual design]

**Critical Path Issues:**
<If multiple blockers cluster early or mid-task, describe the user's likely abandonment point.>

### Confidence
<high/medium/low> — <justification (e.g., "high confidence in visual design blockers; medium on mental model gaps without user validation")>
```
