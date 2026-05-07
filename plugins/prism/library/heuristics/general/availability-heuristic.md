---
name: availability-heuristic
display_name: Availability Heuristic
class: heuristic
underlying_class: native
domain: general
source: Amos Tversky & Daniel Kahneman, 1973
best_for:
  - probability estimation
  - risk assessment
  - frequency judgment
one_liner: "Ease of recall biases probability judgment; vivid or recent events feel more likely than base rates warrant."
---

# Availability Heuristic

## The Rule
People judge the probability or frequency of an event by how easily examples come to mind, not by actual statistical frequency.

## When It Applies
- Estimating accident risk after seeing a high-profile crash or news story about one.
- Assessing how common a software failure mode is after debugging a particularly memorable bug.
- Predicting customer churn after hearing from a vocal dissatisfied user.
- Evaluating the severity of a security threat after a recent breach makes it salient.
- Judging the likelihood of a rare event that has been recently highlighted in conversation or media.

## When It Misleads
- Base rates are low but examples are vivid: plane crashes are extremely rare, but news coverage makes them feel common. A single memorable incident distorts the true probability.
- The event is genuinely rare and no one talks about it: availability heuristic then *underestimates* risk because bad outcomes that leave no survivors or witnesses are invisible.
- Recent events are actually *less* predictive than historical patterns: recency bias amplifies availability. Last month's outlier feels more likely to repeat than it statistically is.
- In domains with selection bias in what becomes "available": only failures get reported and rehashed, while successes are silent. The availability set is structurally skewed.

## Common Misuse
Citing availability as an explanation for why someone else's judgment is wrong, without actually providing the base rate. "You're suffering from availability bias" is often used as a thought-terminating cliché that avoids doing the statistical work to show what the true rate is.

Confusing "I can think of an example" with "this is how often it happens." A memorable anecdote is data of one, not evidence of frequency.

## How Agents Use It
- **Embedded**: in risk assessment, forecasting, and base-rate lenses, as a mandatory check after the initial probability is estimated. Ask: "What makes this example salient? Is it recent, vivid, or widely discussed? How does the base rate compare?"
- **Sanity-gate**: on any finding that claims an event is probable or frequent, force the agent to state the actual rate (if known) and explain whether the judgment tracks the rate or the memorability of the event. Flag findings where vivid examples have been mistaken for statistical weight.
