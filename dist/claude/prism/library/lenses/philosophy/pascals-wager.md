---
name: pascals-wager
display_name: Pascal's Wager
class: lens
underlying_class: native
domain: philosophy
source: Blaise Pascal (Pensées, 1669)
best_for:
  - Evaluating decisions under radical uncertainty with asymmetric payoffs
  - Testing whether a choice is rational even if its probability is unknown
one_liner: "Decision framing for asymmetrical expected value under deep uncertainty."
---

# Pascal's Wager

## Overview
When faced with a choice where the outcome is unknown but the stakes are asymmetrically large, decision-makers often default to demanding proof before committing. Pascal's Wager inverts this: if one outcome has infinite or extremely large value and its probability is nonzero, then rational choice favors that outcome regardless of how low the probability is—even if you cannot calculate it. The lens applies the expected-value framework to decisions where one option dominates mathematically, even under ignorance. Practitioners use it to unlock decisions that appear paralyzed by uncertainty, and to expose when a decision-maker is actually rejecting the framework's logic rather than the probability claim.

## Analytical Procedure

### Phase 1 — Map the Decision Space

1. **Identify the binary choice.** State the two competing options in concrete terms. Avoid jargon. 
   - Bad: "Believe or don't believe."
   - Good: "Commit to living as if God exists, or live as if God does not."

2. **For each option, list the outcomes and their associated values (payoffs).** Use a table:
   | | Condition X is true | Condition X is false |
   |---|---|---|
   | **Choose Option A** | Payoff A1 | Payoff A2 |
   | **Choose Option B** | Payoff B1 | Payoff B2 |
   - Payoffs may be material (money, time), existential (meaning, salvation), or relational (community, identity). Assign rough magnitude: finite, large, infinite, or catastrophic.
   - Be honest about sign. If an outcome is bad, mark it as negative.

3. **Identify which payoffs are asymmetric.** An asymmetry exists when one option has a payoff that is orders of magnitude larger (or smaller, if negative) than the competing option under the same condition.
   - Flag any payoff marked "infinite" or "catastrophic."
   - Note if one option has a payoff you cannot estimate (mark it "unknown but potentially extreme").

### Phase 2 — Test the Expected-Value Argument

4. **State your honest assessment of the probability of Condition X.** Use buckets: certain, very likely, likely, unknown, unlikely, very unlikely, impossible. If you answer "unknown," do not skip to Step 5 — that is the crux.

5. **Calculate expected value for each option.** Use the formula:
   ```
   EV(Option) = [P(X true) × Payoff if X true] + [P(X false) × Payoff if X false]
   ```
   - If P(X true) is unknown, substitute a range: "If P > [threshold], then EV(A) > EV(B)."
   - Solve for the threshold. This is the break-even probability.
   - Do NOT assume the break-even probability is higher than the actual (unknown) probability without argument.

6. **Check if the choice is dominated.** A choice is **dominated** if one option has higher payoff under *all* conditions, or if the expected value of one option exceeds the other *regardless of the probability assignment within reasonable bounds*. 
   - Test: assume P(X) = 0.01, 0.1, 0.5. Do the rankings flip? If not, dominance holds across uncertainty.
   - If dominance holds, the choice is rational independent of exact probability — this is the core of the Wager.

### Phase 3 — Interrogate Refusals

7. **Identify objections to the Wager logic.** Common moves:
   - **"The payoff is not real"** — challenge whether the stated payoff (e.g., salvation) is actually achievable by the proposed choice. Is it a real outcome or a post-hoc justification?
   - **"The cost is hidden"** — ask whether choosing Option A actually has a cost that was omitted from the payoff table (e.g., "living as if God exists" requires sacrifice that reduces welfare even if God exists).
   - **"Belief is not a choice"** — claim that you cannot simply choose to believe. Reframe: the Wager is not about belief itself but about *commitment to a way of living*. Can you choose to commit?
   - **"Probability cannot be assigned"** — if Condition X is metaphysical or outside all evidence, can you even say "P > 0"? Or is the probability so close to zero as to be negligible?
   - **"Infinite payoffs are meaningless"** — infinity is a mathematical abstraction, not a real outcome. Can you make a decision based on an outcome you cannot empirically verify?

8. **For each objection, ask:** Does it invalidate the expected-value calculation, or does it *change the payoff table itself* (e.g., by making a payoff finite, or by adding a hidden cost)?
   - If it changes the table, rerun Phase 2 with the corrected numbers.
   - If it invalidates the calculation, note what assumption of expected-value reasoning it rejects, and whether that assumption is justified.

### Phase 4 — Assess Robustness

9. **Test sensitivity to parameter changes.** For each uncertain parameter (probability, payoff magnitude, cost), vary it ±50% and re-run the expected-value calculation. Does the recommendation flip?
   - If the recommendation flips with small parameter changes, the choice is fragile and the decision-maker should demand better information before committing.
   - If the recommendation holds across reasonable ranges, the Wager is robust.

10. **Identify what would change the decision.** State explicitly: "If [condition], then Option B becomes dominant." This calibrates the decision-maker to what future information matters.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Both options stated concretely, not as abstractions | Y/N |
| Payoff table completed for all four cells | Y/N |
| Asymmetric payoffs identified and flagged | Y/N |
| Probability assessment explicit (even if "unknown") | Y/N |
| Expected value calculated for both options | Y/N |
| Break-even probability computed (if P is unknown) | Y/N |
| At least three objections interrogated in Phase 3 | Y/N |
| Each objection classified: invalidates calculation vs. changes table | Y/N |
| Sensitivity analysis run and documented | Y/N |

## Red Flags

- Payoff table has missing values, especially under "Condition false." The Wager only works if you've accounted for what happens if you're wrong.
- Probability is stated as definitively zero ("Definitely won't happen"). If so, the Wager does not apply — the choice is not uncertain. But check: are you sure, or are you avoiding the argument?
- The asymmetric payoff is asserted without justification ("Salvation is infinitely valuable because I say so"). Interrogate: why infinite and not merely large? Can you name a payoff you'd rank as equally infinite?
- No objections are raised or all objections are strawmanned. The Wager is built to withstand scrutiny; if it feels unassailable, you may not be interrogating hard enough.
- Commitment to Option A is presented as costless. In reality, living as if X is true (even if you don't believe it) has material and psychological costs. These belong in the payoff table as negative values under "Condition false."
- The decision-maker claims to have chosen based on the Wager but then acts inconsistently. This signals that the payoff table was not honest — they do not truly believe the payoff was asymmetric, or they value something else more.

## Output Format

```
## Pascal's Wager Assessment

**Decision frame:**
Choose between [Option A] and [Option B] given [Condition X].

### Payoff Table
| | Condition X True | Condition X False |
|---|---|---|
| **Option A** | <magnitude and description> | <magnitude and description> |
| **Option B** | <magnitude and description> | <magnitude and description> |

### Asymmetries
- <identify which payoff is extreme and why>

### Probability Assessment
P(Condition X true): [certain | very likely | likely | unknown | unlikely | very unlikely | impossible]
(If unknown, state range: P > __ makes Option A dominant)

### Expected Value Calculation
- EV(Option A) = [calculation]
- EV(Option B) = [calculation]
- Dominant choice: [Option A | Option B | neither]
- Break-even probability (if applicable): [P > __]

### Objections Interrogated
1. **Objection:** <state it>
   **Type:** [Invalidates calculation | Changes payoff table | Both]
   **Resolution:** <revised payoff or explanation why calculation stands>

2. [repeat]

### Sensitivity Analysis
| Parameter | Change | EV(A) | EV(B) | Recommendation |
|---|---|---|---|---|
| Payoff(A if X) | +50% | _ | _ | _ |
| P(X) | ±50% | _ | _ | _ |

### Robustness
[Fragile—small changes flip recommendation | Moderately robust | Robust across reasonable ranges]

### Key Uncertainties
- <What would need to change for Option B to dominate?>
- <What information, if obtained, would resolve the decision?>

### Confidence
<high | medium | low> — <justification based on payoff certainty, probability knowledge, and robustness of the recommendation>
```
