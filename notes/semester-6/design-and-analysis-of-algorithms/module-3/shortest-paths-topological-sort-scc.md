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

### Example 1: Bellman-Ford Algorithm Trace [April 2018]
**Problem:** Write down and explain Bellman-Ford algorithm by tracing it on a graph with nodes $\{S, A, B\}$ and edges $(S \to A, 4), (S \to B, 1), (B \to A, 2)$.
**Step-by-step Solution:**
1. **Algorithm Explanation:** 1) Initialize all distances to $\infty$, except $D[S]=0$. 2) Relax every single edge in the graph $V-1$ times. 3) Check for negative weight cycles by relaxing one more time; if any distance decreases, a cycle exists.
2. **Initialization:** $D[S]=0, D[A]=\infty, D[B]=\infty$. Edges: $e_1=(S,A,4), e_2=(S,B,1), e_3=(B,A,2)$.
3. **Pass 1 (Relax all edges):**
   - Relax $e_1 (S \to A)$: $D[S] + 4 = 4 < \infty$. Update $D[A]=4$.
   - Relax $e_2 (S \to B)$: $D[S] + 1 = 1 < \infty$. Update $D[B]=1$.
   - Relax $e_3 (B \to A)$: $D[B] + 2 = 1+2 = 3 < 4$. Update $D[A]=3$.
   - Distances after Pass 1: $D[S]=0, D[A]=3, D[B]=1$.
4. **Pass 2 (Relax all edges again):**
   - $V-1$ = 2 passes required. None of the distances change during Pass 2 because the shortest paths were already found.
5. **Final Distances:** $D[S]=0, D[B]=1, D[A]=3$.

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

---

### Previous Year Questions & Solutions

1. **"Write down and explain Bellman Ford algorithm..." [April 2018, July 2021]**
   - **Solution:**
     ```text
     BellmanFord(G, w, s):
         Initialize dist[v] = infinity for all v, dist[s] = 0
         for i = 1 to |V| - 1:
             for each edge (u, v) in E:
                 if dist[u] + w(u, v) < dist[v]:
                     dist[v] = dist[u] + w(u, v)
         
         // Check for negative-weight cycles
         for each edge (u, v) in E:
             if dist[u] + w(u, v) < dist[v]:
                 return "Graph contains a negative weight cycle"
         return dist
     ```
     **Explanation:**
     - **Concept:** Uses dynamic programming to compute single-source shortest paths. Unlike Dijkstra, Bellman-Ford handles negative edge weights.
     - **Mechanism:** Relaxes all $E$ edges $|V|-1$ times because a simple shortest path can contain at most $|V|-1$ edges. A $V^{th}$ pass checks if any distance can still decrease; if so, a negative cycle exists.
     - **Complexity:** Time: $O(V \cdot E)$, Space: $O(V)$.

2. **"What are different classification of edges based on DFS?" [Dec 2019, Sept 2020]**
   - **Solution:** During a DFS traversal of a directed graph, edges $u \to v$ are classified into four types based on the discovery and finishing times:
     1. **Tree Edge**: Edge in the DFS depth-first forest ($v$ is discovered for the first time from $u$).
     2. **Back Edge**: Edge connecting $u$ to an ancestor $v$ in the DFS tree. *Presence of a back-edge indicates a cycle.*
     3. **Forward Edge**: Non-tree edge connecting $u$ to a descendant $v$ in the DFS tree.
     4. **Cross Edge**: All other edges (connecting nodes in different DFS subtrees or parallel branches with no ancestor relationship).

3. **"Write Dijkstra's Single Source Shortest Path Algorithm." [July 2021, Sept 2020]**
   - **Solution:**
     ```text
     Dijkstra(G, w, s):
         Initialize dist[v] = infinity, visited[v] = false, dist[s] = 0
         Insert all vertices into Min-PriorityQueue Q keying on dist[]
         while Q is not empty:
             u = ExtractMin(Q)
             visited[u] = true
             for each neighbor v of u:
                 if not visited[v] and dist[u] + w(u,v) < dist[v]:
                     dist[v] = dist[u] + w(u,v)
                     DecreaseKey(Q, v, dist[v])
     ```
     - **Constraint:** Requires all edge weights to be non-negative ($w(u,v) \ge 0$).
     - **Complexity:** Time: $O((V + E) \log V)$ using Binary Min-Heap; $O(E + V \log V)$ using Fibonacci Heap.
