---
name: Rumsfeld Matrix (Known/Unknown Matrix)
domain: general
source: Donald Rumsfeld, 2002 (popularized); rooted in the Johari Window (Luft & Ingham, 1955)
underlying_class: frame
best_for: Mapping the current knowledge state of a problem and exposing blind spots before they become failures
one_liner: "Known/Unknown 2x2 that classifies knowledge states and uses proxies to surface unknown unknowns."
---

# Rumsfeld Matrix

## Overview
A 2×2 that sorts every element of a situation by two axes: whether you're aware of it and whether you understand it. The power of the frame is not the three famous quadrants — it's that it forces you to actively hunt for the fourth (Unknown Unknowns), which is where most failures originate. Practitioners use it at the start of any non-trivial investigation to avoid confirmation bias and premature convergence.

## Analytical Procedure

1. **List every element of the situation.** Include claims, assumptions, dependencies, stakeholders, data sources, time constraints, and success criteria. Aim for 15+ items. Don't filter yet.

2. **Classify each element into one quadrant:**
   - **Known Knowns** — You are aware of it AND you understand it. State the evidence that supports your confidence.
   - **Known Unknowns** — You are aware of it but don't understand it. State what specifically you don't know.
   - **Unknown Knowns** — Things you understand implicitly but haven't made explicit. Often tacit expertise, team folklore, or assumptions treated as facts. Ask: "What am I treating as obvious that an outsider would question?"
   - **Unknown Unknowns** — Things you're not aware of at all. You cannot list them directly; you generate them by proxy (see step 3).

3. **Generate Unknown Unknowns by proxy.** Run at least three of these techniques:
   - **Pre-mortem**: assume the effort failed six months from now. List the top 5 failure modes. Anything that surprises you goes here.
   - **Outsider audit**: imagine a new hire from a completely different domain reviewing your plan. What would they ask that you can't immediately answer?
   - **Historical analogy**: find 2-3 prior efforts in adjacent domains that failed. What caused them? Are those causes visible in your situation?
   - **Boundary questions**: what's just outside the scope you've defined? Why is it outside? Are you sure the scope boundary is correct?

4. **Re-classify.** The Unknown Unknowns you just surfaced become Known Unknowns. Some Known Knowns may drop to Known Unknowns once you check the evidence.

5. **Prioritize by exposure.** For each Known Unknown, estimate: impact if wrong (high/med/low) × cost to resolve (high/med/low). Resolve high-impact/low-cost first.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Every quadrant has at least 3 entries | Y/N |
| Unknown Unknowns quadrant has entries from at least 2 proxy techniques | Y/N |
| Each Known Known is tagged with the evidence backing it | Y/N |
| Top 3 Known Unknowns have owners and a resolution path | Y/N |
| At least 1 Unknown Known (tacit assumption) was made explicit | Y/N |

## Red Flags

- Unknown Unknowns quadrant is empty. This means proxy techniques weren't attempted — the whole frame is wasted.
- Known Knowns dominate and other quadrants have 1-2 entries. Classic overconfidence signal.
- Items migrate from Known Known to Known Unknown during classification. You just found a hidden assumption — flag it loudly, don't bury it.
- Unknown Knowns quadrant is empty. Either the team has zero tacit knowledge (unlikely) or no one asked the outsider question.
- Every Known Unknown is "low priority." Prioritization has been anchored to what's cheap rather than what matters.

## Output Format

```
## Rumsfeld Matrix Assessment

### Known Knowns (n=_)
- <item> — evidence: <source/signal>
- ...

### Known Unknowns (n=_)
- <item> — what we don't know: <specific gap> — owner: <name> — path to resolve: <action>
- ...

### Unknown Knowns (n=_)
- <tacit assumption now made explicit> — first surfaced by: <technique/person>
- ...

### Unknown Unknowns → Surfaced (n=_)
- <item> — surfaced via: <pre-mortem | outsider-audit | analogy | boundary>
- ...

### Top 3 Exposures
1. <Known Unknown> — impact: H/M/L — cost: H/M/L — next action: <...>
2. ...
3. ...

### Confidence
<high/medium/low> — <one sentence justification>
```
