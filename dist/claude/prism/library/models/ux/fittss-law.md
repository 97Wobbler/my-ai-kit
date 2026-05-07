---
name: fittss-law
display_name: Fitts's Law
class: model
underlying_class: native
domain: ux
source: Paul M. Fitts, "The information capacity of the human motor system in controlling the amplitude of movement," Journal of Experimental Psychology, 1954
best_for:
  - Predicting pointing and selection task completion time from target size and distance
  - Evaluating UI layouts for motor efficiency
  - Comparing input modalities (mouse, touchscreen, stylus, eye-gaze)
one_liner: "Motor performance model predicting movement time from target size and distance."
---

# Fitts's Law

## Overview

Fitts's Law is a quantitative model of human sensorimotor performance that predicts the time required to move to and select a target on the basis of two factors: the distance to the target and the target's size. The model is predictive, not prescriptive — it describes a fundamental constraint of the human motor system rather than a design rule. The central claim is that smaller targets or greater distances produce longer movement times, and the relationship is logarithmic rather than linear. Fitts's Law is widely validated across pointing devices (mouse, touchscreen, stylus, eye-gaze) and is load-bearing in UX design: it explains why button layouts matter, why mobile targets must be larger than desktop ones, and why edge-of-screen targets are faster than center targets (distance to edge = 0). Applying the law to a concrete interface requires instantiating the core equation against the specific geometry and input modality in question.

## Core Variables and Relationships

The fundamental relationship is expressed as:

    MT = a + b · log₂(D/W + 1)

where:

- **MT** (Movement Time, in milliseconds) is the time from movement start to successful target selection.
- **D** (Distance) is the distance in pixels (or physical units) from the starting position (usually cursor/finger) to the target center.
- **W** (Width) is the effective width of the target in the direction of movement — typically the smaller dimension if the target is rectangular, or the diameter if circular.
- **a** and **b** are empirically fitted constants that depend on the input modality and the person's skill level:
  - **a** (intercept) ≈ 100–200 ms, representing non-movement overhead (decision time, visual processing, motor initiation).
  - **b** (slope) ≈ 100–150 ms per "bit" of information, representing the fundamental rate at which the motor system can acquire information to home in on the target. Smaller b indicates faster performance.
- The term **log₂(D/W + 1)** is the "Index of Difficulty" (ID) in bits — it measures the task's motor complexity. Larger ID (distant + small target) = longer MT.

Key drivers of MT:

- **Target width W** — inversely related to MT. Doubling W (e.g., 20px → 40px) reduces MT by ~100–150 ms. Smaller targets require finer motor control and are subject to larger relative error.
- **Distance D** — directly related to MT. Doubling D (e.g., 100px → 200px) increases MT by ~100–150 ms. Greater distance means more spatial uncertainty to resolve.
- **Input modality** — changes a and b:
  - **Mouse**: b ≈ 100–130 ms/bit (fast, precise, low overhead).
  - **Touchscreen**: b ≈ 130–160 ms/bit (slightly slower due to lack of hover feedback and occlusion of the target by the finger).
  - **Stylus**: b ≈ 90–120 ms/bit (precise, sometimes faster than mouse in controlled settings).
  - **Eye-gaze**: b ≈ 150–200 ms/bit (slower, noisier signal, requires dwell confirmation).
- **User skill and familiarity** — regular users have lower a and b; novices are slower in both categories.
- **Target shape and geometry** — circular or square targets of the same area can have different effective widths depending on approach angle; corner or edge targets have W = 0 in one direction (infinite size in that axis) and are therefore faster to select.

## Key Predictions

- **Edge and corner targeting is fastest.** Because the effective width W in the perpendicular direction is infinite (the screen boundary acts as a "virtual wall"), corner and edge targets have shorter MT than centered targets of the same nominal size. Buttons at screen edges are typically 20–30% faster to acquire than buttons in the center.

- **Doubling button size reduces MT by less than 100 ms, but decreases selection errors by ~25–40%.** Larger targets have both faster acquisition time and larger error tolerance; this creates a trade-off: very small targets are both slow and error-prone.

- **Touchscreen targets should be at least 44–48 px across (device-independent pixels) to match mouse-pointer pointing speed.** Because fingers are less precise than cursors and occlude the target, a touchscreen button must be roughly 2× the nominal mouse target size to achieve comparable MT. Smaller mobile targets incur substantial speed and accuracy penalties.

- **Mobile virtual keyboards are inherently slow because keys are small (W ≈ 30–40 px) and distant from each other.** Fitts's Law predicts that typical key-to-key distance + key width yields ID ≈ 4–5 bits, corresponding to MT ≈ 600–1000 ms per keystroke on mobile. This explains why mobile text entry is an order of magnitude slower than desktop typing.

- **A target's effective width in the direction of approach is what matters, not its visual area.** A tall, narrow button (e.g., 10 px wide × 100 px tall) has effective W ≈ 10 px when approached horizontally and is slow; the same button is fast when approached vertically. This predicts that menu layouts and gesture targets must account for approach direction.

- **Log-linear relationship means diminishing returns for large movements.** Adding 50 px to a 100 px movement increases MT by ~100 ms. Adding 50 px to a 1000 px movement increases MT by only ~30 ms. This explains why mouse acceleration and flick gestures are beneficial: they linearize the relationship for long distances.

## Application Procedure

Instantiate Fitts's Law against a concrete pointing task in your interface.

1. **Define the task precisely.** Identify the starting position (where the cursor/finger begins), the target (what is being selected), and the target's location. Is it a single tap, or a multi-step sequence (e.g., drag-and-drop)? For sequences, apply the law to each movement separately.

2. **Measure or estimate distance D.** If the target is at a known pixel location, compute Euclidean distance from the starting position (usually the user's current cursor/finger, or a default starting point like screen center). Record D in the same units as W (pixels, mm, etc.).

3. **Measure or estimate effective target width W.** 
   - For rectangular targets, use the dimension perpendicular to the direction of approach. If you are moving horizontally to a button, W is the button's height; if moving diagonally, estimate the width in the diagonal direction.
   - For circular targets, W is the diameter.
   - For edge/corner targets, W is bounded by the screen edge (infinite width in the perpendicular direction); treat this as a special case (faster).
   - Document the target's actual visual size and the approach angle, as these determine effective W.

4. **Compute the Index of Difficulty (ID).** Calculate ID = log₂(D/W + 1). This is the task's motor complexity in bits.

5. **Look up or estimate the constants a and b for your input modality.**
   - Use published values if available (see Boundary Conditions for citations).
   - If using a new modality or population, conduct a small calibration study (5–10 users, 10–20 trials per condition).

6. **Compute predicted MT** using MT = a + b · ID. Record the result in milliseconds.

7. **Check boundary conditions** (see below). If any apply strongly, flag that Fitts's Law may not be the bottleneck and alternative factors may dominate.

8. **Compare across alternatives.** Apply the same procedure to multiple UI layouts or target placements. The one with the lowest predicted MT is predicted to be fastest in practice.

## Boundary Conditions

Fitts's Law applies well to fast, visually-guided pointing in open space. It breaks down or becomes misleading under several conditions:

- **Cognitive load or decision time dominates.** If the user must read a label, search for a target, or decide whether to click it, that decision time (which is part of a, the intercept) dwarfs the motor time. Fitts's Law predicts the motor component only; it does not predict total task time when search or deliberation is the bottleneck. Example: finding a button in a cluttered menu is slow because of search, not because of motor time.

- **Multiple targets and visual search.** Fitts's Law applies to a single, known target. When the user must scan a list or grid to find the target (visual search), the scan time can exceed motor time by 2–3×. The law is insufficient for predicting performance in complex, unfamiliar layouts.

- **Targets that move or appear dynamically.** Fitts's Law assumes the target is stationary when the movement begins. Moving targets, animated entries, or occlusion by other elements introduce additional uncertainty and can increase MT beyond the model's prediction.

- **Error correction and target re-acquisition.** Fitts's Law predicts the time to first acquisition. If the target is missed and the user must correct, total task time includes a second trial. High-error tasks (small W, cluttered layout) incur hidden MT cost from corrections; the model does not capture this.

- **Skill and learning plateaus.** Fitts's Law assumes the user has reached a stable, practiced state. Novices exhibit higher a and b; learning curves mean MT decreases over trials. The law does not predict learning, only steady-state performance.

- **Non-ballistic movement or tremor.** Fitts's Law assumes a single, ballistic motor movement. Users with tremor, fatigue, or involuntary movement (e.g., older adults, people with Parkinson's disease) exhibit higher b and sometimes nonlinear MT growth. The law underestimates difficulty in these populations.

- **Multimodal or compound tasks.** Fitts's Law predicts uniaxial or 2D pointing. Tasks that involve rotation, scaling, or 3D targeting require extensions (Accot & Zhai's Steering Law for path tasks, or 3D variants). The 2D law is insufficient.

## Output Format

```
## Fitts's Law Analysis: <task name>

**Task:** <starting position → target location>
**Input modality:** <mouse / touchscreen / stylus / eye-gaze / other>

### Measurements
| Parameter | Value | Notes |
|---|---|---|
| Distance D | <px or units> | measured from start to target center |
| Target width W | <px or units> | effective width in approach direction |
| Index of Difficulty | <ID bits> | log₂(D/W + 1) |

### Model constants
| Constant | Value | Source / justification |
|---|---|---|
| a (intercept) | <ms> | typical <100–200 ms> for modality |
| b (slope) | <ms/bit> | typical <100–160 ms/bit> for modality |

### Prediction
- **Predicted MT:** <ms>
- **Confidence band:** ±<15–25%> (typical measurement noise)

### Comparison (if multiple layouts)
| Layout | D | W | ID | Predicted MT |
|---|---|---|---|---|
| Current | ... | ... | ... | ... ms |
| Alternative A | ... | ... | ... | ... ms |
| Alternative B | ... | ... | ... | ... ms |
| Fastest | | | | <alternative>|

### Boundary-condition check
- Cognitive load dominant: <yes / no — if yes, search/decision time likely > motor time>
- Visual search required: <yes / no — if yes, add ~500–1500 ms for scan>
- Dynamic or moving target: <yes / no — if yes, add uncertainty>
- User population atypical: <yes / no — if yes, adjust a/b empirically>
- Compound / 3D task: <yes / no — if yes, use Steering Law or 3D extension>

### Confidence: high | medium | low
<reasoning: how well constants a/b fit the modality + whether boundary
conditions hold + whether target geometry is standard or unusual>
```
