---
name: Cynefin Framework
domain: general
source: Dave Snowden, IBM Global Services / Cognitive Edge, 1999–2003
best_for: Sorting a problem or decision context into a domain that dictates which kind of response is appropriate
one_liner: "Classify a problem as Clear / Complicated / Complex / Chaotic / Confused to choose the fitting response pattern."
---

# Cynefin Framework

## Overview

Cynefin (Welsh for "habitat") is a sense-making frame that sorts a situation
into one of five domains based on the nature of cause-and-effect in play.
Its core claim is that different domains call for **different kinds of
response pattern** — and applying the wrong pattern to a domain (e.g.,
running a Complex problem as if it were Complicated) is a systematic source
of failure. Cynefin is not a classification matrix you passively label
with: the act of placing the situation *is* the intervention, because it
changes which playbooks are legitimate.

## Categories

1. **Clear** (formerly "Simple" / "Obvious")
   - Cause and effect are **known and stable**.
   - The relationship is self-evident to any trained practitioner.
   - Discriminating criterion: there is an accepted best practice, and
     applying it yields the expected outcome.
   - Example: running payroll, applying a documented refund procedure.

2. **Complicated**
   - Cause and effect are **knowable but not obvious** — they require
     analysis or expertise to uncover.
   - There is usually a right answer, but it takes an expert to find it.
   - Discriminating criterion: multiple defensible solutions exist; a
     specialist can rank them.
   - Example: tuning a production database, diagnosing a rare but
     documented failure mode.

3. **Complex**
   - Cause and effect are **only knowable in retrospect** — the system is
     adaptive and the act of probing it changes it.
   - No "right" answer ex ante; patterns emerge.
   - Discriminating criterion: you cannot predict the outcome of an action
     with confidence, only observe it.
   - Example: launching a new product into an uncharted market, cultural
     change inside an org.

4. **Chaotic**
   - **No discernible cause-and-effect relationships** — the situation is
     turbulent and demands immediate action to stabilize.
   - Discriminating criterion: there is no time to analyze, and inaction
     is itself a decision with clear downside.
   - Example: an active security incident, a crisis moment.

5. **Confused** (formerly "Disorder")
   - The domain itself is **not yet determined**. This is the starting
     default for most people most of the time.
   - Discriminating criterion: participants disagree strongly about which
     of the other four domains applies.
   - Mandatory move: decompose the situation into parts and classify each
     part separately.

## Classification Procedure

1. Write a one-paragraph description of the situation or decision as it
   currently stands.
2. Ask **"Is cause and effect knowable at all?"**
   - If **no**, the situation is either Complex or Chaotic. Ask whether
     there is time to probe (→ Complex) or only time to act (→ Chaotic).
   - If **yes**, go to step 3.
3. Ask **"Is the relationship obvious to any trained practitioner?"**
   - If **yes** → Clear.
   - If **no, but an expert can find it** → Complicated.
4. If participants disagree on which of the four answers is correct, the
   situation is **Confused** — decompose into sub-situations and classify
   each separately.
5. State the classification in writing and name the **next-step response
   pattern** implied by the category (see Implications below).

## Implications per Category

| Category | Response pattern | What the agent should do |
|---|---|---|
| **Clear** | Sense → Categorize → Respond | Apply **best practice**; use a checklist, don't over-analyze. |
| **Complicated** | Sense → Analyze → Respond | Apply **good practice**; bring expert analysis to bear; there can be several defensible answers. |
| **Complex** | Probe → Sense → Respond | Use **emergent practice**; run safe-to-fail experiments, observe what happens, amplify what works. |
| **Chaotic** | Act → Sense → Respond | Use **novel practice**; stabilize first, analyze later. |
| **Confused** | — | **Decompose**; classify each piece before proceeding. |

For a lenslab agent, the practical implication is which **lens bundle** to
load:
- Clear → a single authoritative lens (e.g., a documented checklist).
- Complicated → multiple lenses run in sequence plus a synthesis step.
- Complex → probe-oriented lenses (Pre-mortem, ACH, scenario planning);
  avoid over-confident CVSS-style scoring.
- Chaotic → stabilization heuristics, not lenses; defer full analysis.
- Confused → run classification first, then revisit lens selection.

## Common Misclassifications

- **Complex mistaken for Complicated.** Treating an adaptive system
  (culture change, market behavior) as if it were a tunable machine. The
  tell is that each "fix" produces unexpected downstream effects.
- **Complicated mistaken for Clear.** Assuming "we've done this before"
  when the current situation differs in load-bearing details. The tell is
  that the checklist produces the wrong answer in edge cases and the
  practitioner has no way to recognize the edge.
- **Clear mistaken for Complicated.** Over-analyzing a situation that
  already has a well-known best practice — a common failure mode when a
  specialist is looking for work.
- **Chaotic mistaken for Complex.** Probing when you should be acting.
  The tell is that the situation is actively degrading while you gather
  data.
- **Classifying the whole when parts belong to different domains.** Most
  real situations are Confused at the top level; the useful move is to
  decompose.
