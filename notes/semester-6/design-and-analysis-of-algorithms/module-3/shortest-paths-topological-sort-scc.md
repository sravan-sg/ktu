# Module 3 — Topic 2: Shortest Paths, Topological Sort & SCC

> **Module 3**: Graph Algorithms  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Single-Source Shortest Paths
- **Dijkstra's Algorithm**: Greedy strategy for non-negative edge weights. Time complexity $O((V + E) \log V)$ with min-priority queue.
- **Bellman-Ford Algorithm**: Dynamic programming approach handling negative edge weights. Time complexity $O(V \cdot E)$.

---

## 2. Topological Sorting
- Linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge $u \to v$, $u$ comes before $v$.
- Time Complexity: $O(V + E)$ using DFS or Kahn's algorithm (indegree queue).

---

## 3. Strongly Connected Components (SCC)
- A directed graph is strongly connected if every vertex is reachable from every other vertex.
- **Kosaraju's Algorithm**: Uses 2 passes of DFS and graph transposition. Time complexity $O(V + E)$.
