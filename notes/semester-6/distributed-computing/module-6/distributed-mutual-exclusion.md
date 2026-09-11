# Distributed Mutual Exclusion

## Explanation
In centralized uniprocessor systems, mutual exclusion (ensuring that only one process accesses a critical section at a time) is easily handled using OS-level semaphores, monitors, or hardware locks. 

According to **Tanenbaum (Chapter 6)**, in a **distributed system**, there is no shared memory and no global physical clock. Processes communicate solely by passing messages over a network. Therefore, **Distributed Mutual Exclusion** algorithms must mathematically guarantee that only one node in the entire network can enter a shared Critical Section (CS) at any given time, despite the lack of a central coordinator or shared state.

A robust distributed mutual exclusion algorithm must guarantee three properties:
1. **Safety (Mutual Exclusion):** At most one process may execute in the critical section at any given time.
2. **Liveness (Progress/No Deadlock):** A process requesting entry to the CS will eventually be granted it. The system must be free of deadlocks and starvation.
3. **Ordering (Fairness):** If one request to enter the CS happened before another (often determined using Lamport logical clocks), entry should be granted in that precise temporal order.

Tanenbaum categorizes distributed mutual exclusion into two primary approaches:
- **Token-based solutions (e.g., Ring algorithm):** A special token is passed around; only the token holder can enter the CS.
- **Permission-based solutions (e.g., Ricart-Agrawala, Maekawa):** A process must proactively acquire permission from other processes before entering the CS.

## Example
Consider a distributed database cluster where multiple nodes want to update the master record of a specific user's bank balance. If Node A and Node B attempt to write simultaneously without mutual exclusion, the final balance will be corrupted (a classic race condition). A distributed mutual exclusion algorithm (like Ricart-Agrawala) forces Node A to mathematically prove it requested access first, forcing Node B to wait until Node A has finished its update and sent an `OK` (release) message, even if Node A and Node B are physically located on different continents.

## Applications & Use Cases
- **Distributed File Systems:** Preventing two clients on different machines from simultaneously modifying the exact same block of a shared file.
- **Database Replication:** Ensuring updates to replicated databases occur in a strictly serialized order across all replica nodes to maintain strong sequential consistency.
- **Microservices Resource Allocation:** When multiple microservice instances compete for a limited physical resource (like a specific hardware port or a single-threaded legacy API endpoint).

## 3 Solved Numerical/Analytical Examples

**Example 1: Evaluating Message Complexity**
*Problem:* Why is message complexity the primary metric for evaluating distributed mutual exclusion algorithms?
*Solution:*
1. In distributed systems, network communication (latency and bandwidth limitations) is orders of magnitude slower than local CPU computation. 
2. Therefore, the overhead of an algorithm is heavily dominated by the number of messages it must send across the network to secure the critical section.
*Conclusion:* Network latency is the bottleneck, not CPU cycles.

**Example 2: Analyzing Fault Tolerance in Token Systems**
*Problem:* What happens if the node currently holding the token in a token-based mutual exclusion algorithm crashes?
*Solution:*
1. The token is irrevocably lost. 
2. The system halts (violating Liveness) because no other node can ever enter the CS without the token. 
*Conclusion:* The algorithm must include a complex distributed recovery mechanism (like a timeout and a leader election via the Bully algorithm) to detect the loss and securely generate a new token without accidentally generating two tokens (which would violate Safety).

**Example 3: Centralized vs. Distributed Trade-offs**
*Problem:* Compare the network latency of entering a CS in a centralized algorithm versus a fully distributed, permission-based algorithm (like Ricart-Agrawala).
*Solution:*
1. **Centralized:** A node sends 1 request to the server and receives 1 grant. Total latency = 2 message delays (1 RTT).
2. **Distributed (Ricart-Agrawala):** A node must multicast its request to all $N-1$ nodes and wait for $N-1$ `OK` replies. 
*Conclusion:* The latency remains approximately 2 message delays (assuming perfectly parallel transmission), but the *bandwidth* and *CPU processing* overhead on the network scales linearly with $O(N)$, making it far less scalable.

## Previous Year Questions & Solutions
*(Note: General theoretical concepts are covered here. Specific algorithm implementations are covered in the `central-server-algorithm.md`, `ring-based-algorithm.md`, and `maekawas-voting-algorithm.md` files. There are no standalone PYQs solely on the generic concept of distributed mutual exclusion in the provided syllabus set, as exams focus on specific algorithmic mechanics).*
