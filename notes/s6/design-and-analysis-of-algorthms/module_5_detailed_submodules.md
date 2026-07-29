# Module V: Dynamic Programming vs. Divide & Conquer, and the Greedy Strategy

This module transitions from the fundamental design paradigms you learned earlier into optimization problems, focusing heavily on how to make the most mathematically efficient choices.

### 1. Analysis & Comparison: Divide and Conquer vs. Dynamic Programming
Both Divide and Conquer (D&C) and Dynamic Programming (DP) are algorithm design paradigms that solve a complex problem by breaking it down into smaller subproblems. However, their core mechanics and use cases are vastly different.

- **Divide and Conquer:** This strategy divides a problem into completely independent, disjoint subproblems. It solves each subproblem recursively, then combines the solutions to solve the original problem. Because it does not check if a subproblem has been solved before, it can do a massive amount of redundant work if the subproblems overlap.
- **Dynamic Programming:** This strategy is designed specifically for problems with overlapping subproblems and optimal substructure. Instead of recomputing the same subproblem repeatedly, DP solves each subproblem once and stores the answer in a memory table.
  - **Memoization:** A top-down optimization technique where the results of expensive function calls are saved in a cache. If the exact same subproblem occurs again, the algorithm simply retrieves the cached answer instead of recalculating it.
  - **Tabulation:** A bottom-up approach that systematically fills a table with solutions to all necessary subproblems.

#### Applications & Use Cases:
- **Divide & Conquer:** Best for parallel processing, sorting algorithms (Merge Sort, Quick Sort), and searching (Binary Search).
- **Dynamic Programming:** Best for optimization problems where you need the "best" or "shortest" answer (Bellman-Ford Algorithm, 0/1 Knapsack, Sequence Alignment in bioinformatics).

#### Comparison Table:
| Feature | Divide and Conquer | Dynamic Programming |
| :--- | :--- | :--- |
| **Nature of Subproblems** | Independent / Non-overlapping | Interdependent / Overlapping |
| **Execution Approach** | Top-Down (Recursive) | Usually Bottom-Up (Iterative Tabulation) |
| **Memory Optimization** | Does not store subproblem results | Stores results to avoid recalculation |
| **Time Efficiency** | Slower if subproblems overlap (e.g., $O(2^n)$ for Fibonacci) | Highly efficient for overlapping cases (e.g., $O(n)$ for Fibonacci) |

### 2. The Greedy Strategy: The Control Abstraction
**refferal video:**https://youtu.be/ARvQcqJ_-NY?si=2skdhlcU8xTZTSkp
The Greedy Strategy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most immediate, obvious benefit.

- **The Principle:** It makes a locally optimal choice at each stage with the hope that these local optimums will lead to a globally optimal solution.
- **The Catch:** A greedy algorithm never reconsiders its choices. Once a decision is made, it is final. Therefore, Greedy only works on problems where local optimality guarantees global optimality (known as the greedy-choice property).

#### The Control Abstraction (Conceptual Framework):
A control abstraction is a standard pseudocode template that outlines how all greedy algorithms operate fundamentally.

```plaintext
Algorithm Greedy(a, n)
// a is an array of n inputs
{
    solution = ∅;  // Initialize empty solution set
    for i = 1 to n do
    {
        x = select(a);  // Greedily pick the best item
        if feasible(solution, x) then
        {
            solution = union(solution, x); // Add to solution
        }
    }
    return solution;
}
```
Algorithm Greedy(a, n)
This line defines the start of the algorithm. It takes two parameters: a, which is the set of raw inputs (like tasks to schedule or items to put in a bag), and n, which is the total count of those inputs.

solution = ∅;
Greedy algorithms build a solution piece by piece. This line creates an empty container (represented by the mathematical empty set symbol ∅) where we will store our winning selections.

for i = 1 to n do
This establishes a loop that runs n times. Because a greedy algorithm generally evaluates the available options step-by-step without looking back, it needs a loop to iterate through the choices.

x = select(a);
This is the heart of the greedy strategy. The select function examines the remaining options in a and greedily picks the one that looks like the absolute best choice at this exact moment, ignoring future consequences. For example, if you are making change for a dollar, select would grab the largest coin possible first (a quarter).

if feasible(solution, x) then
Even if an item looks like a great choice, it might not be allowed. This line checks if adding the newly selected item x violates the problem's constraints. For example, if you are packing a backpack with a 50 lb limit, feasible checks if adding item x pushes the total weight over 50 lbs.

solution = union(solution, x);
If the item x passes the feasibility test, it is permanently added to the solution set. The word union means we are merging the new item x into our existing collection. In a greedy algorithm, once a choice is made and added to the solution, it is never reconsidered or removed.

return solution;
Once the loop finishes (meaning we have evaluated our choices n times), the algorithm terminates and hands back the final, built-up solution to the user.

### 3. The Fractional Knapsack Problem
#### Explanation:
You are given $n$ items, each with a specific weight ($w_i$) and a value ($v_i$). You have a knapsack that can carry a maximum weight capacity of $W$. Your goal is to maximize the total value in the knapsack. Unlike the 0/1 Knapsack (which requires DP), the Fractional Knapsack allows you to break items into fractions.

- **The Greedy Choice:** Calculate the value-to-weight ratio ($\frac{v_i}{w_i}$) for every item. Sort the items in descending order based on this ratio. Take as much of the item with the highest ratio as possible, then move to the next.

#### Applications:
Resource allocation in cloud computing (allocating fractions of CPU/RAM for maximum profit) and continuous material cutting.

#### Solved Example 1: Fractional Knapsack
**Problem:** Given a knapsack capacity $W = 50$, and 3 items:
- Item 1: $v_1 = 60$, $w_1 = 10$
- Item 2: $v_2 = 100$, $w_2 = 20$
- Item 3: $v_3 = 120$, $w_3 = 30$

**Step-by-Step Solution:**
1. **Calculate Ratios ($\frac{v}{w}$):**
   - Item 1: $\frac{60}{10} = 6$
   - Item 2: $\frac{100}{20} = 5$
   - Item 3: $\frac{120}{30} = 4$
2. **Sort Items by Ratio (Descending):**
   - Order: Item 1, Item 2, Item 3.
3. **Fill the Knapsack:**
   - **Select Item 1:** $w = 10$. Knapsack has $50 - 10 = 40$ remaining. Current Value = $60$.
   - **Select Item 2:** $w = 20$. Knapsack has $40 - 20 = 20$ remaining. Current Value = $60 + 100 = 160$.
   - **Select Item 3:** We need $20$ weight, but Item 3 is $30$. We take a fraction: $\frac{20}{30} = \frac{2}{3}$ of Item 3.
   - **Fractional Value:** $\frac{2}{3} \cdot 120 = 80$.
4. **Final Result:** Total Value = $160 + 80 = 240$.

### 4. Minimal Cost Spanning Tree: Prim’s Algorithm
**refferal video:**https://youtu.be/EjVHtpWkIho?si=5qfmIAtFY8AXD5Jm

Example
**refferal video :**https://youtu.be/71SJL5lOOzY?si=AZeJaXX9KR32JPN4
#### Explanation:
A Spanning Tree of a connected, undirected graph is a subgraph that includes all vertices but contains no cycles. A Minimal Cost Spanning Tree (MCST) is the spanning tree with the lowest possible total edge weight.

Prim's Algorithm is a greedy approach that starts at an arbitrary node and maintains a single, growing tree. At each step, it safely adds the cheapest edge that connects a vertex inside the tree to a vertex outside the tree.

#### Applications:
Laying out electrical wiring, network routing, and designing printed circuit boards.

#### Solved Example 2: Prim's Algorithm
**Problem:** Find the MCST for a graph with vertices $V = \{A, B, C, D\}$ and weighted edges: $(A,B, 1)$, $(A,C, 4)$, $(B,C, 2)$, $(B,D, 5)$, $(C,D, 3)$.

**Step-by-Step Solution:**
- **Initialization:** Start at arbitrary vertex $A$. Visited set $S = \{A\}$.
- **Iteration 1:** Look at edges leaving $S$: $(A,B, 1)$ and $(A,C, 4)$.
  - **Greedy Choice:** Pick the cheapest edge $(A,B, 1)$.
  - Add $B$ to $S$. $S = \{A, B\}$. Total Cost = $1$.
- **Iteration 2:** Look at edges leaving $S$: $(A,C, 4)$, $(B,C, 2)$, $(B,D, 5)$.
  - **Greedy Choice:** Pick the cheapest edge $(B,C, 2)$.
  - Add $C$ to $S$. $S = \{A, B, C\}$. Total Cost = $1 + 2 = 3$.
- **Iteration 3:** Look at edges leaving $S$: $(A,C, 4)$ (invalid, both in $S$), $(B,D, 5)$, $(C,D, 3)$.
  - **Greedy Choice:** Pick the cheapest edge $(C,D, 3)$.
  - Add $D$ to $S$. $S = \{A, B, C, D\}$. All vertices visited.
- **Final Result:** The MCST edges are $(A,B)$, $(B,C)$, $(C,D)$ with a total minimum cost of $6$.

### 5. Minimal Cost Spanning Tree: Kruskal’s Algorithm
**refferal video:**https://youtu.be/ZtZaR7EcI5Y?si=ee5EngQSkAIU89MW
#### Explanation:
Kruskal's Algorithm is another greedy approach for finding an MCST. Instead of growing a single tree from a starting node, Kruskal's algorithm treats every vertex as its own tree (a forest). It sorts all edges in the entire graph by weight and continuously adds the cheapest edge to the forest, provided that the edge does not form a cycle. Cycle detection is typically handled using a Union-Find Disjoint Set data structure.

#### Applications:
Clustering algorithms in data science, constructing water supply networks across municipalities.

#### Solved Example 3: Kruskal's Algorithm
**Problem:** Find the MCST for a graph with 4 vertices $\{1, 2, 3, 4\}$ and edges: $(1,2, 10)$, $(1,3, 6)$, $(1,4, 5)$, $(2,3, 15)$, $(3,4, 4)$.

**Step-by-Step Solution:**
1. **Sort all edges in non-decreasing order:**
   - $e_1 = (3,4) \rightarrow$ weight $4$
   - $e_2 = (1,4) \rightarrow$ weight $5$
   - $e_3 = (1,3) \rightarrow$ weight $6$
   - $e_4 = (1,2) \rightarrow$ weight $10$
   - $e_5 = (2,3) \rightarrow$ weight $15$
2. **Iterate and select edges:**
   - Check $e_1 (3,4, 4)$: Does not form a cycle. Add to MCST. (Cost = $4$)
   - Check $e_2 (1,4, 5)$: Does not form a cycle. Add to MCST. (Cost = $4 + 5 = 9$)
   - Check $e_3 (1,3, 6)$: If added, it creates a closed loop $(1-3-4-1)$. Reject edge.
   - Check $e_4 (1,2, 10)$: Does not form a cycle. Add to MCST. (Cost = $9 + 10 = 19$)
3. **Termination:** The spanning tree has $V-1$ edges ($4-1 = 3$ edges). The algorithm halts.
4. **Final Result:** The MCST edges are $(3,4)$, $(1,4)$, $(1,2)$ with a total minimum cost of $19$.
