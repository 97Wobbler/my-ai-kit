---
name: Gustafson's Law
domain: architecture
source: John L. Gustafson, "Reevaluating Amdahl's Law," Communications of the ACM 31, no. 5 (1988)
best_for: Predicting speedup when problem size scales with processor count (weak scaling), revealing when parallelization yields near-linear returns despite serial overhead
one_liner: "Scaled speedup — when problem size grows with processor count, parallelism yields near-linear gains (Amdahl's dual)."
---

# Gustafson's Law

## Overview

Gustafson's Law is the **scaled-speedup dual** of Amdahl's Law. Where Amdahl assumes a fixed problem size and asks "how many processors will speed it up?", Gustafson assumes the problem size grows with available processors and asks "how much larger a problem can we solve in the same time?" The law explains why supercomputers and big-data systems achieve near-linear speedup despite serial bottlenecks: they are not solving a fixed problem faster, but solving increasingly large problems in constant time. Gustafson's insight reframes the parallelization picture, showing that the serial fraction's impact is secondary when the workload itself is scaled.

## Core Variables and Relationships

- **P** = parallelizable fraction of the workload (0 ≤ P ≤ 1)
- **S** = serial fraction = 1 − P
- **N** = number of processors
- **Speedup(N)** = theoretical speedup when problem size scales with N

The core formula is:

```
Speedup(N) = N − S·(N − 1) = S + P·N
```

Expanding:

```
Speedup(N) = (1−P) + P·N
```

For large N and small P (typical of big-data and simulation workloads), **Speedup(N) ≈ P·N**, which is nearly linear in the number of processors. The serial overhead (1−P) becomes negligible relative to the total speedup.

## Key Predictions

1. **Near-linear scaling is achievable in weak-scaling workloads.** If P > 0.90 (90% parallelizable), speedup remains close to N even for hundreds of processors, as long as the problem size grows proportionally.

2. **The serial fraction's impact is inverted relative to fixed-size Amdahl analysis.** A 5% serial fraction in Amdahl's Law (ceiling ≈ 20×) becomes nearly invisible in Gustafson's Law: Speedup(128) ≈ 0.05 + 0.95×128 ≈ 121.6×.

3. **Scaling fails when the problem cannot grow.** If the workload is fixed-size (transaction processing, interactive systems), Gustafson's prediction breaks down and Amdahl's Law applies.

4. **Communication and synchronization overhead still matters.** Even though Gustafson predicts near-linear scaling, real communication costs, memory bandwidth limits, and I/O bottlenecks can degrade actual speedup below the formula.

5. **Typical use cases show sustained speedup up to 1000+ processors.** Large-scale simulations, machine-learning training, big-data analytics, and scientific computing achieve close to Gustafson's predictions when the problem size scales.

## Application Procedure

1. **Verify the workload is weak-scaling.** Does the problem size grow with available processors? (e.g., simulation of a larger system, processing a larger dataset, running longer timesteps). If problem size is fixed, use Amdahl's Law instead.

2. **Estimate the serial fraction S.** Profile the code to measure what fraction of per-iteration or per-batch time cannot be parallelized (communication, synchronization, I/O). This should be small (< 10%) for weak-scaling workloads.

3. **Calculate the scaled speedup curve.** For each processor count N, compute Speedup(N) = S + P·N. Plot it.

4. **Compare to Amdahl's ceiling.** Show both models on the same graph. Gustafson's line will be much steeper, illustrating the value of scaling the problem.

5. **Identify communication and I/O bottlenecks** that prevent actual speedup from reaching the formula. Measure bandwidth utilization, network latency, and synchronization overhead.

6. **Measure actual speedup** at key processor counts (e.g., 4, 16, 64, 256). Validate that the weak-scaling assumption holds and that measured speedup tracks the Gustafson formula.

## Boundary Conditions

- **Problem-size scaling assumption.** The law only applies if the problem genuinely scales—not all workloads do. If problem size is bounded (maximum dataset, fixed time budget), the scaling assumption breaks and Amdahl's Law applies.

- **Communication and I/O overhead.** The formula assumes O(1) communication per processor. In reality, all-reduce, broadcast, I/O synchronization, and network latency are O(N) or worse, degrading speedup.

- **Memory bandwidth saturation.** Even if computation is parallelizable, if all N processors contend for the same memory subsystem, bandwidth becomes the bottleneck. Actual speedup plateaus despite the formula predicting linear growth.

- **Not applicable to latency-sensitive workloads.** Interactive systems (web servers, transaction processing) cannot grow the problem size arbitrarily; Gustafson's assumptions fail.

- **Ignores load imbalance.** The formula assumes perfect load balance across processors. Real workloads often have skewed distributions; some processors finish early and idle while others are still computing.

- **Comparison to Amdahl obscures the true difference.** Gustafson does not contradict Amdahl; they answer different questions. Conflating them is a common mistake.

## Output Format

```
## Scaled Speedup Analysis: <application or system>

**Workload profile:**
- Workload type: <simulation, analytics, scientific computing, ML training, etc.>
- Serial fraction (S): <percentage>
- Parallelizable fraction (P): <percentage>
- Scaling method: <how does problem size grow with N?>
- Measurement baseline: <time/problem size on 1 processor or small cluster>

**Speedup comparison:**
| Processor count | Gustafson speedup | Amdahl ceiling | Measured speedup |
|---|---|---|---|
| 1 | 1.0 | 1.0 | ... |
| 4 | ... | ... | ... |
| 16 | ... | ... | ... |
| 64 | ... | ... | ... |
| 256 | ... | ... | ... |

**Scaling limitations:**
- Communication overhead: <estimated O(?) cost per processor>
- Memory bandwidth limit: <GB/s available vs. required>
- I/O bottleneck: <sequential reads/writes that constrain parallelism>
- Load imbalance: <observed distribution of work across processors>

**Actual vs. theoretical:**
- Processor count where measured speedup diverges from Gustafson prediction: <N>
- Primary cause of divergence: <bottleneck>
- Estimated recoverable speedup loss: <percentage>

**Optimization path:**
- Reduction in S: <target serial fraction for next scaling tier>
- Problem-size growth strategy: <how to scale input while maintaining parallel efficiency>
- Communication optimization: <algorithm or infrastructure change to reduce O(N) overhead>

**Confidence: high | medium | low**
<reasoning: stability of measured speedup, whether weak-scaling assumption holds across a wide range of N, applicability of boundary conditions>
```
