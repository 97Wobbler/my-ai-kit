---
name: empathy-map
display_name: Empathy Map
class: lens
underlying_class: native
domain: marketing
source: Dave Gray (XPLANE, 2012); popularized by Strategyzer
best_for:
  - Understanding user behavior and motivations across six dimensions
  - Surfacing gaps between assumed and actual customer experience
  - Grounding product decisions in observed user needs rather than internal assumptions
one_liner: "Six-axis map of what customers think / feel / see / hear / say / do to surface underlying needs."
---

# Empathy Map

## Overview
An Empathy Map captures what a specific user persona thinks, feels, sees, hears, says, and does in a particular context. Rather than listing demographic data or abstract user needs, it forces practitioners to populate six concrete dimensions simultaneously, making contradictions and blind spots visible. Practitioners use it when they suspect their understanding of the customer is second-hand or when product teams lack alignment on who they're actually building for.

## Analytical Procedure

### Phase 1 — Prepare

1. **Define the persona precisely.** Write down the specific user type you're mapping (e.g., "A remote software engineer trying to hire their first freelancer," not "Small business owner"). Include the context where this user operates.

2. **Choose a single moment or decision.** The map is most useful when frozen on a specific scenario: searching for a solution, using a competitor's product, encountering a problem, making a purchase. Write the moment in one sentence.

3. **Assemble 2–3 people who have direct user contact.** Do not rely on one person's interpretation. Include someone from support, sales, or research if possible.

### Phase 2 — Populate the Six Dimensions

For each dimension below, generate items by asking the corresponding questions. Write concrete observations and quotes, not abstractions. If you cannot populate a dimension, note "Unknown" rather than guessing.

4. **SEES.** What does this user encounter in their environment?
   - What is around them? (physical space, tools, others)
   - What do they read or watch?
   - What problems or opportunities do they encounter daily?
   - What do competitors or similar products do?
   - *Document:* 3–5 concrete observations. Use phrases like "notices X," "surrounded by Y," "sees ads for Z."

5. **HEARS.** What influences come through other people?
   - What do friends, family, colleagues, or industry peers say to them?
   - What do influencers or authorities in their space claim?
   - What do they overhear?
   - What media do others recommend to them?
   - *Document:* 3–5 quotes or paraphrases. Tag each by source: "From peers," "From boss," "From community."

6. **THINKS.** What is likely on their mind?
   - What do they worry about?
   - What do they aspire to?
   - What problems are they trying to solve?
   - What does success look like to them?
   - *Document:* 3–5 internal states. Use phrases like "concerned about X," "wants to prove Y," "believes Z is important."

7. **FEELS.** What emotions are present?
   - What frustrates them?
   - What excites them?
   - What makes them anxious or confident?
   - What do they care deeply about?
   - *Document:* 3–5 emotional states. Use adjectives: "frustrated," "proud," "uncertain," "energized."

8. **SAYS.** What do they articulate publicly?
   - What do they claim their priorities are?
   - What do they complain about?
   - How do they describe their role or needs to others?
   - What language do they use naturally?
   - *Document:* 3–5 direct quotes or representative statements. Capture tone and terminology.

9. **DOES.** What are their observable actions?
   - How do they spend their time and money?
   - What workarounds or rituals do they use?
   - How do they make decisions?
   - What do they avoid?
   - *Document:* 3–5 concrete behaviors. Use phrases like "spends 40% of time on X," "always checks Y before Z," "skips Z entirely."

### Phase 3 — Surface Contradictions and Gaps

10. **Compare across dimensions.** Construct a contradiction matrix. Where does what they SAY differ from what they DO? Where does what they THINK diverge from what they HEAR?
    - Example: User says "I care about security" but does "uses same password everywhere" — this gap is actionable.
    - Example: User hears "cloud is the future" but thinks "on-premise is safer" — this tension suggests conflicting influences.

11. **Identify the missing dimension.** Scan the map. Is one dimension sparse or empty? (E.g., "HEARS" is blank.) This usually signals either a genuine gap in the user's environment or insufficient research.

12. **Note emotional vs. rational gaps.** Do they feel differently than they think? Do they say something different than they feel? These gaps often contain the actual user motivation, hidden under professionalism or social desirability.

### Phase 4 — Extract Needs and Pain Points

13. **List the user's unmet needs.** For each dimension, ask: "What is this user lacking?" Do not invent solutions yet — name only the need. A need is a gap between current state (what the map shows) and desired state (what they think, feel, or aspire to).

14. **List pain points.** Extract moments of friction or emotion from the map. A pain point is a specific, observable problem that causes frustration or wasted effort.

15. **Rank by frequency and intensity.** Which needs appear in multiple dimensions? Which pain points come with strong emotion? These are high-signal.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Persona is specific (not a category, an individual archetype) | Y/N |
| Decision moment is named explicitly | Y/N |
| All six dimensions are populated (or marked "Unknown") | Y/N |
| Each dimension has 3+ items drawn from user contact, not assumption | Y/N |
| At least one SAYS/DOES or THINKS/HEARS contradiction is identified | Y/N |
| Needs are stated as gaps, not solutions | Y/N |
| Pain points are tied to observed behavior or quotes | Y/N |

## Red Flags

- All six dimensions are written from internal assumptions without consulting users who have direct contact.
- Multiple dimensions are empty or trivial ("sees: computer," "does: works"). Insufficient research or wrong persona definition.
- SAYS and DOES are nearly identical — the user exhibits no gap between public claim and private action (suspect incomplete observation).
- Every item under THINKS is aspirational; no concerns or conflicts. Users are not monolithic.
- Needs are phrased as features ("needs a dashboard") rather than as outcomes ("needs to monitor team productivity in real time without manual reporting").
- More than one dimension is pure speculation (phrases like "probably feels," "likely believes").

## Output Format

```
## Empathy Map

**Persona:** <name, archetype>

**Context:** <specific moment or decision>

### SEES
- <observation 1>
- <observation 2>
- ...

### HEARS
- <quote/influence 1> — [source]
- <quote/influence 2> — [source]
- ...

### THINKS
- <internal concern/aspiration 1>
- <internal concern/aspiration 2>
- ...

### FEELS
- <emotional state 1>
- <emotional state 2>
- ...

### SAYS
- "<quote or representative statement 1>"
- "<quote or representative statement 2>"
- ...

### DOES
- <behavior 1>
- <behavior 2>
- ...

### Contradictions & Gaps
| Dimension A | Dimension B | Contradiction | Implication |
|---|---|---|---|
| <...> | <...> | <what diverges> | <what this reveals> |

### Unmet Needs
1. <need statement — outcome, not solution>
2. <need statement>
...

### Pain Points
1. <pain point with tie to observed behavior or emotion>
2. ...

### Confidence
<high/medium/low> — <justification based on research depth, contradiction clarity, and team alignment on persona>
```
