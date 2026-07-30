# Module VI: Back Tracking, Branch and Bound, and Complexity Theory

This final module focuses on solving complex, highly constrained problems that require exploring vast "state-space trees," as well as classifying problems based on their overall solvability (Complexity Theory).

### 1. Backtracking: The Control Abstraction
#### Explanation:
Backtracking is an algorithmic paradigm that tries to find a solution by incrementally building candidates. When it realizes that a partial candidate cannot possibly lead to a valid solution, it abandons it ("backtracks") and tries the next available option. It is an organized, optimized version of "brute force" that prunes invalid paths early to save time.

#### The Control Abstraction (Conceptual Framework):
```plaintext
Algorithm Backtrack(k)
// k is the current stage/level in the state-space tree
{
    for (each x in possible_choices) do
    {
        if (isSafe(x)) then // If this choice doesn't violate constraints
        {
            solution[k] = x;
            if (isCompleteSolution(solution)) then
                print solution;
            else
                Backtrack(k + 1); // Move to the next stage
        }
    }
}
```
#### Applications:
Solving Sudoku puzzles, finding paths in a maze, and solving constraint-satisfaction problems like scheduling.

### 2. Backtracking: The N-Queen's Problem
#### Explanation:
The N-Queens problem asks you to place $N$ chess queens on an $N \times N$ chessboard so that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

- **The Strategy:** Place queens column by column, starting from the leftmost column.
- In a given column, check each row. If placing a queen there is "safe", place it and recursively try to place a queen in the next column.
- If no safe row is found in a column, backtrack to the previous column and move that queen to its next safe row.

#### Solved Example 1: 4-Queens Problem
**Problem:** Place 4 queens on a $4 \times 4$ board.

**Step-by-Step Backtracking Trace:**
1. **Col 1:** Place Q1 at $(1, 1)$.
2. **Col 2:** Row 1 is unsafe (row clash). Row 2 is unsafe (diagonal clash). Place Q2 at $(3, 2)$.
3. **Col 3:** Row 1 is unsafe. Row 2 is unsafe. Row 3 is unsafe. Row 4 is unsafe. (Dead End).
4. **Backtrack:** Go back to Col 2. Move Q2 to $(4, 2)$.
5. **Col 3:** Place Q3 at $(2, 3)$.
6. **Col 4:** All rows unsafe. (Dead End).
7. **Backtrack:** Go back to Col 1. Move Q1 to $(2, 1)$.
8. **Col 2:** Place Q2 at $(4, 2)$.
9. **Col 3:** Place Q3 at $(1, 3)$.
10. **Col 4:** Place Q4 at $(3, 4)$.

**Result:** A valid solution is found: $[(2,1), (4,2), (1,3), (3,4)]$.

### 3. Backtracking: 0/1 Knapsack Problem
#### Explanation:
You are given $N$ items, each with a weight and a value, and a knapsack with a maximum capacity $W$. You must either take an item completely or leave it (0/1). The goal is to maximize the value without exceeding capacity.
While Dynamic Programming is the standard approach, Backtracking can solve it by exploring a state-space tree where the left branch includes an item, and the right branch excludes it.

- **The Strategy:** We traverse the tree. If adding an item exceeds the capacity $W$, we prune that branch. We keep a running total of the maximum profit found so far.

#### Solved Example 2: 0/1 Knapsack via Backtracking
**Problem:** $W = 5$. Items:
- $I_1: w=2, v=3$
- $I_2: w=3, v=4$
- $I_3: w=4, v=5$

**Step-by-Step Trace:**
1. Start at $I_1$.
2. **Include $I_1$:** Total Weight=2, Value=3. Space left=3.
   - **Include $I_2$:** Total Weight=5, Value=7. Space left=0. (Best so far: 7).
     - **Include $I_3$:** Weight=9 (Exceeds 5). Prune.
   - **Exclude $I_2$:** Weight=2, Value=3. Space left=3.
     - **Include $I_3$:** Weight=6 (Exceeds 5). Prune.
3. **Exclude $I_1$:** Total Weight=0, Value=0. Space left=5.
   - **Include $I_2$:** Weight=3, Value=4.
     - **Include $I_3$:** Weight=7 (Exceeds). Prune.

**Result:** The maximum value is 7 (Including $I_1$ and $I_2$).

### 4. Branch and Bound: Travelling Salesman Problem (TSP)
#### Explanation:
Branch and Bound (B&B) is an optimization technique specifically for minimization/maximization problems. Like backtracking, it explores a state-space tree, but it computes a Bound (an estimated minimum or maximum cost) at each node. If a node's bound is worse than the best solution already found, the entire subtree is pruned.

In the Travelling Salesman Problem, a salesman must visit $N$ cities exactly once and return to the start, minimizing the total travel distance. B&B solves this efficiently by calculating a "Cost Matrix Reduction" lower bound to prune expensive paths.

#### Applications:
Logistics and delivery routing, manufacturing (drilling holes in circuit boards efficiently).

#### Solved Example 3: Branch and Bound TSP Concept
**Problem:** Imagine a 4-city graph. The current best known full tour costs $100$.

**Step-by-Step Pruning Logic:**
1. Start at City A.
2. **Branch to City B.** You calculate the lower bound (the absolute minimum cost required to complete the rest of the tour based on the remaining unvisited cities). The bound calculation returns $85$.
   - Since $85 < 100$, it is possible this path holds a better solution. We keep exploring this branch.
3. **Branch to City C instead.** The lower bound calculation for the $A \rightarrow C$ path returns $115$.
   - Since the absolute minimum cost of finishing the $A \rightarrow C$ path is $115$, and we already have a valid tour that costs $100$, we instantly prune the $A \rightarrow C$ branch. We do not evaluate any further cities down this path.

### 5. Introduction to Complexity Theory
Complexity Theory categorizes problems based on how inherently difficult they are for a computer to solve.

#### Tractable vs. Intractable Problems:
- **Tractable:** Problems that can be solved in a reasonable amount of time (Polynomial time: $O(n)$, $O(n^2)$, etc.). Example: Sorting an array.
- **Intractable:** Problems that cannot be solved quickly as the input grows. They take Exponential ($O(2^n)$) or Factorial ($O(n!)$) time. Example: Brute-forcing a 256-bit cryptographic key.

#### The Complexity Classes
- **P Class (Polynomial Time):**
  - The set of all decision problems that can be solved by a deterministic computer in polynomial time.
  - *Example:* Searching for an item, determining if a graph is connected.
- **NP Class (Non-Deterministic Polynomial Time):**
  - The set of problems where, if you are given a proposed answer, you can verify if that answer is correct in polynomial time. However, finding the answer might take exponential time.
  - *Note:* Every problem in P is also in NP.
- **NP-Hard Class:**
  - These are the "hardest" problems in computer science. A problem is NP-Hard if every problem in NP can be reduced to it in polynomial time. An NP-Hard problem does not have to be in NP (it might be impossible to even verify quickly).
  - *Example:* The Halting Problem.
- **NP-Complete Class:**
  - The sweet spot where NP and NP-Hard intersect. A problem is NP-Complete if it is both in NP (verifiable quickly) AND it is NP-Hard.
  - If anyone ever finds a fast (Polynomial) algorithm to solve just one NP-Complete problem, they will have proven that $P = NP$, fundamentally changing modern cryptography and computing.
  - *Example:* The Boolean Satisfiability Problem (SAT), The Travelling Salesman Problem (Decision version).

#### Polynomial Time Reductions:
This is the technique used to prove a problem is NP-Complete. If you take a known hard problem (Problem A) and transform it into Problem B using a fast, polynomial-time algorithm, then Problem B must be at least as hard as Problem A.
