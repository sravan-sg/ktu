# Transactions in Distributed Environments

## Explanation
A **transaction** is a sequence of read and write operations on data objects that are executed as a single, indivisible logical unit of work. In a distributed environment, where data might be spread across multiple servers, ensuring the integrity of these operations becomes significantly more complex.

Transactions must satisfy the **ACID properties**:
-   **Atomicity:** "All or nothing." Either all operations within the transaction complete successfully and are committed to the database, or none are. If a failure occurs midway, the transaction is aborted and any partial changes are rolled back.
-   **Consistency:** The transaction must take the system from one valid state to another valid state, maintaining all defined invariants and constraints.
-   **Isolation:** Concurrent transactions must not interfere with each other. The intermediate state of a transaction should be invisible to other concurrent transactions. 
-   **Durability:** Once a transaction commits, its changes are permanent and must survive any subsequent system failures (e.g., power loss).

### Conflict Serializability
To maintain *Isolation*, systems must carefully interleave operations from concurrent transactions. Two operations from different transactions **conflict** if they operate on the same data item and at least one of them is a write. 
An interleaved execution (schedule) of concurrent transactions is **conflict serializable** if it can be transformed into a serial execution (running one transaction completely after another) by swapping non-conflicting adjacent operations. If a schedule is conflict serializable, it guarantees that concurrent execution produces the exact same results as if the transactions had executed sequentially, thereby preserving isolation.

## Example
Consider a simple banking transfer from Account A to Account B.
**Transaction T1 (Transfer $100 from A to B):**
1. Read(A)
2. A = A - 100
3. Write(A)
4. Read(B)
5. B = B + 100
6. Write(B)

If the system crashes after step 3, *Atomicity* ensures that the withdrawal from A is rolled back, preventing money from disappearing. If another transaction tries to read A's balance between steps 3 and 6, *Isolation* ensures it doesn't see the intermediate (inconsistent) state.

## Applications & Use Cases
-   **Financial Systems:** Core banking systems, stock trading platforms, and payment gateways strictly rely on distributed transactions to ensure money is accurately debited and credited across different geographical database shards.
-   **E-commerce Inventory:** When a user buys an item, a transaction must deduct from inventory and process payment simultaneously. If the payment fails, the inventory deduction must be rolled back to prevent overselling.
-   **Airline Reservation Systems:** Ensuring that the same seat is not double-booked by two customers clicking "Purchase" at the exact same millisecond requires strict transactional isolation.

## 3 Solved Numerical/Analytical Examples
**Example 1:**
Given two transactions:
T1: Read(X), Write(X)
T2: Read(X), Write(X)
And the following schedule: 
`S: Read1(X), Read2(X), Write1(X), Write2(X)`
Is this schedule conflict serializable?
*Solution:*
Identify conflicting operations:
- Read1(X) conflicts with Write2(X) -> T1 must precede T2 (T1 -> T2)
- Read2(X) conflicts with Write1(X) -> T2 must precede T1 (T2 -> T1)
Because there is a cycle in the precedence graph (T1 -> T2 and T2 -> T1), the schedule is **not** conflict serializable. This is a classic "lost update" anomaly.

**Example 2:**
Explain the "Dirty Read" problem in the context of ACID properties.
*Solution:*
A dirty read occurs when Transaction T1 modifies a data item, and then Transaction T2 reads that modified item *before* T1 commits. If T1 subsequently aborts and rolls back its changes, T2 has read data that "never officially existed." This violates the **Isolation** property.

**Example 3:**
How does a Two-Phase Commit (2PC) protocol ensure Atomicity in a distributed transaction involving a coordinator and three participant nodes?
*Solution:*
1.  **Phase 1 (Voting):** The coordinator asks all 3 participants if they are prepared to commit. Each node writes changes to a local log and replies "Yes" or "No".
2.  **Phase 2 (Commit/Abort):** If *all* 3 nodes replied "Yes", the coordinator sends a "Commit" message to all. If *any* node replied "No" (or timed out), the coordinator sends an "Abort" message to all. This guarantees "All or Nothing" (Atomicity) across the distributed system.

## Previous Year Questions & Solutions

**[April 2018] Explain the concept of transactions in a distributed environment. (6 marks)**
*Solution:*
A transaction in a distributed environment is a sequence of data operations executed as a single logical unit across multiple networked servers. Its primary purpose is to maintain data consistency in the presence of concurrent access and system failures. 
Distributed transactions must adhere to the ACID properties:
1.  **Atomicity:** The entire distributed transaction either commits on all participating nodes or aborts on all nodes. Partial execution is not allowed. (Usually implemented via Two-Phase Commit).
2.  **Consistency:** The transaction moves the distributed system from one valid state to another, respecting all database constraints.
3.  **Isolation:** Concurrent distributed transactions do not see each other's intermediate states. This is typically achieved using locks or timestamps.
4.  **Durability:** Once the transaction is reported as committed, its effects are permanently saved on disk across the participating nodes, surviving subsequent node crashes.

**[April 2018] State the conditions for conflict serializability. (4 marks)**
*Solution:*
A schedule of concurrent transactions is **conflict serializable** if it produces the same result as some purely serial execution of those same transactions. The conditions for conflict serializability are based on identifying conflicting operations. 
Two operations conflict if:
1. They belong to different transactions.
2. They access the same data item.
3. At least one of the operations is a Write.

The condition for a schedule to be conflict serializable is that its **Precedence Graph (Serialization Graph) must be acyclic**. 
To build the graph:
- Draw a node for each transaction.
- Draw a directed edge from Ti to Tj if an operation in Ti conflicts with a subsequent operation in Tj.
If the resulting graph contains no cycles, the schedule is conflict serializable and therefore guarantees isolation.
