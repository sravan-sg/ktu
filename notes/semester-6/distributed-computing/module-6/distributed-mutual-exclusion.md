# Distributed Mutual Exclusion

## Explanation
In centralized systems, mutual exclusion (ensuring that only one process accesses a critical section at a time) is easily handled using semaphores, monitors, or hardware locks provided by the OS. 

In a **distributed system**, there is no shared memory and no global physical clock. Processes communicate solely by passing messages over a network. Therefore, **Distributed Mutual Exclusion** algorithms must ensure that only one node in the entire network can enter the Critical Section (CS) at any given time, despite the lack of a central coordinator or shared state.

A robust distributed mutual exclusion algorithm must guarantee three properties:
1.  **Safety (Mutual Exclusion):** At most one process may execute in the critical section at a time.
2.  **Liveness (Progress/No Deadlock):** A process requesting entry to the CS will eventually be granted it (no deadlocks or starvation).
3.  **Ordering (Fairness):** If one request to enter the CS happened before another, entry should be granted in that order.

## Example
Consider a distributed database cluster where multiple nodes want to update the master record of a specific user's bank balance. If Node A and Node B attempt to write simultaneously without mutual exclusion, the final balance will be inconsistent (a race condition). A distributed mutual exclusion algorithm forces Node A to wait until Node B has finished its update and released the "lock," even though Node A and Node B are on different continents.

## Applications & Use Cases
-   **Distributed File Systems:** Preventing two clients on different machines from simultaneously modifying the same block of a shared file.
-   **Database Replication:** Ensuring updates to replicated databases occur in a strictly serialized order across all replica nodes to maintain strong consistency.
-   **Microservices resource allocation:** When multiple microservice instances compete for a limited physical resource (like a specific hardware port or a single-threaded legacy API endpoint).

## 3 Solved Numerical/Analytical Examples
**Example 1: Evaluating Message Complexity**
Why is message complexity the primary metric for evaluating distributed mutual exclusion algorithms?
*Solution:*
In distributed systems, network communication (latency and bandwidth) is orders of magnitude slower than local CPU computation. Therefore, the overhead of an algorithm is dominated by the number of messages it must send across the network to secure the critical section, rather than the local CPU cycles it uses.

**Example 2: Analyzing Fault Tolerance**
What happens if the node currently holding the token in a token-based mutual exclusion algorithm crashes?
*Solution:*
The token is lost. The system halts because no other node can enter the CS without the token. The algorithm must include a recovery mechanism (like a timeout and a leader election) to detect the loss and generate a new token.

**Example 3: Centralized vs Distributed Trade-offs**
Compare the latency of entering a CS in a centralized algorithm versus a fully distributed algorithm (like Ricart-Agrawala).
*Solution:*
- **Centralized:** A node sends 1 request to the server and receives 1 grant. Latency = 2 message delays.
- **Distributed (Ricart-Agrawala):** A node must multicast its request to all $N-1$ nodes and wait for $N-1$ replies. Latency = 2 message delays (assuming parallel transmission), but the *bandwidth* and *CPU processing* overhead on the network is significantly higher.

## Previous Year Questions & Solutions
*(General concepts are covered here; specific algorithms are covered in subsequent files. There are no standalone PYQs solely on the generic concept of distributed mutual exclusion in the provided set, as questions focus on specific implementations like Central Server, Ring, or Maekawa's).*
