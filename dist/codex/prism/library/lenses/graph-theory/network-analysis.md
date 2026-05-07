---
name: network-analysis
display_name: Network Analysis (Algorithmic)
class: lens
underlying_class: native
domain: graph-theory
source: Freeman (1978, centrality measures); Newman (2003, community detection); Brin & Page (1998, PageRank); Louvain algorithm (Blondel et al., 2008)
best_for:
  - Identifying influential nodes and connectors in networks
  - Uncovering organizational, social, or technical clusters
  - Diagnosing bottlenecks, single points of failure, and structural vulnerabilities
one_liner: "Compute centrality measures (degree, betweenness, eigenvector, PageRank) and detect communities to map structural roles and influence patterns."
---

# Network Analysis (Algorithmic)

## Overview

Network analysis decomposes a graph into nodes and edges, then applies algorithmic metrics to expose structure hidden in the raw connectivity. Degree centrality reveals raw popularity; betweenness reveals gatekeepers; eigenvector reveals influence through association; PageRank reveals systemic importance under random walk dynamics. Community detection partitions nodes into clusters and identifies inter-cluster bridges. Practitioners use this on organizational charts, software dependency graphs, social networks, and infrastructure maps when they need to move past intuition and see who (or what) actually holds power, where communication breaks, and which parts of the system are tightly coupled or isolated.

## Analytical Procedure

### Phase 1 — Data Preparation and Graph Construction

1. **Acquire and represent the network as an edge list or adjacency matrix.**
   - Format: two-column table (source, target) for each edge, or an NxN matrix where rows/columns are nodes and cells contain edge weights (0 = no edge, 1+ = edge weight).
   - Validate: every node ID is resolvable, every edge has a source and target, no self-loops unless the domain explicitly permits them (e.g., feedback systems).
   - Document: is the graph directed (A→B ≠ B→A) or undirected? Weighted or unweighted? Static or time-varying?
   - Size check: node count (N) and edge count (E). If E > N(N−1)/2, verify the data is not corrupted (dense graphs require different algorithms than sparse ones).

2. **Remove or flag missing and degenerate cases.**
   - Isolated nodes (degree = 0): decide whether to keep (meaningful absence) or drop (noise).
   - Multi-edges (duplicate A→B): collapse into single weighted edge or mark as multi-edge and weight by count.
   - Timestamps (if present): decide on time-window aggregation if the graph is temporal.

3. **Choose metric scope: global (whole graph) or local (node neighborhoods, subgraphs).**
   - Global: when the question is "what is the overall structure?"
   - Local: when the question is "what is this node's role?" or "is this subgraph an anomaly?"

### Phase 2 — Compute Centrality Measures

For each node, compute four centrality measures:

4. **Degree centrality.**
   - Definition: count of edges attached to the node (in-degree + out-degree for directed graphs).
   - Interpretation: raw popularity or activity. A node with high degree is a hub.
   - Calculation: for node i, degree = count of neighbors.
   - Red flag: if all nodes have nearly identical degree, the metric adds little value; the graph is homogeneous.

5. **Betweenness centrality.**
   - Definition: fraction of shortest paths between all node pairs that pass through this node.
   - Interpretation: gatekeeper or broker role. A node with high betweenness controls information flow; removing it fragments the graph.
   - Calculation: for node i, count shortest paths from s to t for all pairs (s, t). Sum paths that include i. Normalize by total paths. (Computationally expensive for large graphs; use sampling or approximation algorithms for N > 5000.)
   - Red flag: betweenness is high for nodes that are merely at the geographic center of the graph, even if they have low degree. Always cross-check with degree and eigenvector.

6. **Eigenvector centrality.**
   - Definition: importance of a node measured as the weighted sum of its neighbors' importances (solved via dominant eigenvector of adjacency matrix).
   - Interpretation: influence through association. A node connected to important nodes is itself important. Captures systemic importance.
   - Calculation: compute the dominant eigenvector of the adjacency matrix A; the i-th entry is node i's eigenvector centrality.
   - Red flag: eigenvector centrality may not exist for disconnected graphs; apply to largest connected component. If one node dominates (e.g., centrality >> others), verify the graph is not artificially centralized around a root.

7. **PageRank.**
   - Definition: importance under a random walk that occasionally teleports to random nodes (stationary probability in a stochastic walk).
   - Interpretation: systemic importance accounting for incoming link quality and diversity. Models user behavior on hyperlinked systems.
   - Calculation: iterate until convergence: PR(i) = (1−d)/N + d × Σ[PR(j)/out-degree(j)] for all j linking to i, where d ≈ 0.85 (damping factor).
   - Red flag: PageRank is biased toward nodes with high in-degree in directed graphs; verify that the interpretation aligns with "importance via incoming reputation," not just popularity.

8. **Comparison matrix: For each node, fill a table with all four centrality scores, ranked by each metric.**
   - Nodes that rank high on multiple metrics are robustly central.
   - Nodes that are high in one metric but low in others have specialized roles (e.g., high betweenness, low degree = rare bridge).

### Phase 3 — Community Detection

9. **Apply a community detection algorithm** (choose based on graph size and structure):
   - **Louvain algorithm** (Blondel et al., 2008): fast, good for large undirected graphs. Optimizes modularity.
   - **Girvan-Newman**: slower, good for small graphs; removes high-betweenness edges iteratively.
   - **Label propagation**: fast, approximate, good for very large sparse graphs.
   - For directed graphs, adapt the algorithm or convert to undirected by treating edges symmetrically.

10. **Run the algorithm and extract partition:** nodes are assigned to communities (disjoint clusters, or overlapping if the algorithm permits).

11. **Compute modularity score:** a measure of partition quality (range: −0.5 to 1.0; >0.3 indicates significant community structure).
    - Formula: Q = (1/2m) × Σ[e_ij − (k_i × k_j) / 2m] where e_ij is edges within community, k_i is degree of i, m is total edges.
    - Interpretation: higher modularity means tighter within-community connections and sparser between-community edges.

12. **For each community, identify:**
    - Size (node count) and density (edges within the community / possible edges).
    - Hubs within the community (high degree nodes).
    - Bridge nodes (inter-community edges): which nodes connect communities? What is their betweenness rank?

### Phase 4 — Interpretation and Diagnosis

13. **Map structure to domain context.**
    - Does community structure align with known organizational, technical, or social divisions (departments, microservices, friend groups)?
    - Are bridges expected or anomalous?
    - Do hub nodes match intuitive power players or are there surprises?

14. **Identify vulnerabilities.**
    - Single-point-of-failure nodes: high betweenness, low redundant paths. (Remove this node and does the graph fragment?)
    - Isolated clusters: communities with no inter-cluster edges (potential communication breakdown).
    - Bottleneck edges: edges with high betweenness relative to degree (high communication load on a thin link).

15. **Generate diagnostic questions:**
    - Why are these communities separated? (By design, accidental, or organizational boundary?)
    - Are the high-degree nodes responsible for their degree (producers) or victims (consumers)?
    - Do community bridges exist where they are needed (e.g., between critical departments) or are critical bridges absent?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Network is represented as edge list or adjacency matrix with node IDs and (optionally) edge weights | Y/N |
| Graph properties documented: directed/undirected, weighted/unweighted, size (N and E) | Y/N |
| All four centrality measures computed for all nodes (or largest component if disconnected) | Y/N |
| Centrality scores ranked and compared; at least 3 nodes identified as high on multiple metrics | Y/N |
| Community detection algorithm applied and modularity score reported | Y/N |
| Communities annotated with size, density, internal hubs, and bridge nodes | Y/N |
| Interpretation cross-checked against domain context (not just numbers) | Y/N |
| At least two structural vulnerabilities or anomalies identified and explained | Y/N |

## Red Flags

- All nodes have nearly identical centrality scores across all four metrics. Either the graph is noise (random connections) or so densely connected that structure is meaningless.
- Modularity score is <0.1 (or negative). The detected "communities" are statistical artifacts, not real clusters. Either the graph is random, or the algorithm is not suited to this graph's structure (e.g., applying undirected community detection to a directed graph).
- High-degree hub nodes are completely absent from the bridge-node list. This suggests the communities are entirely disconnected from each other, not merely loosely connected — check whether the analysis was run on one component only.
- Centrality interpretation contradicts domain knowledge without explanation. "The CEO has low betweenness because they don't directly control information flow" is plausible; "the CEO is irrelevant" is a red flag that metric is misinterpreted.
- Community assignment is based purely on graph structure without validating that the communities are meaningful in the domain. (A community detection algorithm will partition any graph; that doesn't mean the partition is useful.)
- No acknowledgment of algorithm limitations (e.g., "Louvain sometimes merges weakly separated communities"; "betweenness is expensive for N > 5000 without approximation").

## Output Format

```
## Network Analysis Report

**Graph Summary**
- Nodes (N): <count>
- Edges (E): <count>
- Directed/Undirected: <yes/no>
- Weighted/Unweighted: <yes/no>
- Connected components: <count>
- Analysis scope: <global | largest component | subgraph <name>>

### Centrality Rankings

| Node ID | Degree | Degree Rank | Betweenness | Betweenness Rank | Eigenvector | Eigenvector Rank | PageRank | PageRank Rank |
|---|---|---|---|---|---|---|---|---|
| <node> | <score> | <rank> | <score> | <rank> | <score> | <rank> | <score> | <rank> |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Top Hubs (high degree):** <list 3-5 nodes with interpretation>
**Top Gatekeepers (high betweenness):** <list 3-5 nodes with interpretation>
**Top Influential (high eigenvector):** <list 3-5 nodes with interpretation>
**Top Systemic Importance (high PageRank):** <list 3-5 nodes with interpretation>

**Robustly Central (high on 3+ metrics):** <list nodes; these are core to the network>
**Specialized Roles (high on 1-2 metrics):** <describe e.g., "low-degree bridges," "isolated hubs">

### Community Structure

**Modularity Score:** <score> (interpretation: <well-structured | weak structure | no significant communities>)

| Community ID | Size | Density | Internal Hub(s) | Bridge Nodes (to other communities) | Interpretation |
|---|---|---|---|---|---|
| <id> | <count> | <fraction> | <node, node> | <node→community, node→community> | <domain meaning> |
| ... | ... | ... | ... | ... | ... |

**Inter-Community Connectivity:** <list critical bridges, bottleneck edges>

### Vulnerabilities and Anomalies

1. **Single Points of Failure:** <node names with high betweenness and what breaks if removed>
2. **Isolated Clusters:** <communities with sparse inter-cluster edges>
3. **Bottleneck Edges:** <edges with high betweenness relative to degree; communication choke points>
4. **Unexpected Hubs or Absence:** <surprises when compared to domain expectations>

### Cross-Check Against Domain Context

<Reconcile structural findings with what is known about the domain. Note disagreements and hypothesize explanations. E.g., "CEO has low betweenness because chain of command is weak in practice; real power flows through technical leads (high betweenness).">

### Confidence
<high/medium/low> — <justification covering: data quality, algorithm applicability, alignment with domain reality, and whether structure is robust or artifact-prone>
```
---
