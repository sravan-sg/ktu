# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SIXTH SEMESTER B.TECH DEGREE EXAMINATION
### Course Code: CS302 | Course Name: DESIGN AND ANALYSIS OF ALGORITHMS
**Max. Marks: 100** | **Duration: 3 Hours**

---

### PART A
*Answer ALL questions. Each question carries 3 marks (Total: 12 Marks). Covers Modules I & II.*

1. **[Module 1]** Is $3^{n+1} = O(3^n)$? Is $3^{2n} = O(3^n)$? Justify your answers using the formal definition of Big-O notation. `[3 Marks]`
2. **[Module 1]** Calculate the tight Big-$\Theta$ time complexity of the following code snippet:
   ```text
   count = 0
   for i = 1 to n do:
       j = 1
       while j < n do:
           count = count + 1
           j = j * 2
   ``` `[3 Marks]`
3. **[Module 2]** State Master's Theorem. Apply it to determine the asymptotic time bound of the recurrence $T(n) = 3T(n/3) + n^2$. `[3 Marks]`
4. **[Module 2]** Explain the **Union by Rank** (weighted rule) and **Path Compression** (collapsing rule) heuristics in Disjoint Set data structures. What is the combined amortized time complexity per operation? `[3 Marks]`

---

### PART B
*Answer ANY TWO full questions. Each question carries 9 marks (Total: 18 Marks). Covers Modules I & II.*

5. **(a)** Solve the recurrence relation $T(n) = T(n-1) + n^2$ with base case $T(1) = 1$ using the **Iteration (Unrolling) Method**. Express the final result in Big-$\Theta$ notation. `[5 Marks]`  
   **(b)** Differentiate between fixed space complexity and auxiliary space complexity. Compare the auxiliary space complexity of recursive Fibonacci versus iterative Fibonacci. `[4 Marks]`

6. Construct an **AVL Tree** by inserting the following sequence of keys into an initially empty tree: `50, 20, 60, 10, 8, 15, 30, 25`. Show the tree structure and specify the exact rotation type (LL, RR, LR, RL) performed at each step to restore height balance. `[9 Marks]`

7. **(a)** Construct a **Red-Black Tree** by inserting the following sequence of keys into an initially empty tree: `15, 13, 12, 10, 8, 9`. Trace the color changes (Red/Black) and rotations required after each insertion to maintain Red-Black properties. `[6 Marks]`  
   **(b)** Define a B-Tree of order $m$. Explain why B-Trees are preferred over Binary Search Trees for disk-based database indexing systems. `[3 Marks]`

---

### PART C
*Answer ALL questions. Each question carries 3 marks (Total: 12 Marks). Covers Modules III & IV.*

8. **[Module 3]** Define **Topological Sort** of a Directed Acyclic Graph (DAG). Trace Kahn's in-degree algorithm on a DAG with vertices $\{1, 2, 3, 4\}$ and directed edges $(1 \to 2), (1 \to 3), (2 \to 4), (3 \to 4)$. `[3 Marks]`
9. **[Module 3]** Differentiate between the four types of edges in a DFS traversal of a directed graph: **Tree Edges**, **Back Edges**, **Forward Edges**, and **Cross Edges**. Which edge type indicates a cycle? `[3 Marks]`
10. **[Module 4]** State the **Principle of Optimality** in Dynamic Programming. Give an example of a graph problem where the Principle of Optimality fails. `[3 Marks]`
11. **[Module 4]** Write down the general **Control Abstraction** pseudocode for the **Divide and Conquer** paradigm (`Algorithm DAndC(P)`). `[3 Marks]`

---

### PART D
*Answer ANY TWO full questions. Each question carries 9 marks (Total: 18 Marks). Covers Modules III & IV.*

12. **(a)** Trace the **Bellman-Ford Algorithm** to find the single-source shortest path from source vertex $S$ to all other vertices in a directed graph $G=(V,E)$ with vertices $\{S, A, B, C\}$ and directed weighted edges: $(S \to A, 6), (S \to B, 5), (A \to C, -2), (B \to A, -2), (B \to C, 1)$. Show distance updates after each pass. `[6 Marks]`  
    **(b)** Explain **Kosaraju's Algorithm** for finding Strongly Connected Components (SCCs) in a directed graph using two passes of DFS. `[3 Marks]`

13. **(a)** Given a chain of four matrices $A_1, A_2, A_3, A_4$ with dimensions $10 \times 20, 20 \times 5, 5 \times 15, 15 \times 30$ respectively. Use **Dynamic Programming** to construct the cost table $m[i,j]$ and split table $s[i,j]$ to find the minimum number of scalar multiplications and the optimal parenthesization. `[6 Marks]`  
    **(b)** Explain **Strassen's Matrix Multiplication** algorithm. Formulate its recurrence equation, solve it using Master's Theorem, and compare its asymptotic complexity against standard $O(n^3)$ matrix multiplication. `[3 Marks]`

14. **(a)** Write **Dijkstra's Algorithm** for Single-Source Shortest Path using a Min-Priority Queue. Trace the algorithm on a graph with vertices $\{A, B, C, D, E\}$, source $A$, and weighted edges $(A \to B, 4), (A \to C, 2), (B \to C, 1), (B \to D, 5), (C \to D, 8), (C \to E, 10), (D \to E, 2)$. `[6 Marks]`  
    **(b)** Provide a comprehensive comparative matrix between **Divide and Conquer** and **Dynamic Programming** across 5 distinct criteria (Subproblem independence, Solution direction, Memory requirements, Optimization focus, and Example applications). `[3 Marks]`

---

### PART E
*Answer ANY FOUR full questions. Each question carries 10 marks (Total: 40 Marks). Covers Modules V & VI.*

15. **(a)** Formulate the **Fractional Knapsack Problem**. Given a knapsack with maximum weight capacity $W = 60$ and 4 items with profits $P = [30, 100, 120, 160]$ and weights $W_{arr} = [10, 20, 30, 40]$:
    1. Calculate profit-to-weight ratios.
    2. Trace the Greedy selection step-by-step.
    3. Compute the maximum achievable profit. `[6 Marks]`  
    **(b)** Write down **Prim's Algorithm** for Minimum Spanning Tree (MST). Trace it starting from vertex $1$ on a graph with vertices $\{1, 2, 3, 4, 5\}$ and weighted edges $(1-2, 2), (1-3, 3), (2-3, 1), (2-4, 4), (3-5, 5), (4-5, 2)$. Calculate total MST cost. `[4 Marks]`

16. **(a)** Trace **Kruskal's Algorithm** on the same graph as Question 15(b). Show edge sorting, cycle detection using Disjoint-Set Union-Find operations, and final edge selection for the MST. `[5 Marks]`  
    **(b)** Prove the **Cut Property** of Minimum Spanning Trees by contradiction: Let $e = (u,v)$ be the minimum-weight edge crossing a cut $(S, V \setminus S)$ in connected graph $G$. Prove that $e$ belongs to some MST of $G$. `[5 Marks]`

17. **(a)** State the **N-Queens Problem**. Write the complete recursive Backtracking algorithm (`NQueens(row, n)` and `IsSafe(r, c)`). Trace the State Space Tree for placing 4 queens on a $4 \times 4$ board. `[6 Marks]`  
    **(b)** Explain the **0/1 Knapsack Problem** using Backtracking. Define the Upper Bound function (fractional relaxation) used to prune unpromising subtrees. `[4 Marks]`

18. **(a)** Explain the **Least-Cost Branch and Bound (LCBB)** strategy for solving the **Travelling Salesman Problem (TSP)**. Given the 4-city distance matrix $C$:
    $$C = \begin{bmatrix} \infty & 10 & 15 & 20 \\ 5 & \infty & 9 & 10 \\ 6 & 13 & \infty & 12 \\ 8 & 8 & 9 & \infty \end{bmatrix}$$
    1. Perform Row and Column reduction to find the root node's Lower Bound $L_0$.
    2. Branch to Level 1 nodes (paths $1 \to 2$, $1 \to 3$, $1 \to 4$) and compute their reduced lower bounds. `[7 Marks]`  
    **(b)** Define a **State Space Tree**. Explain how bounding functions and an `UpperBound` tracker prune live nodes during LC-Search. `[3 Marks]`

19. **(a)** Differentiate between **Deterministic** and **Non-Deterministic** algorithms. Write the complete pseudocode for the **Non-Deterministic Sorting Algorithm (`NDSort`)** and analyze its non-deterministic time complexity. `[5 Marks]`  
    **(b)** Define the computational complexity classes **P**, **NP**, **NP-Hard**, and **NP-Complete**. Draw a Venn diagram illustrating their relationships under the assumption $P \ne NP$. `[5 Marks]`

20. **(a)** Define **Polynomial-Time Reduction** ($A \le_P B$). Explain why proving a problem $B$ is NP-Complete requires reducing a known NP-Complete problem $A$ to $B$, rather than $B$ to $A$. Summarize the significance of the **Cook-Levin Theorem** (3-SAT). `[5 Marks]`  
    **(b)** Write down the general **Control Abstraction** for the **Greedy Method** (`Algorithm Greedy(A, n)`) and compare it with the general Control Abstraction for **Backtracking** (`Algorithm Backtrack(k)`). `[5 Marks]`
