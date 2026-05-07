---
name: spectromorphology
display_name: Spectromorphology
class: lens
underlying_class: native
domain: music-theory
source: Denis Smalley, 1986 onwards (spectromorphology framework for electroacoustic music)
best_for:
  - Analyzing timbral and morphological evolution in electroacoustic compositions
  - Describing spectral transformation without recourse to pitch-based notation
  - Training perception of microtimbral gesture and spectral motion
one_liner: "Electroacoustic analysis tool that tracks the temporal evolution of spectral shape."
---

# Spectromorphology

## Overview

Spectromorphology is a framework for analyzing the morphology (shape and evolution) of spectral content in electroacoustic music. Rather than reducing sound to pitch and duration, it describes how frequency, amplitude, and timbre transform over time — the spectral gesture. Practitioners reach for it when conventional notation fails or when the compositional intent lies in timbral evolution, not harmonic progression. The method bridges the gap between what the ear hears and what technical analysis can articulate.

## Analytical Procedure

### Phase 1 — Spectral Inventory

1. **Identify the listening window.** Select a continuous passage of 5–30 seconds where a single timbral gesture or morphological shape dominates. Mark start and end times.

2. **Describe the spectral profile at the onset.** Without using pitch labels (C4, F#5, etc.), describe:
   - **Richness**: Is the spectrum broadband noise, harmonic, sparse, or dense?
   - **Centroid region**: Does most energy sit in the low, mid, or high frequency range? (Do not estimate specific Hz; use "low/mid/high" or relative terms.)
   - **Harmonicity**: Are there audible harmonic partials, or is the spectrum inharmonic/noisy?
   - **Amplitude envelope**: Does the attack occur gradually (slow onset) or abruptly (sharp attack)?

3. **Trace the spectral trajectory.** Divide the passage into 3–5 equal time steps (onset, early, middle, late, offset). At each step, note whether each of these parameters **rises, falls, stabilizes, or oscillates**:
   - Spectral brightness (the proportion of high-frequency energy)
   - Spectral width (the range of frequencies occupied)
   - Harmonic clarity (sharpness of partials, if present)
   - Amplitude envelope (loud, quiet, or modulated)
   - Spectral density (how crowded the spectrum feels)

4. **Identify morphological landmarks.** Mark any moment where:
   - The spectral shape changes discontinuously (e.g., noise abruptly shifts to tone)
   - A new frequency region becomes prominent
   - Amplitude jumps or drops
   - Harmonic content emerges or dissolves
   These are breakpoints in the morphological arc.

### Phase 2 — Gestural Characterization

5. **Name the overall morphological type.** Choose one or more from:
   - **Spectral contour**: ascending, descending, or arch (rises then falls)
   - **Spectral envelope shape**: sustained, iterative (pulsing), or transitional (moving between states)
   - **Harmonic motion**: harmonic (pitched), quasi-harmonic (ambiguous), or inharmonic (noise/complex)
   - **Textural quality**: smooth, grainy, spiky, or fractured

6. **Describe the gesture in non-metaphorical motion terms.** Avoid poetic language. Use:
   - "The spectrum narrows while brightening" (not "the sound becomes more agile")
   - "Partials appear at 3, 6, and 9 kHz while low-mid energy decays" (not "the timbre opens up")
   - "Amplitude oscillates at ~4 Hz with decreasing depth" (not "tremolo effect")

### Phase 3 — Comparative and Contextual Analysis

7. **Compare this gesture to adjacent sections.** How does this spectral morphology differ from what precedes and follows it? Note:
   - Did spectral density increase or decrease?
   - Did harmonic clarity shift (more pitched, or more noisy)?
   - Did the overall brightness trajectory reverse or continue?

8. **Identify the morphological function.** Does this gesture:
   - Initiate a new section or idea?
   - Transition between two stable states?
   - Articulate a climax or point of contrast?
   - Decay or dissolve toward silence?

9. **Check for spectral coherence.** Are all parameters moving in the same direction (e.g., brightness and amplitude both rising), or do they move independently (e.g., brightening while amplitude falls)? Independence often signals compositional intent.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Spectral profile at onset is described without pitch labels | Y/N |
| Trajectory across 3–5 time steps is traced for ≥4 parameters | Y/N |
| At least one morphological landmark is identified and marked in time | Y/N |
| Gestural type is named using terms from Phase 2 | Y/N |
| Description uses motion/change language, not metaphor | Y/N |
| Comparative analysis vs. adjacent sections is present | Y/N |
| Morphological function is stated (initiate/transition/climax/decay) | Y/N |

## Red Flags

- Description relies on instrument names or pitch labels ("a violin slide from G to E"). Spectromorphology is timbre-first, not instrument-first.
- No time-domain change is noted; the passage is described as static even though something is audibly evolving.
- Morphological landmarks exist but were not marked. Without them, the analysis is impressionistic.
- Gestural characterization is poetic or metaphorical ("the sound soars," "it falls away"). The method demands physical spectral language.
- Comparative analysis is missing; the gesture is analyzed in isolation. Context reveals function.
- Amplitude and spectral brightness are conflated (saying "the sound gets brighter" when only loudness changed, not spectrum).

## Output Format

```
## Spectromorphological Analysis

**Passage:** [start time]–[end time]
**Duration:** [seconds]

### Phase 1 — Spectral Inventory

**Onset profile:**
- Richness: [broadband / harmonic / sparse / dense]
- Centroid region: [low / mid / high]
- Harmonicity: [harmonic / quasi-harmonic / inharmonic]
- Attack: [sharp / gradual]

**Spectral trajectory:**
| Time step | Brightness | Width | Harmonic clarity | Amplitude | Density |
|---|---|---|---|---|---|
| Onset | [rises / falls / stable / oscillates] | — | — | — | — |
| Early | — | — | — | — | — |
| Middle | — | — | — | — | — |
| Late | — | — | — | — | — |
| Offset | — | — | — | — | — |

**Morphological landmarks:**
- [time]: [description of spectral change]
- [time]: [description]

### Phase 2 — Gestural Characterization

**Morphological type:**
- Spectral contour: [ascending / descending / arch]
- Envelope shape: [sustained / iterative / transitional]
- Harmonic motion: [harmonic / quasi-harmonic / inharmonic]
- Textural quality: [smooth / grainy / spiky / fractured]

**Gesture in motion terms:**
<Non-metaphorical description of spectral changes>

### Phase 3 — Comparative and Contextual Analysis

**Comparison to adjacent sections:**
<Description of differences>

**Morphological function:**
[Initiate / Transition / Climax / Decay / Other]

**Spectral coherence:**
<Whether parameters move together or independently, and significance>

### Confidence
<high / medium / low> — <justification based on clarity of spectral landmarks, stability of descriptive parameters, and distinctness of gesture from surroundings>
```
