---
name: gttm
display_name: Generative Theory of Tonal Music (GTTM)
class: lens
underlying_class: native
domain: music-theory
source: Fred Lerdahl and Ray Jackendoff, 1983
best_for:
  - Analyzing hierarchical structure in tonal compositions
  - Identifying listener perception points in melody and harmony
  - Testing whether a passage exhibits well-formedness in tonal syntax
one_liner: "Generative Theory of Tonal Music — four-layer hierarchical analysis and listener cognition model."
---

# Generative Theory of Tonal Music (GTTM)

## Overview
GTTM models how listeners parse tonal (Western classical, jazz, pop) music into nested hierarchical structures across four independent domains: metrical grid, grouping (phrasing), time-span reduction, and prolongational reduction. The lens operates on audio, scores, or transcriptions of tonal music and produces a four-layer analysis that predicts where a listener perceives structural boundaries, which notes matter most, and how harmonic tension and release articulate the form. Practitioners reach for GTTM when they need to explain why a passage *sounds* coherent or jarring, or when they're comparing two performances or arrangements and need a formal vocabulary for structural differences.

## Analytical Procedure

### Step 1 — Prepare the Score
1. Obtain a complete score or accurate transcription of the passage (at minimum 8–16 bars for a useful analysis).
2. Mark tempo, time signature, key signature, and any marked tempo changes or fermatas.
3. Identify and label all pitch events (notes, rests) and their durations in the score.
4. Note the instrumentation and whether there are multiple staves (piano, ensemble, etc.); GTTM treats all voices equally in the analysis.

### Step 2 — Layer 1: Metrical Structure
Goal: Determine the hierarchical grid of strong and weak beats that a listener infers.

1. **Identify the time signature.** This sets the primary accent level (e.g., 4/4 has beats 1, 2, 3, 4 with 1 and 3 stronger than 2 and 4).
2. **Mark beat levels recursively:**
   - Level 0 (tactus): The main beat the listener taps to (usually the quarter note in 4/4).
   - Level −1: The half-bar or bar (groups of 2 or 4 beats).
   - Level −2: The phrase-level bar (groups of 2 or 4 bars, e.g., the 4-bar hypermeasure).
   - Level +1: The subdivision (if audible and regular, e.g., eighth notes in 4/4).
3. **Mark syncopations or hemiolas** (note when note onsets violate the inferred grid — this is data for later analysis).
4. **Output:** A grid diagram showing which time points carry which metrical strength. Strength is binary at each level: strong or weak.

### Step 3 — Layer 2: Grouping Structure (Phrasing)
Goal: Identify phrase boundaries and segment the passage into nested groups.

Use these heuristics in order of strength:

1. **Rest or silence:** A rest followed by a new attack always signals a group boundary.
2. **Pitch register change:** An abrupt leap upward or downward of a major third or larger, especially on a strong beat, often signals a boundary.
3. **Harmonic change:** A cadence (especially V–I, IV–I, or V–vi), a change in chord quality (major to minor), or a shift from a tonic-like to a dominant-like harmony signals closure.
4. **Duration change:** If all notes in a phrase are predominantly eighth notes and the final note is a half note (or longer), this length change signals closure.
5. **Parallelism:** Two or more identical or near-identical phrase contours suggest grouping them together.
6. **Repetition:** If a melody or harmonic progression repeats, group the repetitions together.

Mark each group boundary (group start and end). Label each group with a unique ID (Group 1a, 1b, 2a, etc.). Recursively check: can groups be combined into larger groups that share a coherent boundary? If yes, nest them.

**Output:** A tree diagram or indented list showing the grouping hierarchy (top level = entire passage, bottom level = smallest phrase units).

### Step 4 — Layer 3: Time-Span Reduction
Goal: Rank notes by structural importance and create a reduction showing the "skeleton" of the passage.

1. **Apply reduction heuristics to each group:**
   - **Downbeat:** The note on the first strong beat of a group carries the most weight.
   - **Stable harmony:** A note that lands on a stable harmony (tonic, in-key root position) is more important than a note on an unstable harmony (secondary dominant, suspension, passing tone).
   - **Longer duration:** A note held for 2 beats is more important than a note that lasts half a beat in the same role.
   - **Metrical strong point:** A note on a metrically strong beat (level −1 or −2) outweighs a note on a weak beat.
   - **Accented by instrument:** If a melody note is doubled in a lower octave or reinforced by a change in timbre, it is structurally stronger.

2. **Create a reduction:** Remove ornamental notes (passing tones, neighbor tones, suspensions, turns) that do not satisfy the above criteria. Keep only notes that are harmonically, metrically, or durational stable points.

3. **Recursively reduce:** Apply the same heuristics to the reduction. A two-level reduction (original → first reduction → second reduction) is common for a 16-bar phrase.

4. **Mark each retained note with a confidence in its structural importance:** High (appears in all reductions), Medium (appears in first but not final reduction), Low (borderline).

**Output:** A 2–3-level tree of reductions, each showing which notes are kept at that level, plus confidence tags.

### Step 5 — Layer 4: Prolongational Reduction
Goal: Map the path of harmonic tension and release, showing which harmonies are primary and which are elaborations.

1. **Identify stable harmonies** (tonic, dominant, subdominant, relative major/minor). In the key of C, these are C major, G major, F major, A minor. All other chords are contextually unstable.

2. **Identify directed motion:**
   - Toward tonic (I) = relaxation, closure.
   - Away from tonic = tension building.
   - To dominant (V) = suspension, expectation of return.

3. **Create the prolongational tree:**
   - Root node = the global harmonic goal (almost always the tonic of the key).
   - Branch to the main harmonic events: e.g., "tonic, modulation to dominant, return to tonic."
   - Under each branch, show the elaborating chords (e.g., IV–V elaborating the overall approach to I).

4. **Label each branch with a structural relation:**
   - **Tonic prolongation:** This chord or harmony is an extension of the tonic (e.g., vi moving back to I).
   - **Dominant prolongation:** This is an approach to the dominant (e.g., ii–V).
   - **Subsidiary prolongation:** This is an elaboration of a non-tonic chord (e.g., vi in its own right, not as part of I).

5. **Mark modulations:** If the passage moves to a new key, note where the modulation begins and ends. The prolongational tree may have multiple roots if the form is multi-sectional (e.g., exposition–development–recapitulation).

**Output:** A tree diagram with harmonic events as nodes, labeled with prolongational relations and tension/relaxation direction.

### Step 6 — Cross-Layer Validation
1. **Check alignment:** Do the grouping boundaries (Layer 2) align with cadences or harmonic closure points (Layer 4)? If not, note the discrepancy — it may indicate irony or structural tension.
2. **Check metrical coherence:** Do the downbeats of groups (Layer 2) fall on metrically strong points (Layer 1)? If not, check whether this is a deliberate syncopation.
3. **Check reduction stability:** Does the time-span reduction (Layer 3) agree with the prolongational structure (Layer 4) on which notes are "main"? Disagreement is interpretively interesting but should be justified.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Metrical grid is marked at three or more levels (tactus, bar, hypermeasure) | Y/N |
| Grouping structure is hierarchical (at least 2 nesting levels) and all boundaries are justified by one of the 6 heuristics | Y/N |
| Time-span reduction retains 25–50% of original notes; each kept note is tagged with confidence | Y/N |
| Prolongational tree has a clear root (harmonic goal) and at least 3 branches | Y/N |
| At least two layers (metrical, grouping, reductions, prolongational) show mutual agreement or documented disagreement | Y/N |

## Red Flags

- Metrical structure is marked at only one level. This suggests the analyst did not interrogate the hypermeter (bar-level grouping), a common oversight.
- Grouping boundaries are marked but none correspond to harmonic events (cadences, key changes). GTTM assumes these are strongly correlated; complete absence is a warning that the passage may be atonal, strictly minimalist, or misanalyzed.
- Time-span reduction removes 80%+ of notes. Either the passage is extremely ornamental (rare) or the analyst was too aggressive. Reductions should retain the melody's outline.
- Prolongational tree is a single chain (I → V → I with no elaborations). A real passage has depth; a flat tree suggests the analyst did not model harmonic tension.
- No discrepancies noted between layers. Perfect alignment across all four layers is structurally suspicious — real music has competing cues. Annotate where they differ and explain why.

## Output Format

```
## GTTM Analysis

**Passage:** <title, composer, bars>

### Layer 1 — Metrical Structure
| Time point | Tactus | Bar | Hypermeasure | Notes |
|---|---|---|---|---|
| 1 | strong | downbeat | level −2 strong | <any syncopations or irregularities> |
| ... | ... | ... | ... | ... |

### Layer 2 — Grouping Structure (Hierarchy)
```
Phrase A (bars 1–4)
  Group A1 (bars 1–2)
  Group A2 (bars 3–4)
Phrase B (bars 5–8)
  ...
```
Justification: <list which heuristic(s) define each boundary>

### Layer 3 — Time-Span Reduction
**Level 0 (original):** <all note onsets and pitches>
**Level 1 (first reduction):** <retained pitches, ornaments removed>
  - <note>: High confidence
  - <note>: Medium confidence
  - ...
**Level 2 (final reduction):** <skeleton>

### Layer 4 — Prolongational Reduction
Root: Tonic (key)
├─ Tonic prolongation (bars 1–2): I–IV–I
├─ Dominant motion (bars 3–6): ii–V–V7
└─ Tonic closure (bars 7–8): I

Harmonic tension direction: <build to V at bar 6, release back to I by bar 8>

### Cross-Layer Check
- Metrical downbeats (Layer 1) align with phrase boundaries (Layer 2)? <Yes/No, with note>
- Grouping boundaries (Layer 2) correspond to cadences (Layer 4)? <Yes/No, with note>
- Time-span reduction (Layer 3) agrees with prolongational main notes (Layer 4)? <Yes/No, with note>

### Confidence
<high/medium/low> — <justification. High = all layers cohere and the analysis is grounded in the score. Medium = one layer has ambiguity or minor discrepancy. Low = multiple interpretations are equally plausible given the passage.>
```
