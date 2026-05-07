---
name: lean-waste
display_name: Lean Waste (TIMWOODS)
class: heuristic
underlying_class: native
domain: operations
source: Taiichi Ohno, Toyota Production System, 1988
best_for:
  - process waste audits
  - value stream mapping
  - operational improvement prioritization
one_liner: "Find and eliminate the eight wastes and efficiency follows."
---

# Lean Waste (TIMWOODS)

## The Rule

In any process, eight categories of waste (Transport, Inventory, Motion, Waiting, Overproduction, Overprocessing, Defects, Skills underutilization) account for most throughput loss; eliminating them compounds efficiency faster than optimizing what remains.

## When It Applies

- Bottleneck diagnosis in manufacturing, logistics, or software delivery pipelines.
- Process redesign where current state is unmeasured and feels inefficient without clear cause.
- Cost reduction efforts where headcount or raw input is not the lever.
- Comparing two operational designs to decide which removes more waste per unit of effort.
- Incident post-mortems where systemic friction patterns emerge.

## When It Misleads

- When the constraint is not process waste but hard resource scarcity (you need more machines, more people, more time) — removing waste from an undersized system does not scale output.
- In domains where waste categories are not independent: removing transport waste may force inventory growth, or reducing defects may require overprocessing. The heuristic assumes orthogonal wastes; it misleads when they trade off.
- When "waste" is smuggled into the definition of value. What looks like overprocessing (extra testing, documentation, redundancy) may be the actual product (safety margins, regulatory compliance, customer expectations). TIMWOODS assumes waste and value are separable; they often are not.
- In highly constrained or regulated environments where process steps exist to satisfy external demands, not internal choice. Removing them is not an efficiency win — it is non-compliance.

## Common Misuse

The heuristic is often applied as a scanning exercise without discipline: spot eight categories, declare all eight present, and call the work done. Real TIMWOODS analysis requires measurement — quantifying the waste, tracing its source, and predicting the impact of removal. Without measurement, TIMWOODS becomes a vocabulary for vague complaint, not diagnosis.

Another misuse is treating the eight categories as exhaustive. Waste outside TIMWOODS (rework loops, unclear ownership, poor incentives) is real but invisible to the framework. Agents often stop after naming the eight, missing compound or structural wastes that are not reducible to a single category.

## How Agents Use It

- **Embedded**: in process-mapping lenses, as the checklist for labeling each step. At the "find and classify waste" step, walk the eight categories explicitly and mark which apply; use that classification to weight improvement candidates.
- **Sanity-gate**: on each operational improvement recommendation, force the agent to state which of the eight wastes it addresses and quantify (or at minimum bound) the expected reduction. If a recommendation does not map to one of the eight, it is a signal to re-examine whether the recommendation is truly about efficiency or about preference.
