---
name: hooked-model
display_name: Hooked Model
class: model
underlying_class: native
domain: product-management
source: Nir Eyal, "Hooked: How to Build Habit-Forming Products," 2014
best_for:
  - Predicting whether a product feature or behavior loop will drive habit formation
  - Designing user engagement loops that increase frequency of use
  - Diagnosing why a product fails to create repeat engagement
one_liner: "Trigger → Action → Variable Reward → Investment cycle that forms habits."
---

# Hooked Model

## Overview

The Hooked Model claims that habit-forming products move users through a
repeating cycle of four stages — **Trigger, Action, Variable Reward, and
Investment** — and that the loop's ability to form habits depends on the
design of each stage and its feedback into the next. The model is both
descriptive and predictive: it explains why some products (email, social
media, mobile games) generate compulsive use while others remain one-off
tools, and it allows a designer to predict whether a proposed feature loop
will stick or fade. The model is prescriptive in structure (each loop must
contain all four elements) but the mechanism is psychological: the product
must align the user's need, the ease of the action, the motivation created
by reward, and the user's investment in the system. Unlike a simple
engagement funnel, the Hooked Model emphasizes the **feedback loop**: each
completed cycle primes the next trigger and deepens the user's investment,
raising the probability of the next iteration.

## Core Variables and Relationships

The Hooked cycle has four sequential stages:

1. **Trigger** — the cue that prompts the user to take action.
   - External triggers: notifications, email, UI affordances, social
     cues, or environmental signals. Strength: immediate, design-controlled.
   - Internal triggers: emotional states (boredom, anxiety, loneliness,
     desire). Strength: more durable because user carries the motivation.
   - For habit formation, internal triggers matter most at scale; external
     triggers are the on-ramp but produce fragile habits if they're the
     only fuel.

2. **Action** — the simplest behavior the user can perform in anticipation
   of reward.
   - Ease of action depends on Fogg's Behavior Model: motivation ×
     ability × trigger = behavior.
   - Ability (friction) is the dominant variable a product controls.
     Reducing friction (one-tap vs. multi-step, frictionless payoff display)
     increases action rate for the same trigger and motivation.
   - Motivation (why the user acts) is user-dependent but can be primed
     by the trigger or by context (e.g., "you have 3 new messages" vs.
     "notifications").

3. **Variable Reward** — the outcome the user receives after the action.
   Variability is crucial.
   - **Reward type matters:** rewards of the tribe (social approval,
     connection), rewards of the hunt (information, curiosity, novelty),
     rewards of the self (mastery, progress, achievement). Products that
     blend multiple reward types are stickier.
   - **Variability drives engagement** more than consistent reward. A fixed
     schedule of rewards (every time the user acts, X happens) is weaker
     than a variable schedule (ratio or interval-based). The slot machine
     effect: uncertainty and intermittent reinforcement create stronger
     behavioral loops than predictable payout.
   - The reward must be perceived as *scarce* (harder to get outside the
     product) or *novel* (pattern-breaking) to sustain engagement; if users
     can easily get the reward elsewhere, the loop breaks.

4. **Investment** — the user's commitment of effort, data, time, or social
   capital into the product, building stored value.
   - Stored value means the user has incentive to return: customization,
     accumulated content, social connections, reputation, payment sunk,
     data (profile, preferences, history).
   - The investment stage is the *transition to habit*. It makes the next
     trigger (external or internal) more likely to drive action because the
     user has "skin in the game."
   - Investment serves as the primer for the next cycle's trigger,
     creating the loop: investment → next external trigger is more likely
     to fire → action → reward → deeper investment.

The core relationship is **cyclic and self-reinforcing**: each loop that
completes increases the user's investment, which lowers the friction for
the next trigger to fire and the next action to occur. A product without
investment (or with weak investment) breaks the cycle after a few
iterations; friction in the action stage throttles the frequency of loops.

## Key Predictions

- **Products that rely primarily on external triggers but have weak
  investment will plateau in engagement** after novelty fades. The product
  is used episodically, not habitually, because each trigger must overcome
  the same friction and motivation each time.

- **A loop with high-friction action (many steps, low ability) cannot form
  habits even if rewards are high and investment is present**, because the
  action rate stays low. Engagement remains low-frequency or one-time. (The
  fix is to reduce friction, not to increase reward value.)

- **Variable rewards drive stronger habit loops than predictable rewards.**
  A feed that always shows the same content (predictable) will have lower
  repeat-visit rates than a feed randomizing the order and type of content
  (variable), holding trigger frequency constant. Users check variable
  feeds more compulsively.

- **High investment + variable reward can sustain a habit loop even when
  the trigger is weak or the action is tedious.** Users return to the
  product primarily to protect or grow their stored value (e.g., returning
  to a multiplayer game to defend territory, or to a social network to
  maintain status).

- **Products that successfully transition triggers from external to
  internal will see engagement become less dependent on marketing or push
  notifications.** The user's emotional state or routine (boredom, habit,
  FOMO, curiosity) becomes the trigger. This is the signature of a habit.

- **A missing element kills the loop.** If any of the four stages is absent
  or severely weakened, habit formation stalls. A product with no clear
  trigger, or a reward that doesn't motivate, or frictionless action but
  no stored value, will not produce compulsive use no matter how strong the
  other elements are.

## Application Procedure

Instantiate the model against a specific product feature or user behavior
flow you are trying to predict or design.

1. **Define the loop scope precisely.** What is the user behavior you are
   analyzing? Is it a single tap, a full feature interaction, a session, or
   a daily routine? Write the boundary: "User opens app → [action]
   → [outcome] → [investment]."

2. **Identify and map each of the four stages for this user.**
   - **Trigger:** What cues this specific behavior? Is it external (push
     notification, button on home screen, a text from a friend) or internal
     (boredom, habit at a specific time, emotional need)? List the top 2–3
     triggers.
   - **Action:** What is the minimum viable behavior? How many taps, how
     much time, how much cognition? Rate friction on a scale (low / medium
     / high). Compare to competing alternatives (e.g., opening Instagram
     vs. opening a web browser to Instagram).
   - **Variable Reward:** What does the user receive? Categorize it:
     social, hunt, or self? Is it variable or fixed? Is it *scarce* — can
     the user get the same reward easily outside your product? How novel or
     surprising is it?
   - **Investment:** What does the user put in? Customization (profile,
     saved preferences), social capital (followers, reputation), content
     (posts, photos, comments), time (account age, engagement history), or
     payment? Quantify or describe the stored value.

3. **Assess the loop's strength.** Score each stage on a 3-level scale:
   weak / moderate / strong. Identify which stage is the bottleneck (the
   one constraining habit formation).

4. **Predict habit formation potential.**
   - If all four stages are strong, the loop is capable of forming a habit
     with high frequency (daily or multiple times per day).
   - If one stage is weak, habit formation is slow or shallow (infrequent,
     fragile to friction increases).
   - If two or more stages are weak, the loop will not form a habit without
     redesign.

5. **Identify failure modes.**
   - If the action stage is too high-friction, lower friction (not by
     increasing reward size).
   - If the reward is predictable, introduce variability or scarcity.
   - If investment is missing or invisible, add stored value.
   - If the trigger is only external, design for internal triggers by
     hooking into emotional states or routines.

6. **Check boundary conditions** (below). If any apply, flag what
   complementary modeling is needed.

7. **Generate the prediction.**
   - Will this loop drive habit formation? (Yes / Unlikely / Uncertain.)
   - What is the predicted frequency if the loop is executed?
   - What single change would most improve habit strength?

## Boundary Conditions

The Hooked Model applies well to engagement loops in digital products where
the user's motivation is genuine and the reward is intrinsic. It is less
reliable when:

- **The reward is purely extrinsic (monetary, coercive, or imposed).**
  External rewards often crowd out intrinsic motivation and can weaken
  habit formation once the external incentive is removed. The model assumes
  the user *wants* the reward; if they don't, the loop doesn't stick.

- **The user population is heterogeneous in motivation.** One cohort's
  trigger (a notification) may be another's friction. The model works best
  when you are designing for a narrow user segment with similar
  psychological needs.

- **The loop frequency is extremely high (sub-second feedback) or extremely
  low (once per year).** The model was empirically developed for daily-use
  products. Slot machines and social media fit; enterprise software
  used quarterly does not.

- **Network effects or switching costs are the primary habit driver.**
  If the user stays because their friends are there or because leaving is
  costly, the loop structure matters less than the network. Complement with
  a network-effects or lock-in model.

- **The product is addressing a genuine one-time need** (flight booking,
  moving, tax filing). Not all products should form habits. If the need is
  satisfied once, the Hooked loop is the wrong target.

- **Satiation or habituation dominates.** For some products (video games,
  news feeds), the variable reward loses novelty fast enough that the
  loop weakens. The model doesn't predict when satiation occurs; you need
  empirical measurement.

## Output Format

```
## Hooked Loop Analysis: <product / feature>

**User segment:** <who is this loop designed for>
**Behavior loop:** <trigger → action → reward → investment>

### Stage assessment

| Stage | Strength | Evidence |
|---|---|---|
| Trigger (external) | W/M/S | <type and frequency> |
| Trigger (internal) | W/M/S | <emotional state or routine> |
| Action | W/M/S | <friction level: # steps, time, cognition> |
| Variable Reward | W/M/S | <type: social/hunt/self; variability; scarcity> |
| Investment | W/M/S | <stored value: profile, social, content, payment> |

### Bottleneck
<which stage is weakest and why>

### Prediction
- Habit formation potential: strong / moderate / weak
- Predicted frequency: <daily / weekly / episodic>
- Most impactful redesign: <change to which stage>

### Mechanisms in play
- Trigger type shifting from external to internal: <yes / no>
- Variable vs. fixed reward: <which dominates>
- Investment accumulation rate: <fast / gradual / absent>

### Boundary-condition notes
<which conditions apply and whether they alter the prediction>

### Confidence: high | medium | low
<reasoning: clarity of trigger and reward + visibility of investment +
homogeneity of user segment + product maturity>
```
```
