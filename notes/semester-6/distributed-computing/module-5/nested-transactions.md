# Nested Transactions

## Explanation
A **Nested Transaction** is an extension of the traditional flat transaction model. According to **Tanenbaum (Chapter 1)**, in distributed systems, transactions are often constructed as a number of subtransactions, jointly forming a hierarchical *nested transaction*. 

A top-level transaction can fork off child subtransactions that run in parallel with one another, often on completely different machines. This provides two main architectural benefits:
1. **Finer-grained fault tolerance:** If a subtransaction fails, it can abort and roll back its local changes without forcing the entire top-level transaction to abort. The parent transaction can choose to handle the failure by retrying the subtransaction, attempting an alternative action, or explicitly aborting itself.
2. **Performance through Concurrency:** Subtransactions belonging to the same parent can execute in parallel, significantly improving performance for complex, logically divided tasks.

### Commit and Abort Semantics (The "Private Universe")
Tanenbaum describes the semantics of nested transactions using the concept of a "private universe":
- **Execution:** When any subtransaction starts, it is conceptually given a private copy of all data in the entire system to manipulate.
- **Provisional Commit:** If a subtransaction finishes successfully, it *commits* its private universe, which then replaces the parent's universe. This makes its results visible to the parent transaction (and subsequently spawned sibling subtransactions). However, these changes are **not yet durable or visible to the outside world**.
- **Parent Abort:** If an enclosing (higher-level) transaction aborts, all its underlying subtransactions have to be aborted as well, *even those that already provisionally committed*. The permanence of the ACID 'Durability' property applies **only** to the absolute top-level root transaction.

## Example
Tanenbaum provides a classic example: a distributed travel booking system orchestrating a trip.
**Top-Level Transaction T (Plan a Trip):**
- **Subtransaction T1 (Book Flight 1):** Queries airline A and reserves a seat.
- **Subtransaction T2 (Book Flight 2):** Queries airline B and reserves a seat.
- **Subtransaction T3 (Book Flight 3):** Queries airline C.
  - **Subtransaction T3.1 (Try Airline C):** Attempts booking. If full, it aborts.
  - **Subtransaction T3.2 (Try Airline D):** Attempts alternative booking. Succeeds.

If T3.1 fails, it doesn't ruin the whole trip booking. The parent T3 catches the abort and tries T3.2. If the user's credit card is declined at the very end, the top-level T aborts, and T1, T2, and T3.2 are all rolled back, despite having previously "committed" their private universes to the parent.

## Applications & Use Cases
- **Workflow Orchestration:** Complex business processes (like order fulfillment, which involves billing, inventory, and shipping) are modeled as nested transactions so that a failure in a minor step (like sending a confirmation email) doesn't roll back the payment processing.
- **Distributed Databases with Replication:** Updating a replicated database can be a top-level transaction, with updates to individual replicas acting as concurrent subtransactions. If one replica fails, the parent might still commit if a majority quorum is reached.
- **Microservices Architectures:** When a service calls multiple downstream microservices, encapsulating those calls as subtransactions allows the calling service to handle localized downstream failures gracefully without catastrophic system-wide rollbacks.

## 3 Solved Numerical/Analytical Examples

**Example 1: Ancestor Abort**
*Problem:* Transaction T has children T1 and T2. T1 has child T1A. T1A commits provisionally. Later, T1 aborts. What is the status of T1A's changes?
*Solution:*
1. According to nested transaction semantics, if an enclosing transaction aborts, all its underlying subtransactions must abort.
2. Because the parent (T1) aborted, all of its descendants are also aborted, regardless of their individual provisional commit status. 
*Conclusion:* T1A's changes vanish as if it never existed.

**Example 2: Outside Visibility**
*Problem:* Transaction T spawns subtransactions T1 and T2. Both T1 and T2 provisionally commit. Then T aborts. Are the changes visible to a completely separate, concurrent transaction T3?
*Solution:*
1. In nested transactions, changes are only made durable and visible to the outside world (like T3) when the absolute top-level transaction (T) commits. 
2. Since T aborted, the provisional commits of T1 and T2 are completely undone. 
*Conclusion:* No, T3 will see the original, unmodified state of the data.

**Example 3: Lock Inheritance**
*Problem:* Explain lock inheritance in nested transactions. If parent T holds a read lock on object X, can child T1 get a write lock on X?
*Solution:*
1. Nested transactions utilize a mechanism called *lock inheritance*. 
2. A child transaction can acquire a lock on an object if its parent holds a compatible lock (or if the parent holds the *same* lock). The child effectively borrows the lock from its parent's "universe."
*Conclusion:* Yes, T1 can upgrade to a write lock on X. However, the parent T cannot see T1's locked modifications until T1 provisionally commits and passes the updated universe and lock back up to the parent.

## Previous Year Questions & Solutions

**[April 2018] What are nested transactions? (4 marks)**
*Solution:*
According to Tanenbaum, a nested transaction is a transaction model where a main, top-level transaction is logically divided and broken down into a hierarchy of subtransactions. 
Key characteristics include:
1. **Hierarchy:** Transactions form a tree structure. The root is the top-level transaction, and the branches are subtransactions, which can be executed across different machines.
2. **Concurrency:** Subtransactions of the same parent can run in parallel, increasing performance.
3. **Independent Recovery:** A subtransaction can fail and abort without forcing its parent or siblings to abort. The parent can handle the failure by retrying or invoking an alternative subtransaction.
4. **Provisional Commits (Private Universes):** When a subtransaction completes, it only "provisionally" commits. Its results are passed to its parent's private universe but are not made durable. The changes only become permanent and visible to the outside world when the top-level root transaction successfully commits. If any ancestor aborts, all provisionally committed descendants are rolled back.
