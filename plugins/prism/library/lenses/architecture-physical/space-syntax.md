---
name: space-syntax
display_name: Space Syntax (Hillier)
class: lens
underlying_class: native
domain: architecture-physical
source: Bill Hillier, University College London; developed 1970s–present
best_for:
  - Diagnosing how spatial layout affects movement, visibility, and social interaction
  - Comparing building or urban designs without user studies
  - Identifying bottlenecks, dead zones, and integration patterns in layouts
one_liner: "Graph-analyze spatial configuration to diagnose circulation, visibility, and social interaction patterns."
---

# Space Syntax (Hillier)

## Overview

Space Syntax treats buildings and urban layouts as graphs where nodes are convex spaces (rooms, plazas, street segments) and edges represent direct adjacency or visibility. By measuring properties like integration (average depth from all other spaces), connectivity (number of neighbors), and control (how much a space constrains access elsewhere), practitioners diagnose how spatial configuration *shapes* occupant behavior without relying on observation or interviews. Architects and urban planners use it to predict congestion, isolation, wayfinding difficulty, and informal surveillance—all from the floor plan alone.

## Analytical Procedure

### Phase 1 — Represent the Layout as a Graph

1. **Obtain a floorplan or site map.** Digital format (CAD, PDF with clear geometry) is strongly preferred. Scale must be readable; ambiguous or hand-sketched drawings will produce unreliable results.

2. **Define the space units.** Choose one of two modes:
   - **Convex mapping:** Break the layout into the largest convex polygons such that any two points within a polygon are visible from each other. Each polygon is a node. This is labor-intensive but captures visibility and natural activity zones.
   - **Axial mapping:** Draw the longest sightlines through open space (down hallways, across plazas, etc.). Each line is a node. This is faster but less sensitive to enclosure and is primarily used for movement prediction.
   
   *Guidance:* For interior layouts (offices, hospitals, museums) use convex. For urban or circulation-heavy layouts (streets, campuses) use axial. Document which you chose; results are not comparable across modes.

3. **Connect nodes with edges.** Two nodes are adjacent (connected by an edge) if:
   - **Convex mode:** They share a boundary or portal (door, opening).
   - **Axial mode:** One sightline intersects another (at grade, not bridged).
   
   Do not skip edges; the completeness of the graph is critical.

4. **Create the adjacency matrix.** Rows and columns are nodes; cell [i,j] = 1 if nodes i and j are adjacent, 0 otherwise. Verify symmetry (if i→j then j→i).

### Phase 2 — Compute Spatial Measures

5. **For each node, calculate depth.** Depth is the minimum number of edges (steps) from that node to every other node. Create a depth vector for each node: depth_i = [d_i1, d_i2, ..., d_in]. (A node's depth to itself is 0.)

6. **Calculate integration.** Integration quantifies how close a space is to all others on average.
   - Sum the depths from node i to all other nodes: Σ d_ij
   - Divide by (n − 1) where n is the total number of nodes: mean_depth_i = Σ d_ij / (n − 1)
   - Integration_i = (n − 1) / Σ d_ij, scaled if desired. Higher integration = closer to everything else on average.
   
   *Interpretation:* Highly integrated spaces attract movement and encounter. Segregated spaces isolate occupants.

7. **Calculate connectivity.** Connectivity is the count of immediate neighbors.
   - Connectivity_i = number of nodes directly adjacent to node i.
   
   *Interpretation:* High connectivity = many access options; low connectivity = limited escape routes.

8. **Calculate control.** Control measures how much a space constrains neighbors' access elsewhere.
   - For each neighbor j of node i, count the total neighbors of j (including i).
   - Control_i = Σ (1 / connectivity_j) for all neighbors j of i.
   
   *Interpretation:* A space with high control is a necessary gateway. A space with low control is a choice, not a bottleneck.

9. **Optional: calculate choice.** Choice counts how many shortest paths between all pairs of nodes pass through a given node.
   - For every pair of nodes (a, b), find the shortest path(s).
   - Increment the count for every node on every shortest path.
   - Choice_i = count for node i.
   
   *Interpretation:* High choice = node lies on many desirable routes. Useful for predicting informal surveillance and secondary gathering spots.

### Phase 3 — Interpret Results

10. **Rank nodes by integration and identify clusters.** Create a sorted list of nodes by integration (highest to lowest). Visually highlight on the floorplan nodes in the top quartile (high integration), bottom quartile (segregated). Do they match your intuition about busy vs. quiet areas?

11. **Cross-reference integration with connectivity.** A node can be highly integrated despite low connectivity (few neighbors but positioned in a central location) or vice versa. Note mismatches:
    - High integration + low connectivity = bottleneck; small area controls major flow.
    - Low integration + high connectivity = cul-de-sac or enclosed cluster; many local options but globally isolated.

12. **Identify dead zones (segregated, low-choice nodes) and hubs (high integration, high choice nodes).** Dead zones invite isolation or underuse. Hubs attract unintended gathering. Mark these on a marked-up plan.

13. **Check for spatial syntax anomalies.** Look for:
    - **Spatial discontinuity:** A partition (wall, locked door) that abruptly severs a historically connected area, forcing long detours.
    - **Over-connection:** A space with unreasonably high connectivity relative to its integration, suggesting confused wayfinding.
    - **Isolated loops:** A subgraph that is internally connected but has only one entrance/exit, creating a trap.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Floor plan or site map is legible at the scale of analysis (convex or axial) | Y/N |
| Space units are exhaustive: every accessible area is represented | Y/N |
| Adjacency graph is complete and symmetric (no missing edges, no errors) | Y/N |
| Depth is calculated correctly for all nodes (spot-check 3 nodes) | Y/N |
| Integration formula is applied consistently (or normalized formula is stated) | Y/N |
| High-integration nodes are plausible as activity centers or circulation spines | Y/N |
| Dead-zone nodes are flagged and justified (not arbitrary designation) | Y/N |

## Red Flags

- The graph is incomplete: a hallway or link is missing, creating a disconnected subgraph. This invalidates all downstream measures.
- Integration ranking contradicts the design intent by a large margin (e.g., the main lobby ranks in the bottom 20% for integration). If this is true, it is a genuine finding; if the graph is incomplete, fix it first.
- All nodes have nearly identical integration values. This suggests either a highly egalitarian layout (rare, but possible) or an error in calculation or representation. Verify the graph diameter (longest shortest-path).
- Dead zones and hubs are identified but not traced back to spatial features. A dead zone should correspond to a visual feature (a corner, a dead end, enclosure) that explains the isolation.
- No distinction is made between mode (convex vs. axial). Results from different modes are being compared as if they are on the same scale.

## Output Format

```
## Space Syntax Assessment

**Layout analyzed:** <building/area name, location, date>

**Mode:** <convex | axial>

**Graph properties:**
- Nodes: _
- Edges: _
- Average connectivity: _
- Graph diameter (longest shortest path): _

### Integration Ranking
| Rank | Node ID / Name | Integration Score | Connectivity | Control |
|---|---|---|---|---|
| 1 | <...> | <...> | <...> | <...> |
| 2 | <...> | <...> | <...> | <...> |
| ... | ... | ... | ... | ... |
| n | <...> | <...> | <...> | <...> |

(Report top 10 and bottom 5.)

### Hubs and Dead Zones

**High-integration hubs (top quartile):**
- Node <X>: Integration <score>. Spatial character: <description—e.g., "main circulation spine, open plan">. Predicted use: <high foot traffic, gathering, surveillance>.

**Segregated zones (bottom quartile):**
- Node <Y>: Integration <score>. Spatial character: <description—e.g., "enclosed corner office, single entry">. Predicted use: <isolation, focused work, low throughput>.

### Anomalies and Critical Findings

1. <anomaly type>: <node or region>, <interpretation>. 
   Example: "Spatial discontinuity at the main stairwell: high connectivity (6 neighbors) but integration rank 23/47, suggesting the stair is a local hub but poorly positioned in overall layout. Users will bypass it if possible."

2. ...

### Design Implications

- <specific actionable insight, tied to a measure>
- <specific actionable insight, tied to a measure>

### Confidence
<high | medium | low> — <justification. For example: "high — graph is complete, measures are internally consistent, and hub/dead-zone rankings match architectural expectations." Or "low — layout contains bridges or multi-level transitions not fully represented; axial mode may not capture vertical circulation.">
```
