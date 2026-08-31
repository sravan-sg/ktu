# CS407 — Distributed Computing

> 3 Credits, L-T-P: 3-0-0

## Grading Criteria

* **Internal Evaluation**: Two internal exams (after Module II and Module IV).
* **End Semester Examination Pattern** (100 Marks Total):
  * **Part A (40 Marks)**: 10 compulsory questions, 4 marks each. (3 from Modules I & II; 3 from Modules III & IV; 4 from Modules V & VI).
  * **Part B (18 Marks)**: Answer 2 out of 3 questions (9 marks each). Covers Modules I & II.
  * **Part C (18 Marks)**: Answer 2 out of 3 questions (9 marks each). Covers Modules III & IV.
  * **Part D (24 Marks)**: Answer 2 out of 3 questions (12 marks each). Covers Modules V & VI.
* **Note**: At least 50% of the questions across all choices will be analytical/numerical.

## Textbooks

1. George Coulouris, Jean Dollimore and Tim Kindberg, Distributed Systems: Concepts and Design, Fifth Edition, Pearson Education, 2011
2. Pradeep K Sinha, Distributed Operating Systems: Concepts and Design, Prentice Hall of India

**References:**
1. A S Tanenbaum and M V Steen, Distributed Systems: Principles and paradigms, Pearson Education, 2007
2. M Solomon and J Krammer, Distributed Systems and Computer Networks, PHI

## Modules

### Module I — Evolution of Distributed Computing
- Issues in designing a distributed system
- Challenges
- Minicomputer model
- Workstation model
- Workstation-Server model
- Processor-pool model
- Trends in distributed systems

### Module II — System models
- Physical models
- Architectural models
- Fundamental models

### Module III — Interprocess communication
- characteristics
- group communication
- Multicast Communication
- Remote Procedure call
- Network virtualization
- Case study: Skype

### Module IV — Distributed file system
- File service architecture
- Network file system
- Andrew file system
- Name Service

### Module V — Transactional concurrency control
- Transactions
- Nested transactions
- Locks
- Optimistic concurrency control

### Module VI — Distributed mutual exclusion and Election
- Distributed mutual exclusion
- central server algorithm
- ring based algorithm
- Maekawa's voting algorithm
- Election: Ring-based election algorithm
- Bully algorithm

## Exam Focus — What to Prioritize

- **High-Weightage Modules (V & VI):** Modules V and VI carry the highest weightage (24 marks in Part D + 16 marks in Part A = 40 marks total). Master concurrency control (locks, optimistic) and all mutual exclusion/election algorithms (Maekawa, Bully, Ring-based) as they are prime candidates for 12-mark questions and numerical/analytical problems.
- **Analytical/Numerical Preparation:** The syllabus mandates at least 50% analytical/numerical questions. Focus on tracing algorithms, calculating message complexities in mutual exclusion/election, and working through concurrency control scenarios (e.g., lock compatibility, conflict serializability).
- **Core Mechanisms (Modules III & IV):** Interprocess Communication (RPC, Multicast) and Distributed File Systems (NFS, AFS) are guaranteed to appear in Part C (18 marks). Focus on their architectural differences and how they handle transparency and fault tolerance.
- **Foundations (Modules I & II):** System Models and Distributed System Evolution form the theoretical foundation. Expect straightforward descriptive questions in Part B (18 marks) comparing different models (e.g., Minicomputer vs. Workstation-Server).
