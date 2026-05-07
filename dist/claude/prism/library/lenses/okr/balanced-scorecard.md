---
name: balanced-scorecard
display_name: Balanced Scorecard
class: lens
underlying_class: native
domain: okr
source: Robert Kaplan and David Norton, 1992
best_for:
  - Translating strategy into measurable outcomes across organizational silos
  - Detecting performance gaps between financial results and operational health
  - Aligning execution to strategy through multi-perspective metrics
one_liner: "Structure strategy across four KPI perspectives — financial, customer, process, learning — for balanced tracking."
---

# Balanced Scorecard

## Overview
The Balanced Scorecard translates organizational strategy into four distinct perspectives — Financial, Customer, Internal Process, and Learning & Growth — each populated with concrete measures and targets. Rather than relying on lagging financial metrics alone, it captures leading indicators that predict financial performance. Practitioners use it to ensure that operational improvements (process efficiency, employee capability, customer satisfaction) actually drive the financial outcomes they're supposed to drive, and to detect when one perspective is improving at the expense of others.

## Analytical Procedure

### Phase 1 — Articulate Strategy

1. **State the organization's core strategy in one sentence.** Include: what customer need you serve, how you differentiate, and what financial outcome you aim for. Examples: "Become the lowest-cost provider of cloud infrastructure to startups" or "Deliver premium analytics software through enterprise relationships."

2. **Map the strategic cause-and-effect chain.** Draw or list how success in Learning & Growth drives Internal Process improvement, which improves Customer outcomes, which drives Financial results. This chain should have 4-6 links. If you cannot articulate the chain, the strategy is not yet clear enough for the scorecard.

### Phase 2 — Define Metrics for Each Perspective

3. **Financial perspective.** Define 2-4 outcome metrics aligned to strategy. These are usually backward-looking (revenue growth, operating margin, ROI) but must connect directly to the strategy. Bad: "Revenue." Good: "Revenue from customers with 2+ product adoptions" (measures depth of adoption, which is your differentiation).

4. **Customer perspective.** Define 2-4 measures of how customers perceive you relative to your value proposition. Common categories:
   - **Satisfaction/Loyalty:** NPS, retention rate, repeat purchase rate
   - **Acquisition:** market share in target segment, win rate vs. named competitors
   - **Delivery:** delivery time, defect rate, responsiveness
   - **Relationship:** share of wallet, upsell success rate
   
   Pick measures that directly support your strategy. If your strategy is "premium," measure perceived quality and willingness to pay, not price or volume.

5. **Internal Process perspective.** Identify the 3-5 critical processes that must excel for the strategy to succeed. For each, define a measure. Examples:
   - If strategy is "innovation," measure: R&D cycle time, time-to-market, patent velocity
   - If strategy is "low cost," measure: manufacturing yield, inventory turns, labor productivity
   - If strategy is "customer intimacy," measure: response time, customization cycle, customer-facing staff retention
   
   Avoid generic operational metrics. Focus on processes that directly enable the customer or financial outcomes you defined above.

6. **Learning & Growth perspective.** Define measures of capability, motivation, and culture that underpin the internal processes. Common categories:
   - **Capability:** training completion, skill certifications, R&D headcount as % of total
   - **Motivation:** employee engagement score, voluntary turnover rate, promotion-from-within %
   - **Culture:** safety incident rate, process compliance rate, innovation ideas submitted per employee
   
   Each should predict improvement in a specific Internal Process metric.

### Phase 3 — Set Targets and Baselines

7. **Establish baseline values** for each metric using current state or historical data. Document the date and method (survey, system log, external benchmark, etc.).

8. **Set targets** for 1-year and 3-year horizons. Targets should be:
   - **Challenging but achievable** — not incremental, not fantasy
   - **Specific** — "improve by 10%" not "improve significantly"
   - **Aligned within the chain** — a target in Learning & Growth should predict a specific movement in Internal Process, etc.

9. **Identify key initiatives** (projects, programs, investments) that will close the gap between baseline and target for each metric. One metric may have multiple initiatives; one initiative may move multiple metrics.

### Phase 4 — Validation and Iteration

10. **Stress-test the cause-and-effect chain.** For each link (e.g., "employee engagement → process efficiency → customer satisfaction → revenue"), ask: Is this causal or only correlated? Do we have evidence? If you cannot defend a link, either add evidence, weaken the claim, or remove the metric.

11. **Check for conflicts.** Do any two metrics pull in opposite directions? Example: "Maximize process automation" (Internal Process) vs. "Maximize custom responsiveness" (Customer). These are not always contradictory — they may operate in different customer segments — but they must be explicitly reconciled in the scorecard narrative.

12. **Validate with leadership and the field.** Present the scorecard to the team that will execute it. Can they explain why each metric matters? Do they see how their work connects? Revise until the chain is credible to them.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Strategy statement is one sentence and includes differentiation | Y/N |
| Cause-and-effect chain from Learning & Growth to Financial is drawn and has 4-6 links | Y/N |
| Each perspective has 2-4 metrics (8-16 total) | Y/N |
| Each metric is specific and measurable (not vague like "improve quality") | Y/N |
| Baseline and target are documented for each metric | Y/N |
| At least one key initiative is mapped to each metric | Y/N |
| At least one cause-and-effect link has been stress-tested for causality | Y/N |
| Conflicting metrics have been identified and explicitly reconciled | Y/N |

## Red Flags

- The Financial perspective contains only traditional metrics (revenue, profit margin) with no tie to strategy. This is a traditional budget, not a scorecard.
- Multiple metrics in the same perspective measure the same underlying thing (e.g., both "market share" and "win rate"). Consolidate.
- The Learning & Growth or Internal Process metrics do not visibly predict Customer or Financial metrics. The causal chain is broken.
- Targets are set by tradition ("increase by 5%") rather than by gap analysis (current 45%, target 60%, therefore increase by 15%).
- No initiatives are linked to any metric. The scorecard describes where you want to be but not how you'll get there.
- The scorecard is one-size-fits-all across all business units. Most organizations require local variants — a retail location's Internal Process metrics differ from manufacturing's.
- Metrics are updated once a year. If updated less frequently than quarterly, there is no opportunity to course-correct.

## Output Format

```
## Balanced Scorecard Assessment

**Organizational Strategy:**
<one sentence with customer need, differentiation, financial outcome>

### Cause-and-Effect Chain
<narrative or diagram showing Learning & Growth → Internal Process → Customer → Financial>

### Perspective Metrics and Baselines

#### Financial
| Metric | Current | Target (1yr) | Target (3yr) | Initiative |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

#### Customer
| Metric | Current | Target (1yr) | Target (3yr) | Initiative |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

#### Internal Process
| Metric | Current | Target (1yr) | Target (3yr) | Initiative |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

#### Learning & Growth
| Metric | Current | Target (1yr) | Target (3yr) | Initiative |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

### Causal Link Validation
| Link | Causal? | Evidence / Notes |
|---|---|---|
| <L&G metric> → <Process metric> | Y/N | <...> |
| <Process metric> → <Customer metric> | Y/N | <...> |
| <Customer metric> → <Financial metric> | Y/N | <...> |

### Conflict Resolution
<Identify any metrics that work against each other and explain how they will be balanced.>

### Confidence
<high | medium | low> — <justification. High: strategy is clear, all links are evidence-based, leadership agrees. Medium: chain has 1-2 unvalidated links or metrics are still proxies. Low: strategy is fuzzy, causal links are speculative, no field validation yet.>
```
