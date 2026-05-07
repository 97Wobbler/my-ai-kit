---
name: motivic-analysis
display_name: Motivic Analysis
class: lens
underlying_class: native
domain: music-theory
source: Heinrich Schenker (Der freie Satz, 1935); systematized in 20th-century music analysis (Forte, Meyer, Caplin)
best_for:
  - Tracking thematic material through transformation and recurrence
  - Identifying structural coherence in multi-movement works
  - Distinguishing motivic variation from genuine new material
one_liner: "Track the transformation and recurrence of motifs to verify a work's unity."
---

# Motivic Analysis

## Overview
Motivic analysis isolates the smallest discrete units of melodic or rhythmic identity in a composition, then systematically traces their transformations, recurrences, and structural functions across the work. A motif is the minimal identifiable unit — usually 2–4 pitches or a characteristic rhythm — that persists even when transposed, inverted, augmented, or fragmented. Practitioners use this lens when they suspect a work has coherence (unity through material reuse) but need to verify it and map *how* that reuse operates. It separates structural weight from coincidence: does a repeated shape matter, or is it just surface similarity?

## Analytical Procedure

### Phase 1 — Motif Identification

1. **Listen or read the score from beginning to end without annotation.** Note which melodic or rhythmic shapes "stick" — appear multiple times or feel thematically important. Do not yet mark them formally.

2. **Choose the opening phrase (typically 4–8 bars).** This is your first candidate pool. Extract the smallest units that feel self-contained:
   - A pitch sequence (e.g., scale fragment, skip-and-fill shape)
   - A rhythmic pattern (e.g., dotted rhythm, syncopation, note-length ratio)
   - A combination (pitch + rhythm together)
   
   Do *not* treat the entire opening as one motif. The goal is granularity — the building blocks.

3. **For each candidate, assign a label** (e.g., "Motif A — rising third + quarter-note rhythm"). Transcribe it as a note sequence or rhythm notation. This is your reference form.

4. **Define the "essential identity" of each motif.** Which elements can change without losing recognition? For instance:
   - Can it transpose? (Usually yes.)
   - Can it invert? (Sometimes.)
   - Can it fragment (use only part of it)? (Often yes.)
   - Can it augment (lengthen note values)? (Depends on context.)
   
   Write this down as constraints. Example: "Motif A survives transposition and fragmentation but not inversion."

### Phase 2 — Occurrence Mapping

5. **Scan the entire work bar-by-bar.** Every time you encounter a form of each motif (transposed, inverted, fragmented, or exact), mark its location and transformation type. Use a table:

   | Bar(s) | Motif | Form | Context | Instrumentation |
   |---|---|---|---|---|
   | 1–4 | A | exact | melody | violin |
   | 12–14 | A | transposed up M2 | countersubject | viola |
   | 28–29 | A | fragmented (first 2 notes only) | accompaniment | cello |

6. **Distinguish echo from development.** A motif that appears twice in quick succession (same bar or adjacent bars) is an *echo* — often a rhetorical device, not necessarily structural material. Mark it but note the proximity. A motif that recurs after a section break or developmental passage is *structural reuse*.

7. **Track combinations.** If two motifs appear simultaneously (overlapped, interlocked, or vertically stacked), record this as a composite. Example: "Bar 45: A in soprano + B in bass, new texture."

### Phase 3 — Structural Weight Assessment

8. **Count occurrences by category:**
   - Exact recurrences
   - Transposed forms
   - Inverted forms
   - Fragmented forms
   - Combinations with other motifs
   
   A motif that appears in every section of the work (exposition, development, recapitulation, coda) has higher structural weight than one confined to one section.

9. **Examine density and timing.** Is the motif densely clustered in the opening, then sparse? Or does it return after long silence? Dense reappearance often signals thematic unity; sparse reappearance can signal a structural boundary or recall. Log the pattern.

10. **Check for motivic hierarchy.** Does one motif "contain" another? Does the opening motif fragment into smaller repeating shapes? Rank them by prevalence:
    - **Primary** — pervasive, appears in most sections
    - **Secondary** — significant but localized to certain movements/sections
    - **Tertiary** — episodic, appears once or twice as accent

### Phase 4 — Coherence Verification

11. **Identify sections where *no* primary motifs appear.** Are there passages of new material, or is the composer resting the primary motifs? If new material dominates, the work may lack motivic unity. If the primary motifs are absent but secondary motifs fill the space, note this pattern.

12. **Examine the recapitulation (or final return).** Does the composer restore the primary motifs in recognizable form, or does development continue? This distinction (formal return vs. continuous development) is diagnostic of the work's overall architecture.

13. **Audit the coda.** Is it built from motifs, or does it introduce new material? A motif-based coda reinforces coherence; new material in the coda can signal collapse of unity or a new phase.

## Evaluation Criteria

| Check | Pass |
|---|---|
| At least 3 distinct motifs identified from opening phrase | Y/N |
| Each motif has an explicit "essential identity" definition (what can change) | Y/N |
| All occurrences in the work logged in a table with bar numbers and transformation type | Y/N |
| Motifs classified as Primary/Secondary/Tertiary by prevalence | Y/N |
| At least one section analyzed for absence/presence of primary motifs | Y/N |
| Recapitulation or final return examined for motif restoration | Y/N |
| Coherence verdict issued: high/medium/low based on motif density and recurrence | Y/N |

## Red Flags

- Every distinct phrase is labeled a new motif. True motifs recur; if a shape appears once, it is not a motif, it is a unique idea.
- The "essential identity" is so broad that unrelated shapes qualify (e.g., "any descending scale"). The definition collapses distinctions; tighten it.
- Motif identifications change mid-analysis (Bar 20: "Motif A transposed" but Bar 40: "similar shape, different motif"). Consistency is essential. If a shape matches the essential identity, it is the same motif.
- The work has no primary motifs (all tertiary or episodic). Either the work is genuinely non-motivic (possible in some post-tonal or aleatoric music), or the analysis missed structural material.
- Recapitulation section is never examined. This is the moment the work declares whether it achieved unity or not — skipping it voids the assessment.
- Confidence is high despite sparse occurrence data (only 2–3 bars of material examined). Thorough motif analysis requires scanning the *entire* score.

## Output Format

```
## Motivic Analysis Report

**Work:**
<Title, Composer, Movement (if applicable)>

**Duration / Scope:**
<total bars analyzed>

### Motif Inventory

| Label | Pitch Shape | Rhythm | Essential Identity | First Appearance |
|---|---|---|---|---|
| A | <notation or description> | <notation> | Survives: transposition, fragmentation; not: inversion | Bar(s) |
| B | ... | ... | ... | ... |

### Occurrence Map

| Bar(s) | Motif | Form | Context | Count (this form) |
|---|---|---|---|---|
| 1–4 | A | exact | opening melody | 1 |
| 12–14 | A | transposed up M2 | countersubject | 1 |
| ... | ... | ... | ... | ... |

### Motif Hierarchy

**Primary:** A (appears in exposition, development, recapitulation, coda; 12 total occurrences)

**Secondary:** B (appears in exposition and coda; 4 occurrences)

**Tertiary:** C (episodic, 2 occurrences in development only)

### Structural Observations

**Density:** <high/moderate/low> — motifs recur in <X>% of bars

**Recapitulation:** Motifs A and B restored in recognizable form at bar [X]; development continues into coda.

**Coda:** Built primarily from motif A, closing section features [description].

**Sections without primary motifs:** None / <list sections>

### Coherence Assessment

The work achieves <high/medium/low> motivic coherence through systematic reuse and transformation of <X> primary motifs across <Y> sections. The recurrence pattern <supports/undermines> structural unity.

### Confidence
<high/medium/low> — <justification based on completeness of scan, clarity of motif definitions, and density of occurrence data>
```
