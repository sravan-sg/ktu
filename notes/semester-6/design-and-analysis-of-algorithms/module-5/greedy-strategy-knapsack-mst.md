# Module 5 — Topic 1: Greedy Strategy (Knapsack & MST)

> **Module 5**: Greedy Strategy & Backtracking  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Greedy Strategy Control Abstraction
Makes locally optimal choices at each step without ever backtracking, hoping to arrive at a globally optimal solution.

---

## 2. Fractional Knapsack Problem
- Items can be broken into fractional parts.
- Strategy: Sort items by profit-to-weight ratio ($p_i / w_i$) in descending order and greedily take as much as possible of the highest ratio item.
- Time Complexity: $O(n \log n)$ due to sorting.

---

## 3. Minimal Cost Spanning Trees (Prim's & Kruskal's)
- **Prim's Algorithm**: Grows a single tree starting from a seed vertex. Uses min-priority queue ($O(E \log V)$).
- **Kruskal's Algorithm**: Sorts all edges by weight and uses Union-Find to add non-cyclic edges ($O(E \log E)$).
