---
name: fault-tree-analysis
display_name: Fault Tree Analysis (FTA)
class: lens
underlying_class: native
domain: manufacturing
source: Bell Laboratories, 1962 (H. A. Watson); ISO 26262 and IEC 61025 standardization
best_for:
  - Mapping failure chains in safety-critical systems
  - Identifying single-point-of-failure vulnerabilities
  - Quantifying probability of catastrophic top-level events
one_liner: "Work backward via AND/OR logic to derive root-cause combinations of failure paths."
---

# Fault Tree Analysis (FTA)

## Overview
Fault Tree Analysis reverse-engineers a system failure by constructing a logic diagram that maps all combinations of subsystem, component, and operator errors that lead to a top-level undesired event. The tree is built downward from the failure outcome (root) to the base faults (leaves), connected by AND gates (all conditions must occur) and OR gates (any condition is sufficient). Practitioners use FTA to expose hidden failure pathways, quantify risk when component failure rates are known, and validate that redundancy is actually redundant. The discipline is in the completeness and precision of the gates — a misplaced AND or OR can hide the real vulnerability.

## Analytical Procedure

### Phase 1 — Define the Top Event and System Boundary

1. **State the top-level undesired event in concrete terms.** Not "system failure" but "loss of brake pressure during descent" or "incorrect drug dosage delivered to patient." Include timing or context if it matters (e.g., "during operation, not during maintenance").

2. **Draw a box around the system.** Everything inside is analyzable; everything outside (user error, natural disaster, malicious sabotage) may be included as a primary event but is not decomposed further. Document what is explicitly out of scope.

3. **Identify constraints on the analysis.** Is this a new design (all failure modes are speculative) or an operational system (failures are observed)? Do you have component failure rate data? Will you do Boolean algebra simplification or leave the tree as-is for readability?

### Phase 2 — Decompose Events into Fault Logic

4. **For the top event, ask: "What must be true for this to happen?"** The answer is either:
   - An AND gate: all of these sub-events must occur (e.g., "pump fails AND backup pump fails AND operator doesn't notice").
   - An OR gate: any one of these sub-events is sufficient (e.g., "primary sensor fails OR secondary sensor fails OR wiring shorts").
   - A hybrid: multiple AND/OR combinations.

5. **Assign each answer as a child event and add the appropriate gate.** Use standard FTA symbols:
   - Rectangle = an event that results from logical combination of other events (decomposable).
   - Circle = a primary event (base fault, leaf — not decomposed, failure rate assumed or measured).
   - Diamond = an event that is conceptually decomposable but for practical/cost reasons is treated as basic.
   - House symbol = an event that is external to the system (e.g., power grid failure).

6. **Repeat for each child event.** Ask "What must be true for *this* to happen?" Continue until:
   - You reach a primary event (circle) with a known or measurable failure rate.
   - You reach an out-of-scope event (house or decision to stop).
   - You have decomposed to a level of detail meaningful for your analysis.

7. **Validate gate type for each node.** A common error: treating an OR gate as AND (or vice versa). Use this decision rule:
   - AND gate: if one child event fails to occur, the parent does NOT occur.
   - OR gate: if one child event occurs, the parent occurs regardless of the others.
   - Conditional gates (INHIBIT, PRIORITY AND): if timing or sequence matters, use these; otherwise they hide information.

### Phase 3 — Populate Failure Rates (if quantitative)

8. **Collect or estimate failure rates for each primary event.** Sources: component datasheets, maintenance records, industry standards (MIL-HDBK-217, Telcordia), expert judgment. Document the source and date. Include units (failures per hour, per million hours, per demand, per calendar year).

9. **Assign a confidence level to each rate:** `measured` (from field data ≥100 failures), `calculated` (from supplier data, ≥10 samples), `assumed` (expert judgment or literature, high uncertainty).

10. **Propagate probabilities up the tree.** For each gate:
    - OR gate: P(parent) = 1 − ∏(1 − P(child_i))
    - AND gate: P(parent) = ∏ P(child_i)
    - Round to appropriate precision (usually 1–2 significant figures given input uncertainty).

11. **Compute the top event probability.** This is the probability that the undesired outcome will occur in the specified operational period (e.g., per flight hour, per year). Compare to the system safety requirement (e.g., "no more than 1 failure per 10^9 hours").

### Phase 4 — Identify Critical Paths and Sensitivity

12. **Rank the primary events by their contribution to top-level risk.** Use Birnbaum importance (for AND gates, how much does P(parent) change if P(child) goes from 0 to 1?) or Fussell-Vesely importance (what fraction of top-level probability is attributable to this event?). List the top 5–10.

13. **Find minimal cut sets.** A cut set is a combination of primary events that, if they all occur, guarantees the top event. A minimal cut set cannot be reduced further (no subset is itself a cut set). These are the real failure pathways. Example: {Pump_fails, Backup_pump_fails, Operator_error} is a cut set; {Pump_fails, Backup_pump_fails} is minimal if the operator error is secondary.

14. **Examine single-point failures.** If any primary event appears alone as a cut set of order 1, the system has no redundancy for that failure mode. These are high-priority for mitigation.

15. **Perform sensitivity analysis.** For each primary event in the critical path, reduce its failure rate by half and recompute top-level risk. Which events have the most impact per unit improvement? These are the best targets for design change.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Top event is concrete, not generic ("system failure") | Y/N |
| System boundary and out-of-scope items explicitly stated | Y/N |
| Every non-primary event has a defined gate (AND/OR/INHIBIT) | Y/N |
| Primary events are basic faults, not intermediate failures | Y/N |
| Decomposition is to a level consistent with available data and safety requirement | Y/N |
| Each primary event has a failure rate with source and confidence tag | Y/N |
| Top-level probability computed and compared to requirement | Y/N |
| Minimal cut sets identified; single-point failures flagged | Y/N |
| Critical path events ranked by importance | Y/N |

## Red Flags

- Top event is vague ("loss of control," "critical failure"). The analysis will inherit that vagueness and hide the real risks.
- All gates are OR. This usually means the tree is too shallow — decomposition stopped too early or every pathway was treated as equivalent in probability.
- Primary events are actually intermediate events ("pump fails due to cavitation"). These hide the actual root causes (worn seal, contaminated oil, etc.) and allow the analysis to miss common-mode failures.
- Failure rates are identical across components or are round numbers (1e-4, 1e-5). These are guesses, not data. Mark them `assumed` and run sensitivity analysis.
- No single-point failures identified, but the system has no redundancy. The tree was drawn incorrectly or the gate logic is wrong.
- Minimal cut sets were not computed. Without them, you cannot answer "what combination of faults will kill this system?" — the core question FTA exists to answer.
- Top-level probability is below the requirement, but no evidence that component reliability is actually that good. Check for optimism bias in failure rate assignment.

## Output Format

```
## Fault Tree Analysis Report

**Top event:**
<concrete, with timing/context>

**System boundary:**
<what is included; what is out-of-scope>

**Analysis type:** [Qualitative | Quantitative]

### Fault Tree Structure
| Event ID | Event Name | Type | Gate | Children | Primary Rate | Source | Confidence |
|---|---|---|---|---|---|---|---|
| T1 | <top event> | Rectangle | AND/OR | <C1, C2, ...> | — | — | — |
| C1 | <intermediate> | Rectangle | AND/OR | <P1, P2> | — | — | — |
| P1 | <primary fault> | Circle | — | — | <rate, /unit> | <source> | measured/calculated/assumed |

### Minimal Cut Sets
1. {<P1>, <P2>} — <brief description>
2. {<P3>} — <single-point failure>
3. ...

### Single-Point Failures
- <P3>: leads to top event directly via cut set {<P3>}
- <P5>: ...

### Top-Level Risk
**Computed probability:** <value, units, confidence>
**Safety requirement:** <value, units>
**Margin:** <compliant / non-compliant>

### Importance Ranking (critical path)
| Event | Birnbaum Importance | Fussell-Vesely % | Sensitivity (% change in top-level risk per 50% reduction) |
|---|---|---|---|
| <P1> | <...> | <...>% | <...>% |

### Recommendations
1. Reduce or eliminate {<P3>} single-point failure via <mitigation>
2. Redesign <intermediate> subsystem to improve <gate> logic
3. Collect field failure data for <P5>; current rate is assumed

### Confidence
<high/medium/low> — <justification: e.g., "Qualitative only; no failure rate data collected," or "Quantitative; 80% of rates from ≥100 observed failures, 20% from literature; single-point failure in power supply not yet designed out.">
```
