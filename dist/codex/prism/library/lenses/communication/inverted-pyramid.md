---
name: inverted-pyramid
display_name: Inverted Pyramid
class: lens
underlying_class: native
domain: communication
source: Journalism (19th century onwards); formalized in news writing practice; adapted to technical and business communication
best_for:
  - Organizing documents where readers scan or stop mid-read
  - Prioritizing what matters in reports, summaries, and announcements
  - Testing whether your most important claim is actually leading
one_liner: "Journalism lede: most important first, supporting material after."
---

# Inverted Pyramid

## Overview
Lead with your conclusion, finding, or most newsworthy fact. Then add supporting detail, context, and elaboration in descending order of importance. The reader gets the full story in the first paragraph and chooses how deep to go. Practitioners use this to optimize for readers who skim, for channels that truncate (email subject lines, chat previews, search snippets), and to force clarity about what actually matters in a document. The discipline is ruthless prioritization — most writers bury their finding under setup and apology.

## Analytical Procedure

### Phase 1 — Extract the Core Finding

1. **Read the entire document or communication.** Do not stop partway.

2. **Write one sentence: "What is the single fact, decision, or claim that would be news to the reader if they knew nothing else?"** This sentence should:
   - Stand alone — the reader should not need any prior context
   - Make a concrete assertion, not pose a question
   - Be jargon-free and under 25 words
   - Answer "so what?" for the reader

3. **If you cannot write this sentence, the document is not ready.** Rewrite it. This step is not skippable.

### Phase 2 — Audit Current Structure

4. **Note the position of your core finding in the draft.**
   - Paragraph 1? (Good)
   - Paragraph 2–3? (Acceptable if para 1 is a brief, strong setup)
   - Paragraph 4 or later? (Inverted Pyramid failure — it's buried)
   - Never stated explicitly? (Structure failure — you are hiding the finding)

5. **List everything that comes *before* your core finding.** Mark each as:
   - **Setup** — historical context, background, or prerequisites the reader needs to understand the finding
   - **Apology** — hedging, caveats, or admissions that the finding is incomplete ("This is preliminary, but...")
   - **Process** — description of how the finding was produced (research method, analysis steps, etc.)

6. **For each item marked "Setup" or "Apology," ask: "Would a reader need this to *understand* the core finding, or does it serve only to soften it?"** If softening, move it after the core finding. If truly necessary for understanding, condense it to one sentence and place it immediately before the core finding (not earlier).

### Phase 3 — Reorganize by Importance

7. **After stating your core finding, list all supporting points from the rest of the document.** Rank them:
   - **Tier 1** — The reader should know this if they read two more sentences
   - **Tier 2** — The reader should know this if they read three paragraphs
   - **Tier 3** — Nice to know; can go at the end or in an appendix

8. **Write each tier as a separate paragraph, in order of importance within that tier.** Each paragraph should:
   - Start with the point (not the evidence)
   - Provide one concrete detail or stat
   - Stop (do not linger for rhetorical effect)

9. **For each paragraph after the core finding, test: "If I deleted this paragraph, would the reader miss anything that changes their understanding of the core finding?"** If no, move it later in the document or cut it.

### Phase 4 — Verify Completeness

10. **Ensure the first paragraph can stand alone.** Read only paragraph 1. Does the reader know what happened, why it matters, and what comes next? If not, rewrite para 1.

11. **Skim the document: first sentence of each paragraph, then stop.** You should track a coherent argument from top to bottom. If you get lost, the hierarchy is wrong.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Core finding is explicitly stated in paragraph 1 | Y/N |
| Core finding is a single, jargon-free sentence under 25 words | Y/N |
| No apology or hedging precedes the core finding | Y/N |
| All necessary setup (if any) is condensed to ≤2 sentences before the core finding | Y/N |
| Supporting points are ranked and ordered by importance tier | Y/N |
| First paragraph stands alone as a complete micro-story | Y/N |
| Reading only the first sentence of each paragraph reveals the main argument | Y/N |

## Red Flags

- The core finding is in paragraph 2 or later, preceded by "background" or "context." Inverted Pyramid requires it to lead.
- The first paragraph is a question ("What is X?") rather than an assertion. Questions force the reader to keep reading to find the answer — they do not optimize for scanning.
- Multiple competing claims vie for "most important" in the opening. Pick one. Others go in Tier 1 or Tier 2.
- The word "however," "but," "unfortunately," or other reversals appear in paragraph 1. That is apology/hedging — move it after the finding.
- The document explains *how* the finding was discovered before stating *what* was found. Process goes after conclusion.
- Sentences in the first paragraph are longer than 20 words. Longer sentences slow scanning and hide the point.
- The document reads the same inverted or rightside-up. If cutting it at 50% would leave the reader with no answer, it is not inverted.

## Output Format

```
## Inverted Pyramid Assessment

**Document / Communication:** <title or type>

### Phase 1 — Core Finding
**Extracted core finding (single sentence):**
> <one assertion, under 25 words, no jargon>

### Phase 2 — Current Structure Audit
**Position of core finding in draft:**
Paragraph _

**Content before core finding:**
| Item | Type | Needed? | Action |
|---|---|---|---|
| <...> | Setup / Apology / Process | Y/N | Keep / Condense / Move |

### Phase 3 — Reorganization
**Tier 1 (read in 2 more sentences):**
- <point 1>
- <point 2>

**Tier 2 (read in 3+ paragraphs):**
- <point 3>
- <point 4>

**Tier 3 (appendix or end):**
- <detail 1>

### Phase 4 — Verification
**First paragraph (stand-alone test):**
<Can it be understood without reading further? Y/N>

**First-sentence skim (coherent argument):**
<Does argument track from top to bottom? Y/N>

### Strengths
- <what the document does well>

### Recommendations
1. <reordering, condensing, or cutting>
2. <...>

### Confidence
<high/medium/low> — <justification>
```
