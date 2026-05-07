---
name: spanning-trees
display_name: Spanning Trees (Borůvka, Kruskal, Prim)
class: model
underlying_class: native
domain: graph-theory
source: Otakar Borůvka, 1926; Joseph Kruskal, "On the Shortest Spanning Subtree of a Graph and the Traveling Salesman Problem," Proceedings of the American Mathematical Society, 1956; Robert C. Prim, "Shortest Connection Networks and Some Generalizations," Bell System Technical Journal, 1957
best_for:
  - Finding minimum-cost network backbones that connect all nodes
  - Characterizing optimal spanning structure under edge-weight constraints
  - Designing efficient network infrastructure (power grids, telecommunications, roads)
one_liner: "Minimum-cost connecting subgraph — selects n−1 edges to span n nodes while minimizing total weight."
---

# Spanning Trees (Borůvka, Kruskal, Prim)

## Overview

A spanning tree model characterizes the optimal subgraph structure for connecting all nodes in an undirected weighted graph using the fewest edges at minimum total cost. The model is prescriptive: given a graph G = (V, E) with edge weights w(e), it identifies which edges to select to form a tree (a connected, acyclic subgraph) that spans all |V| nodes and minimizes total edge weight. Three classic algorithms realize this: Borůvka's (greedy, iteration on components), Kruskal's (greedy, edge-sorted), and Prim's (greedy, node-grown). All three are correct — they produce an identical minimum spanning tree (MST) for any input — but they differ in computational efficiency and the order in which edges are selected. The model is both descriptive (it explains why certain edges must appear in any MST) and prescriptive (it computes which edges those are).

## Core Variables and Relationships

The spanning tree model operates on a weighted undirected graph with the following variables:

1. **Graph structure: G = (V, E, w)**
   - V: set of nodes (vertices), |V| = n
   - E: set of edges, |E| = m
   - w: function mapping each edge e ∈ E to a non-negative real weight w(e)
   - Connectivity: G must be connected (a path exists between any two nodes); if G is disconnected, no spanning tree exists

2. **Spanning tree T ⊂ E**
   - T contains exactly n − 1 edges (constraint from tree structure: a tree on n nodes has n − 1 edges)
   - T is acyclic: no edge in T forms a cycle
   - T is connected: T reaches all n nodes
   - Total weight: W(T) = Σ_{e ∈ T} w(e)

3. **The optimality criterion: Minimum Weight**
   - An MST is any spanning tree with W(T*) ≤ W(T) for all other spanning trees T
   - If all edge weights are distinct, the MST is unique
   - If weights are tied, multiple MSTs may exist, but all have the same total weight

4. **Key structural property: The Cut Lemma (Safe Edge)**
   - For any partition of V into disjoint sets S and V \ S, the minimum-weight edge *crossing the cut* (one endpoint in S, one in V \ S) must appear in some MST
   - Equivalently: if an edge e is the unique minimum weight crossing a cut, e is in every MST
   - This property underlies the correctness of all three algorithms

5. **Edge-selection mechanism (differs by algorithm)**
   - **Kruskal's:** Sort all edges by weight. Iterate through them in increasing order; add each edge if it does not create a cycle (use a union-find data structure to track connected components). Stop when n − 1 edges are selected.
   - **Prim's:** Start with an arbitrary node r. Maintain a set S of nodes in the growing tree. At each step, add the minimum-weight edge from S to V \ S, and include its new endpoint in S. Repeat until S = V.
   - **Borůvka's:** Maintain connected components. At each phase, for each component, select the minimum-weight edge leaving that component (toward a different component). Merge components via selected edges. Repeat until one component remains.

## Key Predictions

- **MST edges are invariant across algorithms:** Despite different selection orders, Kruskal's, Prim's, and Borůvka's all return the same set of edges and total weight W(T*), though not necessarily in the same order of selection. For any given weighted connected graph, there is a unique MST weight (though possibly multiple trees achieving it if weights are tied).

- **Local optimality implies global optimality:** Because of the Cut Lemma, greedily selecting the minimum-weight edge at each step (subject to acyclicity or component-crossing constraint) guarantees the global minimum. No "local greedy trap" exists; this is why all three algorithms are correct.

- **Removing any edge from T* disconnects the tree into two components; the removed edge is the unique heaviest edge on any path between those two components.** Conversely, the MST has the property that for any non-tree edge e, adding e creates a unique cycle, and e is the heaviest edge in that cycle. This characterizes why MST edges are minimal.

- **If a new edge e with weight w(e) is added to the graph, the MST either includes e (if w(e) is small enough to displace some existing edge) or does not.** Specifically, e is in the new MST iff w(e) ≤ the maximum weight on the unique path in the old MST between e's endpoints. This enables fast MST updates.

- **Heavy-weight edges are less likely to appear in the MST.** If the k heaviest edges in the graph are also sparse (few of them), and the rest of the graph is well-connected by lighter edges, then the MST will almost entirely avoid the heavy edges, concentrating on the light subgraph.

- **The MST is a "bottleneck" minimizer:** It minimizes not just total weight but also the maximum edge weight on any path between any two nodes (the diameter, in weight terms). This is why MSTs are used in network design to minimize worst-case link costs.

## Application Procedure

Instantiate the spanning tree model to find the optimal backbone structure for a weighted graph.

1. **Define the graph G and verify connectivity.**
   - Enumerate all nodes V (e.g., cities, routers, substations).
   - Enumerate all edges E and assign weights w(e) (e.g., distance, cost, latency, construction expense).
   - Confirm that G is connected. If not, apply MST separately to each connected component.

2. **Identify the objective: what does minimizing total weight achieve?**
   - In infrastructure, minimizing total edge weight minimizes total construction or maintenance cost while ensuring all sites are reachable.
   - In telecommunications, it may minimize total cable length or total latency sum.
   - Write down the business or operational objective to ensure weight choice is correct.

3. **Choose an algorithm (all yield the same result; choice is computational):**
   - **Kruskal's** is easiest to implement and visualize; O(m log m) with a union-find structure. Use this for small graphs or teaching.
   - **Prim's** is O(m log n) with a binary heap and often faster in practice for dense graphs. Use if graph is dense.
   - **Borůvka's** is O(m log n) and parallelizable; use if you need to distribute the computation or update the MST incrementally.

4. **Run the algorithm and extract the spanning tree T*.**
   - Record all n − 1 edges in T* and their weights.
   - Compute total weight W(T*) = Σ_{e ∈ T*} w(e).

5. **Interpret the MST in context.**
   - Identify which edges (links, connections) must be built or activated.
   - Identify which edges in E were not selected (why not? because they create cycles and are heavier than alternatives).
   - Note the "redundancy gap": graph has m edges; MST uses n − 1. The m − (n − 1) unused edges represent alternatives forgone.

6. **Check boundary conditions** (below). If any apply, note that the MST alone may not be sufficient for the application.

7. **Generate the prediction: the MST is the minimum-cost backbone; any other spanning tree costs more.**
   - Confidence is high if weights are accurately measured and the objective truly is total-weight minimization.

## Boundary Conditions

The spanning tree model assumes an undirected, connected, static graph and a single objective (minimize total weight). It breaks down or becomes incomplete when:

- **The graph is directed.** MSTs are defined for undirected graphs. Directed graphs have minimum spanning *arborescences* (rooted structures), which require different algorithms (Edmonds' algorithm) and may not exist.

- **The objective is multi-criteria** (e.g., minimize weight *and* minimize diameter, or *and* ensure degree constraints). MSTs optimize total weight only; a different tree may be better on a second axis. Use multi-objective optimization or constrained MST variants.

- **Real-time edge arrivals or deletions.** MSTs are static snapshots. If edges appear or disappear dynamically, recomputing the MST from scratch is costly; use dynamic MST data structures (link-cut trees, e.g.) for updates in polylog time.

- **Weights are not fixed or are adversarial.** If an adversary can change edge weights after observing your tree, or if weights are uncertain and you want robust performance, MST gives no guarantee. Use robust optimization or stochastic models instead.

- **Cycles are acceptable and desirable (redundancy for fault tolerance).** MSTs have no cycles; if a single edge failure must not disconnect the graph, add edges to form a k-connected structure (requires k-edge-connected graph theory, not MST).

- **The graph is very large and weights are implicit or computed expensively.** MSTs require access to all edges and their weights. If the graph is implicit (e.g., a metric space with n^2 implicit edges) or weights are expensive to compute (e.g., shortest-path distances in a larger graph), specialized approximate or parametric methods may be needed.

## Output Format

```
## Minimum Spanning Tree: <application domain or graph name>

**Graph:** |V| = <nodes>, |E| = <edges>
**Objective:** <what does minimizing total weight achieve?>
**Weight domain:** <cost, distance, latency, etc.>

### MST result
| Edge | Weight | Nodes | Notes |
|---|---|---|---|
| e1 | w(e1) | (u1, v1) | <context> |
| ... | ... | ... | ... |

**Total MST weight:** W(T*) = <sum>
**Edges selected:** n − 1 = <count>
**Edges not selected:** m − (n − 1) = <count>

### Interpretation
- **Backbone structure:** <which connections are critical; what is the topology?>
- **Cost savings:** <what is the cost of MST vs. selecting all edges, or vs. other candidate trees?>
- **Failure points:** <which single edge removals would disconnect the tree; where is fragility?>

### Boundary-condition check
- Directed graph needed: <yes / no>
- Multi-objective: <yes / no; if yes, supplementary analysis needed>
- Dynamic updates expected: <yes / no; if yes, consider incremental algorithms>
- Redundancy/fault tolerance needed: <yes / no; if yes, MST is insufficient; use k-connectivity>

### Confidence: high | medium | low
<reasoning: weight accuracy and stability + graph connectedness + whether single-objective minimization is truly the goal + whether static snapshot is sufficient>
```
