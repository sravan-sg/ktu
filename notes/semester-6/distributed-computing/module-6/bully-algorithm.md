# Bully Algorithm

## Explanation
The **Bully Algorithm**, devised by Garcia-Molina (1982) and extensively detailed in **Tanenbaum (Chapter 6)**, is a classic leader election algorithm used in distributed systems where nodes can directly communicate with each other (a fully connected network). 

It earns its name because the algorithm guarantees that the running process with the highest ID always wins the election and "bullies" all other nodes into submission, forcing them to accept it as the new coordinator.

**Assumptions:**
- Every process $P_k$ has a unique identifier (e.g., $id(P_k) = k$) and knows the network address of every other process.
- Processes can fail and recover.
- Message delivery is reliable, and timeouts are used to detect crash failures.

**How it works:**
1. **Initiation:** When any process $P$ notices that the current coordinator is no longer responding, it initiates an election.
2. **The Bullying Phase:** Process $P$ sends an `ELECTION` message to all processes that have an ID *strictly greater* than its own.
3. **Waiting for Replies:** 
   - If $P$ receives no `OK` messages from any higher-ID processes within a timeout period, it assumes all higher-ID processes are dead. $P$ wins by default! It broadcasts a `COORDINATOR` message to all lower-ID processes to announce its victory.
   - If $P$ *does* receive an `OK` message from one or more higher-ID processes, it means a higher-ID process is alive and is taking over the election. Process $P$ immediately steps down and simply waits to receive the final `COORDINATOR` message.
4. **Taking Over:** When a higher-ID process $Q$ receives an `ELECTION` message from $P$, it sends an `OK` back to $P$ (telling $P$ to stop). Then, $Q$ immediately holds its own election by sending `ELECTION` messages to all processes with IDs higher than $Q$'s. This cascade continues until the absolute highest alive node is reached.

## Example
Tanenbaum provides an example with 8 processes (IDs 0 to 7). Process 7 was the coordinator but has just crashed.
1. Process 4 is the first to notice the crash. It holds an election by sending `ELECTION` messages to 5, 6, and 7.
2. Processes 5 and 6 are alive and both respond with `OK`, telling 4 to stop. Process 4 sits back and waits.
3. Now, 5 and 6 each hold an election.
   - Process 5 sends `ELECTION` to 6 and 7.
   - Process 6 sends `ELECTION` to 7.
4. Process 6 responds `OK` to Process 5, telling 5 to stop.
5. Process 6 receives no response from 7 (since 7 is dead). Process 6 times out and wins.
6. Process 6 broadcasts a `COORDINATOR` message to all lower-numbered processes (0 through 5).

## Applications & Use Cases
- **Database Clusters:** Used in systems like MongoDB (for replica set primary elections) or Elasticsearch, where the cluster size is relatively small (making the $O(N^2)$ message complexity manageable) and the network is fully connected.
- **High Availability (HA) Pairs:** When two routers or firewalls operate in an active-standby pair, they use a simplified bully-like mechanism to determine who is active if the heartbeat link between them fails.

## 3 Solved Numerical/Analytical Examples

**Example 1: Best-case message complexity**
*Problem:* What is the best-case scenario for the Bully Algorithm, and what is its message complexity?
*Solution:*
1. The best-case scenario occurs when the node with the *second-highest* ID detects the coordinator's failure and initiates the election.
2. Suppose Node $N-1$ detects the failure of Node $N$.
3. Node $N-1$ sends exactly one `ELECTION` message to Node $N$. (1 message)
4. Node $N$ is dead, so no reply.
5. Node $N-1$ times out and broadcasts `COORDINATOR` to the remaining $N-2$ nodes. ($N-2$ messages).
*Conclusion:* Total messages = $1 + (N-2) = N-1$ messages. Therefore, the best-case message complexity is $O(N)$.

**Example 2: Worst-case message complexity**
*Problem:* What is the worst-case message complexity?
*Solution:*
1. The worst-case occurs when the node with the *lowest* ID (e.g., Node 1) initiates the election.
2. Node 1 sends $N-1$ `ELECTION` messages. It receives $N-2$ `OK` replies.
3. Node 2 sends $N-2$ `ELECTION` messages. It receives $N-3$ `OK` replies.
4. This creates a cascade of elections. The total number of messages scales with the sum of an arithmetic progression: $(N-1) + (N-2) + \dots + 1$, which equals $N(N-1)/2$.
*Conclusion:* Therefore, the worst-case message complexity is $O(N^2)$. This makes the Bully algorithm highly inefficient for very large clusters.

**Example 3: Node Recovery (The Bully behavior)**
*Problem:* What happens when a previously crashed coordinator (Node 7) recovers while Node 6 is currently acting as the coordinator?
*Solution:*
1. According to Tanenbaum, if a process that was previously down comes back up, it automatically holds an election.
2. As soon as Node 7 boots up, it sends `ELECTION` messages to higher nodes (none exist).
3. Node 7 immediately wins and sends a `COORDINATOR` message to all others.
*Conclusion:* Node 7 bullies Node 6 into submission, deposing it immediately. Thus, the biggest guy in town always wins.

## Previous Year Questions & Solutions

**[April 2018] Explain the bully algorithm for election. (4 marks)**
*Solution:*
The Bully Algorithm is used to elect a new coordinator in a distributed system where every node knows the ID and address of every other node. It relies on the principle that the node with the highest ID always wins.
1. When a process $P$ detects the coordinator has failed, it sends an `ELECTION` message to all processes with IDs higher than its own.
2. If $P$ receives no responses before a timeout, it assumes it is the highest-ID alive node. It declares itself the winner and sends a `COORDINATOR` message to all lower-ID nodes.
3. If $P$ receives an `OK` message from any higher-ID node, it means a larger node is alive and taking over. $P$ steps down and waits.
4. Any node that replied `OK` to $P$ then starts its own election by sending `ELECTION` messages to nodes higher than itself. This cascade repeats until the highest alive node times out and claims victory. 
It is called the "Bully" algorithm because a recovering node with a high ID will immediately depose the current coordinator and take over.

**[April 2018] Compare Ring-based election algorithm and Bully algorithm with examples. (6 marks)**
*(Part 2 of 2: See `ring-based-algorithm.md` for the full comparison).*
