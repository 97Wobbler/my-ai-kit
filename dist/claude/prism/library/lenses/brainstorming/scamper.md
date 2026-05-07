---
name: scamper
display_name: SCAMPER
class: lens
underlying_class: native
domain: brainstorming
source: Bob Eberle, 1971 (Lateral Thinking and Creativity Techniques)
best_for:
  - Systematically generating product or service variations
  - Breaking mental blocks around existing designs or processes
  - Ensuring no transformation angle is overlooked
one_liner: "Innovate by systematically transforming elements of an existing product or service (Substitute / Combine / Adapt / Modify / Put to another use / Eliminate / Reverse)."
---

# SCAMPER

## Overview
SCAMPER is a structured interrogation tool that applies seven specific transformation lenses to an existing product, service, or process to generate novel variations. Rather than brainstorming in open space, practitioners lock onto one concrete element of the current design and ask "What if we **Substitute** this?" "What if we **Combine** it with that?" and so on through all seven angles. Use this when you have a working artifact and need to systematically exhaust the nearby design space, or when a brainstorm has stalled and you suspect you're circling the same ideas.

## Analytical Procedure

### Phase 1 — Target Definition

1. **Select the artifact.** Choose a specific product, service, process, or component. Write it in one sentence. Examples: "our checkout flow," "the physical shopping cart," "our customer support email loop." Not "e-commerce" — that's too broad.

2. **List the core elements.** Break the artifact into 4–8 tangible parts, materials, steps, or features. For a shopping cart: wheels, handle, basket, payment method, checkout steps. For a support email: sender, recipient, subject line, body template, response SLA. Be granular.

3. **Define the intended user and context.** Who uses this artifact? What job are they doing? What constraints apply (budget, time, environment)? Write this in 2–3 sentences. This anchors your ideas to reality rather than pure fantasy.

### Phase 2 — Apply SCAMPER

For each of the seven letters below, follow the procedure:

**S — Substitute**
- For each element from Phase 1, ask: "What if we replaced this with something else?"
- Consider: materials (plastic → ceramic), processes (manual → automated), people (employee → customer), components (battery → solar), locations (office → remote).
- Generate at least 3 substitutions per element. Write them down.

**C — Combine**
- Ask: "What if we merged this artifact with something else? What if we combined two of its elements?"
- Consider: merge with a different product (shopping cart + phone), combine features (checkout + loyalty program), fuse workflows (support + sales).
- Generate at least 3 combinations. Write the new hybrid and its purpose.

**A — Adapt**
- Ask: "What if we adjusted this to suit a different context, audience, or use case?"
- Consider: time period (how would this work in 1850? in 2050?), geography (how would this work in Tokyo? in rural Kenya?), industry (how would we adapt this from retail to healthcare?), user skill (how for children? for experts?).
- Generate at least 3 adaptations. Write the context and the modified artifact.

**M — Modify**
- Ask: "What if we changed an attribute — size, shape, color, texture, speed, emotion?"
- Consider: scale (tiny → giant), properties (soft → rigid), sensory aspects (add sound, remove color), duration (faster, slower), aesthetics (luxury → minimalist).
- Generate at least 3 modifications. Write the attribute and the new variant.

**P — Put to Other Use**
- Ask: "What if we used this artifact for a completely different purpose? What if a byproduct became the main product?"
- Consider: new user groups (what if children used this?), new contexts (what if this worked offline?), new problems it could solve (what if the packaging was the value?).
- Generate at least 3 reuses. Write the new purpose and the user group.

**E — Eliminate**
- Ask: "What if we removed this element entirely? What is the minimal viable version?"
- Consider: Which parts are luxuries vs. necessities? What breaks if we remove it? What becomes simpler?
- For each element, ask: "Does this *have* to be here?" Generate at least 3 eliminations. Write the element and the consequence.

**R — Reverse**
- Ask: "What if we inverted the order, direction, or logic?"
- Consider: reverse the workflow (checkout before browsing), invert the relationship (customer serves the company), flip the property (expensive → free, complex → simple), opposite sequence (end before beginning).
- Generate at least 3 reversals. Write the inversion and the result.

### Phase 3 — Feasibility and Selection

4. **Mark each idea with a feasibility tag:**
   - `Quick win` — implementable with current resources, high user value
   - `Viable` — requires investment, but the business case is solid
   - `Interesting` — novel but uncertain payoff or requires significant constraints to be relaxed
   - `Fantasy` — fun to think about but not actionable under current conditions

5. **Select the top 5 ideas** across all seven categories. Prioritize by: feasibility + novelty + alignment with user need. Do not pick only the "safe" ideas — include at least one `Interesting`.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Artifact is specific enough to break into 4–8 tangible elements | Y/N |
| User and context are defined in 2–3 sentences | Y/N |
| All seven SCAMPER letters were applied (none skipped) | Y/N |
| Each letter has ≥3 distinct ideas generated | Y/N |
| Ideas are ideas, not vague statements ("make it better" doesn't count) | Y/N |
| Each idea is tagged with a feasibility label | Y/N |
| Top 5 ideas are selected and justified | Y/N |

## Red Flags

- All 21+ ideas are tagged `Fantasy` or all are `Quick win`. The method wasn't applied adversarially — you either daydreamed or recycled the safe baseline.
- Multiple ideas are repeats or trivial variants ("add a button," "remove a button"). You mechanically applied the letters without thinking.
- The "Combine" section merges the artifact with unrelated products just to generate ideas (e.g., "shopping cart + spaceship"). Combinations should have internal logic, not be random mashups.
- No ideas under "Eliminate." This usually means the artifact is already minimal or the exercise assumed every part is sacred. Push harder — what *could* be removed if we relaxed one constraint?
- The original artifact is never questioned. If every idea is an addition or modification and nothing is cut, you're in expansion mode, not design mode.
- Top 5 includes zero `Interesting` ideas. You optimized for safety. Consider including at least one high-novelty idea to expand the design space.

## Output Format

```
## SCAMPER Assessment

**Artifact:**
<one sentence>

**Core Elements:**
1. <element>
2. <element>
...

**User & Context:**
<2–3 sentences>

### S — Substitute
| Element | Substitution | Feasibility |
|---|---|---|
| <...> | <...> | Quick win / Viable / Interesting / Fantasy |

### C — Combine
| Combination | Purpose | Feasibility |
|---|---|---|
| <...> + <...> | <...> | <...> |

### A — Adapt
| Adaptation | New Context | Feasibility |
|---|---|---|
| <...> | <...> | <...> |

### M — Modify
| Attribute | Change | Feasibility |
|---|---|---|
| <...> | <...> | <...> |

### P — Put to Other Use
| Reuse | New Purpose / User | Feasibility |
|---|---|---|
| <...> | <...> | <...> |

### E — Eliminate
| Element | Consequence | Feasibility |
|---|---|---|
| <...> | <...> | <...> |

### R — Reverse
| Inversion | Result | Feasibility |
|---|---|---|
| <...> | <...> | <...> |

### Top 5 Ideas
1. <idea> — <why this one> — [Feasibility]
2. ...

### Confidence
<high/medium/low> — <justification>
```
