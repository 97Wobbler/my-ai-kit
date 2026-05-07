---
name: shape-up
display_name: Shape Up (Basecamp)
class: lens
underlying_class: native
domain: agile
source: Ryan Singer, Basecamp, 2018
best_for:
  - Scoping product work within fixed time horizons
  - Distinguishing genuine feature requests from scope creep
  - Aligning stakeholder appetite with development capacity
one_liner: "Fixed-time (6-week) planning method that sets appetite first, then shapes scope to fit."
---

# Shape Up (Basecamp)

## Overview
Shape Up inverts traditional estimation: instead of asking "how long will this take?", it first asks "how much time are we willing to spend, and what would success look like in that box?" You start with a fixed appetite (a time and resource budget), then shape the work to fit it. The discipline is ruthless scope definition — most teams skip this and let scope expand to fill available time. Practitioners use this when they need to ship on a predictable schedule, protect developers from feature bloat, and make stakeholders explicit about trade-offs.

## Analytical Procedure

### Phase 1 — Define the Raw Idea

1. **Capture the problem or request in narrative form.** Write 2-3 sentences describing what users are struggling with or what opportunity exists. No solution yet. If multiple problems are bundled, separate them.

2. **Identify the key stakeholder(s).** Who brought this idea, and what is their real motivation? (Often the stated reason differs from the actual reason.)

3. **List any hard constraints.** Are there regulatory, technical, or timeline dependencies that lock in a deadline? Note them. If there are none, the appetite is negotiable.

### Phase 2 — Set the Appetite

4. **Propose an appetite in terms of developer-weeks (not story points).** Typical appetites: small (1-2 weeks), medium (3-4 weeks), large (5-6 weeks). Do not say "it depends on implementation" — that's abdicating the appetite decision.

5. **For the chosen appetite, state what *won't* be included.** This is the scope-cutting step. What features, platforms, integrations, or edge cases are explicitly out of scope? Be concrete:
   - Bad: "We'll keep it simple."
   - Good: "Mobile app, API integrations, and offline sync are out of scope. Web-only, single user per session."

6. **Define the hill — the desired outcome in customer terms, not implementation terms.** What does success feel like to the end user? What is the smallest version that solves the problem?
   - Bad: "Build a dashboard with filters and export."
   - Good: "Users can see their top 10 revenue sources at a glance without leaving the main page, and there's one way to drill into details."

### Phase 3 — Shaped Brief

7. **Sketch the solution (wireframe or high-level workflow).** Not pixel-perfect. Just enough that a developer could ask clarifying questions. Include key interactions and decision points.

8. **Flag rabbit holes — known unknowns or risky assumptions.** What could derail this work? What do we think will be easy but might not be? What dependency on another team exists?
   - Examples: "Unclear if legacy payment system can handle new currency." "Performance risk if dataset >10k records."

9. **List explicit trade-offs.** For each scope boundary, state the trade-off:
   - Excluding Y saves 1 week of polish but leaves users unable to Z.
   - Excluding X saves 2 weeks but means we can't A/B test initially.

### Phase 4 — Pressure Test Against Reality

10. **Assign a small shaped group (designer + 1-2 developers).** Before committing to the appetite, have them spend 1-2 days working on the riskiest part. Do prototype or spike work — just enough to validate the appetite is realistic.

11. **Ask the shaped group: "Can this be done in the appetite, or do we need to descope?"** Possible answers:
    - **It fits.** Proceed to build.
    - **It's tight, but doable with these trade-offs.** Refine the brief, lock those trade-offs, proceed.
    - **It overshoots.** Return to Phase 2 — cut scope or increase appetite. No heroics.

12. **Sign off on the brief.** Designer and lead developer agree the hill, scope boundaries, and rabbit holes are realistic. This is not a commitment to a date — it's a contract on scope.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Appetite is stated in developer-weeks, not story points or "ASAP" | Y/N |
| Out-of-scope items are explicit, not implied | Y/N |
| The hill is defined in user outcomes, not feature list | Y/N |
| At least 3 rabbit holes identified (if none, dig deeper) | Y/N |
| Trade-offs explain what is lost by excluding scope | Y/N |
| Shaped group spent time on riskiest work, not just planning | Y/N |
| Brief was pressure-tested and appetite survived intact or was revised | Y/N |

## Red Flags

- Appetite is stated as a date, story points, or "as long as it takes." The whole point is to declare a fixed box.
- Out-of-scope list is vague ("we'll do it simple" instead of "no mobile, no batch exports, single user only").
- The hill is a feature list, not an outcome. "Users can filter by date, price, and category" is features. "Users can find what they bought in under 10 seconds" is an outcome.
- Shaped group spent all 2 days in planning meetings, not building. If you haven't prototyped the risky bit, the appetite is guesswork.
- Appetite was defended without revision after pressure test. Either the test was too soft or the appetite was arbitrary to begin with.
- Stakeholder appetite kept changing during shaping. That usually means the original appetite was not genuine — return to Phase 1 and talk to the decision-maker directly.

## Output Format

```
## Shape Up Brief

**Problem (raw idea):**
<2-3 sentences>

**Stakeholder(s):**
<who brought this, why>

**Appetite:**
<1-2 weeks / 3-4 weeks / 5-6 weeks>

**Hill (success in user terms):**
<user outcome, not feature list>

### Scope Boundaries
| Out of Scope | Rationale | Time Saved |
|---|---|---|
| <item> | <why it's excluded> | <e.g., "1 week"> |

### Rabbit Holes
1. <unknown or risk>
2. <unknown or risk>
3. ...

### Trade-offs
- **Excluding X** saves <time> but means users cannot <consequence>.
- **Excluding Y** saves <time> but leaves <gap>.

### Solution Sketch
<Wireframe or high-level workflow description. Key interactions and decision points.>

### Pressure Test Result
- **Shaped group:** <names>
- **Spike duration:** <days>
- **Outcome:** [It fits | Tight but doable with revisions | Overshoots — descope needed]
- **Revisions made (if any):** <...>

### Confidence
<high | medium | low> — <justification: e.g., "high — spike validated the risky path, stakeholder appetite is firm, team has done similar work before" or "medium — performance assumptions unvalidated, stakeholder may pressure scope upward">
```
