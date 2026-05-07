---
name: veil-of-ignorance
display_name: Veil of Ignorance
class: lens
underlying_class: native
domain: philosophy
source: John Rawls, A Theory of Justice (1971)
best_for:
  - Testing fairness of policies, institutions, or distributions when stakeholders have conflicting interests
  - Surfacing hidden power asymmetries in rule design
  - Designing systems where designers cannot guarantee their own position
one_liner: "Test rule fairness by designing without knowing your own stakeholder position."
---

# Veil of Ignorance

## Overview

The Veil of Ignorance is a thought experiment for testing whether a rule, policy, or institutional design is fair. Imagine the designer must live under the rule they create, but they don't know in advance which role or position they will occupy. They don't know their wealth, talents, beliefs, or social status—only the possible positions that exist in the system. A rule is just if the designer would accept it even knowing they might end up in the worst-off position. Practitioners use this lens when distributing resources, setting voting rules, designing compensation systems, or allocating risk—anywhere power dynamics or information asymmetry could corrupt what seems "fair" into what merely benefits the powerful.

## Analytical Procedure

### Phase 1 — Identify the System and Positions

1. **State the rule, policy, or distribution scheme in one sentence.** No justification yet—just the mechanism.

2. **List all distinct positions, roles, or stakeholder groups that exist under this rule.** Include:
   - Formal roles (manager, employee, customer, regulator)
   - Status categories (experienced, novice; wealthy, poor; majority, minority)
   - Any position with asymmetric risk, benefit, or information access
   
   If a position is invisible (e.g., "people harmed by externalities"), make it visible and name it.

3. **For each position, write the concrete outcomes.** Not abstract benefits—actual costs, risks, and gains:
   - Bad: "The manager gets authority."
   - Good: "The manager can hire/fire, set wages 20–60% above minimum, and retains employment if quarterly revenue grows 5%+. Employees can be terminated with 2 weeks' notice."

### Phase 2 — Remove the Veil (Reverse-Engineer the Designer's Knowledge)

4. **Assume the designer is behind the veil.** They know:
   - The positions and outcomes (from Phase 1).
   - They will be assigned to one position at random (equal probability).
   - They can know general facts (e.g., "markets exist," "people want security") but NOT their own traits.

5. **For each position, rate its attractiveness on a 1–5 scale from the designer's perspective:**
   - 5 = I would be happy to be assigned here.
   - 1 = I would dread being assigned here.
   
   Justify each rating in one sentence. The justification must be *rational self-interest*, not ideology.

6. **Identify the worst-off position(s).** This is the position(s) with the lowest combined score accounting for:
   - Material security (income, stability, exit options)
   - Dignity and autonomy (control over decisions, protection from arbitrary harm)
   - Voice and influence (ability to change rules that affect you)
   
   If multiple positions are equally worst-off, flag it — the rule creates a tie for vulnerability.

### Phase 3 — Apply the Veil Test

7. **Ask: "Would I accept this rule if I knew I might be assigned to the worst-off position?"** 
   
   Answer honestly. Do not hedge. The answer is YES or NO based on whether you would rationally choose it knowing you might lose the lottery.
   
   - YES means: The rule's worst-off position is still acceptable. The gap between best and worst is tolerable.
   - NO means: The rule is fair only if you're not the one at the bottom. It fails the veil test.

8. **If NO, identify the specific harms.** What outcomes in the worst-off position make it unacceptable?
   - Immediate harm (starvation, unsafe conditions)
   - Structural vulnerability (no exit, no recourse, no voice)
   - Dignity violation (humiliation, arbitrariness, total dependence)

9. **Design a revision that would pass the veil test.** Modify the rule so that you would accept even the worst-off position. Document what changed and why.
   - Do not eliminate the position (hiding the problem).
   - Do transfer protections, guarantees, or voice to that position.
   - Common moves: minimum wage floors, grievance procedures, profit-sharing, term limits on power, mandatory diversity in decision-making.

### Phase 4 — Check for Hidden Positions

10. **Ask: Did anyone disappear?** Look for positions or harms that don't show up in the formal structure:
    - Customers harmed by monopoly pricing
    - Future generations bearing environmental costs
    - Outsourced workers not counted as "employees"
    - Children or dependents with no formal position
    
    If yes, add them to the positions list and re-run the veil test.

11. **Ask: Who designed the veil itself?** Veils can be rigged. If the positions listed are predetermined to exclude certain groups or harms, the veil test collapses. Note any design decisions that made the test easier by removing difficult positions from consideration.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All stakeholder positions are named and outcomes are concrete (not abstract) | Y/N |
| Each position is rated 1–5 with a one-sentence self-interested justification | Y/N |
| Worst-off position(s) clearly identified | Y/N |
| Veil test answered YES or NO (not hedged) | Y/N |
| If NO, specific harms are listed (not vague) | Y/N |
| Revision proposal addresses worst-off position (not eliminates it) | Y/N |
| Hidden positions were actively searched for and either included or justified as out-of-scope | Y/N |

## Red Flags

- All positions rate 4–5. Either the rule is genuinely just (rare) or the designer is not being honest about what it means to occupy the worst-off position. Try again and be adversarial.
- The worst-off position was defined away. ("There is no worst-off position; everyone benefits equally.") If true, why does conflict exist over the rule? Someone is losing.
- The revision preserves the rule's main feature but adds cosmetic protections ("We'll add a suggestion box for the worst-off position."). Protections must be binding and materially reduce the gap.
- Hidden positions were not searched for. Externalities, future harms, and invisible groups always exist. If the veil test ignores them, it's not actually testing fairness—it's testing fairness-within-a-chosen-group.
- The veil test itself was redesigned partway through. ("Actually, I'll assume they're risk-averse and prefer security over luxury.") The veil is neutral and equal. If you're adjusting assumptions mid-test, you're steering the outcome.

## Output Format

```
## Veil of Ignorance Assessment

**Rule, policy, or distribution scheme:**
<one sentence>

### Phase 1 — Positions and Outcomes
| Position | Concrete Outcomes |
|---|---|
| <name> | <material gains/losses, risks, autonomy, voice> |

### Phase 2 — Attractiveness Ratings
| Position | Rating (1–5) | Justification |
|---|---|---|
| <...> | <...> | <one sentence, self-interested> |

**Worst-off position(s):**
<name(s) and brief description of why>

### Phase 3 — Veil Test
**Question: Would you accept this rule if assigned randomly to any position, including the worst-off?**

**Answer:** YES / NO

**If NO — Specific harms:**
- <harm 1>
- <harm 2>
- ...

**Revision proposal:**
<Modified rule that passes the veil test. Explain what changed and why it matters for the worst-off position.>

### Phase 4 — Hidden Positions
**Positions initially excluded:**
- <invisible group or harm>
- ...

**Addressed in revision?** YES / NO

**If NO, why out-of-scope:**
<justification>

### Confidence
<high/medium/low> — <justification>
```
