---
name: axiomatic-design
display_name: Axiomatic Design
class: model
underlying_class: native
domain: manufacturing
source: Nam P. Suh, "The Principles of Design," Oxford University Press, 1990; developed further in "Axiomatic Design: Advances and Applications," Oxford University Press, 2001
best_for:
  - Diagnosing whether a design is inherently complex or elegant by mapping the functional requirements → design parameters → process variables chain
  - Predicting design cycle time, manufacturability, and robustness by measuring independence and information content
one_liner: "Predict design elegance and manufacturability via the independence and information axioms."
---

# Axiomatic Design

## Overview

Axiomatic Design claims that elegant, robust, and manufacturable designs are governed by two universal axioms: the **Independence Axiom** (functional requirements must be independently satisfied by design parameters) and the **Information Axiom** (the information content of a design — the gap between what the design can do and what it must do — should be minimized). The model is both diagnostic and prescriptive: it explains *why* some designs are fragile or coupled to manufacturing variation, and it provides a procedure to improve them. Unlike heuristic design rules, Axiomatic Design treats design as a mapping problem with measurable structure, making it predictive for manufacturability, cycle time, and robustness.

## Core Variables and Relationships

The model decomposes a design into three coupled hierarchies:

1. **Functional Requirement (FR) Space** — what the design must do.
   - FRs are independent, testable statements of what the design must achieve (e.g., "minimize vibration," "support load of 1000 N").
   - FRs are hierarchical; each FR can be decomposed into sub-FRs at lower levels.

2. **Design Parameter (DP) Space** — how the design achieves those FRs.
   - DPs are the physical variables the designer controls (dimensions, materials, geometry, topology).
   - Each DP at a level should satisfy one or more FRs.

3. **Process Variable (PV) Space** — how the design is manufactured.
   - PVs are the variables the manufacturer controls (temperature, pressure, feed rate, tooling).
   - Each PV should map to one or more DPs.

The core mapping relationships:

- **Independence Axiom**: The mapping from FR → DP and from DP → PV must be **diagonal or triangular**, never dense or coupled. That is, changing one DP should satisfy one FR without degrading others; changing one PV should affect one DP without cascading into others. A dense coupling matrix means the design is over-constrained, fragile, and difficult to manufacture.

- **Information Axiom**: The **information content I** of a design is defined as:

        I = log₂ (1 / P_design)

  where P_design is the probability that the design successfully meets all FRs given the allowable tolerance band and the manufacturing process capability. Lower information content (higher probability of success) is better; higher information content signals that the design window is tight relative to process variation, so it will fail frequently or require tight tolerance.

- **Design Range vs. System Range**: For each FR, there is a design range (the acceptable values the DP can take) and a system range (the acceptable values for the FR, given by specification). The design must fit: system range ⊇ design range. If the design range exceeds the system range, the design is over-specified; if it falls short, the design is infeasible. The information content is the log-probability that the two overlap, given process variation.

## Key Predictions

- **Coupled designs collapse under variation.** A design with a dense mapping matrix (many DPs coupled to many FRs) will be sensitive to small changes in process capability or tolerance. When manufacturing variation increases, coupled designs fail catastrophically; decoupled designs degrade gracefully or not at all.

- **Design cycle time is proportional to information content.** Designs with high information content require tight control, frequent rework, and longer validation cycles. A design that maps to information content I = 2 bits will take roughly 4× longer to debug than one with I = 0.5 bits, all else equal.

- **Decoupled designs are faster to scale.** A design with a diagonal (fully decoupled) mapping matrix can be scaled to higher production volumes with minimal process redesign. Each DP can be optimized independently; each PV can be tweaked independently. Coupled designs require process-wide redesign whenever a DP changes.

- **Adding constraints to a coupled design makes it worse, not better.** If a design is already dense (many FRs competing for few DPs), adding a new FR or tightening a tolerance increases information content exponentially, not linearly. The design may become infeasible.

- **Designs decompose cleanly along independence boundaries.** A modular design naturally breaks at points where the mapping matrix transitions from diagonal to decoupled; designs that violate this boundary (e.g., forcing a module boundary across a coupled block) will have poor interfaces and high rework.

- **Manufacturability is predictable from the DP-to-PV mapping.** If a design has low DP-to-PV information content but high FR-to-DP information content, the product will be easy to make but fragile in use. Conversely, if DP-to-PV information is high, the design will be robust but expensive to manufacture.

## Application Procedure

Instantiate the model against a specific design or design problem.

1. **Define the functional requirements (FRs) exhaustively.** Write a list of independent, testable requirements the design must satisfy. Avoid conflating FRs with solutions; "minimize vibration" is an FR, "use a spring damper" is a DP. Organize FRs hierarchically if the design is complex.

2. **Identify the design parameters (DPs) that will satisfy those FRs.** For each FR, specify which physical variables (dimensions, materials, topology, etc.) the designer can control to achieve it. Do not pre-commit to a design; list the candidate DPs.

3. **Construct the functional mapping matrix M**, where rows are FRs and columns are DPs. Enter a non-zero value (X) if changing a DP affects that FR; enter 0 if there is no coupling.
   - Ideal: diagonal matrix (each DP couples to exactly one FR).
   - Acceptable: triangular matrix (careful ordering of FRs and DPs reveals no circular coupling).
   - Problematic: dense matrix (multiple FRs depend on the same DP, or one DP affects multiple FRs).

4. **For each DP, estimate the design range** (the range of DP values that satisfy the corresponding FR) and the **system range** (the specification). Compute the probability P_design that a nominal DP value, given manufacturing tolerance, will fall within the system range. Calculate information content I = log₂(1/P_design) for each FR.

5. **Repeat for the DP-to-PV mapping.** Construct the process mapping matrix and estimate information content at the manufacturing stage. If PV information content is very high, manufacturability is at risk.

6. **Decompose the design hierarchically.** For each high-information-content FR or dense region of the mapping, ask whether the FR can be broken into independent sub-FRs, or whether the DP set can be reorganized to decouple them. Redraw the mapping and re-estimate information content.

7. **Identify the dominant information bottleneck.** Is the design bottlenecked by FR ambiguity (information at the top level)? By DP coupling? By process capability? This tells you where to invest engineering effort.

8. **Check boundary conditions** (below). If any apply, note the limits of this analysis.

## Boundary Conditions

Axiomatic Design is powerful for physical product design but breaks down or becomes incomplete under several conditions:

- **Information content cannot be estimated without a process model.** If the manufacturing process is not yet defined or is highly variable / non-deterministic, you cannot compute P_design or I. The model becomes qualitative (check coupling structure only).

- **Soft requirements (aesthetics, user experience, brand fit).** These are genuine FRs but are difficult to map to a design range and system range. Including them in the model requires subjective thresholds that undermine the axiom's rigor.

- **Highly integrated systems (e.g., software, electronics, biological systems).** The model was developed for mechanical design and assumes clear separation of FR, DP, and PV spaces. Software design has dense coupling by nature; applying Axiomatic Design directly often produces artificial decompositions.

- **Adaptive or learning designs.** If the design includes feedback control or learning (e.g., a system that adjusts parameters in real time), the static FR-to-DP mapping does not capture the dynamic corrective mechanism, and information content calculations are misleading.

- **Supply chain and supplier variation.** The model assumes you control the process variables. If key DPs are supplied by external vendors with uncontrolled variation, the DP-to-PV mapping is incomplete.

- **Requirements evolution.** If FRs are discovered late or are subject to change, the hierarchical decomposition and the mapping matrix must be re-done, creating rework that the model does not account for.

## Output Format

```
## Axiomatic Design Analysis: <design name>

**Design scope:** <brief description of what is being designed>
**Decomposition level:** <top-level FRs or detailed sub-FRs>

### Functional Requirements (FR space)
| FR ID | FR | Decomposition path | Notes |
|---|---|---|---|
| FR1 | <requirement> | <hierarchy> | ... |

### Design Parameters (DP space)
| DP ID | DP | Satisfies FR(s) | Design range | System range | Notes |
|---|---|---|---|---|---|
| DP1 | <parameter> | FR1 | <value range> | <spec> | ... |

### Functional Mapping Matrix (FR → DP)
```
     DP1  DP2  DP3
FR1  X    0    0
FR2  X    X    0
FR3  0    X    X
```
**Structure:** <diagonal / triangular / dense>

### Information Content (FR level)
| FR | P_design | Information (bits) | Risk level |
|---|---|---|---|
| FR1 | <probability> | <bits> | <high/medium/low> |

### Process Mapping Matrix (DP → PV)
```
     PV1  PV2  PV3
DP1  X    0    0
DP2  X    X    0
DP3  0    X    X
```
**Manufacturability:** <high-risk / medium / low-risk>

### Key couplings and decoupling opportunities
- <Coupling identified and proposed decomposition>

### Dominant information bottleneck
<Which stage (FR or PV) carries the highest total information, and why>

### Boundary-condition notes
<Which boundary conditions apply and whether the model guidance is actionable>

### Confidence: high | medium | low
<Reasoning: clarity of FR definition + completeness of process model + whether soft requirements dominate + stability of requirements>
```
