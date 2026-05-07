---
name: schenkerian-analysis
display_name: Schenkerian Analysis
class: lens
underlying_class: native
domain: music-theory
source: Heinrich Schenker (Der freie Satz, 1935); pedagogical systematization by Allen Forte and others
best_for:
  - Reducing a composition to its underlying tonal structure
  - Identifying structural levels obscured by surface detail
  - Understanding how a piece unfolds from fundamental harmonic motion
one_liner: "Reduce surface musical detail to fundamental tonal motion across three levels."
---

# Schenkerian Analysis

## Overview
Schenkerian Analysis treats a musical composition as layered levels of decreasing detail, all derived from a single fundamental chord progression called the Ursatz. The analyst works backward from surface figuration through intermediate structural levels to reveal the deep structure — usually a progression in the tonic that descends by step in the soprano voice and resolves to the tonic triad. Practitioners use this lens when a piece's local details obscure its overall coherence, or when they suspect motivic relationships hide a simpler underlying logic.

## Analytical Procedure

### Phase 1 — Score Preparation and Voice-Leading Audit

1. **Obtain or create a clean score.** Use a published edition or notate the work yourself. The score must show all voices clearly enough to track linear motion. If working from a reduction or arrangement, note this limitation — orchestration and register choice can obscure structural voices.

2. **Identify the key and tonal region.** Write the home key and all modulations or tonicizations. For tonal works (common-practice era onwards), Schenkerian analysis assumes a single tonal center governs the whole piece; for atonal or highly chromatic works, note whether the method applies.

3. **Trace the outer voices (soprano and bass).** Mark every note in the soprano line and bass line. Highlight repeated notes, skips, and stepwise motion. Do not reduce yet — you are mapping.

4. **Identify obvious surface diminutions.** Mark passing tones, neighbor tones, suspensions, and arpeggios in the soprano and bass. Use standard abbreviations (PT, NT, SUS, ARP). Circle anything that is purely decorative and does not participate in chord succession.

### Phase 2 — Foreground to Middleground Reduction

5. **Remove the clearest diminutions.** Eliminate passing tones and neighbor tones identified in Step 4. Rewrite the score with these removed. This is your first reduction level (foreground-to-middleground layer).

6. **Identify structural chords.** In the reduced score, mark every chord that is harmonically significant — typically those on strong beats or those that effect a harmonic motion (V→I, IV→V, etc.). Weak-beat passing chords and chords that fill in a single harmony should not be marked as structural at this level.

7. **Extract the upper-voice (soprano) scale degree motion.** Write out the soprano line of the reduced score as scale degrees (1–2–3–4–5, etc., within the home key or relevant key region). This line is your Urlinie (fundamental line).

8. **Extract the bass motion.** Identify the bass root progression. In many works, the bass moves in roots (I–IV–V–I or similar). Circle any bass note that is not a root position harmony (it may be an inversion). This bass progression is the Bassbrechung (bass arpeggio).

### Phase 3 — Middleground to Background Reduction

9. **Compress the middleground further.** Remove inner-voice figuration and chords that fill passing harmony. What remains are only chords that effect large-scale motion. For a typical tonal piece, this might reduce to 4–6 chords across the entire piece.

10. **Identify the Ursatz candidate.** The Ursatz is a two-part structure: the Urlinie (soprano descent, usually 3–2–1, 4–3–2–1, or 5–4–3–2–1) and a I–V–I bass arpeggio, often with prolongation of V in the middle. Examine whether your compressed form fits this template. If the soprano descent does not reach scale degree 1, or if the bass does not form a clear I–V–I frame, the piece may not be Schenkerian-reducible (or may require a variant Ursatz).

11. **Map the prolongation path.** Trace how the intermediate levels (middleground, foreground) elaborate and delay the background Ursatz. For example, the initial tonic may be prolonged by passing through IV (the subdominant), which itself may be elaborated by voice-leading chords. Write out how each level unfolds the level beneath it.

12. **Check for branch lines and coupling.** Some pieces contain secondary structures (Nebensätze) — smaller themes or sections that have their own diminution but are subordinate to the main Ursatz. Mark these. Also note if the soprano and bass are "coupled" (parallel motion in the same sense, which is allowed in background levels).

### Phase 4 — Verification and Interpretation

13. **Redraw the graph.** Using standard Schenkerian graph notation (or a clear prose description if graphing is infeasible), show the background (Ursatz), middleground (one or more intermediate reductions), and foreground (full score or near-full reduction). Vertical alignment should show how each note in a higher level unfolds into a passage at the next lower level.

14. **Test structural coherence.** Play through the background Ursatz alone (e.g., the soprano descent 3–2–1 with a I–V–I bass). Does it make musical sense? Does the piece sound like a single unified motion, or do you hear disjoint sections? Incoherence at the background suggests either a misanalysis or a genuinely non-Schenkerian work.

15. **Identify what the analysis reveals.** Write a short prose account of what you learned: How does the piece prolong its main harmony? Are there surprising voice-leading connections between distant sections? Does a seemingly important surface detail turn out to be subordinate ornament? Do motivic relationships correspond to structural levels?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Score is legible and all voices are traced | Y/N |
| Foreground diminutions (PT, NT, SUS) are identified and marked | Y/N |
| Structural chords (harmony-moving chords) are distinguished from passing/weak-beat chords | Y/N |
| Soprano line is extracted as a scale-degree descent | Y/N |
| Bass forms a clear root-position progression (I–V–I or variant) | Y/N |
| Ursatz candidates are tested (soprano descent, bass arpeggio, tonal unity) | Y/N |
| At least two reduction levels (middleground, background) are shown | Y/N |
| Graph or prose account explains how lower levels elaborate the background | Y/N |

## Red Flags

- The soprano line never reaches scale degree 1 at the structural close. Either the piece is not in traditional tonality, or a note is being misconstrued as structural when it is ornamental.
- The bass progression does not form a coherent I–V–I or plausible variant. This is a strong signal that the work may not be amenable to Schenkerian reduction (or that a major reanalysis is needed).
- Every reduction removes only a few notes and the "reduction" is almost as complex as the original. You may be confusing ornamental chords with structural ones — revisit Step 6.
- The Ursatz is grafted onto the analysis (assumed before analysis rather than derived from it) and the foreground shows no clear path to it. Work backward: start with what the score actually does, then infer the structure.
- The soprano and bass in the background are not paired by common underlying harmonic functions. For example, a soprano descent is paired with a bass that does not coordinate with it harmonically.
- No secondary structures or branch lines are identified in a piece that clearly has formal sections. Schenkerian analysis is not flat; it should hierarchically explain distinct passages.

## Output Format

```
## Schenkerian Analysis

**Work:** <Title, composer, key>

### Structural Levels

#### Background (Ursatz)
Urlinie (soprano): <scale degrees, e.g., 3–2–1>
Bassbrechung (bass): <root progression, e.g., I–V–I>
Harmonic frame: <e.g., tonic prolonged by subdominant, leading-tone chord, and dominant preparation>

#### Middleground Level 1
<Description of how main sections and key harmonic regions elaborate the background.>

#### Middleground Level 2 (if applicable)
<Further subdivision or secondary themes.>

#### Foreground (Surface Detail)
<Most prominent ornamental diminutions and voice-leading chords.>

### Reduction Diagram
<Graph in standard Schenkerian notation or prose account of vertical alignment.>

### Structural Insights
1. <What the analysis reveals about the piece's coherence or hidden connections>
2. <Role of surface detail relative to underlying structure>
3. <Any unexpected voice-leading or harmonic prolongations>

### Confidence
<high/medium/low> — <Justification. For example: "high — soprano descent, bass arpeggio, and harmonic regions all cohere around a clear I–V–I frame." Or "medium — the middleground contains ambiguities in voice-leading that admit two plausible reductions." Or "low — the piece contains large atonal or post-tonal passages that resist background structure.">
```
