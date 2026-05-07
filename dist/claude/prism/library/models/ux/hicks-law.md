---
name: hicks-law
display_name: Hick's Law
class: model
underlying_class: native
domain: ux
source: William Edmund Hick, "On the Rate of Gain of Information," Quarterly Journal of Experimental Psychology, 1952
best_for:
  - Predicting decision latency as a function of choice complexity
  - Diagnosing UI bottlenecks caused by option overload
  - Optimizing information architecture and menu design
one_liner: "Decision time grows with the logarithm of the number of choices."
---

# Hick's Law

## Overview

Hick's Law claims that the time required to make a decision increases logarithmically with the number of equally-likely options available to the decision maker. Formally: **RT = a + b · log₂(n)**, where RT is reaction time, n is the number of choices, and a and b are empirically fitted constants. The model is descriptive and predictive: it explains why cluttered menus slow users down, and it predicts the magnitude of that slowdown. The law originated in psychophysics and has been validated across reaction-time experiments; its application to interface design assumes that interface choices behave like laboratory choice tasks, which is a boundary condition worth scrutinizing (see below).

## Core Variables and Relationships

The core relationship is logarithmic, not linear:

1. **Number of equally-likely options (n)** — the cardinality of the choice set.
   - Doubling n from 2 to 4 increases log₂(n) from 1 to 2; doubling from 8 to 16 increases log₂(n) from 3 to 4.
   - The log relationship means that initial options have disproportionate impact on latency; diminishing returns kick in fast.
   - Applies cleanly when all options are *equally likely* to be selected — if some options dominate, the effective n is smaller (see Boundary Conditions).

2. **Decision time (RT), measured in milliseconds** — the time from stimulus presentation to response.
   - Includes both cognitive processing and motor execution.
   - In UI contexts, often interpreted as "time to locate and select" rather than raw reaction time.

3. **Intercept (a) and slope (b)** — empirical constants that vary by task:
   - **a** captures baseline processing time (stimulus encoding, motor prep).
   - **b** captures the information-processing cost per bit of choice (typically 50–200 ms per doubling in n).
   - Real interfaces show b ≈ 100–200 ms · log₂(n) as a rule of thumb.

**The identity:** RT = a + b · log₂(n). This is the core claim. Doubling the number of choices adds roughly 100–200 ms to decision latency; quadrupling adds ~200–400 ms.

## Key Predictions

- **A menu with 4 equally-likely options will be selected ~100–150 ms faster than a menu with 8 equally-likely options**, all else equal. The difference compounds with interface friction (smaller targets, more scrolling, etc.).

- **Reducing 16 options to 8 saves more decision time (~100 ms) than reducing 8 options to 4** (also ~100 ms) — counterintuitive, because the absolute number cut is the same, but log₂(16)−log₂(8) = log₂(8)−log₂(4) = 1 bit, and each bit has constant cost.

- **Progressive disclosure (breaking a 16-option menu into two 4-option menus with a category first) will *increase* total latency slightly** — the user now makes two choices instead of one, and 2·log₂(4) ≈ 4 bits vs. log₂(16) = 4 bits exactly. The benefit of reduced cognitive load is real but not captured by latency alone; it appears in error rate and user preference.

- **When options are not equally likely**, the effective n collapses toward the subset of plausible options. A dropdown with 50 options, where 30 are rarely relevant, behaves like a 10–15 option menu (the user's search space).

- **Interfaces that allow users to filter or search before choosing can substantially reduce effective n**, shortcutting the log penalty — a 1000-item catalog filtered to 20 candidates via search incurs the log₂(20) cost, not log₂(1000).

## Application Procedure

Instantiate Hick's Law against a concrete UI decision or user behavior.

1. **Define the choice task precisely.** What is the user deciding? Is it a one-time selection from a menu, a navigation step in a flow, or something else? Write the task in one sentence.

2. **Identify the choice set and its size.** Count the options the user perceives as live choices. If some options are visibly disabled, de-emphasized, or contextually inaccessible, count only the accessible set. Note whether options are mutually exclusive (yes, typically).

3. **Assess option likelihood.** Are all options equally probable from the user's perspective? Or is there a clear hierarchy (e.g., "Home" is 50% of clicks, "Settings" is 5%, "Help" is 5%, etc.)? If unequal, estimate the effective n — the cardinality of the subset the user considers first. Hick's Law applies to that subset.

4. **Measure or estimate baseline RT.** Gather or estimate a from a similar UI context (e.g., button-press latency in the interface). Without measurement, assume a ≈ 300 ms (rough floor for stimulus encoding and motor response).

5. **Estimate b from prior work or literature.** If you have time-study data from your own interface, fit the log-linear model. If not, assume b ≈ 100–200 ms per bit (e.g., doubling the menu size adds ~100–200 ms).

6. **Compute RT for the current and proposed designs.** If the current design has n=12 and the proposed has n=6:
   - Current: RT ≈ 300 + 150·log₂(12) ≈ 300 + 150·3.58 ≈ 837 ms.
   - Proposed: RT ≈ 300 + 150·log₂(6) ≈ 300 + 150·2.58 ≈ 687 ms.
   - Predicted savings: ~150 ms.

7. **Check boundary conditions** (below). Do any apply? If so, flag whether Hick's Law is the dominant factor or whether error rate, user learning, or cognitive load matters more.

8. **Generate the prediction.** State the predicted change in decision latency and any caveats.

## Boundary Conditions

Hick's Law applies cleanly to simple stimulus-response tasks with equally-likely options and no learning. It is incomplete or misleading when:

- **Options are not equally likely.** If a menu has 100 options but 80% of users always pick the first one, the effective cognitive load is much lower. Hick's Law alone predicts a 100-option penalty; the user's actual experience is much faster. Supplement with a weighted-entropy model or user-behavior analysis.

- **Users have learned the menu structure.** After 10+ exposures to the same menu, latency drops substantially — users are no longer making a novel choice, they are retrieving a learned response. Hick's Law predicts first-encounter latency, not expert performance. For interface stability and retention, this is often more important.

- **The interface includes search, filtering, or progressive disclosure.** These mechanisms let users reduce effective n before committing to a final choice. Hick's Law predicts the latency of the final-selection step, not the whole funnel. Measure end-to-end task time, not just the menu-selection component.

- **Error rate and user confidence matter as much as latency.** A simpler menu (low n) may reduce latency but increase errors if the option labels are ambiguous. A more cluttered menu (high n) may slow the user down but give them more precise options. Latency alone is a partial metric.

- **The "choice" is hierarchical or branching.** Menus nested in categories (e.g., File > Save > Format) create a sequence of log₂(n) decisions. Hick's Law predicts each step, but the total latency compounds — the user may be depth-first searching a tree, not selecting flatly from a list. Use a tree-search or information-foraging model for complex navigation.

- **Cognitive load, not reaction latency, is the bottleneck.** A 50-item menu may slow the decision by 500 ms, but it may overload working memory or cause choice paralysis before the user settles on a response. Hick's Law says nothing about decision quality, satisfaction, or abandonment — only latency.

## Output Format

```
## Hick's Law Analysis: <UI decision or menu context>

**Task:** <one-sentence description of the choice>
**Current design n:** <number of options>
**Proposed design n:** <number of options, if applicable>
**Option likelihood:** <uniform / skewed toward subset, identify high-probability subset>
**Effective n (accounting for likelihood):** <adjusted count>

### Parameters
| Parameter | Value | Justification |
|---|---|---|
| a (intercept, ms) | <measured or assumed> | <basis: prior measurements, task analogy> |
| b (slope, ms/bit) | <measured or assumed> | <basis: prior measurements, task analogy> |
| log₂(n_current) | <numeric> | |
| log₂(n_proposed) | <numeric> | |

### Prediction
- **Current RT:** a + b·log₂(n_current) = <value> ms
- **Proposed RT:** a + b·log₂(n_proposed) = <value> ms (if applicable)
- **Latency reduction:** <delta> ms (~<percent>%)
- **Effect magnitude:** <negligible / moderate / significant>

### Dominant factors in this decision
- Menu complexity (log penalty): <high / medium / low impact>
- Option likelihood distribution: <uniform / highly skewed, which matters>
- Learning or habituation: <users are experts / novices / mixed>
- Error rate or ambiguity: <is latency the right metric, or should we optimize for accuracy>

### Boundary-condition check
<which of the above boundary conditions apply; whether Hick's Law is sufficient or whether additional analysis is needed>

### Confidence: high | medium | low
<reasoning: are options truly equally likely? Is this a one-shot task or a learned interface? How sensitive is the outcome to the b parameter assumption? Does error rate or subjective load matter more than latency?>
```
---
