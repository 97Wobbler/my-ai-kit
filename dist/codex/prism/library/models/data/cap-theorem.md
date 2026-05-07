---
name: CAP Theorem
domain: data
source: Eric Brewer, "Towards Robust Distributed Systems," PODC keynote (2000); formalized by Gilbert & Lynch, "Brewer's CAP Theorem," ACM SIGACT News 33, no. 2 (2002)
best_for: Characterizing the tradeoff landscape of distributed systems and selecting datastores that match application consistency and availability requirements
one_liner: "Under network partition, a distributed system must trade consistency for availability — choose CP or AP."
---

# CAP Theorem

## Overview

The CAP Theorem (Consistency, Availability, Partition tolerance) states that in a distributed system, when a **network partition** occurs (nodes lose the ability to communicate), the system must choose between:

- **Consistency (C)**: All nodes see the same data at the same time (linearizability).
- **Availability (A)**: Every non-failing node can respond to requests.
- **Partition tolerance (P)**: The system continues to operate despite lost messages.

Since network partitions are **inevitable in real distributed systems**, the practical choice is between **CP** (consistency over availability) and **AP** (availability over consistency). CA (both C and A without P) is not a realistic option because you cannot prevent partitions; pretending they don't exist leads to catastrophic failures. The theorem clarifies that you cannot have all three; you must make an explicit architectural choice about what to sacrifice.

## Core Variables and Relationships

Three system properties:

1. **Consistency (C)**: Linearizability — every read returns the most recent write. All nodes agree on the current state. Once a write is acknowledged, all subsequent reads see that value.

2. **Availability (A)**: Every request to a non-failing node receives a response (success or failure), without timeout. The system is always responding.

3. **Partition tolerance (P)**: The system continues to operate when the network partitions (some messages are lost). Nodes continue to communicate within their partition, even if they cannot reach other partitions.

The theorem: If a partition occurs, you must choose CP or AP.

- **CP systems** (MongoDB with strong consistency, HBase, Zookeeper): When partitioned, the system blocks writes to prevent stale data. Some nodes become unavailable.
- **AP systems** (Cassandra, DynamoDB, DNS, eventual consistency): When partitioned, nodes continue to respond, accepting writes. Data may diverge; consistency is eventual (resolved asynchronously).

## Key Predictions

1. **Partitions always happen.** Assume network partitions will occur multiple times in your system's lifetime. Budget for it.

2. **CP and AP have inverse tradeoffs in failure modes**:
   - CP: Partition causes write unavailability (timeout, 503 errors) until the partition heals. Consistency is maintained.
   - AP: Partition causes temporary inconsistency (stale reads). Consistency is eventually restored but not immediately.

3. **The choice cascades into architecture**:
   - CP systems require careful replication, quorum-based consistency, and (often) centralized coordination. Scaling is harder because you must prevent divergence.
   - AP systems require conflict resolution (last-write-wins, vector clocks, CRDT), async replication, and careful eventual consistency models. Data reconciliation can be complex.

4. **Single-node systems have no partition concern.** A standalone database (single Postgres instance) has no network partition to worry about. CAP does not apply; you can have CA. Scaling to multiple nodes changes this.

5. **Cloud deployments often lean AP.** AWS DynamoDB, Cassandra, and DNS are AP systems designed for high availability across regions even when network faults occur.

## Application Procedure

1. **Identify candidate datastores** — List 3–5 systems you might use (relational, NoSQL, cache, etc.).

2. **Classify each as CP or AP** — For each datastore, determine its behavior during a network partition:
   - MongoDB (with strong consistency): CP — blocks writes during partition.
   - Cassandra: AP — continues serving, eventual consistency.
   - PostgreSQL (single-node): CA — not distributed, partition irrelevant.
   - DynamoDB: AP — partition-resilient, high availability.
   - Redis Sentinel: CP — quorum-based failover.

3. **Map application requirements**:
   - **Strong consistency requirement** (financial transactions, inventory counts): Choose CP.
   - **High availability requirement** (user-facing read-heavy services, CDN): Choose AP.
   - **Mixed**: Use CP for the critical path; AP for non-critical reads.

4. **Evaluate partition behavior in practice** — Study the datastore's documented behavior during partitions. Example: MongoDB's writes to the minority partition fail; DynamoDB's writes succeed but may cause conflicts.

5. **Design conflict resolution** — If AP, decide how to resolve divergence:
   - Last-write-wins (timestamp-based): simple but can lose data.
   - Vector clocks or CRDT: more complex but preserves concurrent updates.
   - Application-side merge logic.

6. **Test partition scenarios** — Use chaos engineering to simulate partitions and verify the system behaves as classified.

## Boundary Conditions

- **PACELC is a modern refinement.** PACELC (Else Latency vs Consistency) extends CAP by noting that even without partitions, you must choose between latency and consistency. A CP system that prioritizes consistency will have higher latency. This is often a bigger concern than partitions.

- **Eventual consistency models vary.** AP systems are not all the same. Cassandra's eventual consistency (read-repair, anti-entropy), DynamoDB's eventual consistency (with strong consistency option per request), and DNS's eventual consistency are all different.

- **Tunable consistency.** Some systems (Cassandra, DynamoDB) allow per-request tuning: strong consistency for critical reads (higher latency), eventual consistency for non-critical reads (lower latency).

- **Simplified binary.** The theorem treats C, A, and P as binary, but real systems exhibit degrees. A system might be "mostly consistent" or "highly available but not always."

- **Network faults vs. node faults are different.** CAP is about network partitions, not single node failures. A node failure can be handled in both CP and AP systems.

- **Not applicable to fully connected systems.** In-process libraries or systems with no network are not subject to CAP constraints.

## Output Format

```
## CAP Analysis: <application or system>

**System scope:**
- Distributed? Yes | No
- Replication factor: <N>
- Geographic spread: <single region | multi-region | global>

**Candidate datastores:**
| Datastore | Consistency model | CAP classification | Partition behavior | Conflict resolution |
|---|---|---|---|---|
| <Name> | <linearizable / eventual / tunable> | CP / AP / CA | <what happens when nodes lose contact> | <method> |
| ... | ... | ... | ... | ... |

**Application requirements:**
- Consistency: required | preferred | not required
- Availability: required | preferred | not required
- Partition tolerance: required (assume partition will happen)
- Acceptable stale data window: <seconds / minutes / not acceptable>
- Write frequency: <requests/sec>
- Geographic spread: <single datacenter / multi-region>

**CAP decision:**
- Chosen model: CP | AP
- Justification: <why this tradeoff is correct for this application>
- Cost of the choice: <availability loss (CP) | consistency loss (AP)>
- Fallback strategy: <if primary choice fails (e.g., failover to read-only mode)>

**Conflict resolution strategy (if AP):**
- Method: <last-write-wins / vector clocks / CRDT / application-side>
- Implementation: <library or custom code>
- Validation: <how conflicts are detected and tested>

**Modern considerations (PACELC):**
- Without partition: consistency vs. latency tradeoff — <how is latency managed?>
- During partition: consistency vs. availability tradeoff — <which is sacrificed?>

**Monitoring & alerting:**
- Partition detection: <how partitions are observed>
- Divergence monitoring: <metrics for consistency drift in AP systems>
- Recovery validation: <how to verify convergence after partition heals>

**Confidence: high | medium | low**
<reasoning: clarity of requirements, stability of network, complexity of conflict resolution, team familiarity with the chosen datastore>
```
