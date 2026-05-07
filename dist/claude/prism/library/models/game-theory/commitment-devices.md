---
name: commitment-devices
display_name: Commitment Devices (Schelling)
class: model
underlying_class: native
domain: game-theory
source: Thomas C. Schelling, The Strategy of Conflict (1960); extended in Arms and Influence (1966)
best_for:
  - Predicting bargaining outcomes when a party voluntarily restricts its own future choices
  - Explaining why constraining oneself can increase negotiating power
  - Analyzing credible threats and promises in strategic interactions
one_liner: "Gain bargaining leverage by strategically restricting your own options."
---

# Commitment Devices (Schelling)

## Overview

Commitment Devices is a descriptive and predictive model of how a party can gain bargaining leverage by irrevocably restricting its own future options. Schelling's central insight is that in negotiations where both parties fear the other will demand too much, the party that can credibly remove its own exit ramps forces the other party to make concessions — because the committed party has no choice but to stand firm, while the uncommitted party retains flexibility and thus bears the risk of breakdown. The model explains behavior that appears irrational in isolation (voluntarily limiting your own options) but is strategically optimal in a bargaining game. It is explanatory and predictive: it reveals when and why actors make costly commitments, and it predicts the distribution of the negotiated surplus.

## Core Variables and Relationships

1. **Commitment cost (C)** — the cost incurred by making the commitment irrevocable.
   - Literal cost of locking in a position (e.g., burning bridges, public announcement, legal penalty)
   - Opportunity cost of eliminated alternatives
   - Cost is *real and borne by the committer*.

2. **Credibility of the commitment** — does the other party believe the commitment is truly irreversible?
   - Observability of the commitment (can the other party verify it was made?)
   - Irreversibility (can the committer escape the commitment costlessly?)
   - Publicity (is the commitment public, so backing down causes reputational cost?)
   - Third-party enforcement (is there a mechanism that punishes deviation?)
   - Committer's demonstrated track record of honoring prior commitments.

3. **Outside options (walk-away value)** — the payoff each party receives if negotiation fails.
   - Party A's outside option: V_A
   - Party B's outside option: V_B
   - If a party commits to a position that offers the other party less than their outside option, negotiation breaks down (unless credibility is high enough that the threat is costlier).

4. **Commitment position (x)** — the specific offer, demand, or threshold the committer locks in.
   - The committed party must gain at least x; equivalently, the other party is offered at most (total value − x).

5. **Bargaining power of the uncommitted party** — once one party commits, the uncommitted party gains relative leverage.
   - The uncommitted party can threaten to walk away, forcing the committer to accept a worse deal or pay the commitment cost to exit.
   - Uncommitted party's ability to make a counter-commitment (raise its own stakes).

**Core relationship:** When Party A commits to a position x with cost C, Party B will accept x if and only if:
- (Total value − x) ≥ V_B (Party B's outside option), *or*
- The cost to Party A of backing down exceeds the cost of breakdown to Party B, making breakdown preferable to Party A.

The effect is **distributive**: commitment allows the committer to capture a larger share of the total surplus, *conditional on credibility*. But if credibility is low, the commitment is a bluff, and the other party calls it.

## Key Predictions

- **Costly commitment increases bargaining power.** A party that irreversibly commits to a high demand (e.g., "I will not accept less than $X, and I have signed a contract that penalizes me $Y if I back down") forces the other party to either accept the demand or walk away. The committer gets a larger share of the surplus than the uncommitted party.

- **Public commitments are more credible than private ones.** A commitment announced to a third party (media, audience, rival) is harder to renege on because backing down incurs reputational cost. In a labor negotiation, a union leader who publicly commits to a strike gains leverage over a manager who has not publicly committed to a walk-away wage.

- **Mutual commitments can lead to breakdown.** If both parties commit to incompatible positions (Party A commits to demand 70% of the surplus, Party B commits to offer only 40%), and both commitments are credible, negotiation fails and both parties suffer the cost of breakdown. The model predicts that actors will be cautious about committing if they expect the other party to also commit.

- **The committer is vulnerable to the uncommitted party's counter-commitment.** Once Party A commits, Party B can raise its stakes by committing as well. The uncommitted party's advantage is transient: if Party B also commits, the game becomes symmetric again, but now both parties have borne a commitment cost, making breakdown more costly to both.

- **Commitment is credible only if the cost of honoring it is less than the cost of breakdown.** If a party commits to a position that offers the other side less than their outside option, and the commitment is credible, the other party will prefer breakdown. The committer must commit to a position that leaves the other party at least as well off as their outside option (or better), or the commitment is not credible.

- **Low-cost commitments are not credible.** If a party claims to be committed but the cost of backing down is trivial, the other party will not believe it. Credible commitment requires visible sacrifice: a CEO who burns cash to fund a strike fund, or a government that moves troops to the border and incurs logistics costs, signals a genuine commitment.

## Application Procedure

Instantiate the model against a specific bargaining scenario with two or more negotiating parties.

1. **Identify the bargainers and the total surplus.** Who are the parties? What is the total value at stake (the sum they would divide if negotiation succeeds)?

2. **Establish outside options for each party.** If negotiation breaks down, what does each party get? This is their walk-away threshold.

3. **Identify any existing commitments.** Has either party already made a public or credible commitment to a position? What is the commitment (specific demand, red line, or walk-away price)? What is the cost of the commitment (reputation, contract penalty, sunk cost)?

4. **Assess credibility of each commitment.**
   - Is it public and observable?
   - Is it irreversible, or can the committer back down?
   - Is there third-party enforcement (media pressure, contractual penalty, reputation)?
   - Does the committer have a history of honoring similar commitments?
   - Rate credibility as High / Medium / Low.

5. **Check compatibility of committed positions against outside options.** Does each committed position offer the other party *at least* their outside option? If not, and if credibility is high, predict breakdown.

6. **Identify the uncommitted party.** If only one party has committed, which party retains flexibility? That party has a transient advantage.

7. **Predict the outcome.**
   - If one party is credibly committed and the other is not, the committed party captures surplus beyond what an uncommitted negotiation would yield.
   - If both parties commit to compatible positions, predict agreement at those positions (but flag the risk of breakdown if positions conflict).
   - If both parties have made incompatible commitments with high credibility, predict breakdown.

8. **Check boundary conditions** (below). If any apply, flag that the model's prediction may be incomplete.

## Boundary Conditions

Commitment Devices assumes rational, payoff-maximizing parties with stable preferences and the ability to make and enforce credible commitments. The model breaks down or becomes partial under several conditions:

- **Imperfect information about outside options.** If Party B does not know its true outside option (or the committer does not know what it is), the committer may misjudge how aggressive to be. A party might commit to a position that looks credible but actually offers the other side less than their true outside option, causing unexpected breakdown.

- **Multiple equilibria in commitment games.** When both parties can commit, the order of moves, timing, and expectation of what the other party will do matter enormously. Schelling's model is static; in dynamic commitment games with alternating moves, subgame-perfect equilibrium can diverge from the model's predictions.

- **Irrationality, emotion, or ideology.** If a party is willing to accept a deal worse than its outside option for symbolic, ideological, or emotional reasons (e.g., a union strikes because of principle, not economics), the model's prediction breaks down. The model assumes payoff-maximization; it does not account for non-material preferences.

- **Commitment costs are unobservable or disputed.** If one party claims to be committed but the other party cannot verify the cost of the commitment (e.g., "I have privately told the board I will not go below this price"), credibility is low and the commitment has little effect.

- **Renegotiation after breakdown is possible.** If parties can re-negotiate after a commitment is tested and found to be costly, the threat of breakdown becomes less credible (the committer can re-enter talks and claim changed circumstances). Schelling's model assumes commitments are terminal; if renegotiation is easy, commitment is weakened.

- **Reputation concerns extend beyond the current negotiation.** If a party cares deeply about how backing down from a commitment will affect future negotiations (with other parties, or in repeated games), the commitment cost is higher than the current negotiation's breakdown cost. The model needs extension to account for long-run reputation.

## Output Format

```
## Commitment Devices Analysis: <negotiation name>

**Parties:** <list negotiators>
**Total surplus:** <what is at stake, in monetary or preference terms>

### Outside options
| Party | Outside option value | Walk-away threshold |
|---|---|---|
| A | <value> | <minimum acceptable offer> |
| B | <value> | <minimum acceptable offer> |

### Existing commitments
| Party | Committed position | Credibility | Cost of commitment | Enforcement mechanism |
|---|---|---|---|---|
| A | <specific demand, red line, or price> | H/M/L | <observable cost> | <third-party, reputation, contract, other> |
| B | <...> | ... | ... | ... |

### Credibility assessment
- Party A: <reasoning on observability, irreversibility, publicity, track record>
- Party B: <...>

### Compatibility check
- Does Party A's commitment offer Party B at least their outside option? <Yes / No>
- Does Party B's commitment offer Party A at least their outside option? <Yes / No>
- Conflict detected: <Yes / No>

### Uncommitted party
<if applicable: which party retains flexibility and thus has transient leverage>

### Prediction
- Predicted outcome (per Commitment Devices): <agreement on specific position, or breakdown>
- Distribution of surplus: <who gains more, and by how much relative to an uncommitted negotiation>
- Risk of breakdown: <high / medium / low, and under what conditions>

### Boundary-condition notes
<which of the six boundary conditions apply and what complementary analysis is needed (e.g., reputation effects, renegotiation dynamics, emotional drivers)>

### Confidence: high | medium | low
<reasoning: clarity and verifiability of commitments + stability of outside options + fit to boundary conditions + observability of commitment costs>
```
