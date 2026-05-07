---
name: kpi-tree
display_name: KPI Tree
class: lens
underlying_class: native
domain: okr
source: origin uncertain; common in strategy and OKR practice (Doerr, 2018)
best_for:
  - Decomposing a top-level business goal into measurable, cascading key performance indicators
  - Identifying which metrics actually move the needle versus vanity metrics
  - Clarifying ownership and dependencies between teams through metric alignment
one_liner: "Decompose the top-level goal into a measurable KPI hierarchy to secure cross-team alignment."
---

# KPI Tree

## Overview
A KPI Tree decomposes a single top-level business outcome into a branching hierarchy of measurable sub-outcomes, each with clear owners and dependencies. Instead of assigning arbitrary metrics to teams, the tree derives metrics from first principles — what must be true at each level for the level above it to succeed. Practitioners use this lens when a strategy exists but teams disagree on what to measure, or when metrics exist but no one can explain why they matter to the business.

## Analytical Procedure

### Phase 1 — Define the Root

1. **State the top-level outcome in one sentence.** Use a business outcome, not a tactic. 
   - Bad: "Increase our ad spend efficiency."
   - Good: "Grow sustainable revenue per user by 25% in 2025 without increasing churn."

2. **Identify the time horizon and success threshold.** When does this outcome matter? By when must it be achieved? What percentage improvement counts as success?

3. **List all ways this outcome could theoretically fail.** These become your decomposition targets. Write 4–6 failure modes. Example: "Revenue per user could grow if we increase revenue AND if we do NOT increase churn" — that's a decomposition point.

### Phase 2 — Decompose One Level

4. **For the root outcome, write the equation or logic that connects sub-outcomes to it.** Be explicit. Do not use "and related factors." Example:
   - Revenue per user = (Average Order Value) × (Orders per User per Year) + (Subscription ARPU)
   - Sustainable Revenue = (Revenue) × (1 - Churn Rate)

5. **For each term in the equation, ask: "Can we influence this directly, or must we go deeper?"** If you or another team can directly move the metric through a clear, single action (e.g., "raise prices" for AOV), mark it a **leaf KPI** and assign an owner. If not, decompose further.

6. **Create sub-KPIs for the terms that require decomposition.** Repeat step 4 for each sub-KPI.
   - Example: If "Orders per User per Year" requires decomposition, break it into (Active Users) × (Conversion Rate) × (Repeat Purchase Rate).

7. **Check for double-counting.** Ensure no metric appears in two different branches. If a sub-outcome affects multiple parents, draw a line between them (not yet a separate branch — just document the dependency).

### Phase 3 — Assign Ownership and Test Clarity

8. **For each leaf KPI, assign a single owner and a clear lever.** Example: "Product Team owns Conversion Rate. Lever: checkout flow optimization." Not "Product Team owns Growth" — too vague. Not "five teams jointly own Conversion Rate" — responsibility diffusion is failure.

9. **For each non-leaf KPI (intermediate node), identify the owner responsible for the sum.** This is usually a manager or a team lead, not an individual contributor. Their job is to monitor whether the sub-KPIs below them cascade correctly.

10. **Walk the tree backwards from leaf to root.** For each leaf, trace upwards: "If we hit this leaf target, will the parent target be hit?" If the answer is uncertain, the decomposition has a logical gap. Stop and fix it.

11. **Mark each edge with a confidence ratio: current value → target value.** Example: "Conversion Rate: 2.1% → 3.5%." If the ratio seems unrealistic (e.g., 5% → 95% in one year), flag it. Unrealistic leaves indicate an ownership or lever problem.

### Phase 4 — Detect Orphaned Metrics and Hedges

12. **List every metric currently tracked by the organization.** Then walk the KPI Tree. For each tracked metric, mark it as either:
    - **On the tree** — contributes to a leaf
    - **Off the tree** — exists but does not roll up to the root outcome
    - **Hedge** — measured but not directly owned (e.g., "we track Net Promoter Score but no one owns it")

13. **For each "off the tree" metric, ask: "If this metric moves in the wrong direction, does it block the root outcome?"** If yes, it belongs on the tree — add it. If no, consider stopping measurement or moving it to a separate monitoring dashboard.

14. **For each hedge, assign an explicit owner and decision rule.** Example: "Engineering owns System Uptime (hedge). If uptime < 99.5% for two weeks, we pause feature development."

## Evaluation Criteria

| Check | Pass |
|---|---|
| Root outcome is a business outcome (not a tactic), time-bound, and success-threshold stated | Y/N |
| Every non-leaf node has a clear mathematical or logical relationship to its children | Y/N |
| Every leaf KPI has a single assigned owner and a named lever | Y/N |
| Tree is walked backward once; no logical gaps detected | Y/N |
| Every current tracked metric is explicitly categorized (on tree / off tree / hedge) | Y/N |
| Ownership of intermediate nodes is assigned to a person or role, not a committee | Y/N |
| At least one leaf target is stress-tested for realism | Y/N |

## Red Flags

- The root outcome is aspirational but unmeasurable ("become a market leader"). If you cannot tell whether you succeeded, the tree is structural but not actionable.
- More than two levels deep without hitting a leaf. KPI Trees that exceed 4 levels often hide poor decomposition — intermediate nodes are often just restatements of parents.
- Leaf KPIs are owned by committees or vague roles ("the Growth team"). Shared ownership is accountability diffusion.
- A metric appears in multiple branches. Either it truly affects multiple outcomes (draw a dependency arrow, don't duplicate) or the decomposition is ambiguous.
- An "off the tree" metric is tracked by many teams and affects decisions daily (e.g., latency, error rate). This is a sign the root outcome was too narrow and doesn't reflect the business.
- The tree exists but teams are not aligned on target values. The tree is a document, not a tool.
- A leaf KPI's current-to-target ratio is implausible given the lever (e.g., "Product Team owns Churn, lever is UI redesign, target is 50% reduction in one quarter"). The lever doesn't match the ambition.

## Output Format

```
## KPI Tree Assessment

**Root Outcome:**
<statement with time horizon and success threshold>

**Failure Modes:**
1. <...>
2. <...>
(4–6 modes)

### Level 1 Decomposition
<Mathematical or logical equation connecting root to sub-outcomes>

| Sub-KPI | Owner | Leaf? | Lever | Current | Target |
|---|---|---|---|---|---|
| <...> | <...> | Y/N | <...> | <...> | <...> |

### Level 2+ Decomposition
(Repeat for each non-leaf KPI requiring further decomposition)

### Dependency Graph
<List edges between non-parent-child nodes, if any>

### Ownership Audit
| Node Type | Owner | Confidence |
|---|---|---|
| Root outcome | <...> | <...> |
| Intermediate node: <...> | <...> | <...> |
| Leaf: <...> | <...> | <...> |

### Metric Alignment
| Metric | Status | Notes |
|---|---|---|
| <...> | On tree / Off tree / Hedge | <...> |

### Backward Walk (Spot Check)
- Leaf: <leaf KPI> → Parent: <parent KPI>. Logic holds? <Y/N>
- (Repeat for 2–3 critical paths)

### Issues Found
1. <issue and remediation>
2. ...

### Confidence
<high/medium/low> — <justification. Note: high confidence requires ownership assigned to all leaves, all target ratios defensible, and backward walk with no gaps.>
```
