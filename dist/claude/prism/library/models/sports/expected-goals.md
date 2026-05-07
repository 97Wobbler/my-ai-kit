---
name: expected-goals
display_name: Expected Goals (xG)
class: model
underlying_class: native
domain: sports
source: origin uncertain; methodology emerged in football analytics circa 2012, formalized by StatsBomb, Opta Sports, and academic soccer analytics communities
best_for:
  - Predicting shot conversion likelihood from spatial and contextual shot characteristics
  - Quantifying shot quality independently of whether it resulted in a goal
  - Comparing player and team shooting efficiency on a model-adjusted basis
one_liner: "Shot-quality model that estimates scoring probability from shot location, angle, and defensive pressure."
---

# Expected Goals (xG)

## Overview

Expected Goals (xG) is a descriptive and predictive model that assigns a probability of goal-scoring to every shot taken in football (soccer), independent of whether that shot actually resulted in a goal. The model's central claim is that shot quality — the likelihood that a given shot should score — is determined by observable spatial, temporal, and contextual variables (distance, angle, defensive pressure, goalkeeper position, shot type), and that these variables predict goal outcomes more reliably than actual outcomes do, especially over short samples. xG is primarily *descriptive* — it quantifies what happened and why — but it is also *predictive* — it forecasts true underlying shooting skill when actual goal tallies are noisy. The model underpins modern shot selection analysis, player comparison, and team efficiency evaluation in football.

## Core Variables and Relationships

xG for a shot is determined by:

1. **Distance from goal (shot range)** — increases from ~0.01 at the halfway line to ~0.4 in the penalty spot.
   - Measured in meters from the center of the goal line.
   - Non-linear relationship: each meter closer increases xG more at short range than long range.
   - Beyond 35 meters, xG typically rounds to near-zero.

2. **Angle to goal** — increases from a near-post angle to a maximum at ~20–30° from goal center, then decreases again at wide angles.
   - Measured as the angle subtended at the goal line by the shot location.
   - Shots from very tight angles (< 10° or > 80°) have xG ~0.01–0.05.
   - Central locations (15–40° from goal line) have highest xG for a given distance.

3. **Defensive pressure / occlusion** — higher pressure or more defenders between shooter and goal reduces xG.
   - Binary or multi-level variable: tight marking vs. open space.
   - Number of defenders within a threshold distance (e.g., 2 meters).
   - Goalkeeper positioning (if forward of the line, reduces xG; if beaten, increases it).

4. **Shot type** — header, weak foot, volley, etc. have different baseline xG.
   - Headers have lower xG than open-play right-footed shots from comparable distance/angle (~0.6× multiplier).
   - Volleys and half-volleys vary widely depending on control; generally lower xG.
   - Penalties have xG ~0.79 in modern football (higher for better takers).

5. **Goalkeeper quality / positioning** — not always explicitly modeled but implied in distance/angle calibration.
   - Most models are trained on average goalkeeper performance.
   - Exceptional goalkeepers may shift realized conversion rates ~1–2 percentage points below xG; poor ones above.

6. **Recent team / player shooting history** — not a direct input to xG but a lens for interpreting xG overperformance or underperformance.

The core calculation is typically:

    xG(shot) = base_xg(distance, angle) × pressure_modifier × type_modifier

where base_xg is calibrated against historical conversion rates and modifiers reflect context. Models vary in complexity; simple ones use only distance and angle; advanced ones add more variables.

## Key Predictions

- **A team that generates 1.5 xG per match will, over a full season (~38 matches), score approximately 1.1–1.3 goals per match on average**, regardless of short-term luck. The spread narrows as sample size grows.

- **Individual players with sustained shooting underperformance (e.g., xG 12 over 10 matches but only 4 goals) will tend to revert toward their xG unless there is a fundamental change in shot selection or finishing technique.** Large single-match underperformance (xG 2.0, 0 goals) is noise; sustained patterns (over 20+ shots) suggest systematic miss or tactical change.

- **Two teams with identical shot volume but different xG distributions will, over time, diverge in goal outcomes.** The team with higher average xG per shot will finish higher despite similar "chance creation" counts.

- **Defender-heavy teams that generate lower xG per shot will sustain lower goal-per-match output even if defensive organization is superior**, unless they also shift toward higher-quality chances (which usually requires attacking quality).

- **xG underperformance at the team level (e.g., 15 xG, 8 goals, a −7 goal differential) is sometimes predictive of poor finishing coaching, but more often regresses toward xG in the next sample.** Goalkeeper injury or unusually poor conversion skill is the primary persistent cause; luck is more common.

- **A single dramatic miss (xG 0.8, open goal, shot wide) has the same numerical xG but dramatically different narrative weight than a low-xG lucky goal (xG 0.03, deflection).** Outcome-based evaluation misses this; xG-based evaluation captures shot quality but can overweight individual misses.

## Application Procedure

Instantiate xG analysis against a specific shooting event, player, match, or season.

1. **Define the scope.** Are you evaluating a single shot, a player's season, a team's tactical shift, or a match? Specify the time window and unit (shot, player-season, match, season).

2. **Collect shot data.** For each shot:
   - Location (x, y coordinates on the pitch, usually normalized to 0–100 for length and width).
   - Distance and angle to goal (calculate or use model's pre-computed values).
   - Shot type (open play, header, penalty, free kick, etc.).
   - Defensive pressure / number of defenders within 2 meters.
   - Goalkeeper positioning (if available; often omitted from public models).
   - Outcome (goal or no goal).

3. **Assign xG to each shot** using an xG model (e.g., StatsBomb, Understat, Opta). Most models are publicly available via platforms like Understat or calculated via published lookup tables. Record xG value per shot.

4. **Aggregate xG.** Sum xG across the scope (e.g., player-season xG, team-match xG).

5. **Calculate Actual Goals (G) and xG Differential (ΔG).**
   - ΔG = Actual Goals − xG. Positive means overperforming; negative means underperforming.
   - Example: 15 xG, 12 goals → ΔG = −3 (underperforming by 3 expected goals).

6. **Interpret the differential in context.**
   - Single match or < 10 shots: Likely noise (±2 ΔG is normal variance).
   - Player over 30+ shots: Sustained differential (ΔG > 1.5 or < −1.5) may indicate finishing skill, tactical luck, or data quality issues.
   - Season-level: ΔG > 2 or < −2 is noteworthy but often reverts; xG is more predictive of *true* underlying skill than any single season's goal total.

7. **Cross-check boundary conditions** (below). If any apply, qualify your inference.

8. **Generate the prediction or diagnosis.**
   - If evaluating a player: Is their shooting skill better/worse than goals suggest, or is the differential due to luck?
   - If evaluating a team: Are we creating high-quality chances (high xG per shot) or just high volume?
   - If forecasting: xG is more stable than goal totals; use it to predict next-season goal output.

## Boundary Conditions

xG is a reliable model for typical open-play shots but breaks down or becomes misleading in several contexts:

- **Set pieces (penalties, free kicks from dangerous positions).** These are often modeled separately or excluded. Penalty xG ~0.79 is stable, but free-kick xG depends heavily on shooter skill and goalkeeper quality in ways the general model does not capture. Direct free-kick goals are often treated as xG 0 or a bespoke value.

- **Very low-probability shots (xG < 0.05).** Calibration is poor at the tail; a shot with xG 0.02 does not meaningfully differ from xG 0.01 in predictive power. The distinction between "very unlikely" and "extremely unlikely" is noise for these shots.

- **Goalkeeper heroics or blunders not captured by positioning.** xG assumes average goalkeeper reflexes and decision-making. An extraordinary save (world-class reflexes) or an error (poor positioning) can shift realized conversion by 1–2 percentage points relative to xG. This is usually small but can matter in close matches.

- **Data quality and model calibration drift.** Different xG models (StatsBomb, Understat, Opta) can assign noticeably different values to the same shot because they weight variables differently or train on different historical data. Always specify which model was used. Recalibration over time as playing style changes (e.g., increased press, longer-range shots) can also shift baselines.

- **Player-specific factors not in the model: weak foot, preference, fatigue, confidence.** A shot taken by a left-footed player on their right foot has the same spatial xG as a natural right-footed shot, but lower actual conversion. xG models sometimes include weak-foot modifiers; many do not.

- **Tactical context changes.** A team that shifts from "create a few high-xG chances" to "lots of low-xG shots" will see xG per shot drop, but this is often a *choice*, not a sign of worse finishing. The model captures shot quality but not shot selection philosophy.

## Output Format

```
## xG Analysis: <player / team / match / period>

**Scope:** <unit of analysis: e.g., "Player season 2025–26", "Team match 2026-04-11">
**xG model used:** <StatsBomb, Understat, Opta, or custom; xG model version if known>

### Shot summary
| Metric | Value | Notes |
|---|---|---|
| Total shots | ... | open play only / including set pieces |
| Total xG | ... | sum of xG across shots |
| Actual goals | ... | goals scored |
| xG differential (ΔG) | ... | Actual − xG; positive = overperforming |
| Avg xG per shot | ... | quality of chances |
| Shot distance (avg) | ... | meters |
| Shot distance (median) | ... | emphasizes volume of high-danger chances |

### Shooting efficiency
- Conversion rate: Actual goals / Total shots (%)
- xG-implied conversion: xG / Total shots (%)
- Differential analysis: <Is the player/team over/underperforming relative to xG? By how much, and is it likely persistent or noise?>

### Key observations
- Shot type distribution: <headers, open play, weak foot, etc.>
- Pressure patterns: <high volume of open-space shots vs. tight-marking shots>
- Notable outliers: <any xG << 0.1 goals, or xG > 0.6 misses>

### Prediction / Diagnosis
- If over 30+ shots: <Do you expect the differential to persist or revert?>
- Underlying skill assessment: <Better/worse finisher than goals suggest, or just luck?>
- Next-period forecast: <Use xG as the anchor for expected goals next season / next month>

### Boundary-condition notes
- <Which of the six boundary conditions above apply?>
- <Any data quality caveats or model limitations specific to this case?>

### Confidence: high | medium | low
<Reasoning: sample size + shot-type mix + whether boundary conditions apply. High confidence for season-level team data; medium for single-player-season if set pieces are excluded; low for small samples (< 10 shots) or if goalkeeper quality or weak-foot effects are material>
```
---
