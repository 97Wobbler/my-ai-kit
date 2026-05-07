---
name: wsjf
display_name: WSJF (Weighted Shortest Job First)
class: lens
underlying_class: native
domain: agile
source: Dean Leffingwell (SAFe 4.0+, 2014)
best_for:
  - Prioritizing a backlog of features or initiatives when multiple trade-offs exist
  - Comparing work items across teams to identify the highest-value sequence
  - Breaking ties between similar-sized features competing for limited capacity
one_liner: "Weighted Shortest Job First — prioritize by Cost of Delay divided by job size."
---

# WSJF (Weighted Shortest Job First)

## Overview

WSJF ranks work items by dividing their Cost of Delay (business value lost per unit time) by their Job Size (effort to deliver). The formula surfaces items where the organization pays the highest penalty per day of delay relative to the work required to finish them. Practitioners use it to sequence backlogs when neither "do the highest-value item first" nor "do the quickest item first" dominates — most real portfolios require balancing both. The discipline is accurate estimation of both numerator and denominator, and honest conversation about what "delay" actually costs.

## Analytical Procedure

### Phase 1 — Estimate Cost of Delay (CoD)

1. **For each work item, identify what breaks if delivery is delayed by one sprint.** Write concretely:
   - Does a customer leave? How many? What is their annual revenue?
   - Does a competitor gain ground? What market share is at risk?
   - Does a regulatory deadline slip? What is the penalty?
   - Does an internal initiative stall? How many dependent teams are blocked?
   - Does a user pain point persist? How much efficiency is lost per user per day?

2. **Assign the Cost of Delay to one or more of four categories.** SAFe uses: User-Business Value, Time Criticality, Risk Reduction, Opportunity Enablement. For each category, score the item on a scale (1–20 is common; use 0–10 if resources are limited). If an item spans multiple categories, score each separately.
   - **User-Business Value:** Direct revenue, cost savings, or user satisfaction gained by shipping.
   - **Time Criticality:** Penalty per day of delay (regulatory, competitive, or time-boxed customer commitments).
   - **Risk Reduction:** Unblocks other work, eliminates technical debt, or mitigates known threats.
   - **Opportunity Enablement:** Enables future revenue streams or strategic moves that are not yet in revenue.

3. **Calculate total CoD.** If using SAFe's four-category model, CoD = (User-Business Value + Time Criticality + Risk Reduction + Opportunity Enablement) × some weight constant (usually 1 for simplicity). If using custom categories, sum them. Do not invent scores — the score should reflect conversation with the business, not guesswork.

### Phase 2 — Estimate Job Size

4. **Define Job Size as total effort in your team's native unit.** This is typically story points, person-weeks, or lines of code. Consistency matters more than absolute accuracy — all items must be estimated in the same scale.

5. **Include all work to make the item shippable.** Design, development, testing, documentation, deployment, and monitoring. Do not exclude "soft" work. If design takes 3 weeks and code takes 4, the Job Size is 7 weeks, not 4.

6. **If the item is large (>2 sprints of effort), break it down.** WSJF works best on items that fit in a sprint or two. For large epics, estimate the Job Size of the smallest shippable slice first, prioritize that, then re-estimate the remainder after that slice is complete.

### Phase 3 — Calculate WSJF Score and Rank

7. **For each item, calculate WSJF = CoD ÷ Job Size.** Use the same units consistently. If CoD is in "business-impact units" (1–100) and Job Size is in story points, the result is dimensionless but comparable across items.

8. **Rank items by WSJF score in descending order.** Highest WSJF = highest priority. If two items have WSJF within 10% of each other, they are tied — use a tiebreaker (see Red Flags).

9. **Sanity-check the ranking against team intuition.** Walk through the top 5 items. If the ranking feels backwards (e.g., a tiny bug that almost no one cares about ranks higher than a major feature), one of these is true:
   - The CoD estimates are wrong (re-discuss with business stakeholders).
   - The Job Size estimates are wrong (re-estimate with the team).
   - WSJF is not the right framework for this decision (it may require strategic override, see Red Flags).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Every work item has a CoD score from at least one category (not guessed) | Y/N |
| Every work item has a Job Size estimate that includes all shippable work | Y/N |
| Job Size scale is consistent across all items (all in same units) | Y/N |
| WSJF = CoD ÷ Job Size for each item and is calculated correctly | Y/N |
| Top-ranked items make intuitive sense to the business and team | Y/N |
| Tiebreaker for items within 10% WSJF is documented | Y/N |

## Red Flags

- CoD scores are all identical or clustered (e.g., everyone scores 10–12). This signals that the estimation conversation was shallow or the scoring scale is not discriminating. Run a second pass, asking: "If you had to rank these by urgency alone, what is the order?" Use that to differentiate.
- Job Size estimates are suspiciously round (all 5, 8, 13). This is a common planning bias. Ask the team to estimate in at least three sizes: 2–3 points (small), 5–8 points (medium), and 13+ points (large). Force distinction.
- A tiny item (Job Size = 1) with moderate CoD (say, 30) ranks above a large item (Job Size = 20) with high CoD (say, 150). WSJF = 30 vs. 7.5. This is working as designed, but if the large item is critical, it signals that CoD was underestimated. Revisit.
- The ranking violates a known strategic priority (e.g., "security is non-negotiable" but a security epic ranks 8th). Do not blindly follow WSJF. Instead, document the override and adjust CoD for future prioritization rounds.
- No tiebreaker is defined. When two items have nearly equal WSJF, WSJF cannot break the tie; you need a secondary criterion (risk, learning value, dependencies, or alignment with quarterly OKRs).
- Job Size includes "nice to have" work like "refactor after shipping." Shippable does not mean perfect. Be honest about the minimal viable scope.

## Output Format

```
## WSJF Prioritization

**Date:** <YYYY-MM-DD>
**Team/Portfolio:** <name>
**Prioritization period:** <e.g., Q2 2026>

### Work Items and Scores

| Item ID | Title | User-Bus Value | Time Crit | Risk Red | Opp Enable | **Total CoD** | **Job Size (pts)** | **WSJF** | Rank |
|---|---|---|---|---|---|---|---|---|---|
| EPIC-1 | <...> | 8 | 6 | 3 | 2 | 19 | 5 | **3.8** | 1 |
| EPIC-2 | <...> | 5 | 4 | 8 | 1 | 18 | 13 | **1.4** | 4 |

### Notes on CoD Estimation
- **User-Business Value:** <how this was assessed; e.g., "revenue impact from customer research">
- **Time Criticality:** <what breaks if delayed; e.g., "competitive window closes in 6 weeks">
- **Risk Reduction:** <what becomes unblocked; e.g., "enables payment system refactor, reducing incidents">
- **Opportunity Enablement:** <future value unlocked; e.g., "platform for B2B upsell">

### Job Size Notes
- <Any estimation anomalies, e.g., "EPIC-3 includes unknown design scope; team estimates 13±5 pts. Will re-estimate after design spike.">

### Tiebreaker (items within 10% WSJF)
- <e.g., "Items ranked 5–6 (WSJF 1.1–1.2) broken by dependency order: EPIC-5 unblocks EPIC-6, so EPIC-5 moves first.">

### Sanity Check
- **Alignment with strategy:** <Any items removed or re-ranked due to strategic override? Document reason.>
- **Team comfort with ranking:** <Did the top 5 pass team intuition check? Any rework needed?>

### Confidence
<high | medium | low> — <Justification. E.g., "high — CoD was estimated via stakeholder interview and validated against last quarter's actuals. Job Size estimates are from experienced team. Ranking passed sanity check." OR "medium — Time Criticality scores are estimates pending customer confirmation of regulatory deadline.">
```
