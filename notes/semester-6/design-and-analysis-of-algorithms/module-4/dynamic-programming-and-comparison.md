# Module 4 — Topic 2: Dynamic Programming & Strategy Comparison

> **Module 4**: Divide and Conquer & Dynamic Programming  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
**Dynamic Programming (DP)** is built on a single, powerful philosophy: *never calculate the same thing twice.*
While Divide and Conquer breaks problems into independent pieces, many real-world problems break into **Overlapping Subproblems** (the same tiny problem needs to be solved repeatedly). If a naive algorithm just recursively computes them, it hits an exponential time complexity $O(2^n)$.
DP introduces a "memory" (a table or array). The first time it solves a tiny problem, it stores the answer. The next time, it simply looks it up in $O(1)$ time (Memoization / Tabulation). 
DP is specifically used for Optimization Problems where the **Principle of Optimality** holds: an optimal overall solution can be built strictly by combining optimal sub-solutions.

### Example
Suppose you are asked to calculate $1 + 1 + 1 + 1 + 1$. You count and say "5".
If someone then asks you to calculate $1 + 1 + 1 + 1 + 1 + 1$, you don't start counting from the beginning again. You just remember your previous answer (5), add 1 to it, and immediately say "6". That is Dynamic Programming in real life—using past stored answers to instantly solve the next step.

### Applications & Use Cases
- **Genomic Sequencing**: The Smith-Waterman algorithm uses a DP matrix to align DNA sequences, identifying identical gene fragments without generating trillions of recursive combinations.
- **Network Routing**: The Bellman-Ford algorithm (which powers the BGP protocol routing the global Internet) uses DP to calculate the shortest path to all IP addresses, even handling negative cost loops.
- **Natural Language Processing (NLP)**: Spell-checkers use DP (Levenshtein Distance) to find the minimum number of character edits required to turn a misspelled word into a dictionary word.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Overlapping Subproblems in Fibonacci
**Problem:** Prove the computational savings of Dynamic Programming over simple recursion when calculating the $5^{th}$ Fibonacci number: $F(5)$.
**Step-by-step Solution:**
1. **Naive Recursion Trace:**
   To calculate $F(5)$, the system calls $F(4) + F(3)$.
   - $F(4)$ calls $F(3) + F(2)$.
   - $F(3)$ calls $F(2) + F(1)$.
   - The original $F(3)$ branch *also* calls $F(2) + F(1)$.
2. **Count the Redundancy:**
   Notice that $F(3)$ is calculated completely from scratch 2 separate times. $F(2)$ is calculated completely from scratch 3 separate times.
   Time Complexity $= O(2^n)$. For $F(50)$, this takes trillions of operations.
3. **Dynamic Programming (Memoization):**
   We create an array `Memo[]`. 
   We calculate $F(2)$, store it in `Memo[2]`.
   When $F(3)$ needs $F(2)$, it just reads `Memo[2]` instantly.
   When the second branch asks for $F(3)$, it reads `Memo[3]` instantly.
4. **Conclusion:** No value is calculated twice. The time complexity plummets from exponential $O(2^n)$ to purely linear $O(n)$.

### Example 2: Matrix Chain Multiplication (MCM) Optimization [April 2018, Dec 2019]
**Problem:** Write and explain an algorithm to find the optimal parenthesization of matrix chain product. We have three matrices: $A_{10 \times 100}$, $B_{100 \times 5}$, and $C_{5 \times 50}$. Prove why DP must be used to choose the parenthesization order by calculating the scalar multiplications for both options.
**Step-by-step Solution:**
1. **Understand Matrix Multiplication Cost:** Multiplying a matrix of size $(p \times q)$ with a matrix of size $(q \times r)$ takes $p \times q \times r$ scalar multiplications.
2. **Option 1: Calculate $(AB)C$**
   - Multiply $AB$: $10 \times 100 \times 5 = 5,000$ operations. Result is a $(10 \times 5)$ matrix.
   - Multiply $(AB)$ by $C$: $10 \times 5 \times 50 = 2,500$ operations.
   - **Total Option 1 Cost** $= 5,000 + 2,500 =$ **$7,500$** operations.
3. **Option 2: Calculate $A(BC)$**
   - Multiply $BC$: $100 \times 5 \times 50 = 25,000$ operations. Result is a $(100 \times 50)$ matrix.
   - Multiply $A$ by $(BC)$: $10 \times 100 \times 50 = 50,000$ operations.
   - **Total Option 2 Cost** $= 25,000 + 50,000 =$ **$75,000$** operations.
4. **Conclusion:** A simple change in grouping caused a 10x explosion in computational cost (75k vs 7.5k). MCM uses a DP table to systematically evaluate and memoize the cost of every sub-pairing $M[i,j]$, guaranteeing the absolute minimum parenthesization cost.

### Example 3: Compare D&C vs DP [Dec 2019]
**Problem:** Give a comparison between dynamic programming and Divide and conquer strategy.
**Step-by-step Solution:**
1. **Subproblem Dependency:**
   - **D&C:** In Merge Sort, the left half of the array is completely independent of the right half. Sorting the left provides zero information about how to sort the right. There are NO overlapping subproblems.
   - **DP:** In Bellman-Ford, finding the shortest path of length 3 depends *entirely* on the stored results of the shortest path of length 2. The subproblems strictly overlap.
2. **Direction of Solution:**
   - **D&C (Top-Down):** It takes the massive initial array and aggressively cuts it in half down to the base case.
   - **DP (Bottom-Up):** It explicitly starts at the base case (paths of length 0), solves them, and uses the table to steadily build up to the global solution (paths of length $V-1$).
3. **Conclusion:** Use D&C when sub-tasks don't overlap. Use DP when they do.

---

### Previous Year Questions & Solutions

1. **"List and explain the characteristic properties associated with a problem that can be solved using dynamic programming." [April 2018, Dec 2019, July 2021, Sept 2020]**
   - **Solution:** A problem can be solved using Dynamic Programming if and only if it exhibits two core properties:
     1. **Optimal Substructure (Principle of Optimality):** An optimal solution to the overall problem contains optimal solutions to its subproblems. If $S_{opt}$ is optimal for $P$, any sub-path within $S_{opt}$ must also be optimal for the corresponding subproblem.
     2. **Overlapping Subproblems:** The recursive space of the problem visits the same small subproblems repeatedly (e.g. computing $F(3)$ multiple times in Fibonacci). Instead of recomputing, DP stores the solution in a table (memoization/tabulation) so subsequent calls run in $O(1)$ time.

2. **"Write and explain an algorithm to find the optimal parenthesization of matrix chain product." [April 2018, Dec 2019]**
   - **Solution:**
     ```text
     MatrixChainOrder(p, n):
         // p is array of dimensions where Matrix i has dimension p[i-1] x p[i]
         Initialize m[1..n, 1..n] to 0
         for L = 2 to n:                 // L is chain length
             for i = 1 to n - L + 1:
                 j = i + L - 1
                 m[i, j] = infinity
                 for k = i to j - 1:
                     q = m[i, k] + m[k+1, j] + p[i-1] * p[k] * p[j]
                     if q < m[i, j]:
                         m[i, j] = q
                         s[i, j] = k     // store split point k
         return m and s
     ```
     - **Explanation:** $m[i,j]$ stores the minimum number of scalar multiplications required to compute $A_i \dots A_j$. We test all possible split points $k$ between $i$ and $j-1$, adding the cost of multiplying the two resulting sub-matrices ($p_{i-1} \cdot p_k \cdot p_j$). Time complexity is $O(n^3)$, space is $O(n^2)$.

3. **"Give a comparison between Dynamic Programming and Divide and Conquer strategy." [Dec 2019, July 2021, Sept 2020]**
   - **Solution:**
     | Feature | Divide and Conquer | Dynamic Programming |
     | :--- | :--- | :--- |
     | **Subproblem Relationship** | **Independent** (no overlap, e.g. Left/Right half of Merge Sort) | **Overlapping** (same subproblems solved multiple times) |
     | **Solution Direction** | **Top-Down** (recursively divides until base case) | **Bottom-Up** (solves smallest subproblems first, builds up) or Top-Down + Memoization |
     | **Memory / Storage** | Requires minimal memory (call stack only) | Requires table/array to store subproblem results |
     | **Optimization** | Used for searching/sorting/arithmetic | Used for combinatorial optimization problems |
     | **Examples** | Merge Sort, Quick Sort, Binary Search | Matrix Chain Multiplication, Bellman-Ford, 0/1 Knapsack |
