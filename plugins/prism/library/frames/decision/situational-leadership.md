---
name: situational-leadership
display_name: Situational Leadership (Hersey-Blanchard)
class: frame
underlying_class: native
domain: decision
source: Paul Hersey and Ken Blanchard, "Management of Organizational Behavior", 1969
best_for:
  - Matching leadership style to follower maturity on a specific task
  - Diagnosing why a directive or delegative approach is failing
  - Deciding when to shift from coaching to autonomy
one_liner: "Pick a leadership style matched to subordinate task maturity."
---

# Situational Leadership (Hersey-Blanchard)

## Overview

Situational Leadership sorts a leader-follower pair on a specific task into one of four leadership styles based on the follower's **task-relevant maturity** — a combination of competence and commitment. The core claim is that there is no single "best" style; the appropriate style depends on where the follower sits on the maturity spectrum for *that particular task*. Applying the wrong style (e.g., delegating to someone with low maturity, or over-directing someone who is competent) is a systematic source of disengagement, frustration, and failure. The frame guides the leader to diagnose maturity and select the corresponding style.

## Categories

1. **Directing (Task behavior, high; Relationship behavior, low)**
   - Follower has **low maturity**: lacks both competence and motivation/commitment on this task.
   - The leader provides explicit instructions, close supervision, and decision-making authority.
   - Discriminating criterion: the follower is new to the task, uncertain, or disengaged; they need clear structure and frequent feedback.
   - Example: a junior engineer assigned their first production incident response; a team member returning from leave who is rusty on the current system.

2. **Coaching (Task behavior, high; Relationship behavior, high)**
   - Follower has **moderate maturity**: some competence but low commitment, or high commitment but unproven competence.
   - The leader remains directive on tasks but adds relationship-building, explanation of the "why," and two-way feedback.
   - Discriminating criterion: the follower has potential and shows signs of willingness to learn but still needs guidance and encouragement.
   - Example: a mid-level team member who is technically capable but lacks confidence in high-stakes decisions; a new hire who is motivated but still building domain knowledge.

3. **Supporting (Task behavior, low; Relationship behavior, high)**
   - Follower has **high maturity**: competent and able to solve problems independently, but may lack confidence or be low on motivation for this specific task.
   - The leader steps back from directive task control and instead provides encouragement, validation, and collaborative problem-solving.
   - Discriminating criterion: the follower can do the work but needs emotional support, recognition, or buy-in on a decision.
   - Example: a senior engineer who knows how to refactor a system but feels uncertain about the trade-offs; a capable team member frustrated by a policy change.

4. **Delegating (Task behavior, low; Relationship behavior, low)**
   - Follower has **high maturity**: fully competent, committed, and self-directed on this task.
   - The leader hands over responsibility for planning, execution, and decision-making.
   - Discriminating criterion: the follower has proven capability and intrinsic motivation; they need autonomy and ownership, not oversight.
   - Example: a senior architect redesigning the data pipeline; a staff engineer owning a critical subsystem.

## Classification Procedure

1. **Identify the specific task** under consideration. Maturity is task-relative, not universal — a senior engineer may be Delegating-ready on infrastructure but Directing-level on front-end UI work.

2. **Assess competence**: Does the follower have the technical knowledge and skill to perform this task independently? (Yes/No or Scale: Low, Moderate, High)

3. **Assess commitment**: Is the follower motivated, confident, and engaged on this task? (Yes/No or Scale: Low, Moderate, High)

4. **Map to maturity**:
   - Low competence + Low commitment → **Directing**
   - Low/Moderate competence + Moderate/High commitment → **Coaching**
   - High competence + Low/Moderate commitment → **Supporting**
   - High competence + High commitment → **Delegating**

5. **Select the corresponding style** from the Categories section. The goal is to provide *just enough* structure and relationship to move the follower toward higher maturity over time.

6. If the follower's maturity changes on this task (e.g., after a course, after success, or after a setback), revisit the classification and adjust the style.

## Implications per Category

| Category | Leadership action | How to interact | What to monitor |
|---|---|---|---|
| **Directing** | Specify goals, methods, and timelines. Give clear instructions. Supervise closely. | Frequent check-ins. Concrete feedback. Explain decisions but make them yourself. | Is the follower gaining competence? Is motivation increasing or stalled? |
| **Coaching** | Explain decisions. Invite input but retain authority. Build confidence through incremental autonomy. | Ask questions to draw out thinking. Praise effort and progress. Balance structure with encouragement. | Is confidence growing? Are they taking on more responsibility? |
| **Supporting** | Ask for their input and ideas. Share decision-making. Recognize their competence. | Listen more than direct. Validate concerns. Facilitate their problem-solving. | Are they regaining motivation? Do they feel heard? |
| **Delegating** | Define outcomes and deadlines; let them choose method. Provide resources and stay available. | Minimal check-ins unless they ask. Trust and autonomy. Celebrate results. | Are they maintaining high performance? Do they feel trusted? |

The implicit goal is to move followers toward higher maturity over time. Over-directing a Delegating-ready person erodes motivation; under-supporting someone in crisis erodes competence.

## Common Misclassifications

- **Confusing maturity with general competence.** A world-class engineer may be low-maturity on a task outside their domain (e.g., new tech stack, new business context). The tell is that you treat the person as Delegating-level and they flounder or become frustrated. Diagnosis: task-specific maturity was overestimated.

- **Mistaking low confidence for low competence.** A Coaching situation (competent but uncertain) is treated as Directing (incompetent but willing). The result is micromanagement of someone who would thrive with encouragement instead. The tell is unusual resistance or disengagement from a capable person. Diagnosis: confidence and competence are different; assess both.

- **Assuming "delegation" means abandonment.** A leader Delegates but provides zero support or resources, leaving the follower stranded. This is neglect, not Delegating. True Delegating includes availability and sufficient authority/resources. The tell is a qualified person failing and feeling unsupported. Diagnosis: the style was nominally Delegating but lacked the relationship behavior foundation.

- **Static maturity across a growing person.** A follower moves from Coaching to Supporting territory as they build competence, but the leader keeps Coaching. The result is underutilization and boredom. The tell is a capable person requesting more autonomy or showing frustration. Diagnosis: maturity was reassessed too slowly; style adjustment is overdue.

- **Failing to re-diagnose after a setback.** A delegated project fails; the leader reverts to Directing across the board instead of analyzing whether the specific task needs a style shift or whether external factors caused the failure. The tell is loss of trust and motivation even on tasks where competence is intact. Diagnosis: over-correcting to a lower style based on one failure.
