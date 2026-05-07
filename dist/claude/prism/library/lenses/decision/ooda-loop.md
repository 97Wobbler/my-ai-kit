---
name: ooda-loop
display_name: OODA Loop
class: lens
underlying_class: native
domain: decision
source: John Boyd, U.S. Air Force (1976)
best_for:
  - Diagnosing slow or rigid decision-making in organizations
  - Accelerating tactical/strategic response cycles
  - Identifying where feedback breaks down in iterative processes
one_liner: "Accelerate the Observe-Orient-Decide-Act cycle to adapt to changing conditions."
---

# OODA Loop

## Overview
The OODA Loop (Observe–Orient–Decide–Act) is a decision cycle that Boyd developed to explain how fighter pilots win under uncertainty. The model proposes that competitive advantage accrues not to the strongest or most resourced actor, but to the one who cycles through observation, interpretation (orientation), choice, and action *fastest*. Practitioners use this lens when decision-making is sluggish, when organizations feel reactive rather than generative, or when they need to diagnose where the feedback loop breaks. The insight is not that these four steps exist — they do in any deliberate system — but that velocity through them, and the quality of the orientation phase, are the decisive factors.

## Analytical Procedure

### Phase 1 — Map the Current Cycle

1. **Identify the decision domain.** State a concrete, time-bounded decision that the organization faced in the last 3–6 months. Example: "Launch a new product feature" or "Respond to a competitor's move." Write it in 1–2 sentences.

2. **Trace the actual cycle that occurred.** Interview participants or review records to document:
   - **Observe:** What information was collected? From where? How fresh was it? What was missed?
   - **Orient:** Who interpreted the information? What mental models, biases, or assumptions framed it? Did orientation differ across teams?
   - **Decide:** Who decided? On what timeline? Were the decision criteria explicit?
   - **Act:** What action was taken? How quickly after the decision? Were there implementation blockers?
   For each phase, note the *people involved*, *time spent*, and *information flow*.

3. **Measure cycle time.** Count calendar days and working hours from initial observation to action completion. Break it down by phase:
   - Days in Observe: ___
   - Days in Orient: ___
   - Days in Decide: ___
   - Days in Act: ___
   - Total: ___

4. **Identify the feedback loop.** After the action, what information returned to the organization? How quickly? Did it feed back into Observe for the next cycle, or was it ignored?
   - Feedback present: Yes / No / Partial
   - Feedback latency: ___ days
   - Was it acted upon in a new cycle? Yes / No

### Phase 2 — Diagnose Friction Points

5. **For each phase, assign a "velocity tax."** Where was time consumed? Mark each as stemming from:
   - **Structural** — the design of the process (e.g., approval gates, handoffs, waiting for a meeting)
   - **Cultural** — norms or psychology (e.g., reluctance to surface bad news, status-driven disagreement)
   - **Skill** — lack of expertise to interpret data or decide quickly (e.g., Orient requires domain knowledge nobody has)
   - **Uncertainty** — the genuine difficulty of the problem (e.g., competitive intent is unknowable)
   Do NOT blame "Uncertainty" for delays that are actually Structural or Cultural.

6. **Test the orientation layer specifically.** This is where Boyd's insight concentrates. Answer:
   - Did the organization's mental models match the actual competitive/market reality?
   - Were there alternative interpretations of the data that were suppressed or not considered?
   - Did the team orient differently (finance vs. engineering vs. product)? If so, how was the gap resolved?
   - How much of the Decide phase was actually re-orienting (reframing the problem) vs. choosing between pre-framed options?

7. **Trace the feedback path.** After Act:
   - Was there a structured way to observe the *results* of the action?
   - Did those results challenge or confirm the original Orient? How did the org respond?
   - Did the feedback loop compress the next cycle, or did the next cycle start fresh (ignoring prior learning)?

### Phase 3 — Benchmark Against Competitors/Alternatives

8. **If possible, estimate a competitor's or counterfactual's cycle time.** Use proxy data: release velocity, product announcements, market response time, or reports from customers. The goal is not precision but order of magnitude.
   - Your cycle: ___ days
   - Competitor/alternative: ___ days
   - Ratio: ___x faster or slower

9. **Identify which phases were the delta.** If you were slower, was it Observe (late information), Orient (misalignment), Decide (too much debate), or Act (implementation drag)?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Decision domain is specific and time-bounded | Y/N |
| Actual cycle traced with people, time, and information flow for all 4 phases | Y/N |
| Cycle time measured in calendar days and broken down by phase | Y/N |
| Feedback loop existence and latency documented | Y/N |
| Velocity taxes assigned to Structural/Cultural/Skill/Uncertainty for each phase | Y/N |
| Orientation layer specifically interrogated (mental models, alternatives, gaps) | Y/N |
| Benchmark or counterfactual provided (or noted as unavailable) | Y/N |

## Red Flags

- All four phases reported equal time. Either measurement is too coarse or the organization did not actually iterate — it made a single sequential decision.
- "Uncertainty" is cited as the reason for 50%+ of delays. Recheck with the original participants — most delays attributed to uncertainty are actually Structural or Cultural once interrogated.
- The feedback loop is missing entirely. If there is no feedback, there is no loop — only a linear decision. This is a critical finding, not a minor point.
- Orientation phase is not explicitly traced. Saying "we discussed it" is not enough. What models were active? What was *not* considered? Was there disagreement?
- Cycle time for the organization and competitors are reported as identical or within 20%. Either your benchmarking is too coarse or there is no competitive disadvantage to fix.
- The revised cycle for the next iteration is not mentioned. If the org learned nothing from Act, the loop is broken.

## Output Format

```
## OODA Loop Assessment

**Decision domain:**
<specific, time-bounded decision>

### Phase 1 — Current Cycle Trace

#### Observe
- Information collected: <list>
- Sources: <list>
- Latency to receipt: <days>
- Gaps or missed signals: <list>

#### Orient
- Interpreters: <roles/teams>
- Mental models active: <list>
- Conflicting interpretations: <list>
- Resolution method: <how was disagreement settled>

#### Decide
- Decision-maker: <role>
- Timeline: <start to decision date>
- Criteria: <explicit criteria or inferred>
- Buy-in: Unanimous / Reluctant / Mixed

#### Act
- Actions taken: <list>
- Implementation timeline: <start to completion>
- Blockers: <list>

#### Feedback Loop
- Feedback mechanism: <structured / ad hoc / absent>
- Feedback latency: <days>
- Fed into next cycle: Yes / No / Partial

**Total cycle time: __ days**
- Observe: __ days | Orient: __ days | Decide: __ days | Act: __ days

### Phase 2 — Friction Analysis

| Phase | Velocity Tax | Type | Evidence |
|---|---|---|---|
| Observe | <delays> | Structural/Cultural/Skill/Uncertainty | <description> |
| Orient | <delays> | ... | ... |
| Decide | <delays> | ... | ... |
| Act | <delays> | ... | ... |

#### Orientation Layer Deep Dive
- **Mental model alignment with reality:** <accurate / misaligned / untested>
- **Suppressed interpretations:** <list>
- **Cross-team orientation gaps:** <list>
- **Reframing in Decide phase:** <occurred / did not occur>

### Phase 3 — Competitive Benchmark
- **Your cycle:** __ days
- **Competitor/counterfactual:** __ days
- **Delta phase:** <Observe / Orient / Decide / Act>
- **Root cause of delta:** <Structural / Cultural / Skill / Uncertainty>

### Recommendations
1. <Target the slowest phase and the Orientation layer explicitly>
2. ...

### Confidence
<high/medium/low> — <justification: based on data completeness, stakeholder alignment, competitive visibility>
```
