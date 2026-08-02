# Module 5 — Topic 2: Backtracking (N-Queens & 0/1 Knapsack)

> **Module 5**: Greedy Strategy & Backtracking  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Backtracking Control Abstraction
Systematically searches the solution space tree using **Depth-First Search**. If a partial state violates constraints (using a **bounding / constraint function**), it prunes the sub-tree and **backtracks** to the parent node.

---

## 2. N-Queens Problem
Place $N$ chess queens on an $N \times N$ chessboard such that no two queens attack each other (no same row, column, or diagonal).
- Solved via state-space tree depth-first search with explicit column/diagonal constraint checks.

---

## 3. 0/1 Knapsack Problem (Backtracking)
Unlike Fractional Knapsack, items cannot be broken (take 0 or 1).
- Explores decision tree (include/exclude item $i$) and prunes branches when current weight exceeds capacity $W$ or upper bound profit cannot beat max profit so far.
