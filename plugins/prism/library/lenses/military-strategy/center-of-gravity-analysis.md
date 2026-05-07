---
name: center-of-gravity-analysis
display_name: Center of Gravity Analysis
class: lens
underlying_class: native
domain: military-strategy
source: J.F.C. Fuller (The Foundations of the Science of War, 1926); systematized by John Boyd (OODA Loop) and modern strategic doctrine
best_for:
  - Identifying the critical vulnerability or dependency in an opponent's system
  - Distinguishing between targets of symbolic vs. operational significance
  - Allocating effort where disruption cascades across multiple nodes
one_liner: "Find the enemy's critical vulnerability to achieve maximum effect with minimum resources."
---

# Center of Gravity Analysis

## Overview
The Center of Gravity (CoG) is the source of an opponent's power — the entity, capability, or relationship that, if removed or degraded, causes their entire system to fail. Unlike attrition strategies that target everything equally, CoG analysis isolates the single point of maximum leverage. Practitioners use this to avoid wasting resources on symptoms and to trace the chain of dependencies backward from a desired end state to the node that, if severed, makes all other targets irrelevant. The discipline is in resistance to the obvious target — the CoG is often not the largest or most visible node.

## Analytical Procedure

### Phase 1 — System Mapping

1. **Define the opponent's strategic objective in one sentence.** What are they trying to achieve or defend? Write it without reference to your own goal — you are describing their goal. Examples: "Maintain territorial control," "Preserve supply flow," "Maintain civilian morale."

2. **List all major nodes that enable that objective.** A "node" is a distinct entity, capability, relationship, or resource. Use these categories:
   - **Physical nodes** — equipment, facilities, personnel, stockpiles (e.g., ammunition depot, airfield, port)
   - **Organizational nodes** — command structure, alliances, supply chains, intelligence networks (e.g., logistics corps, alliance with nation X)
   - **Informational nodes** — morale, legitimacy, shared narrative, trust in leadership (e.g., belief in victory narrative, civilian confidence)
   - **Economic nodes** — sources of revenue, trade relationships, industrial capacity (e.g., oil revenue, foreign currency reserves)

   Do not filter by size or visibility yet. Aim for 8-15 nodes.

3. **For each node, map its dependencies.** Draw or write: "Node A depends on Node B." Create a dependency graph (nodes as boxes, arrows showing "depends on" relationships).
   - Example: "Air Force depends on fuel depot, airfield, pilot training pipeline, spare parts supply, foreign supply guarantee."
   - Example: "Legitimacy depends on control of narrative, military victories, civilian welfare provision."

4. **Identify critical paths.** Mark any node that, if removed, breaks multiple downstream dependencies. Trace upward: what does your target node depend on? If it has few dependencies, it is a candidate for being the CoG.

### Phase 2 — CoG Candidate Assessment

5. **Isolate CoG candidates.** These are nodes that:
   - Have few external dependencies (hard to replace or workaround)
   - Support many downstream nodes (removal cascades)
   - Are vulnerable (within reach of your resources)
   - Are non-redundant (no close substitute exists)
   
   Rank all nodes on these four dimensions. Aim for 2-4 candidates.

6. **For each candidate, run a failure scenario.** Ask: "If this node were removed or degraded by X%, what breaks?" Trace the cascade. Which downstream effects matter most to the opponent's objective?
   - Example: "If fuel depot is destroyed, air force loses 30% sortie rate in days; logistics chain fractures in weeks; legitimacy begins to erode in months as population sees visible military decline."
   - Example: "If we discredit the leadership's narrative, military effectiveness drops 15% (morale-driven decisions), but strategic objective remains intact unless cascaded to desertion."

7. **Stress-test reversibility.** Can the opponent quickly repair or replace this node? Rate as:
   - **Irreversible** — replacement takes months or is impossible (e.g., trained pilots, destroyed port infrastructure)
   - **Slow to reverse** — replacement takes weeks (e.g., ammunition stockpiles, supply rerouting)
   - **Fast to reverse** — replacement takes days or hours (e.g., temporary supply routes, personnel rotation)
   
   CoGs are typically irreversible or slow to reverse.

8. **Distinguish CoG from Critical Vulnerability.** A **Critical Vulnerability** is any weakness you can exploit. A **Center of Gravity** is the weakness that, if exploited, cascades to the opponent's strategic failure. Not all vulnerabilities are the CoG. The CoG is the most-leverage-per-unit-effort point.

### Phase 3 — Validation and Effect Modeling

9. **Validate against the opponent's behavior.** How does the opponent protect this node? Where do they concentrate forces, resources, or attention? High protection often signals high importance — but also note decoys (protected but not actually critical).

10. **Model second and third-order effects.** If you disrupt the CoG, what does the opponent do in response? Do they:
    - Accept the loss and fail to meet their objective?
    - Divert resources from other objectives to restore it?
    - Shift to a different objective altogether (strategic failure even if tactical flexibility remains)?
    
    CoG-level disruption typically forces the opponent to choose between unacceptable outcomes.

11. **Cost the effort.** Estimate the resources, time, and risk required to disrupt this node to the degree needed to trigger cascade. Compare to the value of the outcome (strategic objective denied). If cost is high relative to benefit, look at the next-best candidate.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Opponent's strategic objective stated in one sentence | Y/N |
| Dependency map includes ≥8 distinct nodes across all four categories | Y/N |
| Critical paths identified and nodes ranked on 4 dimensions | Y/N |
| CoG candidates have been stress-tested with failure scenarios | Y/N |
| Each candidate rated on reversibility (irreversible/slow/fast) | Y/N |
| CoG is distinct from supporting vulnerabilities | Y/N |
| Second-order effects traced (opponent's likely response modeled) | Y/N |
| Resource cost vs. strategic benefit estimated | Y/N |

## Red Flags

- The CoG candidate is the largest or most visible node. Size and visibility are not proxies for leverage. The real CoG is often small and hidden.
- The dependency map shows only physical nodes (tanks, bases, weapons). Organizational, informational, and economic nodes are often the true CoG, especially in asymmetric conflict.
- Multiple nodes have equal weight in the analysis. Every system has a bottleneck. If you cannot identify which node matters most, the mapping is incomplete.
- The failure scenario assumes the opponent accepts the loss passively. Real opponents respond. If the response is to shift objectives entirely, you may have found a critical vulnerability but not the CoG.
- Reversibility was not assessed. A node that can be repaired or replaced in days is not a durable CoG.
- The CoG candidate is protected equally with all other nodes. The opponent knows their own CoG and protects it more heavily than peripheral targets — or intentionally decoys you into protecting something else.

## Output Format

```
## Center of Gravity Assessment

**Opponent's Strategic Objective:**
<one sentence>

### System Mapping
| Node | Category | Dependencies | Critical Path? |
|---|---|---|---|
| <...> | Physical/Org/Info/Economic | <upstream node(s)> | Y/N |

### CoG Candidates
| Node | Externals | Downstream Support | Vulnerability | Non-redundant? |
|---|---|---|---|---|
| <...> | low/med/high | <count> | Y/N | Y/N |

### Candidate 1: <Node Name>
**Failure Scenario (X% degradation):**
<cascade description>

**Reversibility:** Irreversible / Slow / Fast — <justification>

**Second-order Response:**
<How opponent likely responds if this node is disrupted>

**Resource Cost:** <estimate>

### Candidate 2: <Node Name>
...

### Center of Gravity Selection
**Selected Node:** <name>

**Justification:**
<Why this node, not others. Summarize: few dependencies, high cascade, hard to reverse, opponent over-protects it.>

**Strategic Effect if Disrupted:**
<Opponent's objective becomes untenable or requires full strategic reset.>

### Confidence
<high/medium/low> — <justification>
```
