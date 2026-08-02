# CS302 — Design and Analysis of Algorithms

> 4 credits, L-T-P 3-1-0 (Year of introduction 2016). Prerequisite: Nil. Derived semester: **S6** (from code CS302). Six modules; end-semester exam out of 100 marks.

## Grading Criteria

The syllabus file specifies the **end-semester exam** weightage and question-paper
pattern only. It does **not** state the internal-assessment split — confirm that
separately against the scheme regulations.

**End-semester per-module weightage (sums to 100%):**

| Modules | Weightage |
|---------|-----------|
| I       | 15 % |
| II      | 15 % |
| III     | 15 % |
| IV      | 15 % |
| V       | 20 % |
| VI      | 20 % |

**Question-paper pattern (end-sem, 100 marks):**

| Part | Marks | Questions | Covers | To answer |
|------|-------|-----------|--------|-----------|
| A | 12 | 4 × 3 | Modules I & II | All 4 |
| B | 18 | 3 × 9 (≤3 subparts each) | Modules I & II | Any 2 |
| C | 12 | 4 × 3 | Modules III & IV | All 4 |
| D | 18 | 3 × 9 (≤3 subparts each) | Modules III & IV | Any 2 |
| E | 40 | 6 × 10 (≤3 subparts each) | Modules V & VI | Any 4 |

- Two internal exams: **First Internal** after Module II, **Second Internal** after Module IV.
- **At least 60 % of questions must be analytical/numerical.**

## Textbooks

1. Ellis Horowitz, Sartaj Sahni, Sanguthevar Rajasekaran — *Computer Algorithms*, Universities Press, 2007. **[Modules 3, 4, 5]**
2. Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein — *Introduction to Algorithms*, MIT Press, 2009. **[Modules 1, 2, 6]**

**References**

1. Aho, Hopcroft, Ullman — *The Design and Analysis of Computer Algorithms*, Pearson, 1999.
2. Anany Levitin — *Introduction to the Design and Analysis of Algorithms*, Pearson, 3rd ed., 2011.
3. Gilles Brassard, Paul Bratley — *Fundamentals of Algorithmics*, Pearson, 1995.
4. Richard E. Neapolitan, Kumarss Naimipour — *Foundations of Algorithms using C++ Pseudocode*, 2nd ed., 1997.

## Modules

### Module I — Introduction to Algorithm Analysis & Recurrences (4 + 4 hrs) — [Module 1 Detailed Notes](file:///Users/sreeram/Developer/sravan/ktu/notes/semester-6/design-and-analysis-of-algorithms/module-1-detailed-notes.md)
- Time and Space Complexity — elementary operations and computation of time complexity
- Best, worst and average case complexities
- Complexity calculation of simple algorithms
- Recurrence equations: solution of recurrence equations
- Iteration Method and Recursion Tree Method

### Module II — Master's Theorem, Asymptotics & Balanced Structures (5 + 5 hrs)
- Master's Theorem (proof not required) — examples
- Asymptotic notations and their properties
- Application of asymptotic notations in algorithm analysis
- Common complexity functions
- AVL Trees — rotations
- Red-Black Trees — insertion and deletion (techniques only; algorithms not expected)
- B-Trees — insertion and deletion operations
- Sets — Union and Find operations on disjoint sets

*(First Internal Exam covers Modules I & II.)*

### Module III — Graph Algorithms (7 hrs)
- Graphs — DFS and BFS traversals, complexity
- Spanning trees — Minimum Cost Spanning Trees
- Single-source shortest path algorithms
- Topological sorting
- Strongly connected components

### Module IV — Divide and Conquer & Dynamic Programming (4 + 5 + 2 hrs)
- Divide and Conquer: the control abstraction; 2-way Merge Sort; Strassen's Matrix Multiplication; analysis
- Dynamic Programming: the control abstraction; the Optimality Principle; optimal matrix multiplication; Bellman-Ford Algorithm
- Analysis and comparison of Divide-and-Conquer vs Dynamic Programming strategies

*(Second Internal Exam covers Modules III & IV.)*

### Module V — Greedy Strategy & Backtracking (4 + 3 + 3 hrs)
- Greedy Strategy: the control abstraction; the Fractional Knapsack Problem
- Minimal Cost Spanning Tree computation — Prim's Algorithm, Kruskal's Algorithm
- Backtracking: the control abstraction; the N-Queens Problem; 0/1 Knapsack Problem

### Module VI — Branch and Bound & Complexity Theory (3 + 3 hrs)
- Branch and Bound: Travelling Salesman Problem
- Introduction to Complexity Theory: tractable and intractable problems
- The P and NP classes
- Polynomial-time reductions
- The NP-Hard and NP-Complete classes

## Exam Focus — What to Prioritize

- **Modules V & VI are decisive: 40 of 100 marks sit in Part E alone** (10-mark questions, answer 4 of 6). Greedy, Backtracking, Branch-and-Bound, and the P/NP classification carry the most weight per topic — invest here first.
- **Master numerical methods, since ≥60 % of the paper is analytical/numerical.** The highest-yield drills: solving recurrences (iteration + recursion tree), applying Master's Theorem, working Prim's/Kruskal's, fractional vs 0/1 Knapsack, optimal matrix-chain (DP), Bellman-Ford, and Strassen's product. These are worked-problem questions, not theory.
- **Modules I & II are guaranteed marks (Parts A + B = 30 marks).** Part A forces all four 3-mark questions, so secure the basics: asymptotic notations and properties, complexity of simple algorithms, and Master's Theorem application — low effort, no choice to dodge them.
- **AVL / Red-Black / B-Tree operations are "techniques only"** (RB-tree algorithms explicitly not expected) — practice the *step-by-step rotations/insertions/deletions* rather than memorizing pseudocode; these appear as trace-the-structure problems.
- **Graph algorithms (Module III) are dense for 7 hours of one module** — DFS/BFS, MST, shortest paths, topological sort, and SCC each recur; expect both a trace and a complexity-justification question in Parts C/D.
- **Know the control abstractions cold.** Each design paradigm (D&C, DP, Greedy, Backtracking, B&B) is introduced via its control abstraction — a reliable short-answer and a framing for the long numericals.
- **DP vs Divide-and-Conquer comparison is an explicit syllabus outcome** — a likely descriptive question; be ready to contrast overlapping subproblems and the optimality principle with a concrete example (e.g., matrix multiplication).
- **For Module VI theory, be precise on definitions:** P, NP, NP-Hard, NP-Complete, and polynomial-time reductions. Classification questions reward exact boundaries, not hand-waving.
