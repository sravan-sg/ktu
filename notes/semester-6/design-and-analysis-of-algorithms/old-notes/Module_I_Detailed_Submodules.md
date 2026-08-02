# CS302 Module I: Detailed Submodules Study Guide

## Submodule 1.1: Introduction to Algorithm Analysis

### Explanation
**Algorithm Analysis** is the process of evaluating the efficiency of an algorithm mathematically, independent of a specific programming language, compiler, or computer hardware. It focuses on how the execution time and memory requirements of an algorithm grow as the input size $n$ increases (asymptotic behavior). We use this to compare different algorithms that solve the same problem to determine which is optimal.

### Example
Suppose two friends write code to find the sum of the first $n$ numbers. 
- Friend A uses a loop adding numbers one by one.
- Friend B uses the mathematical formula $n(n+1)/2$. 
Algorithm analysis allows us to theoretically prove that Friend B's approach is superior because its execution time does not increase as $n$ grows, whereas Friend A's time grows proportionally to $n$.

### Applications & Use Cases
- **Algorithm Selection:** Software engineers use analysis to choose between Data Structures (e.g., choosing a Hash Table vs. a Binary Search Tree) based on expected data scale.
- **Performance Profiling:** Identifying the theoretical "bottleneck" in a complex data pipeline before writing and testing code.

### 3 Solved Numerical/Analytical Examples

**Example 1: Comparing Two Algorithms Theoretically**
*Problem:* Algorithm A takes $T_A(n) = 100n$ steps. Algorithm B takes $T_B(n) = 2n^2$ steps. Find the minimum integer input size $n$ for which Algorithm A becomes strictly faster than Algorithm B.
*Solution:*
1. Set the inequalities to find the crossover point: $100n < 2n^2$
2. Divide both sides by $2n$ (assuming $n > 0$): $50 < n$
3. Therefore, for $n \ge 51$, Algorithm A requires fewer steps than Algorithm B.

**Example 2: Analyzing Execution Steps of a Generic Sequence**
*Problem:* Calculate the total number of theoretical execution steps for the following pseudocode:
```text
1. Read n
2. sum = 0
3. for i = 1 to n do
4.    sum = sum + i
5. print sum
```
*Solution:*
1. Step 1 (Read): 1 step.
2. Step 2 (Assign): 1 step.
3. Step 3 (Loop init/check): $n+1$ steps (checks 1 extra time for exit condition).
4. Step 4 (Add & Assign): $n$ steps.
5. Step 5 (Print): 1 step.
Total steps: $1 + 1 + (n+1) + n + 1 = 2n + 4$.

**Example 3: Predicting Growth Rate Ratio**
*Problem:* An algorithm takes $T(n) = 5n^3$ milliseconds. If the input size is doubled from $n$ to $2n$, by what factor does the runtime increase?
*Solution:*
1. Calculate time for $2n$: $T(2n) = 5(2n)^3$
2. $T(2n) = 5(8n^3) = 40n^3$
3. Ratio = $T(2n) / T(n) = 40n^3 / 5n^3 = 8$.
The runtime increases by a factor of 8.

---

## Submodule 1.2: Time and Space Complexity

### Explanation
- **Time Complexity:** A mathematical representation of the time an algorithm takes to run, expressed as a function of the input size $n$. It abstracts away hardware speed, focusing on the growth rate of the number of operations.
- **Space Complexity:** A measure of the amount of working memory (RAM) an algorithm needs. It is the sum of **fixed space** (instructions, constants) and **variable/auxiliary space** (dynamic allocations, recursive stack). 

 **refference video:** https://youtu.be/h_BY76gPfCQ?si=xnLoneBFpwjxaabZ

### Example
Finding a name in a physical phone book.
- **Time Complexity:** If you read page by page, time grows linearly. If you open to the middle and halve the book repeatedly, time grows logarithmically.
- **Space Complexity:** If you only use your finger to keep track of the current page, the space complexity is constant. If you write down every single page number you visit on a notepad, space complexity grows.

### Applications & Use Cases
- **Embedded Devices:** A smartwatch has very limited RAM. Algorithms running on it must have constant space complexity.
- **Real-Time Data Streams:** High-frequency trading systems receive millions of events per second. The time complexity per event must be minimized to avoid a backlog.

### 3 Solved Numerical/Analytical Examples

**Example 1: Space Complexity of an Array Reversal (In-Place)**
*Problem:* Find the auxiliary space complexity of reversing an array of size $n$ by swapping elements from the ends towards the middle.
*Solution:*
1. We use two pointer variables `start` and `end`, and one temporary variable `temp` for the swap.
2. We do not allocate any new arrays.
3. The variables `start`, `end`, and `temp` consume a fixed amount of memory regardless of $n$.
*Space Complexity:* Auxiliary space is constant.

**Example 2: Space Complexity of an Array Copy**
*Problem:* An algorithm takes an array of size $n$, creates a new empty array of the same size, and copies elements over. What is the auxiliary space complexity?
*Solution:*
1. The new array allocated inside the function depends on the input size $n$.
2. It requires $n$ memory slots.
*Space Complexity:* Auxiliary space is proportional to $n$.

**Example 3: Time Complexity Function Formulation**
*Problem:* A function executes an initialization phase taking 50 ops, a processing loop taking $4n^2$ ops, and a cleanup phase taking $200$ ops. Express the time complexity function $T(n)$.
*Solution:*
1. $T(n) = \text{Init} + \text{Processing} + \text{Cleanup}$
2. $T(n) = 50 + 4n^2 + 200 = 4n^2 + 250$.
*Time Complexity:* The dominant term is $n^2$.

---

## Submodule 1.3: Elementary Operations and Computation of Time Complexity

### Explanation
To compute Time Complexity accurately, we count the number of **elementary operations**. An elementary operation is a basic computational step that takes a constant amount of time (e.g., assignment `x = 5`, arithmetic `a + b`, comparison `i < n`, memory array access `A[i]`, and return statements). We sum these operations to form a polynomial function $T(n)$.

### Example
Consider the line `y = a + b * c;`. It involves:
1. One multiplication `b * c`
2. One addition `a + (...)`
3. One assignment `y = ...`
Total = 3 elementary operations.

### Applications & Use Cases
- **Micro-Optimization:** In game engine development (e.g., rendering loops), developers count elementary operations to optimize critical inner loops (e.g., replacing a division operation with a bit-shift if possible, which lowers the constant factor).

### 3 Solved Numerical/Analytical Examples

**Example 1: Straight-Line Code**
*Problem:* Count the elementary operations in this swap function.
```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```
*Solution:*
1. `int temp = *a;` -> 1 memory read (dereference), 1 assignment = 2 ops.
2. `*a = *b;` -> 1 memory read, 1 memory write = 2 ops.
3. `*b = temp;` -> 1 memory read, 1 memory write = 2 ops.
*Total Operations:* $2 + 2 + 2 = 6$. Constant time.

**Example 2: Single Loop Computation**
*Problem:* Count operations for this sum function.
```c
int sum(int n) {
    int s = 0;
    for(int i = 1; i <= n; i++) {
        s = s + i;
    }
    return s;
}
```
*Solution:*
1. `int s = 0;` (1 op), `int i = 1;` (1 op) -> Total 2 outside loop.
2. Loop check `i <= n`: Evaluated $n+1$ times.
3. Loop body `s = s + i;`: 1 addition, 1 assignment -> 2 ops, executed $n$ times -> $2n$.
4. Loop increment `i++`: 1 addition, 1 assignment -> 2 ops, executed $n$ times -> $2n$.
5. `return s;`: 1 op.
*Total Operations:* $2 + (n+1) + 2n + 2n + 1 = 5n + 4$.

**Example 3: Nested Loops Computation**
*Problem:* Count operations.
```c
for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
        x = x + 1;
    }
}
```
*Solution:*
1. Outer loop runs $n$ times. Inner loop runs $n$ times for each outer loop.
2. The core body `x = x + 1` takes 2 ops (addition, assignment).
3. The core body is executed $n \times n = n^2$ times. Body ops = $2n^2$.
4. Inner loop overhead (check & increment): $(n+1)$ checks + $2n$ increments = $3n+1$ ops per outer loop. Across $n$ outer loops: $n(3n+1) = 3n^2 + n$.
5. Outer loop overhead: $(n+1)$ checks + $2n$ increments = $3n+1$.
*Total Operations:* $2n^2 + 3n^2 + n + 3n + 1 = 5n^2 + 4n + 1$.

---

## Submodule 1.4: Best, Worst, and Average Case Complexities

### Explanation
Algorithm performance often depends on the specific arrangement of the input data.
- **Worst-Case:** The maximum time required for any input of size $n$. (The "pessimistic" bound).
- **Best-Case:** The minimum time required for any input of size $n$. (The "optimistic" bound).
- **Average-Case:** The statistically expected time over all possible inputs of size $n$, assuming a uniform probability distribution.

### Example
Searching for a specific student's exam paper in a random stack of $n$ papers.
- **Best:** It's the very first paper on the top of the stack.
- **Worst:** It's at the very bottom, or not in the stack at all.
- **Average:** You usually find it somewhere around the middle of the stack.

### Applications & Use Cases
- **Cryptography & Security:** Algorithms must have the same Best, Worst, and Average case timings to avoid "Timing Attacks" where hackers deduce keys based on how long an algorithm takes to run.
- **Database Indexing:** B-Trees are used because their worst-case search time is guaranteed logarithmic, unlike Hash Tables whose worst-case is linear.

### 3 Solved Numerical/Analytical Examples

**Example 1: Linear Search Complexities**
*Problem:* Find $x$ in an array of size $n$. Calculate exact comparison counts.
*Solution:*
1. **Best-Case:** $x$ is at index 0. Comparisons = $1$.
2. **Worst-Case:** $x$ is at index $n-1$ or missing. The loop checks every element. Comparisons = $n$.
3. **Average-Case:** If $x$ is present, probability of it being at index $i$ is $1/n$.
   $\text{Average} = \sum_{i=1}^{n} (i \times \frac{1}{n}) = \frac{1}{n} \times \frac{n(n+1)}{2} = \frac{n+1}{2}$.

**Example 2: Insertion Sort Element Shift**
*Problem:* Analyze the number of shifts required to insert the $k$-th element into a sorted sub-array of size $k-1$.
*Solution:*
1. **Best-Case:** The $k$-th element is already larger than the $(k-1)$-th element. Shifts = 0.
2. **Worst-Case:** The $k$-th element is smaller than all elements. It must shift past all $k-1$ elements. Shifts = $k-1$.
3. **Average-Case:** It shifts past half the elements. Shifts $\approx \frac{k-1}{2}$.

**Example 3: Finding the Minimum Element in an Array**
*Problem:* Analyze the number of times the variable `min_val` is updated in the following array scan:
```c
int min_val = A[0];
for(int i=1; i<n; i++) {
    if(A[i] < min_val) min_val = A[i];
}
```
*Solution:*
1. **Best-Case:** Array is sorted in ascending order. `A[i] < min_val` is always false. Updates = $0$.
2. **Worst-Case:** Array is sorted in strictly descending order. `A[i] < min_val` is always true. Updates = $n-1$.
3. **Average-Case:** The probability that the $i$-th element is the smallest seen so far is $1/i$. Expected updates = $\sum_{i=2}^{n} \frac{1}{i}$, which is a Harmonic Number $H_n - 1 \approx \ln(n)$.

---

## Submodule 1.5: Complexity Calculation of Simple Algorithms

### Explanation
We combine the concepts of elementary operations and case-analysis to evaluate standard simple algorithms. By evaluating loops, conditionals, and data swaps, we derive polynomial equations representing the exact operational complexity of standard algorithms.

### Example
In Bubble Sort, the algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. We analyze it by counting the number of passes and the number of comparisons per pass.

### Applications & Use Cases
- **Standard Library Development:** When building sorting functions for programming languages, developers analyze simple algorithmic blocks to build hybrid algorithms (like Timsort, which combines Merge Sort and Insertion Sort).

### 3 Solved Numerical/Analytical Examples

**Example 1: Selection Sort Analysis**
*Problem:* Calculate the number of comparisons in Selection Sort for an array of size $n$.
*Solution:*
1. The algorithm has an outer loop $i$ from 0 to $n-2$.
2. The inner loop $j$ goes from $i+1$ to $n-1$, performing exactly 1 comparison each time to find the minimum.
3. For $i=0$, inner loop runs $n-1$ times.
4. For $i=1$, inner loop runs $n-2$ times.
...
5. For $i=n-2$, inner loop runs $1$ time.
*Total Comparisons:* $(n-1) + (n-2) + ... + 1 = \frac{n(n-1)}{2}$.

**Example 2: Bubble Sort Analysis**
*Problem:* Calculate the maximum number of comparisons and swaps in Bubble Sort.
*Solution:*
1. Outer loop runs $n-1$ times.
2. Inner loop performs comparisons. On the 1st pass, $n-1$ comparisons. On the 2nd, $n-2$.
*Total Comparisons:* $(n-1) + (n-2) + ... + 1 = \frac{n(n-1)}{2}$.
*Swaps:*
- **Best-Case (sorted):** 0 swaps.
- **Worst-Case (reversed):** Every comparison results in a swap. Total swaps = $\frac{n(n-1)}{2}$.

**Example 3: Standard Matrix Multiplication**
*Problem:* Analyze the core operation time complexity of multiplying two $n \times n$ matrices A and B to produce C.
*Solution:*
```c
for(i=0; i<n; i++) {
    for(j=0; j<n; j++) {
        C[i][j] = 0;
        for(k=0; k<n; k++) {
            C[i][j] += A[i][k] * B[k][j];
        }
    }
}
```
1. The three loops `i`, `j`, and `k` each run $n$ times.
2. The core operation `C[i][j] += A[i][k] * B[k][j]` executes $n \times n \times n = n^3$ times.
3. The core operation contains 1 multiplication, 1 addition, and 1 assignment (3 ops).
*Total core ops:* $3n^3$.

---

## Submodule 1.6: Recurrence Equations: Iteration Method and Recursion Tree Method

### Explanation
When an algorithm calls itself recursively, its running time is defined by a **Recurrence Equation**.
- **Iteration Method:** Also called the substitution or unrolling method. We expand the recurrence algebraically, substituting the equation into itself until a discernible mathematical series emerges, which we then solve down to the base case.
- **Recursion Tree Method:** A visual approach where we draw a tree representing the recursive calls. Each node displays the non-recursive cost (the work done at that specific level). We sum the costs across each horizontal level, and then sum all the levels.

**refference video:** https://youtu.be/w8tEY8luUSE?si=urXNvcAngMZDteIS.


### Example
Suppose a problem of size $n$ is divided into 2 subproblems of size $n/2$, and combining them takes $n$ steps. 
Recurrence: $T(n) = 2T(n/2) + n$.

### Applications & Use Cases
- **Divide and Conquer Frameworks:** Analyzing modern distributed processing frameworks (like MapReduce) often relies on solving recurrences to determine how effectively a workload scales when divided across multiple compute nodes.

### 3 Solved Numerical/Analytical Examples

**Example 1: Iteration Method for Arithmetic Series**
*Problem:* Solve $T(n) = T(n-1) + n$, with base case $T(1) = 1$.
*Solution:*
1. Unroll once: $T(n) = [T(n-2) + (n-1)] + n = T(n-2) + (n-1) + n$
2. Unroll twice: $T(n) = [T(n-3) + (n-2)] + (n-1) + n$
3. General form after $k$ steps: $T(n) = T(n-k) + (n-k+1) + ... + (n-1) + n$
4. Set $n-k = 1 \implies k = n-1$.
5. Substitute $k$: $T(n) = T(1) + 2 + 3 + ... + n$
6. $T(n) = 1 + 2 + 3 + ... + n = \frac{n(n+1)}{2}$.

**Example 2: Iteration Method for Geometric Series**
*Problem:* Solve $T(n) = 2T(n/2) + 1$, with $T(1) = 1$.
*Solution:*
1. $T(n) = 2[2T(n/4) + 1] + 1 = 4T(n/4) + 2 + 1$
2. $T(n) = 4[2T(n/8) + 1] + 2 + 1 = 8T(n/8) + 4 + 2 + 1$
3. General form after $k$ steps: $T(n) = 2^k T(n/2^k) + (2^{k-1} + ... + 4 + 2 + 1)$
4. Set $n/2^k = 1 \implies n = 2^k \implies k = \log_2 n$.
5. Substitute: $T(n) = n T(1) + (n - 1)$ (since sum of powers of 2 up to $2^{k-1}$ is $2^k - 1$).
6. $T(n) = n(1) + n - 1 = 2n - 1$.

**Example 3: Recursion Tree Method**
*Problem:* Solve $T(n) = 3T(n/4) + cn^2$.
*Solution:*
1. **Level 0 (Root):** Cost is $cn^2$. It branches into 3 children, each size $n/4$.
2. **Level 1:** There are 3 nodes. The size is $n/4$. Each node cost is $c(n/4)^2 = cn^2 / 16$.
   Level total = $3 \times (cn^2 / 16) = \frac{3}{16}cn^2$.
3. **Level 2:** There are 9 nodes ($3^2$). Size is $n/16$. Node cost is $c(n/16)^2 = cn^2 / 256$.
   Level total = $9 \times (cn^2 / 256) = (\frac{3}{16})^2 cn^2$.
4. **General Level $i$:** The cost is $(\frac{3}{16})^i cn^2$.
5. **Total Cost:** This is a decreasing geometric series: $cn^2 [1 + \frac{3}{16} + (\frac{3}{16})^2 + ... ]$.
6. Because the common ratio $(3/16) < 1$, the infinite sum converges to a constant factor.
   Total cost is bounded by a constant multiple of $n^2$.
