---
name: wardley-map
display_name: Wardley Map
class: frame
underlying_class: native
domain: strategy
source: Simon Wardley, Wardley Mapping / "The Art of Strategy", 2012–present
best_for:
  - Sorting a value chain component by its maturity and visibility to position strategy
  - Identifying which parts of an organization should be standardized vs. differentiated
  - Mapping supply-chain leverage and strategic vulnerability
one_liner: "Value chain × evolution — map strategic advantage and exposure."
---

# Wardley Map

## Overview

A Wardley Map sorts the components of a value chain along two axes: **visibility** (vertical; how far along the chain the component is visible to end users) and **evolution** (horizontal; the component's maturity from emerging to commodity). The core claim is that a component's position in this two-dimensional space determines both its strategic leverage and the appropriate response posture. Components at different evolution stages demand different investment, governance, and sourcing strategies — and mismatching strategy to position (e.g., treating a commodity as if it were emerging, or treating an emerging capability as if it were already standard) is a systematic source of waste and strategic vulnerability.

## Categories

Wardley categorizes components along the **evolution axis** into four stages, each with implications for sourcing, investment, and risk:

1. **Emerging (Genesis)**
   - The capability is **novel and poorly understood**; high uncertainty, no stable practice yet.
   - Discriminating criterion: the component does not yet have a documented, repeatable process; significant R&D investment is still required; sourcing is rare and bespoke.
   - Example: quantum computing in 2015, early blockchain use, novel machine learning architectures at their inception.
   - Visibility: typically low (internal R&D), but may be invisible if the innovation is still experimental.

2. **Growing (Custom-built)**
   - The capability is **proven to work** but still **poorly standardized**; competitive advantage is strong, but variation is high.
   - Discriminating criterion: multiple organizations are building it independently; methods vary widely; best practice is emerging but not yet settled; vendors are beginning to enter the market.
   - Example: cloud infrastructure in 2008–2010, mobile app development in the early 2010s, containerization (Docker) in 2013–2015.
   - Visibility: rising; the capability becomes visible to end users as a source of differentiation.

3. **Maturing (Product)**
   - The capability is **increasingly standardized** and **packaged**; multiple vendors offer similar solutions; differentiation begins to erode.
   - Discriminating criterion: there are established best practices; off-the-shelf products and services exist; switching costs are declining; further investment yields diminishing returns.
   - Example: relational databases by the 1990s, web hosting in the 2000s, cloud platforms (AWS, Azure) in the 2015s.
   - Visibility: commodity; the capability is expected and not a source of competitive advantage.

4. **Commodity (Utility)**
   - The capability is **completely standardized, interchangeable, and cost-driven**; all differentiation has eroded.
   - Discriminating criterion: it is offered as a utility or bulk service; cost is the primary axis of competition; switching is trivial; no organization invests in proprietary advantage here.
   - Example: electricity grids, water supply, TCP/IP routing, SSL certificates, domain registration.
   - Visibility: invisible to end users; it is taken for granted.

**Visibility axis (secondary categorization):**

Components are also positioned vertically on a **visibility spectrum** reflecting how far along the value chain—from user-facing to deep infrastructure—they are:

- **High visibility (user-facing):** directly experienced by end users.
- **Medium visibility (supporting):** used internally to enable user-facing capabilities.
- **Low visibility (infrastructure):** deep utility or platform support; invisible to most end users.

## Classification Procedure

1. **Define the component.** Name the specific capability or service you are classifying (e.g., "machine learning model training," "customer database," "payment processing").

2. **Assess standardization and competition.** Ask: "How many competing implementations exist? Is there a settled best practice? Are off-the-shelf products available?"
   - If the answer is "one or two, all bespoke" → **Emerging**.
   - If the answer is "several, but each different" → **Growing**.
   - If the answer is "many similar products; best practice is known" → **Maturing**.
   - If the answer is "interchangeable commodities; cost is the only axis" → **Commodity**.

3. **Check for evidence of eroding advantage.** Ask: "Was this a source of competitive advantage to us five years ago? Is it still?"
   - If it was emerging and is now widely offered, it has likely moved to Growing or Maturing.

4. **Determine visibility to users.** Ask: "How far along the value chain from raw infrastructure to end-user experience is this component?" Plot it vertically on the map.

5. **Record the position** as a point on the map (evolution stage × visibility).

## Implications per Category

| Evolution Stage | Governance | Sourcing | Investment | Risk posture |
|---|---|---|---|---|
| **Emerging** | Experimentation; loose controls; iterate rapidly. | Build in-house; consider research partners. | High; expect waste. Find where it yields unique advantage. | High; may not work; expect pivot. |
| **Growing** | Formalize; document practice; start building competitive moat. | Build in-house or partner closely; lock in advantage while possible. | Moderate-to-high; racing for advantage. | Moderate; approach is proven, but competition is rising. |
| **Maturing** | Standardize; optimize cost and process. | Increasingly buy off-the-shelf; internal build becomes less defensible. | Moderate-to-low; optimize, don't innovate. | Low if well-commodified; depends on pace of transition. |
| **Commodity** | Minimize; commodity management rules apply. | Buy on the open market; no reason to build. | Minimal; cost-reduction focus only. | Low; substitution is easy; focus on reliability and price. |

**Strategic implication:** Build and invest in **Emerging** capabilities where they are your unique strength. **Grow** capabilities that are becoming differentiated. **Stabilize and optimize** Maturing capabilities. **Outsource or utility-ize** Commodities. Misalignment (e.g., over-investing in commodity components, or failing to invest in emerging strengths) is a major source of strategic and economic inefficiency.

## Common Misclassifications

- **Treating a Commodity as Emerging.** Attempting to build a proprietary advantage in something that has already become undifferentiated. The tell: reinventing the wheel at great cost while competitors buy the same thing for pennies. Consequence: waste; loss of competitive focus.

- **Treating an Emerging capability as already Commodity.** Outsourcing or cutting investment in a nascent differentiator before it has ripened. The tell: a competitor invests and gains advantage while you assumed the capability was not strategic. Consequence: loss of strategic advantage and competitive position.

- **Misplacing visibility.** Plotting a component too far "user-facing" when it is actually deep infrastructure, or vice versa. This error leads to wrong sourcing decisions (e.g., over-investing in internal visibility of an internal-only component). The tell: discovering post-deployment that the component was less or more visible than assumed. Consequence: wrong prioritization of user-facing vs. internal-facing features.

- **Confusing pace of evolution with current stage.** A component may be **about to** move from Growing to Maturing, but treating it as already Commodity prematurely ends investment. The tell: competitors or market leaders are still actively innovating in this space; it is not yet fully standardized. Consequence: being late to commodity transition and paying higher costs than the leader.

- **Classifying without naming the organization.** A capability may be Commodity in the market but Emerging for a specific company entering the space late, or vice versa. Wardley Maps are org-relative, not absolute. Always specify whose map you are drawing.
