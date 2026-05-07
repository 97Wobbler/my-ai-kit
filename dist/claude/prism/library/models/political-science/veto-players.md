---
name: veto-players
display_name: Veto Players
class: model
underlying_class: native
domain: political-science
source: "George Tsebelis, Veto Players: How Political Institutions Work, Princeton University Press, 2002"
best_for:
  - Predicting the likelihood and magnitude of policy change under different institutional configurations
  - Explaining stability and gridlock in legislative systems
  - Analyzing the structural constraints on executive power
one_liner: "More and more-distant veto players reduce the win-set for policy change; policy stability increases with player number and ideological distance."
---

# Veto Players

## Overview

Veto Players theory claims that the scope for policy change in any political system is determined not by the intentions of individual actors but by the **number of veto players and the distance between their preferred policies**. A veto player is an actor whose agreement is required to change the status quo — in legislatures, each legislator (or party, depending on the counting rule) is a veto player; in coalition governments, each coalition partner is a veto player; in presidential systems with separation of powers, the president and legislative majorities are veto players. The model is explanatory and predictive: it reveals *why* some systems produce frequent major policy shifts while others are locked in stasis, and it predicts the set of policies that can actually be enacted (the "win-set") given the current configuration of veto players. Applying it requires the procedure below.

## Core Variables and Relationships

1. **Number of veto players** — each actor whose consent is mandatory to change the status quo.
   - In a legislature with single-party government, the number is proportional to parties whose legislators are required to pass a bill (often 1 if the government has a majority, or more if in a coalition or minority government).
   - In a presidential system, includes both the legislature and the president as distinct players.
   - Supermajority requirements (e.g., 60-vote threshold) create additional veto players.
   - More veto players → larger win-set shrinks → less policy change possible.

2. **Ideological distance between veto players** — the span of the policy spectrum they collectively occupy.
   - Distance measured in policy space (e.g., left-right axis, or multiple dimensions).
   - If veto players are clustered close together (small distance), the win-set is small — only policies near their consensus are feasible.
   - If veto players are spread far apart (large distance), the win-set can be large — many policies fall within the acceptable range of all players.
   - **Counterintuitive effect**: more distant veto players can produce a *larger* win-set, but only if they are still willing to compromise; the critical constraint is the **coalition potential** — whether a subset of veto players with sufficient power can agree on an alternative to the status quo.

3. **Location of the status quo (SQ)** relative to veto players' ideal points.
   - If the SQ lies inside the "core" — the region where all veto players prefer it to any alternative — then no change is possible regardless of how many players want to move policy.
   - If the SQ lies outside the core, some coalition of veto players can move it to a new policy that all members of that coalition prefer.
   - The win-set is the set of policies that can beat the current SQ with support from some feasible coalition of veto players.

4. **Institutional veto players vs. partisan veto players**.
   - Institutional veto players are created by constitutional structure (president, second chamber, judicial review). Their existence is fixed.
   - Partisan veto players are created by party fragmentation and electoral rules. Their number varies with election results.
   - Changing partisan veto players requires an election; institutional veto players persist across elections.

The core relationship is:

    Win-set size ∝ 1/(Number of veto players) − f(ideological distance)

More precisely: **adding a new veto player shrinks the win-set unless that player's ideal point lies far outside the existing players' range.** The model predicts that policy stability (small win-set) increases with the number of veto players and decreases with their ideological dispersion.

## Key Predictions

- **Unified government (single veto player, or a cohesive coalition)** produces large win-sets and high policy volatility. A single dominant player can move policy nearly anywhere within institutional bounds. Illustration: centralized party systems in Europe, or single-party government with party discipline.

- **Divided government with ideologically distant veto players** produces a small win-set: policy can move only into the narrow region acceptable to both the president and the legislature (or both chambers). Example: a right-wing presidency facing a left-wing legislature, or vice versa.

- **Coalition governments force all coalition partners to be veto players.** Adding partners shrinks the win-set. Governments with three or more coalition partners typically produce gridlock on major reforms unless there is broad consensus. Illustration: multiparty systems in Netherlands, Belgium, or Israel.

- **Supermajority requirements (e.g., 60-vote filibuster rule in US Senate) make every senator who is needed to block or enact a bill a veto player**, effectively creating ~50 veto players instead of 1 (the majority). This radically shrinks the win-set and locks in status-quo bias.

- **Constitutional veto players (second chambers, judicial review, federalism) are sticky.** Removing an institutional veto player requires constitutional amendment, which itself requires supermajority agreement — creating a meta-level veto problem. Systems accumulate veto players over time and become less flexible.

- **Polarization (ideological distance between veto players increases)** can paradoxically *shrink* the win-set further if it moves players apart without changing their number. But if polarization fragments a previously unified party into multiple veto players *and* increases distance, the effect is ambiguous — more players shrinks the set, but distance may expand it.

## Application Procedure

Instantiate the model against a specific legislative system or reform proposal.

1. **Define the institutional context.** What is the country/state, what is the time period, and what powers does each branch have? Is it a presidential or parliamentary system? Are there supermajority thresholds, second chambers, or veto gates (judicial review, federalism)?

2. **Enumerate veto players.** List all actors (individuals, parties, chambers, courts) whose consent is required to change the status quo on the policy in question. Apply a conservative rule: only count actors who can credibly block a change. In a parliament where one party has >50% of seats and perfect discipline, there is 1 veto player (the party, or the PM acting for it). In a coalition, each coalition partner is 1 veto player. In a presidential system, count both the presidency and the legislative majority as separate veto players.

3. **Locate each veto player's ideal point in policy space.** Ideally, use expert surveys or roll-call voting data to map their position on the relevant dimension(s) (e.g., tax rate, healthcare coverage, environmental regulation). If data is absent, use public statements or party manifestos. Write down the policy coordinate for each player.

4. **Locate the status quo.** Where does current policy sit relative to the veto players' ideal points?

5. **Identify the win-set.** Graphically (or by enumeration), identify the range of policies that could beat the status quo with support from some feasible coalition of veto players. The win-set is bounded by the preferences of players whose agreement is both necessary and sufficient to pass a new policy. A classic two-player case: if two players have ideal points at 30 and 70 on a 0–100 scale, and the SQ is at 50, the win-set is [30, 70]. If the SQ is at 20, the win-set shrinks to [20, 70] (the player at 30 prefers 30 to moving right past 70).

6. **Estimate the size of the win-set relative to the policy space.** If the win-set is small (< 10% of plausible policy range), predict gridlock / status-quo bias. If large (> 50%), predict high policy volatility.

7. **Identify which veto player(s) are "pivotal."** The pivotal player is the one whose consent is most constraining. In a three-player system where Player 1 is at 20, Player 2 at 50, and Player 3 at 80, Player 2 is often pivotal because they lie between the extremes and their agreement is often needed by both sides. Changes to pivotal players' positions have disproportionate effect on the win-set.

8. **Check boundary conditions** (see below). If any apply, note that Veto Players alone may not account for the observed outcome.

9. **Generate the prediction.** What policies can plausibly pass? Which are locked in by the win-set? If reform is proposed, is it inside or outside the win-set? If outside, what would need to change (election, coalition shift, new veto player) to move it inside?

## Boundary Conditions

Veto Players theory assumes institutional rules are stable and veto players' preferences are known or stable over the decision horizon. It breaks down or becomes incomplete when:

- **Institutional rules are in flux.** If veto players are actively negotiating to change the rules (e.g., changing the supermajority threshold, amending the constitution), the model is undermined — the set of veto players itself becomes endogenous and contested. Supplement with models of constitutional bargaining.

- **Veto players' preferences are deeply uncertain or rapidly changing.** The model requires a stable mapping from player to ideal point. In highly volatile environments (post-revolution, post-coup, or during a pandemic where preferences flip rapidly), the model's predictions decay.

- **Veto players lack credible commitment.** The model assumes that if a veto player says they prefer policy X, they will block alternatives not aligned with X. If a veto player can be bought off, compromised, or is known to renege, the effective set of veto players shrinks. Supplement with models of corruption, side-payments, or internal party discipline.

- **Agenda-setting power is highly asymmetric.** The model assumes all veto players have equal say in what alternatives are tabled. In reality, if one player controls the agenda (e.g., a strong committee chair), the win-set is often much smaller than the static model predicts. Supplement with models of agenda control (Romer-Rosenthal, Schofield).

- **Voters or external actors (courts, international pressure, mass movements) can override veto players.** If there is a revolution, a judicial coup, or massive electoral upheaval, the fixed set of veto players is replaced. The model has no mechanism for these ruptures.

- **Strategic veto players can generate new coalitions through side-deals, linkage, or logrolling.** The model assumes veto players negotiate only over the specific policy in question. If they can trade off multiple issues (health policy for defense spending, for example), the effective win-set may expand beyond what the static model predicts. Supplement with multi-dimensional models of coalition formation.

## Output Format

```
## Veto Players Analysis: <policy domain / reform>

**Institutional context:** <country, system type, time period>
**Policy dimension:** <what is being proposed or analyzed>

### Veto players and ideal points
| Player | Type | Ideal point | Distance to median | Pivotal? |
|---|---|---|---|---|
| <Name> | <Institutional/Partisan> | <coordinate> | <distance> | <Yes/No> |
| ... | ... | ... | ... | ... |

### Status quo location and win-set
- **Status quo:** <coordinate and interpretation>
- **Win-set range:** <[min, max] or description>
- **Win-set size:** <small / medium / large; % of policy space>

### Dominant structural constraint
<Which veto player(s) or which dimension of distance is most constraining? Why is the win-set the size it is?>

### Prediction
- **Policies inside the win-set:** <likely to pass>
- **Policies outside the win-set:** <blocked unless veto player configuration changes>
- **Pivotal player(s):** <whose preference shifts would most affect the win-set>
- **Gridlock prediction:** <likely / unlikely; timescale>

### Scenarios for change
- **Which electoral / institutional changes would expand the win-set?**
- **Which would shrink it further?**

### Boundary-condition notes
<Which boundary conditions apply and what complementary analysis is needed (agenda control, credible commitment, coalition dynamics, voter preferences, etc.)>

### Confidence: high | medium | low
<reasoning: clarity of institutional rules + stability of veto player preferences + applicability of boundary conditions>
```
