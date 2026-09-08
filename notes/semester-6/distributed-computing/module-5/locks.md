# Locks and Two-Phase Locking

## Explanation
**Locks** are the most common mechanism used to implement concurrency control and ensure isolation in database and distributed systems. Before a transaction can access a data item, it must acquire a lock on it from a Lock Manager. 

### Types of Locks
-   **Shared Lock (Read Lock):** If a transaction wants to read a data item, it requests a shared lock. Multiple transactions can hold shared locks on the same data item simultaneously, as reading does not alter data.
-   **Exclusive Lock (Write Lock):** If a transaction wants to write to a data item, it must acquire an exclusive lock. Only one transaction can hold an exclusive lock on an item at a time. If an exclusive lock is held, no other transaction can acquire either a shared or an exclusive lock.

### Two-Phase Locking Protocol (2PL)
While locks prevent simultaneous access, simply locking and unlocking randomly does not guarantee conflict serializability. To guarantee serializability, systems use the **Two-Phase Locking (2PL)** protocol. Under 2PL, a transaction must execute in two distinct phases:
1.  **Growing Phase:** The transaction acquires locks on data items as needed but cannot release *any* locks.
2.  **Shrinking Phase:** Once the transaction releases its first lock, it enters the shrinking phase. In this phase, it can release locks but cannot acquire any *new* locks.

**Strict 2PL:** A widely used variant where the shrinking phase is delayed until the very end. The transaction holds all its exclusive locks until it completely commits or aborts. This prevents "cascading aborts" (where one transaction aborts, forcing others that read its uncommitted data to also abort).

## Example
**Strict 2PL in Action:**
Transaction T1 needs to move $50 from Account A to Account B.
1.  T1 requests **Exclusive Lock(A)**. Granted.
2.  T1 reads A, calculates A-50, writes A.
3.  T1 requests **Exclusive Lock(B)**. Granted.
4.  T1 reads B, calculates B+50, writes B.
5.  T1 **Commits**.
6.  T1 releases **Exclusive Lock(A)** and **Exclusive Lock(B)** simultaneously.

Notice that T1 did not release Lock(A) before requesting Lock(B). This adheres to the growing phase rules of 2PL and strict 2PL.

## Applications & Use Cases
-   **Relational Databases (RDBMS):** SQL databases like PostgreSQL and MySQL heavily utilize lock managers and variants of Strict 2PL to enforce ACID isolation levels like `REPEATABLE READ` and `SERIALIZABLE`.
-   **Distributed Key-Value Stores:** Systems needing strong consistency will use distributed locking mechanisms (e.g., via ZooKeeper or Redis Redlock) to ensure only one node modifies a specific key at a time.
-   **File Systems:** Advisory and mandatory file locking mechanisms in OS and Distributed File Systems ensure multiple processes don't corrupt a file by writing concurrently.

## 3 Solved Numerical/Analytical Examples
**Example 1:**
Transaction T1 holds a Shared Lock on item X. Transaction T2 requests a Shared Lock on X. Will it be granted? What if T2 requests an Exclusive Lock?
*Solution:*
- T2 requesting Shared Lock: **Granted**. Shared locks are compatible with each other.
- T2 requesting Exclusive Lock: **Denied (Blocked)**. Exclusive locks are not compatible with any other lock. T2 must wait until T1 releases its Shared Lock.

**Example 2:**
Explain the concept of Deadlock in the context of locking.
*Solution:*
A deadlock occurs when two or more transactions are waiting for locks held by each other, creating a circular dependency. For example:
- T1 holds Exclusive Lock(A) and requests Lock(B).
- T2 holds Exclusive Lock(B) and requests Lock(A).
Neither can proceed. The lock manager must detect this cycle and abort one of the transactions to break the deadlock.

**Example 3:**
Does Two-Phase Locking (2PL) prevent deadlocks?
*Solution:*
No. 2PL guarantees *conflict serializability*, but it does not prevent deadlocks. As seen in Example 2, both T1 and T2 could be in their growing phases, acquiring locks without releasing them, leading to a circular wait. Deadlock prevention/detection mechanisms are required in addition to 2PL.

## Previous Year Questions & Solutions

**[April 2018] What are locks? Explain two phase locking protocol. (6 marks)**
*Solution:*
**Locks:**
In distributed computing and databases, a lock is a synchronization mechanism used to control concurrent access to shared data. It ensures isolation.
-   **Shared (Read) Lock:** Allows multiple transactions to read a data item concurrently but prevents any transaction from writing to it.
-   **Exclusive (Write) Lock:** Grants a single transaction exclusive rights to both read and write a data item, preventing any other transaction from accessing it.

**Two-Phase Locking (2PL) Protocol:**
2PL is a concurrency control protocol that guarantees conflict serializability of transactions. A transaction following 2PL must divide its execution into two strictly ordered phases regarding lock management:
1.  **Growing Phase:** The transaction may request and acquire new locks on data items. Crucially, during this phase, it is strictly prohibited from releasing *any* locks it currently holds.
2.  **Shrinking Phase:** Once the transaction releases its very first lock, it transitions to the shrinking phase. During this phase, it may release existing locks, but it is strictly prohibited from acquiring any *new* locks.

By adhering to 2PL, the protocol ensures that transactions cannot interleave conflicting operations in a way that creates cycles in the serialization graph, thus guaranteeing a serializable schedule. Most modern systems use *Strict 2PL*, where the shrinking phase is delayed entirely until the transaction commits or aborts, which also prevents cascading rollbacks.
