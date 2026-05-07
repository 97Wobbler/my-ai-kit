---
name: opportunity-scoring
display_name: Opportunity Scoring (Ulwick ODI)
class: lens
underlying_class: native
domain: product-management
source: Anthony Ulwick, Outcome-Driven Innovation, 2005
best_for:
  - Prioritizing features or product improvements by impact potential
  - Identifying underserved customer needs
  - Avoiding feature bloat by scoring ROI
one_liner: "Systematically surface and score opportunities that customers rate important but unsatisfied."
---

# Opportunity Scoring (Ulwick ODI)

## Overview

Opportunity Scoring identifies product opportunities by measuring the gap between how *important* a customer outcome is and how *satisfied* customers currently are with it. High importance + low satisfaction = high opportunity. The framework operates on structured customer outcome data (not solutions, not features) and produces a prioritized list of development targets. Practitioners use it to escape feature-request bias and anchor prioritization in genuine customer pain rather than stakeholder intuition.

## Analytical Procedure

### Phase 1 — Collect Customer Outcomes

1. **Conduct outcome-focused customer interviews.** Interview 20–40 customers in your target segment. Ask: "When you [use/buy/interact with] our product for [job to be done], what outcomes do you want to achieve?" Record outcomes, not solutions. Do not ask "What features do you want?"
   - Bad outcome language: "Add dark mode," "Faster loading," "Better UI"
   - Good outcome language: "Reduce time spent searching for documents," "Minimize distractions while working," "Understand which features I'm using"

2. **Consolidate outcomes into a master list.** Group similar outcomes spoken by different customers. Aim for 50–100 outcomes covering the core job and its context. Each outcome is one sentence, in the form: "Minimize/Maximize [metric/attribute] when [context]."

3. **Validate the list with customers.** Share the consolidated list with 10–15 different customers. Ask: "Are we missing anything?" and "Would you reword any of these?" Revise based on feedback. This ensures the list is representative, not cherry-picked.

### Phase 2 — Measure Importance and Satisfaction

4. **Survey a representative sample** on two scales: importance and satisfaction. Aim for 100–300 respondents.
   - **Importance scale:** "How important is it to you that [outcome] when [context]?" (1–10, where 1 = not important, 10 = extremely important)
   - **Satisfaction scale:** "How satisfied are you with your current ability to [outcome]?" (1–10, where 1 = not satisfied, 10 = very satisfied)
   Each respondent rates all 50–100 outcomes.

5. **Calculate mean importance and mean satisfaction for each outcome.** Outcomes with high variance (wide spread of responses) indicate segmentation opportunities; set those aside initially and note them.

### Phase 3 — Score Opportunity and Rank

6. **Calculate the Opportunity Score for each outcome** using the formula:
   ```
   Opportunity Score = Importance × (10 − Satisfaction)
   ```
   This multiplies importance by the satisfaction gap (how far below "fully satisfied" the outcome is). Higher score = bigger opportunity.

7. **Rank outcomes by Opportunity Score, descending.** The top 10–15 outcomes are your primary development targets.

8. **Segment by importance level** (optional but recommended):
   - **High importance (8–10) + Low satisfaction (1–4):** Urgent. Customers need this badly and don't have it. Highest risk if ignored.
   - **High importance (8–10) + Medium satisfaction (5–6):** Important gaps. Room for meaningful improvement.
   - **Medium importance (5–7) + Low satisfaction (1–4):** Niche or secondary opportunities. May be high-value in specific segments.

9. **Sanity-check the top 5 outcomes.** For each, ask: "Is this achievable for us? Does it align with our product vision? Can we differentiate on this?" If the answer to any is "no," note it and move to the next outcome.

### Phase 4 — Translate to Features

10. **For each high-opportunity outcome, brainstorm solutions.** Do NOT let one solution block others. Example: the outcome "Minimize time to locate the right file" might be solved by search, tags, folders, recent-files lists, or AI recommendations — or a combination.

11. **Estimate effort and business impact** for top solutions. Opportunity Score tells you *where* to focus, not *how* to build. Effort estimation and market impact are separate inputs.

12. **Document the outcome → solution linkage.** In your roadmap, always reference the underlying outcome. This prevents solution-level debates and grounds decisions in customer data.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Outcomes are phrased as customer goals, not feature requests | Y/N |
| Importance and satisfaction were measured from ≥100 respondents | Y/N |
| Each outcome has a calculated Opportunity Score | Y/N |
| Top 10 outcomes show importance ≥ 7 or satisfaction gap ≥ 5 | Y/N |
| At least one segment (high importance + low satisfaction) is non-empty | Y/N |
| Top outcomes have been sanity-checked against product strategy | Y/N |

## Red Flags

- All outcomes cluster around mid-range importance (5–7). Either the outcome list is too generic, the segment is wrong, or the respondents weren't engaged. Go back to interviewing.
- Satisfaction scores are uniformly high (7–9). Customers may be biased toward their current tool, or the outcomes are too vague. Reword outcomes to be more specific ("minimize time searching" vs. "easy to find things").
- Top-ranked opportunities are all feature requests that competitors have. You've validated the feature-request bias rather than escaped it. Check your interview methodology — are you leading customers toward existing solutions?
- Opportunity Scores are driven entirely by low satisfaction, with importance flat across all outcomes. The satisfaction scale is not discriminating — respondents may have anchored to current product experience rather than ideal state. Rescale or re-interview.
- No outcomes in the "high importance + low satisfaction" quadrant. This segment is your primary target; if it's empty, expand the outcome list or interview a different customer segment.

## Output Format

```
## Opportunity Scoring Analysis

**Segment / Job:**
<target customer segment and job to be done>

**Respondent count:** <number>

### Consolidated Outcome List
| Rank | Outcome | Importance (1–10) | Satisfaction (1–10) | Gap (10−Sat) | Opportunity Score | Segment |
|---|---|---|---|---|---|---|
| 1 | <...> | <...> | <...> | <...> | <...> | High Imp / Low Sat |
| 2 | <...> | <...> | <...> | <...> | <...> | <...> |

### Top Opportunities (Opportunity Score ≥ threshold)
1. **<Outcome>** | Score: <X> | Importance: <I> | Satisfaction: <S>
   - Segment: <High/Medium/Low importance + Low/Medium/High satisfaction>
   - Sanity check: Achievable? Aligned with vision? Differentiator?
   
2. ...

### Segmentation Summary
- High Importance (8–10) + Low Satisfaction (1–4): <count> outcomes | Avg score: <X>
- High Importance (8–10) + Medium Satisfaction (5–6): <count> outcomes | Avg score: <X>
- Medium Importance (5–7) + Low Satisfaction (1–4): <count> outcomes | Avg score: <X>

### Recommended Development Priorities
1. <Outcome + proposed solution directions>
2. ...

### Confidence
<high/medium/low> — <justification based on respondent diversity, outcome coverage, and segment clarity>
```
