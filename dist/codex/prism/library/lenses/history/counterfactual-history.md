---
name: counterfactual-history
display_name: Counterfactual History
class: lens
underlying_class: native
domain: history
source: Niall Ferguson (ed., Virtual History, 1997); rooted in historical philosophy (Weber, Collingwood)
best_for:
  - Testing whether a historical outcome was inevitable or contingent
  - Exposing hidden causal assumptions in historical narratives
  - Evaluating the robustness of explanations for major events
one_liner: "Weight 'what if' causes to distinguish historical necessity from contingency."
---

# Counterfactual History

## Overview
Counterfactual History tests whether a historical outcome was truly inevitable by systematically altering one antecedent condition and tracing what would logically follow. Rather than declaring an event "inevitable" because it happened, the lens forces the analyst to identify the specific causal chains that produced it and then deliberately break one link to see if the outcome was contingent on that link or would have occurred anyway. Practitioners use this when a historical narrative treats an outcome as foreordained and they suspect the explanation is lazy or circular.

## Analytical Procedure

### Phase 1 — Establish the Historical Fact

1. **State the outcome in one sentence.** What happened? Write it as a specific event, not a trend or condition. Bad: "The Soviet Union eventually collapsed." Good: "The Berlin Wall fell on November 9, 1989."

2. **Identify the standard explanation.** Write the 4-6 causal steps that textbooks or historians typically cite to explain how this outcome occurred. Do not editorialize; report what the consensus says.

3. **Mark each causal step as one of:**
   - **Structural** — a long-term condition (ideology, economics, technology, demography)
   - **Contingent** — a specific decision, accident, or event that could plausibly have gone the other way
   - **Path-dependent** — a consequence of earlier choices that narrowed later options

   Most outcomes have a mix. Note which one carries the most narrative weight in the standard explanation.

### Phase 2 — Select and Alter a Contingent Antecedent

4. **Choose ONE contingent step from the standard explanation.** Pick one that the narrative treats as a hinge point — a moment where things could have gone differently. Do not choose structural conditions; they are too hard to reverse in a thought experiment without cascading implausibilities.

5. **Specify the counterfactual precisely.** What is the closest plausible alternative? Not "what if World War II never happened" (too large) but "what if the Molotov-Ribbentrop Pact was rejected by Stalin in August 1939?" State the counterfactual as a single, minimal change. Write down the date and the actors involved.

6. **Check the counterfactual for plausibility.** Could this have actually happened, given what people knew at the time? Would someone in 1939 have believed this outcome was possible? If the answer is no, the counterfactual is too fantastic and the analysis becomes idle speculation. Choose again or note the plausibility limit explicitly.

### Phase 3 — Trace Logical Consequences

7. **Given the counterfactual antecedent, trace forward step-by-step.** What would have happened next? You are not predicting; you are asking: *given the actors, their constraints, and their known preferences, what would they have done?*
   - For each step, cite what you know about the actors' actual preferences, capabilities, and information state.
   - Do not assume they would have behaved radically differently. Assume they were roughly as smart and constrained as they actually were.
   - If a step depends on unknowable factors (a secret decision, an unmade choice), mark it as a hinge point and note the uncertainty.

8. **Continue the chain until the outcome either collapses or is reasserted.** Do you end up back at the original outcome anyway, or does the chain diverge?
   - If divergence: the original outcome *was* contingent on the antecedent you altered. It was not inevitable.
   - If reassertion: the outcome *was* overdetermined — even without this causal link, other forces would have produced it anyway.

9. **Identify points of maximum uncertainty.** Where did the chain depend on assumptions you cannot verify? Where would different estimates (of actor preferences, constraints, or information) change the result? Write these down as sensitivity points.

### Phase 4 — Compare to Reality

10. **List all the actual contingencies that occurred in the real historical chain.** What moments genuinely could have gone otherwise and did not? These are the true hinge points.

11. **Assess the distance from the counterfactual outcome to the actual outcome.** How much of the explanation for the actual outcome relies on things that *had* to happen versus things that *happened to* happen?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Outcome is stated as a specific event, not a trend | Y/N |
| Standard explanation is reported in 4-6 causal steps without editorializing | Y/N |
| Each step is tagged Structural/Contingent/Path-dependent | Y/N |
| Counterfactual is a single, minimal change with date and actors | Y/N |
| Counterfactual passes plausibility check against period knowledge | Y/N |
| Forward trace is grounded in known actor preferences and constraints | Y/N |
| At least one sensitivity point is identified (step depending on unknowable factors) | Y/N |
| Conclusion states clearly whether outcome was contingent or overdetermined | Y/N |

## Red Flags

- The counterfactual is so large (e.g., "what if industrialization never happened") that the thought experiment loses connection to actual historical possibility.
- The forward trace assumes actors would have behaved completely differently under the counterfactual without explaining why. ("If X hadn't happened, everyone would have chosen Y instead" — but on what grounds?)
- The analysis ends with "we can't know" at every hinge point. Uncertainty should be noted, but a rigorous counterfactual makes explicit assumptions and traces their implications anyway.
- The outcome is reasserted at the end ("it would have happened anyway") but the mechanisms are not explained. Why would it have happened? Through what causal path?
- The analysis conflates Structural conditions with Contingent ones. Structural conditions are hard to reverse in a thought experiment; focusing on them makes the counterfactual implausible.
- No comparison back to the actual historical chain. The counterfactual is evaluated in isolation without examining whether the real outcome was as contingent as claimed.

## Output Format

```
## Counterfactual History Assessment

**Outcome (actual):**
<specific event with date>

**Standard explanation (4-6 steps):**
1. <step> [Structural | Contingent | Path-dependent]
2. <step> [tag]
...

**Counterfactual antecedent:**
<single, minimal change; date; actors involved>

**Plausibility check:**
<Could this have happened given period knowledge? Y/N. If N, note the limit.>

**Forward trace (logical consequences):**
1. <Given the counterfactual, what follows?> [grounded in known preferences/constraints]
2. <...>
...
[Sensitivity: <step depending on unknowable factor>]

**Outcome under counterfactual:**
<Did the original outcome occur anyway, or did the chain diverge?>

**Reassessment of actual causal chain:**
- Contingencies that actually occurred (could have gone otherwise): <list>
- Steps that were overdetermined (would have happened anyway): <list>

**Conclusion:**
<Was the actual outcome contingent on the altered antecedent, or overdetermined? What does this tell us about how inevitable it really was?>

**Sensitivity Analysis:**
<Which assumptions in the forward trace are most fragile? How would changing them change the conclusion?>

### Confidence
<high | medium | low> — <justification>
```
