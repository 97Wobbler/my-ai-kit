---
name: nudge-choice-architecture
display_name: Nudge / Choice Architecture
class: lens
underlying_class: native
domain: economics
source: Richard Thaler & Cass Sunstein (Nudge, 2008); foundational work in behavioral economics
best_for:
  - Designing interventions that steer behavior without restricting choice
  - Auditing decision environments for hidden bias or friction
  - Increasing desired outcomes (savings, health, organ donation) with minimal coercion
one_liner: "Guide decisions while preserving autonomy by designing the choice environment."
---

# Nudge / Choice Architecture

## Overview
A nudge is an intervention that alters the choice environment in a way that predictably steers behavior toward a specified outcome, without removing options or changing economic incentives materially. The discipline is recognizing that *how* choices are presented (defaults, framing, salience, social proof) has as much power as what incentives reward. Practitioners use this when they want to move a metric without regulation, pricing changes, or removing an option entirely — they need to shift the "path of least resistance."

## Analytical Procedure

### Phase 1 — Map the Current Decision Environment

1. **Identify the target behavior.** State what action you want more people to take. Write it as a concrete verb: "enroll in 401(k)" not "save for retirement."

2. **Observe the current choice architecture.** Document:
   - **Default state**: What happens if the user does nothing?
   - **Choice set**: What options are presented? In what order?
   - **Friction**: What steps, forms, or cognitive load must the user overcome?
   - **Salience**: What information is prominent vs. hidden?
   - **Social signal**: What do others appear to be doing? Is that information visible?
   - **Framing**: Is the option labeled positively or negatively? ("Opt in" vs. "Opt out"?)

3. **Measure the baseline.** Record the current adoption or take-up rate of the target behavior. This is your control.

### Phase 2 — Identify Barriers and Behavioral Pinch Points

4. **Interview 5–10 users who rejected the target behavior.** Ask concretely:
   - "Walk me through what you did instead. Why?"
   - "What would have made this easier?" (Not "Would you like this to be easier?" — that invites yes.)
   - "Did you know this option existed? If yes, why didn't you choose it?"
   - "What did you think would happen if you chose it?"

5. **Categorize barriers by type:**
   - **Friction** — too many steps, forms, or time
   - **Misunderstanding** — user thought the option meant something else
   - **Salience** — user didn't notice it was available
   - **Default effect** — inertia; the default option was acceptable enough
   - **Social proof** — user thought others weren't doing it
   - **Framing** — the option sounded risky, painful, or uncool
   - **Real incentive misalignment** — the user genuinely has a reason not to do it

6. **Distinguish real barriers from choice-architecture barriers.** If interviews repeatedly reveal "I didn't know about it" or "I thought I had to fill out 20 forms," those are architecture problems. If they say "I can't afford it" or "It conflicts with my values," nudges won't help — you need to change incentives or target a different population.

### Phase 3 — Design the Nudge

7. **Map each barrier to a lever in choice architecture:**
   - **Friction** → Simplify forms. Reduce steps. Auto-fill. Offer a shortcut path.
   - **Misunderstanding** → Reframe the name or description. Add one-sentence clarification.
   - **Salience** → Move it higher on the screen. Add a callout. Send a reminder email.
   - **Default effect** → Switch the default (if legally and ethically permissible). Or make the target option the "path of least resistance."
   - **Social proof** → Show a count ("X% of your peers chose this") or a testimonial.
   - **Framing** → Reword in positive or gain terms ("Save $X per month") vs. loss terms ("Lose $X if you don't").

8. **Generate 2–4 nudge variants.** Do not remove or add economic incentives. Do not restrict choice. For each variant:
   - Name it (e.g., "Default + Social Proof," "Simplified Form + Salience Bump").
   - Write the exact change to the choice environment (e.g., "Move enrollment link to top of dashboard. Display: '87% of employees in your department have enrolled.'").
   - Predict the direction and magnitude of effect (e.g., "Expect enrollment to rise 10–20% based on similar defaults in the literature").

### Phase 4 — Test and Measure

9. **Run a controlled test if possible.** Split users randomly:
   - Control: Current environment.
   - Treatment 1–3: Each nudge variant.
   - Duration: Long enough to observe at least 100 target actions in the smallest group.

10. **Measure outcomes:**
    - Primary: Adoption/take-up rate.
    - Secondary: Speed (time to decision), persistence (do people stick with the choice?), and spillover (does the nudge affect other behaviors?).
    - Check for backfire: Did the nudge alienate a subset (e.g., "I felt manipulated")?

11. **Document the delta.** For each variant:
    - Adoption rate vs. control.
    - Confidence interval or statistical test (if available).
    - Cost to implement.
    - Scalability (can this work for the full user base?).

### Phase 5 — Validate Against Ethical Bounds

12. **Ask:**
    - Does the nudge steer users toward an outcome that is *in their interest*, not just in the institution's interest?
    - Would users, if told the nudge existed, feel it was fair and reasonable?
    - Is the nudge durable? (If people discover it, do they resent it or accept it?)
    - Does it exploit a genuine cognitive bias or a temporary attention gap that education could fix?

If the answer to any of these is "no," the nudge may be manipulative rather than helpful. Revise or abandon.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Target behavior is stated as a concrete verb | Y/N |
| Current choice architecture was observed and documented across all 6 dimensions (default, choice set, friction, salience, social signal, framing) | Y/N |
| Baseline adoption rate was measured | Y/N |
| Barriers were collected from actual users, not assumed | Y/N |
| At least one barrier was identified as a choice-architecture problem (not a real incentive problem) | Y/N |
| Nudge variants map barriers to specific levers (not vague) | Y/N |
| Each variant includes predicted effect direction and approximate magnitude | Y/N |
| Test design achieves random assignment and adequate sample size | Y/N |
| Ethical validation step was completed | Y/N |

## Red Flags

- Barriers were inferred from theory, not from user interviews. "Users probably don't know about this option" without evidence is guessing.
- The "nudge" actually changes the incentive (e.g., adding a $5 bonus). That is not a nudge; it's a price change.
- No baseline measurement. You cannot claim the nudge worked without knowing the starting point.
- The nudge steers people away from their own stated preference. ("They *think* they want X, but we know Y is better.") This is paternalism, not choice architecture.
- All variants go in the same direction with similar magnitude. If a social-proof nudge and a framing nudge produce identical results, the environment may have a bigger problem that nudges cannot fix.
- Ethical validation is missing or dismissive. "Our users are unsophisticated, so they won't notice" is not a valid answer.
- Test ran for only a few days. Nudges often decay over time as users learn the environment; short windows overestimate effect.

## Output Format

```
## Nudge / Choice Architecture Assessment

**Target behavior:**
<concrete verb describing the desired action>

**Current adoption rate:**
<baseline percentage or count>

### Choice Environment Map (Current State)
| Dimension | Observation |
|---|---|
| Default | <what happens if user does nothing> |
| Choice set | <what options are presented, in what order> |
| Friction | <steps, forms, time required> |
| Salience | <prominent vs. hidden information> |
| Social signal | <visible cues about what others are doing> |
| Framing | <positive/negative labeling, loss/gain language> |

### Barriers to Target Behavior
| Barrier | Type | Evidence | Real incentive problem? |
|---|---|---|---|
| <...> | Friction / Misunderstanding / Salience / Default / Social / Framing | <from interviews> | Y/N |

### Nudge Variants
#### Variant 1: <Name>
**Change:** <Exact modification to choice environment>
**Predicted effect:** <Direction and magnitude, e.g., "+15% adoption">
**Rationale:** <Which barrier does this address and how?>

#### Variant 2: <Name>
...

### Test Design
- **Assignment:** Random split into control + <N> treatment groups
- **Sample size:** <number> target actions per group
- **Duration:** <weeks or months>
- **Primary metric:** Adoption rate
- **Secondary metrics:** Decision speed, persistence, spillover, backfire signals

### Results
| Variant | Adoption rate | Δ vs. control | 95% CI | Cost to implement | Recommendation |
|---|---|---|---|---|---|
| Control | <...>% | — | — | — | — |
| Variant 1 | <...>% | <...>% | <...> | <...> | Scale / Iterate / Abandon |

### Ethical Validation
- Is the nudge in users' interest? <Yes / No / Conditional>
- Would users find it fair if disclosed? <Yes / No / Unknown>
- Is it durable (survives discovery)? <Yes / No / Uncertain>
- Does it exploit bias or fill an attention gap? <Bias / Gap / Both>
- **Verdict:** Acceptable for deployment / Needs revision / Reject

### Confidence
<high | medium | low> — <Justification: sample size, effect magnitude, generalizability to other populations, or ethical concerns>
```
---
