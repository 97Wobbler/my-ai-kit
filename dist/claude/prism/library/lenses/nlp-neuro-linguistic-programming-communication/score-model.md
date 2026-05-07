---
name: score-model
display_name: SCORE Model
class: lens
underlying_class: native
domain: nlp-neuro-linguistic-programming-communication
source: origin uncertain
best_for:
  - Diagnosing communication breakdowns and systemic problems
  - Mapping intervention points in conflict or performance gaps
  - Structuring feedback that connects observable symptoms to actionable outcomes
one_liner: "Systematically map Symptom / Cause / Outcome / Resource / Effect to understand the root structure of a problem."
---

# SCORE Model

## Overview
The SCORE Model decomposes a problem or complaint into five discrete layers: the Symptoms (what is observed), the Causes (why it occurs), the Outcome (what the person wants instead), the Resources (what strengths or assets are available), and the Effects (what will change when the outcome is achieved). Practitioners use it to move beyond surface complaints and to identify which intervention point—cause mitigation, resource activation, or outcome clarification—will have the highest leverage. The discipline is staying in order and not collapsing layers into each other.

## Analytical Procedure

### Phase 1 — Extract the Complaint

1. **Collect the raw complaint or problem statement** from the subject (person, team, or organization). Write it as a paragraph without editing.

2. **Identify the primary actor.** Who is experiencing the problem? Write it as "[Actor] is experiencing [general difficulty]." If multiple actors are involved, run SCORE separately for each.

### Phase 2 — Map the Five Layers

3. **Symptoms: What is being observed or experienced?**
   - What is actually happening right now that is unwanted?
   - What behaviors, outcomes, or signals indicate the problem exists?
   - Be concrete: describe what someone would see, hear, or measure, not interpretations.
   - Write 3–5 symptoms as observable facts, not theories.

4. **Causes: Why is this happening?**
   - For each symptom, ask "Why is this occurring?" and list the contributing factors.
   - Do NOT assume a single cause — problems are usually overdetermined.
   - Categorize causes into:
     - **Structural** — organizational, process, or system-level factors
     - **Behavioral** — habits, skills, or decision-making patterns
     - **Environmental** — external conditions, resources, or constraints
     - **Cognitive** — misalignment of understanding, expectations, or information
   - List at least 2 causes in each category if applicable.

5. **Outcome: What does success look like?**
   - What is the desired state? Write it as a positive condition, not an absence of the problem.
   - Bad: "Stop being so disorganized."
   - Good: "Projects complete on schedule with clear handoff documentation."
   - Specify measurable criteria if possible (timeline, quality bar, frequency).
   - Identify what the actor(s) will be doing, thinking, or feeling in the desired state.

6. **Resources: What strengths or assets exist to move toward the outcome?**
   - What does the actor already do well?
   - What past successes can be built on?
   - What external resources (tools, expertise, relationships, budget) are available?
   - What constraints or obstacles can be reframed as opportunities?
   - List at least 3 resources across personal, interpersonal, and material categories.

7. **Effects: What will change when the outcome is achieved?**
   - What ripple effects will the solution have?
   - How will this affect the actor, their team, their stakeholders, or the broader system?
   - Identify second-order benefits (not just the direct outcome, but what becomes possible afterward).
   - Write 2–4 effects that extend beyond the immediate problem.

### Phase 3 — Identify Leverage Points

8. **For each cause identified in Phase 2, determine if it is:**
   - **Directly addressable** — the actor or their team can change it
   - **Resource-dependent** — it requires activating a resource already available
   - **Structural** — it requires system-level change outside the actor's direct control
   Mark each accordingly.

9. **Rank causes by leverage:** Which causes, if addressed, would eliminate the most symptoms and move the actor closest to the outcome? Which require the least effort or resources?

10. **Propose intervention hypotheses.** For the top 2–3 causes, sketch what removing or mitigating that cause would look like. Use the Resources list to suggest concrete first steps.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Complaint is stated without editorializing interpretation | Y/N |
| Symptoms are observable, concrete, and distinct from causes | Y/N |
| At least 2 causes are listed; causes are categorized (Structural/Behavioral/Environmental/Cognitive) | Y/N |
| Outcome is framed positively with measurable criteria | Y/N |
| At least 3 resources are identified across multiple categories | Y/N |
| Effects extend beyond the immediate problem (second-order impact included) | Y/N |
| Each cause is marked for addressability (direct/resource-dependent/structural) | Y/N |
| Top causes are ranked and intervention hypotheses are sketched | Y/N |

## Red Flags

- Symptoms are phrased as judgments ("They're lazy") rather than observations ("They miss 3 of 5 weekly deadlines").
- Only one cause is identified, or all causes are attributed to a single person's fault.
- Outcome is stated as "stop doing X" rather than "start doing Y" — this indicates unclear vision, not clarity.
- Resources section is empty or lists only constraints. Every actor has some strengths; missing them suggests the analysis wasn't adversarial enough.
- Effects are identical to the outcome, not extensions of it. Secondary impact was not traced.
- Causes are not marked for addressability — the analysis stops before determining what can actually be changed.
- Intervention hypotheses are vague or recommend behaviors without connecting to identified causes.

## Output Format

```
## SCORE Assessment

**Actor:** <who is experiencing the problem>
**Problem domain:** <brief category>

### Symptoms (Observable facts)
- <observable condition>
- <observable condition>
- <observable condition>

### Causes (Why the symptoms occur)
**Structural:**
- <cause>
- <cause>

**Behavioral:**
- <cause>

**Environmental:**
- <cause>

**Cognitive:**
- <cause>

### Outcome (Desired state)
<Positive statement of what success looks like. Include measurable criteria if applicable.>

### Resources (Strengths and assets available)
- <Personal strength>
- <Skill or past success>
- <External tool, relationship, or budget>
- <Constraint reframed as opportunity>

### Effects (What will change)
- <Immediate ripple effect>
- <Second-order benefit>
- <System-level or relational change>

### Leverage Analysis
| Cause | Category | Addressability | Effort to address | Symptoms eliminated | Rank |
|---|---|---|---|---|---|
| <cause> | Structural/Behavioral/Environmental/Cognitive | Direct/Resource-dependent/Structural | High/Medium/Low | N symptom(s) | 1 |

### Top Intervention Hypotheses
1. **Cause:** <highest-leverage cause> → **Intervention:** <concrete first step using available resources>
2. **Cause:** <second-highest> → **Intervention:** <concrete first step>

### Confidence
<high/medium/low> — <justification. Consider: Were all five layers filled in? Are resources adequately identified? Is the outcome genuinely achievable given the causes and resources?>
```
