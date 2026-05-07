---
name: social-network-analysis
display_name: Social Network Analysis
class: lens
underlying_class: native
domain: sociology
source: Wasserman & Faust (1994); Granovetter (1973); Burt (1992)
best_for:
  - Mapping influence, information flow, and structural advantage in groups
  - Identifying connectors, brokers, and isolated actors
  - Finding hidden dependencies and bottlenecks in organizations
one_liner: "Analyze influence and opportunity of individuals and groups through centrality, ties, and structural holes."
---

# Social Network Analysis

## Overview
Social Network Analysis (SNA) maps relationships between actors (people, organizations, ideas) and measures their position within the structure to identify influence, access, and structural advantage. Rather than analyzing actors in isolation, it treats the network itself as the unit of analysis — who connects to whom, who bridges otherwise separate groups, and who sits in structural holes (gaps between clusters). Practitioners use this lens when trying to understand how information or resources actually flow, who holds disproportionate power, or where organizational bottlenecks hide.

## Analytical Procedure

### Phase 1 — Define the Network and Collect Data

1. **State the network question in one sentence.** What relationship are you mapping? Examples: "Who talks to whom about decisions?" or "Which companies have strategic alliances?" Be specific about the tie type (advice, trust, collaboration, financial, etc.).

2. **Define the actor set.** List all entities that should be included. For an organization: all roles involved in a specific process? All employees above a threshold? All companies in an industry? Justify the boundary. Exclude nobody arbitrarily; include nobody just because they exist.

3. **Collect tie data.** For each pair of actors, record whether the relationship exists. Methods:
   - Interviews: "Who do you go to for advice on X?"
   - Surveys: Roster method (provide full list, mark connections) or free-recall (list people without prompting).
   - Transactions: Extract from email, meeting logs, or collaboration platforms.
   - Documents: Co-authorship, co-mentions, cited together.
   Record the direction of ties if relevant (A→B is different from B→A).

4. **Build the adjacency matrix.** Rows and columns are actors. Entry (i,j) is 1 if a tie exists, 0 otherwise. For weighted networks (strength varies), use the weight value instead of 1.

### Phase 2 — Calculate Centrality Measures

5. **Degree centrality.** For each actor, count the number of direct connections.
   - Formula: degree(i) = sum of ties to/from actor i
   - Interpretation: Raw connectivity. High degree = many direct contacts. Does NOT tell you influence.

6. **Betweenness centrality.** For each actor, measure how often they lie on the shortest path between other actors.
   - Formula: Proportion of shortest paths between all actor pairs that pass through this actor
   - Interpretation: A broker or gatekeeper. High betweenness = control over information flow. This person is hard to bypass.

7. **Closeness centrality.** For each actor, measure average distance to all other actors.
   - Formula: 1 / (average shortest-path distance to all others)
   - Interpretation: How quickly this person can reach others. High closeness = central in the network's geography. Useful for understanding who hears news fastest.

8. **Eigenvector centrality.** For each actor, measure connectivity to well-connected others.
   - Formula: Eigenvector of the adjacency matrix corresponding to the largest eigenvalue
   - Interpretation: Not just having many ties, but having ties to influential people. High eigenvector centrality = connected to hubs.

### Phase 3 — Identify Structural Patterns

9. **Detect clusters or communities.** Use modularity-based algorithms (Louvain, Girvan-Newman) or k-means on network position to find subgroups with dense internal ties and sparse external ties.
   - Record the cluster membership of each actor.
   - Count inter-cluster bridges (ties between groups).

10. **Map structural holes.** Identify pairs of clusters with few or no ties between them.
    - Identify actors who bridge these holes (high betweenness between the two clusters).
    - These bridge actors have disproportionate influence — they control the flow between otherwise isolated subgroups.

11. **Check for reciprocity and hierarchy.** If ties are directed:
    - Reciprocity: What proportion of ties are mutual (A→B and B→A)?
    - Hierarchy: Are there clear "levels" (A→B→C but not C→A)? Plot rank order.

### Phase 4 — Contextualize and Validate

12. **Cross-check centrality measures.** A person high in degree but low in betweenness is well-connected but not a bottleneck. A person high in betweenness but low in degree is a rare, critical link. These mismatches often reveal strategy (A shields B from the network; C is a linchpin). Record the mismatch and the likely reason.

13. **Test structural assumptions.** Ask: Do the identified brokers actually control information? Are the clusters real or artifacts of how you defined ties? Validate by:
    - Interviewing high-betweenness actors about their role.
    - Testing whether information correlates with network distance (does it spread faster through clusters than across?).
    - Checking whether removing a high-betweenness actor actually disrupts flow (simulation or historical record).

14. **Document data quality.** Record:
    - Response rate (what % of actors answered?).
    - Missing ties (are there relationships you couldn't capture?).
    - Recall bias (are people remembering all contacts?).
    - Tie definition drift (does "advice" mean different things to different people?).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Network question is specific (tie type and purpose clear) | Y/N |
| Actor set has justified boundaries; nobody arbitrary | Y/N |
| Tie data collected via consistent method; source documented | Y/N |
| All four centrality measures calculated | Y/N |
| Clusters detected and inter-cluster ties mapped | Y/N |
| At least one structural hole and its broker identified | Y/N |
| Centrality mismatches interrogated (degree vs. betweenness, etc.) | Y/N |
| Data quality assessment completed; limitations documented | Y/N |

## Red Flags

- Degree and betweenness centrality are nearly identical for all actors. Either the network is a random graph (unlikely) or measurement is too coarse. Use weighted ties or directed ties to add texture.
- Clusters are trivial (just the team/department divisions you already knew). The network is not revealing structure — either the tie type is wrong or the network is too stratified to have emergent structure.
- A high-betweenness actor cannot explain why they are in the middle. They don't see themselves as a broker. Either the centrality measure is wrong for this network or their role is different (e.g., they're not *intentionally* brokering, just happen to be between groups).
- No reciprocity analysis for a network you assumed was mutual (e.g., "friendship"). If you didn't explicitly check, you don't know if ties are actually symmetric or if you've incorrectly averaged directed relationships.
- Data quality score is not documented. If you don't know how many ties you missed, your structure map is suspect.
- The network is too complete (density > 0.5 in a large network). You're not seeing structure, just noise. Redraw with tie strength, or redefine ties to be more selective.

## Output Format

```
## Social Network Analysis Report

**Network question:**
<tie type and purpose — one sentence>

**Actor set:**
- Count: _
- Boundary justification: <...>
- Data source: <interviews | surveys | transactions | documents>
- Response/completeness rate: _%

### Centrality Summary
| Actor | Degree | Betweenness | Closeness | Eigenvector | Role |
|---|---|---|---|---|---|
| <name> | <#> | <rank/score> | <rank/score> | <rank/score> | <gatekeeper/hub/peripheral/...> |

**Key findings:**
- Highest degree: <actor> (<#> ties)
- Highest betweenness: <actor> (bridges clusters: <list>)
- Highest closeness: <actor> (reaches all in avg _ steps)
- Eigenvector outlier: <actor> (connected to powerful nodes)

### Structural Patterns
**Clusters identified:** <#>
| Cluster | Size | Internal density | External ties | Key actors |
|---|---|---|---|---|
| <label> | <#> | <density 0-1> | <#> | <high-degree members> |

**Structural holes:**
- Between <cluster A> and <cluster B>: _ ties
- Bridge actor(s): <name(s)> (betweenness <score>)
- Strategic value: <information control / resource gatekeeping / knowledge brokerage>

**Reciprocity & hierarchy:**
- Reciprocal ties: _%
- Hierarchy signal: <strong/moderate/weak> — <evidence>

### Validation
- High-betweenness actors confirmed as brokers? <Y/N, notes>
- Clusters validated by domain knowledge? <Y/N, notes>
- Data quality score: _ / 10
  - Response rate: _%
  - Missing tie estimates: _%
  - Recall bias risk: <low/medium/high>
  - Tie definition consistency: <high/medium/low>

### Critical Mismatches
| Actor | Degree | Betweenness | Mismatch interpretation |
|---|---|---|---|
| <name> | High | Low | <well-connected but not a bottleneck> |

### Confidence
<high | medium | low> — <Justification. E.g., "High: Betweenness validated in interviews; clusters stable across three detection methods; data quality >85%. Low: Single tie definition used; network only 60% response rate; missing corporate contact data.">
```
