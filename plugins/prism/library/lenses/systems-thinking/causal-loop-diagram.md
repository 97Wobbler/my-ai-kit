---
name: causal-loop-diagram
display_name: Causal Loop Diagram (Sterman)
class: lens
underlying_class: native
domain: systems-thinking
source: "John D. Sterman, \"Business Dynamics: Systems Thinking and Modeling for a Complex World\" (2000)"
best_for:
  - Mapping feedback structures in complex systems
  - Identifying reinforcing vs. balancing mechanisms
  - Finding leverage points and unintended consequences
one_liner: "Extract variables and signed causal links, identify reinforcing and balancing loops to expose system behavior drivers."
---

# Causal Loop Diagram (Sterman)

## Overview
A causal loop diagram (CLD) maps how variables in a system influence one another through signed links (positive: increase → increase or decrease → decrease; negative: increase → decrease or decrease → increase) and identifies feedback loops — reinforcing loops that amplify change, and balancing loops that resist it. Practitioners use CLDs to surface the structural reasons a system produces its observed behavior, to spot where interventions will or won't work, and to communicate system logic without equations. The discipline is rigor in identifying every causal link and correctly signing it.

## Analytical Procedure

### Phase 1 — Extract Variables and Links

1. **Define the system boundary.** Write one sentence: what system are you mapping? What phenomena are you trying to explain? This bounds which variables belong in the diagram and which belong outside.

2. **List all relevant variables.** These are quantities that change over time or whose values matter to the question in Step 1. Include stocks (accumulations: inventory, debt, population), flows (rates: hiring, spending, evaporation), and auxiliary variables (intermediate calculations or perceptions). Write 8–15 variables; fewer and you're ignoring structure, more and you're losing clarity.

3. **For each variable, ask: "What causes this to increase or decrease?"** Write down every variable that has a direct causal influence on it. Do not include correlations or consequences — only direct influences.

4. **For each causal link, determine its sign.** Draw an arrow from cause to effect and label it **+** or **−**:
   - **+** (positive): when the cause increases, the effect increases (all else equal). When the cause decreases, the effect decreases.
   - **−** (negative): when the cause increases, the effect decreases. When the cause decreases, the effect increases.
   - Mark **±** if the link changes sign depending on context (e.g., "rainfall" affects "crop yield" positively up to saturation, then negatively). If context-dependent, split into separate links with conditions noted.

5. **Validate each link with a test case.** Pick a concrete scenario: "If [cause] increases by X%, does [effect] increase or decrease?" If you cannot answer confidently, the link is not causal — it's either spurious or you're missing an intermediate variable.

### Phase 2 — Identify Loops

6. **Trace all feedback loops.** A loop is a closed path: start at any variable, follow arrows, and return to the starting variable. Use a distinct color or label for each loop.

7. **For each loop, compute its sign.** Multiply the signs of all arrows in the loop:
   - If the product is **positive** (odd number of minus signs or zero minus signs), it is a **reinforcing loop** (R). A reinforcing loop amplifies; once started, it continues in the same direction until a limit is hit.
   - If the product is **negative** (even number of minus signs), it is a **balancing loop** (B). A balancing loop resists change; it tends toward a goal or equilibrium.

8. **Name each loop.** Use a gerund phrase that describes the dynamic: "Debt Accumulation," "Supply and Demand Stabilization," "Market Share Competition." The name should reveal the mechanism, not just list variables.

### Phase 3 — Structural Analysis

9. **Identify loop dominance.** Which loops compete for control of the system? When reinforcing loops dominate early and balancing loops kick in later, growth-then-plateau behavior results. When balancing loops are stronger, steady-state behavior results.

10. **Spot delay nodes.** Mark variables where there is a time delay between cause and effect (e.g., "Hiring Decision" → [delay] → "Workers on Payroll"). Delays destabilize systems; they are breeding grounds for oscillation and overshoot.

11. **Check for missing links.** Are there any variables that *seem* like they should be connected but aren't? If so, either: (a) they are not actually causal, (b) they are outside your system boundary (intentionally), or (c) your diagram is incomplete. Make the decision explicit.

## Evaluation Criteria

| Check | Pass |
|---|---|
| System boundary is stated in one sentence | Y/N |
| All variables are concrete quantities (not vague concepts) | Y/N |
| Each causal link is signed (+ or −) and test-case validated | Y/N |
| All feedback loops are traced and colored or labeled distinctly | Y/N |
| Each loop is signed (R or B) by multiplying arrow signs | Y/N |
| Each loop has a name describing its mechanism | Y/N |
| Delay nodes are marked where cause-effect is not instantaneous | Y/N |
| No loops are missing (or absences are justified) | Y/N |

## Red Flags

- A variable has no incoming or outgoing causal links. Either it doesn't belong in the diagram or you've missed its connections.
- A link is signed but the test-case validation is hedged ("usually +") or absent. Without validation, the sign is a guess.
- A loop is labeled but never named. The name is where you decode what the loop actually *does* — skipping it leaves the finding opaque.
- All loops are reinforcing. Reinforcing-only systems are unstable and unbounded; if your diagram shows this, check whether balancing mechanisms (market saturation, resource limits, negative feedback) are missing.
- Delays are not marked. Unmarked delays hide the source of oscillation and poor coordination; they are cheap to spot and costly to miss.
- The system boundary is vague ("our business," "the economy"). Vague boundaries create creep — new variables get added midway, invalidating earlier links.

## Output Format

```
## Causal Loop Diagram Analysis

**System definition:**
<one sentence defining what system and phenomenon you are mapping>

### Variables
| # | Variable | Type (Stock/Flow/Auxiliary) | Unit or Range |
|---|---|---|---|
| 1 | <...> | <...> | <...> |
| 2 | <...> | <...> | <...> |

### Causal Links
| From | To | Sign | Test Case | Validity |
|---|---|---|---|---|
| <...> | <...> | +/− | "If [cause] increases by X%, [effect]..." | Solid/Plausible/Shaky |

### Feedback Loops Identified
| Loop Name | Variables | Path | Sign (R/B) | Mechanism |
|---|---|---|---|---|
| <e.g., "Debt Accumulation"> | A → B → C → A | +, +, − (net: −) | B | Resists increase in A by raising costs |

### Delays
| Link | Delay Duration | Impact |
|---|---|---|
| [Cause] → [Effect] | <e.g., "2-week hiring lag"> | Causes overshoot in hiring when demand spikes |

### Dominance Analysis
<Which loops compete for control? When does reinforcing loop activation switch to balancing loop dominance?>

### Missing Links (Justified)
<Are there obvious candidates for causal links that were omitted? Why?>

### Confidence
<high/medium/low> — <justification: e.g., "high — all links validated by domain experts and tested against historical scenarios. Delays marked where data supports them. Medium — two variables (X, Y) are based on assumed proxies, not direct measurement.">
```
