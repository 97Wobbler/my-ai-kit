---
name: Amdahl's Law
domain: architecture
source: Gene Amdahl, "Validity of the single processor approach to achieving large scale computing capabilities," IBM Systems Journal 6, no. 4 (1967)
best_for: Predicting the maximum speedup achievable through parallelization given a fixed problem size and a known serial bottleneck
one_liner: "Maximum parallel speedup is capped by the workload's serial fraction; 5% serial → 20× ceiling."
---

# Amdahl's Law

## Overview

Amdahl's Law quantifies the fundamental constraint on parallelization: no matter how many processors you add to a system, the maximum speedup is bounded by the fraction of the workload that cannot be parallelized. It is a corrective model to the intuition that "more processors = more speedup." In reality, serial bottlenecks (lock contention, dependencies, communication) act as a ceiling on possible improvement. The law explains why a program that is 95% parallelizable can achieve at most 20× speedup, not the naive 1000× from 1,000 processors.

## Core Variables and Relationships

- **P** = proportion of the program that can be parallelized (0 ≤ P ≤ 1)
- **S** = serial fraction = 1 − P (the part that cannot be parallelized)
- **N** = number of processors available
- **Speedup(N)** = overall reduction in execution time

The core formula is:

```
Speedup(N) = 1 / (S + P/N)
```

Equivalently:

```
Speedup(N) = 1 / ((1-P) + P/N)
```

As N increases toward infinity, the speedup asymptotically approaches **1/S = 1/(1-P)**, the inverse of the serial fraction. This is the absolute ceiling speedup no matter how many processors are added.

## Key Predictions

1. **5% serial fraction (P = 0.95)**: Maximum speedup ≈ 20×, even with infinite processors. Beyond 20 processors, adding more provides negligible benefit.

2. **1% serial fraction (P = 0.99)**: Maximum speedup ≈ 100×. Scaling remains useful up to ~100 processors.

3. **10% serial fraction (P = 0.90)**: Maximum speedup ≈ 10×. Systems with high serial overhead see diminishing returns very quickly.

4. **Serial bottleneck identification is the leverage point.** The greatest practical gain comes from reducing the serial fraction itself, not from adding processors. A 1% reduction in the serial bottleneck (from 5% to 4%) yields much more speedup than doubling the processor count.

5. **The speedup curve is not linear.** Initial processors yield high returns; each additional processor yields less benefit. This is why low-core systems (4–8 cores) see near-linear speedup but ultra-high-core systems (128+ cores) show much weaker scaling.

## Application Procedure

1. **Profile the workload** to estimate P (the parallelizable fraction). Run the program and measure what fraction of execution time is spent in truly parallel sections (using tools like perf, flame graphs, or tracing). The remainder is S.

2. **Calculate the theoretical speedup curve** for increasing N using the formula above. Plot speedup vs. processor count.

3. **Identify the asymptote.** Read off the maximum speedup (1/(1-P)) and mark it on the graph. This is the hard ceiling.

4. **Locate the serial bottleneck** in the code or architecture. Common sources: mutex locks, synchronization barriers, data dependencies, I/O waits, memory bandwidth limits.

5. **Prioritize reduction of the serial fraction.** Even a small reduction (from 5% to 3%) can double the maximum speedup. This is where engineering effort is best spent.

6. **Re-profile after optimization.** Parallelization benefits are case-specific; validate assumptions with real data.

## Boundary Conditions

- **Fixed problem Size assumption.** Amdahl assumes the problem size is constant as N grows. In weak-scaling scenarios (big-data, simulation) where the problem size grows with available resources, Gustafson's Law is the appropriate dual model.

- **Communication overhead ignored.** The formula assumes P/N speedup from N processors; in reality, inter-processor communication, cache coherency, and memory contention degrade performance. Actual speedup is lower than the formula predicts.

- **Amdahl's coordination cost.** In practice, adding processors creates coordination overhead (synchronization, lock contention, I/O bottlenecks) that is not explicit in the simple formula. Real systems hit a peak useful processor count and then degrade.

- **Not applicable to embarrassingly parallel workloads.** For truly independent tasks (map-reduce, Monte Carlo), P can approach 1, and Amdahl's ceiling becomes less relevant.

- **Ignores heterogeneous hardware.** The formula assumes all N processors are identical; real heterogeneous systems (GPU + CPU, varying core speeds) require case-specific analysis.

## Output Format

```
## Parallelization Speedup Analysis: <system or program name>

**Workload profile:**
- Parallelizable fraction (P): <percentage>
- Serial fraction (S): <percentage>
- Measurement method: <profiling tool, sampling interval, data size>

**Speedup curve:**
| Processor count | Theoretical speedup | Observed speedup (if measured) |
|---|---|---|
| 1 | 1.0 | ... |
| 2 | ... | ... |
| 4 | ... | ... |
| 8 | ... | ... |
| 16 | ... | ... |
| ∞ | <1/(1-P)> | N/A |

**Serial bottleneck identification:**
- Primary bottleneck: <description, location in code>
- Secondary bottlenecks: <list>
- Estimated impact: <which fraction of S is due to each bottleneck>

**Optimization opportunities:**
- Reducing S from <current> to <target>: estimated new ceiling = <new 1/(1-P)>
- Specific code changes: <list of refactoring targets>

**Scaling recommendation:**
- Useful processor range: <N where returns are still linear or near-linear>
- Beyond this range: <recommendation for alternative approaches (e.g., problem decomposition, algorithmic change)>

**Confidence: high | medium | low**
<reasoning: data quality of profile, stability of serial fraction across workload variants, applicability of boundary conditions>
```
