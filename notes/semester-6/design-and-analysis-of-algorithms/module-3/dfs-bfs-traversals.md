# Module 3 — Topic 1: Graph Traversals (DFS & BFS)

> **Module 3**: Graph Algorithms  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
A **Graph** is a mathematical structure used to model relationships (edges) between objects (vertices/nodes). Unlike trees, graphs can contain cycles (loops) and disconnected components. 
A **Graph Traversal** is a systematic algorithm used to visit every vertex in a graph exactly once without getting trapped in infinite loops. There are two primary paradigms:
- **Depth-First Search (DFS)**: Navigates by diving as deep as possible down a single path. When it hits a dead end, it backtracks to the last fork in the road and tries another path. It uses a **Stack** (or recursion) to remember where to backtrack.
- **Breadth-First Search (BFS)**: Navigates by exploring all immediate neighbors of a node before moving deeper. It explores the graph level-by-level, radiating outward from the start node. It uses a **Queue** to keep track of the exploration frontier.

Both algorithms keep a `visited` array to prevent revisiting nodes and getting stuck in cycles.

### Example
Imagine you are exploring a dark, branching hedge maze looking for an exit:
- **DFS**: You hold your right hand on the wall and walk. If you hit a dead end, you turn around and walk back until you find a path you haven't taken yet.
- **BFS**: You stand at the entrance and deploy 10 drones. They fly 1 meter in every direction. Then they fly another meter. They map the maze layer by layer in expanding concentric circles.

### Applications & Use Cases
- **Maze Solvers & Puzzles (DFS)**: Backtracking through a Sudoku board or finding a path out of a maze inherently uses DFS to explore potential decision branches.
- **GPS Routing & Social Networks (BFS)**: Google Maps or LinkedIn uses BFS to find the absolute shortest path (fewest edges) between two cities or to find "2nd degree connections".
- **Garbage Collection (DFS/BFS)**: Modern programming languages like Java or Python use graph traversals to find all objects in memory that are no longer reachable from the root, safely deleting them.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: BFS Traversal Trace
**Problem:** Given an unweighted, undirected graph with nodes $A, B, C, D, E, F$ and edges $(A,B), (A,C), (B,D), (C,E), (D,E), (D,F)$, trace the Breadth-First Search starting from node $A$. Assume alphabetical tie-breaking.
**Step-by-step Solution:**
1. **Initialization:** Queue $Q = [A]$. Visited = $\{A\}$.
2. **Step 1:** Dequeue $A$. Its unvisited neighbors are $B$ and $C$.
   - Mark $B, C$ visited. Enqueue them. $Q = [B, C]$.
   - BFS Order so far: `A`
3. **Step 2:** Dequeue $B$. Its unvisited neighbor is $D$. 
   - Mark $D$ visited. Enqueue it. $Q = [C, D]$.
   - BFS Order so far: `A, B`
4. **Step 3:** Dequeue $C$. Its unvisited neighbor is $E$. 
   - Mark $E$ visited. Enqueue it. $Q = [D, E]$.
   - BFS Order so far: `A, B, C`
5. **Step 4:** Dequeue $D$. Its unvisited neighbor is $F$. (Neighbor $E$ is already visited).
   - Mark $F$ visited. Enqueue it. $Q = [E, F]$.
   - BFS Order so far: `A, B, C, D`
6. **Step 5 & 6:** Dequeue $E$, no unvisited neighbors. Dequeue $F$, no unvisited neighbors.
   - Final BFS Order: **A, B, C, D, E, F**.

### Example 2: DFS Traversal Trace (Recursive)
**Problem:** Using the exact same graph as Example 1, trace the Depth-First Search starting from node $A$. Assume alphabetical tie-breaking.
**Step-by-step Solution:**
1. **Start at A:** Mark $A$ visited. Neighbors are $B, C$. Alphabetically, go to $B$.
   - DFS Order: `A`
2. **Dive to B:** Mark $B$ visited. Neighbors are $A, D$. $A$ is visited, so go to $D$.
   - DFS Order: `A, B`
3. **Dive to D:** Mark $D$ visited. Neighbors are $B, E, F$. $B$ is visited. Alphabetically, go to $E$.
   - DFS Order: `A, B, D`
4. **Dive to E:** Mark $E$ visited. Neighbors are $C, D$. $D$ is visited, so go to $C$.
   - DFS Order: `A, B, D, E`
5. **Dive to C:** Mark $C$ visited. Neighbors are $A, E$. Both are visited. **DEAD END**.
   - Backtrack from $C \rightarrow E$.
   - Backtrack from $E \rightarrow D$.
6. **Resume at D:** $D$'s last unvisited neighbor is $F$.
   - Dive to $F$. Mark $F$ visited.
   - DFS Order: `A, B, D, E, C, F`.
7. **Finish:** All nodes visited.
   - Final DFS Order: **A, B, D, E, C, F**.

### Example 3: Time and Space Complexity Proof
**Problem:** Mathematically prove the Time and Space Complexity of a standard BFS traversal on a graph represented as an Adjacency List with $V$ vertices and $E$ edges.
**Step-by-step Solution:**
1. **Space Complexity:**
   - BFS requires a Queue data structure to hold nodes waiting to be processed. In the worst case (e.g., a star graph where a central node connects to all others), the Queue holds $V-1$ nodes.
   - It also requires a boolean `visited` array of size $V$.
   - Thus, Space Complexity $= O(V)$.
2. **Time Complexity:**
   - The outer `while (queue is not empty)` loop dequeues each vertex exactly once. This takes $O(V)$ time.
   - Inside the loop, the algorithm iterates through the neighbor list of the dequeued vertex. Across the *entire execution* of the algorithm, the total number of items in all neighbor lists combined is $2E$ for an undirected graph (or $E$ for a directed graph).
   - Therefore, the inner loop body executes a total of $O(E)$ times globally.
   - Adding the vertex processing and edge scanning together, the Time Complexity is strictly bounded by **$O(V + E)$**.
