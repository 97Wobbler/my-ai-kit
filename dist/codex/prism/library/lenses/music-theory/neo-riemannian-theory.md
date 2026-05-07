---
name: neo-riemannian-theory
display_name: Neo-Riemannian Theory
class: lens
underlying_class: native
domain: music-theory
source: Hugo Riemann (19th century harmonic function); formalized by David Lewin (Generalized Interval Systems, 1987); extended by Henry Klumpenhouwer and Richard Cohn (1990s)
best_for:
  - Mapping harmonic relationships between chords without functional tonality
  - Analyzing smooth voice-leading in chromatic or post-tonal music
  - Understanding chord progressions as geometric transformations
one_liner: "Define musical distance by minimal voice leading between chords."
---

# Neo-Riemannian Theory

## Overview

Neo-Riemannian Theory treats chords as points in abstract space and harmonic progressions as geometric transformations. Instead of analyzing chords through functional harmony (tonic, dominant, subdominant), it maps relationships between chords using three minimal transformations—Parallel (P), Leittonwechsel (L), and Relative (R)—each preserving two of three pitches while changing one by semitone. Practitioners use this lens when traditional functional analysis breaks down, when analyzing chromatic composers (Wagner, Ravel, contemporary film scores), or when smooth voice-leading is compositionally more important than harmonic function.

## Analytical Procedure

### Phase 1 — Identify Chord Inventory

1. **List all triads in the passage.** Use root-position or first-inversion notation consistently. Include both major and minor triads, noting enharmonic equivalents (C♯ major = D♭ major) as a single entity.

2. **Represent each triad as a pitch class set.** For a triad on root R, major or minor, note its three component pitch classes modulo 12. Example: C major = {0, 4, 7}; C minor = {0, 3, 7}.

3. **Identify the triad type.** Mark each as:
   - **Maj** (major triad)
   - **Min** (minor triad)
   - **Aug** (augmented triad, if present)
   - **Dim** (diminished triad, if present)

### Phase 2 — Map Transformations Between Adjacent Chords

For each pair of consecutive chords in the passage, identify which transformation(s) connect them.

4. **Test for Parallel (P) transformation:**
   - P maps a major triad to its parallel minor (same root, mode change).
   - P maps a minor triad to its parallel major.
   - Check: Does the root stay the same? Do exactly two pitches remain unchanged?
   - Example: C major {0, 4, 7} → C minor {0, 3, 7}. Pitches 0 and 7 preserved; 4 drops to 3.
   - Mark: **P** if yes.

5. **Test for Leittonwechsel (L) transformation:**
   - L exchanges the root and a pitch one semitone apart (typically the third).
   - L maps major to major or minor to minor (mode preserved).
   - Check: Does the fifth stay the same? Do the root and third swap such that one drops and one rises by semitone?
   - Example: C major {0, 4, 7} → B major {11, 3, 7}. Fifth (7) preserved; C→B and E→F♯ (enharmonic to B).
   - Mark: **L** if yes.

6. **Test for Relative (R) transformation:**
   - R maps a major triad to its relative minor (or vice versa).
   - R exchanges the root and fifth while preserving the third.
   - Check: Does the third stay the same? Do the root and fifth swap positions within the set?
   - Example: C major {0, 4, 7} → A minor {9, 0, 4}. Third (4) preserved; C↔A, E↔E, G↔C.
   - Mark: **R** if yes.

7. **For each chord pair, write the transformation label and the pitches preserved.** If no transformation connects the pair, mark it as **non-PLR** and note which pitches moved and by how much (in semitones).

### Phase 3 — Analyze Voice-Leading Efficiency

8. **Count total semitone movement** for each transformation in the passage. For P, L, R, typically only one pitch moves one semitone. For non-PLR moves, sum the absolute semitone distances.

9. **Compare smooth vs. disjunct passages.** Regions dominated by P, L, R should show minimal voice-leading cost. Regions with large jumps or non-PLR moves indicate harmonic disruption or functional shifts (e.g., cadences, modulations).

10. **Map the progression as a path in the Tonnetz (tonal network).** Optionally, visualize the sequence as a traversal:
    - Plot major triads in one color and minor triads in another.
    - Draw arrows labeled P, L, or R between chords.
    - Closed loops or revisiting nodes may indicate harmonic cycles (e.g., mediant cycles common in film scores).

### Phase 4 — Evaluate Structural Function

11. **Identify passage type:**
    - **Tonal functional** (clearly V→I, IV→V, etc.): Often requires non-PLR moves; check if P/L/R is avoided.
    - **Smooth chromatic** (dominated by P/L/R): Suggests voice-leading primacy over function.
    - **Hybrid** (mixes both): Analyze zones separately.

12. **Note contextual anomalies.** If a passage is otherwise smooth but contains a non-PLR jump, ask: Is this a cadential gesture? A register shift? A modal pivot? Mark these for interpretation.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All triads identified and pitch-class sets written correctly (mod 12) | Y/N |
| Each chord pair tested against P, L, and R definitions | Y/N |
| Transformation labels include pitches preserved (not assumed from definition) | Y/N |
| Non-PLR moves are quantified in semitones and explained contextually | Y/N |
| Voice-leading cost comparison distinguishes smooth vs. disjunct passages | Y/N |
| Passage type (tonal functional / smooth chromatic / hybrid) is assigned with justification | Y/N |

## Red Flags

- Every chord pair maps to exactly one of P, L, R with no alternatives. This is unlikely unless the composer explicitly designed for it; re-check inversions and enharmonic spellings.
- Non-PLR moves exist but are not explained. They may indicate analytical error (wrong triad identification), compositional ambiguity, or missing context (e.g., passing chords).
- The analysis finds P/L/R everywhere but the passage *sounds* tonal and functional. This suggests misidentifying the passage type; functional harmony may override voice-leading smoothness.
- Pitch-class sets are written in unconventional order or enharmonic confusion arises (G♯ vs. A♭). Standardize to ascending order from C=0 for clarity.
- Voice-leading cost is never summed; transformations are noted but not compared to judge smoothness. Without quantification, the lens is descriptive only.

## Output Format

```
## Neo-Riemannian Analysis

**Passage:** <Composer, work, measure range, key context>

### Chord Inventory
| Measure | Chord | Root | Type | Pitch Classes |
|---|---|---|---|---|
| <...> | <...> | <...> | Maj/Min | <{pitch set}> |

### Transformations
| From | To | Transformation | Pitches Preserved | Semitones Moved |
|---|---|---|---|---|
| <chord> | <chord> | P/L/R/non-PLR | <which ones> | <...> |

### Voice-Leading Cost
- P/L/R moves: _ (1 semitone each, typical)
- Non-PLR moves: <total semitones>
- Total voice-leading cost: _ semitones

### Passage Type
<Tonal functional / Smooth chromatic / Hybrid>
Justification: <...>

### Structural Observations
1. <Any cycles, reversals, or anomalies>
2. <Relationship to form, cadences, or modulation>
3. <Comparison to surrounding passages if relevant>

### Confidence
<high/medium/low> — <justification: e.g., "high because all triads are diatonic and no inversions complicate pitch-class analysis; medium if extended tertian or added-tone chords are present; low if passage is non-triadic or functional analysis more salient than voice-leading.">
```
