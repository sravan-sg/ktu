# Module 4 — Topic 2: Dynamic Programming & Strategy Comparison

> **Module 4**: Divide and Conquer & Dynamic Programming  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Dynamic Programming & Principle of Optimality
- **Principle of Optimality**: An optimal sequence of decisions has the property that whatever the initial state and decision are, the remaining decisions must constitute an optimal decision sequence.
- **Overlapping Subproblems**: Subproblems recur multiple times; DP stores intermediate results in a table (memoization / bottom-up tabulation).

---

## 2. Comparison: Divide & Conquer vs Dynamic Programming

| Feature | Divide & Conquer | Dynamic Programming |
| :--- | :--- | :--- |
| **Subproblem Nature** | Independent non-overlapping subproblems | Overlapping subproblems |
| **Approach** | Top-down recursive breakdown | Bottom-up tabulation / Top-down memoization |
| **Re-computation** | Re-computes identical subproblems | Stores and reuses subproblem solutions |
| **Classic Example** | Merge Sort, QuickSort, Binary Search | Optimal Matrix Chain Multiplication, Bellman-Ford |
