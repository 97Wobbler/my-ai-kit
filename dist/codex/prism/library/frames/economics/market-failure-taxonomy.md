---
name: market-failure-taxonomy
display_name: Market Failure Taxonomy
class: frame
underlying_class: native
domain: economics
source: origin uncertain; taxonomy formalized in welfare economics, mid-20th century
best_for:
  - Diagnosing why a market produces suboptimal allocations
  - Choosing which intervention (price control, subsidy, regulation, property rights) matches the failure mode
  - Distinguishing between genuine market failures and other sources of dissatisfaction
one_liner: "Classify the root causes of market failure to match them to appropriate policy responses."
---

# Market Failure Taxonomy

## Overview

The Market Failure Taxonomy sorts an economic situation into one of four categories based on **what structural defect prevents the market from producing a Pareto-optimal allocation**. Its core claim is that different failures demand **structurally different interventions** — and applying the wrong corrective (e.g., price controls for a public goods problem) either fails or creates worse distortions. This frame does not prescribe a solution; it clarifies which class of solution is theoretically appropriate, constraining which policy tools or instruments to consider.

## Categories

1. **Externality**
   - One party's action imposes unpriced costs or benefits on other parties who cannot opt out or bargain.
   - Individuals or firms do not face the full social cost or benefit of their choices, so they over-produce negative externalities and under-produce positive ones.
   - Discriminating criterion: there is a third party harmed or benefited by a transaction, and no property right or contractual mechanism allows the third party to be compensated or to refuse.
   - Example: a factory's pollution harms downstream residents; a homeowner's beautiful garden benefits neighbors without compensation; vaccination prevents disease in non-vaccinated peers.

2. **Public Goods (and Common Resources)**
   - A good is **non-excludable** (hard to prevent non-payers from using it) and/or **non-rival** (one person's use does not diminish another's).
   - The market undersupplies because individual actors cannot capture the full benefit of their investment, so they free-ride on others' contributions or contribute nothing.
   - Discriminating criterion: voluntary payment is unstable because the good exists once produced and you cannot exclude someone from using it, so rational actors wait for others to pay.
   - Example: national defense, basic research, a city's clean air, an open-source library, a shared fishing ground (non-rival until depleted).
   - Note: Common resources add a rivalry dimension — one actor's use degrades the good for others, creating an additional over-consumption problem.

3. **Information Asymmetry**
   - One side of a transaction has significantly better information about quality, risk, or hidden characteristics than the other.
   - The informed party can misrepresent or select against the uninformed party, causing the market to unravel (adverse selection) or encouraging bad behavior (moral hazard).
   - Discriminating criterion: the buyer (or seller) cannot verify a load-bearing claim about what they are purchasing ex ante, and the seller (or buyer) has incentive to exaggerate or hide.
   - Example: a used-car seller knows about hidden defects; an insurance company cannot observe whether a policyholder is taking safety precautions; a borrower knows their own riskiness better than the lender.

4. **Market Power (Monopoly / Oligopoly)**
   - A single seller or small group of sellers can set price above marginal cost because barriers to entry prevent competition.
   - The firm maximizes profit by restricting output and raising price, moving away from the competitive equilibrium.
   - Discriminating criterion: a seller faces a downward-sloping demand curve and can profitably reduce output; or a buyer faces upward-sloping supply and can depress price by reducing demand.
   - Example: a patented drug, a utility with exclusive regional franchise, a dominant online platform, a monopsonist employer in a rural area.

## Classification Procedure

1. **Identify the economic outcome or complaint.** Write down what market behavior is being questioned (high price, low output, non-provision, quality problems, etc.) and *from whose perspective it is a problem* (consumers, producers, society at large, a third party).

2. **Ask: "Are all affected parties represented in the market transaction?"**
   - If **no** — a third party is harmed or benefits but is not compensated and cannot bargain → **Externality**.
   - If **yes**, go to step 3.

3. **Ask: "Can the good be profitably provided by excluding non-payers, or is use by one person preventing use by another?"**
   - If **no to both** (non-excludable and either non-rival or common-pool) → **Public Goods** (or Common Resources).
   - If **yes**, go to step 4.

4. **Ask: "Can both parties verify the quality, risk, or essential facts before the transaction completes?"**
   - If **no** — the informed party has incentive to misrepresent → **Information Asymmetry**.
   - If **yes**, go to step 5.

5. **Ask: "Can a new competitor enter the market and offer a similar product at competitive cost?"**
   - If **no** — barriers to entry allow the current seller(s) to sustain price above marginal cost → **Market Power**.
   - If **yes** — the situation is **not a market failure** in the technical sense; look for other explanations (regulation, transaction costs, tastes, distribution).

6. State the classification and note which parties are bearing the cost of the failure (consumers, producers, or society).

## Implications per Category

| Failure | Core Problem | Appropriate Intervention Class |
|---|---|---|
| **Externality** | Unpriced cost/benefit to third party | Property rights (Coase theorem), Pigouvian tax/subsidy, regulation, liability. |
| **Public Goods** | Underprovision due to free-riding | Public provision, mandate, subsidy, or coordination mechanism (e.g., patent, exclusivity to recoup R&D). |
| **Information Asymmetry** | Adverse selection or moral hazard from hidden information | Mandatory disclosure, certification, bonding, insurance, auditing, or reputation systems. |
| **Market Power** | Price above marginal cost due to barriers to entry | Antitrust, price regulation, entry subsidy, or rate-of-return regulation; distinguish between natural monopoly (allow + regulate) and artificial monopoly (allow + break up). |

For policy agents, the implication is which **regulatory toolkit** is relevant. Using a price ceiling to solve an externality (e.g., capping fuel prices to address pollution) will likely worsen the underlying problem.

## Common Misclassifications

- **Externality mistaken for Market Power.** A factory raising prices and a factory polluting are both welfare-reducing, but they require different responses. The tell is whether the price change is due to restricted competition (Market Power) or unpriced harm to a third party (Externality). Raising environmental standards solves Externality; breaking up a monopoly solves Market Power but not pollution.

- **Public Goods mistaken for Market Power.** Basic research is undersupplied because individuals cannot capture returns (Public Goods), not because researchers have monopoly power. The tell is that competitive entry does not solve the problem; even many researchers cannot fund it, so a subsidy is needed.

- **Information Asymmetry mistaken for Market Power.** High car-insurance prices may be due to unobservable riskiness (Asymmetry) or insurer market power (Power). The tell is whether competitive entry would bring prices down; if entry does not solve it, the problem is likely asymmetry (not all buyers can be screened, so insurers must overprice the average). If entry does solve it, it was Market Power.

- **Regulation-induced scarcity mistaken for Market Failure.** A taxi shortage in a regulated city is not a market failure; it is a result of licensing caps. Removing the license cap, not subsidy, solves it. The tell is that the scarcity disappears if the regulatory barrier is removed, not via Pigouvian intervention.

- **Distribution of wealth mistaken for Market Failure.** If the market outcome is Pareto-optimal but someone is poor, that is a *distributional problem*, not a market failure. It may justify a transfer or redistribution, but the market is not failing — it is working as designed. The tell is that no one is made better off by a trade, so this is not an efficiency problem.
