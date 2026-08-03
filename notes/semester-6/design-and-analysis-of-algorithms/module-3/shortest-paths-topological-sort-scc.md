# Module 3 — Topic 2: Shortest Paths, Topological Sort & SCC

> **Module 3**: Graph Algorithms  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
- **Shortest Paths (Dijkstra & Bellman-Ford)**: In a weighted graph, the goal is to find the path with the minimum total edge weight from a source node to all other nodes. Dijkstra's uses a greedy approach (always picking the closest unvisited node), making it incredibly fast but incapable of handling negative weights. Bellman-Ford uses a dynamic programming approach, checking every edge $V-1$ times, which is slower but can detect and handle negative-weight cycles.
- **Topological Sorting**: Given a Directed Acyclic Graph (DAG), a topological sort is a linear ordering of its vertices such that for every directed edge $u \to v$, vertex $u$ comes before $v$ in the ordering. It is a mathematical way of resolving dependencies.
- **Strongly Connected Components (SCC)**: A sub-graph is strongly connected if there is a valid path from *every* node to *every other* node within that sub-graph. Kosaraju's Algorithm finds these clusters using two passes of DFS and transposing (reversing) the graph's edges.

### Example
- **Shortest Paths**: Navigating a GPS. Every road has a "weight" (time/distance). You want the cheapest route. 
- **Topological Sorting**: Getting dressed in the morning. You must put on your socks before your shoes. Your pants before your belt. The "sort" gives you a valid linear sequence to put your clothes on without violating physical reality.
- **SCCs**: A city road network with one-way streets. An SCC is a specific neighborhood where you can drive from any intersection to any other intersection without breaking one-way traffic laws.

### Applications & Use Cases
- **Network Routing Protocols (Shortest Path)**: OSPF (Open Shortest Path First) uses Dijkstra's algorithm to route internet traffic packets along the fastest paths across routers.
- **Build Systems (Topological Sort)**: Compilers (like Make or Webpack) and Package Managers (like NPM) use topological sorting to figure out the exact order to compile source files or install dependencies so that no file is compiled before its required imports.
- **Social Network Analysis (SCC)**: Used by Facebook/X to find highly cohesive communities or echo chambers where everyone follows or interacts with everyone else within the cluster.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Dijkstra's Algorithm Trace
**Problem:** Trace Dijkstra’s algorithm to find the shortest path from Source $S$ to all nodes. Nodes: $\{S, A, B\}$. Edges: $(S,A,weight=4), (S,B,weight=1), (B,A,weight=2)$.
**Step-by-step Solution:**
1. **Initialization:** Distances: $D[S]=0, D[A]=\infty, D[B]=\infty$. Unvisited set = $\{S, A, B\}$.
2. **Step 1:** Extract minimum distance node $\rightarrow S$ ($D[S]=0$).
   - Check neighbor $A$: $D[S] + 4 = 4$. $4 < \infty$. Update $D[A]=4$.
   - Check neighbor $B$: $D[S] + 1 = 1$. $1 < \infty$. Update $D[B]=1$.
   - Unvisited = $\{A, B\}$.
3. **Step 2:** Extract minimum distance node $\rightarrow B$ ($D[B]=1$).
   - Check neighbor $A$: $D[B] + 2 = 1 + 2 = 3$. $3 < D[A]$ (which is 4). Update $D[A]=3$.
   - Unvisited = $\{A\}$.
4. **Step 3:** Extract minimum distance node $\rightarrow A$ ($D[A]=3$).
   - No outgoing edges from $A$.
   - Unvisited = $\{\}$.
5. **Final Distances:** $D[S]=0, D[B]=1, D[A]=3$. 
*(Note: Because Dijkstra is greedy, it permanently locked in $B$'s distance before finding the shortcut to $A$ via $B$.)*

### Example 2: Kahn's Algorithm for Topological Sorting
**Problem:** Perform a topological sort on a DAG with vertices $\{1, 2, 3, 4\}$ and edges $(1 \to 2), (1 \to 3), (2 \to 4), (3 \to 4)$.
**Step-by-step Solution:**
1. **Calculate In-degrees:** (Number of incoming edges).
   - In(1) = 0
   - In(2) = 1 (from 1)
   - In(3) = 1 (from 1)
   - In(4) = 2 (from 2, 3)
2. **Initialize Queue:** Enqueue all nodes with In-degree 0. $Q = [1]$. Result Array $R = []$.
3. **Step 1:** Dequeue $1$. Add to $R$. $R = [1]$.
   - For neighbor 2: In(2) becomes $1 - 1 = 0$. Enqueue 2. $Q = [2]$.
   - For neighbor 3: In(3) becomes $1 - 1 = 0$. Enqueue 3. $Q = [2, 3]$.
4. **Step 2:** Dequeue $2$. Add to $R$. $R = [1, 2]$.
   - For neighbor 4: In(4) becomes $2 - 1 = 1$. (Not 0, so don't enqueue).
5. **Step 3:** Dequeue $3$. Add to $R$. $R = [1, 2, 3]$.
   - For neighbor 4: In(4) becomes $1 - 1 = 0$. Enqueue 4. $Q = [4]$.
6. **Step 4:** Dequeue $4$. Add to $R$. $R = [1, 2, 3, 4]$.
7. **Final Topological Sort:** $1, 2, 3, 4$ (or $1, 3, 2, 4$ depending on queue insertion order).

### Example 3: Kosaraju's Algorithm for SCCs
**Problem:** Trace Kosaraju's algorithm on a graph with vertices $A, B, C$ and edges $(A \to B), (B \to C), (C \to A)$.
**Step-by-step Solution:**
1. **Pass 1 (DFS for Finish Times):** Perform standard DFS starting from any node, pushing nodes to a Stack when they finish (no more unvisited neighbors).
   - Start at $A$. Dive to $B$. Dive to $C$. 
   - $C$'s neighbor $A$ is visited. $C$ finishes. `Stack.push(C)`.
   - Backtrack to $B$. $B$ finishes. `Stack.push(B)`.
   - Backtrack to $A$. $A$ finishes. `Stack.push(A)`.
   - Final Stack (Top to Bottom): `[A, B, C]`.
2. **Transpose Graph ($G^T$):** Reverse every single edge.
   - New edges: $(B \to A), (C \to B), (A \to C)$.
3. **Pass 2 (DFS on $G^T$ using Stack Order):** Pop nodes from the Stack and run DFS on $G^T$. Each distinct DFS tree formed is one SCC.
   - Pop $A$. Run DFS on $G^T$.
   - $A \to C \to B$. ($B \to A$ is blocked because $A$ is visited).
   - DFS finishes. SCC Found: $\{A, C, B\}$.
4. **Conclusion:** Because the entire graph forms a cycle, Kosaraju's correctly grouped all 3 nodes into a single Strongly Connected Component.
