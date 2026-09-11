# Maekawa's Voting Algorithm

## Explanation
**Maekawa's Voting Algorithm** is a permission-based distributed mutual exclusion algorithm. While algorithms like Ricart-Agrawala require a node to get permission from *all* other nodes in the system ($N-1$ messages), Maekawa observed that a node doesn't need everyone's permission; it only needs permission from a mathematically defined subset of nodes, called its **Voting Set** ($V_i$).

To mathematically guarantee mutual exclusion (Safety), the algorithm enforces a strict intersection rule: **Any two voting sets must have at least one node in common**. Because every node can only cast one "vote" (grant permission) at a time, the common node in the intersecting sets acts as a tie-breaker, preventing two different processes from simultaneously gathering enough votes to enter the Critical Section (CS).

**Mathematical Properties of Voting Sets ($V_i$) for $N$ processes:**
1. **Intersection:** $V_i \cap V_j \neq \emptyset$ (for all $i, j$). This is the core mutual exclusion guarantee.
2. **Self-inclusion:** $P_i \in V_i$.
3. **Size:** $|V_i| = K$ for all $i$ (all sets are exactly the same size).
4. **Workload:** Each process $P_j$ belongs to exactly $M$ voting sets.
*Optimal Configuration:* To minimize message overhead while maintaining perfect fairness, the sets are designed such that $K = M \approx \sqrt{N}$.

**How it works:**
1. **Request:** Process $P_i$ sends a `REQUEST` message to all members of its voting set $V_i$.
2. **Reply (Vote):** When a process $P_j$ receives a request, it sends a `REPLY` (vote) if it hasn't already voted for someone else. If it has already voted, it queues the request.
3. **Enter CS:** $P_i$ enters the CS only when it receives a `REPLY` from *every* single member of its voting set $V_i$.
4. **Release:** Upon exiting the CS, $P_i$ sends a `RELEASE` message to all members of $V_i$.
5. **Next in line:** When a node in $V_i$ receives the `RELEASE`, it can now cast its vote for the next process in its queue (if any).

## Example
Consider a distributed system of $N = 3$ nodes ($P_1, P_2, P_3$). We need voting sets where any two sets intersect.
- $V_1 = \{P_1, P_2\}$
- $V_2 = \{P_2, P_3\}$
- $V_3 = \{P_3, P_1\}$

Notice that $V_1 \cap V_2 = \{P_2\}$, $V_2 \cap V_3 = \{P_3\}$, and $V_1 \cap V_3 = \{P_1\}$.
If $P_1$ wants the CS, it needs votes from $P_1$ and $P_2$. If $P_3$ wants the CS simultaneously, it needs votes from $P_3$ and $P_1$. Since $P_1$ can only vote once, either $P_1$ gets its own vote and enters, or $P_3$ gets $P_1$'s vote. They cannot both enter, guaranteeing mutual exclusion.

## Applications & Use Cases
- **Distributed Quorum Consensus:** Maekawa's algorithm is a foundational mathematical concept for modern quorum-based systems (like Apache Cassandra's read/write quorums or Paxos/Raft leader election protocols), where gaining agreement from a mathematical subset (a quorum) is sufficient to proceed, drastically reducing network traffic compared to requiring full cluster consensus.

## 3 Solved Numerical/Analytical Examples

**Example 1: Calculating optimal set size**
*Problem:* For a distributed system with $N = 73$ nodes, what is the optimal size of a voting set $K$ in Maekawa's algorithm?
*Solution:*
1. In the optimal configuration to minimize overhead, $K \approx \sqrt{N}$.
2. $K \approx \sqrt{73} \approx 8.54$.
*Conclusion:* A voting set size of exactly $K=9$ would be optimal.

**Example 2: Message Complexity Calculation**
*Problem:* Calculate the exact message complexity per CS entry/exit lifecycle in Maekawa's optimal algorithm.
*Solution:*
Let the optimal voting set size be $K \approx \sqrt{N}$.
1. **Request:** Send a `REQUEST` to all $K$ members: $K$ messages.
2. **Reply:** Receive a `REPLY` from all $K$ members: $K$ messages.
3. **Release:** Send a `RELEASE` to all $K$ members upon exit: $K$ messages.
*Conclusion:* Total messages = $3K$. Since $K \approx \sqrt{N}$, the asymptotic message complexity is $O(\sqrt{N})$.

**Example 3: Deadlock Susceptibility**
*Problem:* Can Maekawa's algorithm deadlock?
*Solution:*
1. Yes. Consider the $N=3$ example: $V_1 = \{1, 2\}$, $V_2 = \{2, 3\}$, $V_3 = \{3, 1\}$.
2. If all three request the CS simultaneously:
   - $P_1$ votes for itself ($P_1$).
   - $P_2$ votes for itself ($P_2$).
   - $P_3$ votes for itself ($P_3$).
3. Now $P_1$ waits for $P_2$'s vote. $P_2$ waits for $P_3$'s vote. $P_3$ waits for $P_1$'s vote. 
*Conclusion:* A circular wait (deadlock) occurs. Maekawa's original paper required complex timestamp-based `INQUIRE` and `RELINQUISH` messages to resolve this.

## Previous Year Questions & Solutions

**[April 2018] Describe Maekawa's voting algorithm. Calculate its message complexity. (8 marks)**
*Solution:*
**Algorithm Description (4 marks):**
Maekawa's algorithm is a quorum-based, permission-based distributed mutual exclusion algorithm. Instead of requiring permission from all nodes in the system, a node only needs permission from a specific mathematical subset of nodes called its "Voting Set" ($V_i$).
The algorithm enforces a critical rule to guarantee safety: **The intersection of any two voting sets cannot be empty** ($V_i \cap V_j \neq \emptyset$).
Because every node can only cast one vote at a time, the intersecting node prevents any two processes from receiving enough votes to enter the Critical Section (CS) simultaneously, guaranteeing mutual exclusion.
- **To enter CS:** Process $P_i$ multicasts a `REQUEST` to all members of its voting set $V_i$. It enters the CS only after receiving a `REPLY` (a vote) from every single member.
- **Voting:** A node receiving a `REQUEST` sends a `REPLY` only if it hasn't voted for someone else yet. Otherwise, it queues the request.
- **To exit CS:** $P_i$ sends a `RELEASE` message to all members of $V_i$, allowing them to cast their votes for the next queued request.

**Message Complexity Calculation (4 marks):**
In the optimal configuration of Maekawa's algorithm, the size of each voting set is approximately $K \approx \sqrt{N}$, where $N$ is the total number of processes.
To execute a single critical section lifecycle, a process must perform the following:
1. Send a `REQUEST` message to all $K$ members of its voting set: **$K$ messages**.
2. Receive a `REPLY` message from all $K$ members of its voting set: **$K$ messages**.
3. Send a `RELEASE` message to all $K$ members of its voting set upon exiting: **$K$ messages**.
Total messages per CS execution = $K + K + K = 3K$.
Substituting $K = \sqrt{N}$, the message complexity is **$O(\sqrt{N})$** (specifically $3\sqrt{N}$). This is a massive improvement over $O(N)$ algorithms (like Ricart-Agrawala) for large-scale distributed systems.
