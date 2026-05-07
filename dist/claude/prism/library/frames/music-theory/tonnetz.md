---
name: tonnetz
display_name: Tonnetz
class: frame
underlying_class: native
domain: music-theory
source: Leonhard Euler, 1739 ("Tentamen novae theoriae musicae"); Hugo Riemann, 1880s (modern formulation)
best_for:
  - Classifying chord relationships by geometric distance in pitch space
  - Sorting harmonic progressions into categories based on voice-leading efficiency
  - Determining whether a chord transition is parsimonious or requires larger jumps
one_liner: "Measure chord distance on a 3D lattice of the pitch space to judge voice-leading economy."
---

# Tonnetz

## Overview

The Tonnetz (German: "tone network") is a geometric frame that maps chords and pitch classes onto a two- or three-dimensional lattice, with axes representing intervals (typically thirds and fifths). Its core claim is that **chords occupying neighboring positions on the lattice can be connected with minimal voice motion**, while chords separated by greater lattice distance require larger jumps. By sorting a chord transition into one of three distance categories — adjacent, mediant, or distant — a composer or analyst can immediately predict the voice-leading cost and choose among parsimonious, economical, or dramatic progression strategies.

## Categories

1. **Adjacent (Parsimonious)**
   - Two chords share **one or two common tones** and differ by the minimal pitch movement in one voice.
   - On the lattice, the chords occupy neighboring nodes, separated by a single edge (typically a move of one third or one fifth).
   - Discriminating criterion: exactly one voice moves by a second or third; at least one tone is held.
   - Example: C major (C–E–G) to A minor (A–C–E); only the G moves to A, and C and E are held.

2. **Mediant (Economical)**
   - Two chords share **no common tones** but are close enough on the lattice that voice motion remains manageable (typically 2–3 semitone shifts across voices).
   - The progression requires all three voices to move, but each moves by a small interval (a second, third, or tritone).
   - Discriminating criterion: no shared tones, but the total voice-leading distance is minimized by the lattice structure; each voice moves by a second, third, or tritone.
   - Example: C major (C–E–G) to F-sharp major (F♯–A♯–C♯); a chromatic mediant or relative major/minor relationship requiring coordinated but economical motion.

3. **Distant (Dramatic)**
   - Two chords are **far apart on the lattice** (more than 2–3 steps), requiring large leaps in at least one voice or non-intuitive voice assignments.
   - No common tones; voice-leading is not optimized by proximity.
   - Discriminating criterion: at least one voice must leap by an interval larger than a fifth, or the progression contradicts the lattice geometry.
   - Example: C major (C–E–G) to F-flat major (F♭–A♭–C♭); this requires chromatic or enharmonic retuning and is felt as a dramatic harmonic jump.

## Classification Procedure

1. Write out the two chords in root position or a clear voicing: list the three pitches of each triad.
2. Ask **"Do the two chords share any pitch classes?"** (ignoring octaves)
   - If **yes**, go to step 3.
   - If **no**, go to step 4.
3. For adjacent-sharing chords, measure the **total semitone distance** across all voices.
   - If the total is ≤ 3 semitones and at most one voice moves → **Adjacent**.
   - If the total is 4–6 semitones → **Mediant**.
   - If the total is > 6 semitones → **Distant**.
4. For non-sharing chords, check the **lattice distance** (number of edges on the Tonnetz path between the root pitch classes).
   - If distance is 1 edge → **Adjacent**.
   - If distance is 2–3 edges → **Mediant**.
   - If distance is > 3 edges or requires enharmonic retuning → **Distant**.
5. State the classification and the implied voice-leading strategy (see Implications below).

## Implications per Category

| Category | Voice-leading strategy | What the composer should do |
|---|---|---|
| **Adjacent** | **Hold common tones; move one voice by step.** | Exploit the efficiency: these progressions are smooth and require minimal effort. Use liberally in lyrical or flowing contexts. |
| **Mediant** | **Move all voices, but coordinate so each jumps minimally.** | Plan the voicing carefully; acceptable for dramatic or functional turning points. Requires more listener attention but remains coherent. |
| **Distant** | **Accept large leaps or enharmonic tricks; prioritize the harmonic color over smoothness.** | Reserve for moments of strong intent (key changes, climaxes, abrupt pivots). The listener perceives this as a rupture and a restart, not a continuation. |

For a lenslab agent classifying a composition's progressions, the implication is immediate:
- Adjacent passages → check for phrase structure; these often mark local stability.
- Mediant passages → check for modulation or harmonic function; these often mark transitions.
- Distant passages → check for structural breaks, cadences, or key changes; these mark boundaries.

## Common Misclassifications

- **Adjacent mistaken for Mediant.** Assuming that any progression with shared common tones is smooth, even when one voice leaps more than a third. The tell is that the leap breaks the lattice path. Consequence: overestimating voice-leading efficiency and underestimating the jarring effect of the leap.

- **Mediant mistaken for Distant.** Treating a chromatic mediant (e.g., C major to E major) as far-flung when it is actually only 2–3 lattice steps away. The tell is rechecking the shared-tone count and interval: if the total distance is under 6 semitones and the lattice path is short, it is Mediant. Consequence: unnecessarily recomposing a passage that already works economically.

- **Distant mistaken for Adjacent.** Misidentifying an enharmonic rewriting (e.g., C major to B major, which is enharmonically close but lattice-distant) as adjacent because the two chords look similar on paper. The tell is checking the actual lattice distance, not the visual similarity. Consequence: misjudging voice-leading feasibility.

- **Ignoring octave doubling.** The Tonnetz assumes three-voice harmony; in four- or five-voice music, a doubled voice can create the illusion of greater distance or false common tones. Always re-verify the classification by checking the unique pitch classes, not the voicing.
