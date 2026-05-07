---
name: value-stream-mapping
display_name: Value Stream Mapping
class: lens
underlying_class: native
domain: operations
source: Rother & Shook (Lean Enterprise Institute, 1999); rooted in Toyota Production System
best_for:
  - Identifying bottlenecks and waste in manufacturing or service workflows
  - Visualizing handoffs and information delays between process steps
  - Prioritizing which process segments to optimize first
one_liner: "Visualize material and information flow to make waste and bottlenecks explicit."
---

# Value Stream Mapping

## Overview

Value Stream Mapping (VSM) is a lean technique that visualizes every step required to deliver a product or service—from raw material to customer hand. It captures two parallel streams: the physical flow of material and the flow of information that triggers that movement. The goal is to see waste (muda), waiting time, and rework loops that are invisible in process narratives. Practitioners use VSM when a workflow feels slow but pinpointing the bottleneck is difficult, or when they need to justify process redesign investments to stakeholders who demand a visual proof point.

## Analytical Procedure

### Phase 1 — Define the Value Stream Scope

1. **Select a single product, service, or product family.** VSM works best on a narrow scope. Do not attempt to map an entire factory or department on one diagram—choose one value stream that starts at a clear source (supplier order, customer request) and ends at a clear destination (customer receipt, invoice sent).

2. **Walk the actual process.** Do not rely on documentation or org charts. Visit the shop floor, warehouse, or service center. Observe material movement, operator actions, and wait states. Note equipment setup times, batch sizes, and inventory piles at each step. Record wall-clock time for each operation and for each waiting period between operations.

3. **Identify process boundaries.** Mark the upstream trigger (when does work start?) and the downstream end state (when is the customer satisfied?). Anything outside these boundaries is out of scope.

### Phase 2 — Map Current State

4. **Draw the production process timeline from left to right.** Each box represents a process step (a machine, a person, a batching operation). Include only steps that add value or are legally/contractually required. Document for each step:
   - Cycle time (how long one unit takes to process)
   - Setup time (if this step has changeover delays)
   - Uptime % (if equipment fails unpredictably)
   - Number of operators
   - Batch size (how many units are processed before moving to the next step)

5. **Below each process box, draw an inventory triangle.** The height of the triangle represents the quantity of work-in-progress (WIP) inventory between that step and the next. If inventory is measured in days, convert it to a count (days × daily demand).

6. **Draw the information flow above the process boxes.** Show how instructions, orders, or production schedules reach each step. Use arrows for push information (schedule broadcast to all stations) and pull signals (replenishment triggered by consumption). Note the frequency and latency of information updates (e.g., "batch order every week" or "real-time via system").

7. **Calculate total lead time.** Sum all processing times (cycle + setup). Separately, sum all waiting times (the gaps between process steps). Record both. The gap between them—waiting time divided by total lead time—is the "value ratio"; most processes run 5–30% value, meaning 70–95% is waste.

### Phase 3 — Analyze for Waste

8. **For each inventory triangle, interrogate its existence:**
   - Why is inventory here? Is it a buffer for uncertainty (demand variability, equipment failures, quality issues)? Is it a side effect of batch sizing? Is it because the upstream step produces faster than the downstream step consumes?
   - What is the cost of storing it (space, handling, obsolescence, working capital)?
   - What would happen if it was cut in half? Trace the consequence upstream and downstream.

9. **For each information gap, identify the latency cost:**
   - How long does it take for a customer order to reach the first process step?
   - How long does it take for a quality issue to propagate upstream?
   - Are orders broadcast in batches (causing delay for orders in the middle of the batch) or in real time?

10. **Spot the constraint.** The process step with the lowest uptime × (1 / cycle time) is the bottleneck. This is the gateway—optimizing anything downstream does not improve overall throughput; optimizing this step does. Mark it.

11. **List all observable waste types:**
    - **Waiting:** time between process steps (idle inventory)
    - **Motion:** unnecessary movement of people or material (distance, ergonomics)
    - **Transport:** unnecessary handling or conveying (not adding value)
    - **Overproduction:** making more than the customer needs right now
    - **Defects:** rework loops or scrap
    - **Over-processing:** steps that add no customer-visible value (excessive inspections, redundant paperwork)
    - **Underutilized talent:** operators doing repetitive work that could be prevented by system design

### Phase 4 — Design Future State

12. **Imagine the process with waste removed.** Do not redesign the equipment yet—redesign the logic. Ask:
    - What if batches were smaller (or continuous)?
    - What if information was pulled by demand instead of pushed by schedule?
    - What if the bottleneck step ran continuously and all other steps fed it exactly-in-time?
    - What if defects were prevented instead of inspected?

13. **Sketch a future-state VSM.** Use the same format as the current state but reflect your answers above. Redraw inventory triangles as they should be (usually smaller). Redraw information flow as it should be (usually faster/more frequent).

14. **Calculate the projected lead time of the future state.** Be conservative; do not assume defect-free production unless you've committed to root-cause action.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Current-state map includes cycle time, setup time, and batch size for every step | Y/N |
| Inventory levels are quantified (not just "small" or "large") | Y/N |
| Information flow is drawn and its latency documented | Y/N |
| Lead time and value ratio are calculated | Y/N |
| At least three waste categories are identified with specific examples | Y/N |
| The bottleneck step is marked and justified by math (uptime × throughput) | Y/N |
| Future-state map shows a specific intervention for each identified waste | Y/N |
| Future-state lead time is lower than current state by at least 20% | Y/N |

## Red Flags

- The current-state map is identical to the process documentation or org chart. VSM must reflect actual behavior (batch sizes, wait times, information delays), not intended behavior.
- Inventory triangles are qualitative ("a lot" or "moderate"). If you cannot measure it, you cannot reduce it.
- The bottleneck is not clearly identified or is claimed to be everywhere. Only one step is the constraint; others have slack.
- Future state is a polished version of the current state with minor efficiency tweaks. Real VSM futures challenge fundamental logic (batch size, push vs. pull, frequency of information).
- Lead time calculation excludes waiting time between steps. All time counts; "non-value time" is not ignored—it is documented and attacked.
- No traceability between identified waste and interventions in the future state. Every waste item in Phase 3 should have a corresponding change in Phase 4.

## Output Format

```
## Value Stream Map Assessment

**Product / Service:** <name and scope>
**Current lead time:** <total time from order to delivery>
**Current value ratio:** <% time spent on value-adding steps>

### Current-State Summary
| Process Step | Cycle Time | Setup Time | Batch Size | WIP | Uptime % |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | <...> |

**Information Flow:** <description of how orders/schedules reach the first step; latency>

**Total Processing Time:** <sum of cycles + setups>
**Total Waiting Time:** <sum of gaps>

### Identified Waste
1. <category>: <specific example and measured impact>
2. <category>: <specific example and measured impact>
3. ...

**Bottleneck:** <step name> — <justification by throughput math>

### Future-State Design
| Process Step | Cycle Time | Setup Time | Batch Size | WIP | Target Uptime % |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | <...> |

**Information Flow (future):** <revised cadence and mechanism>

**Projected lead time:** <X% reduction>

**Interventions per waste type:**
1. <waste type>: <specific change> → <expected outcome>
2. ...

### Implementation Priority
1. <intervention with highest impact and lowest cost>
2. ...

### Confidence
<high | medium | low> — <justification: measurement completeness, data freshness, constraint clarity, feasibility of future state>
```
