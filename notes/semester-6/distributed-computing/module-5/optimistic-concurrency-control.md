# Optimistic Concurrency Control (OCC)

## Explanation
Locking-based concurrency control (like 2PL) is inherently **pessimistic**. It assumes that conflicts between transactions *will* frequently happen, and therefore severely restricts access by enforcing locks proactively. This adds significant system overhead (lock manager administration, deadlock detection, and transaction blocking).

**Optimistic Concurrency Control (OCC)**, originally developed by Kung and Robinson, takes the exact opposite approach. It assumes that conflicts between transactions are fundamentally rare. Therefore, it allows transactions to proceed completely unhindered without locking any data. It operates in three distinct, strictly ordered phases:

1. **Working Phase (Read/Execution Phase):** The transaction reads data from the database and performs all necessary computations locally. Any write operations (updates) are not applied to the actual shared database; instead, they are recorded in a private, temporary workspace (a "tentative" version).
2. **Validation Phase:** When the transaction attempts to commit, the system checks if the transaction's operations conflicted with any other concurrent transactions. It validates whether applying the tentative changes from the private workspace will violate conflict serializability.
3. **Update Phase (Write Phase):** If validation is successful (meaning no conflicts occurred), the tentative changes in the private workspace are made permanent in the actual database. If validation fails, the transaction is **aborted**, its private workspace is immediately discarded, and the transaction is forced to restart from scratch.

### Validation Strategies
To validate Transaction $T_v$, the distributed system checks its Read Set (RS) and Write Set (WS) against other overlapping transactions:
- **Backward Validation:** Checks if $T_v$'s Read Set intersects with the Write Set of any transaction that committed *during* $T_v$'s working phase. (i.e., "Did someone overwrite the data I just read?")
- **Forward Validation:** Checks if $T_v$'s Write Set intersects with the Read Set of any currently active transaction. (i.e., "Will my tentative writes ruin someone else's current reads?")

## Example
**OCC Workflow in a Distributed Wiki:**
Imagine a collaborative wiki platform where users edit articles.
1. **User A ($T_1$)** opens the "Distributed Systems" article to edit (Working Phase). No locks are taken; the server sends a snapshot.
2. **User B ($T_2$)** opens the exact same article to edit. No locks are taken.
3. User A finishes and clicks Save.
   - *Validation:* $T_1$ checks if anyone modified the article since $T_1$ opened it. Nobody has.
   - *Update:* $T_1$'s changes are durably saved to the database.
4. User B finishes and clicks Save.
   - *Validation:* $T_2$ checks if anyone modified the article since $T_2$ opened it. The system detects $T_1$ *did* modify it. Conflict detected!
   - *Update:* Validation fails. $T_2$ is aborted. User B receives an error: "Conflict detected, please merge your changes."

## Applications & Use Cases
- **Web Applications (e.g., Wikis, CMS):** In systems where read operations vastly outnumber write operations, pessimistic locking creates unnecessary bottlenecks. OCC is perfect because write conflicts (two people editing the exact same paragraph simultaneously) are statistically rare.
- **NoSQL Databases & ORMs:** Many Object-Relational Mappers (like Hibernate or Entity Framework) use a version number column to implement OCC. When an object is updated, the DB checks if the version number matches what was originally read.
- **Software Transactional Memory (STM):** Programming languages using STM (like Clojure) use optimistic techniques to manage concurrent threads accessing shared memory without relying on explicit mutexes.

## 3 Solved Numerical/Analytical Examples

**Example 1: The Thrashing Phenomenon**
*Problem:* Why does Optimistic Concurrency Control perform terribly in high-contention environments?
*Solution:*
1. In high-contention environments, many transactions try to modify the exact same data items simultaneously. 
2. Because OCC allows them all to proceed through the working phase without blocking, almost all of them will fail during the validation phase. 
*Conclusion:* This results in massive CPU and I/O waste because transactions execute all their operations only to be aborted and restarted repeatedly, leading to a phenomenon known as "thrashing."

**Example 2: Backward Validation Analysis**
*Problem:* Transaction $T_1$ has ReadSet(X) and WriteSet(Y). Transaction $T_2$ has ReadSet(Y) and WriteSet(Z). $T_1$ starts, $T_2$ starts, $T_1$ validates and commits, $T_2$ validates. Using Backward Validation, will $T_2$ pass validation?
*Solution:*
1. $T_2$ validates against committed transactions that overlapped its execution (which is $T_1$).
2. Backward validation checks if `ReadSet(T2) INTERSECT WriteSet(T1)` is empty.
3. ReadSet($T_2$) = {Y}. WriteSet($T_1$) = {Y}. 
4. The intersection is {Y}, which is *not* empty. 
*Conclusion:* Therefore, $T_1$ overwrote data that $T_2$ had read. $T_2$ will fail validation and abort to preserve serializability.

**Example 3: Deadlock Freedom**
*Problem:* How does OCC guarantee that deadlocks will never occur?
*Solution:*
1. Deadlocks strictly require a circular wait condition where processes hold resources while waiting indefinitely for others. 
2. Because OCC explicitly acquires *zero locks* during its working phase, it is impossible for transactions to block each other or wait for resources. 
*Conclusion:* Therefore, OCC is mathematically and inherently deadlock-free.

## Previous Year Questions & Solutions

**[April 2018] Explain optimistic concurrency control in detail. (6 marks)**
*Solution:*
Optimistic Concurrency Control (OCC) is a deadlock-free concurrency mechanism based on the fundamental assumption that conflicting transactions are rare. Instead of locking data proactively (the pessimistic approach), transactions proceed without restrictions and are checked for conflicts only at the very end.

It operates in three distinct, ordered phases:
1. **Working Phase:** The transaction reads values from the database and executes all its operations locally. Any write operations are not applied to the shared database. Instead, they are kept in a local, private workspace belonging only to that transaction.
2. **Validation Phase:** When the transaction requests to commit, the system performs a mathematical validation check. It determines if the transaction's execution was serializable by comparing its Read Set and Write Set against the sets of other overlapping transactions.
   - *Backward Validation* ensures the transaction didn't read data that was subsequently altered by a newly committed transaction.
   - *Forward Validation* ensures the transaction's intended writes won't invalidate the reads of currently active transactions.
3. **Update Phase:** If the validation phase determines there are no conflicts, the transaction is committed, and the tentative changes in the private workspace are made permanent in the database. If validation fails, the transaction is immediately aborted, its private workspace is discarded, and it must be restarted.

This approach is highly efficient and highly parallel for read-heavy workloads but degrades quickly under high contention due to the overhead of repeated aborts.
