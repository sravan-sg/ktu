# Ring-Based Election Algorithm

## Explanation
In distributed systems, many algorithms rely on a central coordinator (e.g., the Central Server Algorithm for mutual exclusion). If this coordinator crashes, the remaining nodes must elect a new one. This is called a **Leader Election Algorithm**.

The **Ring-Based Election Algorithm** assumes that all nodes are arranged in a logical ring, and each node knows its immediate successor. Every node is assigned a unique identifier (ID). The goal is to elect the node with the highest ID as the new coordinator.

**How it works:**
1.  **Detecting Failure & Initiating Election:** When any process $P_i$ notices the coordinator is dead, it creates an `ELECTION` message containing its own ID ($i$) and sends it to its successor.
2.  **Passing the Message:** When a process $P_j$ receives an `ELECTION` message, it compares the ID in the message with its own ID:
    -   If the message ID > $j$: It forwards the message to its successor exactly as received.
    -   If the message ID < $j$: It replaces the message ID with its own ID ($j$) and forwards it. (Note: if $P_j$ has already forwarded an election message, it might just discard this lower one to save bandwidth).
    -   If the message ID == $j$: This means the message has circulated the entire ring and $P_j$ is the highest ID! $P_j$ declares itself the winner.
3.  **Announcing the Winner:** The winner ($P_j$) changes the message type from `ELECTION` to `COORDINATOR` (containing its ID) and circulates it around the ring once more. Every node that receives this updates its internal state to recognize $P_j$ as the new coordinator and forwards the message. When $P_j$ receives its own `COORDINATOR` message, the election is complete.

## Example
Consider a ring of 4 nodes with IDs: 10, 24, 8, 15. Node 24 is the coordinator.
- Node 24 crashes.
- Node 8 notices the crash. Node 8 sends `ELECTION(8)` to Node 15.
- Node 15 sees 8 < 15. It replaces it and sends `ELECTION(15)` to Node 10.
- Node 10 sees 15 > 10. It forwards `ELECTION(15)` to Node 8 (since 24 is dead, 10's successor is now 8).
- Node 8 sees 15 > 8. It forwards `ELECTION(15)` to Node 15.
- Node 15 receives `ELECTION(15)`. It recognizes its own ID. It is the winner!
- Node 15 circulates a `COORDINATOR(15)` message to inform everyone.

## Applications & Use Cases
-   **Token Ring Recovery:** Historically used in token ring networks to regenerate a lost token.
-   **Cluster Management:** Simple clusters organized in logical rings use this for master node failover. It is easy to implement when network topology inherently forms a ring or when establishing TCP connections in a strict circle is feasible.

## 3 Solved Numerical/Analytical Examples
**Example 1: Multiple simultaneous elections**
What happens if two nodes, A and B, notice the coordinator crashed at the exact same time and both initiate an election?
*Solution:*
Two `ELECTION` messages will circulate. Suppose A has ID 10 and B has ID 20.
- A's message `ELECTION(10)` will eventually reach B. Since 10 < 20, B will discard it or replace it with 20.
- B's message `ELECTION(20)` will reach A. Since 20 > 10, A will forward it.
Eventually, `ELECTION(20)` will make a full circle back to B, and B will declare itself the winner. The algorithm naturally resolves simultaneous elections without conflict.

**Example 2: Message Complexity (Worst Case)**
What is the worst-case message complexity of the ring-based election algorithm for a ring of $N$ nodes?
*Solution:*
The worst case occurs when the node that initiates the election has the *lowest* ID, and the nodes are ordered such that the IDs are decreasing in the direction of message passing (e.g., initiator is 1, next is 100, then 90, 80...).
- The initiator sends `ELECTION(1)`.
- The next node (100) intercepts it and sends `ELECTION(100)`. This message must travel $N-1$ hops to return.
- In the absolute worst case of simultaneous elections started by everyone, it takes $O(N^2)$ messages because many partial `ELECTION` messages are sent before being swallowed by higher IDs. However, for a *single* initiator, it takes $N$ messages for the election round, plus $N$ messages for the coordinator announcement, totaling $2N$ messages.

**Example 3: Handling Node Recovery**
What happens if the old coordinator (Node 24 in our previous example) reboots and comes back online?
*Solution:*
When Node 24 recovers, it doesn't know who the new coordinator is. It will typically just start a new election by sending `ELECTION(24)`. Since 24 is the highest ID, it will win the election and reclaim its position as coordinator. This means the algorithm inherently supports graceful recovery of primary nodes.

## Previous Year Questions & Solutions

**[April 2018] Compare Ring-based election algorithm and Bully algorithm with examples. (6 marks)**
*(Part 1 of 2: The Bully algorithm details are covered in the next file. The comparison is provided here.)*

*Solution:*
Both algorithms aim to elect the node with the highest ID as the new coordinator when the existing one fails.

**1. Topology & Knowledge:**
-   **Ring-based:** Nodes are logically organized in a ring. A node only needs to know the address of its immediate successor.
-   **Bully:** Nodes are fully connected (or at least can communicate with all others). Every node must know the IDs and addresses of *all* other nodes in the system.

**2. Election Process:**
-   **Ring-based:** An `ELECTION` message is passed sequentially around the ring. Nodes replace the ID in the message with their own if theirs is higher. The message must complete a full circle for the winner to be determined.
-   **Bully:** An initiator broadcasts an `ELECTION` message directly to all nodes with *higher* IDs. If no higher ID responds, it wins. If a higher ID responds, the initiator steps down, and the higher ID takes over the election process.

**3. Message Complexity:**
-   **Ring-based:** For a single initiator, it takes exactly $2N$ messages ($N$ for the election phase, $N$ for the coordinator announcement phase). It is consistent and predictable.
-   **Bully:** In the worst-case scenario (where the node with the lowest ID initiates), the message complexity is $O(N^2)$ because it triggers a cascade of elections from every higher-numbered node. However, if the node with the second-highest ID initiates, it only takes $O(N)$ messages.

**Example Comparison:**
If Node 10 detects a failure:
- In the **Ring**, Node 10 sends a single message to Node 11. Node 11 passes it to 12, etc., until it loops back.
- In the **Bully**, Node 10 sends messages directly to Nodes 11, 12, 13, 14, and 15 simultaneously, waiting for any of them to reply "I'm taking over."
