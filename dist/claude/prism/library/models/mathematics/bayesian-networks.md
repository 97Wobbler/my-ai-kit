---
name: bayesian-networks
display_name: Bayesian Networks
class: model
underlying_class: native
domain: mathematics
source: Judea Pearl, "Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference," Morgan Kaufmann, 1988
best_for:
  - Encoding conditional-independence structure in a domain via directed acyclic graphs (DAGs)
  - Deriving exact or approximate probability queries using graph-aware inference algorithms
  - Handling missing data and causal reasoning in systems with latent variables
one_liner: "Encode conditional independence as a directed acyclic graph for efficient inference."
---

# Bayesian Networks

## Overview

A Bayesian Network is a directed acyclic graph (DAG) in which each node represents a random variable and each directed edge encodes a direct probabilistic influence. The core claim is that **the joint probability distribution of all variables can be factored as a product of conditional probabilities, one per node, each conditioned only on that node's parents in the graph**. This structure enables two key capabilities: (1) it makes conditional-independence relationships explicit and exploitable, and (2) it grounds efficient inference algorithms that leverage sparsity in the graph rather than brute-force enumeration over the full joint. The model is both descriptive — revealing the independence structure of a domain — and computational, enabling prediction and diagnosis via message-passing and exact / approximate inference.

## Core Variables and Relationships

A Bayesian Network is defined by:

1. **Directed Acyclic Graph (DAG)** with nodes V = {X₁, X₂, ..., Xₙ} and directed edges E.
   - Each node Xᵢ is a random variable with a discrete or continuous domain.
   - An edge from Xⱼ to Xᵢ means Xⱼ is a parent of Xᵢ; written Pa(Xᵢ).
   - Acyclicity ensures a well-defined topological ordering and no circular dependencies.

2. **Conditional Probability Tables (CPTs)** or conditional density functions.
   - For each node Xᵢ, specify P(Xᵢ | Pa(Xᵢ)).
   - If Xᵢ has no parents, P(Xᵢ | Pa(Xᵢ)) = P(Xᵢ), the marginal distribution.

3. **Factorization identity** — the joint probability of all variables is:

       P(X₁, X₂, ..., Xₙ) = ∏ᵢ P(Xᵢ | Pa(Xᵢ))

   This factorization is equivalent to assuming that each variable is conditionally independent of its non-descendants given its parents (the Markov condition).

4. **Conditional independence** is read directly from the graph structure via d-separation.
   - Two nodes A and B are d-separated given a set Z of conditioning nodes if no active path exists between them when Z is observed.
   - d-separated variables are conditionally independent: A ⊥ B | Z.
   - This allows the model to identify which variables can be safely ignored in queries, reducing computation.

## Key Predictions

- **Efficient factorization.** A Bayesian Network over n variables with maximum parent set size k requires storage of O(n · 2^k) parameters instead of O(2^n) for the full joint distribution. Sparse graphs yield exponential savings.

- **Query answers scale with graph connectivity.** Posterior probabilities P(query | evidence) can be computed in time polynomial in n for networks with bounded treewidth. Dense networks (high connectivity) require exponential time in worst case, even with evidence.

- **Explaining away (Markov property consequence).** Observing a common effect (child node) creates dependence among its causes (parent nodes) that would otherwise be independent. Example: rain and sprinkler are independent; observing "wet grass" makes them dependent (one explains away the other).

- **Latent variables are recoverable via marginalization.** If the network includes unobserved variables, queries over observed variables are obtained by summing out the latent ones — the graph structure ensures the sum factorizes and avoids explicit enumeration.

- **Causal direction matters for inference asymmetry.** A network encoding X → Y supports efficient inference from X to Y (prediction); inference from Y to X (diagnosis) requires message-passing in the reverse direction and may be more expensive if the reverse direction has high fan-in.

- **Approximate inference with message-passing is often necessary.** For networks with high treewidth or many evidence nodes, exact inference becomes intractable; belief propagation (loopy BP), variational inference, or sampling approximate the true posterior, with guaranteed convergence only on tree-structured networks.

## Application Procedure

Instantiate the model against a specific domain and reasoning task.

1. **Define the domain and identify variables.** List all relevant random variables — both observable (evidence) and latent (unobserved). Write their domains (categorical, continuous, etc.). Example: disease diagnosis problem with disease D, symptoms S₁, S₂, test result T.

2. **Elicit the causal / dependency structure.** Draw the DAG by adding directed edges from each parent to its child. Edges should reflect direct probabilistic influence, not mediation through other variables. Verify acyclicity (no loops). If uncertain whether an edge exists, document it; this is often the hardest step.

3. **Populate conditional probability tables.** For each node, estimate or observe P(node | parents) from data, domain experts, or prior distributions. For discrete variables, this is a table; for continuous, a parametric family (e.g., Gaussian conditional on parents). If data are sparse for some CPTs, note that inference will be high-variance or require smoothing.

4. **Identify the query and evidence.** Write down:
   - Query nodes: variables you want to compute probabilities for (e.g., P(D | S₁=true, T=positive)).
   - Evidence nodes: variables that are observed (conditioned on).
   - Unobserved nodes: variables that will be marginalized out.

5. **Choose an inference algorithm.** 
   - For tree-structured networks or small networks: exact inference via variable elimination or belief propagation.
   - For general DAGs with low treewidth: exact variable elimination, exploiting the graph structure to avoid exponential blow-up.
   - For high-treewidth networks or real-time requirements: approximate methods (belief propagation, sampling, variational inference).

6. **Compute the posterior.** Execute the algorithm. Output is P(query | evidence) or a sample from it.

7. **Check boundary conditions** (below). If any apply, document assumptions and limitations of the result.

8. **Generate prediction and confidence.**
   - State the posterior probability for the query.
   - Explain which variables were critical (had high mutual information with the query) and which were negligible (d-separated).
   - Flag any CPT entries that were estimated from sparse data or expert guesses.

## Boundary Conditions

Bayesian Networks are powerful within their scope but break down or require extension under several conditions:

- **Cyclic or feedback structures.** The DAG assumption fails if the domain has true cycles or feedback loops (e.g., closed-loop control systems, temporal dynamics). Use dynamic Bayesian networks (DBNs) or state-space models instead.

- **Continuous variables with complex conditional distributions.** If conditional distributions are non-Gaussian or high-dimensional, exact inference becomes intractable and the CPT representation becomes unwieldy. Use graphical models with continuous relaxations or sampling-based methods.

- **Model misspecification.** If the true causal/dependency structure differs from the elicited graph, posterior probabilities can be severely biased. Sensitivity analysis and robustness checks become critical; consider structure learning from data if domain knowledge is weak.

- **Insufficient or biased observational data for CPT estimation.** Small-sample CPTs introduce high variance in posteriors. Missing data patterns can violate the missing-at-random assumption, biasing inference. Document data quality explicitly.

- **High-treewidth networks.** Networks with highly interconnected nodes (many paths between query and evidence) have exponential inference complexity. Approximation methods are necessary, but their accuracy is not guaranteed. Bound the treewidth or restructure the network if feasible.

- **Non-local dependencies.** If two distant nodes have a hidden confounding cause (a "backdoor" path via unobserved variables), standard inference will conflate correlation with causation. Causal inference using do-calculus or instrumental variables may be required instead.

## Output Format

```
## Bayesian Network Analysis: <domain / task>

**Domain:** <description of the system being modeled>
**Query:** P(<query variables> | <evidence variables>)
**Network structure:** <number of nodes, edges; key ancestors of query>

### Variables and domains
| Variable | Domain | Role | Notes |
|---|---|---|---|
| ... | ... | Query / Evidence / Latent | ... |

### DAG summary
<acyclic, max in-degree, max out-degree>
<textual or sketch description of key edges: what causes what>

### CPT data quality
<which CPTs are learned from data (sample size), which from expert elicitation, which smoothed / regularized>

### Inference method
<exact / approximate; algorithm name; computational complexity estimate>

### Posterior and interpretation
- **Predicted posterior:** P(query | evidence) = <result>
- **Marginal query:** P(query) = <if relevant>
- **High-impact variables:** <which nodes have high mutual information with query; which are d-separated>
- **Explaining-away or other dependencies:** <key patterns in the result>

### Model assumptions and limitations
<which boundary conditions apply; sensitivity to CPT errors; structural assumptions that may not hold>

### Confidence: high | medium | low
<reasoning: (1) CPT data quality and sample sizes, (2) network structure clarity (elicited vs. learned), (3) treewidth and inference tractability, (4) fit to boundary conditions>
```
