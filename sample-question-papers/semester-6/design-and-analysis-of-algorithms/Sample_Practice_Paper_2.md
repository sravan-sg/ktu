# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SIXTH SEMESTER B.TECH DEGREE EXAMINATION
### Course Code: CS302 | Course Name: DESIGN AND ANALYSIS OF ALGORITHMS
**Max. Marks: 100** | **Duration: 3 Hours**

---

### PART A
*Answer ALL questions. Each question carries 3 marks (Total: 12 Marks). Covers Modules I & II.*

1. **[Module 1]** Prove that $n^2 + 5n + 10 = \Theta(n^2)$ using the formal definition of Big-$\Theta$ notation. Find the constants $c_1, c_2,$ and $n_0$. `[3 Marks]`
2. **[Module 1]** Calculate the tight Big-$\Theta$ time complexity of the following code block:
   ```text
   count = 0
   for i = 1 to n do:
       for j = 1 to n do:
           k = n
           while k >= 1 do:
               count = count + 1
               k = k / 2
   ``` `[3 Marks]`
3. **[Module 2]** Apply Master's Theorem to solve the recurrence relation $T(n) = 2T(n/4) + \sqrt{n}$. `[3 Marks]`
4. **[Module 2]** Define the fundamental operations `MAKE-SET(x)`, `UNION(x, y)`, and `FIND-SET(x)` in Disjoint Set data structures. `[3 Marks]`

---

### PART B
*Answer ANY TWO full questions. Each question carries 9 marks (Total: 18 Marks). Covers Modules I & II.*

5. **(a)** Solve the recurrence relation $T(n) = 2T(n/2) + n^2$ with base case $T(1) = 1$ using the **Recursion Tree Method**. Show level costs and tree height derivation. `[5 Marks]`  
   **(b)** Analyze the Best-case, Worst-case, and Average-case time complexities of **Insertion Sort** with explicit step counts for each case. `[4 Marks]`

6. Construct an **AVL Tree** by inserting the following sequence of keys into an initially empty tree: `30, 40, 50, 10, 20, 25, 28, 22`. Show the tree state after each insertion and specify the rotation type (LL, RR, LR, RL) performed. `[9 Marks]`

7. **(a)** Construct a **Red-Black Tree** by inserting keys `21, 15, 10, 5, 12, 17` into an initially empty tree. Trace all recoloring and rotation steps clearly. `[6 Marks]`  
   **(b)** Explain the deletion process in B-Trees. Differentiate between borrowing a key from a sibling versus merging nodes. `[3 Marks]`

---

### PART C
*Answer ALL questions. Each question carries 3 marks (Total: 12 Marks). Covers Modules III & IV.*

8. **[Module 3]** Define **Strongly Connected Components (SCC)** in a directed graph. State the time complexity of Kosaraju's algorithm. `[3 Marks]`
9. **[Module 3]** Explain **Breadth-First Search (BFS)** traversal using a FIFO Queue. Show why its time complexity is $O(V+E)$ when represented via Adjacency Lists. `[3 Marks]`
10. **[Module 4]** Formulate the recurrence relation for 2-way **Merge Sort**. Analyze its time complexity using Divide and Conquer principles. `[3 Marks]`
11. **[Module 4]** Differentiate between **Top-Down Memoization** and **Bottom-Up Tabulation** approaches in Dynamic Programming. `[3 Marks]`

---

### PART D
*Answer ANY TWO full questions. Each question carries 9 marks (Total: 18 Marks). Covers Modules III & IV.*

12. **(a)** Trace **Dijkstra's Algorithm** to find the shortest path from source node $S$ to all other nodes in a directed weighted graph $G$ with vertices $\{S, A, B, C, D, E\}$ and edges: $(S \to A, 7), (S \to B, 2), (B \to A, 3), (B \to C, 8), (A \to C, 1), (A \to D, 4), (C \to D, 2), (D \to E, 5)$. Show min-heap extract operations. `[6 Marks]`  
    **(b)** Write down the algorithm for **Topological Sorting** using DFS finishing times. `[3 Marks]`

13. **(a)** Solve the **0/1 Knapsack Problem** using Dynamic Programming. Given 3 items with profits $P = [10, 15, 40]$, weights $W = [1, 2, 3]$, and maximum capacity $W_{max} = 5$:
    1. Construct the 2D DP table $V[i, w]$.
    2. Trace back to find the selected item set. `[6 Marks]`  
    **(b)** Explain how **Bellman-Ford Algorithm** detects negative-weight cycles in a graph. `[3 Marks]`

14. **(a)** Explain **Strassen's Matrix Multiplication**. Write down the 7 matrix product formulas ($P_1$ through $P_7$) and explain how it reduces scalar multiplications from 8 to 7. `[6 Marks]`  
    **(b)** Write the recursive **DFS algorithm** pseudocode and trace its call stack on a simple triangle graph. `[3 Marks]`

---

### PART E
*Answer ANY FOUR full questions. Each question carries 10 marks (Total: 40 Marks). Covers Modules V & VI.*

15. **(a)** Trace **Kruskal's Algorithm** to find the Minimum Spanning Tree (MST) on an undirected graph with vertices $\{1, 2, 3, 4, 5, 6\}$ and edges $(1-2, 4), (1-3, 2), (2-3, 1), (2-4, 5), (3-4, 8), (3-5, 10), (4-5, 2), (4-6, 6), (5-6, 3)$. Show Disjoint-Set `UNION` and `FIND` operations. `[6 Marks]`  
    **(b)** Compare the **Control Abstraction for Greedy Strategy** against the **Control Abstraction for Dynamic Programming**. `[4 Marks]`

16. **(a)** Provide a detailed comparative matrix between **Prim's Algorithm** and **Kruskal's Algorithm** across 5 distinct parameters (Approach, Graph density suitability, Data structures used, Cycle check method, Time complexity). `[5 Marks]`  
    **(b)** Solve the **Fractional Knapsack Problem** using the Greedy method for $W = 50$, items $P = [60, 100, 120]$, $W_{arr} = [10, 20, 30]$. Show ratio calculation and item fractions taken. `[5 Marks]`

17. **(a)** Explain the **8-Queens Problem** using Backtracking. State the mathematical condition to check diagonal conflicts between queen at $(i, j)$ and candidate queen at $(r, c)$. Draw the State Space Tree for 4 Queens. `[6 Marks]`  
    **(b)** Explain the **0/1 Knapsack Problem** using Backtracking. Formulate the bounding function used to prune nodes in the state space tree. `[4 Marks]`

18. **(a)** Explain the **Least-Cost Branch and Bound (LCBB)** strategy for the **Travelling Salesman Problem (TSP)**. Given the cost matrix $C$:
    $$C = \begin{bmatrix} \infty & 20 & 30 & 10 \\ 15 & \infty & 16 & 4 \\ 3 & 5 & \infty & 2 \\ 19 & 6 & 18 & \infty \end{bmatrix}$$
    1. Calculate the initial reduced matrix and Lower Bound $L_0$.
    2. Calculate reduced lower bounds for child nodes corresponding to paths $1 \to 2, 1 \to 3, 1 \to 4$. `[7 Marks]`  
    **(b)** Differentiate between **State Space Tree** and **Solution Space** in combinatorial optimization. `[3 Marks]`

19. **(a)** Define computational complexity classes **P**, **NP**, **NP-Hard**, and **NP-Complete**. Give two benchmark problem examples for each class. `[5 Marks]`  
    **(b)** Define **Non-Deterministic Algorithms**. Explain `choice()`, `failure()`, and `success()` functions. Write non-deterministic pseudocode for the **Clique Problem**. `[5 Marks]`

20. **(a)** Explain the concept of **Polynomial-Time Reduction** ($A \le_P B$). Show how reducing $3\text{-SAT}$ to **Vertex-Cover** proves Vertex-Cover is NP-Complete. `[5 Marks]`  
    **(b)** Define the **Hamiltonian Cycle Problem**. Explain why it belongs to class NP and outline why it is NP-Complete. `[5 Marks]`
