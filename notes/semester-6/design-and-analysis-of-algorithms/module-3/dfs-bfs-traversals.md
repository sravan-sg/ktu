# Module 3 — Topic 1: Graph Traversals (DFS & BFS)

> **Module 3**: Graph Algorithms  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Depth-First Search (DFS)
- **Concept**: Explores as deep as possible along each branch before backtracking. Uses a **Stack** (or recursion).
- **Time Complexity**: $O(V + E)$ using adjacency list representation.
- **Space Complexity**: $O(V)$ for call stack and visited array.

---

## 2. Breadth-First Search (BFS)
- **Concept**: Explores neighbor nodes level-by-level starting from the source. Uses a **Queue**.
- **Time Complexity**: $O(V + E)$ using adjacency list.
- **Applications**: Shortest path in unweighted graphs, connected components.
