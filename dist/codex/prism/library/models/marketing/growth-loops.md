---
name: growth-loops
display_name: Growth Loops
class: model
underlying_class: native
domain: marketing
source: origin uncertain — framework popularized in product-led growth and viral marketing contexts; antecedents in feedback-loop thinking and network effects literature
best_for:
  - Designing self-sustaining user acquisition where output of one cohort becomes input to the next
  - Predicting sustainable growth rates when direct spend holds constant
  - Identifying which product features or mechanics create loop closure
one_liner: "Design feedback loops where product output becomes an input for acquiring new users."
---

# Growth Loops

## Overview

Growth Loops models the mechanism by which a product or service becomes
self-amplifying: each user or transaction produces an output (referral,
content, network effect, or byproduct) that directly feeds acquisition of
new users without additional marketing spend. The model is predictive — it
explains under what conditions growth compounds, at what rate, and which
product design choices are load-bearing for loop closure. Unlike viral
coefficient models that treat virality as a fixed parameter, Growth Loops
is structural: it maps the machinery that converts user action into new
user arrival, showing how changes to output quality or input conversion
affect the growth trajectory. The model is mechanistic, not merely
correlative.

## Core Variables and Relationships

A Growth Loop consists of five linked variables:

1. **Output produced per user** (O). Each user action generates an asset
   or signal that can reach non-users.
   - Form: referral link, content, network profile, social signal, search
     index entry, or recommendation
   - Quality: clarity, relevance, persuasiveness, credibility
   - Reach: how many non-users does one output typically touch?
   - Persistence: does the output remain valuable indefinitely or decay?

2. **Exposure rate** (E). Fraction of the non-user population that
   encounters the output.
   - Driven by: distribution channel, algorithmic amplification, peer
     proximity, search discoverability, organic sharing
   - Formula: E = (reach of output) / (target non-user population)
   - Constraint: E can never exceed 1, and typically << 0.1 for cold
     audiences

3. **Conversion rate** (C). Fraction of exposed non-users who take action
   (signup, purchase, trial) after encountering the output.
   - Driven by: output quality, clarity of call-to-action, urgency,
     credibility of the referrer, discount or incentive structure
   - Varies by: channel (direct referral C >> algorithmic discovery C),
     user segment, timing
   - Bounded: typically 1–15% in consumer settings; higher in B2B warm
     intro contexts

4. **Loop velocity** (V). Average time from user action to output
   production to new-user conversion.
   - Measured in: days, and critical for compounding speed
   - Driven by: notification latency, content indexing time, network
     propagation, user onboarding friction
   - Faster V → same annual growth rate achieved in fewer cycles

5. **Loop coefficient** (L). The net multiplication rate per loop cycle:
   - L = O × E × C
   - **L > 1**: growth compounds (self-sustaining)
   - **L = 1**: growth is linear (each cohort replaces itself)
   - **L < 1**: growth decays (loop adds value but is not self-sustaining)

The sustained growth rate is approximately:
    g ≈ (L − 1) / V (in fractional terms per unit time)

All else equal: faster V amplifies growth rate; higher L enables growth.

## Key Predictions

- **Loop closure requires all five variables to be nonzero and structured
  consistently.** A product with high-quality output (O) but zero exposure
  (E = 0, closed network) cannot loop. A product with 20% exposure but
  0.5% conversion loops too slowly to matter. The binding constraint is
  usually exposure or conversion, not output quality.

- **Growth loops are not viral at inception.** Early products often have
  L << 1 because output is sparse or conversion is low. The loop becomes
  self-sustaining only after deliberate product changes (e.g., adding a
  referral mechanism, improving content discoverability, incentivizing
  sharing). The jump from L = 0.3 to L = 1.2 is what separates a feature
  from a growth engine.

- **Loop velocity creates a growth-rate ceiling that cannot be overcome by
  higher L alone.** A loop with L = 2.0 but V = 180 days (6 months per
  cycle) produces slower absolute growth than a loop with L = 1.3 and
  V = 7 days. Optimizing V compounds faster than optimizing L, but
  diminishing returns set in quickly on velocity alone.

- **Loops are brittle to changes in output or distribution.** If an
  external platform (e.g., social network algorithmic feed) deprioritizes
  the output channel, E drops abruptly, and L may fall below 1. Loops that
  depend entirely on a single channel fail faster than loops backed by
  multiple channels (email, organic search, word-of-mouth, in-product).

- **Loop quality compounds stronger than loop breadth.** A product with one
  tight loop (high O, E, C, low V) reaches N users faster than a product
  with three weak loops. Invest in closing one loop fully before opening
  three.

- **Loops create power-law acquisition cost curves.** Early users cost full
  CAC. By year 2, CAC per user drops as the loop saturates the addressable
  market, but absolute acquisition volume stays high. This creates a
  natural monopoly dynamic: the first product to close a loop at scale
  usually wins the market.

## Application Procedure

Instantiate the model against a specific product and a specific user action
you believe closes a growth loop.

1. **Define the loop boundary.** What is the user action (A) that produces
   output? What is the output (O)? What is the target outcome (new user
   signup, paid conversion, etc.)? Write this as: "Users who [A] produce
   [O] which reaches non-users, who then [outcome]."

2. **Estimate or measure output O.** For each user who takes action A:
   - How much output is produced? (count: one referral link, one review, one
     network connection, one indexed page)
   - How long does one unit of output remain discoverable?
   - How credible is the output to a non-user?

3. **Quantify exposure E.** 
   - How many non-users does one unit of output reach on average? Survey,
     log data, or run a small experiment.
   - Is the reach organic (search, algorithmic feed, peer network) or
     owned (email to warm list)?
   - What is the denominator (total addressable non-user population at your
     current stage)?
   - Calculate E = (average non-user audience per output) / (non-user
     population).

4. **Measure conversion C.**
   - Track: what fraction of non-users who encounter the output take the
     target action?
   - Segment by channel (referral links often have C = 5–15%; algorithmic
     discovery C = 0.1–1%).
   - Note incentives: C is much higher when the referrer or non-user
     receives a reward.

5. **Calculate loop velocity V.**
   - Measure the median time from user action A to the new user converting.
   - Include delays: notification latency, content indexing, user
     discovery, signup friction.
   - Shorter V is better; V > 90 days usually means the loop is too slow to
     matter.

6. **Calculate L = O × E × C.** Is L > 1? If yes, the loop is
   self-sustaining. If L < 1, it adds growth but is not self-sustaining at
   current parameters.

7. **Identify the binding constraint.** Which of O, E, C is smallest?
   That is your highest-leverage lever for improvement.

8. **Check boundary conditions** (below). If any apply, flag that the loop
   may not close at scale or may be cannibalistic.

9. **Predict growth trajectory.**
   - If L > 1, estimate the annual growth rate: g ≈ (L − 1) / V in
     fractional terms per unit time.
   - Project user count forward 12 months assuming constant L and V.
   - Note: saturation will eventually cap growth when the loop exhausts its
     addressable market.

## Boundary Conditions

Growth Loops fail or become partial under several conditions:

- **Network saturation or market size constraint.** A loop with L = 1.5
  becomes L = 0.8 once the loop has reached 30% of the addressable market
  (fewer non-users left to convert). The loop does not compound forever; it
  hits a ceiling determined by the size of the addressable market and the
  loop's reach within it. Ignoring this leads to over-optimizing a loop
  that is already hitting saturation.

- **Platform dependency.** If the loop relies entirely on a third-party
  platform's distribution (Instagram feed, Google Search, TikTok
  algorithmic promotion), the loop coefficient is hostage to platform
  policy. Changes in algorithm or terms of service can reduce E from 0.08
  to 0.01 overnight, collapsing growth. Single-channel loops are
  structurally fragile.

- **Output decay or quality degradation.** Some outputs (e.g., referral
  links, time-limited content) have short half-lives. Others (e.g.,
  user-generated reviews, network profiles) improve with age. If output
  decays faster than new users can act on it, effective E decays, and the
  loop weakens. Legacy or archived content may have E ≈ 0.

- **Misaligned incentives.** Growth loops often rely on referral incentives
  (referrer discount, referee discount, or both) to boost C. If incentives
  are too aggressive, quality of referred users drops (lower LTV, higher
  churn), which reduces the effective lifetime value of the loop and may
  make it negative-margin at scale. Loops can be growth-efficient but
  margin-negative.

- **Cannibalization.** If the loop's new users are largely diverting from
  non-loop channels (paid ads, organic search, partnerships), the net
  acquisition benefit of the loop is much smaller than L suggests. The
  loop accelerates existing demand but does not create net new demand. This
  is especially common in B2B where the addressable market is small and
  concentrated.

- **Attribution and measurement noise.** Loops are hard to measure cleanly
  when multiple channels drive conversion (is the new user coming from the
  referral link or from a parallel email campaign?). Mis-attribution inflates
  perceived L and causes over-investment in a loop that is weaker than it
  appears. This is load-bearing in the Application Procedure.

## Output Format

```
## Growth Loop Analysis: <product name / loop type>

**Loop definition:** Users who [action A] produce [output O], reaching
non-users who then [target outcome].

**Time period:** <measurement interval>

### Loop parameters
| Variable | Value | Source / method |
|---|---|---|
| O (output per user) | <count per action> | <survey / log data / estimate> |
| E (exposure rate) | <fraction> | <reach / population; or log-derived> |
| C (conversion rate) | <fraction or %> | <funnel data, segmented by channel> |
| V (loop velocity) | <days> | <median time from action to conversion> |
| **L (loop coefficient)** | **O × E × C = ?** | <product; interpretation: sustaining? not?> |

### Growth trajectory
- Sustaining (L > 1) or not (L ≤ 1)?
- Implied annual growth rate: ~<g> (qualitative: fast / moderate / slow)
- Addressable market size and saturation timeline

### Binding constraint
Which of O, E, C is smallest and most depressing L? <answer, with data>

### Channel risk
- Is the loop dependent on a single third-party platform? <yes / no>
- If yes, what is the downside if that channel is deprioritized?

### Incentive sustainability
- Are referral incentives active? <yes / no>
- If yes, are referred users lower lifetime value? <assessment>
- Net margin impact of loop at scale: <positive / negative / uncertain>

### Measurement quality
- Attribution: <clean / noisy; if noisy, what is the uncertainty band on L?>
- Cannibalization: <assessed / not assessed>

### Boundary-condition notes
<which boundary conditions apply and whether they cap or collapse the
loop's effectiveness>

### Confidence: high | medium | low
<reasoning: measurement quality on L parameters + channel concentration risk +
market saturation timeline clarity + incentive sustainability>
```
