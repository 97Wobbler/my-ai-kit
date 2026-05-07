---
name: value-chain-analysis
display_name: Value Chain Analysis (Porter)
class: lens
underlying_class: native
domain: strategy
source: Michael E. Porter, Competitive Advantage (1985)
best_for:
  - Identifying where margin is created or destroyed across a business
  - Finding cost reduction and differentiation opportunities in specific activities
  - Understanding competitive advantage through operational efficiency
one_liner: "Trace value added and cost per activity to find the source of competitive advantage."
---

# Value Chain Analysis (Porter)

## Overview

The value chain disaggregates a firm into its strategically relevant activities to understand behavior, costs, and the sources of differentiation. Instead of treating a business as a black box, you decompose it into primary activities (inbound logistics, operations, outbound logistics, marketing & sales, service) and support activities (procurement, technology development, human resource management, firm infrastructure), then trace margin contribution and cost driver dependencies across the chain. Practitioners use this when they suspect competitive advantage lies not in a single capability but in how activities connect, or when cost reduction efforts target the wrong levers.

## Analytical Procedure

### Phase 1 — Map the Value Chain

1. **Define the business scope.** State the primary product or service, the customer segment, and the geographic market. Example: "Premium athletic footwear sold directly to North American consumers."

2. **Identify primary activities.** For your business, list the major sequential steps from raw input to delivered product:
   - **Inbound Logistics:** procurement, warehousing, materials handling of inputs
   - **Operations:** manufacturing, assembly, quality control, packaging
   - **Outbound Logistics:** storage, order fulfillment, shipping, delivery
   - **Marketing & Sales:** advertising, sales force, pricing, channel management, brand
   - **Service:** installation, repair, warranties, customer support
   
   Adapt the names to your industry. For a software company, "Operations" might be "Product Development & Deployment." For a consulting firm, "Inbound Logistics" might not exist. List only activities that apply.

3. **Identify support activities.** These cut across the primary chain:
   - **Procurement:** sourcing of materials, equipment, and services (other than labor)
   - **Technology Development:** R&D, process innovation, equipment design
   - **Human Resource Management:** recruitment, training, compensation, retention
   - **Firm Infrastructure:** finance, legal, government relations, quality assurance, planning
   
   Again, adapt to your context. Note where support activities serve multiple primary activities or specific ones.

4. **Draw a simple diagram.** Horizontally list primary activities left to right. Below, show support activities spanning or feeding into them. This is your value chain map.

### Phase 2 — Trace Cost Drivers and Margin Contribution

5. **For each primary activity, estimate the percentage of total operating cost.** Interview operations, finance, or cost accounting. If exact figures are unavailable, make a reasonable estimate. Example:
   - Inbound Logistics: 8%
   - Operations: 35%
   - Outbound Logistics: 12%
   - Marketing & Sales: 28%
   - Service: 5%
   - Support activities: 12%

6. **For each activity, identify 2–4 cost drivers.** Cost drivers are factors that cause costs to vary. Examples:
   - **Inbound Logistics:** supplier lead times, batch size, inventory turns, transportation distance
   - **Operations:** production volume, batch size, labor skill level, process automation, capacity utilization
   - **Outbound Logistics:** order size, shipping distance, delivery speed, packaging complexity
   - **Marketing & Sales:** sales channel (direct vs. retail), brand investment, promotional intensity, customer acquisition cost
   - **Service:** warranty scope, customer density, technical skill required, response time SLA

7. **Estimate the margin contribution of each activity.** Margin = revenue minus cost for that activity. If activity cost is 12% of revenue, and you sell at a 25% gross margin (gross profit / revenue), then the activity consumes half of available margin. Document your logic.

### Phase 3 — Identify Linkages and Dependencies

8. **Map horizontal linkages between activities.** Where does one activity's output feed into another's input, and how does performance in one affect cost or quality in another?
   - Example: Poor inbound logistics quality (damaged materials) increases operations cost (rework, scrap).
   - Example: Operations throughput and batch size affect outbound logistics complexity and cost.
   - Document at least 3 linkages relevant to your business.

9. **Map vertical linkages to support activities.** Which support activities have the highest leverage on primary activities?
   - Example: Technology Development in operations might reduce labor cost; in marketing, it might enable better targeting.
   - Example: Procurement affects both inbound logistics cost and operations cost.
   - Note which support activities you currently invest heavily in and which are neglected.

10. **Identify cost driver interdependencies.** Where does optimizing one cost driver make another worse?
    - Example: Reducing batch size in operations lowers inventory holding cost but increases setup time and labor cost per unit.
    - Example: Accelerating delivery (outbound logistics) increases transportation cost.
    - List at least 2–3 such tradeoffs.

### Phase 4 — Benchmark Against Competitors

11. **For a direct competitor, estimate their value chain structure.** Use public filings, supply chain research, or interviews with customers. Estimate their cost allocation and cost drivers. You rarely will have exact figures; plausible ranges are sufficient.

12. **Compare your cost drivers to theirs.** For each activity where you have a material cost or margin disadvantage, ask: Are their costs lower because they have better technology, scale, process discipline, or input costs? Or do they have a different value chain (e.g., they outsource a high-cost activity)?

### Phase 5 — Synthesize Opportunities

13. **Identify cost reduction opportunities.** For activities consuming significant cost, ask:
    - Can we improve the cost driver (e.g., reduce batch size, automate, improve capacity utilization)?
    - Can we reduce the activity's cost by changing the value chain (e.g., outsource, integrate upstream)?
    - Are we paying for activities the customer doesn't value?

14. **Identify differentiation opportunities.** For activities where competitors are weak or where customers are price-insensitive, ask:
    - Can we invest in this activity to create competitive advantage (e.g., superior service, brand, innovation)?
    - Does investment in this activity create positive linkages (lower cost elsewhere or higher willingness to pay)?

15. **Assess strategic focus.** Evaluate which activities are strategic (core to advantage) and which are not. Support activities that are not strategic can often be outsourced; primary activities that are not strategic can sometimes be eliminated or commoditized.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Value chain diagram includes all primary activities and key support activities relevant to the business | Y/N |
| Cost or margin percentage is estimated for each primary activity (even if approximate) | Y/N |
| At least 2–4 cost drivers are identified for each major primary activity | Y/N |
| At least 3 horizontal linkages between primary activities are documented | Y/N |
| At least 2 vertical linkages to support activities are documented | Y/N |
| At least 2 cost driver tradeoffs are identified and explained | Y/N |
| Competitor value chain is estimated (at least qualitatively) for at least one competitor | Y/N |
| At least 2 cost reduction and 2 differentiation opportunities are proposed with linkage rationale | Y/N |

## Red Flags

- Value chain is generic across all industries (e.g., identical primary activity names and cost percentages regardless of business type). This indicates insufficient adaptation to the specific business model.
- Cost drivers are listed but never traced to actual margin impact or compared against alternatives. Without this tracing, the lens is descriptive but not actionable.
- No competitor comparison. Without benchmarking, you cannot distinguish what is structurally inevitable (industry-level) from what is company-specific (competitive opportunity).
- Linkages are claimed but not traced. Example: "Operations and marketing are linked" without explaining how a change in one actually changes cost or customer perception in the other.
- Support activities are assigned the same percentages regardless of business model (e.g., HR always 5%, Procurement always 8%). This suggests estimates rather than investigation.
- Opportunities are proposed without cost-benefit estimate. A "reduction opportunity" with unknown payoff and implementation cost is academic.
- Value chain omits or minimizes activities where the business actually spends money. If you claim outbound logistics is 2% of cost but the company operates a large distribution network, the chain is incomplete.

## Output Format

```
## Value Chain Analysis

**Business:** <product/service, customer segment, geography>

### Primary Activities Map
| Activity | Cost % | Margin % | Key Cost Drivers |
|---|---|---|---|
| Inbound Logistics | _% | _% | <driver 1>, <driver 2>, <driver 3> |
| Operations | _% | _% | <driver 1>, <driver 2>, <driver 3> |
| Outbound Logistics | _% | _% | <driver 1>, <driver 2>, <driver 3> |
| Marketing & Sales | _% | _% | <driver 1>, <driver 2>, <driver 3> |
| Service | _% | _% | <driver 1>, <driver 2>, <driver 3> |

### Support Activities
| Activity | Coverage | Primary leverage points |
|---|---|---|
| <...> | <which primary activities it serves> | <cost drivers affected> |

### Horizontal Linkages (between primary activities)
1. <Activity A> → <Activity B>: <effect on cost or quality>
2. <Activity A> → <Activity B>: <effect on cost or quality>
3. ...

### Cost Driver Tradeoffs
1. <Tradeoff 1>: <optimize X, worsen Y because...>
2. <Tradeoff 2>: <optimize X, worsen Y because...>

### Competitor Benchmark
**Competitor:** <name>
| Activity | Your cost driver advantage/disadvantage | Reason (scale / process / input cost / different chain) |
|---|---|---|

### Cost Reduction Opportunities
1. <Opportunity>: <activity>, <cost driver to improve>, <estimated cost reduction %>, <feasibility>
2. <Opportunity>: <activity>, <cost driver to improve>, <estimated cost reduction %>, <feasibility>

### Differentiation Opportunities
1. <Opportunity>: <activity>, <competitive lever>, <estimated willingness-to-pay lift or defensive value>, <investment required>
2. <Opportunity>: <activity>, <competitive lever>, <estimated willingness-to-pay lift or defensive value>, <investment required>

### Strategic Activity Assessment
| Activity | Strategic? | Rationale | Action |
|---|---|---|---|
| <...> | Y/N | <...> | Keep / Outsource / Divest / Invest |

### Confidence
<high/medium/low> — <justification based on data quality, benchmark visibility, and estimated payoff clarity>
```
---
