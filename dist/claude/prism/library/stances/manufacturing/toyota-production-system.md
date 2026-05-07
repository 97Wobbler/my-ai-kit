---
name: toyota-production-system
display_name: Toyota Production System
class: stance
underlying_class: native
domain: manufacturing
source: Taiichi Ohno (Toyota Production System: Beyond Large-Scale Production, 1988), Shigeo Shingo (A Study of the Toyota Production System, 1989), James Womack et al. (The Machine That Changed the World, 1990), Yasuhiro Monden (Toyota Management System, 1993)
best_for:
  - Reading manufacturing systems and workflows to see how elimination of waste reveals actual value
  - Analyzing production to expose assumptions about what counts as "necessary" work
  - Understanding pull-driven versus push-driven organizational logic
one_liner: "Philosophy that makes flow visible by eliminating waste and automating, while centering human judgment and improvement."
---

# Toyota Production System

## Overview

The Toyota Production System is a commitment to treating **the manufacturing process as a continuous flow whose value is defined by the customer pull, not by departmental efficiency or machine utilization — and to making waste visible as the primary site of improvement, where "waste" means any activity that does not add value from the customer's perspective**. The stance is not a set of tools (kanban, andon, heijunka) but an interpretive position: it asks what becomes visible when you stop optimizing each machine and start optimizing the entire flow, and what assumptions about work and human judgment are revealed in the act of eliminating waste. It is suited to reading manufacturing operations, software delivery pipelines, service workflows, and any system where work flows through multiple stages and where the relationship between local efficiency and system efficiency is contested.

## Foundational Commitments

- **Value is defined by the customer, not by the producer.** What counts as valuable work is not determined by what the factory finds difficult, expensive, or technically sophisticated to make. It is determined by what the customer is willing to pay for. Everything else is waste, regardless of how sophisticated or busy it looks.

- **Waste is the primary problem, not cost.** Cost reduction follows naturally from waste elimination; pursuing cost reduction directly often hides waste. The stance's primary object is to make waste visible and removable. The seven wastes (transportation, inventory, motion, waiting, overprocessing, defects, underutilized talent) are categories of visibility, not a checklist.

- **Flow is prior to efficiency.** A system that moves work steadily through every stage is superior to one where individual stages are "efficient" (highly utilized, with high throughput) but work stalls between them. The stance rejects local optimization that breaks flow.

- **Pull, not push.** Work should move through the system only when the next stage is ready to accept it. A system driven by demand (pull) is superior to one driven by production plans or departmental targets (push), because pull prevents overproduction and reveals actual bottlenecks.

- **Continuous improvement requires making the actual work visible.** Gemba (the real place where work happens) is the only valid source of truth. Improvement cannot happen through remote planning; it emerges from the people doing the work seeing their own process clearly.

- **The worker's judgment and problem-solving capacity are the most durable asset.** Jidoka (autonomation) means empowering workers to stop the line when something is wrong, not replacing judgment with automation. The system should amplify human perception and decision-making, not bypass it.

- **Small problems are signals, not anomalies.** A defect, a small delay, a moment when a worker has to pause — these are not irritations to suppress but invitations to understand what the system is not yet capable of doing reliably.

## Guiding Questions

**The flow and its obstacles**
- Where does work wait? For how long? Why?
- Where does work move faster than the next stage can absorb it?
- What is the actual cycle time for a complete unit, and how does it compare to the time the unit spends actually being worked on?
- Where is work stalling, and what is causing the stall?

**Waste and its visibility**
- What activities in the process add no value from the customer's perspective? (Not the company's perspective — the customer's.)
- Where is inventory sitting, and what is it hiding?
- What motion is necessary, and what is wasted motion?
- Where is work being done twice, or done and then undone?
- What information or decisions are being delayed or duplicated?

**Push versus pull**
- Is this work being initiated by a upstream plan, or by a signal from downstream that something is needed?
- What happens when production exceeds what the next stage can absorb?
- Are there buffers and queues, and what are they masking about the system?

**Gemba and actual conditions**
- What does the actual process look like when observed in real time? How does it differ from the documented process?
- Where is the worker slowing down, pausing, or working around a system constraint?
- What information is the worker holding in their judgment that is not captured in the system?

**Jidoka and problem visibility**
- Where could the worker stop the line (literally or metaphorically) when something is wrong? Are they empowered to do so?
- What small problems are being tolerated or hidden rather than treated as improvement opportunities?
- What judgment is being automated away that should remain in human hands?

**The root cause beneath the symptom**
- When something goes wrong, are we treating the symptom or asking "why?" five times?
- What does the repeated occurrence of the same defect or delay reveal about the system's design?

## What It Reveals

- **Hidden waste:** The vast majority of time and motion in most processes is non-value-added — waiting, transporting, handling inventory, rework. Only direct, visible observation surfaces this; planning documents hide it.
- **The real constraint:** The bottleneck in a system is often not the most expensive or sophisticated stage but the least visible one. Optimizing elsewhere wastes effort.
- **The cost of push:** Systems driven by production plans or departmental targets create overproduction, inventory buffers, and rework. The cost of these is not captured in individual department metrics.
- **Worker knowledge:** The people doing the work routinely see problems, inefficiencies, and improvements that do not appear in meetings or dashboards because the workers are not asked, or their expertise is not recognized.
- **The relationship between standardization and improvement:** Improvement only becomes visible and repeatable if the baseline (standard work) is first clear. Standards are not constraints but foundations.
- **The difference between busyness and value:** A worker or machine that is constantly in use but producing for inventory or rework is not productive. A process that sometimes waits is often healthier than one that is perpetually congested.

## What It Obscures

- **Social distribution of gains and losses.** TPS focuses on eliminating waste but does not inherently ask who benefits when waste is eliminated. Productivity gains may accrue to ownership, not workers; a TPS reading without labor analysis misses this. (Pair with a labor-focused or Marxist reading when power distribution matters.)
- **The tacit knowledge that TPS depends on.** The stance assumes workers can articulate problems and improvements, and that management will listen. It obscures the organizational and cultural preconditions required for Gemba to work. Applied in a hierarchical or adversarial setting, TPS becomes theater.
- **Variability and adaptation.** TPS standardizes work to make waste visible, but highly variable or adaptive processes (creative work, novel problem-solving, customization) may resist standardization. The stance is weaker in domains where the work itself is not repeatable.
- **Long-term innovation beyond incremental improvement.** Continuous improvement of existing flow is TPS's strength; breakthrough redesign or exploration of fundamentally different approaches is less central. A system optimized for lean flow may resist the waste and duplication that radical innovation sometimes requires.
- **Quality-cost-delivery trade-offs in contexts of scarcity.** TPS assumes that eliminating waste improves all three. In contexts where quality is genuinely expensive, or delivery is constrained by scarce resources, the harmony can break. The stance has less to say about hard prioritization.
- **Systems where pull cannot be clearly defined.** In domains where demand is uncertain, irregular, or where the customer cannot specify what they want in advance, pull-driven logic becomes harder to apply. The stance works best where the product and demand are relatively stable and clear.

## Output Format

```
## Toyota Production System Reading: <process / workflow / system>

### Scope
- What is being read: <manufacturing / service / delivery process>
- Why this object: <what makes it a good site for the stance>

### The actual flow
- Where work waits and for how long
- Where work moves faster than the next stage can absorb
- Cycle time versus total lead time
- Actual bottlenecks in the flow

### Waste and its distribution
- Non-value-added activities visible in Gemba observation
- Inventory and what it is masking
- Motion waste and work-around patterns
- Rework and duplication
- Delayed information or decisions

### Push versus pull logic
- What initiates work: upstream plan or downstream signal
- Buffers and queues and what they hide
- Overproduction and its consequences

### Gemba observations
- What the actual process reveals that documented process does not
- Where workers pause, slow, or work around constraints
- Judgment being held in worker hands versus automated away

### Problem visibility and Jidoka
- Where the line could be stopped and is not
- Repeated small problems treated as normal
- Opportunities for worker autonomy and problem-sensing

### Root cause and standard work
- What the repeated occurrence of problems reveals about system design
- Current standard work and where it is breaking down
- What standardization would enable

### Conversation with other stances
- What a labor, feminist, or critical reading would add about who gains
  and loses from waste elimination and productivity increases
- What a design or innovation stance would push back on regarding the
  limits of incremental improvement

### Confidence: high | medium | low
<basis: how directly the process exposes its own waste and flow
constraints; how stable and repeatable the work is; whether the
organizational culture supports actual Gemba observation and worker
input; whether the system's constraints are technical or social >
```
