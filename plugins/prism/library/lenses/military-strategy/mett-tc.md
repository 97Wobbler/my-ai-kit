---
name: mett-tc
display_name: METT-TC Analysis
class: lens
underlying_class: native
domain: military-strategy
source: U.S. Army doctrine (FM 34-130, Intelligence Preparation of the Battlefield); formalized in operational planning circa 1980s–1990s
best_for:
  - Structuring operational estimates under time pressure
  - Ensuring no major planning factor is overlooked
  - Briefing commanders on decision-critical variables
one_liner: "Situational assessment framework across six key variables — Mission, Enemy, Terrain, Troops, Time, Civil."
---

# METT-TC Analysis

## Overview
METT-TC is a checklist-driven framework for operational situation assessment that ensures planners interrogate six interdependent factors before committing to a course of action. Each letter represents one variable: Mission (the task), Enemy (opposition), Terrain (physical environment), Troops (own forces), Time (temporal constraints), and Civilians (non-combatant population). Practitioners use it when planning operations, defending estimates against challenge, or discovering gaps in their intelligence picture. The discipline is the enforced completeness — plans that skip any of the six tend to fail against friction.

## Analytical Procedure

### Phase 1 — Intelligence Gathering

1. **State the operational task in one sentence.** What are we trying to accomplish, for whom, by when? This anchors all downstream analysis.

2. **For each of the six factors, collect raw intelligence and observations:**

   **Mission:** Define the strategic objective and the specific tactical task. Write the commander's intent (what end state would constitute success). Identify any constraints imposed by higher authority (rules of engagement, no-go zones, force caps).

   **Enemy:** Document known enemy strength (personnel, equipment, firepower), disposition (where they are, how spread), doctrine (how they typically fight), and leadership structure (who commands what). Note intelligence gaps and confidence levels (e.g., "we estimate 500–800 combatants within 20 km, low confidence on actual positions").

   **Terrain:** Map the physical environment: elevation, vegetation, water, lines of sight, chokepoints, natural obstacles. Identify urban vs. rural vs. open. Note weather patterns and seasonal effects (e.g., rainy season increases travel time by 40%). Mark locations critical to the mission (supply routes, defensive positions, civilian centers).

   **Troops:** Inventory own forces: available units, equipment status, training readiness, logistics capacity, reserve depth. Note morale and fatigue. Identify any shortages (ammo, fuel, specialized skills). Document recent casualty rates and medical evacuation capability.

   **Time:** Establish the operational timeline. When does the mission begin? What is the commander's desired endstate timeline? What are external time pressures (enemy reinforcements arriving, political deadlines, seasonal windows)? How long can the operation sustain itself before resupply? Map any critical decision points (e.g., "we must establish fire bases by day 3 or the operation fails").

   **Civilians:** Identify civilian population distribution, tribal/ethnic composition, political allegiances, economic dependencies, and prior interactions with military forces. Note which civilians are potential intelligence sources and which are hostile. Document displacement risk, humanitarian constraints, and local leadership.

### Phase 2 — Factor-by-Factor Assessment

3. **For each factor, answer the canonical questions** (see table below). Write answers in 2–4 sentences per question. Do not skip questions marked "critical."

| Factor | Critical Questions | Answer |
|---|---|---|
| **Mission** | What is the end state? Are there implicit sub-goals? What happens if we fail? | |
| | What constraints are we under (legal, political, logistical)? | |
| **Enemy** | Where is the enemy most likely to be? Where could they surprise us? | |
| | What is their most dangerous action? What is their most likely action? | |
| | How will they respond to our expected approach? | |
| **Terrain** | What terrain advantage does the enemy hold? What advantage do we need? | |
| | What terrain forces us to expose ourselves? What terrain is impassable? | |
| | How does weather change movement speeds and visibility? | |
| **Troops** | Can we mass sufficient force where we need it? In what timeframe? | |
| | What is our most exposed flank or weakest element? | |
| | What happens if we lose 20% of our combat power? 50%? | |
| **Time** | How long can we sustain the operation? | |
| | What do we need to accomplish in the first 48 hours? | |
| | When does the enemy's reinforcement arrive? When do we run out of ammunition? | |
| **Civilians** | Are civilians a resource, a liability, or a threat? | |
| | Could civilian movement interfere with our operations? | |
| | What civilian harm would turn the population against us? | |

### Phase 3 — Interaction and Conflict Mapping

4. **Map dependencies between factors.** For each pair (Mission–Enemy, Mission–Terrain, etc.), identify how one constrains the other:
   - Mission requires seizing a bridge; Enemy is entrenched on the far bank; Terrain has limited crossing points upstream. Mark this as a conflict.
   - Troops are mechanized; Terrain is swampy; Time is short. Mark as conflict.
   - Write 2–3 sentences on how this conflict must be resolved.

5. **Identify critical assumptions.** For each factor, list assumptions you're making (e.g., "we assume the enemy will defend in depth; assume civilians will not interfere; assume supply convoys can transit Route 4"). Mark each as `high confidence,` `plausible,` or `shaky.` Shaky assumptions are threats to the plan.

### Phase 4 — Threat and Opportunity Synthesis

6. **Extract the top 3 risks.** For each risk, state: What is it? How likely? What is the cascading effect? How do we mitigate?

7. **Extract the top 3 opportunities.** For each opportunity, state: What is it? How do we exploit it? What second-order effects does it carry?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Mission is stated in one sentence with clear end state | Y/N |
| All six factors have intelligence collected (no blanks) | Y/N |
| Confidence levels are assigned to intelligence gaps | Y/N |
| All critical questions have answers of 2+ sentences | Y/N |
| At least 3 factor-pair interactions are explicitly mapped | Y/N |
| All assumptions are tagged (high/plausible/shaky) | Y/N |
| Top 3 risks and 3 opportunities are identified and mitigation stated | Y/N |

## Red Flags

- Intelligence on one or more factors is missing or labeled "assumed." Proceeding without it increases plan failure risk.
- All assumptions are marked `high confidence.` Either intelligence was genuinely complete (rare) or risk was underestimated.
- The Mission section makes no mention of constraints. Unconstrained missions are fantasies; real operations have limits on force, time, rules of engagement, or politics.
- Enemy analysis consists only of order-of-battle numbers (strength, equipment). Doctrine, leadership, and likely responses are absent — this is a gap that hostile action will exploit.
- Terrain analysis is generic ("hilly," "populated") with no specific callouts of chokepoints or defensive positions. Specificity matters operationally.
- No civilian factor analysis, or it is stereotyped ("local population is friendly"). Civilians shift during operations; surprises here are common.
- Time section has no critical decision points, only a start date. Without knowing when you must achieve specific milestones, you cannot manage the operation.

## Output Format

```
## METT-TC Assessment

**Mission:**
<end state, strategic objective, task, constraints>

### Factor Analysis

| Factor | Key Intelligence | Confidence |
|---|---|---|
| Enemy | <disposition, strength, doctrine, likely response> | High/Medium/Low |
| Terrain | <key terrain, obstacles, chokepoints, weather effects> | |
| Troops | <available forces, shortages, reserves, readiness> | |
| Time | <timeline, decision points, reinforcement windows> | |
| Civilians | <distribution, allegiances, risks, opportunities> | |

### Critical Assumptions
1. <assumption> — [High Confidence | Plausible | Shaky]
2. <assumption> — [tag]
3. ...

### Factor-Pair Conflicts
| Pair | Conflict | Resolution |
|---|---|---|
| Mission–Terrain | <...> | <...> |
| Mission–Enemy | <...> | <...> |
| Troops–Time | <...> | <...> |
| ... | ... | ... |

### Top 3 Risks
1. **Risk:** <what> — **Likelihood:** <high/medium/low> — **Cascade:** <effect> — **Mitigation:** <action>
2. ...

### Top 3 Opportunities
1. **Opportunity:** <what> — **How to exploit:** <action> — **Second-order effects:** <consequence>
2. ...

### Confidence
<high/medium/low> — <justification. Note: high confidence requires complete intelligence on all six factors and minimal shaky assumptions; medium indicates 1–2 factors have gaps or 2+ assumptions are shaky; low indicates critical gaps in any factor or 3+ shaky assumptions>
```
