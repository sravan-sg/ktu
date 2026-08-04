# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SIXTH SEMESTER B.TECH DEGREE EXAMINATION
### Course Code: CS302 | Course Name: DESIGN AND ANALYSIS OF ALGORITHMS
**Max. Marks: 100** | **Duration: 3 Hours**

---

### PART A
*Answer ALL questions. Each question carries 3 marks (Total: 12 Marks). Covers Modules I & II.*

1. **[Module 1]** Define the asymptotic notations $O$, $\Omega$, and $\Theta$ using rigorous mathematical inequalities and sketch their graphical representations. `[3 Marks]`
2. **[Module 1]** Perform frequency count analysis to derive the exact operation count $T(n)$ for standard $n \times n$ matrix multiplication using 3 nested loops. `[3 Marks]`
3. **[Module 2]** Apply Master's Theorem to determine the asymptotic time complexity of $T(n) = 4T(n/2) + n^3$. `[3 Marks]`
4. **[Module 2]** List the 5 fundamental properties that define a **Red-Black Tree**. `[3 Marks]`

---

### PART B
*Answer ANY TWO full questions. Each question carries 9 marks (Total: 18 Marks). Covers Modules I & II.*

5. **(a)** Solve the recurrence relation $T(n) = 2T(n/2) + n \log n$ using the **Recursion Tree Method** or extended Master's Theorem. `[5 Marks]`  
   **(b)** Compare the Best-case, Worst-case, and Average-case time complexities of **Linear Search** versus **Binary Search**. `[4 Marks]`

6. Construct an **AVL Tree** by inserting the sequence of keys: `14, 15, 4, 3, 9, 7, 18, 16` into an initially empty tree. Draw the intermediate trees after every insertion and label every single rotation (LL, RR, LR, RL) performed. `[9 Marks]`

7. **(a)** Construct a **Red-Black Tree** by inserting keys `10, 20, 30, 40, 50, 25` into an initially empty tree. Detail all structural rotations and color changes. `[6 Marks]`  
   **(b)** Describe the node split and node merge algorithms in B-Trees. Explain how they maintain perfect leaf height balance. `[3 Marks]`

---

### PART C
*Answer ALL questions. Each question carries 3 marks (Total: 12 Marks). Covers Modules III & IV.*

8. **[Module 3]** Explain **Breadth-First Search (BFS)** level-order traversal on a graph. How is BFS used to find the unweighted shortest path? `[3 Marks]`
9. **[Module 3]** Define a **Transpose Graph** $G^T$. How is $G^T$ utilized in Kosaraju's algorithm for finding Strongly Connected Components? `[3 Marks]`
10. **[Module 4]** Explain why **Dynamic Programming** is applicable to problems with overlapping subproblems, whereas Divide and Conquer is applicable to independent subproblems. `[3 Marks]`
11. **[Module 4]** State the 7 scalar multiplication equations ($P_1$ to $P_7$) used in **Strassen's Matrix Multiplication** algorithm. `[3 Marks]`

---

### PART D
*Answer ANY TWO full questions. Each question carries 9 marks (Total: 18 Marks). Covers Modules III & IV.*

12. **(a)** Trace the **Bellman-Ford Algorithm** on a directed graph with 5 vertices $\{A, B, C, D, E\}$ and weighted edges: $(A \to B, -1), (A \to C, 4), (B \to C, 3), (B \to D, 2), (B \to E, 2), (D \to B, 1), (D \to C, 5), (E \to D, -3)$. Show distance updates for 4 relaxation passes. `[6 Marks]`  
    **(b)** Explain how DFS detects cycles in directed graphs using **Back Edges**. `[3 Marks]`

13. **(a)** Use **Dynamic Programming** to find the optimal matrix chain parenthesization for 4 matrices with dimensions $p = [5, 10, 3, 12, 5, 50]$. Construct the complete $m[i,j]$ cost table and $s[i,j]$ split table. `[6 Marks]`  
    **(b)** Trace the 2-way **Merge Sort** algorithm on the input array `[38, 27, 43, 3, 9, 82, 10]`. Show the divide and merge steps explicitly. `[3 Marks]`

14. **(a)** Trace **Dijkstra's Algorithm** on a directed graph with vertices $\{1, 2, 3, 4, 5, 6\}$, source vertex $1$, and weighted edges $(1 \to 2, 9), (1 \to 3, 4), (2 \to 4, 2), (3 \to 2, 3), (3 \to 5, 6), (4 \to 5, 3), (4 \to 6, 2), (5 \to 6, 1)$. `[6 Marks]`  
    **(b)** Prove that the **Shortest Path Problem** satisfies the **Principle of Optimality**. `[3 Marks]`

---

### PART E
*Answer ANY FOUR full questions. Each question carries 10 marks (Total: 40 Marks). Covers Modules V & VI.*

15. **(a)** Formulate the **Fractional Knapsack Problem**. Solve it using the Greedy method for $W = 50$, items with profits $P = [60, 100, 120]$ and weights $W_{arr} = [10, 20, 30]$. `[6 Marks]`  
    **(b)** Trace **Prim's Algorithm** to find the Minimum Spanning Tree (MST) on a 6-vertex graph starting from vertex $A$. `[4 Marks]`

16. **(a)** Trace **Kruskal's Algorithm** on a 6-vertex graph. Show edge sorting, Disjoint Set Union-Find operations, and cycle prevention. `[5 Marks]`  
    **(b)** State and formally prove the **Cut Property** of Minimum Spanning Trees using proof by contradiction. `[5 Marks]`

17. **(a)** Write the recursive **Backtracking algorithm** for the **N-Queens Problem**. Draw the State Space Tree for 4 Queens on a $4 \times 4$ chessboard. `[6 Marks]`  
    **(b)** Explain the **0/1 Knapsack Problem** using Backtracking. Define the bounding function used to prune unpromising subtrees. `[4 Marks]`

18. **(a)** Trace the **Least-Cost Branch and Bound (LCBB)** algorithm for the **Travelling Salesman Problem (TSP)** on a 4-city cost matrix. Perform Row/Column reductions to derive lower bounds for root and Level 1 nodes. `[7 Marks]`  
    **(b)** Compare **Branch and Bound** versus **Backtracking** in terms of state space exploration strategy (FIFO, LIFO, LC-Search). `[3 Marks]`

19. **(a)** Write the complete pseudocode for the **Non-Deterministic Sorting Algorithm (`NDSort`)** and analyze its time complexity. `[5 Marks]`  
    **(b)** Define the computational complexity classes **P**, **NP**, **NP-Hard**, and **NP-Complete**. Explain the significance of the $P$ versus $NP$ problem. `[5 Marks]`

20. **(a)** Explain the concept of **Polynomial-Time Reduction** ($A \le_P B$). Summarize the **Cook-Levin Theorem** (3-SAT) and how NP-Completeness is established. `[5 Marks]`  
    **(b)** Compare the general **Control Abstraction for Greedy Method** with the general **Control Abstraction for Dynamic Programming**. `[5 Marks]`
