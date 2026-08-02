# Module 6 — Topic 1: Branch and Bound & Travelling Salesman Problem

> **Module 6**: Branch and Bound & Complexity Theory  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Branch and Bound Control Abstraction
Unlike Backtracking (which uses DFS), **Branch and Bound** uses **Breadth-First Search (BFS)** or **Best-First Search (Least Cost Search)** to explore state-space trees for optimization problems.
- Maintains an **Upper Bound (cost of best solution found so far)** and calculates a **Lower Bound $c(x)$** for each active live node.
- If $c(x) \ge \text{Upper Bound}$, node $x$ is killed (pruned).

---

## 2. Travelling Salesman Problem (TSP) using LCBB
Find minimum cost tour visiting every city exactly once and returning to starting city.
- Computes reduced cost matrices to find lower bounds $c(x)$ at each state-space node.
