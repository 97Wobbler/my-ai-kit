---
name: rhythmic-analysis
display_name: Rhythmic Analysis
class: lens
underlying_class: native
domain: music-theory
source: Music theory pedagogy (Lerdahl & Jackendoff, *A Generative Theory of Tonal Music*, 1983); metric grouping analysis (Yeston, 1976)
best_for:
  - Identifying tension between notated meter and perceived grouping
  - Analyzing syncopation and rhythmic displacement in compositions
  - Evaluating whether a passage's metrical stress aligns with its structural phrasing
one_liner: "Map tension between score meter and musical grouping and analyze rhythmic regions."
---

# Rhythmic Analysis

## Overview
Rhythmic Analysis maps the relationship between notated meter (the time signature and downbeat structure) and perceived grouping (how the composition's phrasing, accents, and melodic units actually organize the pulse). When these two systems align, the music feels stable. When they conflict, tension emerges—sometimes productively (syncopation, hemiola, cross-rhythm) and sometimes as compositional error. Practitioners use this lens when a passage sounds rhythmically unstable, when they need to diagnose why a performer's interpretation creates drag or lift, or when analyzing how a composer generates momentum through metric ambiguity.

## Analytical Procedure

### Phase 1 — Establish the Notated Meter

1. **Identify the time signature** and write it clearly. If the signature changes, note each change and its measure number.

2. **Mark the downbeats and metrical hierarchy.** For a 4/4 measure:
   - Primary stress: beat 1
   - Secondary stress: beat 3
   - Weak beats: 2, 4
   
   For compound meters (6/8, 9/8, 12/8), identify whether the ear naturally groups them as two or three beats per measure.

3. **Write out one full bar of the notated meter on staff paper or in a grid.** Label each beat and subdivision. This becomes your reference grid.

### Phase 2 — Extract the Perceived Grouping

4. **Listen to the passage (if audio is available) or imagine its performance.** Do not rely solely on notation—your ear and body matter. Tap along and feel where the accents fall.

5. **Identify the structural downbeats by ear.** These are points where the melody, harmony, or texture initiates a new phrase or gesture. Mark them on the score with a bracket or label.

6. **Measure the distance between perceived structural downbeats in beats or eighth-notes.** If the structure groups in fours but the meter is in threes, note that explicitly.

7. **List all salient accents in the passage:**
   - Dynamic accents (marked as `>` or `mf` after `p`)
   - Melodic accents (leap, registral peak, longer note duration)
   - Harmonic accents (chord change, cadence, harmonic motion)
   - Registral accents (highest or lowest note in a phrase)
   
   Mark the beat each accent lands on.

### Phase 3 — Map the Conflict

8. **For each structural downbeat identified in Phase 2, determine which notated beat it falls on.** Create a table:

   | Structural Downbeat | Notated Beat | Metrical Status |
   |---|---|---|
   | Phrase 1 start | 1 | On-beat (aligned) |
   | Phrase 2 start | 3 | On-beat (aligned) |
   | Phrase 3 start | 2+ | Off-beat (syncopated) |

9. **Classify the type of rhythmic tension:**
   - **Aligned**: Structural downbeat falls on a primary or secondary metrical stress.
   - **Syncopated**: Structural downbeat falls between beats or on a weak beat.
   - **Hemiola**: Two groupings of three replace three groupings of two (or vice versa) for one or more bars.
   - **Cross-rhythm**: Two independent metrical layers sound simultaneously (e.g., 3 against 4).
   - **Anacrusis**: Phrase begins before the notated downbeat (upbeat structure).

10. **Measure the *consistency* of the grouping.** Does the perceived meter shift mid-passage or remain stable? If it shifts, mark the measure where the shift occurs.

### Phase 4 — Assess Function

11. **Determine the compositional or interpretive purpose of the tension:**
    - Is it intentional (creating drive, emphasis, or surprise)?
    - Is it unintentional (a misalignment between notation and effect)?
    - Does it serve a structural function (e.g., building energy into a cadence)?
    - Does it reflect performance choice (rubato, swing, articulation)?

12. **Check for resolution.** If tension is created, does the passage later return to metrical alignment? Mark the measure where resolution occurs (if any).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Notated meter is identified and one bar is transcribed as reference | Y/N |
| Structural downbeats are marked by ear, not inferred from notation alone | Y/N |
| Accent table lists dynamic, melodic, harmonic, and registral accents with beat locations | Y/N |
| Alignment/conflict table maps all major perceived downbeats to notated beats | Y/N |
| Tension is classified into one of five types (aligned, syncopated, hemiola, cross-rhythm, anacrusis) | Y/N |
| Purpose assessment distinguishes intentional from unintentional tension | Y/N |
| If tension is present, resolution point is identified or noted as unresolved | Y/N |

## Red Flags

- Perceived grouping is inferred entirely from notation without listening or physical response. Rhythmic analysis that skips the ear is notation analysis, not rhythm analysis.
- The accent table is empty or lists only dynamic markings. Melodic and harmonic accents often carry more weight than markings.
- Structural downbeats are spaced at arbitrary intervals (e.g., every 4 beats) with no justification. Structural boundaries exist because the music articulates them, not because the meter prescribes them.
- Alignment/conflict table shows no conflicts or tension. Every passage has some degree of polyrhythmic play; if none appears, the analysis stopped too early or the passage is genuinely trivial (which should be stated).
- Purpose assessment assumes all tension is intentional without considering whether it arises from performance practice, notation limitations, or compositional error.
- Tension is named (e.g., "hemiola") but never mapped to specific beats. Naming without location is vague.

## Output Format

```
## Rhythmic Analysis Report

**Passage:** <Composer, work, measure range>
**Time signature:** <e.g., 4/4, 6/8>

### Notated Meter Reference
<One bar of the meter with beats and stresses labeled>

### Structural Downbeats (by ear)
- Phrase 1: <start measure, description>
- Phrase 2: <start measure, description>
- ...

### Accent Inventory
| Beat Location | Type | Source | Effect |
|---|---|---|---|
| 1.2+ (beat 2, eighth-note off) | Dynamic | `>` marking | Weak metrical beat, strong accent |
| 2.1 (beat 1 of measure 2) | Melodic | Registral peak | Aligns with metrical stress |
| 3.3 (beat 3, third eighth) | Harmonic | V–I cadence | Off-beat; creates syncopation |

### Alignment & Conflict Map
| Structural Downbeat | Notated Beat | Classification |
|---|---|---|
| Phrase 1 (m. 1) | 1 | Aligned |
| Phrase 2 (m. 5) | 2+ | Syncopated |
| Phrase 3 (m. 9) | 3 | Syncopated |

### Rhythmic Tension Analysis
**Type:** <Syncopation / Hemiola / Cross-rhythm / Anacrusis / Aligned>
**Consistency:** <Stable throughout / Shifts at m. X>
**Resolution:** <Resolves at m. X / Unresolved / N/A>

### Compositional Purpose
<Intentional or unintentional; structural function if present; interpretation role if performance-based>

### Confidence
<high/medium/low> — <justification, e.g., "high — passage has clear structural markers and audible accents that were cross-verified against notation" or "medium — anacrusis is implied but not definitively marked; performer interpretation may vary">
```
