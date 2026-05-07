---
name: Technical Debt
domain: agile
source: Ward Cunningham, "The WyCash Portfolio Management System," OOPSLA 1992; formalized as financial metaphor in numerous subsequent works by Cunningham, Martin Fowler, and others
best_for: Characterizing and evaluating the long-term cost of deferred refactoring, prioritizing which debts to repay, and predicting team velocity impact of growing debt
one_liner: "Shortcuts borrow development speed today and accrue compounding interest until repaid."
---

# Technical Debt

## Overview

Technical Debt is Ward Cunningham's financial metaphor for the cost of taking shortcuts in code, design, or architecture. When a team decides to skip refactoring, defer test coverage, or use a quick-and-dirty solution to meet a deadline, they are borrowing future development capacity to pay present time costs. Like financial debt, technical debt **accrues interest**: each change to the affected code takes longer, requires more knowledge of workarounds, and introduces more bugs. If debt is left unmanaged, interest payments eventually dominate and the team's ability to ship anything declines (terminal velocity collapse). The model explains why "messy" systems become progressively slower, and why active, periodic refactoring is not optional—it is a cost of doing business.

## Core Variables and Relationships

- **Principal (P)**: The engineering effort required to repay the debt (refactor the code, add missing tests, rewrite the module). Measured in story points, person-days, or hours.

- **Interest rate (r)**: The productivity drag per unit of future work that touches the debt. Measured as a percentage of effort per feature that must navigate or work around the debt.

- **Interest accrual**: Compounds with each change touching the debt. If a debt has 5% interest and is touched in 3 sprints, the total interest accrued is roughly 3 × 5% = 15% of effort over those 3 sprints.

- **Debt service capacity**: The team's bandwidth allocated to repayment (refactoring, test coverage, tech investment sprints). Measured as % of sprint capacity.

- **Debt threshold**: The point at which interest payments consume so much capacity that new feature development stalls. Beyond this point, velocity collapses and the team effectively becomes unable to ship.

**Key insight**: Deferred refactoring compounds; the team doesn't pay interest once and move on. Each new feature that touches the debt incurs the cost again. If the debt is never repaid, interest payments grow unbounded.

## Key Predictions

1. **Debt hits a tipping point.** A system with small technical debt (< 10% of sprint effort spent on rework) is manageable. As debt grows, the tipping point arrives suddenly: once debt-related work exceeds ~40% of capacity, new feature velocity drops sharply (from 40 points/sprint to 10–20 points/sprint).

2. **Interest compounds rapidly.** Code that was a 1-point workaround when created can become a 100-point refactoring project if left for two years and touched by five different features. Each touch adds coupling and hidden complexity.

3. **Deliberate vs. inadvertent debt have different curves**:
   - **Deliberate debt** (we know we're cutting a corner, with plans to repay): Interest remains stable and manageable until repayment.
   - **Inadvertent debt** (we didn't realize we were taking a shortcut): Interest grows faster because the team doesn't see the problem coming; rework and surprises multiply.

4. **Terminal velocity collapse is sudden.** Before collapse: velocity is steady despite rising debt. At collapse: adding more developers doesn't help because all effort goes to rework, not new features.

5. **Refactoring is not a luxury; it is a velocity maintenance cost.** Teams that allocate 10–20% of capacity to refactoring maintain steady velocity. Teams that allocate zero to refactoring experience declining velocity that eventually hits zero.

## Application Procedure

1. **Enumerate known debts** — Identify every instance of known shortcuts:
   - Skipped unit tests for a module
   - Copy-paste code duplicated across 3+ places
   - Module with >500 lines and >20 cyclomatic complexity
   - API with undocumented quirks that all clients must work around
   - Dependency on deprecated library that is still in use
   - Configuration that is scattered across code instead of centralized

2. **Estimate principal (refactoring cost)** for each debt:
   - Write missing tests: 5–20 points
   - Refactor duplicated code: 10–30 points
   - Rewrite overly complex module: 30–80 points
   - Upgrade deprecated dependency: 5–50 points (depending on breaking changes)

3. **Estimate interest rate (drag per touch)** — For each debt, estimate how much slower a feature becomes if it must navigate or modify this code:
   - Debt with good documentation but messy code: 5% interest
   - Debt with no tests and no documentation: 20% interest
   - Debt that is actively avoided (most developers don't go near it): 30% interest

4. **Classify each debt** using Fowler's quadrant:
   - **Deliberate + Reckless**: High-risk shortcut taken knowing the cost (e.g., shipping v1 with no tests). Repay quickly.
   - **Deliberate + Prudent**: Calculated technical debt for strategic timing (e.g., MVP to hit market window). Plan specific repayment date.
   - **Inadvertent + Reckless**: Incompetence or negligence (e.g., copy-paste because no one knew DRY). Fix immediately.
   - **Inadvertent + Prudent**: Recognized only after delivery (e.g., design limitation revealed by usage). Prioritize for next refactoring cycle.

5. **Simulate interest accrual** — Model how many sprints touch each debt and how much interest is paid:
   - Debt A: 20-point principal, 10% interest, touched every 2 sprints → 5 points of interest every 2 sprints.
   - Debt B: 50-point principal, 5% interest, touched every sprint → 2.5 points of interest every sprint.

6. **Identify the debt threshold** — Calculate total interest load across all debts. If approaching 40% of sprint capacity, activate repayment immediately.

7. **Schedule repayment** — Allocate specific sprints to paying down principal. Prioritize high-interest debts first (largest interest payments).

## Boundary Conditions

- **Not all "messy code" is debt.** Code written by someone else that you don't understand is not necessarily debt. It may just be unfamiliar. Debt is specifically unplanned coupling or missing tests that slow future change.

- **"Design debt" may not have a clear principal.** Some debts (wrong architectural choice, misaligned component boundaries) cannot be repaid by refactoring alone; they require redesign. Estimate conservatively.

- **Interest rate is context-dependent.** A 50-line function is less debt in a stable module than in a rapidly-evolving feature. Interest is highest in code that changes frequently.

- **Refactoring is not free.** The principal (cost of refactoring) is often higher than the original shortcut. This is why deliberate debt trades off short-term delivery for long-term cost.

- **Technical debt is a team-level phenomenon.** Individual developers cannot unilaterally "repay" debt; it requires allocation and coordination.

## Output Format

```
## Technical Debt Assessment: <system or module>

**Known debts:**
| Debt | Location | Principal (points) | Interest rate | Classification | Last touched |
|---|---|---|---|---|---|
| Missing unit tests | payment_processor.py | 15 | 15% | Deliberate + Reckless | 3 sprints ago |
| Duplicated auth logic | auth_handler.py, user_service.py, admin_service.py | 25 | 10% | Inadvertent + Prudent | Every sprint |
| Deprecated API wrapper | legacy_client.py | 30 | 20% | Deliberate + Prudent | 2 sprints ago |
| ... | ... | ... | ... | ... | ... |

**Interest accrual projection (next 6 sprints):**
| Sprint | Total interest load (points) | % of capacity | Velocity impact | Notes |
|---|---|---|---|---|
| Sprint 1 | 8 | 10% | Minimal | ... |
| Sprint 2 | 12 | 15% | ... | ... |
| ... | ... | ... | ... | ... |

**Debt threshold analysis:**
- Current total principal: <sum> points
- Current interest burden: <percentage> % of sprint capacity
- Threshold approached? Yes | No | Imminent
- Estimated runway before velocity collapse: <N sprints>

**Repayment plan:**
1. **Highest priority (immediate)**
   - Debt: <name>
   - Principal: <X> points
   - Target completion: <Sprint N>
   - Expected velocity recovery: <Y points/sprint>

2. **Secondary (next quarter)**
   - Debt: <name>
   - ...

**Monitoring metrics:**
- Interest load (% of sprint): <target: < 20%>
- Refactoring allocation (% of sprint): <target: 15–20%>
- Module age before major refactor: <target: 2–3 years>
- Lines of code in top-5 messiest modules: <trend: should stabilize>

**Confidence: high | medium | low**
<reasoning: accuracy of principal estimates, stability of interest rates across teams, clarity of debt classification, team buy-in on refactoring allocation>
```
