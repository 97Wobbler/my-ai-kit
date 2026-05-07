---
name: goodharts-law
display_name: Goodhart's Law
class: heuristic
underlying_class: native
domain: okr
source: Charles Goodhart, "Problems of Monetary Management: The U.K. Experience" (1975); reformulated by Marilyn Strathern (1997)
best_for:
  - KPI and metric design
  - OKR goal-setting validation
  - performance incentive structure review
  - metric gaming prevention
one_liner: "When a measure becomes a target, it ceases to be a good measure."
---

# Goodhart's Law

## The Rule
When a metric is adopted as an official goal or target, people optimize for the metric itself rather than the underlying value it was meant to measure.

## When It Applies
- Code coverage mandates that drive developers to write trivial tests that pass without improving actual product safety.
- Lines of code (LOC) as a productivity KPI, causing engineers to write unnecessarily verbose, redundant code.
- Ticket-close-rate targets that incentivize developers to split work into artificially small tickets or close incomplete work early.
- Response-time SLOs that encourage teams to prioritize quick replies over correct solutions, hiding deeper problems.
- Customer acquisition cost (CAC) targets that drive sales teams to sign unprofitable customers who churn immediately.

## When It Misleads
- Applied without examining what behavior actually changes when the metric becomes public. Not all metrics produce gaming; some remain stable and valid as targets.
- Assuming the metric *itself* is the problem rather than the alignment between the metric and the underlying goal. The issue is often poor metric selection, not metric-setting as a practice.
- Treating metric corruption as inevitable rather than manageable. Well-designed metrics, clear constraints (e.g., "code coverage is necessary but not sufficient"), and transparency about trade-offs can reduce gaming.
- Ignoring that some optimization is legitimate. A code-coverage target of 80% may correctly drive adoption of testing discipline; the law applies when the tail (the metric) wags the dog (the goal).

## Common Misuse
Organizations adopt Goodhart's Law as an excuse to avoid metrics altogether. They retreat to vague goals ("build great products") because measurable goals invite gaming. This inverts the insight: the law is not an argument *against* measurement, but a call for better measurement. The real misuse is setting the wrong metric or failing to pair it with complementary signals. For example, using lines-of-code without code-review feedback, or response time without accuracy checks.

Another pattern: teams acknowledge the law but continue operating as though it doesn't apply to *their* metrics, claiming their targets are "incentive-proof." This overconfidence leads to slow, creeping optimization that only becomes visible after months of distorted behavior.

## How Agents Use It

- **Embedded**: Within KPI-tree and OKR-design lenses, Goodhart's Law is a validation gate. After selecting candidate metrics, the agent asks: "What behavior would an engineer exhibit if they optimized purely for this number?" and flags metrics where the answer suggests gaming.
- **Embedded**: When evaluating DORA metrics or SLO recommendations, the agent notes which metrics are direct (e.g., incident severity) versus proxy measures (e.g., mean-time-to-resolution), and assigns lower confidence to targets based on proxies alone.
- **Sanity-gate**: Before recommending any new performance metric, bonus structure, or team scorecard, the agent runs a checklist: (1) Is the metric a direct measure or a proxy? (2) What perverse incentive emerges if someone optimizes purely for it? (3) What complementary metric would signal if the primary metric was being gamed? (4) Is there transparency about trade-offs?

Related principle: Campbell's Law (measurements used for decision-making are more likely to be manipulated) and the distinction between *leading* indicators (effort, velocity) and *lagging* indicators (revenue, user retention) — gaming is most dangerous when organizations target leading indicators in isolation.
