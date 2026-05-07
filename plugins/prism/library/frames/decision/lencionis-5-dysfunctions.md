---
name: lencionis-5-dysfunctions
display_name: Lencioni's 5 Dysfunctions
class: frame
underlying_class: native
domain: decision
source: Patrick Lencioni, The Five Dysfunctions of a Team, 2002
best_for:
  - Sorting team or organizational dysfunction into a specific failure mode
  - Identifying which dysfunction is the root cause blocking progress
  - Determining what kind of intervention is needed to restore trust and performance
one_liner: "Pyramid of team dysfunctions stemming from lack of trust."
---

# Lencioni's 5 Dysfunctions

## Overview

Lencioni's 5 Dysfunctions sorts team behavior into a hierarchical pyramid of five reinforcing failure modes, each rooted in the absence of trust at the foundation. The core claim is that these dysfunctions **cascade upward** — fixing surface symptoms without addressing trust is futile, and conversely, building real trust automatically dismantles layers above it. Unlike a flat taxonomy, this frame is **ordered by dependency**: you cannot skip steps. A team stuck at layer 2 cannot move to layer 3 until layer 1 is resolved. This ordering means the diagnostic value of the frame lies not just in classification, but in identifying the deepest dysfunction blocking progress.

## Categories

1. **Absence of Trust** (foundational)
   - Team members do not believe others have their back or share a common intent.
   - Characterized by unwillingness to be vulnerable, admit mistakes, or ask for help.
   - Discriminating criterion: members withhold honest opinions and feedback; conversations happen offline in side conversations rather than in the room.
   - Example: a product team where engineers distrust the PM's prioritization process so deeply that they re-scope in secret and miss deadlines.

2. **Fear of Conflict** (enabled by absence of trust)
   - Team members avoid healthy debate and disagreement.
   - Manifests as artificial harmony, unexamined assumptions, and decisions that lack full buy-in.
   - Discriminating criterion: meetings are polite and quick, but nothing controversial gets raised; objections surface after decisions are made.
   - Example: a leadership team that rubber-stamps the CEO's strategy in meetings but complains in the hallway because no one felt safe to question assumptions.

3. **Lack of Commitment** (enabled by unresolved conflict)
   - Members do not genuinely buy into decisions or goals, even when they publicly agree.
   - Decisions are made but not owned; accountability is diffused.
   - Discriminating criterion: people move slowly, hedge their bets, or quietly plan exit strategies when priorities shift.
   - Example: a go-to-market plan is approved in a meeting, but sales never fully staffs it because they don't believe in it.

4. **Avoidance of Accountability** (enabled by lack of commitment)
   - Members do not hold each other to standards or call out missed commitments.
   - Performance gaps persist; underperformers are managed by the leader in private rather than by peers in public.
   - Discriminating criterion: when someone misses a deadline or commits to a low-quality output, peers let it slide; the leader eventually steps in alone.
   - Example: a design team where junior designers ship substandard work and senior designers complain to the manager instead of giving direct feedback.

5. **Inattention to Results** (enabled by avoidance of accountability)
   - The team prioritizes individual achievement, politics, or personal interests over collective goals.
   - Discriminating criterion: team members care more about being "right" or protecting their function than about whether the team's mission succeeds.
   - Example: an engineering and product org where eng celebrates shipping quickly and product celebrates shipping features, but the product stalls in user adoption because no one optimized for the shared goal.

## Classification Procedure

1. Observe the team's behavior for one sprint or cycle. Write down one or two
   concrete examples of conflict or friction that surfaced (or notably did
   not surface).

2. Ask: **"Do team members openly admit mistakes and ask for help from each other?"**
   - If **no** → dysfunction is at **Layer 1 (Absence of Trust)**. Stop here.
   - If **yes**, go to step 3.

3. Ask: **"Do team members have heated debates about ideas and decisions in real-time?"**
   - If **no** → dysfunction is at **Layer 2 (Fear of Conflict)**.
   - If **yes**, go to step 4.

4. Ask: **"After a decision is made, do all members visibly own and execute it?"**
   - If **no** → dysfunction is at **Layer 3 (Lack of Commitment)**.
   - If **yes**, go to step 5.

5. Ask: **"Do team members hold each other publicly accountable for missed commitments?"**
   - If **no** → dysfunction is at **Layer 4 (Avoidance of Accountability)**.
   - If **yes**, go to step 6.

6. Ask: **"Is the team optimized for collective results, or does each member prioritize their own function or advancement?"**
   - If **the latter** → dysfunction is at **Layer 5 (Inattention to Results)**.
   - If **the former** → the team is healthy on this frame.

7. Document the identified layer and note that all layers above it are likely symptomatic; intervention at the deepest layer is the leverage point.

## Implications per Category

| Layer | Manifestation | What the leader should do |
|---|---|---|
| **Absence of Trust** | Guarded communication, side conversations, no vulnerability. | Run trust-building interventions (offsite, personal sharing, one-on-ones); model vulnerability first; set explicit norms around transparency. |
| **Fear of Conflict** | Polite meetings, offline dissent, unexamined decisions. | Normalize healthy debate; reward people for raising concerns in the room; reframe conflict as clarity, not threat. |
| **Lack of Commitment** | Slow execution, hedging, quiet disagreement post-decision. | Require explicit buy-in (not just silence) before moving forward; surface objections; make decisions reversible to lower stakes. |
| **Avoidance of Accountability** | Underperformance tolerated, peer feedback withheld, manager handles corrections in private. | Institute peer feedback norms; make standards visible and public; have peers give feedback before the leader does. |
| **Inattention to Results** | Team members optimize for their function, politics, or individual goals rather than the collective mission. | Align incentives to shared outcomes, not individual metrics; celebrate collective wins; make team results the primary measure. |

**Critical note:** Fixes applied to a lower layer before the layer above it is resolved will be undermined. For instance, attempting accountability interventions (Layer 4) while trust is absent (Layer 1) will backfire — members will experience it as blame, not growth.

## Common Misclassifications

- **Confusing Lack of Commitment with Inattention to Results.** Lack of Commitment is about not believing in the *decision*; Inattention is about not believing in the *collective mission*. The tell: in Lack of Commitment, people execute decisions they don't believe in poorly; in Inattention, people execute their own goals very well. Fix the first with better decision-making transparency; fix the second with mission clarity and incentive alignment.

- **Attributing Fear of Conflict to Absence of Trust.** These are adjacent but distinct. Fear of Conflict shows as artificial harmony *despite* relatively functional trust — people trust each other personally but fear the interpersonal friction of disagreement. The tell: one-on-ones are candid; group meetings are careful. Absence of Trust shows as reluctance to be vulnerable *at all*. Fix the first with norms around debate; fix the second with transparency and vulnerability.

- **Mistaking Avoidance of Accountability for Inattention to Results.** Avoidance shows as peer feedback withheld and underperformance tolerated; Inattention shows as strong peer feedback but *for the wrong goal* (each person holds the other accountable to their function, not the collective mission). The tell: ask whether the team enforces accountability — if yes, but to misaligned goals, it's Layer 5; if they avoid enforcement altogether, it's Layer 4.

- **Assuming the bottom layer is always the problem.** Teams can be healthy at Layer 1 (high trust) but dysfunctional at Layer 4 or 5 (poor accountability or mission misalignment). The frame is hierarchical, but not all teams fail at the foundation — always classify from the top down.
