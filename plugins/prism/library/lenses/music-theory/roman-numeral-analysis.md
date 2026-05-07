---
name: roman-numeral-analysis
display_name: Roman Numeral Analysis
class: lens
underlying_class: native
domain: music-theory
source: Rameau (Traité de l'harmonie, 1722); formalized in 19th-century pedagogy (Richter, Piston)
best_for:
  - Analyzing harmonic function in tonal music
  - Teaching chord progressions and voice leading
  - Identifying structural patterns in classical and contemporary compositions
one_liner: "Analyze functional harmonic roles via Roman numerals to grasp tonal structure."
---

# Roman Numeral Analysis

## Overview
Roman numeral analysis encodes the harmonic function of chords within a key using scale-degree notation (I, IV, V, etc.). Each numeral signals both the chord's pitch content and its role in the tonal hierarchy — I is tonic (home), V is dominant (tension), IV is subdominant (preparation). Practitioners use this lens to reverse-engineer the underlying harmonic grammar of a passage, identify deviations from expected progressions, and teach why certain voice-leading sequences feel inevitable or jarring. The discipline is precision: a chord labeled ii instead of IV has a different function, even if the notes overlap.

## Analytical Procedure

### Phase 1 — Establish Tonal Center and Key

1. **Determine the key.** Listen for the tonic pitch (the note that feels like "home" when held). If the passage is ambiguous, check the first and last chords — these often establish tonality. Write the key in the format: Major or Minor (e.g., C Major, G Minor).

2. **Build the scale in that key.** Write out the seven scale degrees (1–7) in order. For major keys, use the major scale. For minor keys, specify which minor (natural, harmonic, or melodic) based on the accidentals in the passage.

3. **Map every chord to its root.** For each chord in the passage, identify its root note and count its distance from the tonic in scale degrees. A root on the second scale degree = ii (or II if major).

### Phase 2 — Classify Chords by Inversion and Quality

4. **Identify the inversion.** 
   - Root position (root in bass): use the numeral alone (V).
   - First inversion (third in bass): add superscript 6 (V⁶).
   - Second inversion (fifth in bass): add superscript 6/4 (V⁶₄).
   - If unsure, write out the interval between bass and highest note; if it's a third and sixth, it's first inversion.

5. **Mark the chord's quality.** 
   - Roman numerals for major chords (I, IV, V in major keys).
   - Lowercase for minor chords (ii, iii, vi in major keys; i, iv, v in minor keys).
   - Diminished chords get a ° symbol (vii°).
   - Augmented chords get a + symbol (III+ if it occurs).
   - Seventh chords and extensions: add 7 (V7), 9 (V9), etc. Place the symbol after the numeral (V⁶₇ for V7 in first inversion).

6. **Check the pitch content against the numeral.** Does the chord match the expected pitches for that scale degree? If not, mark it as an alteration (e.g., V♯ if the fifth is raised, or note that this is a borrowed chord from the parallel minor).

### Phase 3 — Trace Function and Progression Logic

7. **Label the harmonic function of each chord.**
   - **Tonic (I, vi):** stability, resolution, "home."
   - **Subdominant (IV, ii):** preparation, movement away from home.
   - **Dominant (V, vii°):** tension, expectation of return to tonic.
   - **Secondary dominants (V/ii, V/IV, etc.):** temporary tension pointing to a chord other than tonic.
   - Write the function below or beside the numeral.

8. **Map the progression as a sequence of functions.** Write the entire passage as a string of functions (e.g., T – S – D – T). This reveals the underlying harmonic rhythm independent of specific chords.

9. **Identify any deviations or special moves.**
   - **Deceptive cadence:** V resolves to vi instead of I. Write as V → vi (deceptive).
   - **Borrowed chords:** chords from the parallel key (e.g., iv in C Major, borrowed from C Minor). Mark with a note.
   - **Modulation:** the key changes. Note the pivot chord or the moment tonality shifts, and re-analyze the passage in the new key.
   - **Chromatic alterations:** V♯, iv♯, etc. Explain what the alteration does (e.g., "makes the leading tone sharper, strengthening the approach to the tonic").

### Phase 4 — Evaluate Against Voice-Leading Rules

10. **Check for parallel fifths and octaves.** Track the outer voices (soprano and bass) between consecutive chords. If they move by the same interval in the same direction, mark it (e.g., "parallel fifths between I and IV"). Context matters; some styles tolerate them.

11. **Verify smoothness of voice leading.** For each of the four voices (SATB if applicable), do notes move by step or small leap? Large jumps should be justified (e.g., bass motion that outlines the harmonic function).

12. **Check resolution of chord tones.** 
   - Sevenths in dominant chords (V7) should resolve down by step.
   - Leading tones (scale degree 7 in major, or raised 7 in minor) should resolve up to the tonic.
   - Suspensions should resolve to the expected chord tone.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Tonal center established and key written explicitly | Y/N |
| All chords identified by root and mapped to scale degree | Y/N |
| All inversions correctly noted (root position, ⁶, or ⁶₄) | Y/N |
| All chord qualities (major, minor, ○, +) marked accurately | Y/N |
| Harmonic functions assigned (T, S, D) to all chords | Y/N |
| Deviations (deceptive, borrowed, modulation) identified and noted | Y/N |
| Voice-leading checked for fifths/octaves and smoothness | Y/N |
| Seventh and suspension resolutions verified | Y/N |

## Red Flags

- The key is unclear and oscillates between two candidates. Re-listen for the tonic; if still ambiguous, state the ambiguity and analyze both keys in parallel.
- Chords are labeled by note names ("Dm, G, C") instead of scale degrees. This defeats the purpose — the analyst has skipped the functional mapping.
- Inversions are ignored (all chords marked as root position). This hides bass motion and functional clarity; re-examine the score.
- Borrowed chords are labeled as if they belong to the key without notation. Mark them explicitly (e.g., iv from C Minor borrowed into C Major).
- Voice leading has many parallel fifths or octaves but is unmarked. Either the style tolerates them (note this context) or there is an error in the harmonic reading.
- A "V" is followed directly by "vi" without acknowledgment that this is deceptive. Name the cadence; it's a structural signal.
- Modulations are present but the second key is analyzed in the first key's numerals. Reanalyze in the new key once it is established.

## Output Format

```
## Roman Numeral Analysis

**Key:** <Major or Minor>

**Scale degrees:** 1 (tonic), 2, 3, 4, 5, 6, 7

### Chord-by-Chord Breakdown
| Measure | Chord (notation) | Root | Numeral | Inversion | Quality | Function | Notes |
|---|---|---|---|---|---|---|---|
| 1 | C | C | I | root | major | Tonic | — |
| 2 | F | F | IV | root | major | Subdominant | — |
| 3 | G | G | V | root | major | Dominant | — |
| 4 | C | C | I | root | major | Tonic | — |

### Harmonic Progression (function sequence)
T – S – D – T

### Deviations and Special Moves
- Measure X: <description of deceptive cadence, borrowed chord, modulation, etc.>

### Voice-Leading Check
- Parallel fifths: <none | location and context>
- Parallel octaves: <none | location and context>
- Seventh resolutions: <all correct | location of error>
- Suspension resolutions: <all correct | location of error>
- Overall smoothness: <high | moderate | low> — <justification>

### Confidence
<high | medium | low> — <justification based on key clarity, chromatic complexity, style conventions, or ambiguities encountered>
```
