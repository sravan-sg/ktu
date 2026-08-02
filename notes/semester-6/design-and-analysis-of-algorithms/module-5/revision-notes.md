# Module 5: Last-Minute Revision & Submodule Guide

> **Semester**: S6 | **Subject**: Design and Analysis of Algorithms (CS302)  
> **Purpose**: Rapid revision guide for Module 5 covering Greedy strategy, Fractional Knapsack, Prim's/Kruskal's, Backtracking, N-Queens, and 0/1 Knapsack.

---

## Submodule 5.1: Greedy Strategy & Minimum Spanning Trees

### 1. Explanation
Greedy makes local optimal choices. Fractional Knapsack takes items by highest profit/weight ratio. Prim's grows MST from a vertex; Kruskal's sorts edges and uses Union-Find.

### 2. Real-World Example
Laying out fiber optic cables between cities with minimum total cable length.

### 3. Applications & Use Cases
Network infrastructure, Huffman coding data compression.

### 4. 3 Solved Micro-Examples
- **Example 1**: Fractional Knapsack achieves exact optimal profit in $O(n \log n)$ time.
- **Example 2**: Kruskal's algorithm runtime with edge sorting is $O(E \log E)$.
- **Example 3**: Prim's algorithm runtime with min-heap is $O(E \log V)$.

---

## Submodule 5.2: Backtracking Strategy & Applications

### 1. Explanation
Systematic state-space tree traversal using DFS. Aborts invalid branches using bounding functions.

### 2. Real-World Example
Sudoku solvers and crosswords exploring number assignments and pruning conflicts.

### 3. Applications & Use Cases
Constraint satisfaction problems, circuit layout verification.

### 4. 3 Solved Micro-Examples
- **Example 1**: 4-Queens problem has 2 distinct non-attacking board solutions.
- **Example 2**: 0/1 Knapsack cannot be solved greedily by ratio sorting; requires Backtracking/DP.
- **Example 3**: Backtracking worst-case time complexity is exponential ($O(2^n)$ or $O(n!)$).
