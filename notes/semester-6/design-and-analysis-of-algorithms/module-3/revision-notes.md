# Module 3: Last-Minute Revision & Submodule Guide

> **Semester**: S6 | **Subject**: Design and Analysis of Algorithms (CS302)  
> **Purpose**: Rapid revision guide for Module 3 covering Graph Traversals, Shortest Paths, Topological Sort, and SCCs.

---

## Submodule 3.1: Graph Traversals (DFS & BFS)

### 1. Explanation
- **DFS (Depth-First Search)**: Explores deep into a branch using a stack before backtracking.
- **BFS (Breadth-First Search)**: Explores neighbors level by level using a queue.

### 2. Real-World Example
- Web crawlers use BFS to crawl pages level by level from a starting URL.
- Solving a maze uses DFS to explore a path to a dead end before backing up.

### 3. Applications & Use Cases
- Cycle detection, topological ordering, unweighted shortest paths.

### 4. 3 Solved Micro-Examples
- **Example 1**: BFS runtime on adjacency list is $O(V + E)$.
- **Example 2**: DFS discovery and finishing times allow classifying edges into Tree, Back, Forward, and Cross edges.
- **Example 3**: Unweighted shortest path using BFS runs in $O(V + E)$.

---

## Submodule 3.2: Shortest Paths, Topological Sort & SCC

### 1. Explanation
- **Dijkstra**: Greedy shortest path algorithm for non-negative edge weights.
- **Topological Sort**: Ordering of DAG vertices where dependencies come first.
- **SCC**: Subgraph where every vertex is reachable from every other vertex.

### 2. Real-World Example
- **GPS Navigation (Google Maps)**: Uses Dijkstra / A* search for shortest driving routes.
- **Build Systems (Make / Gradle)**: Use Topological Sort to compile source file dependencies in correct order.

### 3. Applications & Use Cases
- Task scheduling, network routing protocols (OSPF), compiler optimization.

### 4. 3 Solved Micro-Examples
- **Example 1**: Dijkstra with Fibonacci heap runs in $O(E + V \log V)$.
- **Example 2**: Topological sort is only possible on Directed Acyclic Graphs (DAGs).
- **Example 3**: Kosaraju's SCC algorithm runs 2 passes of DFS in $O(V + E)$ time.
