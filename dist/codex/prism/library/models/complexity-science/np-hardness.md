---
name: np-hardness
display_name: NP-Hardness (Cook-Karp)
class: model
underlying_class: native
domain: complexity-science
source: Stephen Cook, "The Complexity of Theorem-Proving Procedures," Proceedings of the 3rd ACM STOC, 1971; Richard Karp, "Reducibility Among Combinatorial Problems," Complexity of Computer Computations, 1972
best_for: Determining whether a decision problem admits a polynomial-time algorithm or requires switching strategy to approximation, heuristic, or constraint relaxation
one_liner: "Classify decision problems as tractable (P) or likely intractable (NP-hard); if NP-hard, polynomial-time optimality is implausible and you must reframe."
---

# NP-Hardness (Cook-Karp)

## Overview

NP-Hardness is the theoretical boundary between computational problems that are provably solvable in polynomial time (P) and those for which no known polynomial-time algorithm exists, and for which a polynomial-time algorithm would imply P = NP (widely conjectured false). The theory does not tell you whether an NP-hard problem *can* be solved; it tells you that finding a polynomial-time *optimal* solution to all instances is implausible unless the unproven P = NP conjecture is true. The practical consequence is a binary classification: if your problem is in P, invest in exact algorithms; if it is NP-hard, you must switch to approximation, heuristic, parameterized, or offline (precomputed) methods. The model is fundamentally predictive — it predicts the computational *structure* of the problem space, not the outcome of any single instance.

## Core Variables and Relationships

The core claim rests on three variables and one canonical relationship:

1. **Decision problem D** — a well-defined Yes/No question parameterized by input size n.
   - A decision problem is solvable in polynomial time (in P) if there exists an algorithm that solves all instances of size n in O(n^k) steps for some fixed k.
   - Verifiable in polynomial time means: given a proposed "Yes" answer, you can check it in O(n^k) time. (This defines NP, the Nondeterministic Polynomial class.)

2. **Polynomial-time reduction R from a known NP-hard problem H to D** — a mapping that transforms any instance of H into an instance of D such that:
   - The reduction itself runs in polynomial time.
   - H has a "Yes" answer if and only if the reduced instance of D has a "Yes" answer.
   - If D were solvable in polynomial time, H would be too.

3. **The containment relationship:**
   - **P ⊆ NP** (every polynomial-time solvable problem is also verifiable in polynomial time).
   - **NP-complete problems** are in NP *and* are NP-hard (a polynomial-time solution to any one would solve all NP problems in polynomial time).
   - **NP-hard problems** are at least as hard as the hardest problems in NP, even if they are not verifiable in polynomial time themselves (e.g., optimization versions of NP-complete problems).

The canonical claim: **If D is NP-hard and a polynomial-time algorithm for D is found, then P = NP, which contradicts the widespread (but unproven) belief that P ≠ NP.**

## Key Predictions

- **An NP-hard decision problem has no known polynomial-time algorithm and no proof that one cannot exist**, but the absence of a polynomial-time solution is *consistent* with the strong empirical evidence across 50+ years and millions of researcher-hours that P ≠ NP. Betting your timeline on discovering a polynomial-time algorithm for an NP-hard problem is implausible.

- **Instances of NP-hard problems can be solved**, but the time required to find an optimal solution grows exponentially in the worst case — O(2^n) or O(n!) — even with the best known algorithm. Small instances (n < 30) may be tractable; large instances are not.

- **Approximation and heuristic methods become necessary at scale.** If D is NP-hard, a 2-approximation algorithm (guaranteed within 2× optimal) or a greedy heuristic (no guarantee but empirically good) running in polynomial time is often the practical boundary.

- **Structure within an NP-hard problem can be exploited.** Parameterized algorithms, branch-and-bound, dynamic programming on tree-decompositions, and integer linear programming solve many NP-hard problems for *some* input distributions or sizes, even though worst-case complexity remains exponential.

- **NP-hardness is a *worst-case* statement.** It says nothing about the *average-case* or *typical-case* complexity. Many NP-hard problems (e.g., random 3-SAT at certain density thresholds) are easy on average and hard only on rare pathological instances.

- **The boundary is sharp: a small change in the problem statement can move a problem from P to NP-hard.** Example: shortest path in a DAG is in P; longest path is NP-hard. This brittleness makes problem formulation critical.

## Application Procedure

Instantiate the model against a concrete computational problem you are tasked with solving.

1. **Define the decision problem precisely.** State the Yes/No question. What is the input? What is the constraint or goal? Write an instance and a "Yes" answer.

2. **Determine whether the problem is in NP.** Can you *verify* a proposed "Yes" answer in polynomial time? (This is often easier than deciding the problem itself.) If no, the problem is outside NP and may be even harder (e.g., co-NP-hard, PSPACE-hard).

3. **Search for a known NP-hardness result.** Consult standard references (Garey & Johnson *Computers and Intractability*, NP-completeness databases like NIST FOCS or Wikipedia lists of NP-complete problems). Is your problem a known NP-hard variant?

4. **If not found directly, attempt a polynomial-time reduction from a known NP-hard problem to yours.** Pick a canonical hard problem (3-SAT, Hamiltonian cycle, 3-partition, bin packing, traveling salesman decision version). Can you transform instances of it into instances of your problem in polynomial time, preserving the Yes/No answer?

5. **If the reduction succeeds, classify your problem as NP-hard.** Document the reduction for future reference.

6. **If no reduction is found and no polynomial-time algorithm is known, classify the problem as "likely NP-hard"** (open problem) and flag the uncertainty.

7. **If a polynomial-time algorithm is found, the problem is in P; NP-hardness is ruled out.**

8. **Based on the classification, choose your strategy:**
   - **If in P:** Implement the polynomial-time algorithm. Optimize as needed.
   - **If NP-hard and instance sizes are small (n < 25–30):** Exact algorithms (branch-and-bound, dynamic programming, integer linear programming, SAT solvers) are viable.
   - **If NP-hard and instance sizes are large:** Switch to approximation algorithms (with bounded error guarantees), heuristics (greedy, local search, simulated annealing, genetic algorithms), or problem relaxation (drop constraints, ask for "good enough" instead of optimal).
   - **If NP-hard and a special structure is present:** Use parameterized algorithms, preprocessing reductions, or structure-exploiting methods (e.g., tree-width decomposition for graph problems).

9. **Check boundary conditions** (below). Flag any that apply.

## Boundary Conditions

NP-Hardness is a worst-case, asymptotic, theoretical statement. It provides incomplete guidance when:

- **The instance sizes are always small** (n < 20). Worst-case exponential algorithms often outperform heuristics on small instances in practice. NP-hardness does not say "never use exact methods here."

- **The problem has special structure** (e.g., bipartite graphs, interval graphs, planar graphs, tree decompositions). Many problems are NP-hard on general graphs but polynomial-time solvable on restricted classes. A general NP-hardness classification may not apply to your specific instances.

- **The average or typical case, not the worst case, dominates.** Many NP-hard problems (random 3-SAT, random instances of knapsack) are easy on average. NP-hardness says nothing about this and can lead to overestimating practical difficulty.

- **Approximation or relaxation is acceptable and your problem admits a constant-factor or PTAS (polynomial-time approximation scheme).** If you can relax the objective from "optimal" to "within 1.5× optimal," NP-hardness becomes less binding.

- **You can precompute, cache, or exploit dynamic inputs.** Offline optimization (precompute once, serve many queries) or online algorithms with lookahead can circumvent worst-case hardness in specific contexts.

- **The problem is in a higher complexity class** (PSPACE-hard, undecidable). NP-hardness does not capture these; you need a different framework entirely.

## Output Format

```
## NP-Hardness Classification: <problem name>

**Problem definition:** <precise Yes/No question with input/output specification>
**Input size parameter:** <n = number of items/nodes/variables/constraints, etc.>
**Feasibility:** <in P / NP-hard / unknown / conjectured hard>

### Verification (NP membership)
- Can a proposed "Yes" answer be verified in polynomial time? <yes/no>
- Verification procedure: <describe the check>

### Hardness evidence
- Known NP-hard variant or reduction: <cite the source or describe the reduction from a canonical hard problem>
- Reduction mapping: <input → transformed input, correctness argument in 1–2 sentences>

### Practical implications
- Worst-case complexity: <O(2^n), O(n!), other>
- Instances solvable exactly: <size range where exact methods are practical>
- Necessary strategy for larger instances: <approximation / heuristic / relaxation / parameterized / other>

### Special structure or exceptions
- Does your problem fall into a polynomial-time subclass? <e.g., bipartite variant, tree-structured, etc.>
- Average-case complexity: <if known, e.g., "easy on random instances">

### Recommended approach
- Algorithm tier 1 (try first): <exact solver for small n, heuristic for large n, approximation, etc.>
- Algorithm tier 2 (if tier 1 insufficient): <alternative heuristic, relaxation, or constraint-loosening>
- Fallback: <further problem simplification or reformulation>

### Confidence: high | medium | low
<reasoning: clarity of problem definition + strength of NP-hardness proof + applicability of boundary conditions>
```
