---
name: rice-scoring
display_name: RICE Scoring
class: lens
underlying_class: native
domain: product-management
source: Intercom, 2016 (Sean McBride); popularized across product teams
best_for:
  - Prioritizing product features and initiatives across a portfolio
  - Making explicit the trade-offs between reach, impact, effort, and confidence
  - Surfacing disagreements about relative priority before committing resources
one_liner: "Quantitatively prioritize features via Reach × Impact × Confidence / Effort."
---

# RICE Scoring

## Overview
RICE is a scoring model that combines four dimensions of a feature or initiative—how many users it reaches, how much it improves their experience, how confident you are in your estimates, and how much engineering effort it requires—into a single comparable number. The output is not a decision rule but a ranking that forces product teams to articulate assumptions about scope, benefit, and cost upfront. Practitioners use it to break tie-breaking deadlock, to make resource-constrained prioritization repeatable, and to make implicit disagreements visible.

## Analytical Procedure

### Phase 1 — Define the Initiative

1. **Write a one-sentence description of the feature or initiative.** No vision language. What does it do?

2. **Identify the target user population.** Who uses this feature? Be specific:
   - Total addressable market (e.g., "all paid users" vs. "users in US") 
   - Affected segment (e.g., "power users who create >10 reports/month")
   - Include any geographic, plan-tier, or behavioral constraints.

### Phase 2 — Estimate Reach

3. **Estimate the number of users who will encounter or benefit from this feature in the next time period (typically the next quarter or year).**
   - If the initiative is a mandatory update, Reach = % of active users who will be exposed to it.
   - If it's optional (e.g., a new report type), Reach = estimated % of target segment who will use it.
   - State the time window explicitly: "Reach over Q2 = 15,000 users, or 30% of power users."
   - Disagree out loud: If the team split on this estimate, write both numbers and note the disagreement.

4. **Sanity-check the reach estimate against historical data:**
   - What was adoption of similar features? (e.g., previous optional reports, settings changes)
   - Did users churn if they were forced to adopt? 
   - Has the user base or behavior changed since the last comparable feature?
   - Document the comparables used or note if none exist.

### Phase 3 — Estimate Impact

5. **Define what "impact" means for this feature.** Impact is user outcome, not business outcome. Choose one primary metric:
   - Time saved (e.g., "saves 2 hours/month per user")
   - Frequency increase (e.g., "increases report exports by 40%")
   - Error reduction (e.g., "eliminates 90% of manual data entry")
   - Satisfaction (e.g., "resolves the top user complaint")
   
   Do not conflate impact with reach. A feature that reaches 1000 users but saves each one 5 hours is high-impact. A feature that reaches 100,000 users but saves 1 minute is not.

6. **Map impact to a 3–4 point scale:**
   - **High (3):** Changes user behavior materially or solves a blocking problem. Users would notice immediately if it disappeared.
   - **Medium (2):** Noticeable improvement but not transformative. Nice-to-have.
   - **Low (1):** Minor convenience or edge-case benefit.
   
   Justify your choice with user feedback, observed usage, or explicit hypothesis if data is absent.

### Phase 4 — Estimate Confidence

7. **Rate your confidence in the reach and impact estimates together on a 0.5–1.0 scale:**
   - **1.0 (High):** Historical data exists (similar feature shipped, user feedback is explicit, behavior is predictable).
   - **0.75 (Medium-High):** One dimension well-measured, the other estimated (e.g., you know reach from sign-ups but impact is modeled).
   - **0.5 (Low):** Both reach and impact are hypothesis-driven with no prior data.
   
   This is not a vote. It's a penalty for uncertainty. A high-reach, high-impact feature with low confidence (0.5) still scores well, but the team should plan to validate before full rollout.

### Phase 5 — Estimate Effort

8. **Break effort into engineering weeks (one engineer, full-time).**
   - Include design, implementation, testing, and one round of bug fixes.
   - Do not include ongoing maintenance, support, or future scaling.
   - If multiple teams are involved, sum their effort: "3 weeks backend + 2 weeks frontend = 5 weeks effort."
   
9. **Pressure-test the estimate:**
   - Does this match the scope? If the feature description is vague, the estimate is wrong.
   - Have similar features taken longer or shorter? Note the deltas.
   - If the team is uncertain, use the upper-bound estimate or break the feature into smaller slices.

### Phase 6 — Calculate and Rank

10. **Compute RICE = (Reach × Impact × Confidence) ÷ Effort.**
    - Reach: numeric (e.g., 10,000 users)
    - Impact: 1, 2, or 3
    - Confidence: 0.5, 0.75, or 1.0
    - Effort: weeks
    - Example: (10,000 × 2 × 0.75) ÷ 5 = **3,000 RICE score**

11. **Rank all features in the backlog by RICE score.** Ties are broken by confidence (prefer high-confidence unknowns over low-confidence bets) or by strategic importance (defer to PM judgment, but document the override).

12. **Inspect the ranking for absurdities:**
    - Does a high-RICE feature depend on a low-RICE feature shipping first? Note the dependency.
    - Are features with very different confidence levels now interleaved? Consider running two backlogs: "high-confidence bets" and "validated experiments."
    - Did a low-reach, high-impact feature score surprisingly low because of effort? That's correct — it signals that the feature is expensive to build, not that it's unimportant. Use this to decide whether to descope or deprioritize.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Every initiative has a one-sentence description | Y/N |
| Reach is bounded to a specific user segment and time window | Y/N |
| Reach estimate is compared against historical adoption data or explicitly flagged as hypothesis | Y/N |
| Impact is defined as a user outcome, not business outcome | Y/N |
| Impact is justified with user feedback or explicit hypothesis | Y/N |
| Confidence is scored between 0.5 and 1.0 and is transparent about what is known vs. assumed | Y/N |
| Effort includes all work (design, implementation, test, bug fixes) and excludes ongoing maintenance | Y/N |
| RICE calculation is shown (not just final score) | Y/N |
| Ranking is inspected for logical absurdities and dependencies | Y/N |

## Red Flags

- Reach is expressed as a percentage without a denominator ("20% of users" — 20% of which population?).
- Impact is stated as a business metric ("will increase revenue by $X") rather than user outcome.
- Confidence is 1.0 (100% certain) for every estimate. Uncertainty is always present; missing it signals overconfidence.
- Effort includes speculative work ("we might also add analytics," "we might need to refactor the backend"). Scope creep in estimates inflates effort and suppresses RICE scores.
- Two features have identical RICE scores but radically different confidence or reach profiles. The tie-breaker rule (confidence, then strategy) was never applied.
- The ranking puts a 3-week feature below a 15-week feature despite both having similar impact. Check whether the low-effort feature's reach or impact estimate is understated.
- Reach, Impact, or Confidence estimates changed mid-prioritization without re-scoring all features. RICE is a snapshot; if assumptions shift, recalculate.

## Output Format

```
## RICE Scoring Output

**Initiative:** <one-sentence description>

### Dimensions

**Reach:** <number of users> over <time window>
- Target segment: <description>
- Historical comparison: <similar feature adoption or flagged as hypothesis>

**Impact:** <High/Medium/Low>
- User outcome metric: <what changes for the user>
- Justification: <user feedback, observed behavior, or hypothesis>

**Confidence:** <0.5 / 0.75 / 1.0>
- Known: <what data exists>
- Assumed: <what is hypothesis-driven>

**Effort:** <number> engineering weeks
- Breakdown: <discipline breakdown if multi-team>
- Compared to: <similar feature effort or flagged as estimate>

### Calculation
RICE = (Reach × Impact × Confidence) ÷ Effort
RICE = (<Reach> × <Impact> × <Confidence>) ÷ <Effort> = **<score>**

### Ranking Context
- Rank position: <ordinal among backlog>
- Notes: <dependencies, tie-breakers, or flags>

### Confidence
<high/medium/low> — <justification based on data completeness and estimate maturity>
```
