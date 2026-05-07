---
name: bayesian-reasoning
display_name: Bayesian Reasoning
class: model
underlying_class: native
domain: information-analysis
source: Thomas Bayes, "An Essay towards solving a Problem in the Doctrine of Chances," 1763; formalized in frequentist and subjective frameworks by R.A. Fisher, Bruno de Finetti, and others through the 20th century
best_for:
  - Updating beliefs under uncertainty when new evidence arrives
  - Comparing competing hypotheses by weighting prior plausibility against likelihood of observed data
  - Detecting when new data is uninformative or when a prior is sufficiently strong that evidence cannot budge it
one_liner: "Prior × likelihood → posterior; how evidence updates belief."
---

# Bayesian Reasoning

## Overview

Bayesian Reasoning is a formal framework for updating beliefs when new
evidence arrives. Its central claim is that all rational belief revision
obeys a single equation: the posterior probability of a hypothesis given
observed data is proportional to the product of the prior probability and
the likelihood of the data under that hypothesis. The model is **normative
and descriptive**: it prescribes how rational agents *should* update
beliefs, and empirically it explains many real-world judgments when
people have access to relevant data and are not under cognitive pressure.
Unlike frequentist hypothesis testing, Bayesian reasoning treats the
hypothesis itself as a random variable with a probability distribution,
not as a fixed unknown to be tested against. This permits direct statements
like "the probability this patient has disease D given these symptoms is
75%" — which classical statistics cannot produce. The model is explanatory
and predictive: apply it to a concrete inference problem to see which
hypotheses should gain or lose credence.

## Core Variables and Relationships

Bayesian reasoning uses four core elements:

1. **Prior probability P(H)** — the agent's belief in hypothesis H before
   seeing the new data.
   - Reflects domain knowledge, historical base rates, or symmetry
     (uniform prior when no information exists).
   - Must be positive (P(H) > 0) for the hypothesis to be updated at all
     by evidence; if P(H) = 0, no amount of evidence will change it.
   - Drives the result strongly when data are sparse or ambiguous.

2. **Likelihood P(D|H)** — the probability of observing the data D if
   hypothesis H were true.
   - Depends *only* on how well H predicts D, not on how probable H is.
   - Higher likelihood means the data are more consistent with H.
   - Multiple hypotheses are compared by taking their likelihood ratio:
     P(D|H₁) / P(D|H₂).

3. **Marginal likelihood (evidence) P(D)** — the total probability of
   observing D across *all* hypotheses, weighted by their priors.
   - P(D) = Σ P(D|Hᵢ) · P(Hᵢ) over all hypotheses.
   - Acts as a normalizing constant so the posterior probabilities sum
     to 1.
   - In practice, often computed implicitly rather than explicitly.

4. **Posterior probability P(H|D)** — the agent's updated belief in H
   after observing D.
   - The central output: what should I believe now?
   - Formula (Bayes' rule):

     **P(H|D) = P(D|H) · P(H) / P(D)**

   - Equivalently, posterior odds equal prior odds times likelihood ratio:

     **P(H₁|D) / P(H₂|D) = [P(H₁) / P(H₂)] × [P(D|H₁) / P(D|H₂)]**

The posterior of one observation becomes the prior for the next. As data
accumulates, the prior's influence fades if the data are informative.

## Key Predictions

- **Bayes' rule predicts belief revision direction and magnitude.** When
  D is more likely under H₁ than H₂, the likelihood ratio pushes the
  posterior toward H₁. The magnitude of the shift depends on both the
  likelihood ratio *and* how confident the agent was beforehand.

- **A strong prior resists weak evidence.** If P(H) is very low (e.g.,
  0.1%) and the likelihood ratio is modest (10:1), the posterior remains
  low. Extraordinary claims do require extraordinary (high-likelihood)
  evidence.

- **Uninformative data (likelihood ratio ≈ 1:1) leave beliefs unchanged.**
  If an observation is equally likely under all hypotheses, no update
  occurs; the posterior equals the prior.

- **With sufficient informative data, the prior is eventually overwhelmed.**
  Two agents with different priors but the same data converge toward the
  same posterior, provided the true hypothesis has high likelihood and the
  false ones have low likelihood.

- **The model predicts failure modes of human reasoning.** People often
  ignore base rates (the prior), anchor on vivid data, or treat
  likelihoods as if they were posteriors. Bayes predicts when these
  heuristics will lead to systematic error (e.g., the false-positive
  problem in medical testing).

- **Rare hypotheses require rare evidence to become plausible.** A
  hypothesis with prior 0.001 needs to have likelihood at least 1000× a
  competing hypothesis to tie in the posterior. This quantifies the
  intuition of "extraordinary claims."

## Application Procedure

Instantiate Bayesian reasoning against a concrete inference problem where
you must weigh evidence to update a belief.

1. **Define the hypothesis set crisply.** What are the competing
   explanations? State each as a testable claim. Include a catch-all
   hypothesis (e.g., "none of the above") if appropriate. The set must
   be exhaustive (one is true) and mutually exclusive.

2. **Assign prior probabilities to each hypothesis.** 
   - Draw on base-rate data, domain knowledge, or symmetry.
   - If prior information is absent, use a uniform prior (all hypotheses
     equally likely) explicitly.
   - Ensure the priors sum to 1. Document your reasoning.

3. **Identify the observed data D.** State it precisely: what was
   observed, under what conditions, with what measurement fidelity?

4. **Estimate the likelihood P(D|H) for each hypothesis.**
   - For each H, ask: "How likely is this data if H is true?"
   - Use data models, causal reasoning, or domain expertise.
   - If available, cite base rates or experimental evidence.
   - Likelihoods do *not* need to sum to 1.

5. **Compute the likelihood ratio(s).**
   - For two hypotheses: P(D|H₁) / P(D|H₂).
   - This isolates how much the data favor one over the other.

6. **Apply Bayes' rule to compute the posterior.**
   - Use the formula above, or reason through the relative odds.
   - Qualitative reasoning is sufficient: does the evidence push you
     toward H₁ or H₂, and by how much?

7. **Iterate if new data arrive.** The posterior becomes the prior for
   the next update.

8. **Check boundary conditions** (below). If any apply, flag where the
   model may not capture the full picture.

## Boundary Conditions

Bayesian reasoning is a normative ideal for belief updating under well-defined
uncertainty. It breaks down or becomes misleading under:

- **Unknown or disputed prior.** If experts disagree on the base rate (e.g.,
  "what fraction of startup founders are successful?"), the posterior will
  depend heavily on which prior you choose, and two agents may arrive at
  opposite conclusions from the same data. Bayes is robust to the prior
  only when data are abundant and informative.

- **Ambiguous or model-dependent likelihood.** If how you model P(D|H)
  itself depends on unstated assumptions (e.g., what causal mechanism
  produces D), two analysts may compute different likelihoods and again
  diverge. Bayes formalizes reasoning but does not resolve disagreement
  about the generative model.

- **Data that are not independent.** Bayesian updating treats each new
  observation as independent given H. If data points are correlated
  (e.g., clustered in time or space), the effective sample size is
  smaller, and the prior persists longer than the formula naively
  suggests. This requires careful likelihood modeling.

- **Post-hoc hypothesis formation ("p-hacking").** If hypotheses are
  invented after observing the data to fit what was found, Bayes applies
  to the true hypothesis set (including the new hypothesis), but the prior
  on the invented hypothesis should reflect that it was chosen because the
  data fit — a strong downward adjustment that is hard to quantify.

- **Continuous or very high-dimensional hypothesis spaces.** Bayes' rule
  still applies, but computing P(D) requires integration and becomes
  intractable without approximations (MCMC, variational inference). The
  formula is correct but operationally difficult.

- **Misspecified model.** If the true data-generating process is not
  captured by any of the hypotheses, Bayesian updating will favor the
  best-fit hypothesis, but the posterior may be overconfident and the true
  process may remain unseen.

## Output Format

```
## Bayesian Reasoning Analysis: <inference problem>

**Hypothesis set:**
- H₁: <statement>
- H₂: <statement>
- [H₃, etc. as needed]

**Prior probabilities:**
| Hypothesis | P(H) | Justification |
|---|---|---|
| H₁ | ... | <base rate, domain knowledge, or uniform> |
| H₂ | ... | ... |

**Observed data D:** <precise description of what was observed>

**Likelihoods:**
| Hypothesis | P(D\|H) | Reasoning |
|---|---|---|
| H₁ | ... | <how likely is D if H₁ is true?> |
| H₂ | ... | ... |

**Likelihood ratio(s):**
- P(D\|H₁) / P(D\|H₂) = <ratio> (H₁ is <ratio>× more likely to produce this data)

**Posterior probabilities:**
| Hypothesis | P(H\|D) | Change from prior |
|---|---|---|
| H₁ | ... | <direction and magnitude> |
| H₂ | ... | ... |

**Interpretation:**
- Which hypothesis now has the highest posterior probability?
- Did the data shift your belief materially, or did the prior dominate?
- What additional evidence would materially change the posterior?

**Boundary-condition notes:**
<which boundary conditions apply and how they affect the reliability of the
inference>

### Confidence: high | medium | low
<reasoning: how well-founded are the priors and likelihoods; are the
hypotheses exhaustive and well-defined; does the data quality match the
model's assumptions; how sensitive is the posterior to the prior>
```
