# Module 5 — Topic 1: Greedy Strategy (Knapsack & MST)

> **Module 5**: Greedy Strategy & Backtracking  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Greedy Strategy** is an algorithmic paradigm that builds up a solution piece by piece. At every single step, it makes the choice that looks most profitable or optimal *at that exact moment*. 
Unlike Dynamic Programming (which exhaustively evaluates all future consequences before deciding) or Backtracking (which reverses bad decisions), a Greedy algorithm has **no memory and no foresight**. Once it makes a choice, it locks it in forever.
Because it doesn't evaluate every combination, it is incredibly fast (often $O(n \log n)$). However, it only yields the correct global solution if the problem exhibits the **Greedy-Choice Property**: the mathematical guarantee that a local optimum directly leads to a global optimum.

### Example
Imagine you are a thief breaking into a jewelry store with a small backpack (a Knapsack). You see gold dust, silver dust, and copper dust. You can take fractions of the dust.
A Greedy approach says: calculate the value-per-ounce of each metal. Gold is the highest. Shovel as much gold into your bag as it can possibly hold. If the bag isn't full, move to the next highest value (silver), and so on. Because the items are divisible, this locally greedy choice guarantees you walk out with the absolute maximum possible wealth.

### Applications & Use Cases
- **Data Compression (Huffman Coding)**: ZIP files and JPEGs use a greedy algorithm to assign the shortest binary codes to the most frequently occurring characters, guaranteeing the smallest possible compressed file size.
- **Network Routing & Wiring (MST)**: Telecommunication companies use Prim's or Kruskal's greedy algorithms to lay down fiber-optic cables connecting entire neighborhoods using the absolute minimum total length of wire.
- **Operating System Scheduling**: An OS CPU scheduler uses greedy algorithms to pick the shortest available job in the queue to minimize the average waiting time for all processes.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Fractional Knapsack Problem [April 2018, Dec 2019]
**Problem:** A knapsack has a maximum capacity $W = 50$. There are 3 items available: 
- Item 1: Profit $P_1 = 60$, Weight $W_1 = 10$
- Item 2: Profit $P_2 = 100$, Weight $W_2 = 20$
- Item 3: Profit $P_3 = 120$, Weight $W_3 = 30$
Find the maximum profit using the Greedy Strategy.
**Step-by-step Solution:**
1. **Calculate Profit-to-Weight Ratio ($P/W$):**
   - Item 1: $60 / 10 = 6$
   - Item 2: $100 / 20 = 5$
   - Item 3: $120 / 30 = 4$
2. **Sort by Ratio (Descending):**
   - Order of selection: Item 1, then Item 2, then Item 3.
3. **Greedy Selection:**
   - **Take Item 1:** Bag capacity drops to $50 - 10 = 40$. Current Profit $= 60$.
   - **Take Item 2:** Bag capacity drops to $40 - 20 = 20$. Current Profit $= 60 + 100 = 160$.
   - **Take Item 3 (Fractional):** The bag only has 20 capacity left, but Item 3 weighs 30. We take a fraction: $20/30 = 2/3$ of Item 3.
   - Profit from fraction: $(2/3) \times 120 = 80$.
4. **Final Result:** Total Maximum Profit $= 160 + 80 =$ **$240$**.

### Example 2: Kruskal's Algorithm (Minimum Spanning Tree) [Dec 2019]
**Problem:** Given a graph with nodes $A, B, C, D$ and edges: $(A,B,1), (B,C,4), (C,D,2), (A,D,3), (B,D,5)$. Trace Kruskal's algorithm to find the Minimum Spanning Tree (MST).
**Step-by-step Solution:**
1. **Sort all edges by weight:**
   - $(A,B): 1$
   - $(C,D): 2$
   - $(A,D): 3$
   - $(B,C): 4$
   - $(B,D): 5$
2. **Greedy Selection with Cycle Detection (Union-Find):**
   - **Pick $(A,B,1)$:** No cycle. Add to MST. (Connected components: $\{A,B\}, \{C\}, \{D\}$).
   - **Pick $(C,D,2)$:** No cycle. Add to MST. (Connected components: $\{A,B\}, \{C,D\}$).
   - **Pick $(A,D,3)$:** No cycle. Add to MST. Merges the two components. (Connected components: $\{A,B,C,D\}$).
3. **Termination:** We have connected all 4 vertices using $V-1 = 3$ edges. The algorithm stops.
4. **Final Result:** The MST consists of edges $(A,B), (C,D), (A,D)$ with a total minimum cost of $1 + 2 + 3 =$ **$6$**.

### Example 3: Prim's Algorithm (Minimum Spanning Tree) [April 2018]
**Problem:** Using the exact same graph as Example 2, trace Prim's algorithm starting from node $A$.
**Step-by-step Solution:**
1. **Initialization:** Start at Node $A$.
   - `Visited` = $\{A\}$. `Unvisited` = $\{B, C, D\}$.
   - Available edges from visited set: $(A,B,1)$ and $(A,D,3)$.
2. **Step 1:** Greedily pick the minimum available edge $\rightarrow (A,B,1)$.
   - Move $B$ to `Visited`.
   - `Visited` = $\{A, B\}$.
   - Available edges from $\{A, B\}$: $(A,D,3), (B,C,4), (B,D,5)$.
3. **Step 2:** Greedily pick the minimum available edge $\rightarrow (A,D,3)$.
   - Move $D$ to `Visited`.
   - `Visited` = $\{A, B, D\}$.
   - Available edges from $\{A, B, D\}$: $(B,C,4), (B,D,5), (C,D,2)$. *(Note: $B,D$ is an internal cycle edge now, effectively ignored)*.
4. **Step 3:** Greedily pick the minimum available edge to an unvisited node $\rightarrow (C,D,2)$.
   - Move $C$ to `Visited`.
   - `Visited` = $\{A, B, C, D\}$.
5. **Termination:** All nodes are visited.
6. **Final Result:** The MST consists of edges $(A,B), (A,D), (C,D)$ with a total minimum cost of $1 + 3 + 2 =$ **$6$**. Both greedy algorithms yielded the exact same optimal tree.

---

### Previous Year Questions & Solutions

1. **"Write down Prim's algorithm and analyse the complexity." [April 2018, July 2021]**
   - **Solution:**
     ```text
     Prim(G, w, r):
         for each u in V:
             key[u] = infinity, parent[u] = NIL
         key[r] = 0
         Q = BuildMinPriorityQueue(V)
         while Q is not empty:
             u = ExtractMin(Q)
             for each neighbor v of u:
                 if v in Q and w(u, v) < key[v]:
                     parent[v] = u
                     key[v] = w(u, v)
                     DecreaseKey(Q, v, key[v])
     ```
     **Complexity Analysis:**
     - ExtractMin takes $O(\log V)$ and runs $V$ times $\implies O(V \log V)$.
     - DecreaseKey takes $O(\log V)$ and runs at most $E$ times $\implies O(E \log V)$.
     - Total Time Complexity: **$O(E \log V)$** (with Binary Heap) or **$O(E + V \log V)$** (with Fibonacci Heap).

2. **"Formulate Fractional Knapsack Problem. Write greedy algorithm for Fractional Knapsack." [April 2018, Dec 2019, July 2021]**
   - **Solution:**
     - **Formulation:** Given $n$ items with profits $p_i > 0$, weights $w_i > 0$, and knapsack capacity $W$, find fractions $x_i \in [0, 1]$ to maximize $\sum_{i=1}^n x_i p_i$ subject to $\sum_{i=1}^n x_i w_i \le W$.
     ```text
     FractionalKnapsack(P, W_arr, W, n):
         for i = 1 to n: ratio[i] = P[i] / W_arr[i]
         Sort items by ratio in descending order
         total_profit = 0
         for i = 1 to n:
             if W_arr[i] <= W:
                 W = W - W_arr[i]
                 total_profit += P[i]
             else:
                 total_profit += P[i] * (W / W_arr[i])
                 break
         return total_profit
     ```
     - **Complexity:** Sorting takes $O(n \log n)$, greedy loop takes $O(n)$. Total time: **$O(n \log n)$**.

3. **"Let (u,v) be a minimum-weight edge in a graph G. Show that (u,v) belongs to some minimum spanning tree of G." [April 2018]**
   - **Solution:**
     **Proof by Contradiction (Cut Property):**
     1. Assume edge $e = (u,v)$ is the unique minimum weight edge in graph $G$, but does NOT belong to MST $T$.
     2. Adding edge $e$ to $T$ creates a unique cycle $C$ containing $e$.
     3. Since $T$ is a tree connecting all vertices, there must exist at least one other edge $e' = (x,y)$ on cycle $C$ that crosses between the components connected by $e$.
     4. Since $e$ has strict minimum weight, $w(e) < w(e')$.
     5. Replace $e'$ with $e$ to form new spanning tree $T' = T \cup \{e\} \setminus \{e'\}$.
     6. Weight of $T' = w(T) - w(e') + w(e) < w(T)$, contradicting that $T$ was a minimum spanning tree.
     7. Thus, $e$ must belong to the MST.

4. **"Define spanning tree of a graph." [Dec 2019, July 2021]**
   - **Solution:** A spanning tree $T$ of an undirected connected graph $G = (V,E)$ is a minimal connected subgraph that contains all $|V|$ vertices of $G$ and exactly $|V| - 1$ edges with no cycles.
