---
name: double-diamond
display_name: Double Diamond
class: lens
underlying_class: native
domain: product-management
source: British Design Council, 2005
best_for:
  - Separating problem discovery from solution design
  - Validating problem scope before committing to development
  - Reducing rework caused by building the wrong solution
one_liner: "Two cycles of divergence and convergence — solve the right problem the right way."
---

# Double Diamond

## Overview

The Double Diamond maps product work across four consecutive phases: Discover (divergent exploration of the problem space), Define (convergent scoping of the problem), Develop (divergent exploration of solutions), and Deliver (convergent validation and execution). Rather than moving linearly from problem to solution, practitioners use two divergence-convergence pairs to reduce the risk of solving the wrong problem or solving the right problem badly. Teams use this when they suspect the problem statement is vague or when a solution is contested and they need explicit permission to explore before committing.

## Analytical Procedure

### Discover Phase (Problem Divergence)

1. **State the trigger.** Why is the team entering the Discover phase? Is it a new product, a crisis, a hypothesis about a gap, or user feedback? Write it in one sentence. This is your anchor if the phase drifts.

2. **Define the population or scope.** Who are the potential users, customers, or stakeholders? How many? Where? Document constraints: budget, time, access, or regulatory boundaries that will limit exploration.

3. **Run at least three data collection methods.** Pick from: user interviews (5–10 people minimum), surveys (30+ respondents), field observation, usage logs, competitive teardowns, internal subject-matter experts, or customer support tickets. Spend 1–2 weeks on this. Do not skip this step or collapse it to "we already know the user."

4. **Synthesize findings into themes.** Group observations by topic (pain point, desire, workflow, constraint). Aim for 5–8 themes, not 20. For each theme, write: what did users say, how many said it, what does it imply about unmet need?

5. **Create 2–3 user personas or archetypes.** These are not marketing personas. They should capture behavioral and motivational differences among your discovery subjects. Example: "Task-focused manager who has limited time" vs. "Detail-oriented auditor who needs proof."

### Define Phase (Problem Convergence)

6. **Conduct a "problem mapping" workshop.** Bring 4–6 people from product, engineering, and support into a room (or video call) for 90 minutes. Post the themes and personas. Ask: "Which of these pain points, if solved, would move the needle for the business and the user?" Avoid solution language here — stay in the problem domain.

7. **Write the problem statement.** Use the format: "Our <population> struggles with <specific pain> because <root cause>, which results in <consequence>. We believe solving this would <measurable outcome>." This is binding — all later work must address this statement or formally revisit it. Get stakeholder sign-off.

8. **Define success criteria for the problem.** What would we measure to know if this problem is real and material? Examples: "30% of users report this pain weekly," "Support spends 8 hours/week on this," "Customers churn when this fails." These are *not* success criteria for the solution; they are criteria for knowing the problem is worth solving.

9. **Establish constraints and trade-offs.** Are there hard constraints (technical debt, regulatory, budget, timeline)? Document them. Ask: "If we had unlimited resources, would this change our problem definition?" If yes, note it. If no, the constraint is real.

### Develop Phase (Solution Divergence)

10. **Generate 4–6 solution concepts** without evaluating them. Assign different people or pairs to each. Concepts should vary in approach (e.g., one is education-focused, one is automation-focused, one is structural). Spend 2–3 days. Write each at storyboard or narrative level, not mock-up level yet.

11. **Test each concept against the problem statement.** For each of the 4–6 concepts, ask: "Does this actually solve the problem we defined?" If it pivots the problem or doesn't address the root cause, flag it. Rate each concept: solves problem fully / partially / not at all.

12. **Pressure-test feasibility.** For the 2–3 concepts that solve the problem, ask engineering: "Is this buildable in our timeline and tech stack, or does it require a rewrite?" Identify the feasibility risk level (low / medium / high) for each. Do not let feasibility eliminate a concept yet — just name the risk.

13. **Run concept testing with users.** Show the 2–3 viable concepts to 8–12 users (same or different cohort as Discover). Do not ask "which do you like?" Ask "which one would you use?" and "what problems do you see with each?" Record objections and enthusiasm separately.

14. **Synthesize concept feedback.** Tally which concept had fewer or milder objections, which generated feature requests, and which created confusion. Do not choose based on enthusiasm — choose based on clarity and alignment with the problem statement.

### Deliver Phase (Solution Convergence)

15. **Select the leading concept.** Formally name the concept that will move into design and development. Document why: it solves the problem statement, passed user testing, and has acceptable feasibility risk. Note if you're carrying forward 2–3 concepts in parallel (rare but acceptable if the risk is very high).

16. **Design the solution to fidelity level.** Depending on complexity, create a prototype, wireframe set, or detailed spec. The goal is testability — something a user can interact with or evaluate. Spend 1–2 weeks.

17. **Run a final validation with users.** Show the design to 5–8 users. Specific goal: "Does this solution address the pain point from Discover?" Do not ask for design feedback; ask if it solves the problem. If 70% or more say yes, proceed to development. If fewer, revisit the design or the problem statement.

18. **Plan the build and rollout.** Define what "done" means for each part of the solution. Plan phased rollout if high-risk (e.g., beta, canary, full). Set success metrics that correspond to the success criteria from Define.

19. **Document what you learned and what you're uncertain about.** Before shipping, write a summary of: what discovery told you, what the Define phase locked in, which design concepts lost and why, and what bets you're making in Deliver. This is the institutional memory — it prevents rework if the first release misses.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Discover phase includes 3+ data collection methods (not just internal stakeholder assumptions) | Y/N |
| Define phase produced a signed problem statement with measurable success criteria | Y/N |
| At least 2–3 distinct solution concepts were generated before convergence | Y/N |
| Each solution concept was tested with real users before Deliver phase began | Y/N |
| Develop phase included explicit user feedback that shaped the final concept choice | Y/N |
| Deliver phase included a final validation with users before full development | Y/N |
| Problem statement is formally revisited if business constraints or scope shift | Y/N |

## Red Flags

- Discover phase lasted less than one week or was skipped entirely ("we know the users already"). This is the highest-risk shortcut.
- Define phase produced a problem statement that stakeholders do not agree on in writing. Disagreement surfaces later in Deliver and becomes expensive.
- Only one solution concept was generated. Single-track thinking cannot surface the actual trade-offs.
- Solution concepts were not tested with users before Develop moved to high-fidelity design. User feedback in high-fidelity design is feedback on design taste, not problem fit.
- Deliver phase began before a final user validation. Shipping a solution that users do not recognize as addressing the problem is rework.
- The problem statement was never formally written down or was written so vaguely that different team members interpret it differently.
- Trade-offs and constraints (from Define) were not referenced during Develop and Deliver. This indicates the earlier phases were ceremonial, not binding.

## Output Format

```
## Double Diamond Assessment

**Trigger (why are we doing this):**
<one sentence>

**Population/Scope:**
<who, how many, where, constraints>

### Discover Phase
- Data collection methods used: <list>
- Key themes: <bullet list of 5–8 themes>
- User archetypes: <brief description of 2–3 types>

### Define Phase
**Problem Statement:**
> Our <population> struggles with <pain> because <root cause>, which results in <consequence>. We believe solving this would <outcome>.

**Success Criteria (for the problem):**
1. <measurable signal of real problem>
2. <...>

**Constraints:**
- <hard constraint and impact>

### Develop Phase
- Solution concepts generated: <count and brief names>
- Concepts tested with users: <which and user count>
- Leading concept chosen: <name and rationale>

### Deliver Phase
**Final User Validation:**
- Users tested: <count>
- Validation result: <X% confirmed this solves the problem>

**Planned Success Metrics:**
1. <metric tied to Define success criteria>
2. <...>

### Key Uncertainties
- <what we're betting on without full certainty>
- <...>

### Confidence
<high/medium/low> — <justification based on data quality, user consensus, feasibility confidence, and time spent in each phase>
```
