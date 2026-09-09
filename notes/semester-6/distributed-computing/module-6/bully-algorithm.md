# Bully Algorithm

## Explanation
The **Bully Algorithm** (devised by Garcia-Molina) is a classic leader election algorithm used in distributed systems where nodes can directly communicate with each other (a fully connected network, or one where every node knows the IP of every other node). 

It earns its name because the node with the highest ID "bullies" all other nodes into submission, forcing them to accept it as the new coordinator.

**Assumptions:**
- Every process knows the unique ID and network address of every other process.
- Processes can fail and recover.
- Message delivery is reliable, and timeouts are used to detect failures.

**How it works:**
1.  **Initiation:** When a process $P$ notices that the coordinator is no longer responding, it initiates an election.
2.  **The Bullying Phase:** Process $P$ sends an `ELECTION` message to all processes that have an ID *strictly greater* than its own.
3.  **Waiting for Replies:** 
    -   If $P$ receives no `OK` (or `ANSWER`) messages from any higher-ID processes within a timeout period, it assumes all higher-ID processes are dead. $P$ wins by default! It broadcasts a `COORDINATOR` message to all lower-ID processes to announce its victory.
    -   If $P$ *does* receive an `OK` message from one or more higher-ID processes, it means a higher-ID process is alive and taking over the election. Process $P$ steps down and simply waits to receive the final `COORDINATOR` message.
4.  **Taking Over:** When a higher-ID process $Q$ receives an `ELECTION` message from $P$, it sends an `OK` back to $P$ (telling $P$ to step down). Then, $Q$ immediately starts its own election by sending `ELECTION` messages to all processes with IDs higher than $Q$'s. This cascade continues until the absolute highest alive node is reached.

## Example
Consider a system with 5 nodes: IDs 1, 2, 3, 4, 5. Node 5 is the coordinator.
- Node 5 crashes.
- Node 2 notices the crash and starts an election.
- Node 2 sends `ELECTION` to nodes 3, 4, and 5.
- Nodes 3 and 4 are alive, so they both reply `OK` to Node 2. Node 2 steps down.
- Node 3 and Node 4 now both start their own elections.
- Node 3 sends `ELECTION` to 4 and 5.
- Node 4 replies `OK` to Node 3. Node 3 steps down.
- Node 4 sends `ELECTION` to 5.
- Node 5 is dead, so it doesn't reply.
- Node 4 times out. Node 4 realizes it is the highest alive ID.
- Node 4 broadcasts `COORDINATOR(4)` to nodes 1, 2, and 3.

## Applications & Use Cases
-   **Database Clusters:** Used in systems like MongoDB (for replica set elections) or Elasticsearch, where the cluster size is relatively small (making the $O(N^2)$ message complexity manageable) and the network is fully connected.
-   **High Availability (HA) Pairs:** When two routers or firewalls operate in an active-standby pair, they use a simplified bully-like mechanism to determine who is active if the link between them fails.

## 3 Solved Numerical/Analytical Examples
**Example 1: Best-case message complexity**
What is the best-case scenario for the Bully Algorithm, and what is its message complexity?
*Solution:*
The best-case scenario occurs when the node with the *second-highest* ID detects the coordinator's failure and initiates the election.
Suppose Node $N-1$ detects the failure of Node $N$.
- Node $N-1$ sends an `ELECTION` message to Node $N$. (1 message)
- Node $N$ is dead, so no reply.
- Node $N-1$ times out and broadcasts `COORDINATOR` to the remaining $N-2$ nodes. ($N-2$ messages).
Total messages = $1 + (N-2) = N-1$ messages. Therefore, the best-case message complexity is $O(N)$.

**Example 2: Worst-case message complexity**
What is the worst-case message complexity?
*Solution:*
The worst-case occurs when the node with the *lowest* ID (e.g., Node 1) initiates the election.
- Node 1 sends $N-1$ `ELECTION` messages. It receives $N-2$ `OK` replies.
- Node 2 sends $N-2$ `ELECTION` messages. It receives $N-3$ `OK` replies.
- ...and so on.
This creates a cascade of elections. The total number of messages scales with the sum of an arithmetic progression: $(N-1) + (N-2) + ... + 1$, which equals $N(N-1)/2$.
Therefore, the worst-case message complexity is $O(N^2)$. This makes the Bully algorithm highly inefficient for very large clusters.

**Example 3: Node Recovery (The Bully behavior)**
What happens when a previously crashed coordinator (Node 5) recovers?
*Solution:*
As soon as Node 5 boots up, it doesn't bother asking who the coordinator is. Because it has the highest ID, it immediately acts like a "bully." It broadcasts a `COORDINATOR(5)` message to all other nodes (or initiates an election which it guarantees to win). The current coordinator (Node 4) receives this and is forced to step down immediately.

## Previous Year Questions & Solutions

**[April 2018] Explain the bully algorithm for election. (4 marks)**
*Solution:*
The Bully Algorithm is used to elect a new coordinator in a distributed system where every node knows the ID and address of every other node. It relies on the principle that the node with the highest ID always wins.
1.  When a process $P$ detects the coordinator has failed, it sends an `ELECTION` message to all processes with IDs higher than its own.
2.  If $P$ receives no responses before a timeout, it assumes it is the highest-ID alive node. It declares itself the winner and sends a `COORDINATOR` message to all lower-ID nodes.
3.  If $P$ receives an `OK` message from any higher-ID node, it means a larger node is alive and taking over. $P$ steps down and waits.
4.  Any node that replied `OK` to $P$ then starts its own election by sending `ELECTION` messages to nodes higher than itself. This process repeats until the highest alive node times out and claims victory. 
It is called the "Bully" algorithm because a recovering node with a high ID will immediately depose the current coordinator and take over.

**[April 2018] Compare Ring-based election algorithm and Bully algorithm with examples. (6 marks)**
*(Part 2 of 2: See `election-ring-based-election-algorithm.md` for the full comparison).*
