---
name: six-thinking-hats
display_name: Six Thinking Hats
class: lens
underlying_class: native
domain: brainstorming
source: Edward de Bono, "Six Thinking Hats" (1985)
best_for:
  - Breaking groupthink in brainstorms by enforcing sequential thinking modes
  - Preventing dominant voices from collapsing discussion into one perspective
  - Systematically covering emotional, critical, creative, and logistical dimensions
one_liner: "Apply six modes of thinking sequentially for a bias-free, comprehensive review."
---

# Six Thinking Hats

## Overview
Six Thinking Hats enforces parallel thinking by assigning each participant a single thinking mode (represented by a colored hat) at a time, rather than allowing simultaneous debate. Instead of the usual chaos where optimists clash with critics while creative thinkers get ignored, everyone dons the same hat, thinks in that mode together, then switches. Practitioners use this when a brainstorm or decision meeting has devolved into tribal argument, when creative ideas die under immediate criticism, or when emotional concerns get dismissed as irrational rather than heard.

## Analytical Procedure

### Phase 1 — Setup

1. **Name the decision or problem to be explored.** Write it as a clear, jargon-free statement. Example: "Should we migrate our database to PostgreSQL?"

2. **Identify participants.** Write down who is in the room and their likely biases (engineer = efficiency-first, finance = cost-focused, product = user-centric). This is for your own awareness; do not assign hats based on role.

3. **Announce that you will wear hats in a fixed sequence.** Explain: "Each hat is a thinking mode. When we put on a hat, everyone thinks that way. No hat-switching mid-hat. The order locks in balance."

4. **Optionally set a time limit per hat.** (Example: 5 minutes for white, 10 for blue, 7 for red, etc.) Strict time-boxing prevents extended argument and forces conciseness.

### Phase 2 — Execute the Six Hats (in this order)

**White Hat — Facts and Data**
5. Everyone states: "Here is what we know. Here is what we don't know. Here is what we'd need to know to decide."
   - Write down facts (no opinion).
   - Write down gaps in information.
   - Write down what information is missing and why it matters.
   - **You are NOT evaluating, judging, or solving. You are inventorying.**

**Red Hat — Emotions, Hunches, Intuition**
6. Everyone states: "Here is how I feel about this. Here is my gut reaction. Here is what worries or excites me."
   - Feelings do NOT need justification.
   - Hunches do NOT need evidence.
   - Fears, hopes, and aesthetic reactions are all valid here.
   - **The discipline is saying feelings out loud instead of hiding them.**
   - No one is allowed to challenge a feeling statement ("That's not logical" is forbidden in this hat).

**Black Hat — Critical Judgment, Risks, Problems**
7. Everyone states: "Here is what could go wrong. Here is the flaw in this idea. Here is why it might not work."
   - Identify logical flaws, resource gaps, dependencies that could fail, and worst-case scenarios.
   - This is where skeptics legitimately dominate — it's their hat.
   - Distinguish between "this won't work" (problem) and "this is hard" (challenge). Both belong here.
   - **The discipline is comprehensive critical thinking without dismissing the idea entirely.**

**Yellow Hat — Optimism, Benefits, Best Case**
8. Everyone states: "Here is the upside. Here is what could go right. Here is the opportunity if this works."
   - Identify second-order benefits, not just the stated goal.
   - Speculate on positive scenarios without needing evidence yet.
   - Balance the black hat. If an idea has *any* value, the yellow hat finds it.
   - **The discipline is constructive speculation, not naive cheerleading.**

**Green Hat — Creativity, Alternatives, Improvements**
9. Everyone states: "Here is a variant that might work better. Here is a wild idea. Here is an angle we haven't considered."
   - Generate modifications, hybrids, and out-of-left-field approaches.
   - Separate ideation from evaluation (evaluation comes in later hats).
   - Build on others' ideas; don't veto them in this hat.
   - **The discipline is quantity over quality. Capture volume first.**

**Blue Hat — Control, Process, Synthesis**
10. Everyone states: "Here is what we've learned. Here is the next step. Here is what the group decision is."
    - Summarize what each hat revealed (you may read from your notes).
    - If a decision is due now, apply a decision rule (consensus, vote, single owner's call, etc.) and announce it.
    - If more work is needed, define what happens next and who owns it.
    - **The discipline is closure and clarity.**

### Phase 3 — Record and Review

11. **Transcribe the session.** For each hat, write down 3-5 key points from the discussion (facts, feelings, risks, benefits, ideas, next steps). Do not try to synthesize or edit — just capture.

12. **Review the balance.** Count how many turns/topics each person spoke in across all hats. If someone dominated one hat, note it. If someone was silent in a hat, note why (sometimes legitimate, sometimes a sign they don't feel safe in that mode).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem/decision stated clearly before hats begin | Y/N |
| All six hats were worn in sequence (no hat-skipping or backtracking) | Y/N |
| Each hat session has ≥3 substantive contributions from participants | Y/N |
| Red hat (emotions) was treated as valid input, not dismissed | Y/N |
| Black hat (criticism) did not slide into contempt for the idea | Y/N |
| Green hat (creativity) produced ≥2 novel alternatives or modifications | Y/N |
| Blue hat (control) produced a decision, next step, or explicit open question | Y/N |

## Red Flags

- White hat revealed almost no missing information. Either the group knows everything already (rare) or they didn't interrogate gaps hard enough.
- Red hat was skipped or compressed to 30 seconds. Emotions didn't disappear; they just went underground and will resurface as sabotage later.
- Black hat turned into personal attack ("This idea is stupid because you thought of it"). The flaw must be separated from the idea-holder.
- Yellow hat felt forced or dishonest. If an idea has NO upside, that's information — say so. But most ideas have some angle; if you can't find it, the idea may genuinely be without merit.
- Green hat produced no variants or improvements — only defenses of the original idea. Creativity was mistaken for loyalty.
- Blue hat had no decision, no next step, and no clarity on what the brainstorm produced. The session was venting, not thinking.
- One person wore all the hats while others watched. Hats enforce *parallel* thinking; solo thinking is not the method.

## Output Format

```
## Six Thinking Hats Session

**Problem / Decision:**
<statement>

### White Hat — Facts & Data
- Known facts: <...>
- Unknown facts: <...>
- Information needed: <...>

### Red Hat — Emotions & Intuition
- Feelings on the table: <...>
- Concerns: <...>
- Hopes / Excitements: <...>

### Black Hat — Risks & Criticism
- Logical flaws: <...>
- Resource gaps: <...>
- Worst case: <...>

### Yellow Hat — Benefits & Optimism
- Direct upside: <...>
- Second-order benefits: <...>
- Best-case scenario: <...>

### Green Hat — Creativity & Alternatives
- Variants: <...>
- Novel angles: <...>
- Hybrid ideas: <...>

### Blue Hat — Control & Synthesis
- Summary of findings: <...>
- Decision: <...>
- Next steps: <...>
- Owner: <...>

### Participation Balance
| Participant | White | Red | Black | Yellow | Green | Blue |
|---|---|---|---|---|---|---|
| <name> | <#> | <#> | <#> | <#> | <#> | <#> |

### Confidence
<high/medium/low> — <justification. E.g., "high — all hats were completed in sequence, emotional input was honored, and the group reached explicit next steps" or "medium — blue hat was weak and next steps remain unclear">
```
