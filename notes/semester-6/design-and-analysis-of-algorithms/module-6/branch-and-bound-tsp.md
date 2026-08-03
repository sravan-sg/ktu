# Module 6 — Topic 1: Branch and Bound & Travelling Salesman Problem

> **Module 6**: Branch and Bound & Complexity Theory  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
**Branch and Bound (B&B)** is a highly optimized algorithm design paradigm used strictly for solving hard combinatorial **Optimization Problems** (where you want to find the absolute minimum cost or maximum profit).
While Backtracking uses Depth-First Search (DFS) to blindly dive down paths, B&B explores the state-space tree using **Breadth-First Search (BFS)** or **Least-Cost (Best-First) Search (LC-Search)**. 
- **Branching**: It generates all possible next steps (children nodes) from the current state.
- **Bounding**: For every child, it calculates an optimistic *bound* (a theoretical absolute best-case scenario if you go down this path). 
If a node's optimistic bound is mathematically *worse* than a complete solution you already found earlier (your `UpperBound`), you immediately kill (prune) that node. You don't even bother generating its children because it is mathematically impossible for it to yield a better answer.

### Example
Imagine you are at an auction trying to buy a rare painting for the minimum possible price. Your absolute upper limit (your `UpperBound`) is $500.
There are three different bidding rooms (Branches). You peek into Room A and the current bid is already $600. Even if no one else bids, the absolute minimum (the `Bound`) you could pay is $601. Because $601 > 500, you don't even enter the room (Pruning). You successfully ignored a path because its most optimistic scenario was still worse than your limit.

### Applications & Use Cases
- **Logistics & Delivery (TSP)**: FedEx, Amazon, and UPS use B&B (specifically cutting-plane variants) to solve the Travelling Salesman Problem, finding the absolute minimum mileage route for a delivery truck hitting 50 different houses and returning to the depot.
- **Circuit Board Routing**: Finding the shortest possible length of copper wire to connect components on a PCB without lines crossing uses B&B to minimize signal delay and interference.
- **Job Shop Scheduling**: Manufacturing plants use B&B to assign hundreds of production jobs to specific machines in an order that minimizes the total completion time (makespan).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Bounding Logic in LC-Search
**Problem:** You are using Least-Cost Branch and Bound (LCBB) to minimize a cost function. You have found a valid complete solution with a cost of 45 (`UpperBound` = 45). Your Priority Queue currently holds three live nodes: Node $X$ (Bound = 30), Node $Y$ (Bound = 48), Node $Z$ (Bound = 40). Trace the immediate next actions of the LCBB algorithm.
**Step-by-step Solution:**
1. **Current State:** `UpperBound` = 45. Queue = $\{X(30), Y(48), Z(40)\}$.
2. **Apply Bounding:** 
   - Node $Y$ has an optimistic minimum bound of 48. This means any full solution passing through $Y$ will cost *at least* 48.
   - Since $48 > 45$, Node $Y$ is mathematically useless.
   - **Action:** Prune (kill) Node $Y$. Queue is now $\{X(30), Z(40)\}$.
3. **Apply LC-Search (Best-First):**
   - LC-Search dictates we always expand the node with the lowest bound next.
   - $X$ has Bound 30. $Z$ has Bound 40.
   - **Action:** Dequeue Node $X$ and branch it to generate its children.

### Example 2: 15-Puzzle Bounding Function
**Problem:** The 15-Puzzle is a $4 \times 4$ sliding tile game. Define a mathematical bounding function $c(x)$ that can be used in Branch and Bound to estimate the minimum number of moves required to solve the puzzle from state $x$.
**Step-by-step Solution:**
1. **Define the Cost:** Let $g(x)$ be the number of actual moves taken from the start state to reach state $x$.
2. **Define the Heuristic (Optimistic Estimate):** Let $h(x)$ be the *Manhattan Distance* of all tiles. For each tile, calculate $|CurrentRow - TargetRow| + |CurrentCol - TargetCol|$. Sum this up for all 15 tiles. 
   - *(Note: We use Manhattan distance because a tile can only move up, down, left, or right. The Manhattan distance is an optimistic lower bound because it assumes tiles can magically pass through each other to reach their target).*
3. **Formulate Bounding Function:** $c(x) = g(x) + h(x)$.
4. **Execution Logic:** When branching, LCBB will calculate $c(x)$ for sliding a tile Up, Down, Left, or Right. It will always prioritize exploring the board state with the lowest $c(x)$ (the state that appears closest to the solved configuration).

### Example 3: TSP Cost Matrix Reduction (Finding the Root Lower Bound)
**Problem:** You are solving the Travelling Salesman Problem for 4 cities using B&B. The original cost matrix $C$ is below. Find the absolute minimum Lower Bound cost of the root node by reducing the matrix (ensuring every row and column has at least one 0).
$$C = \begin{bmatrix} \infty & 20 & 30 & 10 \\ 15 & \infty & 16 & 4 \\ 3 & 5 & \infty & 2 \\ 19 & 6 & 18 & \infty \end{bmatrix}$$
**Step-by-step Solution:**
1. **Row Reduction:** Subtract the minimum element of each row from every element in that row.
   - Row 1 Min = 10. $\rightarrow [\infty, 10, 20, 0]$
   - Row 2 Min = 4. $\rightarrow [11, \infty, 12, 0]$
   - Row 3 Min = 2. $\rightarrow [1, 3, \infty, 0]$
   - Row 4 Min = 6. $\rightarrow [13, 0, 12, \infty]$
   - Total Row Reduction Cost $= 10 + 4 + 2 + 6 = 22$.
2. **Column Reduction:** Subtract the minimum element of each column (using the new matrix) from every element in that column.
   - Col 1 Min = 1. $\rightarrow [\infty, 11, 1, 13] \rightarrow [\infty, 10, 0, 12]$
   - Col 2 Min = 0. $\rightarrow [10, \infty, 3, 0]$ (No change)
   - Col 3 Min = 12. $\rightarrow [20, 12, \infty, 12] \rightarrow [8, 0, \infty, 0]$
   - Col 4 Min = 0. $\rightarrow [0, 0, 0, \infty]$ (No change)
   - Total Column Reduction Cost $= 1 + 0 + 12 + 0 = 13$.
3. **Final Result:** The Lower Bound for the root node is the sum of all reduction costs: $22 + 13 =$ **$35$**. Any valid TSP tour in this graph will cost absolutely no less than 35.
