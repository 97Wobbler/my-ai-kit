---
name: editing-analysis
display_name: Editing Analysis
class: lens
underlying_class: native
domain: film-theory
source: Soviet montage theory (Eisenstein, Pudovkin, Kuleshov, 1920s); formalized in contemporary film grammar
best_for:
  - Identifying the functional role of a cut in relation to narrative and visual rhythm
  - Diagnosing editing mistakes by understanding what each cut type is designed to accomplish
  - Building coherence across a sequence by matching cut types to dramatic intent
one_liner: "Diagnose editorial intent and effect by classifying cut types and their functions."
---

# Editing Analysis

## Overview

Editing Analysis examines individual cuts in a film sequence by categorizing the type of cut and measuring whether it serves its intended function. A cut is a transition from one shot to another; its type (match, jump, cross-cut, etc.) carries meaning and guides the viewer's attention and emotional state. Practitioners use this lens when a sequence feels disjointed, when the pacing seems wrong, or when they need to verify that editorial choices align with the story's dramatic beats. The discipline is matching cut type to intent — a jump cut that should be invisible makes itself visible; an invisible cut in a moment meant to disorient damages the effect.

## Analytical Procedure

### Step 1 — Identify the Sequence and Mark All Cuts

1. **Isolate the sequence** you are analyzing (a scene, a montage, or a continuous dramatic moment — typically 30 seconds to 3 minutes).

2. **Timestamp each cut.** Use frame-accurate timing if possible; shot duration is secondary. List cuts in chronological order.

3. **For each cut, document:**
   - Timecode
   - Outgoing shot (framing, subject, camera movement if any)
   - Incoming shot (framing, subject, camera movement if any)
   - Shot duration (seconds)

### Step 2 — Classify Each Cut by Type

For each cut, assign it to one of the following categories. A single cut may belong to multiple types; list all that apply.

| Cut Type | Definition | Intent |
|---|---|---|
| **Match cut** | Outgoing and incoming frames match on action, position, or geometry. Viewer perceives continuity. | Preserve spatial/temporal logic; let action flow invisibly across shots. |
| **Jump cut** | Outgoing and incoming shots break spatial or temporal continuity. Jolt is visible. | Signal discontinuity, time passage, mental disruption, or rhythmic punctuation. |
| **Cross-cut (parallel action)** | Alternates between two or more actions happening simultaneously in different locations. | Build tension, show relationship between actions, compress dramatic time. |
| **Cut on action** | Transition occurs during a character's gesture or movement; the action completes in the next shot. | Smooth flow despite camera angle change; motion masks the cut. |
| **Graphic match** | Shapes, colors, or lines in the outgoing frame visually echo in the incoming frame. | Create visual harmony; link thematic or emotional content without narrative logic. |
| **Transition match** | Incoming shot is a zoomed, panned, or rotated version of the outgoing shot. Geometric transformation links them. | Smooth reframing; emphasize a detail or shift focus within a space. |
| **Reaction/cutaway** | Cut to a character's response or to contextual detail while another action continues off-screen. | Reveal emotional subtext; expand scene geography; build rhythm. |
| **L-cut / J-cut** | Audio and video cuts are staggered (sound precedes or follows image change by 1+ frames). | Smooth pacing; let dialogue or sound guide attention before image arrives. |

### Step 3 — Assess Functional Success

For each cut, answer these questions:

1. **What is this cut meant to accomplish?** (e.g., "maintain continuity," "signal time jump," "build urgency")
   - State the intent in one clause. Infer intent from dramatic context if not explicitly discussed in production notes.

2. **Does the cut type match the intent?**
   - If intent is continuity, is it a match cut or cut-on-action? Or does a jump cut sabotage the effect?
   - If intent is discontinuity, is it a jump cut or graphic mismatch? Or does a match cut hide what should be visible?
   - If intent is emotional response, is there a reaction cut? Or does the camera stay locked on the action?

3. **What does the viewer experience at this cut?**
   - Smooth/invisible (did not register the transition)
   - Noticeable but coherent (saw the transition; understood why)
   - Jarring/broken (transition contradicts intent or confuses geography)

### Step 4 — Trace Cumulative Pacing

1. **Calculate average shot duration** for the sequence: total duration ÷ number of shots.

2. **Identify deviations.** Shots much shorter than average create urgency; shots much longer create contemplation or suspense.

3. **Ask:** Does the pacing curve match the dramatic curve? Should tension be rising (cuts accelerating) or falling (cuts slowing)? Does the editing achieve it?

### Step 5 — Identify Patterns and Anomalies

1. **Cluster cuts by type.** How many match cuts, jump cuts, reaction cuts, etc.?

2. **Check for overuse or absence.** Is every transition a match cut (stale rhythm)? Are jump cuts absent when narrative calls for rupture? Are reaction cuts missing during emotional peaks?

3. **Map intent vs. type.** Create a simple table:

| Timestamp | Intent | Cut Type | Success? |
|---|---|---|---|
| 0:00–0:05 | Maintain spatial continuity | Match cut | Y |
| 0:05–0:10 | Signal time jump | Jump cut | Y |
| 0:10–0:18 | Build urgency | Match cut | N (pacing undermines intent) |

## Evaluation Criteria

| Check | Pass |
|---|---|
| All cuts in sequence are identified and timestamped | Y/N |
| Each cut is assigned at least one type from the taxonomy | Y/N |
| Stated intent for each cut is present (inferred or documented) | Y/N |
| Cut type matches intent in ≥80% of cuts | Y/N |
| Average shot duration is calculated and deviations noted | Y/N |
| Pacing curve is assessed against dramatic curve | Y/N |
| At least one pattern (overuse, absence, or mismatch) is identified | Y/N |

## Red Flags

- No jump cuts or reaction cuts exist in a dramatic peak. The editing may be inert at the moment of highest emotional demand.
- All match cuts, no variation. The sequence feels mechanical or TV-like; rhythm is flattened.
- Intent cannot be inferred because the cut makes no spatial or narrative sense. Either the scene was not understood during editing or the takes available were incompatible.
- Pacing accelerates where the story is meant to linger, or decelerates where tension should rise. The editing works against the story.
- Cut types are labeled correctly but the functional purpose of each cut is never stated. Categorization without intent is academic.
- Graphic matches or L-cuts are present but were unintentional (revealed through production notes or storyboards). Unintended effects can be strength or weakness depending on whether they reinforce or contradict dramatic intent.

## Output Format

```
## Editing Analysis Report

**Sequence:**
<Title, scene description, timecode range>

**Duration:** <total seconds>  
**Number of shots:** <N>  
**Average shot duration:** <seconds>

### Cut-by-Cut Assessment

| Time | Outgoing | Incoming | Type | Intent | Success | Notes |
|---|---|---|---|---|---|---|
| 0:00–0:03 | MCU, character at door | CU, hand on knob | Match, cut-on-action | Maintain spatial continuity | Y | Action masks transition |
| 0:03–0:07 | LS, door opens to hallway | MS, character enters hallway | Match | Extend action | Y | Clean geography |
| 0:07–0:12 | MS, character walking (front) | CU, feet on tiles | Reaction/cutaway, graphic match | Emphasize isolation | Y | Tiles echo earlier set |
| ... | ... | ... | ... | ... | ... | ... |

### Pacing Analysis

**Dramatic curve:** <rising, falling, plateau, oscillating>  
**Pacing curve:** <accelerating (cuts shorter), decelerating (cuts longer), flat>  
**Alignment:** <match/mismatch and why>

Example shot durations: 0:00–0:03 (3s), 0:03–0:07 (4s), 0:07–0:12 (5s)  
Trend: gradual lengthening as sequence moves from action to introspection.

### Cut Type Distribution

- Match cuts: <count>
- Jump cuts: <count>
- Cut-on-action: <count>
- Reaction/cutaway: <count>
- Graphic matches: <count>
- L-cuts: <count>
- Other: <count>

### Pattern Analysis

**Strengths:**
- <Pattern observed with functional effect>
- <Pattern observed with functional effect>

**Weaknesses or anomalies:**
- <Missing cut type or overused type with impact>
- <Mismatch between intent and execution>

### Confidence
<high | medium | low> — <justification>

Example: "high — all cuts were identifiable, intent inferred from scene context and dialogue, 90% of cuts matched intent, pacing curve aligned with dramatic arc. One cut (0:45) remains ambiguous because the outgoing take was unclear on playback."
```
