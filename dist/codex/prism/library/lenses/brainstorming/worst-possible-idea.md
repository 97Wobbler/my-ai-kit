---
name: worst-possible-idea
display_name: Worst Possible Idea
class: lens
underlying_class: native
domain: brainstorming
source: Charlie Munger (inversion); popularized in design by Shawn Coyle and in product by Paul Graham
best_for:
  - Unblocking stuck brainstorms by inverting the problem
  - Extracting quality attributes from constraint avoidance
  - Stress-testing assumptions by exploring failure modes
one_liner: "Design the worst idea on purpose, then invert it to extract the best attributes."
---

# Worst Possible Idea

## Overview
Instead of asking "How do we solve this?" ask "How would we make this fail catastrophically?" Generate the worst possible approaches to the problem, then invert each failure mode to extract the quality attributes a good solution must possess. Practitioners use this when straightforward brainstorming has run dry, when a team is locked in groupthink, or when the problem resists obvious solutions. The discipline is the inversion — most people stop after listing bad ideas and never extract the learnings.

## Analytical Procedure

### Phase 1 — Define the Problem

1. **State the problem in one sentence.** No jargon. Example: "How do we ship software faster?" not "Accelerate the CI/CD pipeline in an heterogeneous microservices environment."

2. **Identify the core constraint or outcome you're optimizing.** What does success look like? Write it as a measurable or observable target: speed, cost, quality, user satisfaction, safety, etc.

### Phase 2 — Generate Worst Possible Ideas

3. **Ask: "How would we guarantee failure at this problem?"** Generate 6-10 intentionally bad approaches. Do not hold back. The ideas should be:
   - Absurdly contrary to the stated goal
   - Grounded enough to be implementable (not pure fantasy)
   - Concrete, not vague ("make everything worse" is not enough; "hire only interns and fire anyone with 5+ years experience" is)

   Record each one as a single sentence or short description.

4. **For each worst idea, write down the failure mode it produces.** What specifically goes wrong? How does it fail at the goal?
   - Example worst idea: "Ship code on Friday afternoons with no testing."
   - Failure mode: "High defect rate, weekend outages, on-call burnout, loss of team trust."

### Phase 3 — Invert to Extract Quality Attributes

5. **For each failure mode, write the opposite as a quality attribute the good solution must have.** Do not stop at surface-level inverses. Push deeper.
   - Surface inverse (weak): "Test code before shipping."
   - Deeper inverse (strong): "Have sufficient test coverage that the team ships without fear of regressions."
   - Even deeper: "Make the cost of running tests low enough that developers run them locally before push, every time, without resentment."

6. **Group related inversions across the worst ideas.** You will see themes: "team trust," "visibility," "rapid feedback," "automation," etc. These are your emergent quality attributes. List them.

7. **For each attribute, write a one-sentence description of what it means in the context of the original problem.** Not a solution—a requirement.

### Phase 4 — Synthesis

8. **Compare the extracted attributes to the default/incumbent solution.** Does the incumbent actually possess these attributes? If not, that's a gap. If yes, you've validated the incumbent or identified why it works.

9. **Identify any attributes that emerged that you had not explicitly valued before.** These are the surprising findings — the things inversion surfaced that normal brainstorming would have missed.

10. **Map attributes to potential solutions.** For each quality attribute, sketch 2-3 possible concrete implementations. You are not committing to these; you are checking that the attributes are achievable.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem statement is jargon-free and under 20 words | Y/N |
| At least 6 worst possible ideas are generated | Y/N |
| Each worst idea has a corresponding failure mode written out | Y/N |
| Each failure mode is inverted to a quality attribute | Y/N |
| Inversions go deeper than surface opposites (≥2 levels of depth) | Y/N |
| Quality attributes are grouped into themes | Y/N |
| At least one emergent/surprising attribute is identified | Y/N |
| Each attribute is grounded in the problem context, not generic | Y/N |

## Red Flags

- The worst ideas are not bad enough. If they sound like mild critiques of the status quo, they are not inverted enough. "Reduce testing" is surface-level; "eliminate testing entirely and hire based on resume alone" is inverted.
- The failure modes are vague ("things break," "users unhappy"). Concrete failures drive better inversions.
- Inversions stay at the surface level: "Reduce defects" instead of "Eliminate the conditions that create defects in the first place."
- Only 2-3 worst ideas are generated. The session gave up too early. Keep going until ideas become absurd, then push past that boundary.
- Emergent attributes are absent. If every attribute was already part of the problem statement, inversion added no new insight — you did not go deep enough.
- No attribute is surprising or in tension with the others. Good inversions often produce tradeoffs. If everything aligns too neatly, the analysis was superficial.
- The mapped solutions in Phase 4 are just rewrites of existing solutions. If inversion only validates the incumbent, the worst ideas were not worst enough.

## Output Format

```
## Worst Possible Idea Assessment

**Problem (plain language):**
<one sentence>

**Success metric/outcome:**
<measurable or observable target>

### Phase 2 — Worst Possible Ideas and Failure Modes
| Worst Idea | Failure Mode |
|---|---|
| <...> | <...> |
| <...> | <...> |

### Phase 3 — Inversions to Quality Attributes
| Failure Mode | Surface Inverse | Deeper Inverse | Emergent Attribute |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

### Quality Attributes (Grouped)

**Theme 1: <name>**
- <attribute 1>: <one-sentence description>
- <attribute 2>: <one-sentence description>

**Theme 2: <name>**
- <...>

### Surprising / Emergent Findings
<List any attributes that were not explicitly part of the original problem framing but emerged from inversion.>

### Comparison to Incumbent/Default Solution
| Attribute | Present in incumbent? | Gap or validation |
|---|---|---|
| <...> | Y/N | <...> |

### Potential Implementations (sketch only)
**Attribute: <name>**
- Approach 1: <...>
- Approach 2: <...>

### Confidence
<high/medium/low> — <justification>
```
