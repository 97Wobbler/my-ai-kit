---
name: cliodynamics
display_name: Cliodynamics (Turchin)
class: model
underlying_class: native
domain: history
source: Peter Turchin, *War and Peace and War*, 2006; *Secular Cycles*, 2009
best_for:
  - Predicting periods of political instability and state collapse
  - Understanding the long-term dynamics of population, inequality, and institutional capacity
  - Identifying when a civilization is approaching a "crisis of the 13th century" pattern
one_liner: "Predict state-power cycles and collapses via mathematical models (secular cycles)."
---

# Cliodynamics (Turchin)

## Overview

Cliodynamics claims that historical dynamics—rise, stability, and collapse of empires and civilizations—are governed by quantifiable feedback loops between population growth, resource availability, inequality, and state capacity. Rather than attributing major transitions to great men, ideas, or chance, the model proposes that societies follow predicable cyclical patterns spanning 50–300 years, driven by the interaction of demographic, economic, and institutional variables. The theory is explanatory and predictive: it explains *why* states collapse and *when* we should expect crisis periods. It is not deterministic—human choice and contingency remain—but the deep variables constrain the range of outcomes. The model is calibrated to historical data from the Roman Empire, medieval Europe, and pre-industrial states, though application to modern economies requires careful boundary checking.

## Core Variables and Relationships

Cliodynamics operates via a set of coupled stocks and flows:

1. **Population (P)** — the carrying capacity of the territory and the actual population relative to it.
   - Driven up by: favorable climate, agricultural technology, peace (no war loss)
   - Driven down by: resource depletion, famine, epidemic, warfare
   - Constraint: no population can exceed carrying capacity indefinitely; overshoot triggers starvation and collapse

2. **Per-capita wealth (W)** — the aggregate resource base divided by population.
   - W = (Resource stock) / P
   - Driven down by: population growth exceeding resource-production growth (the "overshoot" dynamic)
   - Driven down by: resource degradation (deforestation, soil depletion, overhunting)
   - Consequence: as W falls, living standards decline for the mass population

3. **Inequality (I)** — the ratio of elite wealth to commoner wealth, measured as the Gini coefficient or elite resource share.
   - Driven up by: high per-capita wealth (elites extract rent and keep the surplus)
   - Driven up by: state capacity to tax and extract (stronger institutions → greater elite extraction)
   - Driven down by: population pressure on commoners (mass poverty reduces what elites can extract without rebellion)
   - Consequence: high inequality at low overall wealth is **unstable** — it produces revolts, civil war, and loss of tax revenue

4. **State capacity (S)** — the ability of the state to project power, raise revenue, field armies, and enforce order.
   - Driven up by: high per-capita wealth (more resources to tax)
   - Driven up by: technological/institutional innovation (bureaucracy, roads, written law)
   - Driven down by: civil conflict, loss of tax base, elite fragmentation
   - Consequence: high S at high I and low W is inherently contradictory (the elites need the state to extract, but mass unrest destabilizes it)

5. **Elite numbers (E)** — the absolute count of nobles, officials, military, priesthood competing for power and resources.
   - Driven up by: historical success of the state (attracts ambitious individuals, increases hereditary nobility)
   - Driven up by: population growth (more competitors for elite status)
   - Driven down by: civil war, epidemics, resource collapse
   - Consequence: E grows faster than the resource base can support in the elite tier; **elite overproduction** creates a surplus of ambitious people with few positions, driving political instability

**The secular cycle**: The model predicts a **boom-bust oscillation** spanning 50–300 years:
   - **Phase 1 (Expansion):** P ↑, W ↑, S ↑, I ↑, E ↑. Golden age, institutional innovation, population recovers.
   - **Phase 2 (Plateau):** P reaches carrying capacity, W peaks then flattens, I continues to rise, E continues to grow.
   - **Phase 3 (Crisis):** P > carrying capacity or resources degrade, W ↓, S remains high (inertia), I reaches critical level, E = surplus of elites competing for fixed rents. State taxes collapse as base shrinks. Elites wage civil war. Popular revolts. State capacity fractures. Epidemic + famine. Population collapse.
   - **Phase 4 (Recovery):** P ↓ sharply, W recovers (fewer mouths), I ↓ (mass poverty reduces what elites can extract), S ↓ (state loses reach), E ↓ (civil war kills elites). Cycle begins again in 2–3 generations.

## Key Predictions

- **Crisis clustering.** Major collapses (Roman 3rd-century crisis, European 13th-century crisis, Ottoman 17th century) occur when population has grown to carrying-capacity limits *and* elite overproduction has created a surplus of competitors *and* state institutions are rigid and extractive. All three must align; any one alone is survivable.

- **Counterintuitive: collapse in affluent, well-organized states.** The most sophisticated empires (Rome, Ottoman, medieval Europe) collapse *because* their high state capacity allows extreme elite extraction at low mass welfare. This breeds the instability that state capacity cannot contain. Weak states with low inequality may be volatile but do not collapse in the same way.

- **Elite overproduction as the endogenous instability driver.** The number of aspiring elites grows logistically; the number of elite positions grows linearly (or slower). The gap becomes explosive, driving internal warfare that weakens state capacity. This mechanism is independent of external invasion or climate shock — it is internal feedback.

- **Population crash is not voluntary.** When W falls below subsistence, P crashes via famine, epidemic, and infanticide. The state cannot prevent it even if it wanted to — resource constraints are binding.

- **Recovery timescale is 2–3 generational cycles** (60–100 years), not centuries. Once the population crashes and elite numbers fall, per-capita wealth recovers quickly if new institutions emerge to prevent re-extraction. If rent-seeking resurfaces, the cycle restarts.

- **Secular cycles are not unique to empires.** The pattern appears in the data for Anasazi pueblos, Maya city-states, China (multiple dynasties), medieval Europe, and the Islamic world. This suggests the mechanism is deep and structural, not culturally contingent.

## Application Procedure

Instantiate the model against a historical period or a contemporary society to diagnose its position in the secular cycle and predict the likelihood of crisis.

1. **Define the polity and the time window.** What is the territorial unit (empire, kingdom, city-state)? Over what span of years or decades are you analyzing? Write one sentence.

2. **Estimate the core variables at the start and end of your window.**
   - **Population:** Use census data, tax records, or archaeological estimates. Compute the ratio of actual P to estimated carrying capacity of the territory (based on climate, agricultural productivity, water availability). Is P < 0.5 × carrying capacity? Near 1.0? Overshooting?
   - **Per-capita wealth:** Estimate from tax records, wages, grain prices, or proxy series (archaeological pottery volume, ceramic quality). Is it rising, flat, or falling?
   - **Inequality:** Use tax records, land-ownership data, or wage ratios (elite salary vs. peasant wage). Compute Gini or the elite-to-commoner wealth ratio. Is I rising even as W falls?
   - **State capacity:** Estimate from military size, tax revenues, bureaucratic reach, and infrastructure. Is S rising (new roads, laws, military expansion) or declining (loss of provinces, tax non-collection)?
   - **Elite numbers:** Count known elites (nobility, officials, military officers, clergy) from rosters or narrative sources. Is E growing faster than P?

3. **Identify the phase of the secular cycle.** Based on the trajectory of P, W, I, S, E:
   - **Phase 1 (Expansion):** All variables rising, carrying capacity not yet reached, surplus of resources.
   - **Phase 2 (Plateau):** P near carrying capacity, W flattens or peaks, I still rising, E growing.
   - **Phase 3 (Crisis):** P = carrying capacity or declining, W falling, I at maximum, E in surplus, S about to collapse, revolts and civil war visible.
   - **Phase 4 (Recovery):** P falling sharply, W recovering, I falling, E falling, S fragmented.

4. **Identify which feedback loops are active.** Is the society in the benign regime (expansion, falling I) or the dangerous regime (plateau or crisis, rising I while W falls)? Which constraints are about to bind?

5. **Generate a prediction.**
   - If in Phase 2–3 with high I, high E relative to elite positions, and W at or below previous peak: expect crisis within 10–30 years (one generation).
   - If in Phase 3 with multiple crises visible (civil war, revolt, resource shock): expect major collapse and population crash within 5–15 years.
   - If in Phase 4 after collapse: expect recovery and renewed expansion over 50–100 years *unless* new predatory institutions lock in elite extraction again.

6. **Check boundary conditions** (below). If any apply strongly, flag that Cliodynamics gives the structural prediction but may miss important contingencies or modern dynamics.

## Boundary Conditions

Cliodynamics was developed on pre-industrial agrarian empires and applies well to them. It becomes unreliable or incomplete under:

- **Technological disruption beyond incremental agriculture.** Industrial technology, fossil-fuel energy, and global trade decoupled per-capita wealth from land carrying capacity. Modern economies can sustain 10× the population on the same land. The model's carrying-capacity constraint is partially bypassed, so its core mechanism misfires.

- **Global trade and supply-chain elasticity.** Carrying capacity is local in the model; a pre-industrial empire cannot import food or labor from abroad. Modern economies are networked. A city or region can sustain 10× its local carrying capacity via trade. This invalidates the overshoot-and-collapse mechanism for localized polities.

- **Technological adjustment in real time.** Agricultural technology improved slowly in pre-industrial eras (decades to centuries). In the industrial and information eras, response timescales are years to decades. Societies can avoid overshoot by adopting intensive agriculture or birth control. The cyclical prediction breaks down.

- **Democratic institutions and wage adjustments.** The model predicts crisis when I is high and W is low because elites extract all surplus, leaving commoners in poverty. Modern democracies and labor markets allow real-wage adjustment and wealth redistribution. I may rise, but W need not fall simultaneously, decoupling the instability mechanism.

- **Demographic transition and voluntary fertility decline.** The model assumes population grows until resources fail. Modern societies undergo fertility decline at higher income (the demographic transition), stopping population growth before overshoot. The cycle truncates.

- **Institutional pluralism and veto players.** The model predicts elite civil war when E > available positions. In large, heterogeneous modern states, competing elites cannot easily consolidate power, and competing power centers (legislatures, courts, media, corporations) stabilize against any single faction. The elite-overproduction crisis is modulated.

## Output Format

```
## Cliodynamics Analysis: <polity and time period>

**Polity:** <empire, kingdom, or regional unit>
**Period:** <years or decades analyzed>
**Carrying capacity of territory:** <estimated, with data source>

### Variable trajectory

| Variable | Start | End | Trajectory | Data source |
|---|---|---|---|---|
| Population (ratio to carrying capacity) | ... | ... | ↑ / → / ↓ | ... |
| Per-capita wealth | ... | ... | ↑ / → / ↓ | ... |
| Inequality (Gini or elite:commoner ratio) | ... | ... | ↑ / → / ↓ | ... |
| State capacity (military, tax revenue, reach) | ... | ... | ↑ / → / ↓ | ... |
| Elite numbers relative to elite positions | ... | ... | ↑ / → / ↓ | ... |

### Secular cycle phase
<Phase 1 / 2 / 3 / 4, with justification>

### Active feedback loops
- Carrying-capacity constraint: <binding / loosening / not yet binding>
- Elite overproduction: <acute / developing / not present>
- Inequality-stability trap: <high I + low W: yes / no>

### Structural prediction
- **Crisis likelihood in the next 10–30 years:** High / Medium / Low
- **Type of crisis (if predicted):** <civil war / peasant revolt / state collapse / epidemic-driven population decline>
- **Recovery timescale (if crisis occurs):** <estimated generations and conditions for recovery>

### Contingencies and modern-era adjustments
<Does technological capacity, trade access, or institutional structure modify the prediction? For modern polities, note which boundary conditions apply.>

### Confidence: high | medium | low
<Reasoning: data quality of population and inequality estimates + whether carrying-capacity constraint is plausibly binding + extent to which boundary conditions (technology, trade, demographic transition) override the model>
```
---
