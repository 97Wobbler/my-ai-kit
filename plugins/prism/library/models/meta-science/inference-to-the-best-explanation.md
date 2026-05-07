---
name: inference-to-the-best-explanation
display_name: Inference to the Best Explanation
class: model
underlying_class: native
domain: meta-science
source: Gilbert Harman, "The Inference to the Best Explanation," Philosophical Review, 1965; developed further in Harman (1986) and Lipton (2004)
best_for:
  - Selecting among competing explanations for an observed phenomenon
  - Diagnosing why a hypothesis is favored over rivals in scientific reasoning
  - Understanding abduction as the inference strategy that drives hypothesis generation
one_liner: "Reasoning by selecting the best explanation for observed phenomena."
---

# Inference to the Best Explanation

## Overview

Inference to the Best Explanation (IBE) claims that we infer a hypothesis to be true when it provides the best explanation of the available evidence — even if the hypothesis is not deductively entailed by the evidence and even if we have no direct observational access to the explanatory entity. The core insight is that explanatory power is itself an epistemic virtue: if hypothesis H explains the data better than rival hypotheses H', H'', etc., we are warranted in inferring H, provisionally treating it as true. The model is descriptive — it explains why scientists and reasoners actually prefer certain hypotheses — and prescriptive — it formalizes a rational procedure for choosing among explanations. IBE is the bridge between deduction (certainty) and induction (frequency), capturing the abductive reasoning that generates new scientific hypotheses.

## Core Variables and Relationships

An explanation is a hypothesis or set of propositions offered to account for an observed fact or set of facts. The quality of an explanation depends on several dimensions:

1. **Explanatory scope** — the range of phenomena the hypothesis accounts for.
   - A hypothesis that explains only the target observation has narrow scope.
   - A hypothesis that explains the target plus many related observations has broad scope.
   - Broader scope (ceteris paribus) favors the hypothesis.

2. **Simplicity** — the economy of assumptions and entities posited.
   - Fewer independent assumptions or postulates → simpler hypothesis.
   - Fewer kinds of entities or forces invoked → simpler hypothesis.
   - Simpler hypotheses are preferred (Occam's razor constraint on explanation).

3. **Coherence with background knowledge** — how well the explanation fits with established theories, laws, and prior observations.
   - A hypothesis that aligns with accepted theory is more credible than one requiring rejection of multiple settled facts.
   - A hypothesis invoking entities or processes already known to exist is preferred over one requiring wholly novel mechanisms.
   - Fit with background knowledge is not absolute (paradigm shifts violate it), but it is a strong default preference.

4. **Explanatory depth** — whether the hypothesis explains *why* the phenomenon occurs or only *how* it occurs, and how fundamental the level of explanation.
   - A mechanistic explanation (showing the causal process) is deeper than a descriptive pattern.
   - An explanation grounded in fundamental laws is deeper than one invoking ad hoc regularities.
   - Greater depth is preferred.

5. **Absence of ad hocness** — whether the hypothesis was tailored specifically to fit the observed data or whether it was independently motivated.
   - A hypothesis motivated by prior theory and *then* tested is non-ad-hoc.
   - A hypothesis invented post-hoc specifically to fit unexpected data is ad hoc.
   - Non-ad-hoc hypotheses are strongly preferred.

6. **Fruitfulness** — whether the hypothesis generates novel predictions and opens new research directions.
   - A hypothesis that merely accounts for known facts is less fruitful than one that predicts new phenomena.
   - Fruitfulness is a secondary virtue (weaker than the above) and is sometimes context-dependent.

The "best explanation" is the hypothesis that scores highest on a weighted combination of these dimensions. No single dimension dominates; trade-offs are common. A hypothesis may be simpler but narrower in scope; another may be more complex but more coherent with background knowledge. The reasoner must weigh these trade-offs.

## Key Predictions

- **When multiple hypotheses fit the data equally well deductively, the one with greater explanatory scope (accounting for more phenomena) will be inferred.** For example, both geocentric and heliocentric models could fit planetary observations before the 17th century, but heliocentrism eventually prevailed partly because it unified terrestrial and celestial mechanics.

- **A hypothesis that is simpler and more coherent with background knowledge will be inferred over a hypothesis that is ad hoc, even if the ad hoc hypothesis is slightly better at fitting a narrow dataset.** This explains why scientists rejected Ptolemaic epicycles in favor of Newtonian mechanics despite the former being locally accurate.

- **A hypothesis that invokes an already-known mechanism will be inferred over a hypothesis that requires a wholly novel, unobserved mechanism, unless the novel-mechanism hypothesis has substantially superior explanatory scope.** This is why "disease is caused by invisible germs" (once microbes were known) was accepted over "disease is caused by miasma" — the germ hypothesis leveraged known entities.

- **When evidence forces a choice between a hypothesis that preserves background knowledge and one that revises it, the revision-averse hypothesis is initially favored — but as anomalies accumulate, the threshold for accepting the revisionary hypothesis lowers.** This explains why Newtonian mechanics was initially defended against quantum mechanics, but eventually quantum mechanics was inferred as the better overall explanation.

- **A hypothesis that generates novel, independently confirmable predictions will gain inferred credibility more quickly than one that merely post-dicts known facts.** Fruitfulness acts as a tie-breaker or slow accumulator of confidence.

- **When a hypothesis has been inferred as the best explanation and new evidence emerges that fits it perfectly, but an alternative hypothesis emerges that is simpler and has equal scope, the simpler alternative will be inferred.** This captures the dynamic nature of IBE — inferences are provisional and subject to revision as the explanatory landscape changes.

## Application Procedure

Instantiate IBE against a concrete set of observations and a set of competing candidate explanations.

1. **Define the target phenomenon precisely.** What is the observed fact that needs explaining? Write it as a clear, bounded statement (e.g., "the patient presents with fever, fatigue, and rash onset 48 hours ago").

2. **Enumerate the candidate explanations.** List at least 2–3 hypotheses that could account for the observation. For each, state the explanatory mechanism explicitly (e.g., "bacterial infection causing systemic inflammation" vs. "viral infection causing localized immune response").

3. **Assess each hypothesis on the six dimensions above.** For each candidate:
   - What phenomena does it explain (scope)?
   - How many assumptions does it require (simplicity)?
   - Does it align with known mechanisms and prior observations (coherence with background knowledge)?
   - Does it explain the mechanism, or only describe a pattern (depth)?
   - Was it motivated by prior theory or invented to fit the data (ad hocness)?
   - Does it generate novel, testable predictions (fruitfulness)?
   Score each on a 3-level scale (High / Medium / Low) for each dimension, with supporting evidence or reasoning.

4. **Identify the trade-offs.** Candidates often trade scope for simplicity, or coherence for depth. Explicitly note which hypotheses win on which dimensions and which are dominated.

5. **Assign weights to the dimensions.** Depending on the context (e.g., applied medical diagnosis vs. fundamental physics), different dimensions carry different force. State your weighting and justify it.

6. **Identify the best explanation.** Which hypothesis scores highest when weighted? This is the one IBE recommends as inferred.

7. **Assess confidence in the inference.** Is the winning hypothesis clearly dominant, or is it a close call with multiple plausible alternatives? How much additional evidence would it take to flip the ranking?

8. **Check boundary conditions** (below). If any apply, note that IBE may be incomplete or misleading in this context.

## Boundary Conditions

IBE is a powerful and widely applicable model, but it has limits:

- **Underdetermination of theory by evidence.** IBE assumes there is a unique or near-unique best explanation; but in many domains (especially social science, history, and philosophy), multiple explanations may be roughly equally good on all dimensions. IBE does not help break the tie. Supplement with additional constraints or pragmatic criteria.

- **Failure to know the true hypothesis space.** IBE selects the best among *known* candidates. If the true explanation has not yet been considered, IBE will infer a false hypothesis. This is particularly acute in early-stage inquiry and in domains with high novelty (e.g., emerging diseases, new physics). No remedy exists until new candidates are proposed.

- **Circular justification of the explanatory dimensions.** The criteria for "best explanation" (simplicity, scope, coherence) are themselves learned and shaped by culture, training, and disciplinary practice. Different scientific communities may weigh them differently, leading to the objection that IBE is "loaded" with hidden assumptions. Be transparent about the weightings.

- **Ad hocness is context-dependent and hard to judge.** Whether a hypothesis is ad hoc depends on the history and motivation of the reasoner — an explanation that appears ad hoc in one context may be pre-motivated in another. Apply this dimension carefully and with awareness of what you do and don't know about the hypothesis's origin.

- **Inferences about unobservables.** IBE is often used to infer the existence of entities we cannot directly observe (electrons, genes, dark matter). This works well when the unobservable explains a large and diverse set of phenomena, but it is vulnerable to skepticism — we cannot be certain the entity is "real" rather than a useful fiction. Mark inferences about unobservables as provisional.

- **Temporal and methodological constraints.** In time-critical decisions (medical diagnosis under time pressure, incident response), you may not have time to assess all candidates and dimensions. IBE assumes deliberation; under extreme time pressure, use heuristics and update as new information arrives.

## Output Format

```
## IBE Analysis: <phenomenon being explained>

**Target phenomenon:** <precise statement of what is being explained>
**Candidate explanations:** <list of 2–3+ hypotheses>

### Explanatory quality scorecard
| Dimension | Hypothesis A | Hypothesis B | Hypothesis C |
|---|---|---|---|
| Scope | <H/M/L + evidence> | ... | ... |
| Simplicity | ... | ... | ... |
| Coherence with background knowledge | ... | ... | ... |
| Depth | ... | ... | ... |
| Ad hocness (non-ad-hoc is better) | ... | ... | ... |
| Fruitfulness | ... | ... | ... |

### Trade-off analysis
<which hypotheses dominate on which dimensions; where are the tensions>

### Dimension weights
<how much does each dimension matter in this context, and why>

### Best explanation
<which hypothesis wins, and by what margin>

### Novel predictions generated by the best explanation
<what does it predict that has not yet been observed, and how could we test>

### Confidence in the inference: high | medium | low
<reasoning: clarity of dominance + whether true hypothesis space is known + whether boundary conditions apply>

### Next steps
<what additional evidence or candidates would shift the ranking>
```
```
