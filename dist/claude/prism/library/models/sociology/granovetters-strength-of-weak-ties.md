---
name: granovetters-strength-of-weak-ties
display_name: Granovetter's Strength of Weak Ties
class: model
underlying_class: native
domain: sociology
source: Mark S. Granovetter, "The Strength of Weak Ties," American Journal of Sociology, 1973
best_for:
  - Predicting information flow and access across social networks
  - Explaining job search success and career mobility
  - Understanding how novel information reaches individuals
one_liner: "Weak ties transmit novel information more efficiently than strong ties."
---

# Granovetter's Strength of Weak Ties

## Overview

Granovetter's Strength of Weak Ties model claims that **weak ties — infrequent, emotionally thin connections — are the primary conduits for novel information and opportunity in social networks**. The model inverts intuition: people assume close friends (strong ties) matter most for outcomes like employment, yet the empirical pattern shows that weak ties (acquaintances, former classmates, distant colleagues) are far more valuable for accessing non-redundant information and bridging between social clusters. The model is descriptive and predictive. It explains why networks with high density among close ties but sparse bridges to distant clusters produce information poverty despite apparent connectedness, and it predicts who will receive novel opportunities and information first. Applying it requires the procedure below.

## Core Variables and Relationships

The model operates on two structural properties of networks and one information property:

1. **Tie strength** (dyadic property) — driven by:
   - Frequency of interaction (more → stronger)
   - Emotional intensity (high affect → stronger)
   - Intimacy / mutual confiding (higher → stronger)
   - Reciprocity of support (more reciprocal → stronger)
   
   **Direction of effect:** Stronger ties → more frequent contact → more redundant information shared → less novel information per contact.

2. **Network clustering / density** — characteristics of the local neighborhood:
   - Proportion of a focal person's alters who are also connected to each other (transitivity)
   - Tendency of strong ties to form cliques or tightly interconnected subgroups
   - Sparse bridges between clusters (structural holes)
   
   **Direction of effect:** High clustering within strong-tie groups + sparse bridges → information stagnation within clusters, slow diffusion between them.

3. **Information novelty and non-redundancy** — the content property:
   - Is the information already known to the focal person?
   - Is the information known to everyone the focal person already talks to?
   - Does the information come from a distant part of the network the focal person does not have access to?
   
   **Direction of effect:** Weak ties are more likely to span structural holes and connect to distant clusters → weak ties carry non-redundant information → weak ties are more valuable for outcomes that depend on novel information (jobs, ideas, opportunities).

The central identity is **non-redundancy**: the probability that an alters provides novel information is inversely related to the number of other alters that person already knows. Weak ties, by definition, are less likely to be embedded in the same cluster, so they are less likely to be redundant.

## Key Predictions

- **Job-search success correlates more strongly with weak ties than strong ties.** Empirically, people find jobs through acquaintances and distant contacts more often than through close friends. This is not because friends are unhelpful, but because close friends move in the same information network; acquaintances have access to different channels.

- **High-clustering networks (where strong ties are densely connected) suffer slower information diffusion despite apparently good connectivity.** A person may have high local density (many friends who know each other) but be isolated from novel information sources — an apparent paradox until clustering is visible.

- **Brokers — people with weak ties spanning structural holes — have disproportionate access to non-redundant information and opportunity.** They are the first to hear about new jobs, innovations, rumors, and can arbitrage information asymmetries.

- **Removing a weak tie from the network has larger effects on network diameter and information reachability than removing a strong tie of similar frequency.** Weak ties are the bridges; strong ties within clusters are redundant.

- **In-group homogeneity reduces inter-group information flow even when weak ties are present, if those weak ties are few.** A single weak tie to another cluster is better than none, but a single bridge can be a bottleneck.

- **Strong ties are locally efficient (high support, coordination, trust) but globally inefficient (information stagnation).** A person with many strong ties but few weak ties will be well-supported but poorly informed.

## Application Procedure

Instantiate the model against a concrete individual, organization, or information-diffusion process.

1. **Define the person / node and the information-search or opportunity outcome in question.** Who is the focal actor? What are they trying to find or learn? (e.g., "Alice looking for a new job," "An R&D team seeking novel technical approaches").

2. **Map the focal person's network — ties, tie strength, and clustering.**
   - Enumerate frequent contacts (strong ties) and occasional contacts (weak ties).
   - For each tie, assign strength using the criteria above: frequency, emotional intensity, intimacy, reciprocity. Use a 3-level scale (Strong / Medium / Weak) or a rough ordering.
   - For each strong tie, note which other ties it is connected to. Compute local clustering: what fraction of the person's alters are also connected to each other?
   - Identify structural holes: clusters of densely connected people with few bridges between clusters. Mark which weak ties (if any) span those holes.

3. **Assess the redundancy of information flowing through each tie.**
   - For strong ties: what information do they have? Is it information the focal person already has access to through others?
   - For weak ties: do they connect to clusters or people the focal person does not otherwise reach? If so, the tie is non-redundant.
   - Estimate the proportion of weak ties that span structural holes vs. weak ties that are still within the focal person's local cluster.

4. **Predict information access and opportunity arrival.**
   - If the person has few weak ties and high local clustering, predict slow access to novel information and delayed opportunity arrival.
   - If the person has several weak ties spanning different clusters, predict faster access to non-redundant information and earlier opportunity detection.
   - If the person is a broker (weak ties to multiple clusters), predict information advantage and early access.

5. **Check boundary conditions** (below). If any apply, note how the prediction may be incomplete.

6. **Generate the prediction.**
   - Will the person find the job / idea / opportunity through strong ties or weak ties? When?
   - What is the speed of information diffusion through their network to other people?
   - What advice follows: should the person maintain or cultivate more weak ties? Which weak ties are most valuable because they span the largest holes?

## Boundary Conditions

Granovetter's model assumes a classical social network (dyadic, local, stable). It becomes partial or misleading under:

- **Digitally mediated networks with low interaction cost.** Online platforms reduce the frequency and emotional cost of weak-tie maintenance. A person can have thousands of weak ties at low cost. The redundancy heuristic breaks down if the "frequency" is now a weak signal of cluster membership. Supplement with an information-diffusion / cascade model.

- **Homophily and assortativity.** The model assumes structural holes are real gaps in the network. But if people select into tight-knit groups with others like themselves, weak ties may still be to similar people. Weak ties may not span the hole you thought. Audit tie content, not just structure.

- **Organizations with strong gatekeeping or hierarchy.** In a firm where a manager controls information flow, the model's prediction about who learns first is masked by formal channels. The weak-tie signal may be overwhelmed by rank.

- **Ambiguous or polarized information.** The model treats information as a signal to be transmitted. But in contexts where information is contested (political, ideological, scientific during paradigm shifts), weak ties may transmit different *versions* or *interpretations* of information, not just novel facts. Requires adding a content / credibility layer.

- **Network intervention or artificial tie creation.** If weak ties are created by policy (e.g., a program that pairs people across silos), the natural redundancy assumptions break. An artificially created weak tie may not actually reduce redundancy if the intervention does not change the underlying cluster structure.

- **Time and tie dynamics.** The model is static — it assumes tie strength and clustering are stable. In reality, weak ties decay (people lose touch), strong ties weaken (relationships cool), and new clusters emerge. Over long time horizons, the network structure that determined information flow shifts unpredictably.

## Output Format

```
## Network Analysis: <focal person/organization and outcome>

**Focal actor:** <name, role, context>
**Outcome of interest:** <job search, innovation adoption, rumor spread, etc.>
**Network boundary:** <whose connections count as "in the network"; what time period>

### Tie inventory
| Tie | Strength | Frequency | Emotional intensity | Cluster membership | Spans hole? |
|---|---|---|---|---|---|
| <Name> | S/M/W | ... | ... | <Cluster A / B / Bridge> | Y/N |
| ... | ... | ... | ... | ... | ... |

### Clustering analysis
- Local clustering coefficient: <high / medium / low with supporting observation>
- Structural holes identified: <list clusters and which weak ties bridge them>
- Redundancy concentration: <which strong ties are most redundant; which weak ties are most non-redundant>

### Information flow prediction
- Primary channel for novel information: <strong ties / weak ties / specific tie name>
- Predicted speed of access: <early / moderate / late in the diffusion process>
- Bottleneck or advantage: <specific weak tie that is critical, or absence of a bridge>

### Boundary-condition notes
<which boundary conditions apply; what network changes would alter the prediction>

### Confidence: high | medium | low
<reasoning: clarity of tie-strength data, stability of network structure, presence of confounding gatekeepers or digital platforms, homophily risk>
```
