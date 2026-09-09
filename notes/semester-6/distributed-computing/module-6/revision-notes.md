# Module 6: Mutual Exclusion & Election - Revision Notes

## 1. Quick Summary
Module 6 addresses two foundational problems in distributed systems: how to restrict access to a shared resource to one node at a time (Distributed Mutual Exclusion), and how to choose a new coordinator when the current one fails (Leader Election). It covers three mutual exclusion algorithms (Central Server, Ring-based, Maekawa's Voting) and two election algorithms (Ring-based, Bully).

## 2. Key Definitions & Formulas
*   **Mutual Exclusion Requirements:** Safety (only one in CS), Liveness (no deadlock/starvation), Ordering (fairness).
*   **Central Server Algorithm:** 3 messages per CS entry (Request, Grant, Release). Single point of failure.
*   **Ring-based Algorithm (Mutual Exclusion):** Token circulates in a logical ring. Hold token to enter CS. High synchronization delay, constant network load even when idle.
*   **Maekawa's Voting Algorithm:** Quorum-based. A node needs votes from its Voting Set ($V_i$) to enter CS. Rule: $V_i \cap V_j \neq \emptyset$. Optimal set size $K \approx \sqrt{N}$. Message complexity = $3\sqrt{N}$. Prone to deadlock without timestamps.
*   **Ring-based Election:** `ELECTION` message circulates. Nodes replace ID if theirs is higher. Highest ID makes a full circle to win. Message complexity: $2N$.
*   **Bully Algorithm:** Node with highest ID forces others to step down. Sends `ELECTION` to higher IDs. If no `OK` replies, it wins. Worst-case message complexity: $O(N^2)$ (cascade effect). Best-case: $O(N)$.

## 3. Top Exam Focus Areas (PYQ Patterns)
1.  **Bully vs Ring Election:** Extremely common to ask for a comparison. Contrast their topology (fully connected vs ring) and message complexity ($O(N^2)$ worst case vs strictly $2N$). (6 marks, April 2018)
2.  **Maekawa's Complexity:** Be able to calculate the message complexity ($3\sqrt{N}$) and explain *why* it's calculated that way (Request + Reply + Release for $\sqrt{N}$ members). (8 marks, April 2018)
3.  **Central Server Mechanism:** Explain the queueing mechanism and the 3 distinct messages used. (4 marks, April 2018)
4.  **Ring Mutual Exclusion vs Election:** Do not confuse the token-passing algorithm for mutual exclusion with the ID-replacing algorithm for election, even though both use a ring topology.

## 4. Most Common Mistakes & Tips
*   **Message Complexity Calculation:** When asked for message complexity, break it down step-by-step (e.g., "To request, it sends X messages..."). Don't just write "$O(N)$".
*   **Maekawa's Intersection Rule:** The most important detail to remember for Maekawa's is that the intersection of any two sets cannot be empty. This is the entire basis for its safety guarantee.
*   **Bully's Cascade:** The reason the Bully algorithm has $O(N^2)$ worst-case complexity is because every node that replies `OK` *also* starts its own election. It's not just one round of messages; it's a branching cascade.