---
name: stock-and-flow
display_name: Stock-and-Flow
class: model
underlying_class: native
domain: systems-thinking
source: Jay W. Forrester, "Industrial Dynamics," MIT Press, 1961; foundational to system dynamics modeling
best_for:
  - Predicting long-term system behavior from accumulation and rate structures
  - Identifying why delays and feedback loops cause overshoot and oscillation
  - Understanding why intuitive policy interventions often backfire
one_liner: "Predict system dynamics via stocks (accumulations), flows (rates), and feedback delays—not via goals or intentions."
---

# Stock-and-Flow

## Overview

Stock-and-Flow is the foundational architecture of system dynamics. It claims that the **long-term behavior of any system emerges deterministically from the structure of its accumulations (stocks) and the rates at which material, money, or information flows in and out**. The model is predictive and mechanistic: given a stock, its inflow and outflow rates, and any feedback loops that govern those rates, the model predicts whether the system will grow, stabilize, oscillate, or collapse. The central intuition is that many counterintuitive behaviors—overshoots, cycles, delayed responses, policy failures—are not caused by irrational actors or external shocks but by the **geometry of accumulation and the time lags in feedback**. The model is descriptive of system structure; applying it requires mapping a real domain onto its variables and then simulating or reasoning through the trajectories.

## Core Variables and Relationships

1. **Stock (state variable, accumulation, level)**: A quantity that changes only through flows. Examples: inventory, cash, population, carbon in the atmosphere, knowledge in an organization.
   - Increases only via inflows
   - Decreases only via outflows
   - Change in stock = inflow − outflow (the fundamental identity)
   - Stocks have inertia: they change slowly relative to their magnitude

2. **Inflow**: The rate at which material or information enters the stock. Examples: hiring rate, production rate, revenue, birth rate.
   - Typically governed by a decision, policy, or feedback rule
   - Often depends on one or more stocks (either directly or with delay)
   - Can be constant, step-function, or dynamic

3. **Outflow**: The rate at which material leaves the stock. Examples: attrition, sales, expenses, death rate.
   - Often proportional to the stock itself (decay / drain)
   - Or driven by external demand or policy
   - Frequently contains a delay relative to changes in upstream stocks

4. **Feedback loop (negative or positive)**:
   - **Negative (balancing) loop**: stock increases → outflow increases or inflow decreases → stock growth slows → equilibrium or stability
   - **Positive (reinforcing) loop**: stock increases → inflow increases or outflow decreases → stock grows faster → runaway growth
   - Loops can be chained and nested

5. **Delay (lag, information delay, material delay)**:
   - **Material delay**: physical time for stock to flow through a process (e.g., a purchase order takes 8 weeks to arrive in inventory)
   - **Information delay**: time before a signal about stock level feeds back to control an inflow or outflow (e.g., a manager sees inventory is low, takes 2 weeks to order more)
   - Delays destabilize feedback loops: a negative feedback loop with long delay becomes oscillatory; the corrective action arrives after the problem has reversed

The **fundamental identity** is:
```
Stock(t+dt) = Stock(t) + [Inflow(t) − Outflow(t)] × dt
```

Behavior emerges from the feedback rules that govern inflows and outflows as functions of stocks and perceived needs.

## Key Predictions

- **Stocks with long inflows and short outflows accumulate faster and overshoot their equilibrium**, then oscillate as the feedback lag forces overshoot in the corrective direction.

- **A system with a positive feedback loop (inflow increases as stock increases) exhibits exponential growth until it hits a constraint or external shock**. Early acceleration is slow and invisible; late acceleration is violent and seems to come from nowhere.

- **Delays in feedback cause oscillation and instability even in systems with stabilizing (negative feedback) intent.** A manager responds to low inventory with aggressive ordering, but the orders take weeks to arrive; by the time they do, the manager has ordered again, causing oscillation. This is not irrationality; it is inherent to delayed feedback.

- **Policy changes that target the wrong variable or that ignore the stock-and-flow structure often backfire or cause long lags before effect.** E.g., raising prices to reduce demand works only if inventory inflow adjusts quickly; if inflow is set by a forecast that lags actual demand, inventory first surges (orders placed under old forecast), then collapses.

- **Systems with large stocks relative to their flows are slow to respond and hard to reverse.** Atmospheric CO₂, institutional cultures, disease prevalence, and species populations all have long time horizons because the stocks are large.

- **A system can exhibit different stable states or multiple equilibria depending on the feedback rules and the initial stock levels.** The same inflow-outflow structure can lead to low-stock equilibrium or high-stock equilibrium depending on whether the feedback loops are tuned to reinforce scarcity or abundance.

## Application Procedure

Instantiate the model against a concrete system or policy scenario.

1. **Define the system boundary and the primary stock of interest.** What is accumulating? (inventory, population, debt, skills, reputation). Write one sentence defining the stock and its units (e.g., "unit inventory in widget supply chain, measured in units held in warehouses").

2. **Identify the inflow and outflow processes.** What brings material into the stock? What takes it out? Name the rates (orders/week, births/year, learning hours/month) and their current approximate magnitudes.

3. **Identify the feedback rules.** What determines the inflow rate? Is it a goal (e.g., "maintain 2 weeks of inventory")? A formula (e.g., "order based on forecast + safety stock")? An external policy? Write the rule explicitly. Do the same for outflow.

4. **Locate the delays.** Is there a lag between observing the stock level and acting on it (information delay)? Is there a lag between initiating an inflow and it arriving (material delay)? Estimate the lag in the same units as the stock change rate (e.g., if outflow is 100 units/week, is the information delay 1 week or 4 weeks?).

5. **Classify the loops.** Trace through the feedback: if stock increases, what happens to inflow and outflow? If outflow increases faster than inflow increases (or inflow decreases), it's a negative (stabilizing) loop. If inflow increases or outflow decreases, it's positive (destabilizing). Map at least one primary loop.

6. **Simulate or reason through the trajectory.** Start with the current stock level. Run forward in time:
   - At each time step, apply the current inflow and outflow rules to the stock.
   - After each delay period, apply any feedback rule that was triggered.
   - Watch for overshoot, oscillation, exponential growth, or collapse.
   - Mark the time at which the system reaches a new equilibrium or becomes unstable.

7. **Predict the response to a policy change.** If you impose a new rule (e.g., "cut inflow by 20%"), step forward again. Note whether the response is fast or delayed, whether the system oscillates before settling, and whether the final equilibrium is what the policy intended.

8. **Check boundary conditions** (below). If any apply, note where stock-and-flow reasoning is incomplete and what other lens is needed.

## Boundary Conditions

Stock-and-Flow is a purely mechanical model and breaks down or becomes partial under several conditions:

- **Nonlinear discontinuities or phase changes.** The model assumes smooth flows and continuous feedback. If the system has a tipping point (e.g., climate collapse, sudden job loss, market crash), the linear stock-and-flow structure misses it. Supplement with a catastrophe or tipping-point model.

- **Bounded rationality or strategic behavior by agents.** Stock-and-Flow assumes the feedback rules are mechanical or exogenous. If agents are gaming the system, hiding information, or changing their behavior in anticipation of a policy, the model predicts the wrong response. Add game-theoretic or behavioral framing.

- **External shocks and stochasticity.** The model is deterministic. If the inflow or outflow is subject to random shocks (supply chain disruption, disease, financial crisis), the model predicts the deterministic trajectory only; add Monte Carlo or robust control analysis.

- **Multiple heterogeneous stocks with cross-coupling.** The model scales poorly to very large systems with many interdependent stocks. Simulation is necessary, and structural insights become harder to extract; use computational system dynamics.

- **Heterogeneous agents with distributed decision-making.** Stock-and-Flow assumes a single inflow/outflow rule. Real organizations have thousands of people deciding independently. The aggregate rule may break down if agents' behaviors are correlated (herding, panic) or if information is asymmetric.

- **Unobserved stocks or hidden delays.** If the true inflow/outflow rules depend on stocks you have not identified (e.g., a manager's "confidence" or "fear" stock driving hiring decisions), the model will miss the dynamics. Always check whether you have enumerated all relevant stocks.

## Output Format

```
## Stock-and-Flow Analysis: <system name>

**System boundary:** <one-sentence scope>
**Primary stock:** <name, units, current level if known>

### Stock-and-flow structure
| Element | Value/Rule | Notes |
|---|---|---|
| Inflow | <rate and rule> | <what governs it> |
| Outflow | <rate and rule> | <what governs it> |
| Primary negative loop | <stock → signal → inflow/outflow change → stock stabilizes> | <mechanism> |
| Primary positive loop (if any) | <stock → signal → inflow/outflow change → stock grows> | <mechanism> |
| Material delays | <delay duration, where> | <e.g., 4-week procurement lag> |
| Information delays | <delay duration, where> | <e.g., 2-week forecast lag> |

### Trajectory prediction
- **Baseline (no change):** <will stock grow, stabilize, oscillate, or collapse? Over what time horizon?>
- **Overshoot risk:** <if any, describe when and why stock overshoots equilibrium>
- **Oscillation:** <if any, describe the period and amplitude>
- **Time to new equilibrium:** <rough estimate in same units as delays>

### Policy scenario: <if applicable, a specific intervention>
- **Intended effect:** <what the policy aims to do>
- **Predicted actual effect (via stock-and-flow):** <mechanism, timing, and whether the effect is achieved>
- **Unintended consequences:** <overshoot, oscillation, or backfire driven by the stock-and-flow structure>

### Boundary-condition check
<which of the boundary conditions apply; what complementary models or data are needed>

### Confidence: high | medium | low
<reasoning: clarity of stock definition + accuracy of inflow/outflow rules + quality of delay estimates + whether nonlinearities or agent behavior are present>
```
---
