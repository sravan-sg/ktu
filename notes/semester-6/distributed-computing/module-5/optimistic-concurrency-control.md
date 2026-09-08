# Optimistic Concurrency Control (OCC)

## Explanation
Locking-based concurrency control is inherently **pessimistic**. It assumes that conflicts between transactions *will* happen, and therefore severely restricts access by enforcing locks, which adds significant overhead (lock management, deadlocks, waiting). 

**Optimistic Concurrency Control (OCC)**, developed by Kung and Robinson, takes the opposite approach. It assumes that conflicts are rare. Therefore, it allows transactions to proceed without locking any data. It operates in three distinct phases:
1.  **Working Phase (Read Phase):** The transaction reads data from the database and performs all computations locally. Any writes (updates) are not applied to the actual database; instead, they are recorded in a private, temporary workspace (a "tentative" version).
2.  **Validation Phase:** When the transaction is ready to commit, the system checks if the transaction's operations conflicted with any other concurrent transactions. It validates whether applying the tentative changes will violate serializability. 
3.  **Update Phase (Write Phase):** If validation is successful (no conflicts), the changes in the private workspace are made permanent in the actual database. If validation fails, the transaction is **aborted** and its private workspace is discarded. The transaction must restart.

### Validation Strategies
To validate Transaction Tv, the system checks its Read Set (RS) and Write Set (WS) against other transactions:
-   **Backward Validation:** Checks if Tv's Read Set intersects with the Write Set of any transaction that committed *during* Tv's working phase. (Did someone overwrite what I read?)
-   **Forward Validation:** Checks if Tv's Write Set intersects with the Read Set of any currently active transaction. (Will my writes ruin someone else's current reads?)

## Example
**OCC Workflow:**
Imagine a wiki where users edit articles.
1.  **User A (T1)** opens "Distributed Systems" to edit (Working Phase). No locks are taken.
2.  **User B (T2)** opens the exact same article to edit. No locks taken.
3.  User A finishes and clicks Save.
    -   *Validation:* T1 checks if anyone modified the article since T1 opened it. Nobody has.
    -   *Update:* T1's changes are saved to the database.
4.  User B finishes and clicks Save.
    -   *Validation:* T2 checks if anyone modified the article since T2 opened it. T1 *did* modify it. Conflict detected!
    -   *Update:* Validation fails. T2 is aborted. User B receives an error: "Conflict detected, please merge your changes."

## Applications & Use Cases
-   **Web Applications (e.g., Wikis, CMS):** In systems where read operations vastly outnumber write operations, locking creates unnecessary bottlenecks. OCC is perfect because conflicts (two people editing the exact same paragraph simultaneously) are rare.
-   **NoSQL Databases & ORMs:** Many Object-Relational Mappers (like Hibernate or Entity Framework) use a version number column to implement OCC. When an object is updated, the DB checks if the version number matches what was originally read.
-   **Software Transactional Memory (STM):** Programming languages using STM (like Clojure) use optimistic techniques to manage concurrent threads accessing shared memory without using explicit mutexes.

## 3 Solved Numerical/Analytical Examples
**Example 1:**
Why does Optimistic Concurrency Control perform poorly in high-contention environments?
*Solution:*
In high-contention environments, many transactions try to modify the same data simultaneously. Because OCC allows them all to proceed through the working phase without blocking, almost all of them will fail during the validation phase. This results in massive CPU and I/O waste because transactions do all the work only to be aborted and restarted repeatedly (a phenomenon known as "thrashing").

**Example 2:**
Transaction T1 has ReadSet(X) and WriteSet(Y). Transaction T2 has ReadSet(Y) and WriteSet(Z). T1 starts, T2 starts, T1 validates and commits, T2 validates. 
Using Backward Validation, will T2 pass validation?
*Solution:*
T2 validates against committed transactions that overlapped its execution (T1).
Backward validation checks if `ReadSet(T2) INTERSECT WriteSet(T1)` is empty.
ReadSet(T2) = {Y}. WriteSet(T1) = {Y}. 
Intersection is {Y}, which is not empty. Therefore, T1 overwrote data that T2 had read. T2 will **fail** validation and abort.

**Example 3:**
How does OCC avoid deadlocks?
*Solution:*
Deadlocks require a circular wait condition where processes hold resources while waiting for others. Because OCC explicitly acquires *no locks* during its working phase, it is impossible for transactions to block each other or wait for resources. Therefore, OCC is inherently deadlock-free.

## Previous Year Questions & Solutions

**[April 2018] Explain optimistic concurrency control in detail. (6 marks)**
*Solution:*
Optimistic Concurrency Control (OCC) is a deadlock-free concurrency mechanism based on the assumption that conflicting transactions are rare. Instead of locking data proactively (pessimistic approach), transactions proceed without restrictions and are checked for conflicts only at the end.
It operates in three distinct phases:
1.  **Working Phase:** The transaction reads values from the database and executes its operations. Any write operations are not applied to the shared database. Instead, they are kept in a local, private workspace belonging only to that transaction.
2.  **Validation Phase:** When the transaction requests to commit, the system performs a validation check. It determines if the transaction's execution was serializable by comparing its Read Set and Write Set against the sets of other overlapping transactions.
    -   *Backward Validation* ensures the transaction didn't read data that was subsequently altered by a newly committed transaction.
    -   *Forward Validation* ensures the transaction's intended writes won't invalidate the reads of currently active transactions.
3.  **Update Phase:** If the validation phase determines there are no conflicts, the transaction is committed, and the changes in the private workspace are made permanent in the database. If validation fails, the transaction is immediately aborted, its private workspace is discarded, and it must be restarted.
This approach is highly efficient for read-heavy workloads but degrades quickly under high contention due to the cost of repeated aborts.
