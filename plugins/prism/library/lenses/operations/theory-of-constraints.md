---
name: theory-of-constraints
display_name: Theory of Constraints
class: lens
underlying_class: native
domain: operations
source: Eliyahu Goldratt, *The Goal* (1984); extended in *Critical Chain* (1997)
best_for:
  - Identifying the real bottleneck in a system (not the loudest complaint)
  - Unlocking throughput without proportional cost increase
  - Breaking deadlock in multi-constraint environments
one_liner: "Identify the bottleneck, exploit it, subordinate the rest, and elevate the constraint."
---

# Theory of Constraints

## Overview

A system's throughput is determined by its single most restrictive resource (the constraint). Improving anything else wastes effort. The discipline is ruthlessly identifying *which one thing* actually limits output, then systematically exploiting it before subordinating everything else to feed it. Practitioners reach for this when a system is producing less than expected and the traditional response—"speed up everything"—yields diminishing returns or costs more than the gain justifies.

## Analytical Procedure

### Step 1 — Identify the Constraint

1. **Measure end-to-end system throughput.** What is the actual output rate? (units per hour, transactions per day, revenue per week—whatever the system optimizes for). Record this as the baseline.

2. **Map the value chain.** List every major process, resource, or step between input and output. Include: equipment, people, suppliers, regulatory gates, external dependencies.

3. **For each process, measure:
   - Capacity** (maximum sustainable rate under normal conditions)
   - **Current utilization** (what fraction of capacity is actually being used)
   - **Cycle time** (time spent in this process per unit)
   - **Quality loss** (percent of output rejected, reworked, or lost)

4. **Identify candidate constraints:**
   - Highest utilization rate relative to capacity (working hardest)
   - Longest queue time upstream (pile-up before it)
   - Lowest capacity relative to system demand
   - Highest quality loss rate (largest rework loop)
   Do NOT assume the constraint is the one your team complains about most.

5. **Validate the constraint.** Imagine removing one bottleneck entirely (infinite capacity, zero queue). Would system throughput increase? By how much? The constraint is the one whose removal would increase end-to-end throughput the most. (This is the "5 Focusing Steps" Step 1.)

### Step 2 — Exploit the Constraint

6. **Map all work currently flowing through the constraint.** Categorize it:
   - **Critical path** — directly produces output the system sells
   - **Support** — required but non-revenue (compliance, maintenance, meetings)
   - **Waste** — redundant, low-value, or habitual (rework, approval chains, batch delays)

7. **Remove non-critical work from the constraint.** Redirect support and waste to non-bottleneck resources, or eliminate it entirely. Do not optimize—eliminate.

8. **Optimize *only* the critical flow through the constraint.** Examples:
   - Batch jobs to reduce setup overhead
   - Pre-stage materials so the constraint never waits
   - Remove quality checks after the constraint (move them before)
   - Prioritize high-margin or high-priority units
   Do not spend money yet. Reorganize free.

9. **Measure the gain.** What is the new throughput? Quantify the improvement cost-free.

### Step 3 — Subordinate Everything Else

10. **Make every non-constraint resource a feeder** that supplies the constraint at exactly the right rate, no more and no less. This means:
    - Non-constraint processes should run *slower* than the constraint (not faster)
    - Quality gates before the constraint should be tighter
    - Scheduling should be pulled from the constraint, not pushed from inputs
    - Buffers (inventory, queue) should exist *before* the constraint, not after

11. **Establish a signal system** that tells upstream processes the constraint's status. Example: if the constraint has 2-hour queue, upstream should release work to fill a 2-hour buffer, then stop. If queue empties, release more. If queue overflows, upstream stops.

12. **Measure subordination cost.** What is the inventory, waiting time, or throughput loss in non-constraint processes? Document it as the price of respecting the constraint.

### Step 4 — Elevate (Break) the Constraint

13. **Quantify the constraint's impact on profit.** (Throughput loss × unit margin, or time-to-market cost, or customer dissatisfaction cost.)

14. **List all ways to expand the constraint's capacity.** Include: add equipment, hire people, outsource, redesign the process, relax a hidden policy, challenge an assumption about what's possible.

15. **For each option, calculate ROI:**
    - Cost to implement
    - Throughput gain (measured after exploitation and subordination are in place)
    - Payback period
    - Risk (likelihood the gain materializes, or side effects)

16. **Implement only high-ROI options.** Do NOT implement unless the gain justifies the cost. Low-ROI improvements are waste, even if they feel productive.

17. **Re-run the entire loop.** After the constraint is broken, a new constraint emerges. Return to Step 1 and identify it.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Constraint identified by capacity/utilization data, not anecdote | Y/N |
| Removal of proposed constraint would increase system throughput | Y/N |
| Non-critical work removed or redirected from constraint | Y/N |
| Exploitation improvements implemented without capital spend | Y/N |
| Non-constraint processes explicitly scheduled to feed the constraint | Y/N |
| Elevation decision is based on quantified ROI, not intuition | Y/N |
| Throughput measured before and after each step | Y/N |

## Red Flags

- The constraint is identified as "people working too slowly" or "we need better culture." This is diagnosis failure—the method wasn't applied.
- Exploitation step was skipped; improvements jump straight to buying equipment. Money spent before waste eliminated.
- Subordination created massive inventory queues upstream. This protects the constraint but destroys working capital. Red-flag sign the constraint choice was wrong.
- Multiple constraints claimed simultaneously. TOC assumes one constraint. If you see multiple, one usually dominates; if truly equal, the bottleneck is the system's policy or incentive structure, not a resource.
- Throughput measured at the constraint only, not end-to-end. A constraint producing more output that then gets rejected downstream is not a gain.
- Loop never re-runs. After the first constraint is broken, the team declares victory. In a living system, there is always a next constraint.

## Output Format

```
## Theory of Constraints Assessment

### Step 1 — Constraint Identification

**Baseline throughput:**
<measured rate, units, period>

**System map:**
| Process | Capacity | Current utilization | Queue time | Quality loss |
|---|---|---|---|---|
| <...> | <...> | <...>% | <...> | <...>% |

**Constraint candidate:**
<name>

**Validation:**
- Throughput if removed: <...>
- Gain vs. current: <...>%
- Why this over others: <justification>

### Step 2 — Exploitation

**Work flowing through constraint:**
- Critical path: <description>
- Support: <description>
- Waste: <description>

**Elimination/redirection:**
- Removed: <...>
- Redirected to: <...>
- Retained: <...>

**Optimization (non-capital):**
1. <specific change>
2. <specific change>

**New throughput:** <measured rate>
**Gain:** <% or absolute>

### Step 3 — Subordination

**Constraint signal system:**
<describe how upstream processes know the constraint's state>

**Buffer policy:**
<pre-constraint buffer size, refill rule, stop rule>

**Scheduling mechanism:**
<how demand is pulled from constraint, not pushed from input>

**Subordination cost:**
<inventory, queue time, or throughput loss in non-constraint processes>

### Step 4 — Elevation (if applicable)

**Constraint's impact on profit:**
<quantified cost of the bottleneck>

**Expansion options considered:**
| Option | Cost | Throughput gain | Payback | Risk | ROI verdict |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | Go/No-go |

**Selected option:**
<chosen lever, cost, expected gain>

**Next constraint (if applicable):**
<anticipated new bottleneck after this one is broken>

### Confidence
<high | medium | low> — <justification>
```
