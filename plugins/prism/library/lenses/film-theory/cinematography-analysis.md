---
name: cinematography-analysis
display_name: Cinematography Analysis
class: lens
underlying_class: native
domain: film-theory
source: Cinematographers Guild; formalized in film theory by Syd Field, ASC handbooks; modern codification from *In the Blink of an Eye* (Walter Murch)
best_for:
  - Diagnosing visual storytelling choices in shot sequences
  - Training eye to see compositional intent vs. accident
  - Auditing whether image supports narrative or undermines it
one_liner: "Read visual intent through framing, optics, movement, lighting, and color."
---

# Cinematography Analysis

## Overview
Cinematography operates across five interdependent dimensions — framing (composition), lens choice (focal length and depth of field), camera movement (spatial and temporal rhythm), lighting (contrast and mood), and color (palette and grading). Rather than evaluating each as isolated technique, this lens examines how they work in concert to either reinforce or contradict the narrative moment. Practitioners use this to audit whether visual choices are serving story or merely decorating it, and to surface when cinematography contradicts dialogue or plot.

## Analytical Procedure

### Phase 1 — Inventory the Shot

Select a single shot (5–60 seconds of continuous image). Do not move to Phase 2 until you can describe this shot in purely visual terms.

1. **Describe framing without interpretation.** What is in the center, left third, right third, foreground, mid-ground, background? Name objects and people, not emotions. Example: "Subject is center-left, face in left-third rule; window reflection in background right; out-of-focus lamp in immediate foreground."

2. **Identify the lens.** Estimate focal length (wide: 14–35mm; standard: 50mm; long: 75–200mm+) by observing:
   - Perspective distortion: exaggerated depth = wide; compressed space = long
   - Depth of field: shallow focus = longer focal length or wider aperture; deep focus = wider lens or stopped down
   - Field of view: how much space is visible edge-to-edge

3. **Document camera movement.** Classify as static, pan (horizontal), tilt (vertical), dolly (toward/away), crane (vertical lift), steadicam (smooth tracking), or combination. Note direction, speed, and whether movement starts/ends the shot or occurs during.

4. **Map the light.** Identify key light direction (front, side, back, top, none). Estimate contrast ratio (soft/even vs. high-contrast). Note colored gels, practicals (lights within the scene), shadows cast and their edge quality (hard or soft).

5. **Extract the color palette.** List dominant hues (not just "blue and orange" — be specific: "cyan walls, amber desk lamp, neutral skin tone"). Note saturation (vibrant, muted, desaturated). Is there color grading applied (overall warmth shift, one color boosted, etc.)?

### Phase 2 — Relate to Narrative Moment

Do not skip this phase. Cinematography divorced from story is decoration.

6. **State the narrative function of this moment in one sentence.** What is happening in the story? Example: "Character realizes they've been betrayed."

7. **For each of the five dimensions, ask: Does this choice reinforce or contradict the narrative?**
   - **Framing:** Does composition guide the eye to what matters narratively? Does it isolate or connect characters?
   - **Lens:** Does focal length create psychological distance or intimacy? Does depth of field isolate subject or connect to environment?
   - **Movement:** Does camera movement amplify tension, reveal information, or undermine the moment with busyness?
   - **Lighting:** Does contrast and direction convey mood that matches the story beat? Are shadows hiding or revealing?
   - **Color:** Does the palette evoke the emotional state of the character or scene? Or does it look arbitrary?

   Answer with "reinforces," "contradicts," or "neutral" for each. Provide one-sentence justification for each.

### Phase 3 — Surface Hidden Choices

8. **Identify what *isn't* shown.** What is outside the frame? Is that absence intentional (to create mystery or withhold information) or accidental (sloppy framing)?

9. **Check for dominance hierarchy.** In multi-character shots, which person draws the eye first? Is that the character whose agency matters at this moment? If not, is that discrepancy intentional?

10. **Trace the cut.** If this shot follows another, does the new framing, lens, or lighting choice change our relationship to the same space or character? Does the cut feel motivated or arbitrary?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Shot described in purely visual terms with no interpretive language | Y/N |
| Focal length estimated with evidence (distortion, DoF, field of view) | Y/N |
| Camera movement classified and direction/speed noted | Y/N |
| Light mapped (key direction, contrast ratio, gels/practicals listed) | Y/N |
| Color palette listed with saturation and grading notes | Y/N |
| Narrative function stated in one sentence | Y/N |
| All five dimensions assessed as reinforce/contradict/neutral with justification | Y/N |
| Absence (out-of-frame) explicitly addressed | Y/N |
| Dominance hierarchy identified and evaluated against narrative need | Y/N |

## Red Flags

- The shot is described entirely in emotional terms ("moody," "intimate," "aggressive"). This is projection, not analysis. Go back to Phase 1.
- Focal length is guessed without reference to perspective or depth of field. Focal length cannot be assumed — it must be observed.
- All five dimensions are rated "neutral." Either the shot is purely functional (possible, but rare) or the assessment wasn't adversarial. Push harder on which choices could have been different.
- Narrative function is vague ("the character is having feelings"). Restate it as a story event. Cinematography serves plot beats, not abstract mood.
- Cut analysis is missing. A shot does not exist in isolation; its meaning shifts based on what precedes it.
- The assessment concludes cinematography is "good" or "bad" without naming what it serves. The verdict is always relative to narrative function.

## Output Format

```
## Cinematography Analysis

**Shot:** <timestamp or scene identifier>
**Duration:** <seconds>

**Narrative Function:**
<one-sentence story event>

### Phase 1 — Visual Inventory

**Framing:**
<center, thirds, foreground/mid/background placement; specific objects and people named>

**Lens:**
<estimated focal length with evidence>
- Perspective distortion: <observation>
- Depth of field: <observation>
- Field of view: <observation>

**Camera Movement:**
<classification; direction; speed; scope (static/during/bookending)>

**Lighting:**
- Key direction: <front/side/back/top/none>
- Contrast ratio: <soft/even vs. high-contrast>
- Colored gels: <yes/no; which colors>
- Practicals: <lights within the frame>
- Shadow edge quality: <hard/soft>

**Color Palette:**
- Dominant hues: <list with specificity>
- Saturation: <vibrant/muted/desaturated>
- Grading: <applied shift; if none, note>

### Phase 2 — Narrative Alignment

| Dimension | Framing | Lens | Movement | Lighting | Color |
|---|---|---|---|---|---|
| **Verdict** | Reinforces / Contradicts / Neutral | ... | ... | ... | ... |
| **Justification** | <one sentence> | <one sentence> | <one sentence> | <one sentence> | <one sentence> |

### Phase 3 — Hidden Choices

**Out-of-Frame:**
<What is not shown; is this intentional?>

**Dominance Hierarchy:**
<Which figure draws eye first; does this match narrative agency at this moment?>

**Cut Context:**
<How does this shot's framing/lens/light differ from the preceding shot; is the cut motivated?>

### Confidence
<high | medium | low> — <justification>
```
