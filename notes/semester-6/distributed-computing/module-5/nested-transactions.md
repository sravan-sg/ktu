# Nested Transactions

## Explanation
A **Nested Transaction** is a transaction model that extends the traditional flat transaction model. In a nested transaction, a top-level transaction can spawn multiple sub-transactions (or child transactions). These sub-transactions can, in turn, spawn their own sub-transactions, creating a hierarchical tree structure.

This architecture provides two main benefits:
1.  **Finer-grained fault tolerance:** If a sub-transaction fails, it can abort and roll back its local changes without forcing the entire top-level transaction to abort. The parent transaction can choose to retry the sub-transaction, try an alternative action, or explicitly choose to abort itself.
2.  **Concurrency within a transaction:** Sub-transactions belonging to the same parent can execute concurrently, improving performance for complex tasks.

### Commit and Abort Semantics
The rules for nested transactions differ from flat transactions:
-   **Isolation:** A sub-transaction's changes are not visible to the outside world (or even to other branches of the transaction tree) until it completes. However, its changes *are* visible to its parent once it "commits".
-   **Provisional Commit:** When a sub-transaction finishes successfully, it performs a *provisional commit*. Its changes become visible to its parent, but they are not made permanent (durable) to the database yet.
-   **Top-level Commit:** Only when the absolute top-level root transaction commits are the changes of all provisionally committed sub-transactions made permanent and durable.
-   **Parent Abort:** If a parent transaction aborts, all of its sub-transactions (even those that provisionally committed) are forced to abort and roll back.

## Example
Consider a distributed travel booking system orchestrating a vacation package.
**Top-Level Transaction T (Book Vacation):**
-   **Sub-transaction T1 (Book Flight):** Queries airline database and reserves a seat.
-   **Sub-transaction T2 (Book Hotel):**
    -   **Sub-transaction T2.1 (Try Hotel A):** Attempts booking. If full, it aborts.
    -   **Sub-transaction T2.2 (Try Hotel B):** Attempts booking. Succeeds.
-   **Sub-transaction T3 (Book Car):** Reserving a rental car.

If T2.1 fails, it doesn't ruin the whole vacation booking. The parent T2 catches the abort and tries T2.2. If T3 (Car) fails entirely, the top-level T might decide a car is optional and commit anyway, finalizing T1 and T2.2. If T (Book Vacation) fails (e.g., credit card declined), T1, T2.2, and T3 are all rolled back.

## Applications & Use Cases
-   **Workflow Orchestration:** Complex business processes (like order fulfillment, which involves billing, inventory, and shipping) are modeled as nested transactions so that a failure in a minor step (like sending a confirmation email) doesn't roll back the payment processing.
-   **Distributed Databases with Replication:** Updating a replicated database can be a top-level transaction, with updates to individual replicas acting as concurrent sub-transactions. If one replica fails, the parent might still commit if quorum is reached.
-   **Component-based Software Architectures:** When a service calls multiple downstream microservices, encapsulating those calls as sub-transactions allows the calling service to handle localized failures gracefully.

## 3 Solved Numerical/Analytical Examples
**Example 1:**
Transaction T has children T1 and T2. T1 has child T1A. 
T1A commits provisionally. T1 aborts. What is the status of T1A's changes?
*Solution:*
Because the parent (T1) aborted, all of its descendants are also aborted, regardless of their individual provisional commit status. Therefore, T1A's changes are rolled back.

**Example 2:**
Transaction T spawns sub-transactions T1 and T2. Both T1 and T2 provisionally commit. Then T aborts. Are the changes visible to a completely separate transaction T3?
*Solution:*
No. In nested transactions, changes are only made durable and visible to the outside world (like T3) when the top-level transaction (T) commits. Since T aborted, the provisional commits of T1 and T2 are undone. T3 will see the original state of the data.

**Example 3:**
Explain lock inheritance in nested transactions. If parent T holds a read lock on object X, can child T1 get a write lock on X?
*Solution:*
Yes, through a mechanism called *lock inheritance*. A child transaction can acquire a lock on an object if its parent holds a compatible lock (or even if the parent holds the *same* lock). The child effectively borrows the lock. However, a parent cannot see the child's locked modifications until the child provisionally commits and passes the lock back up to the parent.

## Previous Year Questions & Solutions

**[April 2018] What are nested transactions? (4 marks)**
*Solution:*
A nested transaction is a transaction model where a main, top-level transaction can be broken down into a hierarchy of sub-transactions. 
Key characteristics include:
1.  **Hierarchy:** Transactions form a tree structure. The root is the top-level transaction, and the leaves are operations.
2.  **Concurrency:** Sub-transactions of the same parent can run concurrently, increasing parallelism.
3.  **Independent Recovery:** A sub-transaction can fail and abort without forcing its parent or siblings to abort. The parent can handle the failure by retrying or invoking an alternative sub-transaction.
4.  **Provisional Commits:** When a sub-transaction completes, it only "provisionally" commits. Its results are passed to its parent but are not made durable. The changes only become permanent and visible to the outside world when the top-level root transaction successfully commits. If any ancestor aborts, all provisionally committed descendants are rolled back.
