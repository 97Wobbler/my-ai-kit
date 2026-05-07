---
name: 5c-analysis
display_name: 5C Analysis
class: lens
underlying_class: native
domain: strategy
source: Origin uncertain; popularized in marketing and business strategy literature
best_for:
  - Mapping the competitive ecosystem before strategy formulation
  - Identifying gaps and opportunities in market structure
  - Pressure-testing assumptions about who your stakeholders are
one_liner: "Scan Company, Customers, Competitors, Collaborators, Context to locate strategic position."
---

# 5C Analysis

## Overview
Map the five forces shaping your strategic position: your Company (resources, capabilities, position), Customers (segments, needs, behaviors), Competitors (direct and indirect rivals, their moves), Collaborators (partners, suppliers, ecosystem players), and Context (macro trends, regulations, technology shifts). Unlike Porter's Five Forces (which measures competitive intensity), 5C is a structural inventory — it answers "who and what are we actually contending with?" Practitioners use this when entering a new market, launching a product, or sensing that the environment has shifted and old assumptions no longer hold.

## Analytical Procedure

### Phase 1 — Define Your Focal Point

1. **State what business, product, or market you are analyzing.** Be specific: not "e-commerce" but "direct-to-consumer dog food delivery in urban North America." This is your lens — all five Cs are evaluated relative to this focal point.

2. **Set a time horizon.** Analysis is different for "next 12 months" versus "next 5 years." Write it down.

### Phase 2 — Company Assessment

3. **List your core assets and liabilities:**
   - Financial position (runway, capital access, profitability)
   - Technical/operational capabilities (what you can and cannot do at scale)
   - Brand and customer relationships (awareness, trust, switching cost)
   - Human capital (team depth, expertise, retention risk)
   - IP and defensibility (patents, data, network effects, moats)

4. **For each asset, rate it relative to competitors:** Superior / Parity / Inferior. Be honest — parity is common.

5. **Identify the 1–2 asymmetries where you have genuine edge.** If none exist, that is a finding.

### Phase 3 — Customer Assessment

6. **Identify customer segments** served by this business or product. Segment by:
   - Job-to-be-done (what problem they are solving, not who they are)
   - Willingness to pay (price sensitivity, budget allocation)
   - Switching cost (switching cost within segment, not overall)
   - Growth trajectory (growing, stable, declining)

7. **For each segment, complete:**
   - Size (TAM, SAM, SOM or your best estimate)
   - Top 3 unmet needs or pain points
   - Current alternative (what they do instead if your product doesn't exist)
   - Concentration: are a few customers critical, or is demand distributed?

8. **Identify your penetration and share of wallet within each segment.** Where are you winning; where are you losing?

### Phase 4 — Competitor Assessment

9. **Map direct competitors.** List 3–5 companies or offerings that serve your customers' primary job-to-be-done. Include internal alternatives ("do nothing," "build in-house").

10. **For each direct competitor, assess:**
    - Their segmentation (which customer segments do they target most heavily?)
    - Their cost structure (capital-intensive, margin-constrained, or asset-light?)
    - Their strategic move (are they attacking, defending, consolidating, exiting?)
    - Their moat (what keeps customers from leaving them?)

11. **Map indirect/adjacent competitors.** Who solves the same job differently? (E.g., if your focal point is "project management," indirect competitors include Slack, email, paper notebooks, in-person stand-ups.)

12. **Identify white space.** Are there segments or use cases none of you serve?

### Phase 5 — Collaborator Assessment

13. **List key collaborators required to deliver value:**
    - Suppliers (material, labor, technology)
    - Distribution partners (channels, resellers, platforms)
    - Ecosystem partners (integrations, complementary services)
    - Influencers (industry bodies, analysts, adjacent vendors)

14. **For each collaborator, assess:**
    - Concentration: how many viable alternatives do you have?
    - Dependency: how critical is this relationship to your unit economics?
    - Leverage: do they have pricing power over you? Can they easily switch to a competitor?
    - Strategic alignment: are their interests aligned with yours?

15. **Identify dependency risks.** Which collaborators could abandon you, and what would it cost?

### Phase 6 — Context Assessment

16. **Identify macro forces** reshaping the landscape across 5 dimensions:
    - **Regulatory/Legal:** Coming laws, compliance cost shifts, litigation risk
    - **Economic:** Inflation, interest rates, recession, currency moves affecting your suppliers or customers
    - **Technological:** New capabilities (AI, hardware, platforms) that could disrupt your business or open new segments
    - **Social/Demographic:** Changing preferences, workforce, generational shifts
    - **Environmental:** Supply chain exposure, carbon cost trends, resource scarcity

17. **For each force, assess:**
    - Time to impact (next 12 months, 2–3 years, longer)
    - Which of the other four Cs does it hit hardest? (competitors, collaborators, customers, company)
    - Your preparedness (are you ahead, at parity, or behind?)

### Phase 7 — Integration

18. **Draw dependency arrows between the five Cs.** Example: if a key collaborator is the only one with a proprietary technology and a competitor just partnered with them, that is a company threat. Write these explicitly.

19. **Identify the 3–5 highest-leverage findings:** the things that, if they shift, change your strategy. Rank by consequence × uncertainty.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Focal point is specific enough that different analysts would converge on same competitors/customers | Y/N |
| Company assets are assessed relative to competitors, not in absolute terms | Y/N |
| At least 3 customer segments identified with distinct needs and willingness to pay | Y/N |
| Competitors assessed on segmentation and moat, not just market share | Y/N |
| White space identified (segments or use cases underserved) | Y/N |
| Collaborators ranked by concentration and leverage | Y/N |
| At least 3 macro forces interrogated across dimensions | Y/N |
| Dependency arrows drawn between Cs (not isolated analysis) | Y/N |
| Top 3–5 findings identified and ranked by consequence × uncertainty | Y/N |

## Red Flags

- All five Cs come out as "strong" or "no risk." Either the environment is unusually benign (rare) or the analysis lacked rigor.
- Competitors are listed by name but not mapped to customer segments. This means you don't actually know who you compete with in each segment — a critical gap.
- Collaborators section is empty or generic (e.g., "suppliers"). You likely have single-source dependencies you haven't surfaced.
- Customer segments are defined by demographics (age, geography) rather than job-to-be-done or willingness to pay. Wrong segmentation produces wrong strategy.
- No explicit white space or unmet need. Every market has gaps; missing them suggests the interrogation wasn't adversarial.
- Context forces are listed but not traced to the other four Cs. You've listed noise, not strategy inputs.
- Findings are phrased as threats or opportunities without ranking. Low-consequence findings ranked equally with high-consequence ones paralyze decision-making.

## Output Format

```
## 5C Assessment

**Focal point:** <specific business, product, or market>
**Time horizon:** <12 months / 2–3 years / other>

### Company
| Asset | Relative Position | Notes |
|---|---|---|
| <asset> | Superior / Parity / Inferior | <...> |

**Key asymmetries:** <1–2 genuine edges, or "none identified">

### Customers
| Segment | Size | Job-to-be-done | Top pain point | Current alternative | Penetration |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | <...> |

**Share of wallet:** <where winning, where losing>
**White space:** <unserved segments or use cases>

### Competitors
| Name | Target segments | Cost structure | Strategic move | Moat |
|---|---|---|---|---|
| <direct competitor> | <...> | <...> | <...> | <...> |

**Indirect/adjacent competitors:** <list>

### Collaborators
| Type | Concentration | Dependency | Leverage | Alignment |
|---|---|---|---|---|
| <supplier / partner / platform / etc.> | <high / medium / low> | <critical / important / low> | <theirs / ours / balanced> | <aligned / tension / hostile> |

**Key dependency risks:** <which collaborator loss would hurt most>

### Context
| Force | Dimension | Time to impact | Which C most affected | Your preparedness |
|---|---|---|---|---|
| <e.g., AI tooling commoditization> | <Technology> | <...> | <Company / Competitors / Customers / Collaborators> | <ahead / parity / behind> |

### Cross-C Dependencies
<Dependency arrows or narrative: how do shifts in one C cascade to others?>

### Top 3–5 Findings
1. <High consequence × uncertainty finding, ranked 1st>
2. <...>
3. <...>

### Confidence
<high/medium/low> — <Data available? Were all segments/competitors covered? Were collaborator interviews or market signals used to validate, or inference only? Any blind spots acknowledged?>
```
