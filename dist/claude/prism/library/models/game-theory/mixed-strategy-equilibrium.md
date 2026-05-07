---
name: mixed-strategy-equilibrium
display_name: Mixed Strategy Equilibrium
class: model
underlying_class: native
domain: game-theory
source: John von Neumann & Oskar Morgenstern, Theory of Games and Economic Behavior, 1944; formalized by John Nash, "Equilibrium Points in N-Person Games," PNAS, 1950
best_for:
  - Predicting behavior in simultaneous-move games where pure strategies lead to inefficient or unstable outcomes
  - Explaining randomization and apparent irrationality in competitive or coordination failures
  - Analyzing equilibrium in sports, auctions, bargaining, and zero-sum conflicts
one_liner: "Predict optimal behavior when equilibrium is reached via probabilistic rather than pure strategies."
---

# Mixed Strategy Equilibrium

## Overview

Mixed Strategy Equilibrium claims that in games where no pure (deterministic) strategy pair is stable—where each player's best response to what the opponent does pushes the opponent away from their current choice—rational players will randomize over a subset of actions according to specific probabilities. The equilibrium is the probability distribution over actions such that each player is indifferent among the actions in their support, and no unilateral deviation (including changing the probability weights) makes them better off. The model is predictive: it says what equilibrium behavior looks like and what probability distribution rational players will adopt. Unlike pure-strategy equilibrium, mixed-strategy equilibrium is always existant in finite games—a foundational result in game theory. Applying the model to a concrete game requires the procedure below.

## Core Variables and Relationships

Mixed Strategy Equilibrium hinges on indifference and mutual best responses:

1. **Player i's mixed strategy σᵢ**: a probability distribution over player i's action set Aᵢ. If Aᵢ = {a, b}, then σᵢ(a) + σᵢ(b) = 1, and σᵢ(a) ∈ [0, 1].

2. **Indifference condition**: In equilibrium, player i must be indifferent among all actions that have strictly positive probability in σᵢ. If player i plays action a with probability p > 0 and action b with probability (1−p) > 0, then the expected payoff from action a given the opponent's mixed strategy σⱼ must equal the expected payoff from action b given σⱼ.
   - Formally: **E[u(a | σⱼ)] = E[u(b | σⱼ)]** for all a, b in the support of σᵢ.
   - If an action is in the support (played with positive probability), the expected payoff from it must equal the expected payoff from every other action in the support.

3. **Best-response property**: Neither player can improve their expected payoff by deviating unilaterally—neither by switching to a pure strategy nor by shifting probabilities.
   - If player j plays σⱼ, then no action gives player i a strictly higher payoff than the expected payoff from σᵢ.
   - Formally: **σᵢ ∈ BR(σⱼ)** and **σⱼ ∈ BR(σᵢ)**, where BR is the best-response correspondence.

4. **Support of the mixed strategy**: the set of actions played with positive probability. In equilibrium, the support is typically small; the equilibrium probability assigns zero weight to dominated actions.

5. **Key relationship**: The opponent's mixed strategy must be such that you are indifferent across your support. Conversely, your mixed strategy must leave your opponent indifferent across *their* support. This mutual indifference locks in the equilibrium probabilities.

## Key Predictions

- **In a 2×2 game with no pure-strategy equilibrium**, there exists a unique mixed-strategy equilibrium, and both players randomize over both actions. The equilibrium probabilities are determined by the payoff structure, not by any external randomization device.

- **The player who is "hurt more" by a given opponent action will randomize more heavily away from it.** In a Matching Pennies game (a zero-sum game where Player 1 wins if choices match, Player 2 wins if they don't), each player plays each action with 50% probability, but the calculation reveals that the underdog in the payoff space still randomizes with equal weight because of the indifference condition.

- **Adding a third action creates a mixed-strategy equilibrium in which one or more actions may have zero probability in equilibrium.** The support shrinks; the equilibrium may involve only a subset of available actions.

- **Correlated payoffs across actions change the equilibrium probabilities sharply.** A small change in the payoff matrix—e.g., raising the payoff to one action—shifts the equilibrium mix discontinuously. The indifference condition is sensitive to payoff structure.

- **In zero-sum games, the mixed-strategy equilibrium makes the opponent indifferent, thereby eliminating exploitability.** This is why a minimax strategy is a mixed strategy in many zero-sum games: it randomizes in a way that guarantees the opponent cannot gain an advantage.

- **Mixed-strategy equilibrium predicts observable randomization in high-stakes real games** (tennis serves, penalty kicks, currency attack timing, audits). Players who are predictable (pure strategies) are exploited; equilibrium randomization prevents exploitation.

## Application Procedure

Instantiate the model against a concrete simultaneous-move game.

1. **Define the game precisely.** Who are the players? What are their action sets (and are they finite)? What are the payoffs for each outcome? Write out the payoff matrix or bimatrix.

2. **Check for pure-strategy Nash equilibria.** For each cell in the payoff matrix, check whether each player is playing a best response to the other player's action. If a pure-strategy equilibrium exists, report it; you may not need the mixed model. If none exists, proceed.

3. **Assume a fully-mixed symmetric equilibrium** (both players play both actions with positive probability). Denote player 1's probability of playing action a as p; player 2's probability of playing action a as q.

4. **Apply the indifference condition to player 1.** Player 1 must be indifferent between playing action a and action b. Write out the expected payoff from each:
   - **E[u(a | q)] = u(a,a) · q + u(a,b) · (1−q)**
   - **E[u(b | q)] = u(b,a) · q + u(b,b) · (1−q)**
   - Set them equal and solve for q.

5. **Apply the indifference condition to player 2.** Player 2 must be indifferent between playing action a and action b. Write out the expected payoffs conditional on player 1's p, set them equal, and solve for p.

6. **Verify the solution.** Both p and q must lie in [0, 1]. If either is outside this range, the fully-mixed assumption is violated; revert to a boundary equilibrium (one player plays pure, the other mixes, or both play pure).

7. **Check that no pure action gives a strictly higher payoff than the indifference level.** This ensures that the derived mixed strategy is indeed a best response.

8. **Check boundary conditions** (below). If any apply, note what complementary analysis (incomplete information, dynamic play, learning) is needed.

9. **Report the equilibrium probabilities and the expected payoffs.**

## Boundary Conditions

Mixed Strategy Equilibrium applies cleanly to finite, simultaneous-move games with complete information. It breaks down or becomes incomplete under several conditions:

- **Incomplete information (Bayesian games).** If players are uncertain about payoffs or types, the mixed-strategy equilibrium is over action-type pairs, and the analysis is more complex. A Bayesian equilibrium may involve different mixing for different types of the same player.

- **Infinite or continuous action spaces.** The indifference approach still applies in principle (e.g., bidding in first-price auctions), but the solution method changes and equilibrium may be in a continuum of mixed strategies. The model's predictions are less precise.

- **Dynamic games (sequential move, repeated play, or learning).** In a repeated or sequential game, mixed strategies can emerge from dynamic play or learning even if the stage game has a pure equilibrium. The model does not capture how mixing arises from strategic foresight across multiple periods.

- **Correlated equilibrium or communication.** If players can communicate or correlate their play (e.g., both observing a public randomization device), they may achieve an outcome that Pareto-dominates the mixed-strategy equilibrium. The model assumes independence; communication breaks this.

- **Heterogeneous or biased beliefs.** The model assumes players hold correct beliefs about the opponent's strategy. If a player believes the opponent will play a different distribution (e.g., overestimating the opponent's rationality or assuming irrational behavior), the indifference condition no longer holds and observed mixing will differ.

- **Real-world randomization devices are imperfect.** The model assumes players can randomize exactly according to the equilibrium probabilities. In practice, humans randomize noisily or use heuristics (e.g., "alternate after a loss"). The observed frequencies will deviate from the prediction.

## Output Format

```
## Mixed Strategy Equilibrium Analysis: <game name>

**Game:** <players, action sets, payoff matrix or explicit payoffs>
**Equilibrium type:** Fully mixed | Partially mixed (specify support) | Pure (if applicable)

### Indifference calculations
**Player 1's expected payoffs:**
- E[u(action a | opponent mixes q)] = <calculation>
- E[u(action b | opponent mixes q)] = <calculation>
- Indifference yields: q = <value>

**Player 2's expected payoffs:**
- E[u(action a | opponent mixes p)] = <calculation>
- E[u(action b | opponent mixes p)] = <calculation>
- Indifference yields: p = <value>

### Equilibrium probabilities
- Player 1: σ₁(a) = p, σ₁(b) = 1−p
- Player 2: σ₂(a) = q, σ₂(b) = 1−q

### Expected payoffs at equilibrium
- Player 1: <expected utility value>
- Player 2: <expected utility value>

### Predictions and implications
- Both players are indifferent across their support: <confirm>
- No unilateral deviation improves payoff: <confirm>
- Observed behavior should exhibit randomization with frequencies: <reported probabilities>
- Exploitability if opponent deviates to pure strategy: <which player is exposed, to which deviation>

### Boundary-condition check
<which boundary conditions apply; if any, flag what complementary analysis is needed (Bayesian equilibrium, learning dynamics, communication, etc.)>

### Confidence: high | medium | low
<reasoning: clarity of payoff matrix + whether game is finite and simultaneous-move + robustness to boundary conditions + quality of belief assumption>
```
Human: Generate a model file for the following framework.

Name: Signaling Games
Slug: signaling-games
Domain: game-theory
One-liner (existing summary): information asymmetry equilibrium

Reference the two model examples from the previous request to match tone, density, and section structure exactly.

---

name: mixed-strategy-equilibrium
display_name: Mixed Strategy Equilibrium
class: model
underlying_class: native
domain: game-theory
source: John von Neumann & Oskar Morgenstern, Theory of Games and Economic Behavior, 1944; formalized by John Nash, "Equilibrium Points in N-Person Games," PNAS, 1950
best_for:
  - Predicting behavior in simultaneous-move games where pure strategies lead to inefficient or unstable outcomes
  - Explaining randomization and apparent irrationality in competitive or coordination failures
  - Analyzing equilibrium in sports, auctions, bargaining, and zero-sum conflicts
one_liner: "순수전략이 아닌 확률 혼합으로 균형을 이루는 상황에서의 최적 행동 예측"
---

(You have already received the Mixed Strategy Equilibrium model file as an example.)

Now generate the Signaling Games model file. Follow the voice and structure of the examples exactly.

---
name: signaling-games
display_name: Signaling Games
class: model
underlying_class: native
domain: game-theory
source: <determine from your knowledge>
best_for:
  - <at least 2 application contexts>
one_liner: "정보 비대칭 상황에서 신호를 통해 균형을 이루는 메커니즘"
---

Now write the full model file. Output frontmatter + body only, no preamble, no code fence around the whole file.

---
name: signaling-games
display_name: Signaling Games
class: model
underlying_class: native
domain: game-theory
source: Michael Spence, "Job Market Signaling," Quarterly Journal of Economics, 1973; developed in game-theoretic framework by Cho & Kreps, "Signaling Games and Stable Equilibria," REStud, 1987
best_for:
  - Predicting equilibrium outcomes when one player has private information (type or quality) that the other player cannot observe
  - Explaining costly signals like education, warranties, or quality investments that reveal unobservable attributes
  - Analyzing market unraveling, separating equilibria, and pooling equilibria in markets with information asymmetry
one_liner: "정보 비대칭 상황에서 신호 전달자가 자신의 유형을 공개하려 하는 메커니즘과 수신자의 신뢰 형성"
---

# Signaling Games

## Overview

Signaling Games model strategic interactions between a **Sender** who has private information about their own type or quality and a **Receiver** who does not observe the sender's type directly but observes a signal the sender chooses to send. The model claims that in equilibrium, the sender will choose a signal (education level, price, warranty terms, investment in reputation) that credibly reveals their type to the receiver, *if and only if* the cost of sending that signal is low enough for the true type and high enough for the false type. The receiver updates their beliefs about the sender's type based on the observed signal and responds accordingly. The model is both descriptive and predictive: it explains why costly signals exist and predicts which equilibria (separating, pooling, or partial pooling) will arise given the payoff and cost structure. Unlike signaling in isolation, signaling games emphasize the strategic interplay between belief updating and optimal response, which locks in the equilibrium signal.

## Core Variables and Relationships

Signaling games involve a sequence of moves and information:

1. **Nature chooses the Sender's type θ ∈ Θ** according to a prior distribution p(θ). The Receiver observes only that a sender exists, not the sender's type.

2. **The Sender observes their own type θ and chooses a signal m ∈ M.** The signal is costly; the cost depends on the sender's type. Denote the cost to a sender of type θ sending signal m as c(m, θ).

3. **The Receiver observes the signal m but not the type θ.** The Receiver updates their belief about θ using Bayes' rule (if the signal is informative). Denote the posterior belief as μ(θ | m).

4. **The Receiver chooses an action a ∈ A** based on the posterior belief μ. The receiver's payoff is u_R(a, θ), which depends on both the action chosen and the true type.

5. **Payoffs are realized.** The Sender's payoff is u_S(a, θ) − c(m, θ); the Receiver's payoff is u_R(a, θ).

**The critical relationships:**

- **Cost structure drives separability.** For two types θ_H (high) and θ_L (low), a separating equilibrium exists only if the cost ratio favors honesty: c(m_H, θ_H) < c(m_H, θ_L) and c(m_L, θ_L) < c(m_L, θ_H). The low type must find it cheaper to signal "low" than "high," and vice versa.

- **Belief updating via Bayes' rule (on the equilibrium path).** If the Receiver observes a signal m that a type θ sends with positive probability in equilibrium, the posterior is μ(θ | m) = p(θ) · P(m | θ) / Σ_θ' p(θ') · P(m | θ').

- **Best-response consistency.** The Receiver's action a(m) must be a best response to the posterior belief μ(θ | m). Formally, a(m) ∈ argmax_a E_θ ~ μ(θ|m) [u_R(a, θ)].

- **Incentive compatibility.** Each type must prefer the signal (and resulting action) they are assigned in equilibrium to any other signal (and the action that would follow). A type θ prefers signal m to signal m' if u_S(a(m), θ) − c(m, θ) ≥ u_S(a(m'), θ) − c(m', θ).

- **Equilibrium conditions:** A separating equilibrium assigns a different signal to each type, and each type is willing to send that signal (incentive compatibility) and prefers not to mimic any other type. A pooling equilibrium assigns the same signal to all types, and the receiver's belief after observing that signal equals the prior. A partially separating (or semi-pooling) equilibrium involves some types separating and others pooling.

## Key Predictions

- **A separating equilibrium exists if and only if the cost structure satisfies the single-crossing condition:** higher types find it cheaper (in relative terms) to send "high-quality" signals. When this holds, types sort themselves through signal choices; the receiver's belief becomes certain upon observing the signal.

- **Pooling can occur even when separation is feasible,** if the signaling costs are high enough that lower types cannot afford to separate. In equilibrium, all types send the same (or overlapping) signal, and the receiver's posterior remains close to the prior.

- **The Receiver may rationally ignore costly signals if the cost differential is small.** A slight change in the cost structure (e.g., education becoming cheaper for everyone) can trigger a collapse from separating to pooling equilibrium.

- **Information destruction through pooling:** In a pooling equilibrium, the private information the Sender holds is not revealed. The Receiver must take an action based on the average type, and the Sender captures no information rent. This is often inefficient compared to separation.

- **Market unraveling (the "Lemons" problem):** If signaling is costly and the low type can mimic the high type cheaply, the receiver may assign low probability to high type signals. In the extreme, only low types send signals (or no signals are sent); high types exit the market because they cannot reveal their quality cost-effectively.

- **Equilibrium multiplicity:** For a given cost structure, multiple equilibria can coexist (separating and pooling). Which equilibrium is selected depends on the off-equilibrium-path beliefs—what the Receiver believes if an unexpected signal is observed.

## Application Procedure

Instantiate the model against a market or strategic situation with information asymmetry.

1. **Identify the Sender and Receiver.** Who holds private information? Who makes the downstream decision based on that information? (Example: job applicant with hidden ability and employer making hiring decision.)

2. **Define the type space Θ and the prior p(θ).** What are the possible types, and how common is each? (Example: high ability with probability 0.3, low ability with probability 0.7.)

3. **Specify the signal space M and the cost structure c(m, θ).** What signals are available? What does it cost each type to send each signal? Write out the cost matrix.
   - Verify that the single-crossing condition holds or fails: does a higher type have lower relative cost for high-quality signals?

4. **Specify the Receiver's action space A and payoffs u_R(a, θ).** What decision does the Receiver make? How do payoffs depend on the true type? (Example: wage offer w, and the employer profits more if the worker is actually high-ability.)

5. **Specify the Sender's payoffs u_S(a, θ).** How does the Sender benefit from the Receiver's action, as a function of type? (Example: higher wage is better, but both types value wages equally—payoff difference is only from cost.)

6. **Construct the pooling equilibrium candidate.** Assume all types send the same signal m*. Compute the Receiver's posterior (equals prior) and the Receiver's best-response action a*. Check whether each type is willing to send m*: is sending m* and receiving a* better than deviating to any other signal?

7. **Construct the separating equilibrium candidate.** Assign each type a different signal: θ_H sends m_H, θ_L sends m_L. Check incentive compatibility for both types: does θ_H prefer (m_H, a_H) to (m_L, a_L) after accounting for costs? Does θ_L prefer (m_L, a_L) to (m_H, a_H)?

8. **Identify which equilibrium(ria) survive.** Apply the D1 criterion or another off-equilibrium refinement if multiple equilibria exist, to select the most plausible one.

9. **Check boundary conditions** (below). Flag if the information structure, payoff structure, or equilibrium concept assumptions are violated.

10. **Report the equilibrium: type distribution, signals, posterior beliefs, Receiver actions, and payoffs.**

## Boundary Conditions

Signaling Games assume complete information about payoff functions and preferences, and that types are exogenous. The model breaks down or becomes incomplete under several conditions:

- **Unknown cost structure to the Receiver.** If the Receiver does not know the cost function c(m, θ), or learns it imperfectly over time, the inference problem becomes more complex (Bayesian learning, experimentation). The separating equilibrium may not hold even if the cost structure would support it.

- **Endogenous type / cheap-talk signals.** If the signal is costless to send (e.g., a verbal claim) and the type is not exogenous (the Sender can invest to change their type), the model becomes a cheap-talk game or an investment game. Separating equilibrium no longer relies on cost; it relies on the Receiver ignoring non-credible claims.

- **Multiple Receivers or audience fragmentation.** If the Sender must signal to multiple audiences with different preferences (e.g., an employee signaling to multiple employers with different skill valuations), signaling becomes more complex. A signal optimal for one audience may repel another.

- **Dynamic signaling / reputation effects.** If the interaction is repeated or the Sender's type is partially revealed through past actions, the game becomes dynamic. Mixed-strategy and reputational dynamics may dominate the static signaling logic.

- **Pooling with asymmetric information at the Receiver level.** If the Receiver also has private information (e.g., the employer doesn't know their own value for the worker), the equilibrium is a Bayesian equilibrium and the analysis becomes more subtle.

- **Continuous or high-dimensional type and signal spaces.** The intuition holds, but the separating equilibrium may not exist in closed form. Numerical or approximation methods may be needed.

## Output Format

```
## Signaling Games Analysis: <market or situation>

**Sender type and prior:** θ ∈ {<types>}, p(θ) = {<probabilities>}
**Signal space M:** {<available signals>}
**Receiver action space A:** {<available actions>}

### Cost structure for signaling
| Type | Signal 1 cost | Signal 2 cost | ... |
|---|---|---|---|
| θ_H | c(m_1, θ_H) | c(m_2, θ_H) | ... |
| θ_L | c(m_1, θ_L) | c(m_2, θ_L) | ... |

**Single-crossing condition:** [Satisfied / Violated / Unclear]

### Payoff functions
**Receiver:** u_R(a, θ) = <specification>
**Sender:** u_S(a, θ) = <specification>

### Candidate equilibria
**Pooling equilibrium:**
- Common signal: m* = <signal>
- Posterior belief: μ(θ | m*) = <prior>
- Receiver action: a* = <action>
- Type θ_H willing to send m*? <yes / no, with payoff comparison>
- Type θ_L willing to send m*? <yes / no, with payoff comparison>
- **Equilibrium status:** <pooling equilibrium / not an equilibrium>

**Separating equilibrium:**
- Type θ_H sends: m_H = <signal>
- Type θ_L sends: m_L = <signal>
- Receiver actions: a_H = <action if m_H observed>, a_L = <action if m_L observed>
- Incentive compatibility for θ_H: u_S(a_H, θ_H) − c(m_H, θ_H) > u_S(a_L, θ_H) − c(m_L, θ_H)? <yes / no>
- Incentive compatibility for θ_L: u_S(a_L, θ_L) − c(m_L, θ_L) > u_S(a_H, θ_L) − c(m_H, θ_L)? <yes / no>
- **Equilibrium status:** <separating equilibrium / not an equilibrium>

### Equilibrium selection and outcomes
- Dominant equilibrium: <which equilibrium is most plausible>
- **Sender outcome:** types, signals sent, resulting receiver actions, expected payoffs
- **Receiver outcome:** posterior beliefs, actions taken, expected payoffs
- **Efficiency:** <is the equilibrium efficient? is there information destruction or waste?>

### Boundary-condition check
<which boundary conditions apply; if any, flag what complementary analysis is needed (cheap talk, repeated signaling, learning dynamics, multiple equilibria refinement, etc.)>

### Confidence: high | medium | low
<reasoning: clarity of payoff and cost functions + realism of cost structure + robustness to off-equilibrium beliefs + quality of type-space assumption>
```

---
name: signaling-games
display_name: Signaling Games
class: model
underlying_class: native
domain: game-theory
source: Michael Spence, "Job Market Signaling," Quarterly Journal of Economics, 1973; developed in game-theoretic framework by Cho & Kreps, "Signaling Games and Stable Equilibria," REStud, 1987
best_for:
  - Predicting equilibrium outcomes when one player has private information (type or quality) that the other player cannot observe
  - Explaining costly signals like education, warranties, or quality investments that reveal unobservable attributes
  - Analyzing market unraveling, separating equilibria, and pooling equilibria in markets with information asymmetry
one_liner: "정보 비대칭 상황에서 신호 전달자가 자신의 유형을 공개하려 하는 메커니즘과 수신자의 신뢰 형성"
---

# Signaling Games

## Overview

Signaling Games model strategic interactions between a **Sender** who has private information about their own type or quality and a **Receiver** who does not observe the sender's type directly but observes a signal the sender chooses to send. The model claims that in equilibrium, the sender will choose a signal (education level, price, warranty terms, investment in reputation) that credibly reveals their type to the receiver, *if and only if* the cost of sending that signal is low enough for the true type and high enough for the false type. The receiver updates their beliefs about the sender's type based on the observed signal and responds accordingly. The model is both descriptive and predictive: it explains why costly signals exist and predicts which equilibria (separating, pooling, or partial pooling) will arise given the payoff and cost structure. Unlike signaling in isolation, signaling games emphasize the strategic interplay between belief updating and optimal response, which locks in the equilibrium signal.

## Core Variables and Relationships

Signaling games involve a sequence of moves and information:

1. **Nature chooses the Sender's type θ ∈ Θ** according to a prior distribution p(θ). The Receiver observes only that a sender exists, not the sender's type.

2. **The Sender observes their own type θ and chooses a signal m ∈ M.** The signal is costly; the cost depends on the sender's type. Denote the cost to a sender of type θ sending signal m as c(m, θ).

3. **The Receiver observes the signal m but not the type θ.** The Receiver updates their belief about θ using Bayes' rule (if the signal is informative). Denote the posterior belief as μ(θ | m).

4. **The Receiver chooses an action a ∈ A** based on the posterior belief μ. The receiver's payoff is u_R(a, θ), which depends on both the action chosen and the true type.

5. **Payoffs are realized.** The Sender's payoff is u_S(a, θ) − c(m, θ); the Receiver's payoff is u_R(a, θ).

**The critical relationships:**

- **Cost structure drives separability.** For two types θ_H (high) and θ_L (low), a separating equilibrium exists only if the cost ratio favors honesty: c(m_H, θ_H) < c(m_H, θ_L) and c(m_L, θ_L) < c(m_L, θ_H). The low type must find it cheaper to signal "low" than "high," and vice versa.

- **Belief updating via Bayes' rule (on the equilibrium path).** If the Receiver observes a signal m that a type θ sends with positive probability in equilibrium, the posterior is μ(θ | m) = p(θ) · P(m | θ) / Σ_θ' p(θ') · P(m | θ').

- **Best-response consistency.** The Receiver's action a(m) must be a best response to the posterior belief μ(θ | m). Formally, a(m) ∈ argmax_a E_θ ~ μ(θ|m) [u_R(a, θ)].

- **Incentive compatibility.** Each type must prefer the signal (and resulting action) they are assigned in equilibrium to any other signal (and the action that would follow). A type θ prefers signal m to signal m' if u_S(a(m), θ) − c(m, θ) ≥ u_S(a(m'), θ) − c(m', θ).

- **Equilibrium conditions:** A separating equilibrium assigns a different signal to each type, and each type is willing to send that signal (incentive compatibility) and prefers not to mimic any other type. A pooling equilibrium assigns the same signal to all types, and the receiver's belief after observing that signal equals the prior. A partially separating (or semi-pooling) equilibrium involves some types separating and others pooling.

## Key Predictions

- **A separating equilibrium exists if and only if the cost structure satisfies the single-crossing condition:** higher types find it cheaper (in relative terms) to send "high-quality" signals. When this holds, types sort themselves through signal choices; the receiver's belief becomes certain upon observing the signal.

- **Pooling can occur even when separation is feasible,** if the signaling costs are high enough that lower types cannot afford to separate. In equilibrium, all types send the same (or overlapping) signal, and the receiver's posterior remains close to the prior.

- **The Receiver may rationally ignore costly signals if the cost differential is small.** A slight change in the cost structure (e.g., education becoming cheaper for everyone) can trigger a collapse from separating to pooling equilibrium.

- **Information destruction through pooling:** In a pooling equilibrium, the private information the Sender holds is not revealed. The Receiver must take an action based on the average type, and the Sender captures no information rent. This is often inefficient compared to separation.

- **Market unraveling (the "Lemons" problem):** If signaling is costly and the low type can mimic the high type cheaply, the receiver may assign low probability to high type signals. In the extreme, only low types send signals (or no signals are sent); high types exit the market because they cannot reveal their quality cost-effectively.

- **Equilibrium multiplicity:** For a given cost structure, multiple equilibria can coexist (separating and pooling). Which equilibrium is selected depends on the off-equilibrium-path beliefs—what the Receiver believes if an unexpected signal is observed.

## Application Procedure

Instantiate the model against a market or strategic situation with information asymmetry.

1. **Identify the Sender and Receiver.** Who holds private information? Who makes the downstream decision based on that information? (Example: job applicant with hidden ability and employer making hiring decision.)

2. **Define the type space Θ and the prior p(θ).** What are the possible types, and how common is each? (Example: high ability with probability 0.3, low ability with probability 0.7.)

3. **Specify the signal space M and the cost structure c(m, θ).** What signals are available? What does it cost each type to send each signal? Write out the cost matrix.
   - Verify that the single-crossing condition holds or fails: does a higher type have lower relative cost for high-quality signals?

4. **Specify the Receiver's action space A and payoffs u_R(a, θ).** What decision does the Receiver make? How do payoffs depend on the true type? (Example: wage offer w, and the employer profits more if the worker is actually high-ability.)

5. **Specify the Sender's payoffs u_S(a, θ).** How does the Sender benefit from the Receiver's action, as a function of type? (Example: higher wage is better, but both types value wages equally—payoff difference is only from cost.)

6. **Construct the pooling equilibrium candidate.** Assume all types send the same signal m*. Compute the Receiver's posterior (equals prior) and the Receiver's best-response action a*. Check whether each type is willing to send m*: is sending m* and receiving a* better than deviating to any other signal?

7. **Construct the separating equilibrium candidate.** Assign each type a different signal: θ_H sends m_H, θ_L sends m_L. Check incentive compatibility for both types: does θ_H prefer (m_H, a_H) to (m_L, a_L) after accounting for costs? Does θ_L prefer (m_L, a_L) to (m_H, a_H)?

8. **Identify which equilibrium(ria) survive.** Apply the D1 criterion or another off-equilibrium refinement if multiple equilibria exist, to select the most plausible one.

9. **Check boundary conditions** (below). Flag if the information structure, payoff structure, or equilibrium concept assumptions are violated.

10. **Report the equilibrium: type distribution, signals, posterior beliefs, Receiver actions, and payoffs.**

## Boundary Conditions

Signaling Games assume complete information about payoff functions and preferences, and that types are exogenous. The model breaks down or becomes incomplete under several conditions:

- **Unknown cost structure to the Receiver.** If the Receiver does not know the cost function c(m, θ), or learns it imperfectly over time, the inference problem becomes more complex (Bayesian learning, experimentation). The separating equilibrium may not hold even if the cost structure would support it.

- **Endogenous type / cheap-talk signals.** If the signal is costless to send (e.g., a verbal claim) and the type is not exogenous (the Sender can invest to change their type), the model becomes a cheap-talk game or an investment game. Separating equilibrium no longer relies on cost; it relies on the Receiver ignoring non-credible claims.

- **Multiple Receivers or audience fragmentation.** If the Sender must signal to multiple audiences with different preferences (e.g., an employee signaling to multiple employers with different skill valuations), signaling becomes more complex. A signal optimal for one audience may repel another.

- **Dynamic signaling / reputation effects.** If the interaction is repeated or the Sender's type is partially revealed through past actions, the game becomes dynamic. Mixed-strategy and reputational dynamics may dominate the static signaling logic.

- **Pooling with asymmetric information at the Receiver level.** If the Receiver also has private information (e.g., the employer doesn't know their own value for the worker), the equilibrium is a Bayesian equilibrium and the analysis becomes more subtle.

- **Continuous or high-dimensional type and signal spaces.** The intuition holds, but the separating equilibrium may not exist in closed form. Numerical or approximation methods may be needed.

## Output Format

```
## Signaling Games Analysis: <market or situation>

**Sender type and prior:** θ ∈ {<types>}, p(θ) = {<probabilities>}
**Signal space M:** {<available signals>}
**Receiver action space A:** {<available actions>}

### Cost structure for signaling
| Type | Signal 1 cost | Signal 2 cost | ... |
|---|---|---|---|
| θ_H | c(m_1, θ_H) | c(m_2, θ_H) | ... |
| θ_L | c(m_1, θ_L) | c(m_2, θ_L) | ... |

**Single-crossing condition:** [Satisfied / Violated / Unclear]

### Payoff functions
**Receiver:** u_R(a, θ) = <specification>
**Sender:** u_S(a, θ) = <specification>

### Candidate equilibria
**Pooling equilibrium:**
- Common signal: m* = <signal>
- Posterior belief: μ(θ | m*) = <prior>
- Receiver action: a* = <action>
- Type θ_H willing to send m*? <yes / no, with payoff comparison>
- Type θ_L willing to send m*? <yes / no, with payoff comparison>
- **Equilibrium status:** <pooling equilibrium / not an equilibrium>

**Separating equilibrium:**
- Type θ_H sends: m_H = <signal>
- Type θ_L sends: m_L = <signal>
- Receiver actions: a_H = <action if m_H observed>, a_L = <action if m_L observed>
- Incentive compatibility for θ_H: u_S(a_H, θ_H) − c(m_H, θ_H) > u_S(a_L, θ_H) − c(m_L, θ_H)? <yes / no>
- Incentive compatibility for θ_L: u_S(a_L, θ_L) − c(m_L, θ_L) > u_S(a_H, θ_L) − c(m_H, θ_L)? <yes / no>
- **Equilibrium status:** <separating equilibrium / not an equilibrium>

### Equilibrium selection and outcomes
- Dominant equilibrium: <which equilibrium is most plausible>
- **Sender outcome:** types, signals sent, resulting receiver actions, expected payoffs
- **Receiver outcome:** posterior beliefs, actions taken, expected payoffs
- **Efficiency:** <is the equilibrium efficient? is there information destruction or waste?>

### Boundary-condition check
<which boundary conditions apply; if any, flag what complementary analysis is needed (cheap talk, repeated signaling, learning dynamics, multiple equilibria refinement, etc.)>

### Confidence: high | medium | low
<reasoning: clarity of payoff and cost functions + realism of cost structure + robustness to off-equilibrium beliefs + quality of type-space assumption>
```
