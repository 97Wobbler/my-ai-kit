---
name: swot
display_name: SWOT Analysis
class: lens
underlying_class: native
domain: strategy
source: Albert Humphrey (Stanford Research Institute, 1960s); formalized by Weihrich
best_for:
  - Situational assessment before strategy formation
  - Portfolio review against competitive environment
  - Risk identification and opportunity mapping
one_liner: "Align internal strengths/weaknesses with external opportunities/threats in a 2x2 to derive strategy inputs."
---

# SWOT Analysis

## Overview
SWOT maps the current state of an organization or initiative across four quadrants: internal factors you control (Strengths, Weaknesses) and external factors you don't (Opportunities, Threats). It is not a strategy in itself, but a structured inventory that feeds strategy. Practitioners use it to avoid blindside risks, to identify asymmetric advantages, and to force honest acknowledgment of what the organization is actually good at versus what it claims to be good at.

## Analytical Procedure

### Phase 1 — Scope Definition

1. **Define the subject and time horizon.** A SWOT on "our company" is too loose. Specify: "Our mobile app division's competitive position in the North American market, 18-month horizon" or "Our new enterprise product line against incumbent vendors, 12-month horizon." Write one sentence.

2. **Identify your reference competitor or baseline.** Against whom or what are you measuring yourself? Name them. If you're comparing against "the market," name the top 2-3 actual competitors. This prevents the analysis from drifting into vague assertions.

3. **List the key stakeholders who will act on this SWOT.** Product, Sales, Engineering, Finance — whoever will make decisions based on it. Their blind spots matter; if they don't participate in the inventory, those blind spots survive into the final list.

### Phase 2 — Internal Inventory (Strengths and Weaknesses)

4. **Brainstorm Strengths: capabilities, assets, or track records your organization has that competitors lack or do worse.**
   - Be granular. "Strong engineering" is too vague. "Built a zero-downtime deployment pipeline that competitors take 2-4 hours for" is actionable.
   - Include: technical debt or lack thereof, team depth in specific domains, brand equity, cost structure, installed base, regulatory approvals, data advantages, existing partnerships.
   - For each strength, note why it is hard to replicate. If a competitor could match it in 6 months, it's not a lasting strength.
   - Gut-check: Would a candid customer say this is true? Or are you claiming something you *want* to be true?

5. **Brainstorm Weaknesses: gaps, liabilities, or areas where you are behind competitors.**
   - Use the same granularity. "Weak sales team" → "Sales team is 40% of target headcount and lacks domain relationships in financial services."
   - Include: technical debt, skill gaps, missing features in your product, higher cost structure, limited geographic presence, regulatory constraints, lack of brand awareness in target segments.
   - For each weakness, estimate how long it would take to fix. If it takes 18+ months and your horizon is 12, it's a constraint you must design around, not a gap to fix.
   - Do not list weaknesses that are actually just "things our competitor is better at." Weaknesses are holes you have, not the fact that someone else is shinier.

6. **Pressure-test both lists.** Ask: "Would our top 3 customers or our most critical hire candidate list these as our real strengths and weaknesses?" If not, revise. Revisit Steps 4–5 with that feedback.

### Phase 3 — External Inventory (Opportunities and Threats)

7. **Brainstorm Opportunities: shifts in market, regulation, technology, or customer demand that you could capitalize on better than competitors.**
   - Include: regulatory openings (deregulation, new compliance-as-a-service markets), technology shifts (AI enabling new use cases, APIs replacing installed software), customer migration (vertical shift, geographic expansion), partnerships becoming available, supply chain disruption favoring new entrants.
   - For each, ask: Could a competitor seize this faster than us? If yes, it's not an opportunity, it's a threat. If we're uniquely positioned (due to our strengths), flag that linkage.
   - Time-bound each opportunity. "AI" is not an opportunity. "Enterprises adopting RAG pipelines in the next 12 months and lacking in-house expertise" is.

8. **Brainstorm Threats: shifts that could shrink your market, erode your advantages, or strengthen competitors.**
   - Include: competitive threats (new entrant with VC, incumbent pivoting into your segment), technology obsoletion (your solution becoming unnecessary), customer consolidation (your buyers getting acquired, losing influence), regulatory shifts (new compliance burden, licensing changes), macroeconomic pressure (budget freezes, customer churn), supply chain risk.
   - For each threat, note its probability (high/medium/low) and the lead time before impact (immediate, 6 months, 18+ months). Threats with high probability and short lead time require immediate mitigation.
   - Distinguish between threats that affect everyone in your market and threats that specifically target you. The latter are more critical.

9. **Pressure-test external lists.** Ask: "If we were a customer of a competitor, would they be worried about these opportunities and threats?" If the external environment looks unchanged, you missed something. Revisit Steps 7–8 by reading recent analyst reports, earnings calls, or news in adjacent segments.

### Phase 4 — Linkage and Implications

10. **Map Strength-Opportunity pairs.** For each opportunity, list which of your strengths position you to win. If an opportunity has no matching strength, either develop that strength or deprioritize the opportunity.

11. **Map Weakness-Threat pairs.** For each threat, list which of your weaknesses make you vulnerable. If a threat exposes a weakness you can't fix in time, you need a mitigation strategy (partnership, product pivot, market exit).

12. **Identify Strength-Threat mismatches.** Are there threats that none of your strengths defend against? Flag these as systemic risks.

13. **Identify Weakness-Opportunity mismatches.** Are there high-value opportunities you can't pursue because a weakness blocks you? Note the cost of fixing versus the opportunity cost of not fixing.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Subject and time horizon defined in one sentence | Y/N |
| Reference competitor(s) named (not "the market") | Y/N |
| Strengths are specific (e.g., "6-month lead in X" not "strong X") | Y/N |
| Weaknesses include repair timeline and criticality | Y/N |
| Opportunities are time-bounded (not evergreen) | Y/N |
| Threats include probability and lead time | Y/N |
| At least one Strength-Opportunity pair identified | Y/N |
| At least one Weakness-Threat pair identified | Y/N |

## Red Flags

- Strengths list is long (8+) or contains only generic claims ("good team," "innovative culture"). Pressure-test ruthlessly or cut the list.
- Weaknesses are listed as "competitors do X better" rather than "we lack X capability." That's competitive positioning, not inventory.
- Opportunities and Threats are identical to last year's SWOT. Either the environment is static (unlikely) or the inventory was copy-pasted without rethinking.
- No linkages drawn between internal and external. SWOT becomes a pile of facts instead of a basis for decisions.
- The SWOT is used to confirm a decision already made, rather than to discover what options are actually available.

## Output Format

```
## SWOT Assessment

**Subject:** <organization/product, 18-month horizon, reference competitors>

### Strengths (internal, hard to replicate)
- <capability> — <why hard to replicate> — <time to competitive match>
- <...>

### Weaknesses (internal, constraining)
- <gap> — <repair timeline> — <criticality>
- <...>

### Opportunities (external, time-bounded)
- <shift> — <time window> — <uniquely positioned? Y/N>
- <...>

### Threats (external, time-bounded)
- <shift> — <probability: high/medium/low> — <lead time>
- <...>

### Strength-Opportunity Pairs
| Opportunity | Matching strength(s) | Ready to execute? |
|---|---|---|
| <...> | <...> | Y/N |

### Weakness-Threat Pairs
| Threat | Exploitable weakness(es) | Mitigation strategy |
|---|---|---|
| <...> | <...> | <...> |

### Key Findings
1. <Insight: asymmetry, blind spot, or critical constraint>
2. <...>

### Confidence
<high/medium/low> — <justification: data sources, stakeholder consensus, time since last review>
```
