---
name: distributed-fallacies
display_name: Fallacies of Distributed Computing
class: heuristic
underlying_class: native
domain: architecture
source: L. Peter Deutsch and James Gosling, Sun Microsystems (~1994-1997)
best_for:
  - Distributed system design and risk assessment
  - Microservices architecture review
  - API and network boundary validation
one_liner: "Bundle — 8 false assumptions that trap distributed system designers."
---

# Fallacies of Distributed Computing

When designing a distributed system, engineers often begin with false assumptions about how the network, systems, and components will behave. These eight fallacies are not rules that *always* hold; rather, they are mistakes that almost *always* cause problems because they go unexamined. Each fallacy is a common design assumption that breaks in production. This bundle is best applied as a **sanity gate** when reviewing distributed system architectures or microservices designs: walk through each fallacy and ask whether the design acknowledges and handles the failure mode.

The fallacies grew out of early network and RPC design at Sun Microsystems and have been refined through decades of distributed systems practice. They remain remarkably durable: systems that overlook them suffer nearly identical failures, decades apart.

---

## The Network Is Reliable

**The Rule**
The network will fail: packets are lost, messages are dropped, connections hang, and timeouts occur. There is no such thing as a perfectly reliable network.

**When It Applies**
- Designing communication between microservices, servers, or components in different failure domains.
- Evaluating whether a system has circuit breakers, retries, and fallback logic.
- Assessing the consequences of a service becoming unreachable for seconds or minutes.

**When It Misleads**
- In tightly-coupled, single-datacenter systems with high-speed interconnect, network failures are rare and latency is very low. The fallacy is less urgent there, though it is never absent.
- If applied to suggest the system should not try to communicate at all. The goal is to design *for* failures, not to avoid communication.

**Common Misuse**
Assuming that because you deployed retries, the network is now reliable. Retries add resilience but introduce new problems: idempotence, thundering herd, and cascade failures. The fallacy is a reminder that no amount of client-side logic makes an unreliable network reliable.

**How Agents Use It**
- **Sanity-gate**: on every cross-service call, ask: "What happens if this request hangs for 30 seconds? 5 minutes? Forever?" If the system has no answer, the fallacy is not being addressed.

---

## Latency Is Zero

**The Rule**
Network communication takes time. Remote calls are orders of magnitude slower than local function calls. Design assuming calls will be slow and variable.

**When It Applies**
- Evaluating whether a design makes too many network round-trips. Chatty RPC patterns (request → response → request → response) amplify latency pain.
- Assessing whether timeout values are realistic for the actual network distances involved.
- Determining batch sizes, prefetch depths, or pipelining strategies to hide latency.

**When It Misleads**
- In local in-memory systems or same-process communication where latency is genuinely near-zero.
- If used to forbid all remote communication. Some latency is worth paying for better separation of concerns.

**Common Misuse**
Setting timeouts that are too short because "the network should be fast," or designing a system to make synchronous calls when batching or asynchrony would be better. The fallacy is a call to measure and plan around actual latencies, not to deny them.

**How Agents Use It**
- **Sanity-gate**: for critical or frequent cross-service calls, require explicit documentation of the expected latency range and the timeout strategy.

---

## Bandwidth Is Infinite

**The Rule**
Network bandwidth is finite and often the bottleneck. Transferring large amounts of data, making many concurrent requests, or assuming you can send whatever you want will exhaust capacity.

**When It Applies**
- Designing APIs where every response includes full nested objects instead of summaries or IDs.
- Assessing whether the system is making too many concurrent requests to a single service, causing queue buildup or backpressure.
- Choosing between multiple APIs: one that returns a large response versus one that requires multiple smaller requests.

**When It Misleads**
- In gigabit internal networks where bandwidth pressure is rarely the first constraint.
- If it discourages caching or compression, which reduce bandwidth pressure.

**Common Misuse**
Assuming that better compression or caching solves all bandwidth problems, or designing for "typical" bandwidth when the system needs to handle spikes. The fallacy is a reminder to measure and monitor bandwidth usage.

**How Agents Use It**
- **Sanity-gate**: for data-heavy operations, ask: "Is the response size proportional to its value? Could we reduce it by pagination, filtering, or lazy loading?"

---

## The Network Is Secure

**The Rule**
Network traffic can be observed and modified by unauthorized parties. Assume all traffic is visible and may be tampered with unless actively secured.

**When It Applies**
- Designing systems that expose data to the network without encryption.
- Assessing whether authentication and authorization are applied at every network boundary, not just the perimeter.
- Evaluating the consequences of a service being accessed from a hostile network (e.g., the internet).

**When It Misleads**
- In completely air-gapped, physically-secured networks with no external connections.
- If applied to forbid any unencrypted communication. Some traffic (e.g., within a secured datacenter) may not need encryption, but this is an explicit choice, not an assumption.

**Common Misuse**
Assuming that "we are inside the company network" is sufficient security, or that "everyone here is trustworthy." Network security is layered; internal networks still require authentication and validation.

**How Agents Use It**
- **Sanity-gate**: on every service-to-service or service-to-external interface, ask: "Is authentication required? Are we validating input? Is the connection encrypted?"

---

## Topology Does Not Change

**The Rule**
Network and infrastructure topology changes: nodes fail, services are redeployed, load balancers are reconfigured, and data center failovers happen. Do not assume a fixed, static set of nodes or paths.

**When It Applies**
- Designing systems with hardcoded IP addresses or service locations instead of service discovery.
- Assessing whether a system can handle the rolling restart or replacement of nodes without user-facing impact.
- Evaluating whether a cache or routing layer will invalidate or update when the underlying topology changes.

**When It Misleads**
- In completely static, never-changing production environments (rare).
- If applied to require elaborate dynamic discovery when a simple, infrequent manual update is more practical.

**Common Misuse**
Building dynamic service discovery but then caching service locations too aggressively, defeating the purpose. The fallacy is about preparing for change, not necessarily about making change instantaneous.

**How Agents Use It**
- **Sanity-gate**: on deployment and infrastructure changes, ask: "Are clients notified when the topology changes? Is there a graceful transition period, or will requests fail?"

---

## There Is One Administrator

**The Rule**
In large distributed systems, no single person understands or controls the entire system. Teams, organizations, and domains have overlapping responsibilities and incomplete information.

**When It Applies**
- Designing systems that must coordinate across multiple teams or organizations.
- Assessing whether error messages and monitoring expose enough information for distributed troubleshooting.
- Evaluating whether one team can deploy or patch without waiting for others.

**When It Misleads**
- In very small organizations with one person actually operating everything, the fallacy has less relevance (though knowledge concentration is still a risk).
- If applied to forbid any shared responsibility or coordination. Some coordination is necessary and valuable.

**Common Misuse**
Assuming that if a system is complex, more documentation and central coordination will solve it. The fallacy is a reminder that humans are the bottleneck, not information flow alone.

**How Agents Use It**
- **Sanity-gate**: on operational recommendations, ask: "Who is responsible for each piece? Is that person or team equipped with the information and authority they need?"

---

## Transport Cost Is Zero

**The Rule**
Moving data across the network has a financial and operational cost: bandwidth charges, energy consumption, and latency. This cost must be considered in system design.

**When It Applies**
- Designing data synchronization between datacenters or cloud regions, where egress charges apply.
- Assessing whether the system is replicating or moving more data than necessary.
- Evaluating the cost-benefit of caching versus re-fetching.

**When It Misleads**
- In systems with unlimited bandwidth and no metering (rare in modern cloud).
- If applied to forbid all data movement; some movement is necessary and worth the cost.

**Common Misuse**
Optimizing for zero transport cost and creating a system too chatty to debug. The fallacy is a reminder to measure and plan around actual costs.

**How Agents Use It**
- **Sanity-gate**: on data-heavy operations, especially those crossing organizational or regional boundaries, ask: "What is the operational and financial cost of moving this data? Is it justified by the benefit?"

---

## The Network Is Homogeneous

**The Rule**
Not all network paths, services, and infrastructure are identical. Latency, reliability, bandwidth, and security differ across connections. Do not assume uniform behavior.

**When It Applies**
- Designing systems that must work across multiple cloud providers or on-premises data centers.
- Assessing whether the system can handle customers on different network qualities (broadband, mobile, satellite).
- Evaluating whether a single timeout value or buffer size is appropriate for all network segments.

**When It Misleads**
- In fully standardized, homogeneous infrastructure (rare in large systems).
- If applied to suggest that systems should not share infrastructure. Some consolidation is valuable; the fallacy is about preparing for variance.

**Common Misuse**
Tuning the system for the fastest, most reliable network path available and then being surprised when it fails for users on slower connections. The fallacy is a reminder that real-world networks are varied.

**How Agents Use It**
- **Sanity-gate**: on performance, reliability, and scalability recommendations, ask: "Is this tuned for a specific network condition? Will it fail or degrade gracefully on slower, less reliable paths?"
