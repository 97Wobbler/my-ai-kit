---
name: mental-accounting
display_name: Mental Accounting
class: model
underlying_class: native
domain: behavioral-finance
source: "Richard H. Thaler, \"Mental Accounting and Consumer Choice,\" Marketing Science, 1985; \"Mental Accounting: An Analysis of Buying Behavior,\" Journal of Decision Making, 1999"
best_for:
  - Explaining and predicting spending, saving, and investment decisions that violate monetary fungibility
  - Understanding how framing by source or intended use overrides rational preferences
  - Diagnosing why identical dollars are treated as incompletely substitutable
one_liner: "Predict spending and saving biases via mental accounts keyed to income source, spending category, and time horizon."
---

# Mental Accounting

## Overview

Mental Accounting claims that people do not treat all money as fungible
(interchangeable). Instead, people mentally partition money into separate
**accounts** keyed to its source (salary, bonus, inheritance, found money),
its intended use (rent, discretionary, emergency reserve), or a time
horizon (daily, monthly, yearly). Each account operates under different
spending and saving rules, and transfers between accounts are cognitively
costly. The theory is descriptive: it explains why a person will reject a
favorable financial trade at the aggregate level but will accept it when
framed within a single mental account, why windfalls are spent rather than
integrated with permanent income, and why people simultaneously borrow at
high rates and hold low-yield savings. Applying the model requires mapping
a concrete financial decision onto the mental accounts the decision-maker
is using.

## Core Variables and Relationships

Mental Accounting operates through three nested layers:

1. **Account Definition** — which money belongs to which account.
   - **Source effect.** Income labeled "salary" is coded differently from
     "bonus" or "tax refund," even if received in the same month.
   - **Use intention effect.** Money set aside for "rent" is segregated
     from money for "entertainment," even in the same bank account.
   - **Time horizon effect.** Money earmarked for "next month" is
     separated from "retirement" funds, affecting the decision weight on
     current vs. future utility.
   - **Explicit vs. implicit framing.** A bonus is more likely to be
     treated as discretionary if it is labeled "bonus" than if it is
     spread into the regular paycheck, even if the total income is
     identical.

2. **Account Rules** — the spending and saving behavior rules attached to
   each account.
   - **Spend rate.** Discretionary / bonus accounts have higher marginal
     propensity to spend (MPS). Emergency or goal accounts have low MPS.
   - **Loss aversion within accounts.** Money assigned to a goal is
     defended against withdrawal; the same amount in an undifferentiated
     pool is spent freely.
   - **Outcome integration.** A gain in one account is *not* treated as
     offsetting a loss in another account at the decision level, even if
     they net to zero at the portfolio level.
   - **Temporal separation.** Weekly, monthly, and yearly accounts are
     not integrated in real-time; budget constraints are enforced per
     account, not globally.

3. **Account Boundaries and Transfers** — the friction that prevents
   reallocation of money across accounts.
   - **Cognitive cost of reallocation.** Moving money from a "rainy day"
     account to a "discretionary" account requires justification and
     deliberation — it is not automatic.
   - **Psychological lock-in.** Once money is labeled (e.g., "rent
     deposit"), changing its use induces guilt or violation of self-image.
   - **Salience of the frame.** The more explicitly a person has framed
     the account (e.g., opened a separate savings account), the higher
     the transfer friction.

The core prediction: **money with identical monetary value and utility
will be spent, saved, or invested differently depending on which mental
account it is assigned to.** Aggregate fungibility fails because the
decision is local to the account, not global.

## Key Predictions

- **Windfall non-integration.** A $5,000 bonus is largely spent on
  discretionary purchases (dining, travel), while a $5,000 salary
  increase is integrated into permanent income and partially saved. The
  bonus is assigned to a mental account with higher spend rules, despite
  identical economic status.

- **Dual-account paradox.** A person simultaneously holds a savings
  account earning 0.5% and a credit card debt at 18% interest. Rational
  arbitrage would eliminate the spread, but the mental accounts are
  separate — savings is a "safe" account and debt payoff is not coded as
  an investment option in the savings account.

- **Goal-based spending lock-in.** Money accumulated for a specific goal
  (home down payment, vacation) is spent only on that goal; the same
  amount in an undifferentiated account would be partially redirected.
  Loss aversion within a named account makes reallocation costly.

- **Source-dependent marginal propensity to consume (MPC).** Found money
  or a tax refund has an MPC ~0.5–0.7; regular salary has an MPC ~0.2–0.3.
  The *same dollar* exhibits different spending behavior based on its
  origin label.

- **Time-horizon segregation.** A person budgets daily cash, monthly rent,
  and annual insurance separately, rather than integrating all into a
  single intertemporal optimization. This leads to apparent
  time-inconsistency (preferring $10 today to $11 tomorrow, but $11 in
  52 weeks to $10 in 51 weeks).

- **Framing-induced preference reversal.** Presenting a financial choice
  as "saving in a dedicated account" vs. "investing in a diversified
  portfolio" shifts choice even when the underlying returns are identical,
  because the frame induces different mental account assignments and
  spending rules.

## Application Procedure

Instantiate the model against a concrete financial decision or spending
pattern you are trying to explain or predict.

1. **Identify the decision maker and the financial choice or pattern.**
   Who is deciding, and what are they spending, saving, or investing in?
   Is this a one-shot choice or a repeated pattern?

2. **Locate the mental accounts relevant to the decision.**
   - What *labels* or frames has the decision-maker applied to the money
     in question? (salary, bonus, windfall, savings, "emergency fund",
     "college fund", etc.)
   - How explicitly are these accounts separated (separate bank account,
     mental note, envelope system)?
   - What is the intended use, and how salient is it?
   - What time horizon is attached to each account (weekly, monthly,
     annual)?

3. **Infer the spend and save rules attached to each account.**
   - Is this account coded as "discretionary" or "protected"?
   - What is the historical spend rate? (Bonuses might have MPS ~0.6;
     retirement savings MPS ~0.05.)
   - Would the person transfer money between accounts to equalize returns,
     or is that transfer cognitively costly?

4. **Identify the account(s) the decision-maker is using to evaluate the
   current choice.** Are they thinking locally (within one account) or
   globally (across all accounts)?

5. **Decompose the choice into account-level decisions.**
   - If the decision is "should I spend $200 on dinner?", is the person
     evaluating it against a weekly cash account or a monthly budget?
   - If the decision is "should I pay off credit card debt or save?", are
     they keeping debt and savings accounts mentally separate?
   - If the decision is "how much of this bonus should I save?", is the
     bonus being assigned to a high-spend account?

6. **Apply account-level rules and predict behavior.** Using the
   historical spend rates and account rules you inferred:
   - Which account(s) drive the decision?
   - What does the account rule predict for this choice?
   - Does that prediction match the observed behavior, or is there a
     gap?

7. **Identify transfers or reallocation opportunities** that the model
   predicts will NOT occur (because transfer friction is high). Where
   would a rational, fully fungible agent reallocate, but a mental
   accountant would not?

8. **Check boundary conditions** (below). If any apply, note that Mental
   Accounting alone may not explain the behavior.

## Boundary Conditions

Mental Accounting describes individual consumer behavior well but breaks
down or becomes partial under these conditions:

- **Financial sophistication and training.** Accountants, investors, and
  others trained in fungibility treat money as closer to fully fungible.
  Expert override of mental accounting is real, though incomplete.
  Predict weaker effects for financially literate subjects.

- **Very large stakes.** At the level of household or firm balance-sheet
  decisions (mortgage, capital investment), decision-makers are more likely
  to integrate accounts and optimize globally. The mental accounts are
  shallower or absent.

- **Repeated, high-frequency transactions.** When a person spends out of
  the same account daily and reviews it regularly, integration increases
  and the account boundaries blur. Mental accounting is strongest for
  isolated or infrequent decisions.

- **Explicit budget constraint or enforcement mechanism.** If a decision-maker
  has a hard budget rule (e.g., "I allocate 30% of take-home to savings
  no matter what"), or uses a budgeting app that enforces global constraints,
  mental accounts are overridden by the explicit mechanism.

- **Institutional or automated allocation.** Payroll deduction directly to
  savings, automatic bill payment, and employer retirement contributions
  reduce the salience of account boundaries and lower mental-accounting
  effects.

- **Social or cultural norms override frames.** In some cultures or social
  groups, strong norms about saving or spending override individual account
  definitions. Predict weaker effects when norms are explicit and enforced.

## Output Format

```
## Mental Accounting Analysis: <decision or pattern>

**Decision maker:** <who>
**Financial choice or pattern:** <spending, saving, or investment pattern>
**Time scope:** <one-shot or recurring>

### Mental accounts identified
| Account label | Source / use | Spend rule | Account boundary (high/low friction) |
|---|---|---|---|
| ... | ... | ... | ... |

### Account assignment for the current decision
- Which account(s) is the decision-maker using to evaluate this choice?
- Is the decision local (within one account) or global (fungible)?

### Account-level prediction
- What does each account's rule predict for this choice?
- Will the decision-maker integrate across accounts (fungible) or keep them separate?
- Which potential transfers or reallocations would a rational agent make, but mental accounting predicts will NOT occur?

### Observed behavior vs. prediction
- Does the predicted account-driven behavior match the observed choice?
- If not, which boundary condition may be overriding mental accounting?

### Boundary-condition check
<which of the boundary conditions apply and whether the Mental Accounting
prediction is still the load-bearing explanation>

### Confidence: high | medium | low
<reasoning: clarity of account frames + sophistication of decision-maker +
salience of account boundaries + boundary-condition fit>
```
