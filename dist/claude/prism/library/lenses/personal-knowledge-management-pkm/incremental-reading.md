---
name: incremental-reading
display_name: Incremental Reading (SuperMemo)
class: lens
underlying_class: native
domain: personal-knowledge-management-pkm
source: Piotr Wozniak (SuperMemo algorithm), 1987
best_for:
  - Retaining high-volume source material without rereading entire texts
  - Balancing breadth and depth in knowledge acquisition
  - Detecting when a text deserves deeper study vs. abandonment
one_liner: "Split large texts into fragments for repeated exposure, dynamically adjusting depth by interest."
---

# Incremental Reading (SuperMemo)

## Overview

Incremental reading breaks long texts into small, self-contained chunks and exposes you to each chunk multiple times over expanding intervals (1 day, 3 days, 7 days, etc.), prioritizing chunks by relevance and retention difficulty. Rather than read a 50-page paper once, you read page fragments in parallel with dozens of other sources, resurfacing high-value chunks repeatedly while dropping low-value ones early. Practitioners use it when managing sources faster than they can deeply learn them — the goal is to maximize signal extracted per unit time, not to achieve mastery of every source.

## Analytical Procedure

### Phase 1 — Source Intake

1. **Collect the source material (article, book chapter, research paper, long-form post).** Write down: source URL/citation, estimated length in words, domain (technical, narrative, reference), and your initial urgency (high/medium/low). Do not begin reading yet.

2. **Skim the material in 2–3 minutes.** Read only: title, subheadings, first paragraph, last paragraph, and any bolded/highlighted text. Produce a one-sentence summary of the core claim or topic.

3. **Decide: "Is this worth incremental reading?"** Ask:
   - Will you return to this material in the next 6 months?
   - Does it contain concrete facts, methods, or perspectives you may need later?
   - Is it longer than 2000 words?
   
   If all three are yes, proceed to Phase 2. If no, read it straight through or discard it now.

### Phase 2 — Chunking and First Exposure

4. **Divide the source into 3–8 independent chunks**, each 200–400 words, ending at a natural boundary (end of paragraph or section). Chunks should stand alone — a reader seeing only one chunk should understand its main point. Write a label for each chunk: "Section 3: Mechanisms of X" or "Objection and response."

5. **For each chunk, extract one question or gap.** This is the *entry point* — the thing you don't yet understand or want to remember about this chunk. Write it down. Examples:
   - "How does this evidence contradict the mainstream view?"
   - "What is the practical implication of this mechanism?"
   - "What would I tell someone who asked about this?"
   - Bad entry points: "What is this section about?" (too vague) or "I should memorize all the details" (too ambitious).

6. **Read the chunk. As you read, mark:**
   - **Retain** — a sentence or phrase you want to encounter again (1–2 per chunk).
   - **Clarify** — something you don't understand yet; re-read it and note what's unclear.
   - **Connect** — something that links to another source or concept; write the link.
   
   Do not try to memorize. You are reading to orient yourself, not to commit to memory.

7. **Schedule the chunk for re-exposure in 1 day.** (In a paper system: write it on a card and set it aside. In SuperMemo or Anki: tag it and set the interval.) Record: chunk label, date first read, and the entry point (the question from step 5).

### Phase 3 — Re-exposure and Filtering

8. **On the scheduled day, re-expose the chunk (read it again, 1–2 minutes).** Before re-reading, try to answer your entry-point question from memory. Then read the chunk.

9. **After re-exposure, judge the chunk:**
   - **Keep (promote):** The chunk answers your entry-point question or contains something you want to see again. Schedule it for 3 days out.
   - **Modify:** The question was wrong or the chunk is less relevant than you thought. Rewrite the entry point or split the chunk into smaller pieces. Schedule one of the pieces for 3 days out; discard the rest.
   - **Drop:** You've now read it twice and don't see why you'd need it again. Remove it from the rotation.
   
   You should drop 30–50% of chunks by the second exposure. If you're keeping everything, your entry points are too vague or your chunks are too broad.

10. **For chunks marked "Keep," apply spaced repetition.** Schedule each promoted chunk for increasingly distant reviews:
    - 1st read: today
    - 2nd read: +1 day
    - 3rd read: +3 days
    - 4th read: +7 days
    - 5th read: +14 days
    - 6th read: +30 days
    
    If a chunk survives to the 30-day review, decide: "Will I ever need this again?" If yes, schedule it for 90 days. If no, retire it.

11. **On each re-exposure, ask: "What's new or surprising about this chunk compared to what I already know?"** Write down one concrete application or connection. This forces active processing instead of passive rereading.

### Phase 4 — Escalation and Integration

12. **If a chunk produces consistent surprises or connections across multiple re-exposures, escalate it.** Extract the key insight (one sentence) and migrate it into your permanent knowledge system (a wiki, note network, or list of "core ideas I've validated"). Record the source.

13. **If a chunk stops producing new connections by the 4th re-exposure, retire it.** You have extracted the signal; further exposure has diminishing returns.

14. **Track the sources as a whole.** Count: "Of the 8 chunks from Source A, how many survived to the 30-day mark?" Sources that yield high-retention chunks are your high-signal sources; sources that shed 70%+ are low-signal. Use this to shape future intake.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Source meets 3-question intake filter (return use, concrete facts, >2000 words) | Y/N |
| Chunks are 200–400 words and end at natural boundaries | Y/N |
| Each chunk has a single, answerable entry-point question | Y/N |
| Marks (Retain/Clarify/Connect) are present for first reading | Y/N |
| Re-exposure decisions (Keep/Modify/Drop) are made by day 1 review | Y/N |
| At least 30% of chunks are dropped by second exposure | Y/N |
| Escalated insights (step 12) are captured and sourced | Y/N |
| Retirement decisions are made (no chunks remain in rotation >90 days without escalation) | Y/N |

## Red Flags

- All chunks are retained through multiple cycles. Entry points are too generic, or you're optimizing for completion instead of signal.
- Chunks are larger than 400 words or don't end at natural boundaries. You're not actually chunking; you're just rereading the full source in pieces.
- No entry-point questions exist, or they are variations of "What is this about?" Re-exposure will be passive and produce no new connections.
- Sources accumulate without retirement. You're building a read-once pile, not a spaced-repetition system. If a chunk hasn't been scheduled past 30 days, it should be gone.
- More than 50% of chunks survive the second exposure. You're being too generous; the filter isn't working, and you'll overload your system.
- No integration into a permanent knowledge system. Chunks are reviewed but not escalated or connected to anything else. The signal is being lost.
- Entry-point questions are unanswered by the end of the final re-exposure. The chunk doesn't resolve what made it worth reading; drop it.

## Output Format

```
## Incremental Reading Assessment

**Source:**
- Title: <...>
- URL/Citation: <...>
- Length: <...> words
- Domain: <...>
- Urgency: high/medium/low

**Intake decision:** Keep / Drop (and reason)

### Chunks and Entry Points
| Chunk label | Words | Entry-point question | Retain marks | Clarify marks | Connect marks |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | <...> |

### Re-exposure Log
| Chunk | 1st read | 2nd read | 3rd read | Decision | Final status |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | Keep/Modify/Drop | Promoted/Retired |

### Escalations (chunks migrated to permanent knowledge system)
1. <chunk label> → <one-sentence insight>
2. <...>

### Source Signal Score
- Total chunks: <N>
- Survived to 30-day mark: <N> (<percent>)
- Escalated insights: <N>
- Signal rating: high / medium / low

### Confidence
<high/medium/low> — <justification. For example: "high — entry-point questions were specific and survived three exposures; 35% of chunks were retained, matching the expected filter rate. Two insights escalated to permanent knowledge. Source is high-signal." Or "low — unclear whether chunks were truly independent, or whether the 30-day interval will hold in practice.">
```
