---
name: schelling-focal-points
display_name: Schelling Focal Points
class: model
underlying_class: native
domain: game-theory
source: Thomas C. Schelling, "The Strategy of Conflict," Harvard University Press, 1960
best_for:
  - Predicting convergence outcomes in coordination games where communication is absent or limited
  - Explaining why actors coordinate on culturally salient conventions rather than other equilibria
  - Analyzing tacit coordination in repeated interactions and institutional design
one_liner: "In coordination games without communication, players converge on outcomes with cultural salience, historical precedent, or mathematical prominence."
---

# Schelling Focal Points

## Overview

Schelling's Focal Points model claims that in games where multiple equilibria exist and players cannot communicate, actors will coordinate on an outcome that stands out as **salient, prominent, or conventionally significant** within their shared cultural context. The model is fundamentally about *equilibrium selection*: in a coordination game, many outcomes are rational (all players' incentives align to reach them), but which one will actually occur? Standard game theory is silent; Schelling's insight is that the answer is not arbitrary—it is predictable from properties of the options themselves: their names, numbers, historical associations, symmetries, and cultural meaning. The model is descriptive and predictive: it explains observed coordination and allows prediction of which outcome will be selected when multiple equilibria coexist.

## Core Variables and Relationships

The salience of a potential focal point depends on several interacting factors:

1. **Cultural or historical convention** — outcomes that have been used before or carry deep cultural meaning.
   - Prior coordination on the same outcome (path dependence)
   - Explicit social norms or etiquette governing the choice
   - Religious, national, or ethnic significance
   - Time depth of the convention (older conventions stronger)

2. **Mathematical or structural prominence** — outcomes that stand out by their properties, independent of context.
   - Symmetry (e.g., meeting at the center of a city, not the corner)
   - Boundary or endpoint effects (choosing zero or maximum rather than intermediate values)
   - Round numbers or "nice" numbers (50, 100, rather than 47 or 83)
   - Uniqueness of a property (the only option of its kind)

3. **Cognitive salience** — outcomes that are easier to see, name, or remember.
   - Perceptual prominence (Grand Central Terminal at noon is more salient than a random subway entrance)
   - Linguistic simplicity (red rather than "reddish-brown")
   - Visual distinctiveness or markers
   - Ease of communication (even in indirect form)

4. **Payoff symmetry** — when outcomes offer symmetric payoffs to players.
   - Equal division is salient when players are identical and the problem is symmetric
   - The payoff structure itself does not determine the focal point but can reinforce salience

The **convergence mechanism** is not explicit communication but a process of mutual reasoning: "I think *he* will think that *I* think that *we both* recognize this outcome as special." This iterative common knowledge of salience drives coordination without explicit agreement.

## Key Predictions

- **When cultural conventions exist, players will coordinate on them even when other Pareto-dominant equilibria are available**, because the convention carries pre-existing common knowledge.

- **Symmetric problems favor symmetric solutions.** In a coordination problem between identical players with identical payoffs, the equal-division outcome will be selected even if asymmetric divisions yield higher total payoff.

- **Mathematical simplicity and boundary effects dominate in novel coordination problems.** When players have no cultural precedent, they will converge on round numbers, extremes (zero, maximum), or outcomes with unique structural properties.

- **Perceptual or named distinctiveness predicts the focal point.** The outcome that is easiest to name, visualize, or describe will be chosen — this is why "Grand Central Terminal at noon" (not midnight, not 1 p.m., not Pennsylvania Station) is the focal point in Schelling's famous example.

- **Multiple focal points can coexist and create coordination risk.** If two or more outcomes are equally salient in different subcultures or contexts, players may fail to coordinate despite both wanting to.

- **Focal points are fragile to reframing.** Changing the *labels* or *descriptions* of options can shift which outcome is salient, even if the underlying game is identical — because salience is in the mind.

## Application Procedure

Instantiate the model against a concrete coordination problem where communication is absent, limited, or unreliable.

1. **Define the coordination problem precisely.** What outcome is each player trying to reach? What does success look like? Are payoffs symmetric or asymmetric?

2. **Enumerate all equilibria in the game.** Identify outcomes where all players' incentives align: no player wants to deviate unilaterally. (If there is only one equilibrium, the model does not apply.)

3. **Apply the salience filters in order:**
   - Is there an existing cultural convention or historical precedent for coordination on one of these equilibria? If yes, that is the focal point.
   - If no convention, is the game mathematically symmetric? If yes, does one outcome have a unique structural property (center, boundary, round number)? If yes, that is salient.
   - If still multiple candidates, which outcome is easiest to name, perceive, or describe in the players' shared language or context? That is the focal point.

4. **Check the payoff structure.** Does the focal point align with a Pareto-dominant equilibrium, or is it suboptimal? Note whether the payoff structure reinforces or contradicts the salience.

5. **Assess the strength of the focal point.**
   - Is it strongly salient (e.g., "noon" vs. "11:47 a.m.")? Expect high coordination rates.
   - Is it weakly salient or contested (e.g., "center" when the city is sprawling or off-center)? Expect lower coordination rates and some probability of miscoordination.

6. **Predict the outcome.** The focal point should coordinate the players better than other equilibria, even without communication.

7. **Check boundary conditions** (below). If any apply, note that Schelling's model may not fully predict and what additional analysis is needed (e.g., learning, asymmetric information, strategic signaling).

## Boundary Conditions

Schelling's Focal Points model applies to coordination problems in which salience is the binding force. It weakens or fails under:

- **Strategic miscommunication or deliberate obfuscation.** If one player has incentive to make the salient outcome *less* obvious to the other (e.g., a buyer in a bargaining game), the buyer may obscure the focal point to shift outcome to their advantage. The model assumes good-faith coordination, not adversarial signaling.

- **Heterogeneous cultural backgrounds.** If players come from different cultures with different conventions and salience markers, what is salient to one may be invisible to the other. Coordination fails. Supplement with a model of cultural translation or prior common experiences.

- **High-dimensional or continuous choice spaces.** In discrete games (meeting at noon vs. midnight, or taking the left or right fork), focal points are crisp. In continuous games (agreeing on a price for a good), mathematical prominence is much weaker, and the model's predictive power degrades unless there is an anchor or convention.

- **Large information asymmetries.** If one player knows payoff structures or available options that the other does not, the focal point is computed on different platforms and coordination fails. Supplement with Bayesian games or signaling analysis.

- **Repeated play with learning.** If players will interact multiple times and can observe deviations, they may learn a different equilibrium than the focal point predicts (e.g., a coordination convention that emerges from play rather than salience). The model predicts the first-round outcome better than long-run behavior.

- **Outcomes that are literally unobservable or difficult to verify.** If a player cannot directly see or verify that the other player chose the intended outcome (e.g., in a hidden-action or hidden-information setting), the focal point loses force because players fear mutual misalignment and may defect to a safer, less-salient equilibrium.

## Output Format

```
## Focal Point Analysis: <coordination problem>

**Problem:** <players, objective, equilibria available>
**Payoff structure:** <symmetric / asymmetric, brief note on payoffs>

### Salience assessment
| Candidate equilibrium | Salience basis | Strength |
|---|---|---|
| <outcome A> | <convention / math / language / precedent> | Strong / Weak / Contested |
| <outcome B> | ... | ... |

### Focal point identification
**Selected focal point:** <outcome>
**Primary salience driver:** <which mechanism: convention, math, language, perceptual, symmetry>
**Secondary reinforcements:** <any other factors that reinforce this outcome>

### Coordination prediction
- Predicted outcome (Schelling): <the focal point>
- Confidence in convergence: <High / Medium / Low>
- Probability of miscoordination: <if multiple salient equilibria exist>
- Payoff consequence: <is the focal point Pareto-optimal, or do players end up in a suboptimal equilibrium?>

### Salience fragility
<is the focal point robust to reframing, or could relabeling the options shift coordination? any competing focal points?>>

### Boundary-condition check
<which of the boundary conditions apply; is the model's prediction still load-bearing given communication level, cultural homogeneity, information asymmetry, and observability?>

### Confidence: high | medium | low
<reasoning: clarity and uniqueness of salience markers + payoff structure alignment + cultural homogeneity + frequency of prior coordination on this equilibrium>
```
