---
name: north-star-framework
display_name: North Star Framework
class: lens
underlying_class: native
domain: product-management
source: Sean Ellis (Startup Metrics for Startups, 2010); popularized by Reforge and modern product teams
best_for:
  - Aligning cross-functional teams on a single measurable outcome
  - Identifying which input metrics drive the business outcome
  - Avoiding metric sprawl and conflicting optimization targets
one_liner: "Align the organization via a single north star metric and its input drivers."
---

# North Star Framework

## Overview
A North Star metric is the single number that best captures the core value proposition your product delivers to customers. Contributing metrics are the 2-5 measurable inputs that directly drive the North Star. The discipline is rigorous selection — most teams confuse revenue (a lagging proxy) with value, or pick metrics so complex that no one understands what to optimize. Practitioners use this when cross-functional work is fragmented (engineers building features, marketing chasing growth, support chasing retention) and the organization needs a shared target.

## Analytical Procedure

### Phase 1 — Articulate the Core Promise

1. **Write your product's customer value proposition in one sentence.** Not "we're a SaaS platform." Instead: "We help remote teams avoid back-to-back meetings" or "We reduce the cost of legal document review by 70%." If you cannot write this without jargon, the proposition is unclear.

2. **Identify what success looks like from the customer's perspective.** Not from your business perspective. Ask: "If the customer uses this product and achieves their goal, what happens?" Examples:
   - Customer goal: "I have time back in my week." Success metric: time saved per week.
   - Customer goal: "I reduce my legal costs." Success metric: dollars saved per transaction.
   - Customer goal: "I understand my data." Success metric: decisions made faster based on insights.

3. **List the jobs customers actually do with your product.** Not the features. Examples: "Scroll through updates," "Add team members," "Review a document." Write 3-6 of the most frequent.

### Phase 2 — Candidate North Star Selection

4. **For each job, propose a metric that captures success at that job.** Use these templates:
   - **Engagement**: How often does the customer do the job? (e.g., DAU, queries per user, messages sent)
   - **Value realization**: How much value does the customer extract per job? (e.g., time saved, cost reduced, quality improved)
   - **Scope**: How many of the customer's intended use cases does the product cover? (e.g., % of team invited, % of documents processed)

5. **For each candidate, test against these criteria:**
   - **Moves with revenue.** Plot the metric over 6+ months. Does it lead or lag revenue? A true North Star should move before revenue — it's predictive.
   - **Controlled by the product.** Can the product team move this metric by shipping features, or is it moved entirely by sales/marketing? North Star should be moved primarily by product.
   - **Understandable to a new hire.** Can a junior engineer, new designer, or contractor understand in 60 seconds what this metric means and why it matters? If explanation takes 5 minutes, it's too complex.
   - **Not gamed.** Can teams boost the metric without delivering real customer value? (e.g., "Daily Active Users" is gameable — bots inflate it; "Revenue per retained user" is harder to game.)
   - **Directional for 18+ months.** Does this metric remain the right target as the product evolves? Or will the business model shift it in 6 months?

### Phase 3 — Contributing Metrics Selection

6. **For your leading North Star candidate, list the levers that influence it.** For example, if North Star is "Queries per active user per month":
   - New user acquisition (more users)
   - Time to first query (activation)
   - Queries per session (engagement)
   - Monthly churn rate (retention)
   - Feature adoption (advanced features increase query frequency)

7. **Rank these levers by impact.** Run a simple regression or ask your data analyst: which 2-3 levers explain 70%+ of variance in the North Star? These become your contributing metrics. Ignore levers that are high-effort or low-signal.

8. **Define each contributing metric operationally.** Example:
   - *Activation*: % of new users who complete onboarding and submit their first query within 7 days
   - *Engagement*: Queries per monthly active user
   - *Retention*: % of users who return 4+ weeks in a row

   Each must be measurable, owned by at least one team, and updated monthly or faster.

### Phase 4 — Validation and Adoption

9. **Test the framework in decision-making.** For 2-4 weeks, bring all planned work to the North Star lens: "Does this project move one of our contributing metrics?" Discuss misalignments.

10. **Collect counterarguments.** Ask finance, support, and sales: "Is this the right target?" Listen especially to users and support — they catch metric shortcomings that data alone misses.

11. **Lock the framework.** Write down the North Star, contributing metrics, definitions, and cadence for review. Review quarterly, not monthly (constant tweaking defeats the purpose).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Customer value proposition is stated in one jargon-free sentence | Y/N |
| North Star candidate passes all five tests in Phase 2, step 5 | Y/N |
| North Star moves with revenue in historical data (6+ months of correlation) | Y/N |
| Contributing metrics are ranked by impact and add to 70%+ of North Star variance | Y/N |
| Each contributing metric is operationally defined (numerator, denominator, update cadence) | Y/N |
| At least one team other than product has reviewed and agreed to the framework | Y/N |

## Red Flags

- North Star is revenue or ARR. This is a lag metric, not a lead. If you only track revenue, you're steering by the rearview mirror.
- North Star requires manual data entry or depends on a single data source that could break. (It needs to be automated or extremely reliable.)
- Teams are still working toward different metrics. If engineering optimizes for engagement but sales optimizes for new accounts, the North Star was not adopted.
- Contributing metrics do not add up to the North Star in your data. (The causal model is wrong, or the North Star is too complex.)
- North Star contains a negation ("low churn" instead of "retention"). Positive metrics are easier to rally around.
- The North Star has never moved month-over-month. Either it's too hard to influence (not a good lever) or it's not actually being tracked correctly.

## Output Format

```
## North Star Assessment

**Customer value proposition (plain language):**
<one sentence>

**Core jobs customers do:**
1. <job>
2. <job>
3. <job>

### Phase 2 — North Star Candidates
| Candidate | Moves with revenue? | Product-controlled? | Understandable? | Hard to game? | 18+ month horizon? |
|---|---|---|---|---|---|
| <metric> | Y/N | Y/N | Y/N | Y/N | Y/N |

**Selected North Star:** <metric>

### Phase 3 — Contributing Metrics
| Metric | Definition | Owner | % Impact on North Star |
|---|---|---|---|
| <metric> | <numerator / denominator, update frequency> | <team> | <percent> |

**Total variance explained:** _%

### Phase 4 — Cross-functional validation
- Finance review: <approved / concerns>
- Support feedback: <approved / concerns>
- Sales alignment: <approved / concerns>

### Decision impact (2-4 week test)
<Description of decisions made using the framework and whether teams aligned on priority.>

### Revised framework (if needed)
<Changes made based on validation, or "No changes — framework adopted as proposed.">

### Confidence
<high/medium/low> — <justification>
```
