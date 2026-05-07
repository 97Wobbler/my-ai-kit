---
name: sound-analysis
display_name: Sound Analysis
class: lens
underlying_class: native
domain: film-theory
source: Michel Chion (Audio-Vision, 1994); formalized in film studies pedagogy
best_for:
  - Decomposing soundtrack layers to understand emotional and narrative function
  - Identifying gaps between image and sound that create meaning
  - Diagnosing why a scene feels off despite correct dialogue/music
one_liner: "Classify diegetic versus non-diegetic sound and track divergences between image and audio for meaning."
---

# Sound Analysis

## Overview
Film sound exists in two domains: diegetic (characters and the world can hear it) and non-diegetic (only the audience hears it — narration, score, sound effects added in post). The analytical power lies not in simply labeling sounds, but in identifying moments where the boundary blurs or where the relationship between sound and image contradicts expectations. Practitioners use this lens when a scene's emotional weight feels misaligned with the dialogue and music, or when they need to isolate which layer (dialogue, effect, score) is carrying narrative load.

## Analytical Procedure

### Phase 1 — Inventory and Classify

1. **Watch the scene without subtitles and write a timeline of every distinct sound element you hear.** Include silence. Be specific: "car horn at 2:15" not "traffic." Aim for 10–20 elements per 60-second scene.

2. **For each sound, classify it by source:**
   - **Diegetic (on-screen source visible)** — door slam, character dialogue, phone ring, radio playing in the car
   - **Diegetic (on-screen source implied but not visible)** — dialogue from off-screen room, car engine when we see only the road
   - **Non-diegetic** — voice-over narration, orchestral score, sound effect added for drama (not from the world)
   - **Ambiguous** — music playing from a source in the world (radio, concert) but mixed to feel cinematic; mark these clearly

3. **For each element, record:**
   - **Onset timing** — when it enters (in seconds)
   - **Duration** — how long it plays
   - **Loudness relative to dialogue** — louder / equal / quieter (use `-`, `=`, `+` notation)
   - **Frequency band** — high (strings, voice, hiss), mid (dialogue, most instruments), low (bass, rumble, heartbeat)

### Phase 2 — Identify Bridges and Transitions

4. **Find moments where diegetic and non-diegetic sound overlap or transition into each other.** These are "bridges." Examples:
   - Character's humming becomes orchestral score
   - Radio music fades to underscore
   - Dialogue from a phone call blends with non-diegetic ambience
   - Record the exact second and describe the blend.

5. **For each bridge, note whether it is:**
   - **Smooth** (blended, audience may not notice the transition)
   - **Jarring** (distinct cut or audible shift; draws attention)
   - **Functional** (clarifies narrative intent or emotion)
   - **Disorienting** (confuses where the sound originates or what we're meant to feel)

### Phase 3 — Map Sound to Visual Content

6. **Watch the scene again with sound only (close your eyes or mute the video).** Write what you infer about the visual content from sound alone. Then unmute and compare.
   - What did sound tell you to expect that the image contradicted?
   - What did the image show that sound downplayed or ignored?
   - Record discrepancies as separate rows in your analysis.

7. **For each major sound element (dialogue, primary effect, score), ask:**
   - What character or object is this sound attached to, and is that attachment clear from the image?
   - Does this sound come before, during, or after the visual event it relates to? (e.g., the door slam sound happens before we see the door close = temporal mismatch)
   - Is the sound's emotional tone (bright, dark, tense, peaceful) aligned with the image's tone?

### Phase 4 — Evaluate Functional Load

8. **Assign each sound element one of these functional roles:**
   - **Narrative-critical** — essential to understanding plot or character (dialogue, crucial sound cue)
   - **Emotional-critical** — carries the scene's affect (score, heartbeat, silence)
   - **Environmental** — builds world and context (ambient traffic, wind, room tone)
   - **Ornamental** — adds texture or texture but could be removed without loss (occasional bird call, distant dog bark)

9. **Count how many non-diegetic elements are narrative-critical vs. emotional-critical.** If the score is doing narrative work (revealing information only in music), flag it. If dialogue is doing emotional work alone (without support from sound design or score), flag it.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Every distinct sound element in the scene is listed with timing and classification | Y/N |
| At least one bridge between diegetic and non-diegetic sound is identified | Y/N |
| Each classified sound has a loudness and frequency notation | Y/N |
| At least two discrepancies between sound inference and visual content are documented | Y/N |
| Every sound element is assigned a functional role | Y/N |
| Non-diegetic elements are tagged as smooth, jarring, functional, or disorienting | Y/N |

## Red Flags

- No bridges found. Either the scene is exceptionally clean (rare) or the boundary between diegetic and non-diegetic was not carefully examined.
- All non-diegetic sounds are tagged "smooth." This suggests the analysis is describing what works, not interrogating the choices. Mark some as disorienting or jarring to test your perception.
- Functional load is evenly distributed across all elements. Some sounds are ornamental — if you can't name any, the inventory was too coarse.
- Discrepancies between sound and image were not recorded. This is the highest-value output; absence suggests the analysis was shallow.
- A sound element is classified as diegetic but cannot be visually sourced, and no explanation is offered. This ambiguity matters — call it out.

## Output Format

```
## Sound Analysis Report

**Scene:** <title, timecode range>

### Inventory and Classification
| Time (s) | Element | Source | Diegetic? | Loudness | Frequency | Duration |
|---|---|---|---|---|---|---|
| 0–3 | Room ambience | world | Y | = | mid/low | 3s |
| 1.2 | Character A dialogue | A on-screen | Y | = | mid | ongoing |
| 2.8 | Footsteps | off-screen B | Y (implied) | - | mid/high | 1.2s |
| 3.5 | Orchestral swell | score | N | + | high/mid | 4s |

### Bridges and Transitions
1. **At 3.5s:** Character B's breathing transitions into orchestral swell
   - Type: smooth
   - Effect: Functional — marks shift from external action to internal state
2. ...

### Sound–Image Discrepancies
1. **At 1.8s:** Sound suggests an empty hallway; image shows a crowded office
   - Inference gap: Audio was recorded separately; spatial contradiction
2. ...

### Functional Load Assignment
| Element | Role | Notes |
|---|---|---|
| Dialogue | Narrative-critical | Delivers plot point |
| Score (3.5–7.5s) | Emotional-critical | Carries the scene's dread |
| Room ambience | Environmental | World-building |

### Key Findings
- Non-diegetic score carries emotional weight that dialogue alone does not establish
- Bridge at 3.5s is key transition point; disrupting it would flatten the scene
- Sound design emphasizes isolation (minimal environmental ambience) while image emphasizes crowding

### Confidence
<high/medium/low> — <justification>
```
