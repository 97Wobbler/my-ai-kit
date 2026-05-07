---
name: dfma
display_name: Design for Manufacturing & Assembly
class: lens
underlying_class: native
domain: manufacturing
source: Boothroyd & Dewhurst (1983); widely adopted in aerospace, automotive, and consumer electronics
best_for:
  - Reducing part count and assembly labor before tooling
  - Identifying manufacturability problems in design phase
  - Quantifying the cost impact of design choices on production
one_liner: "Design for Manufacturing and Assembly — score designs to reduce cost and process complexity early."
---

# Design for Manufacturing & Assembly

## Overview
DFMA evaluates a design (product structure, materials, geometry, tolerances) against the practical constraints of manufacturing processes and assembly labor. Rather than throwing a design over the wall to manufacturing and discovering problems late, DFMA interrogates the design *before* tooling is cut. Practitioners use it to identify parts that should be eliminated, materials that are unnecessarily expensive, and assembly sequences that will jam up the production line. The discipline is quantifying what "manufacturability" actually costs.

## Analytical Procedure

### Phase 1 — Design Decomposition

1. **Obtain or sketch the product bill of materials (BOM).** List every part, fastener, and subassembly. Include quantities and current material/process assumptions (e.g., "aluminum 6061-T6, CNC-machined," "steel stamping," "injection-molded plastic"). If the design is still on paper, sketch it; if it exists, photograph the prototype or obtain CAD.

2. **For each part, complete a Design Entry Sheet:**
   - Part name and function (what does it do in the assembly?)
   - Current material and process (material grade, process name, surface finish)
   - Annual volume (how many units per year?)
   - Current estimated piece-part cost (material + labor + overhead, or best guess)
   - Lead time for tooling (days or weeks to cut a mold or die?)

3. **Trace the assembly sequence.** In the order a worker (or robot) would assemble this product, list each step. For each step, note:
   - Which part is being added and to what
   - The orientation (does it require positioning or alignment?)
   - The fastening method (screw, snap, weld, adhesive, press-fit?)
   - Estimated labor time in seconds
   - Tools or fixtures required

### Phase 2 — Manufacturability Interrogation

For each part in the BOM, ask:

4. **Can this part be combined with another?** If this part serves only one function and is not used elsewhere, it may be a candidate for consolidation. Mark it as:
   - **Consolidate** if it can be merged into an adjacent part (e.g., a mounting boss molded into the housing instead of a separate bracket)
   - **Keep separate** if it must be separate (different material, different supplier, different lifecycle, assembly constraint)
   - **Conditional** if consolidation is possible but would require design change (e.g., "yes, if we switch to injection molding")

5. **Does this part require tight tolerances?** Measure or review the tolerance stack. For each dimension:
   - If tolerance is tighter than ±0.1 mm: mark as **tight**
   - If tolerance is ±0.1–0.5 mm: mark as **normal**
   - If tolerance is ±0.5 mm or looser: mark as **loose**
   - For each tight tolerance, ask: what fails if this tolerance is relaxed by 50%? If the answer is "nothing," relax it.

6. **Is the chosen material optimal for the process?** Review:
   - For machined parts: is the material harder than necessary (adds cost and tool wear)?
   - For stamped or molded parts: are there thin sections (<1 mm wall) that will cause flow or fill issues?
   - For assembled parts: is the material unnecessarily expensive (e.g., stainless steel for a non-corrosive environment)?
   - For high-volume parts: is the material compatible with the tooling cost structure (e.g., hard plastics suit injection molding but not hand-layup)?

7. **Does the part have unnecessary features?** Review geometry:
   - Are there holes, slots, or pockets that serve no function? (Delete them.)
   - Are there undercuts, threads, or inserts that require secondary operations? (Avoid them if possible; move to press-fit or molded inserts.)
   - Are there sharp corners or thin ribs that will stress the tooling? (Relax radii; thicken ribs.)

### Phase 3 — Assembly Interrogation

8. **For each assembly step, ask: can this be eliminated or merged?**
   - If a fastener is used, can it be replaced by a snap, adhesive, or interference fit?
   - If a part requires orientation (e.g., "align keyed slot to post"), can the geometry be made fool-proof (no wrong orientation)?
   - If a step requires a tool (screwdriver, crimper, welder), can tooling be eliminated by changing the joining method?

9. **Estimate assembly labor cost per unit:**
   - Sum all assembly step times (in seconds).
   - Multiply by effective hourly labor rate including overhead (typically $30–80/hour in developed markets, $5–15 in low-cost regions).
   - Divide by 3600 to get cost per second, then multiply by total assembly time.

10. **Identify bottlenecks:** Which step takes the longest? Which requires the most precision or the most operator training? These are high-impact candidates for redesign.

### Phase 4 — Cost Impact and Recommendations

11. **Quantify the cost-saving potential of each recommended change:**
    - **Part consolidation:** estimated savings = (piece-part cost of eliminated part) + (labor to assemble that part)
    - **Tolerance relaxation:** savings = (process cost delta if moving from precision to standard machining or molding) × (annual volume)
    - **Material substitution:** savings = (material cost delta) × (annual volume)
    - **Assembly method change:** savings = (labor time saved in seconds) × (labor cost per second) × (annual volume)

12. **Rank changes by payback period:** (Tooling cost to implement change) / (annual cost savings). Prioritize changes with payback under 1 year.

## Evaluation Criteria

| Check | Pass |
|---|---|
| BOM includes every part, fastener, and subassembly | Y/N |
| Assembly sequence is traced step-by-step with estimated times | Y/N |
| Each part was evaluated for consolidation, tolerances, material, and geometry | Y/N |
| At least 3 candidates for cost reduction were identified | Y/N |
| Savings estimates include both material and labor deltas | Y/N |
| Recommended changes are rank-ordered by payback period | Y/N |

## Red Flags

- No parts were consolidated or no assembly steps were eliminated. Either the design is near-optimal (uncommon) or the interrogation was not adversarial enough. Typical DFMA findings reduce part count by 20–40%.
- Assembly labor cost is estimated as "negligible" or not included in savings. Assembly labor often dominates unit cost for products with >5 parts; excluding it makes the analysis academic.
- Tight tolerances are marked as "required" but no failure mode is articulated. If you cannot name what breaks when the tolerance is relaxed, the tolerance is cargo-cult engineering.
- Material substitution is proposed without testing compatibility with the chosen manufacturing process (e.g., "switch to titanium" for a stamped part, which is impossible).
- Recommended changes are not costed. Consolidating two parts might save $0.50 per unit but cost $50,000 in tooling redesign; without costing, the recommendation is hollow.
- Payback period calculations omit the cost to redesign, test, and validate the change. All-in cost must be included.

## Output Format

```
## DFMA Assessment

**Product / Assembly:**
<name and brief description>

**Current annual volume:**
<units per year>

### Part Count & Consolidation
| Part | Function | Consolidate? | Rationale |
|---|---|---|---|
| <name> | <function> | Yes / No / Conditional | <reason> |

### Manufacturability Issues
| Part | Current Process | Material | Tolerances | Concern | Recommendation |
|---|---|---|---|---|---|
| <name> | <e.g., CNC mill> | <e.g., Aluminum 6061-T6> | <tight/normal/loose> | <e.g., undercut requires secondary op> | <e.g., mold-in inserts instead> |

### Assembly Sequence & Labor
| Step | Parts Involved | Method | Time (sec) | Bottleneck? | Recommendation |
|---|---|---|---|---|---|
| 1 | <...> | <screw/snap/weld> | <time> | Y/N | <e.g., use snap instead of screw> |

**Total assembly time per unit:** <seconds>
**Estimated assembly labor cost per unit:** $<x.xx> (at $<rate>/hr)

### Cost-Saving Opportunities
| Change | Impact Type | Savings Potential | Tooling Cost | Payback (months) | Priority |
|---|---|---|---|---|---|
| Consolidate X into Y | Part count reduction | $<x.xx> per unit | $<cost> | <months> | High / Med / Low |
| Relax tolerance on Z | Yield/scrap improvement | $<x.xx> per unit | $<cost> | <months> | High / Med / Low |

**Total annual cost reduction potential:** $<x> at current volume

### Confidence
<high | medium | low> — <justification. High confidence requires: confirmed assembly labor rates in the target region, validated material costs from suppliers, and design sign-off from manufacturing engineering. Medium if labor rates are estimated or material costs are preliminary. Low if design is still in concept phase or no manufacturing input has been sought.>
```
