---
name: electoral-systems
display_name: Electoral Systems
class: frame
underlying_class: native
domain: political-science
source: Maurice Duverger, Arend Lijphart, 1951–1999
best_for:
  - Sorting electoral rule into a category that predicts party-system structure and representation outcomes
  - Understanding why the same vote share produces different seat distributions under different rules
one_liner: "Classify an electoral system as FPTP / PR / MMP / Runoff / AV to predict party-system fragmentation and representation type."
---

# Electoral Systems

## Overview

Electoral Systems is a frame that sorts voting rules into categories based on the **relationship between vote share and seat allocation**. Its core claim is that different systems create **systematically different incentives for party formation, coalition, and representation**—and the same electoral outcome (e.g., a 30% vote share) translates into radically different seat counts, government formation paths, and minority representation depending on which rule is in play. Duverger's Law and Lijphart's comparative work show that the choice of system is not neutral; it is a load-bearing structural decision that shapes the entire party system downstream.

## Categories

1. **First-Past-The-Post (FPTP)**
   - Single-member districts; the candidate with the most votes wins the seat, regardless of margin.
   - Produces disproportionality: a party winning 35% of votes nationally may win 55% of seats.
   - Discriminating criterion: no proportionality requirement; winner-take-all at district level creates strong incentive to consolidate support into two major parties.
   - Example: United Kingdom, United States, Canada.

2. **Proportional Representation (PR)**
   - Seats allocated to parties in proportion to vote share, usually via party-list voting or multi-member districts with quota-based allocation.
   - A party with 10% of votes receives approximately 10% of seats.
   - Discriminating criterion: explicit proportionality constraint; incentivizes smaller parties to run and survive because they can win seats at low vote thresholds.
   - Example: Netherlands, Israel, Spain (regional lists).

3. **Mixed-Member Proportional (MMP)**
   - Voters cast two votes: one for a local representative (FPTP-style), one for a party.
   - Seat totals are adjusted so that party representation in the legislature matches the party vote share.
   - Discriminating criterion: hybrid mechanism; uses local representation as primary layer but corrects for overall proportionality through list seats.
   - Example: Germany, New Zealand, Mexico.

4. **Runoff / Two-Round System (TRS)**
   - If no candidate wins a majority in the first round, a second election is held, usually between the top two finishers.
   - More majoritarian than FPTP but less consolidating; allows a broader field in round one.
   - Discriminating criterion: requires explicit majority threshold, forcing candidates to build broader coalitions in round two; often used in presidential elections.
   - Example: France (presidential), many Latin American countries.

5. **Alternative Vote / Instant Runoff (AV)**
   - Voters rank candidates in order of preference; if no candidate wins a majority of first preferences, the lowest-ranked candidate is eliminated and their votes redistributed; process repeats until someone has a majority.
   - Seat allocation can be proportional or majoritarian depending on district size; often uses single-member districts with preference ranking.
   - Discriminating criterion: eliminates spoiler effects by allowing voters to express true preference without fear; requires ordinal (not cardinal) input from voters.
   - Example: Australia (House), Ireland (some local elections), Papua New Guinea.

## Classification Procedure

1. **Identify the voting unit.** What is the geographic or organizational scope of a single vote? Is it a single-member district, a multi-member district, or a national list?
   
2. **Determine the seat-allocation rule.** How are seats awarded?
   - If "winner of most votes in district gets the seat" and votes are cast in single-member districts → **FPTP**.
   - If "parties receive seats proportional to their vote share" across multi-member districts or via list allocation → **PR**.
   - If "two votes: one local, one party; final seat count corrected to match party vote share" → **MMP**.
   - If "candidate must win a majority; if not, hold a second round (or eliminate low finishers)" → **Runoff or AV** (see step 3).

3. **If majority requirement is in play, distinguish Runoff from AV.**
   - If the second-round vote is **a new election** (voters vote again, often between top two) → **Runoff**.
   - If second preferences are **expressed in the first round** (ranked ballot) and counted mechanically without a new election → **AV**.

4. **Verify with seat proportionality.** Does the resulting seat distribution closely match the vote share?
   - If no, and the system is not explicitly designed for proportionality → FPTP, Runoff, or AV.
   - If yes, or the system explicitly targets proportionality → PR or MMP.

5. **State the classification and note the expected party-system implication** (see Implications below).

## Implications per Category

| System | Party-system prediction | Representation outcome | Typical government formation |
|---|---|---|---|
| **FPTP** | **Duopoly**: strong incentive to coalesce into two major parties; smaller parties face "wasted vote" problem. | **Disproportional** and **majoritarian**: 35% of votes often yields 55%+ of seats; landslide swings possible. | Single-party majority government is norm; coalition rare. |
| **PR** | **Fragmented**: low barrier to entry for small parties; multiple parties survive. | **Proportional**: 10% votes → ~10% seats; no wasted votes. | Multi-party coalition or minority government is norm; requires negotiation. |
| **MMP** | **Moderate fragmentation**: local races incentivize local candidacies, but party vote allows smaller parties. | **Proportional overall** with local representation preserved. | Coalition or minority government; often produces governments with 3+ parties. |
| **Runoff** | **Moderate duopoly**: fewer incentives to coalesce as aggressively as FPTP, but majority requirement pushes toward fewer large parties. | **Moderately disproportional** but less extreme than FPTP; majority guaranteed. | Single-party majority or stable coalition; depends on second-round dynamics. |
| **AV** | **Moderate duopoly**: spoiler effect reduced; allows voter expression of true preference without penalty. | **Moderately disproportional** (less than FPTP); depends on district magnitude and threshold. | Single-party majority typical if used in single-member districts; more fragmented if multi-member. |

The frame implies that **system choice determines which coalitional and representational outcomes are structurally easier or harder**, not which are morally preferable.

## Common Misclassifications

- **PR mistaken for MMP.** The tell: in PR, seats are allocated purely by vote share; in MMP, there are two distinct voting channels and a correction mechanism. If voters cast one vote per party and all seats flow from that vote → PR. If voters cast two votes and seats are adjusted to match the party vote → MMP.

- **FPTP mistaken for Runoff.** The tell: Runoff has an explicit majority threshold and a second round if no one reaches it; FPTP awards the seat to whoever has the most votes regardless of margin. If 35% wins the seat with no majority requirement → FPTP. If a second round is triggered or a candidate must clear 50% → Runoff.

- **AV mistaken for Runoff.** The tell: AV uses ranked preferences on a single ballot and redistributes votes mechanically; Runoff holds a new election. If preferences are collected in one round → AV. If a new election is held → Runoff.

- **Confusing the threshold with the system.** Many PR systems use a legal threshold (e.g., 3%) to filter out tiny parties; this is a **parameter, not a category**. A system is still PR even with a high threshold—it is still proportional within the eligible pool.

- **Classifying by outcome rather than rule.** It is tempting to label a result (e.g., "the government has only two parties") as FPTP-like, but outcome depends on vote distribution and history, not just rule. A PR system can produce a two-party parliament if voters choose to vote for only two parties. The frame is about the **rule structure**, not the observed parliament.
