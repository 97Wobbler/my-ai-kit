---
name: nielsens-10-heuristics
display_name: Nielsen's 10 Usability Heuristics
class: lens
underlying_class: native
domain: ux
source: Jakob Nielsen, 1994 (Usability Engineering) and 2020 (revised heuristics)
best_for:
  - Rapid evaluation of interface usability without formal user testing
  - Identifying recurring patterns of poor design across products
  - Training non-specialists to spot usability problems
one_liner: "Check interface usability against Nielsen's 10 heuristics."
---

# Nielsen's 10 Usability Heuristics

## Overview
Nielsen's 10 Heuristics are a set of broad, empirically-derived guidelines for evaluating how well an interface lets users accomplish their goals without confusion, frustration, or waste. Rather than measuring user behavior quantitatively, the heuristics encode patterns of failure that Nielsen observed across thousands of interfaces. Practitioners use them for rapid expert review — one analyst with training can walk a product and flag problems in hours that might take formal user testing weeks to surface. The discipline is systematic application: each heuristic is a lens, and they must all be examined.

## Analytical Procedure

### Phase 1 — Setup

1. **Define the scope and user context.** What is the product or feature? Who is the intended user? What is a typical task they would perform? Write this in one sentence each. This prevents the evaluator from drifting into "general usefulness" and keeps focus on the specific user-task pairing.

2. **Gather artifacts.** Collect the actual interface (live product, prototype, screenshots, or recorded walkthrough). Do not rely on description. If a feature is described but you cannot see it, mark it as out-of-scope for this evaluation.

3. **Plan a walkthrough.** Identify 3–5 realistic user journeys. A journey is a sequence of actions that a user would perform (e.g., "sign up → upload a file → share with a colleague → check download history"). You will evaluate each heuristic against these journeys, not against isolated screens.

### Phase 2 — Evaluate Each of the 10 Heuristics

For each heuristic, perform the following steps:

4. **Read the heuristic definition and concrete examples.** The 10 heuristics are:

   1. **Visibility of system status** — The system keeps users informed in real time. (Examples: loading spinners, error messages with context, status of long-running tasks.)
   
   2. **Match between system and real world** — The system uses language and metaphors from the user's world, not the engineer's. (Examples: "trash" instead of "rm -rf", "save" instead of "persist".)
   
   3. **User control and freedom** — Users can undo/redo, exit unwanted modes, and recover from mistakes without data loss. (Examples: undo button, "cancel" next to "delete", confirmation dialogs.)
   
   4. **Error prevention and recovery** — The system prevents problems before they happen; if problems occur, error messages are plain-language and suggest a fix. (Examples: disabling invalid buttons, client-side validation, "This email is already registered — do you mean to sign in?" instead of "Invalid input.")
   
   5. **Aesthetic and minimalist design** — The interface contains only what is necessary for the task. No clutter, no ads, no decorative elements that distract from the goal. (Examples: form with only required fields visible, dashboard with essential metrics only.)
   
   6. **Help and documentation** — The product is self-explanatory, but if help is needed, it is easy to search, focused on real tasks, and concrete. (Examples: contextual tooltips, a searchable FAQ, "how to X" guides.)
   
   7. **Flexibility and efficiency of use** — The system offers shortcuts for frequent tasks and allows power users to operate faster. (Examples: keyboard shortcuts, saved templates, bulk actions.)
   
   8. **Consistency and standards** — The system follows established conventions. Buttons look like buttons. Navigation is in the same place on every page. Interactions behave the same way throughout. (Examples: confirming destructive actions, using standard icon styles.)
   
   9. **Error diagnosis** — If an error occurs, the message explains what went wrong, why it happened, and what to do next — in the user's language. (Examples: "Password too short (minimum 8 characters)" instead of "Invalid input", "Your file is larger than 50MB — please compress or split it".)
   
   10. **Emergency exits** — Users can always get out of a mode or dialog without losing their work. (Examples: "X" button on modals, back button works as expected, saves in progress.)

5. **For each heuristic, walk the user journeys and note violations.** A violation is a specific moment in the walkthrough where the interface fails the heuristic. Write each violation as: *Heuristic N: [What the user is trying to do] → [What the interface does wrong].*
   
   Example: "Heuristic 1 (Visibility): User uploads a large file → no progress indicator appears; it looks like the upload hung."

6. **Rate the severity of each violation** on a three-point scale:
   - **Critical** — The user cannot complete the task without help or data loss. (Stop-the-task failures.)
   - **Major** — The user can complete the task but only with significant effort, confusion, or frustration. (Slows or confuses but doesn't block.)
   - **Minor** — The user notices something odd but it doesn't materially affect the task. (Rough edges.)

7. **Record violations in a table.** (See Output Format below.) If a heuristic has zero violations in the walkthrough, note it as "PASS" but do not skip applying the heuristic — try harder to find edge cases or less common journeys before concluding the interface actually satisfies it.

### Phase 3 — Synthesis

8. **Identify patterns.** Do violations cluster around a few heuristics? (Example: three critical violations all in Heuristic 4 = error handling is broken.) Or is the damage spread? Patterns inform priority.

9. **Distinguish real problems from reviewer bias.** If you are rating something "minor," ask: Would the user notice this and care? Or is this a designer's preference leaking into the evaluation? Mark evaluator judgment calls explicitly.

10. **Estimate effort to fix each critical violation.** Low-effort fixes (copy change, button re-label) vs. high-effort (redesign a flow, add new infrastructure). This informs the roadmap.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Scope (product, user, task) is explicitly defined | Y/N |
| At least 3 realistic user journeys were planned and walked | Y/N |
| All 10 heuristics were applied to at least one journey | Y/N |
| Each violation is specific (what, where, why) and not vague | Y/N |
| Each violation is rated Critical/Major/Minor | Y/N |
| At least one violation is identified (unless the product is genuinely near-perfect) | Y/N |
| Patterns across heuristics are noted | Y/N |
| Estimations of fix effort are included for critical violations | Y/N |

## Red Flags

- All 10 heuristics rated as "PASS" with no violations found. Either the interface is exceptionally well-designed (rare) or the reviewer applied the heuristics shallowly — walked too few journeys or accepted edge cases as acceptable.
- Violations are described in jargon or evaluator opinion ("bad UX", "confusing") rather than as concrete user actions and system failures. These are unfixable feedback.
- Only 2–3 heuristics are evaluated in depth; others are marked "N/A" or skipped. Skipping shortcuts the analysis. Apply all 10 to the walkthrough.
- No distinction between Critical, Major, and Minor violations. Severity rating is essential for prioritization. Without it, the report is a list, not actionable insight.
- The same violation is listed under multiple heuristics. Usually, a violation belongs to one heuristic; if it belongs to several, it is a system-level problem (which is worth noting, but don't double-count effort).
- Violation is stated as a fix ("add a loading bar") not as a failure. The lens should report what is wrong, not prescribe the solution. Leaving room for the designer to innovate.

## Output Format

```
## Nielsen's 10 Heuristics Evaluation

**Scope:**
- Product: <name/description>
- User: <role/persona>
- Task: <primary user journey>

### Walkthrough Journeys
1. <journey 1>
2. <journey 2>
3. <journey 3>
(additional as needed)

### Violations by Heuristic

| Heuristic | Journey | What the user is doing | What the interface does wrong | Severity | Effort to fix |
|---|---|---|---|---|---|
| 1. Visibility | <journey> | <action> | <failure> | Critical/Major/Minor | Low/Medium/High |
| 4. Error prevention | <journey> | <action> | <failure> | Major | Medium |
| (... continue for all heuristics with violations) | | | | | |

### Heuristics with no violations
- 2. Match between system and real world — PASS
- 6. Help and documentation — PASS
(list only those that passed)

### Pattern Analysis
**Concentration:** Violations cluster in <heuristic names> — indicates <root issue>.

**Severity distribution:** _X_ Critical, _Y_ Major, _Z_ Minor violations identified.

**High-effort vs. low-effort fixes:** 
- Quick wins (< 1 day): <...>
- Medium effort (1–3 days): <...>
- Large effort (> 1 week): <...>

### Critical Violations (Roadmap Priority)
1. <violation> — blocks <user goal>. Fix: <brief approach>. Effort: <estimate>
2. <...>

### Evaluator Notes
<Any judgment calls, edge cases not covered by walkthrough, or caveats on the evaluation>

### Confidence
<high/medium/low> — <justification. Example: "High — all 10 heuristics applied systematically across 5 journeys; violations are concrete and reproducible. Low — only 2 journeys were walked due to time constraints; some heuristics (e.g., Help) may have violations not yet surfaced.">
```
