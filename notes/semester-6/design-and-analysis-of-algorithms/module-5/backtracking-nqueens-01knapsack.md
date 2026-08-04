# Module 5 — Topic 2: Backtracking (N-Queens & 0/1 Knapsack)

> **Module 5**: Greedy Strategy & Backtracking  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
**Backtracking** is a systematic algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time. It uses a **Depth-First Search (DFS)** to traverse a "State Space Tree" of all possible decisions.
The core power of backtracking lies in **Pruning**. At each step, a constraint function checks if the current partial solution is still legally valid. If it violates a rule (or if it is mathematically impossible for it to yield a better result than what we already have), the algorithm immediately stops exploring that entire branch. It "backtracks" (steps back) to the parent node and tries the next available option. This avoids the catastrophic $O(N!)$ or $O(2^N)$ time limits of naive Brute Force.

### Example
Imagine navigating a physical corn maze looking for an exit. You pick a path and walk down it. Eventually, you hit a dead end (a constraint violation). Instead of magically teleporting back to the very start of the maze and starting over from scratch, you simply walk backward (backtrack) to the last intersection and try a different path. You prune the dead-end branch from your mental map.

### Applications & Use Cases
- **Constraint Satisfaction Puzzles**: Sudoku solvers, Crosswords, and cryptarithmetic puzzles inherently rely on backtracking to rapidly test and prune invalid number/letter placements.
- **Pathfinding in Robotics**: If a robot is trying to navigate a factory floor filled with moving obstacles, it uses backtracking to dynamically re-evaluate paths when its current trajectory is suddenly blocked.
- **Compiler Syntax Parsing**: When a compiler tries to match your code to a grammar rule, it uses backtracking (like recursive descent parsers) to try a rule, and if it fails, backs up and tries the next possible grammar rule.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: N-Queens Constraint Logic [April 2018, Dec 2019]
**Problem:** State the N-queens problem. Prove the specific mathematical constraints used to prune branches in the N-Queens problem on an $N \times N$ board. If a queen is placed at row $i$ and column $j$, how do we mathematically verify that a new queen at row $r$ and column $c$ is safe?
**Step-by-step Solution:**
1. **Row Constraint:** A queen can attack anything in its row.
   - Constraint: $r \neq i$.
   - *(Note: Most algorithms just place one queen per row automatically, inherently satisfying this).*
2. **Column Constraint:** A queen can attack anything in its column.
   - Constraint: $c \neq j$.
3. **Diagonal Constraints:** A queen attacks diagonally. On a 2D grid, two points $(i, j)$ and $(r, c)$ are on the same diagonal if the absolute difference between their rows equals the absolute difference between their columns.
   - Constraint: $|r - i| \neq |c - j|$.
4. **Conclusion:** Before placing a queen at $(r, c)$, the algorithm loops through all previously placed queens. If *any* previous queen at $(i, j)$ violates either $c = j$ or $|r - i| = |c - j|$, the algorithm prunes the branch and immediately tries column $c+1$.

### Example 2: 4-Queens State Space Tree Trace [April 2018]
**Problem:** Explain the solution by tracing the initial backtracking steps to place 4 queens on a $4 \times 4$ board.
**Step-by-step Solution:**
1. **Row 1:** Place $Q_1$ at $(1, 1)$. (Valid).
2. **Row 2:** 
   - Try $(2, 1)$: Fails column check ($1 = 1$).
   - Try $(2, 2)$: Fails diagonal check ($|2-1| = |2-1| \rightarrow 1 = 1$).
   - Try $(2, 3)$: Valid. Place $Q_2$ at $(2, 3)$.
3. **Row 3:**
   - Try $(3, 1)$: Fails column check ($1 = 1$ from $Q_1$).
   - Try $(3, 2)$: Fails diagonal check from $Q_2$ ($|3-2| = |2-3| \rightarrow 1 = 1$).
   - Try $(3, 3)$: Fails column check ($3 = 3$ from $Q_2$).
   - Try $(3, 4)$: Fails diagonal check from $Q_2$ ($|3-2| = |4-3| \rightarrow 1 = 1$).
4. **Dead End & Backtrack:** Row 3 has no valid spots. The algorithm immediately aborts, backtracks to Row 2.
5. **Resume Row 2:** Remove $Q_2$ from $(2, 3)$.
   - Try $(2, 4)$: Valid. Place $Q_2$ at $(2, 4)$.
6. **Resume Row 3:** ... (Algorithm continues successfully from here).

### Example 3: 0/1 Knapsack Backtracking Bounding Function
**Problem:** We have a Knapsack of capacity $W=10$. We have 3 items: $I_1(\text{weight}=4, \text{profit}=40)$, $I_2(\text{weight}=7, \text{profit}=42)$, $I_3(\text{weight}=5, \text{profit}=25)$. We sort them by Profit/Weight ratio: $I_1(10), I_2(6), I_3(5)$. We are currently at a node where we included $I_1$ and excluded $I_2$. Prove mathematically using a Bounding Function whether we should continue exploring this branch, assuming we already found a known valid solution with a total profit of $60$.
**Step-by-step Solution:**
1. **Current State:** Included $I_1$, Excluded $I_2$.
   - Current Weight $CW = 4$ (from $I_1$).
   - Current Profit $CP = 40$ (from $I_1$).
2. **Calculate Upper Bound (Fractional Relaxation):** To know if this branch is worth exploring, we pretend we can take fractions of the remaining items to see the *absolute maximum* theoretical profit possible.
   - Remaining Capacity $= W - CW = 10 - 4 = 6$.
   - Next item is $I_3$. Weight is 5, Profit is 25.
   - We take all of $I_3$. Remaining capacity $= 6 - 5 = 1$. $CP$ becomes $40 + 25 = 65$.
   - No more items exist.
   - Upper Bound $U = 65$.
3. **Constraint Check:** Compare the theoretical Upper Bound $U$ against the `MaxProfit` found so far in the algorithm.
   - $U = 65$. `MaxProfit` $= 60$.
   - Since $65 > 60$, it is mathematically possible that this branch holds a better solution.
4. **Conclusion:** The algorithm will **NOT** prune this branch, and will continue to explore whether including or excluding $I_3$ yields the 65 profit. *(If $U$ had been 50, the algorithm would have pruned immediately without looking at $I_3$)*.

---

### Previous Year Questions & Solutions

1. **"Define N-Queens problem. Write down and explain an algorithm to solve N-Queens problem." [Dec 2019, July 2021]**
   - **Solution:**
     - **Definition:** The N-Queens problem asks to place $N$ chess queens on an $N \times N$ chessboard so that no two queens attack each other (no two queens share the same row, column, or diagonal).
     ```text
     NQueens(row, n):
         if row > n:
             print solution board and return true
         for col = 1 to n:
             if IsSafe(row, col):
                 board[row] = col        // place queen at (row, col)
                 NQueens(row + 1, n)     // recurse to next row
                 board[row] = 0          // backtrack
     
     IsSafe(r, c):
         for i = 1 to r - 1:
             if board[i] == c or abs(board[i] - c) == abs(i - r):
                 return false            // column or diagonal conflict
         return true
     ```

2. **"Explain 8-Queens problem and its backtracking solution." [April 2018]**
   - **Solution:**
     - The 8-Queens problem places 8 queens on an $8 \times 8$ board.
     - **Constraint Logic:** For a queen at $(i, j)$ and a new candidate queen at $(r, c)$:
       1. **Column Conflict:** $c == j$.
       2. **Diagonal Conflict:** $|r - i| == |c - j|$.
     - **Backtracking Mechanism:** The algorithm places queens row by row. If row $r$ has no safe column $c \in [1, 8]$, the branch is pruned. The algorithm steps back (backtracks) to row $r-1$, moves the queen in row $r-1$ to its next available safe column, and resumes forward search.

3. **"Explain the concept of Backtracking." [Sept 2020]**
   - **Solution:** Backtracking is a systematic search strategy for solving constraint satisfaction and optimization problems by building candidate solutions incrementally along a State Space Tree. Key features:
     1. **Depth-First Search (DFS):** Explores choices node by node.
     2. **Pruning (Bounding/Bounding Function):** If a partial candidate violates constraints, the algorithm immediately abandons the entire subtree (prunes the branch).
     3. **Backtrack Step:** Returns to the parent decision node and attempts the next choice.
