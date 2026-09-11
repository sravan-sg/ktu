# Transactions in Distributed Environments

## Explanation

In distributed systems, applications frequently need to update data spread across multiple independent servers. A **transaction** is a mechanism that groups a sequence of read and write operations into a single, indivisible logical unit of work. 

According to **Tanenbaum (Chapter 1 & 8)**, transactions are manipulated using standard primitives (e.g., `BEGIN_TRANSACTION`, `END_TRANSACTION`, `ABORT_TRANSACTION`, `READ`, `WRITE`) and must rigorously satisfy the **ACID properties**:

1. **Atomicity:** "All or nothing." Either all operations within the transaction execute to completion, or none do. If a failure occurs before `END_TRANSACTION`, the system executes an `ABORT_TRANSACTION` and all partial changes vanish as if they never happened.
2. **Consistency:** A transaction guarantees that it will take the system from one valid, consistent state to another valid state, never leaving invariants broken (e.g., in a banking transfer, the total money across accounts must remain constant).
3. **Isolation:** Concurrent transactions do not interfere with each other. If multiple transactions execute concurrently, the final result must be identical to if they had executed sequentially in some unspecified order (known as **serializability**).
4. **Durability (Permanence):** Once a transaction commits, its effects are permanent and must survive any subsequent system failures, usually by writing logs to persistent storage.

### Transaction Processing (TP) Monitors
Tanenbaum notes that coordinating transactions across distributed servers is extremely complex. Rather than forcing application developers to implement this, distributed systems use a **Transaction Processing Monitor (TP Monitor)**. The TP Monitor acts as a middleware component that tracks the state of distributed subtransactions and enforces the **Distributed Commit Protocol** (like Two-Phase Commit) to ensure atomicity across the network.

## Example

Consider a distributed system handling a trip reservation involving a flight booking server and a hotel booking server.

**Client Code:**
```text
BEGIN_TRANSACTION
    READ  flight_db for Flight 101
    WRITE flight_db (Reserve seat)
    READ  hotel_db  for Hotel Alpha
    WRITE hotel_db  (Reserve room)
END_TRANSACTION
```

- **Atomicity:** If the flight is booked but the hotel database crashes before the reservation is made, the TP Monitor aborts the entire transaction. The flight reservation is automatically rolled back.
- **Isolation:** If another user queries the flight database while this transaction is active (but not yet committed), they will not see the temporarily reserved seat until `END_TRANSACTION` succeeds.

## Applications & Use Cases

- **Financial Systems:** Core banking, stock trading platforms, and payment gateways strictly rely on distributed transactions and TP Monitors to ensure money is accurately debited and credited across different database shards.
- **E-commerce Inventory:** When a user buys an item, a transaction must deduct from inventory and process payment simultaneously. If the payment fails, the inventory deduction must be rolled back.
- **Cloud Databases (e.g., Google Spanner):** Modern distributed databases implement massive-scale transactions utilizing synchronized atomic clocks (TrueTime) to assign precise timestamps, guaranteeing strict serializability across globally distributed datacenters.

## 3 Solved Numerical/Analytical Examples

**Example 1: Analyzing Conflict Serializability**
*Problem:* Given two transactions:
`T1: Read(X), Write(X)`
`T2: Read(X), Write(X)`
And the following schedule: `S: Read1(X), Read2(X), Write1(X), Write2(X)`. Is this schedule conflict serializable?
*Solution:*
1. Identify conflicting operations (where at least one operation is a Write on the same data item):
   - `Read1(X)` conflicts with `Write2(X)` -> `T1` must precede `T2` (`T1 -> T2`).
   - `Read2(X)` conflicts with `Write1(X)` -> `T2` must precede `T1` (`T2 -> T1`).
2. Because there is a cycle in the precedence graph (`T1 -> T2` and `T2 -> T1`), the schedule is **not** conflict serializable. 
*Conclusion:* This is a classic "lost update" anomaly violating the Isolation property.

**Example 2: The Dirty Read Problem**
*Problem:* Explain the "Dirty Read" problem in the context of ACID properties.
*Solution:*
1. A dirty read occurs when Transaction `T1` modifies a data item, and then Transaction `T2` reads that modified item *before* `T1` commits. 
2. If `T1` subsequently aborts and rolls back its changes, `T2` has read data that "never officially existed." 
*Conclusion:* This violates the **Isolation** property, as the intermediate, uncommitted state of `T1` leaked to `T2`.

**Example 3: TP Monitor Two-Phase Commit Overhead**
*Problem:* A TP Monitor coordinates a transaction across 3 databases using the Two-Phase Commit (2PC) protocol. How many total messages are exchanged between the TP Monitor (coordinator) and the databases (participants) in a successful transaction?
*Solution:*
1. **Phase 1 (Voting):** Coordinator sends `VOTE_REQUEST` to 3 participants (3 messages). Participants reply with `VOTE_COMMIT` (3 messages).
2. **Phase 2 (Commit):** Coordinator sends `GLOBAL_COMMIT` to 3 participants (3 messages). Participants reply with `ACK` (3 messages).
*Conclusion:* Total messages = $3 + 3 + 3 + 3 = 12$ network messages. This highlights the high communication overhead required to guarantee Atomicity.

## Previous Year Questions & Solutions

**[April 2018] Explain the concept of transactions in a distributed environment. (6 marks)**
*Solution:*
Based on Tanenbaum's principles, a transaction in a distributed environment is a sequence of read and write operations executed as a single logical unit across multiple networked servers. Its primary purpose is to maintain data consistency in the presence of concurrent access and system failures. 

Distributed transactions are often managed by a middleware **TP Monitor** and must adhere to the ACID properties:
1. **Atomicity:** The entire distributed transaction either commits on all participating nodes or aborts on all nodes. Partial execution is forbidden, usually guaranteed via distributed commit protocols.
2. **Consistency:** The transaction moves the distributed system from one valid state to another.
3. **Isolation:** Concurrent distributed transactions do not see each other's intermediate states. This is typically achieved using concurrency control mechanisms like locking.
4. **Durability:** Once the transaction commits, its effects are permanently saved on persistent storage across the participating nodes.

**[April 2018] State the conditions for conflict serializability. (4 marks)**
*Solution:*
A schedule of concurrent transactions is **conflict serializable** if it produces the same result as some purely serial execution of those same transactions. 
Two operations conflict if:
1. They belong to different transactions.
2. They access the same data item.
3. At least one of the operations is a Write.

The condition for a schedule to be conflict serializable is that its **Precedence Graph (Serialization Graph) must be acyclic**. To build the graph, draw a directed edge from $T_i$ to $T_j$ if an operation in $T_i$ conflicts with and executes before a subsequent operation in $T_j$. If the resulting graph contains no cycles, the schedule is conflict serializable and therefore guarantees strict isolation.
