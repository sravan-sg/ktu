# Module 1: Last-Minute Revision & Submodule Guide

> **Semester**: S6 | **Subject**: Design and Analysis of Algorithms (CS302)  
> **Purpose**: Rapid, last-minute review of core Module 1 concepts, simple explanations, practical examples, use cases, and 3 solved micro-problems per submodule.

---

## Submodule 1.1: Time and Space Complexity & Elementary Operations

### 1. Explanation
- **Algorithm Analysis**: Evaluating how the time and memory requirements of an algorithm grow as input size $n$ increases, without depending on specific computer hardware or programming languages.
- **Time Complexity**: The total number of basic steps (like additions, comparisons, assignments) executed by an algorithm as a function of input size $n$.
- **Space Complexity**: The total RAM memory needed by an algorithm to run to completion.
  $$\text{Total Space } S(n) = \text{Fixed Space (Code, Constants)} + \text{Auxiliary Space (Dynamic Memory, Stack Frames)}$$
- **Elementary Operation**: A single basic step (like `x = 5`, `a + b`, or `i < n`) that takes 1 unit of time.

### 2. Real-World Example
Think of calculating total shopping bill items:
- If you read $n$ items one by one on a paper receipt, the time spent grows linearly with $n$ (Linear Time Complexity).
- If you only use one calculator screen to keep the running total, your extra memory needed is just 1 slot regardless of receipt length (Constant Auxiliary Space).

### 3. Applications & Use Cases
- **Smartphones & Embedded Devices**: Memory-constrained devices require algorithms with $O(1)$ auxiliary space so they don't run out of RAM.
- **High-Frequency Trading**: Financial systems require low time complexity per trade event to process thousands of transactions per second without lagging.

### 4. 3 Solved Numerical / Analytical Micro-Examples

#### Example 1: In-Place Array Swap Memory Analysis
- **Problem**: Calculate the auxiliary space complexity of swapping two array elements using a single temporary variable `temp`.
- **Solution**:
  1. Only 1 extra variable `temp` is used.
  2. Memory needed does not change with array size $n$.
  3. **Auxiliary Space**: Constant $O(1)$.

#### Example 2: Step Count of a Single Loop
- **Problem**: Find total elementary operations executed in the following code:
  ```c
  int sum = 0;
  for (int i = 1; i <= n; i++) {
      sum = sum + i;
  }
  ```
- **Solution**:
  1. `int sum = 0` (1 op), `int i = 1` (1 op) $\rightarrow$ 2 initial ops.
  2. Loop check `i <= n`: evaluated $n + 1$ times.
  3. Loop body `sum = sum + i` (2 ops) executed $n$ times $\rightarrow 2n$ ops.
  4. Loop increment `i++` (2 ops) executed $n$ times $\rightarrow 2n$ ops.
  5. **Total Operations**: $2 + (n+1) + 2n + 2n = 5n + 3$. Time Complexity $= \Theta(n)$.

#### Example 3: Space Overhead of Array Copying
- **Problem**: An algorithm takes an array of size $n$ and creates a duplicate array of size $n$ to store output. What is the space complexity?
- **Solution**:
  1. The new array requires $n$ memory slots.
  2. **Auxiliary Space**: Linear $O(n)$.

---

## Submodule 1.2: Best, Worst, and Average Case Complexities

### 1. Explanation
An algorithm's speed often depends on the arrangement of input data:
- **Worst-Case $T_{\text{worst}}(n)$**: The maximum time required over all possible inputs of size $n$. Provides a strict safety guarantee.
- **Best-Case $T_{\text{best}}(n)$**: The minimum time required over all inputs of size $n$. Lucky scenario, rarely useful in practice.
- **Average-Case $T_{\text{avg}}(n)$**: The expected time averaged over all possible inputs of size $n$, assuming equal likelihood of input patterns.

### 2. Real-World Example
Searching for a friend's contact number in a list:
- **Best-Case**: Friend's name is the very first entry on the list (1 check).
- **Worst-Case**: Friend's name is the very last entry, or not on the list at all ($n$ checks).
- **Average-Case**: Friend's name is somewhere around the middle ($\approx n/2$ checks).

### 3. Applications & Use Cases
- **Mission-Critical Systems**: Flight control software and medical devices rely strictly on worst-case bounds to prevent unexpected freezing or delays.
- **Database Engine Indexing**: Databases use B-Trees because their worst-case search time is guaranteed $O(\log n)$, avoiding linear slowdowns.

### 4. 3 Solved Numerical / Analytical Micro-Examples

#### Example 1: Linear Search Exact Comparisons
- **Problem**: Calculate best, worst, and average case comparisons for finding target $x$ in an array of size $n$.
- **Solution**:
  1. **Best-Case**: $x$ is at index 0 $\rightarrow 1$ comparison.
  2. **Worst-Case**: $x$ is at index $n-1$ or missing $\rightarrow n$ comparisons.
  3. **Average-Case**: Assuming $x$ is equally likely at any position $1 \dots n$:
     $$\text{Avg} = \frac{1 + 2 + 3 + \dots + n}{n} = \frac{n(n+1)}{2n} = \frac{n+1}{2}$$

#### Example 2: Finding Minimum Element Update Counts
- **Problem**: Analyze how many times `min` updates in `int min = A[0]; for(i=1; i<n; i++) if(A[i] < min) min = A[i];`.
- **Solution**:
  1. **Best-Case (Sorted Ascending)**: $A[0]$ is already smallest $\rightarrow 0$ updates.
  2. **Worst-Case (Sorted Descending)**: Every element is smaller than previous $\rightarrow n-1$ updates.
  3. **Average-Case**: Expected updates $\approx \ln(n)$ (Harmonic series sum).

#### Example 3: Insertion Sort Shift Analysis
- **Problem**: Calculate worst-case and best-case element shifts in Insertion Sort for array size $n$.
- **Solution**:
  1. **Best-Case (Already Sorted)**: 0 shifts $\rightarrow \Theta(n)$ time.
  2. **Worst-Case (Reverse Sorted)**: $1 + 2 + \dots + (n-1) = \frac{n(n-1)}{2}$ shifts $\rightarrow \Theta(n^2)$ time.

---

## Submodule 1.3: Complexity Calculation of Simple Algorithms

### 1. Explanation
To compute the overall complexity of a block of code, we identify loop structures, conditional checks, and variable updates. We sum step counts across nested loops to construct a polynomial function representing total operations.

### 2. Real-World Example
Thinking about reading pages in a book:
- Reading $n$ pages one by one $\rightarrow$ Linear $\Theta(n)$.
- For every page, comparing it against every other page $\rightarrow$ Nested Loops $\Theta(n^2)$.
- Cutting remaining unread pages in half every time $\rightarrow$ Logarithmic $\Theta(\log n)$.

### 3. Applications & Use Cases
- **Game Development**: Game render loops run 60 times per second. Developers analyze inner loop operation counts to eliminate unnecessary calculations and maintain high FPS.

### 4. 3 Solved Numerical / Analytical Micro-Examples

#### Example 1: Dependent Nested Loop Summation
- **Problem**: Compute the time complexity of:
  ```c
  for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= i; j++) {
          x = x + 1;
      }
  }
  ```
- **Solution**:
  1. When $i=1$, inner loop runs 1 time.
  2. When $i=2$, inner loop runs 2 times.
  3. Total inner runs $= 1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2} = \frac{n^2 + n}{2}$.
  4. **Complexity**: $\Theta(n^2)$.

#### Example 2: Logarithmic Multiplying Loop
- **Problem**: Find iterations of `i = 1; while(i < n) { i = i * 3; }`.
- **Solution**:
  1. Values of $i$: $1, 3^1, 3^2, 3^3, \dots, 3^k$.
  2. Loop stops when $3^k \ge n \implies k = \lceil \log_3 n \rceil$.
  3. **Complexity**: $\Theta(\log_3 n) = \Theta(\log n)$.

#### Example 3: Matrix Multiplication Core Operations
- **Problem**: Calculate core multiplications in standard $n \times n$ matrix multiplication.
- **Solution**:
  1. Requires 3 nested loops (for row $i$, column $j$, dot product $k$).
  2. Each loop runs $n$ times $\rightarrow n \times n \times n = n^3$ iterations.
  3. **Core Multiplications**: $n^3 \rightarrow \Theta(n^3)$.

---

## Submodule 1.4: Recurrence Equations — Iteration Method

### 1. Explanation
Recursive algorithms call themselves on smaller inputs. Their running time is written as a **Recurrence Equation** (e.g. $T(n) = T(n-1) + c$).

The **Iteration Method** (or Unrolling Method) repeatedly expands $T(\text{subproblem})$ until a clear algebraic series appears, which is then solved down to the base case $T(1)$.

### 2. Real-World Example
Russian Matryoshka dolls: To find the smallest inner doll in a stack of $n$ nested dolls, you open doll $n$, leaving a stack of $n-1$ dolls. You repeat this $n-1$ times until reaching the tiny base doll.

### 3. Applications & Use Cases
- **Analyzing Recursive Search & Divide-and-Conquer**: Used by software engineers to prove the theoretical runtime of recursive functions like Merge Sort or QuickSort before implementation.

### 4. 3 Solved Numerical / Analytical Micro-Examples

#### Example 1: Solving $T(n) = T(n-1) + 1$ with $T(1) = 1$
- **Problem**: Solve using Iteration Method.
- **Solution**:
  1. $T(n) = T(n-1) + 1$
  2. $T(n) = [T(n-2) + 1] + 1 = T(n-2) + 2$
  3. After $k$ steps: $T(n) = T(n-k) + k$
  4. Base case $n - k = 1 \implies k = n - 1$.
  5. $T(n) = T(1) + (n - 1) = 1 + n - 1 = n \rightarrow \Theta(n)$.

#### Example 2: Solving $T(n) = T(n-1) + n$ with $T(1) = 1$
- **Problem**: Solve using Iteration Method.
- **Solution**:
  1. $T(n) = T(n-1) + n = T(n-2) + (n-1) + n$
  2. After $k$ steps: $T(n) = T(n-k) + \sum_{j=0}^{k-1} (n - j)$
  3. Base case $n - k = 1 \implies k = n - 1$.
  4. $T(n) = T(1) + 2 + 3 + \dots + n = \frac{n(n+1)}{2} \rightarrow \Theta(n^2)$.

#### Example 3: Solving $T(n) = 2T(n-1) + 1$ with $T(0) = 1$ (Tower of Hanoi)
- **Problem**: Solve using Iteration Method.
- **Solution**:
  1. $T(n) = 2[2T(n-2) + 1] + 1 = 2^2 T(n-2) + 2 + 1$
  2. After $k$ steps: $T(n) = 2^k T(n-k) + (2^{k-1} + \dots + 2 + 1)$
  3. Base case $n - k = 0 \implies k = n$.
  4. $T(n) = 2^n(1) + (2^n - 1) = 2^{n+1} - 1 \rightarrow \Theta(2^n)$.

---

## Submodule 1.5: Recurrence Equations — Recursion Tree Method

### 1. Explanation
The **Recursion Tree Method** converts recursive calls into a visual tree diagram.
- Each node represents the cost of work done at that single step.
- We sum the node costs across each level of the tree.
- We sum all level costs from root to leaves to get the final total time.

### 2. Real-World Example
Organizing a tournament bracket:
- Root match divides into 2 semi-finals ($n/2$), which divide into 4 quarter-finals ($n/4$).
- The height of the tournament bracket tree is $\log_2 n$.

### 3. Applications & Use Cases
- **Distributed Computing & MapReduce**: Analyzing how workloads split across worker nodes and combine results in cluster computing architectures.

### 4. 3 Solved Numerical / Analytical Micro-Examples

#### Example 1: Merge Sort Tree $T(n) = 2T(n/2) + cn$
- **Problem**: Calculate level costs and total cost using Recursion Tree.
- **Solution**:
  1. **Root (Level 0)**: Cost $= cn$.
  2. **Level 1**: 2 nodes of cost $c(n/2) \rightarrow 2 \times c(n/2) = cn$.
  3. **Level 2**: 4 nodes of cost $c(n/4) \rightarrow 4 \times c(n/4) = cn$.
  4. **Cost per level** is constant $cn$.
  5. **Tree Height** $= \log_2 n$.
  6. **Total Cost**: $cn \times (\log_2 n + 1) \rightarrow \Theta(n \log n)$.

#### Example 2: Binary Search Tree $T(n) = T(n/2) + c$
- **Problem**: Solve using Recursion Tree.
- **Solution**:
  1. **Root**: Cost $= c$.
  2. **Level 1**: 1 node of cost $= c$.
  3. **Tree Height**: $\log_2 n$.
  4. **Total Cost**: $c \times \log_2 n \rightarrow \Theta(\log n)$.

#### Example 3: Geometrically Decreasing Tree $T(n) = 3T(n/4) + cn^2$
- **Problem**: Determine dominant layer in Recursion Tree.
- **Solution**:
  1. **Root Cost**: $cn^2$.
  2. **Level 1 Cost**: $3 \times c(n/4)^2 = \frac{3}{16} cn^2$.
  3. **Level 2 Cost**: $9 \times c(n/16)^2 = (\frac{3}{16})^2 cn^2$.
  4. Since ratio $\frac{3}{16} < 1$, costs decrease exponentially down levels.
  5. **Root node dominates** $\rightarrow \Theta(n^2)$.
