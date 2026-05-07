---
name: set-theory
display_name: Set Theory (Forte)
class: lens
underlying_class: native
domain: music-theory
source: Allen Forte, *The Structure of Atonal Music* (1973)
best_for:
  - Analyzing pitch-class relationships in atonal and twelve-tone music
  - Identifying and comparing pitch-class sets across compositions
  - Understanding structural coherence without reliance on traditional harmony
one_liner: "Systematically analyze pitch-class sets to reveal interval relationships in atonal music."
---

# Set Theory (Forte)

## Overview
Set Theory categorizes the twelve pitch classes (C, C♯, D, etc.) as a finite set and treats all subsets of pitches abstractly, independent of octave, register, or instrumental timbre. A pitch-class set (or simply "set") is a collection of distinct pitch classes that can be represented as a point in a high-dimensional space, with each set assigned a prime form (canonical representation) and a Forte number (e.g., 3-1, 4-18). Practitioners use this lens to uncover structural patterns in atonal and twelve-tone music that would be invisible to harmonic analysis, especially when measuring how compositions exploit or avoid particular pitch-class combinations and transformations.

## Analytical Procedure

### Phase 1 — Extract and Normalize

1. **Identify the passage or complete work to analyze.** Mark the beginning and end point clearly. Set Theory can be applied to a single measure, a phrase, a section, or an entire piece.

2. **List all pitch classes present in the passage, ignoring octave, duration, and dynamics.** Use integer notation: C=0, C♯=1, D=2, ..., B=11. Write them in ascending order, with no duplicates. Example: if the passage contains C4, G3, E♭5, C♯6, write `{0, 1, 3, 7}`.

3. **Remove any duplicate pitch classes.** A set has no repeated members. If the passage uses C multiple times, list it once.

4. **Determine the cardinality (size) of the set.** Count how many distinct pitch classes are present. Cardinality ranges from 1 to 12.

### Phase 2 — Find the Prime Form

5. **Generate all possible transpositions of the set.** Transposition shifts all pitch classes by a constant interval (modulo 12). For the set {0, 1, 3, 7}:
   - T₀ (no transposition): {0, 1, 3, 7}
   - T₁ (up one semitone): {1, 2, 4, 8}
   - T₂: {2, 3, 5, 9}
   - ... continue through T₁₁

6. **Generate the inversion of the original set.** Inversion flips the set around an axis. The standard method: invert by replacing each pitch class *p* with (−*p* mod 12). For {0, 1, 3, 7}: inversion gives {0, 11, 9, 5}, then reorder it as {0, 5, 9, 11}.

7. **Generate all transpositions of the inverted set.** Apply T₀ through T₁₁ to the inverted form.

8. **Calculate the interval vector for each transposition and inversion.** The interval vector measures the frequency of each interval class (0 to 6) within the set. For a 4-note set, it has 6 positions. This is mechanical: list all pairwise intervals, reduce them to interval classes 1–6 (ignoring unison), and count occurrences.

9. **Select the prime form.** Apply the standard Forte ordering rule: choose the transposition/inversion pair that has the tightest spacing when written in ascending order from 0, prioritizing the smallest intervals at the start. In practice: the set with the smallest second element, then smallest third element, etc., reading left-to-right. This is the **prime form**.

10. **Assign the Forte number.** Cross-reference your prime form against Forte's table (or a music theory reference). The Forte number has the form `n-m`, where `n` is the cardinality (3 to 9; sets of 1, 2, 10, 11, 12 are trivial or complements of smaller sets) and `m` is the ordinal index within that cardinality. Example: {0, 1, 4} is `3-3`.

### Phase 3 — Analyze Structure

11. **Document the interval vector.** This vector reveals how "consonant" or "dissonant" the set sounds: high frequency of intervals 1, 5, or 6 suggests triadic-like or whole-tone-like quality; high frequency of 2 or 4 suggests chromatic or tritone saturation.

12. **Check for subset and superset relationships.** If the passage contains multiple sets, identify which are subsets of others. For example, {0, 4, 7} (major triad) is a subset of {0, 1, 4, 7}. This reveals structural nesting.

13. **Measure set transformations across time.** If analyzing multiple passages, compare the Forte numbers and prime forms. Ask: are sets related by transposition, inversion, or subset inclusion? Are complementary sets (pairs that together use all 12 pitch classes) employed?

14. **Contextualize within the work.** Note where the set appears, how long it persists, whether it returns, and whether other sets are built from it. Link the analysis to compositional strategy, not just numerical identity.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All pitch classes in the passage are correctly extracted and deduplicated | Y/N |
| Transpositions T₀ through T₁₁ are correctly calculated (modulo 12 arithmetic verified) | Y/N |
| Inversion is correctly computed and all transpositions of the inversion are listed | Y/N |
| Interval vector is calculated accurately for at least one form | Y/N |
| Prime form selection follows Forte's priority rule (tightest spacing from 0) | Y/N |
| Forte number is correctly assigned and cross-checked against a reference | Y/N |
| Interval vector interpretation connects to perceptual or structural quality | Y/N |
| Multiple sets in the passage are compared for subset, complement, or transformation relationships | Y/N |

## Red Flags

- Pitch classes are extracted with octave notation still present (e.g., C4 vs. C). Set Theory operates only on pitch-class identity, not register.
- Transpositions or inversions contain errors in modulo 12 arithmetic, or some transpositions are skipped.
- Interval vector is calculated for all intervals, including unison (interval class 0). Interval class 0 is excluded by convention.
- Prime form is selected solely by smallest cardinality or first element, ignoring the full tightness criterion.
- Forte number is not verified against a published table or reference; the analyzer is guessing.
- Analysis stops after assignment of a Forte number, with no attention to what the interval vector or set structure reveals about the composition.
- Multiple sets are listed but never compared for relationships; the analysis is a catalogue, not an interpretation.

## Output Format

```
## Set Theory Analysis

**Passage analyzed:**
<description of temporal location or extent>

### Pitch-class extraction
Pitch classes (integer notation): <{...}>
Cardinality: _

### Prime form and Forte number
Prime form: <{...}>
Forte number: <n-m>

### Interval vector
IC 1: _  |  IC 2: _  |  IC 3: _  |  IC 4: _  |  IC 5: _  |  IC 6: _
Quality assessment: <e.g., "chromatic saturation with tritone emphasis" or "high whole-tone content">

### Subset and transformation analysis
- Subsets identified: <list>
- Supersets identified: <list>
- Transformation relationships to other sets in the work: <description>

### Structural significance
<Interpretation of how the set functions in the composition: Does it return? Does it mutate? Is it part of a larger strategic plan?>

### Confidence
<high | medium | low> — <justification>
```
---
