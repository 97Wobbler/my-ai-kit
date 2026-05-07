---
name: progressive-summarization
display_name: Progressive Summarization
class: lens
underlying_class: native
domain: personal-knowledge-management-pkm
source: Tiago Forte, Building a Second Brain (2022)
best_for:
  - Extracting signal from long-form content without losing context
  - Training attention and pattern recognition through layered refinement
  - Creating reusable knowledge assets from raw captures
one_liner: "Progressively compress source → bold → highlight → summary → expression."
---

# Progressive Summarization

## Overview

Progressive Summarization is a technique for distilling knowledge through repeated passes over source material, each pass extracting a denser, more actionable layer. Rather than summarizing once (which loses nuance and forces premature interpretation), the method applies four refinement layers—bolding key phrases, highlighting the boldest material, writing a summary of highlights, and finally expressing the distilled insight in your own terms—building a trail of breadcrumbs from raw source to actionable principle. Practitioners use this when working with articles, research, videos, or notes that contain signal worth keeping but are too bulky for immediate use.

## Analytical Procedure

### Pass 1 — Bolding

1. **Read or consume the source material end-to-end without taking action.** Let it settle. Do not highlight or annotate during this pass.

2. **Re-read the material.** This time, **bold any phrase, sentence, or short passage** that feels relevant to your current project or question. Bold is the coarsest filter—if you'd mention it to someone, bold it.

3. **Record your selection criterion explicitly.** Write one sentence: "I bolded X because ___" (e.g., "I bolded X because it relates to how users perceive onboarding friction").

4. **Review what you bolded.** Does it form a coherent spine? If more than 50% of the material is bolded, you have not filtered—reset and bold only the top 10-20% by relevance.

### Pass 2 — Highlighting

5. **Wait at least one day.** Fresh context reduces false positives. Return to the material with your bolded passages visible.

6. **Highlight only the boldest material.** Of everything you bolded, which phrases are *essential*? Highlight only those—typically 50% of what you bolded, or the top 5-10% of the original source.

7. **Note any patterns or connections.** As you highlight, jot down 1-2 observations in the margin: "This connects to X" or "This contradicts my assumption that Y."

### Pass 3 — Summary

8. **Write a summary of *only the highlighted passages*.** Do not reference the source directly. Use your own words. The summary should be 1-3 short paragraphs and answer: "What is the core insight here, and why did I flag it?"

9. **Check the summary for jargon.** If it uses terms from the source without defining them, rewrite. The summary should be readable to someone unfamiliar with the original material.

### Pass 4 — Expression

10. **Translate the summary into a concrete form relevant to your work.** This might be:
    - A principle you'll apply (e.g., "When designing forms, batch related fields to reduce cognitive load")
    - A question to revisit (e.g., "How does this pattern apply to our notification system?")
    - A decision rule (e.g., "If X, then do Y")
    - A hypothesis to test (e.g., "Removing step Z will increase adoption by ~15%")

11. **Make it actionable.** If someone hands you this expression without the source, could they use it? If not, rewrite.

12. **Cite the source and layer depth.** Note which pass produced this expression (Pass 4) and link back to the source material.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Pass 1: Bolded material is 10–20% of source length | Y/N |
| Pass 1: Selection criterion is explicit and defensible | Y/N |
| Pass 2: Highlighted material is ~50% of bolded content | Y/N |
| Pass 2: At least one margin connection noted | Y/N |
| Pass 3: Summary is jargon-free and uses own words | Y/N |
| Pass 3: Summary is 1–3 paragraphs (not longer) | Y/N |
| Pass 4: Expression is concrete and actionable | Y/N |
| Pass 4: Source and layer depth are cited | Y/N |

## Red Flags

- No bolding done. The material was passively consumed but not interrogated for relevance.
- Pass 1 bolding exceeds 50% of source. The filter is broken — every line feels important, which means nothing is.
- Pass 2 highlighting is not a strict subset of bolding. Highlighting introduced new material instead of refining what was already bolded.
- Pass 3 summary is longer than the original source, or repeats source language verbatim. No compression or translation happened.
- Pass 4 expression is still generic (e.g., "This is important for user experience"). It cannot guide a decision or action.
- No margin connections recorded. The passes were mechanical — no thinking occurred.
- The four passes collapsed into one (all done in a single sitting). Spacing enables the filter to work; rushing defeats it.

## Output Format

```
## Progressive Summarization Report

**Source:**
<Title, Author, Date, Link or Citation>

**Selection criterion (Pass 1):**
<One sentence: why this material was approached>

### Pass 1 — Bolded Material
<Bolded passages or a short list of boldface key phrases>
Length: _% of source

### Pass 2 — Highlighted Passages
<Highlighted subset, or list of most essential phrases>
Margin connections:
- <Observation 1>
- <Observation 2>

### Pass 3 — Summary
<1–3 paragraphs in own words, summary of only the highlighted material>

### Pass 4 — Expression
**Form:** [Principle | Question | Decision Rule | Hypothesis | Other: ___]

<Concrete, actionable statement. If someone reads only this, they can use it.>

**Cited layer depth:** Pass 4 (final)
**Link to source:** <URL or reference>

### Confidence
<high | medium | low> — <Justification: was the source material fresh enough to filter accurately? Did the four passes feel mechanically sound, or rushed? Did Pass 4 output feel crisp and usable, or loose and generic?>
```
