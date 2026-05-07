---
name: voice-leading-rules
display_name: Voice Leading Rules
class: lens
underlying_class: native
domain: music-theory
source: Johann Joseph Fux (Gradus ad Parnassum, 1725); systematized in 19th-century pedagogy (Riemann, Prout)
best_for:
  - Evaluating melodic independence and harmonic smoothness in polyphonic writing
  - Identifying voice crossing, parallels, and registration problems
  - Teaching counterpoint and part-writing discipline
one_liner: "Rule system for maintaining voice independence and smooth interval motion."
---

# Voice Leading Rules

## Overview

Voice leading rules constrain how individual melodic lines move in relation to each other and to the underlying harmonic structure. They serve two functions: preserve the independence and singability of each line, and ensure harmonic progressions sound smooth and coherent. Practitioners apply them when writing counterpoint, four-part chorales, orchestral arrangements, or any texture where multiple simultaneous lines must cohere as a unified whole. The rules are not laws of nature; they are conventions that became rules because they reliably prevent listener confusion and performer difficulty.

## Analytical Procedure

### Phase 1 — Inventory the Voices

1. **Identify all distinct melodic lines in the score.** Write out the pitch sequence of each voice separately. If voices share the same staff (e.g., two soprano lines), extract them explicitly. Label each voice (Soprano, Alto, Tenor, Bass, or S1, S2, A, T, B, etc.).

2. **Mark all harmonic changes.** For each chord boundary in the progression, note the beat or measure number. Circle or highlight transitions where at least one voice changes pitch.

### Phase 2 — Evaluate Each Rule Category

#### Category A: Parallels and Unisons

3. **Check for perfect fifths and octaves.** For every adjacent pair of voices, scan each measure. When two voices move *simultaneously* from one note to another, check if both intervals are perfect (P5 or P8). 
   - If yes, mark it as "parallel fifths/octaves."
   - Exception: parallels are acceptable if the top voice moves by leap (non-step).
   - Exception: parallels in inner voices or bass-to-tenor are more tolerable than soprano-bass.

4. **Check for unison.** Scan for two voices sounding the same pitch simultaneously (not an octave above/below, but the identical pitch class). Mark all instances. Note: unison is acceptable in some contexts (dialogue, reinforcement) but problematic if it erases voice independence.

5. **Check for hidden fifths/octaves (direct fifths/octaves).** For soprano and bass only: if both voices move by leap to a perfect fifth or octave, mark it as "direct motion to P5/P8." This is a mild violation; tolerance depends on era and style.

#### Category B: Leaps and Melodic Shape

6. **Identify all leaps (intervals larger than a second).** For each voice, note every leap. After each leap, check if the melody fills in the leap by stepwise motion in the opposite direction within the next 1-3 steps.
   - If yes: leap is justified.
   - If no: mark as "unresolved leap."

7. **Check for large or awkward intervals.** Scan for leaps larger than a major sixth (except diminished sevenths, which are permitted in certain contexts). These are difficult for singers and rare in idiomatic writing. Mark any interval larger than a major 7th as "extreme leap."

#### Category C: Voice Range and Registration

8. **Confirm each voice stays within its typical range.** Use these standard ranges:
   - Soprano: C4–C5 (or higher in modern contexts)
   - Alto: G3–D5
   - Tenor: C3–A4
   - Bass: F2–D4
   Mark any notes that exceed these ranges by more than a third as "out of range."

9. **Check for voice crossing.** Scan each moment in time. Is the soprano ever lower than the alto? Alto lower than tenor? Tenor lower than bass? Mark all crossings. Context: light crossing (a single note) is tolerable; sustained crossing erases the harmonic definition.

#### Category D: Motion to/from Unison and Doubling

10. **Examine doublings at each harmony.** In each chord, identify which pitch classes appear and how many times. Note if the root, third, or fifth is doubled; whether a tendency tone is doubled (problematic); or if the chord is missing a necessary voice.

11. **Check motion into unison.** If two voices are at different pitches and move toward the same pitch, confirm they arrive by contrary or oblique motion, not parallel motion. Parallel motion into unison is historically acceptable but uncommon; mark for awareness.

#### Category E: Harmonic Rhythm and Pacing

12. **Measure rhythmic activity per voice.** Count the average number of note onsets per measure in each voice. If one voice has far more activity than others (e.g., rapid sixteenth-note figures in soprano while bass has whole notes), check if the texture remains balanced and whether the active voice is the most prominent (usually soprano).

### Phase 3 — Score and Categorize Violations

13. **Create a violation table.** For each rule infraction found, record:
    - **Location** (measure, beat, or voice pair)
    - **Rule violated** (parallel fifths, unresolved leap, out of range, etc.)
    - **Severity** (critical, moderate, minor)
    - **Context** (is this an acceptable exception in the style, era, or texture?)

Use this severity guide:
   - **Critical:** Parallels in outer voices (S-B), severe voice crossing, tendency tones doubled, or sustained register confusion.
   - **Moderate:** Parallels in inner voices, small crossings, unresolved leap in inner voice, minor range overshoot.
   - **Minor:** Direct fifths in supporting voices, rhythmic imbalance, aesthetic preference (not strictly a rule).

## Evaluation Criteria

| Check | Pass |
|---|---|
| All voices are extracted and labeled clearly | Y/N |
| Harmonic changes are marked | Y/N |
| Parallels checked for all adjacent voice pairs | Y/N |
| Leaps identified; unresolved leaps marked | Y/N |
| Voice ranges confirmed against standard | Y/N |
| Voice crossings documented with context | Y/N |
| Doublings examined; tendency tones checked | Y/N |
| Violation table complete with severity tags | Y/N |
| At least 3 categories (A–E) were interrogated | Y/N |

## Red Flags

- All violations are marked "critical" with no severity distinction. This suggests over-application or misunderstanding of context-dependent rules.
- No parallel fifths or octaves found in a four-voice chorale or dense polyphony. Parallel motion is nearly impossible to avoid entirely; missing it suggests the parallel check was cursory.
- Unresolved leaps are absent even in the inner voices. Strictness varies by style; inner-voice leaps are far more forgivable than soprano leaps, but complete absence is rare.
- Voice crossings are marked but never contextualized. Crossing is not always wrong; the assessment must explain whether each crossing supports or undermines the texture.
- Doubling violations flagged without reference to harmonic function. In a V chord, the fifth is often doubled; in a vii°, doubling is carefully constrained. The context determines acceptability.
- Rhythm assessment is missing entirely. Pacing and activity balance are not "optional" — they determine whether listeners hear one main line or confused counterpoint.

## Output Format

```
## Voice Leading Assessment

**Score Title / Excerpt:**
<label>

**Texture:**
<number of voices, approximate key/style>

### Phase 1 — Voice Inventory
| Voice | Range | Pitch sequence (first 8 bars) |
|---|---|---|
| <S/A/T/B> | <e.g., C4–C5> | <e.g., C–E–G–A–...> |

### Phase 2 — Rule Violations by Category

#### A. Parallels and Unisons
| Location | Interval | Voices | Severity | Context / Exception |
|---|---|---|---|---|
| m. 4, beat 2 | P5 | S–B | moderate | leap in soprano; acceptable |

#### B. Leaps and Melody
| Location | Voice | Interval | Unresolved? | Severity |
|---|---|---|---|---|
| m. 2–3 | S | major 7th | no | critical |

#### C. Range and Registration
| Voice | Violation | Measure | Severity |
|---|---|---|---|
| B | F1 (below range) | m. 7 | moderate |

#### D. Voice Crossing and Doubling
| Location | Type | Voices | Duration | Severity |
|---|---|---|---|---|
| m. 5 | crossing | A–T | one note | minor |

#### E. Harmonic Rhythm
| Voice | Activity level | Imbalance with... | Severity |
|---|---|---|---|
| S | high (1/16 notes) | B (whole notes) | minor |

### Summary
**Total violations:** _
**Critical:** _ | **Moderate:** _ | **Minor:** _
**Largest issue:** <description>
**Overall registration:** <compact / spacious / muddy / clear>

### Recommendations
1. <specific fix for critical violation>
2. <style-appropriate rewrite for moderate violation>

### Confidence
<high | medium | low> — <justification. Example: "high — parallels and crossings systematically checked against Fux-era conventions; context-dependent rules applied correctly">
```
---
