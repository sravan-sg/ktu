# Module 1: Introduction to Algorithm Analysis & Recurrences — Detailed Study Guide

> **Semester**: S6 | **Subject**: Design and Analysis of Algorithms (CS302)  
> **Target Outcome**: Master the foundational tools for evaluating algorithm speed and memory usage, calculating operation counts, analyzing best/worst/average cases, and solving recursive recurrence equations using the Iteration Method and Recursion Tree Method.

---

## 1. Core Intuition & Fundamental Concepts

### 1.1 What is an Algorithm?
Imagine you are following a recipe to bake a cake. The recipe gives you exact, step-by-step instructions. If the instructions are vague, you might end up with a ruined cake. In computer science, an **algorithm** is just like a strict recipe for a computer: a clear, step-by-step set of instructions to convert a given **input** into a desired **output**.

To be a valid algorithm, five basic rules must be satisfied:
1. **Input**: It receives zero or more values from the outside world.
2. **Output**: It produces at least one result.
3. **Definiteness**: Every step is completely clear and has only one meaning.
4. **Finiteness**: It must eventually stop after a finite number of steps (it cannot run forever in an infinite loop).
5. **Effectiveness**: Every instruction must be simple enough to be done by hand with pencil and paper.

---

### 1.2 Why Do We Analyze Algorithms?
Suppose two programmers are asked to write a program to search for a user's ID in a database of 1 million users:
- **Programmer A** checks every user from the beginning to the end one by one.
- **Programmer B** uses a smart binary search that repeatedly cuts the search area in half.

If we test both programs on a supercomputer with 5 users, both will run instantly. But on a phone with 1 million users:
- Programmer A's code might take **1 million steps**.
- Programmer B's code takes only **20 steps** ($\log_2(1,000,000) \approx 20$).

**Algorithm Analysis** is the mathematical tool that lets us compare the efficiency of different solutions **on paper** before spending hours writing and testing code. It tells us how the running time and memory footprint will grow as the input size $n$ gets larger.

---

### 1.3 Time Complexity and Space Complexity

#### Time Complexity
**Time Complexity** is a measure of how the total running time of an algorithm grows as the size of the input data ($n$) increases. We measure time not in clock seconds (which depend on how fast your laptop CPU is), but in the **number of basic operations** executed.

#### Space Complexity
**Space Complexity** measures how much extra memory (RAM) an algorithm needs to run to completion as a function of input size $n$.

Memory needed by an algorithm comes in two parts:
$$\text{Total Space } S(n) = \text{Fixed Space} + \text{Auxiliary Space}$$

1. **Fixed Space**: Memory needed for the code instructions, simple constants, and simple variables. This memory does not change when the input grows larger.
2. **Auxiliary Space**: Temporary memory created while running the program, such as new arrays allocated on the heap or function call records saved on the stack during recursion.

```
+-------------------------------------------------------------+
|                      Total Memory S(n)                      |
+------------------------------------+------------------------+
|             Fixed Space            |    Auxiliary Space     |
| (Program code, fixed constants)    | (New arrays, recursion |
|                                    |   call stack frames)   |
+------------------------------------+------------------------+
```

---

### 1.4 The Computer Model: Random Access Machine (RAM)
To analyze algorithms fairly without worrying about whether you are running Mac, Windows, or Linux, computer scientists use a simplified model called the **Random Access Machine (RAM) model**:
- **One step at a time**: Instructions run sequentially, one after another (no multi-core parallelism).
- **Constant Cost for Basic Steps ($O(1)$)**: Simple operations take 1 unit of time:
  - Math: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`).
  - Logic & Checks: comparing numbers (`a < b`), boolean AND/OR.
  - Memory: reading or writing to a variable or array slot (`A[i] = x`).
- **Equal Access Speed**: Reading any memory location takes the exact same amount of time regardless of where it is stored.

---

## 2. Theoretical Framework & Formal Definitions

### 2.1 Elementary Operations and Step-Count (Frequency) Method
An **elementary operation** is a single basic action that takes a constant amount of time (1 unit of work). 

The **Frequency Count Method** calculates total time complexity by adding up how many times each line of code runs:

$$\text{Total Time } T(n) = \sum (\text{Cost of Line}) \times (\text{How many times line executes})$$

#### Step-Count Walkthrough: Array Sum
Let's analyze a simple function that adds up $n$ numbers in an array:

```python
def compute_sum(A, n):
    total = 0            # Line 1: Runs 1 time
    for i in range(n):   # Line 2: Checks condition (n + 1) times
        total += A[i]    # Line 3: Runs n times
    return total         # Line 4: Runs 1 time
```

Let's tabulate the steps:

| Line | Statement | Cost per execution | Frequency (Times executed) | Total Line Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Line 1** | `total = 0` | $c_1$ | $1$ | $c_1$ |
| **Line 2** | `for i in range(n)` | $c_2$ | $n + 1$ *(extra check to stop)* | $c_2(n + 1)$ |
| **Line 3** | `total += A[i]` | $c_3$ | $n$ | $c_3 n$ |
| **Line 4** | `return total` | $c_4$ | $1$ | $c_4$ |

Adding up the total cost:
$$T(n) = c_1 + c_2(n+1) + c_3 n + c_4 = (c_2 + c_3)n + (c_1 + c_2 + c_4) = a \cdot n + b$$

Since $a \cdot n + b$ grows linearly with $n$, the time complexity is **linear**, written as $O(n)$ or $\Theta(n)$.

---

### 2.2 Best, Worst, and Average Case Complexities

An algorithm's running time doesn't just depend on the size of the input $n$, but also on **how the input data is arranged**.

```
                         Input Data of Size n
                                  |
      +---------------------------+---------------------------+
      |                           |                           |
      v                           v                           v
  Best Case                   Average Case               Worst Case
(Lucky layout)             (Expected layout)         (Unlucky layout)
Min time needed            Average time needed       Max time guaranteed
```

1. **Worst-Case Complexity $T_{\text{worst}}(n)$**:
   - The maximum time the algorithm could possibly take for any input of size $n$.
   - **Why it matters**: It gives a strict **guarantee**. The program will *never* be slower than this limit. This is vital for real-time systems like airplane controls or banking apps.

2. **Best-Case Complexity $T_{\text{best}}(n)$**:
   - The minimum time the algorithm could take for any input of size $n$.
   - **Why it matters**: It represents the luckiest scenario (e.g., searching for a number and finding it on the very first try). It is rarely useful because real life is seldom perfectly lucky.

3. **Average-Case Complexity $T_{\text{avg}}(n)$**:
   - The expected running time averaged over all possible inputs of size $n$.
   - **Why it matters**: It tells us how the algorithm will perform on typical, everyday data.

---

### 2.3 Detailed Example: Linear Search Case Analysis

Let's search for a target value $x$ in an array of $n$ numbers:

```python
def linear_search(A, n, x):
    for i in range(n):
        if A[i] == x:
            return i     # Found! Return index
    return -1            # Not found!
```

- **Best Case**: The value $x$ happens to be at the very first slot ($A[0]$).
  - Loop runs 1 time.
  - $T_{\text{best}}(n) = O(1)$ (Constant time).

- **Worst Case**: The value $x$ is at the very last slot ($A[n-1]$) or is missing completely.
  - Loop runs all $n$ times.
  - $T_{\text{worst}}(n) = O(n)$ (Linear time).

- **Average Case**:
  - Suppose $x$ is present in the array with probability $p = 1$, and is equally likely to be at any index from $0$ to $n-1$.
  - If $x$ is at index $0$, it takes $1$ check.
  - If $x$ is at index $1$, it takes $2$ checks.
  - If $x$ is at index $i$, it takes $i + 1$ checks.

$$\text{Average checks} = \frac{1 + 2 + 3 + \dots + n}{n} = \frac{\frac{n(n+1)}{2}}{n} = \frac{n+1}{2}$$

For large $n$, $\frac{n+1}{2} \approx \frac{n}{2}$, which is still proportional to $n$. Therefore, $T_{\text{avg}}(n) = \Theta(n)$.

---

## 3. Complexity Calculation of Simple Algorithms

### 3.1 Loop Pattern Lookup Table

By looking at how loops are structured, you can quickly spot their time complexity:

| Loop Type | Code Example | Execution Count Formula | Complexity |
| :--- | :--- | :--- | :--- |
| **Simple Linear Loop** | `for i in range(n):` | Iterates $n$ times | $\Theta(n)$ |
| **Stepped Linear Loop** | `for i in range(0, n, 2):` | Iterates $n/2$ times | $\Theta(n)$ |
| **Independent Nested Loops** | `for i in range(n):`<br>&nbsp;&nbsp;`for j in range(m):` | Iterates $n \times m$ times | $\Theta(n \cdot m)$ |
| **Dependent Nested Loops** | `for i in range(1, n+1):`<br>&nbsp;&nbsp;`for j in range(1, i+1):` | $1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$ | $\Theta(n^2)$ |
| **Logarithmic Loop (Multiply)** | `i = 1`<br>`while i < n: i = i * 2` | $i$ takes values $1, 2, 4, 8, \dots, 2^k \ge n$ | $\Theta(\log n)$ |
| **Logarithmic Loop (Divide)** | `i = n`<br>`while i > 1: i = i // 2` | $i$ takes values $n, n/2, n/4, \dots \le 1$ | $\Theta(\log n)$ |
| **Square-Root Loop** | `i = 1`<br>`while i * i <= n: i += 1` | Runs until $i^2 > n \implies i > \sqrt{n}$ | $\Theta(\sqrt{n})$ |

---

### 3.2 Walkthrough Derivations for Common Loops

#### Example 3.2.1: Logarithmic Multiplication Loop
```python
def log_example(n):
    i = 1
    count = 0
    while i < n:
        count += 1
        i = i * 2
```
- At step 0: $i = 1 = 2^0$
- At step 1: $i = 2 = 2^1$
- At step 2: $i = 4 = 2^2$
- At step $k$: $i = 2^k$

The loop stops when $i \ge n \implies 2^k \ge n$.  
Taking $\log_2$ on both sides: $k = \log_2 n$.  
**Time Complexity**: $\Theta(\log n)$.

---

#### Example 3.2.2: Insertion Sort Step-Count Analysis
Insertion Sort works like sorting playing cards in your hand. You take one card at a time and slide it left until it is in the right spot:

```python
def insertion_sort(A, n):
    for j in range(1, n):             # Line 1: Outer loop runs (n-1) times
        key = A[j]                    # Line 2
        i = j - 1                     # Line 3
        while i >= 0 and A[i] > key:  # Line 4: Inner shift loop
            A[i + 1] = A[i]           # Line 5
            i = i - 1                 # Line 6
        A[i + 1] = key                # Line 7
```

- **Best Case (Already Sorted Array)**:
  - The inner `while` loop condition `A[i] > key` fails immediately on the very first check.
  - Inner loop runs $1$ time per outer loop iteration.
  - Total steps $\approx (n-1) \times 1 = \Theta(n)$ (Linear time).

- **Worst Case (Reverse Sorted Array)**:
  - For every card $j$, you must shift it past all $j$ previous cards.
  - Inner loop runs $1 + 2 + 3 + \dots + (n-1) = \frac{n(n-1)}{2}$ times.
  - Total steps $\approx \Theta(n^2)$ (Quadratic time).

---

## 4. Recurrence Equations

### 4.1 What is a Recurrence Equation?
When an algorithm solves a problem by calling itself recursively on smaller pieces (using **Divide-and-Conquer**), we write its running time as a mathematical equation called a **Recurrence Equation**.

A recurrence equation expresses $T(n)$ (the time needed for input size $n$) in terms of $T(\text{smaller size})$ and a base case.

#### General Form:
$$T(n) = \begin{cases}
c & \text{if } n = 1 \text{ (Base case: easy small problem)} \\
a T(n/b) + f(n) & \text{if } n > 1 \text{ (Recursive case)}
\end{cases}$$

- $a$: Number of smaller subproblems generated.
- $n/b$: Size of each subproblem.
- $f(n)$: Extra time spent dividing the problem and combining the results.

---

### 4.2 Standard Recurrences Reference

| Algorithm | How it breaks the problem down | Recurrence Equation | Solution |
| :--- | :--- | :--- | :--- |
| **Factorial / Linear Search** | 1 subproblem of size $n-1$, constant work | $T(n) = T(n-1) + O(1)$ | $\Theta(n)$ |
| **Binary Search** | 1 subproblem of size $n/2$, constant work | $T(n) = T(n/2) + O(1)$ | $\Theta(\log n)$ |
| **Tower of Hanoi** | 2 subproblems of size $n-1$, constant work | $T(n) = 2T(n-1) + O(1)$ | $\Theta(2^n)$ |
| **Merge Sort** | 2 subproblems of size $n/2$, linear combining work | $T(n) = 2T(n/2) + O(n)$ | $\Theta(n \log n)$ |
| **Binary Tree Traversal** | 2 subproblems of size $n/2$, constant root work | $T(n) = 2T(n/2) + O(1)$ | $\Theta(n)$ |

---

## 5. Solution of Recurrences — Iteration Method

The **Iteration Method** (also called the **Unrolling Method**) solves a recurrence by expanding $T(n)$ again and again until a pattern appears, then solving down to the base case.

### 5.1 Simple 4-Step Recipe:
1. **Unroll**: Replace $T(n-1)$ or $T(n/2)$ using the formula 2 or 3 times.
2. **Find Pattern**: Write the equation after $k$ unrolling steps.
3. **Set Base Case**: Find the value of $k$ where the input reaches the base case (e.g. $n - k = 1$ or $n/2^k = 1$).
4. **Substitute & Simplify**: Plug $k$ back in and solve the basic algebra.

---

### 5.2 Solved Step-by-Step Examples

#### Example 5.2.1: Solve $T(n) = T(n-1) + c$ with $T(1) = 1$

- **Step 1: Unroll**
  - Start: $T(n) = T(n-1) + c$
  - Since $T(n-1) = T(n-2) + c$, substitute it in:  
    $T(n) = [T(n-2) + c] + c = T(n-2) + 2c$
  - Substitute $T(n-2) = T(n-3) + c$:  
    $T(n) = [T(n-3) + c] + 2c = T(n-3) + 3c$

- **Step 2: Pattern after $k$ steps**
  $$T(n) = T(n-k) + k \cdot c$$

- **Step 3: Base Case**
  We know $T(1) = 1$. Set subproblem size $n - k = 1 \implies k = n - 1$.

- **Step 4: Substitute $k$ back**
  $$T(n) = T(1) + (n-1)c = 1 + c n - c = \Theta(n)$$

---

#### Example 5.2.2: Solve $T(n) = T(n/2) + c$ with $T(1) = 1$ (Binary Search)

- **Step 1: Unroll**
  - Start: $T(n) = T(n/2) + c$
  - Substitute $T(n/2) = T(n/4) + c$:  
    $T(n) = [T(n/4) + c] + c = T(n/2^2) + 2c$
  - Substitute $T(n/4) = T(n/8) + c$:  
    $T(n) = [T(n/8) + c] + 2c = T(n/2^3) + 3c$

- **Step 2: Pattern after $k$ steps**
  $$T(n) = T\left(\frac{n}{2^k}\right) + k \cdot c$$

- **Step 3: Base Case**
  Set $\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$.

- **Step 4: Substitute $k$ back**
  $$T(n) = T(1) + (\log_2 n) \cdot c = 1 + c \log_2 n = \Theta(\log n)$$

---

#### Example 5.2.3: Solve $T(n) = 2T(n/2) + cn$ with $T(1) = c$ (Merge Sort)

- **Step 1: Unroll**
  - Start: $T(n) = 2T(n/2) + cn$
  - Substitute $T(n/2) = 2T(n/4) + c(n/2)$:  
    $T(n) = 2[2T(n/4) + c(n/2)] + cn = 4T(n/4) + cn + cn = 2^2 T(n/2^2) + 2cn$
  - Substitute $T(n/4) = 2T(n/8) + c(n/4)$:  
    $T(n) = 4[2T(n/8) + c(n/4)] + 2cn = 8T(n/8) + cn + 2cn = 2^3 T(n/2^3) + 3cn$

- **Step 2: Pattern after $k$ steps**
  $$T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot cn$$

- **Step 3: Base Case**
  Set $\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$.

- **Step 4: Substitute $k$ back**
  $$T(n) = n \cdot T(1) + (\log_2 n) \cdot cn = n \cdot c + cn \log_2 n = \Theta(n \log n)$$

---

## 6. Solution of Recurrences — Recursion Tree Method

The **Recursion Tree Method** visualizes recursive calls as a tree structure. Each node in the tree shows the work done at that single step.

### 6.1 Understanding the Tree Layout

For a recurrence like $T(n) = 2T(n/2) + cn$:

```
 Level 0 (Root):               cn                     ---> Level Cost: cn
                             /    \
 Level 1:              c(n/2)      c(n/2)             ---> Level Cost: 2 * c(n/2) = cn
                       /    \      /    \
 Level 2:        c(n/4)  c(n/4)  c(n/4)  c(n/4)       ---> Level Cost: 4 * c(n/4) = cn
                    :       :       :       :
 Level h (Leaves):   T(1)    T(1)    T(1) ...  T(1)       ---> Level Cost: n * T(1) = cn
```

- **Tree Height ($h$)**: The problem size shrinks from $n \to n/2 \to n/4 \dots \to 1$.  
  Height $h = \log_2 n$.
- **Number of Levels**: $h + 1 = \log_2 n + 1$.
- **Cost at Level $i$**: $2^i \times c(n/2^i) = cn$.
- **Total Tree Cost**: Add up the costs of all levels:
  $$\text{Total Time } T(n) = \sum_{i=0}^{\log_2 n} cn = cn \times (\text{number of levels}) = cn(\log_2 n + 1) = \Theta(n \log n)$$

---

### 6.2 The Golden Rule of Recursion Trees

When you add up work across the levels of a recursion tree, look at how the level costs behave:

1. **Equal Level Costs** (like Merge Sort: $cn, cn, cn\dots$):  
   $$\text{Total Time} = \text{(Cost per level)} \times \text{(Tree Height)} = \Theta(f(n) \cdot \log n)$$
2. **Decreasing Level Costs** (work gets much smaller at lower levels, e.g. $cn^2, \frac{1}{2}cn^2, \frac{1}{4}cn^2 \dots$):  
   The **root node dominates**.  
   $$\text{Total Time} = \Theta(\text{Root Cost})$$
3. **Increasing Level Costs** (work grows rapidly at lower levels):  
   The **bottom leaves dominate**.  
   $$\text{Total Time} = \Theta(\text{Number of Leaves})$$

---

## 7. Real-World Engineering Trade-offs & CS Architecture Insights

### 7.1 Array Locality vs. Linked List Memory Traversal
Why do algorithms operating on contiguous arrays run faster in real life than those operating on linked lists or binary trees, even if both have the same theoretical Big-O complexity?

```
CPU Cache Line (64 Bytes)
+---------------------------------------------------+
| A[0] | A[1] | A[2] | A[3] | A[4] | A[5] | A[6] |  ---> Array (Sequential Memory)
+---------------------------------------------------+
```

- **CPU Cache Hits (Array)**: Modern computer CPUs load data from RAM in 64-byte chunks into high-speed **L1/L2 Cache**. Reading `A[0]` automatically fetches `A[1]` through `A[7]` into the cache. This makes array loops lightning fast.
- **CPU Cache Misses (Linked List / Pointer Chasing)**: Linked list nodes and tree nodes are scattered randomly across RAM. Moving to `node.next` requires jumping to a new RAM address, causing a **cache miss** and slowing down execution.

---

### 7.2 Call Stack Memory Overhead in Recursion
Recursive algorithms (like recursive Binary Search or Merge Sort) consume hidden memory on the **System Call Stack**:
- Every time a function calls itself, a new **Stack Frame** (holding function arguments, local variables, and return addresses) is pushed onto the stack.
- Recursion of depth $d$ requires $O(d)$ auxiliary stack memory.
- If recursion goes too deep (e.g., $n = 100,000$ in linear recursion), the program will crash with a **StackOverflowError**.

---

## 8. Summary Reference Tables

### 8.1 Comparison of Asymptotic Cases

| Case | Definition | Math Representation | Practical Usage |
| :--- | :--- | :--- | :--- |
| **Worst-Case** | Maximum time over all inputs of size $n$ | $T_{\text{worst}}(n) = \max T(I)$ | Guaranteed safety limit (Critical systems) |
| **Best-Case** | Minimum time over all inputs of size $n$ | $T_{\text{best}}(n) = \min T(I)$ | Rarely useful (Optimistic scenario) |
| **Average-Case** | Expected time averaged over all inputs | $T_{\text{avg}}(n) = E[T(I)]$ | Predicts real-world typical performance |

---

### 8.2 Standard Recurrence Solutions Summary

| Recurrence Equation | Method | Final Solution | Example Algorithm |
| :--- | :--- | :--- | :--- |
| $T(n) = T(n-1) + 1$ | Iteration | $\Theta(n)$ | Simple Counting Loop / Factorial |
| $T(n) = T(n-1) + n$ | Iteration | $\Theta(n^2)$ | Recursive Selection Sort |
| $T(n) = 2T(n-1) + 1$ | Iteration | $\Theta(2^n)$ | Tower of Hanoi |
| $T(n) = T(n/2) + 1$ | Iteration / Tree | $\Theta(\log n)$ | Binary Search |
| $T(n) = 2T(n/2) + n$ | Iteration / Tree | $\Theta(n \log n)$ | Merge Sort |
| $T(n) = 2T(n/2) + 1$ | Iteration / Tree | $\Theta(n)$ | Full Binary Tree Traversal |

---

## 9. KTU Exam Practice Problems & Solved Numericals

### Problem 1: Step-Count Calculation for Nested Loops
**Question**: Find the exact step count and asymptotic time complexity of the following code:
```c
int count = 0;
for (int i = 1; i <= n; i = i * 2) {
    for (int j = 1; j <= i; j++) {
        count++;
    }
}
```

**Solution**:
1. Look at the outer loop variable $i$: it doubles each time ($i = 1, 2, 4, 8, \dots, 2^k \le n$).
2. For a given value of $i$, the inner loop runs exactly $i$ times.
3. Total execution count is the sum of inner loop runs for all values of $i$:
   $$\text{Total } T(n) = 1 + 2 + 4 + 8 + \dots + 2^{\lfloor \log_2 n \rfloor}$$
4. This is a Geometric Progression with first term $a = 1$ and common ratio $r = 2$:
   $$T(n) = \frac{1 \cdot (2^{\log_2 n + 1} - 1)}{2 - 1} = 2 \cdot 2^{\log_2 n} - 1 = 2n - 1$$
5. **Answer**: Exact count $= 2n - 1$, Time Complexity $= \Theta(n)$.

---

### Problem 2: Solving Recurrence using Iteration Method
**Question**: Solve the recurrence $T(n) = T(n-1) + n^2$ given base case $T(1) = 1$.

**Solution**:
1. **Unroll once**: $T(n) = T(n-1) + n^2$
2. **Unroll twice**: Substitute $T(n-1) = T(n-2) + (n-1)^2$:  
   $T(n) = T(n-2) + (n-1)^2 + n^2$
3. **General pattern after $k$ steps**:  
   $$T(n) = T(n-k) + \sum_{j=0}^{k-1} (n-j)^2$$
4. **Apply Base Case**: Set $n - k = 1 \implies k = n - 1$.
5. **Evaluate Summation**:
   $$T(n) = T(1) + 2^2 + 3^2 + \dots + n^2 = \sum_{i=1}^{n} i^2$$
6. Using the standard formula for sum of squares $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$:
   $$T(n) = \frac{2n^3 + 3n^2 + n}{6} = \Theta(n^3)$$
7. **Answer**: $T(n) = \Theta(n^3)$.

---

### Problem 3: Solving Recurrence using Recursion Tree Method
**Question**: Solve $T(n) = 2T(n/2) + n^2$ using the Recursion Tree Method.

**Solution**:
1. **Root Cost (Level 0)**: $n^2$.
2. **Level 1**: 2 nodes of size $n/2$.  
   Cost $= 2 \times (n/2)^2 = 2 \times \frac{n^2}{4} = \frac{n^2}{2}$.
3. **Level 2**: 4 nodes of size $n/4$.  
   Cost $= 4 \times (n/4)^2 = 4 \times \frac{n^2}{16} = \frac{n^2}{4}$.
4. **General Level $i$ Cost**: $\frac{n^2}{2^i} = n^2 \left(\frac{1}{2}\right)^i$.
5. **Summing all level costs**:
   $$T(n) = \sum_{i=0}^{\log_2 n - 1} n^2 \left(\frac{1}{2}\right)^i = n^2 \sum_{i=0}^{\log_2 n - 1} \left(\frac{1}{2}\right)^i$$
6. Since $\frac{1}{2} < 1$, this is a geometrically decreasing series whose sum is bounded by $\frac{1}{1 - 1/2} = 2$.
7. **Answer**: $T(n) \le 2n^2 \implies \Theta(n^2)$. (Root cost dominates!).
