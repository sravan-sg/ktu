# Module 6: Last-Minute Revision & Submodule Guide

> **Semester**: S6 | **Subject**: Design and Analysis of Algorithms (CS302)  
> **Purpose**: Rapid revision guide for Module 6 covering Branch and Bound (TSP) and Complexity Theory (P, NP, NP-Hard, NP-Complete).

---

## Submodule 6.1: Branch and Bound (TSP)

### 1. Explanation
Branch and Bound uses BFS/Best-First Search to explore state-space trees for optimization. It prunes live nodes whose lower bound $c(x)$ exceeds the current best upper bound.

### 2. Real-World Example
Logistics and delivery route optimization (Amazon / FedEx truck routing).

### 3. Applications & Use Cases
Integer Linear Programming (ILP) solvers, TSP tour optimization.

### 4. 3 Solved Micro-Examples
- **Example 1**: Reduced cost matrix subtracts minimum row and column values to calculate lower bound root cost.
- **Example 2**: LCBB uses a min-priority queue based on lower bound $c(x)$ to expand the most promising state node first.
- **Example 3**: TSP worst-case state space size is $(n-1)!$.

---

## Submodule 6.2: Complexity Theory (P, NP, NP-Complete)

### 1. Explanation
- **P**: Solvable in polynomial time $O(n^k)$.
- **NP**: Verifiable in polynomial time.
- **NP-Complete**: Hardest problems in NP; if any single NP-Complete problem is solved in $O(n^k)$, then $P = NP$.

### 2. Real-World Example
Password hashing & Cryptography (RSA security relies on integer factorization being intractable/hard).

### 3. Applications & Use Cases
Classifying hard algorithmic problems to determine when to switch from exact algorithms to approximation/heuristic algorithms.

### 4. 3 Solved Micro-Examples
- **Example 1**: Every problem in P is also in NP ($P \subseteq NP$).
- **Example 2**: Cook's Theorem proved Boolean Satisfiability (3-SAT) is NP-Complete.
- **Example 3**: If $L_1 \le_P L_2$ and $L_1$ is NP-Hard, then $L_2$ is also NP-Hard.
