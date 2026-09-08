# Module 5: Transactional Concurrency Control - Revision Notes

## 1. Quick Summary
Module 5 focuses on managing concurrent access to shared data in distributed environments using transactions. It covers the fundamental rules that transactions must obey (ACID), the theoretical basis for correct concurrent execution (Conflict Serializability), and structural extensions (Nested Transactions). The module contrasts two primary mechanisms for ensuring isolation: pessimistic locking (2PL) and Optimistic Concurrency Control (OCC).

## 2. Key Definitions & Formulas
*   **ACID Properties:** Atomicity (All or nothing), Consistency (Valid state to valid state), Isolation (No intermediate visibility), Durability (Permanent changes).
*   **Conflict Serializability:** A schedule of concurrent transactions is valid if its operations can be rearranged into a strictly serial execution without altering the outcome. Requires an acyclic precedence graph.
*   **Nested Transactions:** A transaction hierarchy where sub-transactions can fail independently without aborting the parent. Uses *provisional commits* which are only made durable when the top-level root transaction commits.
*   **Two-Phase Locking (2PL):** A protocol ensuring serializability. Phase 1 (Growing): Acquire locks, release none. Phase 2 (Shrinking): Release locks, acquire none. Strict 2PL delays the shrinking phase until commit/abort to prevent cascading rollbacks.
*   **Optimistic Concurrency Control (OCC):** A deadlock-free approach assuming low conflict. Operates in three phases: Working (local workspace, no locks), Validation (check for conflicts via read/write set intersection), Update (commit changes or abort/restart).

## 3. Top Exam Focus Areas (PYQ Patterns)
1.  **Optimistic Concurrency Control (OCC):** Highly tested. Be prepared to explain the 3 phases (Working, Validation, Update) in detail and explain why it's deadlock-free. (6 marks, April 2018)
2.  **Two-Phase Locking (2PL):** Understand the difference between the growing and shrinking phases, and explain the difference between shared and exclusive locks. (6 marks, April 2018)
3.  **Transactions & ACID:** Be able to define distributed transactions and explain the four ACID properties. (6 marks, April 2018)
4.  **Nested Transactions:** Explain the hierarchy, independent recovery, and provisional commit semantics. (4 marks, April 2018)
5.  **Conflict Serializability:** Define it and list the conditions for two operations to conflict (different transactions, same data, at least one write). (4 marks, April 2018)

## 4. Most Common Mistakes & Tips
*   **2PL vs Deadlocks:** Remember that 2PL guarantees *serializability*, but it **does not** prevent deadlocks. (Transactions can still be in their growing phases, waiting on each other). OCC, however, is deadlock-free.
*   **Nested vs Flat:** In a nested transaction, a sub-transaction committing does *not* make data durable. Only the top-level commit makes data durable. 
*   **OCC Validation:** Understand that backward validation checks if your *reads* were overwritten by recently committed transactions, while forward validation checks if your *writes* will overwrite currently active reads.