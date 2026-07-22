CS302 Design and Analysis of Algorithms

Module III: Graph Algorithms & Traversals

1. Graphs: DFS and BFS Traversals & Complexity

Explanation

A graph is a data structure consisting of vertices (nodes) and edges (connections between nodes).

**Graph Representations:**
**Refferl video:**https://youtu.be/5hPfm_uqXmw?si=3MZaUDSNCFp_ME62
*   **Adjacency Matrix (The Grid Approach):** Imagine a grid (like a spreadsheet) where both the rows and the columns represent your nodes. If Node A is connected to Node B, you put a '1' in the box where Row A and Column B meet. If they aren't connected, you put a '0'. It's very fast to look up if two nodes are connected, but it takes up a lot of memory because you have to draw the whole grid even if there are very few connections.
*   **Adjacency List (The Friends List Approach):** Imagine every node has its own personal "friends list" (a linked list). For Node A, you just write down the names of the nodes it is directly connected to. This is much better for saving memory when most nodes only have a few connections, because you only write down the connections that actually exist.


**Refferl document:**https://share.gemini.google/70HbdAj0Qrif
**Refferl video:**https://youtu.be/vf-cxgUXcMk?si=S6nbNN2XWYkXpWoL
Graph traversal is the process of visiting every vertex and edge in a systematic way. There are two primary algorithms for this:
Breadth-First Search (BFS): Explores the graph level by level. It starts at a source node, visits all its immediate neighbors, then visits all the neighbors of those neighbors. It uses a Queue (First-In-First-Out) data structure to keep track of nodes to visit next.
Depth-First Search (DFS): Explores as far down a single path as possible before backtracking. It dives deep into the graph. It uses a Stack (Last-In-First-Out) data structure, or system recursion, to keep track of the path.

**Types of Edges in Traversals (A Quick Summary):**
During traversals, edges are classified based on how they are encountered:
*   **Tree Edge:** The edges you actually travel on to discover new, unvisited nodes. They build the main structure of your search.
*   **Back Edge (Mainly DFS):** An edge leading back to a node you are currently still exploring (an ancestor). Finding a back edge means there is a cycle (a loop) in the graph!
*   **Forward Edge (Mainly DFS):** An edge leading forward to a node you've already fully explored (a descendant) through a different, longer path.
*   **Cross Edge:** An edge between two nodes that don't have a direct parent/child relationship (e.g., jumping between different branches of your search). BFS often finds cross edges connecting nodes on the same level.

Time and Space Complexity:
Time Complexity: For both BFS and DFS, the time complexity is $\Theta(V + E)$ when the graph is represented as an adjacency list (where $V$ is the number of vertices and $E$ is the number of edges). If an adjacency matrix is used, the complexity becomes $\Theta(V^2)$.
Space Complexity: $O(V)$ in the worst case to store the Queue (for BFS), the Stack/Recursion Tree (for DFS), and the visited array.

Example

Imagine a pyramid of friends. You are at the top.
BFS: You ask all your direct friends a question. Then, you ask all of their friends.
DFS: You ask your best friend, who asks their best friend, who asks their best friend, continuing down the chain until someone says "I don't know," at which point you backtrack.

Applications & Use Cases

BFS: GPS Navigation finding the shortest path (in unweighted graphs), Web Crawlers building search engine indexes, and broadcasting packets in computer networks.
DFS: Solving mazes, detecting cycles in graphs (preventing infinite loops), and analyzing topological ordering.

3 Solved Examples

Example 1.1: BFS Traversal Trace

Problem: Given an unweighted, undirected graph defined by the adjacency list:
$A \rightarrow [B, C]$
$B \rightarrow [A, D, E]$
$C \rightarrow [A, F]$
$D, E, F \rightarrow \text{leaf nodes}$.
Perform a BFS starting at node $A$.

Solution:

Initialize a Queue and a Visited list.

Enqueue $A$. Mark $A$ visited. (Queue: $[A]$, Visited: $[A]$)

Dequeue $A$. Enqueue unvisited neighbors $B, C$. (Queue: $[B, C]$, Visited: $[A, B, C]$)

Dequeue $B$. Enqueue its unvisited neighbors $D, E$. (Queue: $[C, D, E]$, Visited: $[A, B, C, D, E]$)

Dequeue $C$. Enqueue its unvisited neighbor $F$. (Queue: $[D, E, F]$, Visited: $[A, B, C, D, E, F]$)

Dequeue $D, E, F$. They have no unvisited neighbors. Queue is empty.

Final BFS Order: $A, B, C, D, E, F$

Example 1.2: DFS Traversal Trace
Problem: Using the exact same graph from Example 1.1, perform a DFS starting at node $A$. Always visit alphabetically first.
Solution:

Start at $A$. Mark visited. Output $A$.

Visit first unvisited neighbor of $A$, which is $B$. Output $B$.

Visit first unvisited neighbor of $B$, which is $D$. Output $D$.

$D$ has no unvisited neighbors. Backtrack to $B$.

Visit next unvisited neighbor of $B$, which is $E$. Output $E$.

$E$ has no unvisited neighbors. Backtrack to $B$, then to $A$.

Visit next unvisited neighbor of $A$, which is $C$. Output $C$.

Visit $C$'s neighbor, $F$. Output $F$.

Final DFS Order: $A, B, D, E, C, F$

Example 1.3: Complexity Calculation
Problem: A social network represents $10,000$ users as vertices, and their friendships as $50,000$ edges using an adjacency list. A feature requires running BFS to find a connection. Calculate the worst-case number of operations mathematically bounds.
Solution:

Identify the variables: $V = 10,000$ and $E = 50,000$.

State the complexity for an adjacency list: $O(V + E)$.

Substitute the values: $10,000 + 50,000 = 60,000$ operations.

Conclusion: The algorithm will scale linearly with the sum of users and connections, requiring roughly bounded $\sim 60,000$ primitive loop iterations, avoiding the $O(V^2)$ cost of a $100,000,000$ cell adjacency matrix.

2. Minimum Cost Spanning Trees (MCST)

Explanation

A Spanning Tree of a connected, undirected graph is a subgraph that includes all the vertices of the original graph but has no cycles (it must be a tree). A graph can have many spanning trees.
A Minimum Cost Spanning Tree (MCST) is a spanning tree where the sum of the weights of all its edges is as small as possible.

Key Properties: If a graph has $V$ vertices, any spanning tree will have exactly $V - 1$ edges.

(Note: The specific algorithms to find MCSTs—Kruskal's and Prim's—are covered deeply in Module V under Greedy Algorithms, but we will demonstrate their logic here as SSSP foundations).

Example
Imagine 4 cities that need to be connected to a power grid. There are various costs to lay cables between different cities. The MCST is the cheapest possible network of cables that ensures every single city has power, without building redundant loop-backs.

Applications & Use Cases
Network Design: Telecommunications networks, water supply networks, and electrical grids.
Approximation Algorithms: Used as a baseline to solve the NP-Hard Travelling Salesman Problem.
Cluster Analysis: Used in machine learning to group similar data points.

3 Solved Examples
Example 2.1: Finding the MCST Cost (Kruskal's Logic)
Problem: A graph has 3 vertices ($X, Y, Z$). Edges and weights are: $(X-Y, 10)$, $(Y-Z, 5)$, $(X-Z, 15)$. Find the minimum cost to connect all nodes.
Solution:

Sort edges by weight: $(Y-Z, 5)$, $(X-Y, 10)$, $(X-Z, 15)$.

We need $V - 1 = 3 - 1 = 2$ edges.

Pick the smallest edge: $(Y-Z, 5)$. Nodes $Y, Z$ connected.

Pick the next smallest: $(X-Y, 10)$. Node $X$ connected. No cycles formed.

Total Cost: $5 + 10 = 15$.

Final Answer: The Minimum Cost is $15$.

Example 2.2: Cycle Property Validation
Problem: Prove whether the heaviest edge in a cycle can ever be part of a unique Minimum Spanning Tree. Graph: $A-B (2), B-C (3), C-A (4)$.
Solution:

The edges form a cycle: $A-B-C-A$.

The heaviest edge is $C-A$ with weight $4$.

If we include $C-A$, we must remove a lighter edge (like $2$ or $3$) to maintain a tree (no cycles). This would increase the total cost.

Therefore, removing $C-A$ and keeping $A-B$ and $B-C$ yields a cost of $5$.

Conclusion: By the MCST Cycle Property, the maximum weight edge in any cycle will never be in the unique Minimum Spanning Tree.

Example 2.3: Cut Property Validation
Problem: Given vertices $S = \{A, B\}$ and $V-S = \{C, D\}$. The crossing edges between these two sets are $(A-C, 8)$, $(A-D, 12)$, and $(B-C, 5)$. Which edge is guaranteed to be in the MCST?
Solution:

The Cut Property states that for any cut of a graph, the crossing edge with the absolute minimum weight is guaranteed to belong to the MCST.

Compare the crossing weights: $8, 12, 5$.

The minimum weight is $5$ (Edge $B-C$).

Final Answer: Edge $(B-C, 5)$ is guaranteed to be in the MCST.



3. Single Source Shortest Path Algorithms (Dijkstra's)
Explanation
The Single Source Shortest Path (SSSP) problem asks: Given a specific starting node (source), what is the shortest possible path (lowest total edge weight) to every other node in the graph?
The most famous algorithm for this is Dijkstra's Algorithm. It maintains a list of the minimum known distance to every node. It continually visits the unvisited node with the smallest known distance, and checks if it can update the distances to its neighbors to be shorter (a process called relaxation).
Limitation: Dijkstra's algorithm fails if the graph contains negative weight edges.
Time Complexity: $O((V + E) \log V)$ when implemented efficiently with a Min-Priority Queue.

Example
Imagine flying from New York (Source). You want to know the cheapest flight cost to London, Tokyo, and Paris. Some layover combinations might be cheaper than direct flights. Dijkstra calculates the absolute cheapest route to all of them.

Applications & Use Cases
Mapping/GPS: Finding the fastest driving route between your house and all nearby restaurants.
IP Routing: OSPF (Open Shortest Path First) protocol uses Dijkstra's to route data packets across the internet.

3 Solved Examples

Example 3.1: Dijkstra Trace (Basic)
Problem: Graph with nodes $S, A, B$. Edges: $S \rightarrow A (5)$, $S \rightarrow B (10)$, $A \rightarrow B (2)$. Find shortest paths from $S$.
Solution:

Initialize distances: $S=0, A=\infty, B=\infty$.

Visit $S$ (dist $0$). Relax neighbors: $A = 0+5 = 5$. $B = 0+10 = 10$.

Unvisited nodes are $A(5)$ and $B(10)$. Pick smallest: $A$.

Visit $A$ (dist $5$). Relax neighbors: The path to $B$ via $A$ is $5(\text{to A}) + 2(\text{A to B}) = 7$. Since $7 < 10$, update $B$'s distance to $7$.

Final Answer: Shortest distances from $S$ are $A=5, B=7$.

Example 3.2: Relaxation Step
Problem: During Dijkstra's algorithm, the current known distance to node $U$ is $15$. The known distance to node $V$ is $25$. There is a directed edge from $U \rightarrow V$ with weight $8$. Demonstrate the relaxation step.
Solution:

The relaxation formula is: $\text{if } dist[U] + weight(U,V) < dist[V] \text{, then update } dist[V]$.

Calculate new possible distance: $15 + 8 = 23$.

Compare with current distance: $23 < 25$.

Final Answer: The relaxation is successful. The new shortest distance to $V$ is updated from $25$ to $23$, and $U$ becomes the predecessor of $V$.

Example 3.3: Negative Weight Limitation
Problem: Graph: $S \rightarrow A (5)$, $S \rightarrow B (2)$, $B \rightarrow A (-5)$. Run Dijkstra's from $S$.
Solution:

Visit $S(0)$. Relax neighbors: $A=5, B=2$.

Visit smallest unvisited, $B(2)$. Relax neighbor $A$: $2 + (-5) = -3$. Update $A$ to $-3$.

Visit $A(-3)$. No neighbors to relax.

Wait! Dijkstra assumes once a node is visited, its shortest path is final. If the graph had a loop or further negative cycles, Dijkstra would fail to find the true shortest path because it commits greedily. (Note: Bellman-Ford solves this, covered in Module IV).

Conclusion: Dijkstra finalized $B$ before considering negative paths. It only works on non-negative graphs.

4. Topological Sorting
Explanation
Topological Sorting is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge $U \rightarrow V$, vertex $U$ comes before vertex $V$ in the ordering.
Note: A topological sort is only possible if the graph has no cycles.

Kahn's Algorithm (In-degree approach):
Calculates the "in-degree" (number of incoming edges) for all nodes. Nodes with an in-degree of 0 have no prerequisites and are added to a queue, processed, and removed, reducing the in-degree of their neighbors.
Time Complexity: $O(V + E)$.

Example

Getting dressed. You must put on your socks ($U$) before your shoes ($V$). The directed edge is $\text{Socks} \rightarrow \text{Shoes}$. A topological sort ensures "Socks" appears before "Shoes" in your instruction manual.

Applications & Use Cases
Task Scheduling: Determining the order of tasks in a project management system where some tasks depend on others.
Software Compilation: Determining the compilation order of files (e.g., make files) or resolving package dependencies (apt-get install).
University Prerequisites: Creating a valid graduation path taking prerequisite courses into account.

3 Solved Examples
Example 4.1: Kahn's Algorithm Trace
Problem: DAG with edges: $1 \rightarrow 2$, $1 \rightarrow 3$, $2 \rightarrow 4$, $3 \rightarrow 4$. Find the topological sort.
Solution:

Calculate in-degrees: $1(0), 2(1), 3(1), 4(2)$.

Queue starts with in-degree 0: Node 1. (Output: 1)

Remove 1 and its edges. Update in-degrees: $2(0), 3(0), 4(2)$.

Add 2 and 3 to queue.

Dequeue 2. Remove edges. Update in-degree: $4(1)$. (Output: 1, 2)

Dequeue 3. Remove edges. Update in-degree: $4(0)$. (Output: 1, 2, 3)

Add 4 to queue. Dequeue 4. (Output: 1, 2, 3, 4)

Final Answer: Valid Sort: $1, 2, 3, 4$ (Note: $1, 3, 2, 4$ is also valid).

Example 4.2: DFS Approach Trace
Problem: Given edges: $A \rightarrow B$, $B \rightarrow C$. Use DFS to find topological sort.
Solution:

Run DFS. Start at $A$. Go to $B$. Go to $C$.

$C$ has no unvisited neighbors. Push $C$ to a Stack. Backtrack to $B$.

$B$ has no unvisited neighbors. Push $B$ to Stack. Backtrack to $A$.

$A$ has no unvisited neighbors. Push $A$ to Stack.

Pop all items off the Stack.

Final Answer: Stack pops $A$, then $B$, then $C$. Sort is $A, B, C$.

Example 4.3: Cycle Detection (Failure Case)
Problem: Apply Kahn's Algorithm to: $1 \rightarrow 2$, $2 \rightarrow 3$, $3 \rightarrow 1$.
Solution:

Calculate in-degrees: $1(1), 2(1), 3(1)$.

Are there any nodes with an in-degree of 0? No.

The Queue is empty, but we haven't outputted any nodes.

Conclusion: Because the algorithm terminates with unvisited nodes, we have mathematically proven a cycle exists. Topological sorting is impossible.



5. Strongly Connected Components (SCC)
Explanation
In a directed graph, a Strongly Connected Component (SCC) is a maximal sub-graph where every single vertex is reachable from every other vertex within that sub-graph. If you pick any two nodes $A$ and $B$ in an SCC, there is a path from $A$ to $B$ AND a path from $B$ to $A$.
Kosaraju's Algorithm is the standard method for finding SCCs. It operates in 3 steps:
Perform DFS and push vertices to a stack based on their finishing times.
Reverse (transpose) the direction of all edges in the graph.
Pop vertices off the stack and run a second DFS on the reversed graph. Each successful DFS pass discovers one distinct SCC.
Time Complexity: $\Theta(V + E)$ because it essentially performs two standard DFS passes.

Example
Imagine a one-way road system in a city. An SCC is a specific neighborhood where you can drive from any house to any other house without ever breaking the one-way street laws.

Applications & Use Cases
Social Networks: Finding clusters or cliques of users who mutually follow each other.
Software Engineering: Identifying cyclic dependencies in code architecture that need to be refactored.
Ecology: Analyzing food webs to find closed ecosystems.

3 Solved Examples
Example 5.1: Kosaraju Step 1 (Finishing Times)
Problem: Graph: $A \rightarrow B, B \rightarrow C, C \rightarrow A$, and $C \rightarrow D$. Perform the first pass of Kosaraju's algorithm starting at $A$.
Solution:

DFS from $A \rightarrow B \rightarrow C \rightarrow D$.

$D$ finishes (no outgoing edges). Push $D$ to Stack.

Backtrack to $C$. $C$'s other neighbor $A$ is visited. $C$ finishes. Push $C$ to Stack.

Backtrack to $B$. $B$ finishes. Push $B$ to Stack.

Backtrack to $A$. $A$ finishes. Push $A$ to Stack.

Final Stack: Top $[A, B, C, D]$ Bottom.

Example 5.2: Kosaraju Step 2 & 3 (Transpose and Find SCCs)
Problem: Continue Example 5.1. Reverse the graph and find the SCCs.
Solution:

Reversed edges: $B \rightarrow A, C \rightarrow B, A \rightarrow C, D \rightarrow C$.

Pop Top of Stack: $A$. Run DFS on reversed graph.

DFS($A$) visits $C$, which visits $B$. $B$ tries to visit $A$ (visited).

The first SCC is $\{A, B, C\}$.

Pop $B$ and $C$ (already visited, ignore).

Pop $D$. Run DFS($D$). $D$ tries to visit $C$ (already visited).

The second SCC is $\{D\}$.

Final Answer: Two SCCs found: $\{A, B, C\}$ and $\{D\}$.

Example 5.3: Component Graph Generation
Problem: Once SCCs are found, how is the "Meta-Graph" (Component Graph) structured?
Solution:

In the previous example, we found $SCC_1 = \{A, B, C\}$ and $SCC_2 = \{D\}$.

Look at the original edges connecting vertices from $SCC_1$ to $SCC_2$. We had original edge $C \rightarrow D$.

Shrink the SCCs into single super-nodes. Draw a directed edge between them based on original crossing edges.

Final Answer: The Meta-Graph is $SCC_1 \rightarrow SCC_2$. Crucial Theorem: The Meta-Graph of SCCs is always a Directed Acyclic Graph (DAG). If it had a cycle, the two SCCs would just merge into one larger SCC.
