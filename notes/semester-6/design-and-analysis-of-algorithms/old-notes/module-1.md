# Module 1: Introduction to Algorithm Analysis & Recurrences

---

## 1. Foundations of Algorithm Analysis & Computation Models

### 1.1 What is an Algorithm?
An **algorithm** is a well-defined, finite sequence of unambiguous computational steps that transforms a given input into a desired output.

Formally, an algorithm must satisfy five core criteria:
1. **Input**: Zero or more quantities supplied externally.
2. **Output**: At least one quantity produced as a result.
3. **Definiteness**: Each instruction must be clear, precise, and unambiguous.
4. **Finiteness**: For all valid inputs, the algorithm must terminate after a finite number of steps.
5. **Effectiveness**: Every operation must be basic enough to be carried out, in principle, by a person using paper and pencil in finite time.

---

### 1.2 The Computation Model: Random Access Machine (RAM)
To analyze algorithms independently of specific hardware, operating systems, or programming languages, we adopt an abstract model of computation: the **Random Access Machine (RAM)** model.

#### Key Assumptions of the RAM Model:
- **Instructions are executed sequentially**: One instruction runs at a time (no parallelism).
- **Basic operations take $O(1)$ time** (Uniform Cost Criteria):
  - Arithmetic operations: Addition, subtraction, multiplication, division, modulo.
  - Logical operations: AND, OR, NOT, bitwise shifts.
  - Memory operations: Variable assignment, pointer dereferencing, array indexing.
  - Control operations: Conditional branching (`if/else`), function call/return overhead.
- **Memory is infinite and uniformly accessible**: Accessing any memory location $A[i]$ takes equal time regardless of $i$.

> [!NOTE]
> **Engineering Reality Check (Uniform Cost vs. Logarithmic Cost)**:
> In theoretical analysis (Uniform Cost Model), adding two 64-bit integers takes 1 unit of time ($O(1)$). However, in cryptography or big-number arithmetic with numbers of bit-length $b$, arithmetic operations scale with the bit-length (Logarithmic Cost Model), where addition takes $O(b)$ time and multiplication takes $O(b^2)$ or $O(b \log b)$ time.

---

### 1.3 Time Complexity and Space Complexity

#### Time Complexity
**Time Complexity** $T(n)$ measures how the execution time of an algorithm grows as a function of the input size $n$. It is determined by counting the total number of **elementary operations** executed.

#### Space Complexity
**Space Complexity** $S(n)$ measures the total amount of memory required by an algorithm to run to completion as a function of input size $n$.

Space complexity consists of two components:
$$S(n) = \text{Fixed Space} + \text{Variable / Auxiliary Space}$$

1. **Fixed Space (Instruction Space & Fixed Data)**: Memory needed for the code instructions, simple variables, fixed-size constants, and data independent of input size $n$.
2. **Auxiliary Space**: Dynamic memory allocated during execution (e.g., dynamically allocated arrays, hash tables, and call stack frames generated during recursive execution).

```
+-------------------------------------------------------------+
|                      Total Memory S(n)                      |
+------------------------------------+------------------------+
|             Fixed Space            |    Auxiliary Space     |
| (Code, Constants, Simple Variables)| (Arrays, Dynamic Heap, |
|                                    | Recursion Call Stack)  |
+------------------------------------+------------------------+
```

---

### 1.4 Frequency Count Method (Step-Count Analysis)
The **Frequency Count Method** determines time complexity by assigning a cost ($c_i$) to each statement and calculating its **execution frequency** ($f_i$) in terms of input size $n$. The total runtime is:

$$T(n) = \sum c_i \cdot f_i$$

#### Example 1: Sum of an Array
Consider the algorithm to compute the sum of $n$ elements:

```python
def compute_sum(A, n):
    total = 0            # Line 1
    for i in range(n):   # Line 2
        total += A[i]    # Line 3
    return total         # Line 4
```

| Line | Statement | Cost ($c_i$) | Frequency ($f_i$) | Total Cost |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `total = 0` | $c_1$ | $1$ | $c_1$ |
| 2 | `for i in range(n)` | $c_2$ | $n + 1$ *(includes final failing test)* | $c_2(n + 1)$ |
| 3 | `total += A[i]` | $c_3$ | $n$ | $c_3 n$ |
| 4 | `return total` | $c_4$ | $1$ | $c_4$ |

$$\begin{aligned}
T(n) &= c_1(1) + c_2(n+1) + c_3(n) + c_4(1) \\
&= (c_2 + c_3)n + (c_1 + c_2 + c_4) \\
&= a \cdot n + b \quad \implies \Theta(n)
\end{aligned}$$

---

## 2. Complexity Frameworks: Best, Worst, and Average Cases

The runtime of an algorithm depends not only on the input size $n$, but also on the specific **structure/instance** of the input data.

Let $\mathcal{I}_n$ denote the set of all valid inputs of size $n$, and $T(I)$ be the running time on input instance $I \in \mathcal{I}_n$.

```
           Input Space of Size n (I_n)
  +-------------------------------------------+
  |  Best Case I_best  ---> Min T(I)          |
  |  Average Case      ---> E[T(I)]           |
  |  Worst Case I_worst ---> Max T(I)         |
  +-------------------------------------------+
```

---

### 2.1 Definitions and Mathematical Formulations

#### 1. Worst-Case Complexity $T_{\text{worst}}(n)$
The maximum running time over all possible inputs of size $n$:
$$T_{\text{worst}}(n) = \max_{I \in \mathcal{I}_n} T(I)$$

- **Why it matters**: It provides an **absolute upper bound guarantee**. An algorithm will never take longer than $T_{\text{worst}}(n)$. This is essential for mission-critical, real-time systems (e.g., flight control, medical devices, databases).

#### 2. Best-Case Complexity $T_{\text{best}}(n)$
The minimum running time over all possible inputs of size $n$:
$$T_{\text{best}}(n) = \min_{I \in \mathcal{I}_n} T(I)$$

- **Why it matters**: Rarely useful in practice because it represents an overly optimistic scenario (e.g., sorting an already sorted array). It can be misleading when choosing algorithms.

#### 3. Average-Case Complexity $T_{\text{avg}}(n)$
The expected running time over a probability distribution $P(I)$ of inputs of size $n$:
$$T_{\text{avg}}(n) = E[T(I)] = \sum_{I \in \mathcal{I}_n} P(I) \cdot T(I)$$

If all inputs of size $n$ are equally likely (uniform distribution, $P(I) = \frac{1}{|\mathcal{I}_n|}$):
$$T_{\text{avg}}(n) = \frac{1}{|\mathcal{I}_n|} \sum_{I \in \mathcal{I}_n} T(I)$$

---

### 2.2 Detailed Comparative Analysis: Linear Search

Algorithm: Search for key $x$ in array $A[0 \dots n-1]$.

```python
def linear_search(A, n, x):
    for i in range(n):
        if A[i] == x:
            return i     # Found at index i
    return -1            # Not found
```

#### Analytical Breakdown:
- **Best Case**: $x$ is found at index $0$.
  - Number of comparisons = $1$.
  - $T_{\text{best}}(n) = O(1)$.

- **Worst Case**: $x$ is at index $n-1$ or not present in $A$.
  - Number of comparisons = $n$.
  - $T_{\text{worst}}(n) = O(n)$.

- **Average Case Analysis**:
  - Assume $x$ is present in $A$ with probability $p$, and equally likely to be at any index $0 \dots n-1$ with probability $\frac{p}{n}$.
  - Probability that $x$ is not present = $1 - p$.
  - If $x$ is at index $i$, the loop performs $i+1$ comparisons.
  - If $x$ is not present, the loop performs $n$ comparisons.

$$\begin{aligned}
T_{\text{avg}}(n) &= \left( \sum_{i=0}^{n-1} \frac{p}{n} \cdot (i+1) \right) + (1-p) \cdot n \\
&= \frac{p}{n} \sum_{k=1}^{n} k + (1-p)n \\
&= \frac{p}{n} \cdot \frac{n(n+1)}{2} + (1-p)n \\
&= \frac{p(n+1)}{2} + (1-p)n
\end{aligned}$$

- **Case A**: If $x$ is guaranteed to be in $A$ ($p = 1$):
  $$T_{\text{avg}}(n) = \frac{n+1}{2} = \Theta(n)$$
- **Case B**: If $p = 0.5$ (50% chance key is present):
  $$T_{\text{avg}}(n) = \frac{n+1}{4} + \frac{n}{2} = \frac{3n + 1}{4} = \Theta(n)$$

---

## 3. Complexity Calculation of Simple Algorithms

### 3.1 Loop Pattern Analysis Reference Table

| Loop Pattern | Code Example | Step Count Formula | Asymptotic Complexity |
| :--- | :--- | :--- | :--- |
| **Linear Loop** | `for i in range(1, n+1, c)` | $\sum_{i=1}^{n/c} 1 = \frac{n}{c}$ | $\Theta(n)$ |
| **Nested Loop (Independent)** | `for i in range(n): for j in range(m):` | $\sum_{i=1}^n \sum_{j=1}^m 1 = n \cdot m$ | $\Theta(n \cdot m)$ |
| **Dependent Nested Loop** | `for i in range(1, n+1): for j in range(1, i+1):` | $\sum_{i=1}^n i = \frac{n(n+1)}{2}$ | $\Theta(n^2)$ |
| **Logarithmic Loop (Multiply)** | `i = 1; while i < n: i = i * 2` | $\log_2 n$ iterations | $\Theta(\log n)$ |
| **Logarithmic Loop (Divide)** | `i = n; while i > 1: i = i // 2` | $\log_2 n$ iterations | $\Theta(\log n)$ |
| **Square Root Loop** | `i = 1; while i * i <= n: i += 1` | $\sqrt{n}$ iterations | $\Theta(\sqrt{n})$ |

---

### 3.2 Walkthrough Derivations

#### Example 3.2.1: Dependent Nested Loop
```python
def dependent_loop(n):
    k = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            k += 1
```

**Step-Count Summation**:
$$T(n) = \sum_{i=1}^{n} \sum_{j=1}^{i} 1 = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \frac{n^2}{2} + \frac{n}{2} = \Theta(n^2)$$

---

#### Example 3.2.2: Logarithmic Loop with Variable Increments
```python
def log_loop(n):
    i = 1
    count = 0
    while i < n:
        count += 1
        i = i * 2
    return count
```

**Derivation**:
Let $k$ be the total number of iterations.
- At iteration $0$: $i = 1 = 2^0$
- At iteration $1$: $i = 2^1$
- At iteration $2$: $i = 2^2$
- At iteration $k$: $i = 2^k$

The loop terminates when $i \ge n \implies 2^k \ge n$.
Taking $\log_2$ on both sides:
$$k = \lceil \log_2 n \rceil \implies T(n) = \Theta(\log n)$$

---

#### Example 3.2.3: Square-Root Loop
```python
def primality_check(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
```

**Derivation**:
The loop body executes while $i^2 \le n \implies i \le \sqrt{n}$.
Since $i$ increments by $1$ in each step starting from $2$, the total iterations are $\lfloor \sqrt{n} \rfloor - 1$.
$$T(n) = \Theta(\sqrt{n})$$

---

#### Example 3.2.4: Insertion Sort Analysis

```python
def insertion_sort(A, n):
    for j in range(1, n):             # Line 1: Key loop (n-1 times)
        key = A[j]                    # Line 2
        i = j - 1                     # Line 3
        while i >= 0 and A[i] > key:  # Line 4: Inner shifting loop
            A[i + 1] = A[i]           # Line 5
            i = i - 1                 # Line 6
        A[i + 1] = key                # Line 7
```

Let $t_j$ be the number of times the `while` loop test (Line 4) is executed for a given value of $j$.

Total running time equation:
$$T(n) = c_1 n + c_2 (n-1) + c_3 (n-1) + c_4 \sum_{j=1}^{n-1} t_j + c_5 \sum_{j=1}^{n-1} (t_j - 1) + c_6 \sum_{j=1}^{n-1} (t_j - 1) + c_7 (n-1)$$

- **Worst-Case Analysis** (Array is sorted in reverse order):
  For each $j$, $A[i] > key$ is true for all $i$ from $j-1$ down to $0$. Thus $t_j = j + 1$.
  $$\sum_{j=1}^{n-1} t_j = \sum_{j=1}^{n-1} (j+1) = \frac{n(n+1)}{2} - 1 = \Theta(n^2)$$
  $$\sum_{j=1}^{n-1} (t_j - 1) = \sum_{j=1}^{n-1} j = \frac{n(n-1)}{2} = \Theta(n^2)$$
  Substituting back: $T_{\text{worst}}(n) = a n^2 + b n + c = \Theta(n^2)$.

- **Best-Case Analysis** (Array is already sorted):
  For each $j$, $A[j-1] \le key$ immediately on the first check. Thus $t_j = 1$.
  $$\sum_{j=1}^{n-1} t_j = n - 1, \quad \sum_{j=1}^{n-1} (t_j - 1) = 0$$
  Substituting back: $T_{\text{best}}(n) = k_1 n + k_2 = \Theta(n)$.

---

## 4. Recurrence Equations

### 4.1 What is a Recurrence Relation?
A **recurrence relation** is an equation or inequality that defines a function $T(n)$ in terms of its value on **smaller inputs** (e.g., $T(n/2)$ or $T(n-1)$), along with one or more **base cases**.

Recurrences naturally model the time complexity of **recursive algorithms**, especially those using the **Divide-and-Conquer** strategy.

---

### 4.2 Formulating Recurrences from Recursive Code

#### General Divide-and-Conquer Recurrence:
$$T(n) = \begin{cases} 
\Theta(1) & \text{if } n \le n_0 \\
a T(n/b) + D(n) + C(n) & \text{if } n > n_0 
\end{cases}$$

Where:
- $a \ge 1$: Number of subproblems generated at each step.
- $n/b$: Size of each subproblem ($b > 1$).
- $D(n)$: Time taken to **Divide** the problem into subproblems.
- $C(n)$: Time taken to **Combine** the solutions of the subproblems.

---

### 4.3 Standard Recurrences Reference

| Algorithm | Recursive Structure | Formulated Recurrence | Solution |
| :--- | :--- | :--- | :--- |
| **Factorial / Recursive Linear Search** | 1 subproblem of size $n-1$, $O(1)$ work | $T(n) = T(n-1) + \Theta(1)$ | $\Theta(n)$ |
| **Recursive Sum of Array** | 1 subproblem of size $n-1$, $O(1)$ work | $T(n) = T(n-1) + \Theta(1)$ | $\Theta(n)$ |
| **Tower of Hanoi** | 2 subproblems of size $n-1$, $O(1)$ work | $T(n) = 2T(n-1) + \Theta(1)$ | $\Theta(2^n)$ |
| **Binary Search** | 1 subproblem of size $n/2$, $O(1)$ work | $T(n) = T(n/2) + \Theta(1)$ | $\Theta(\log n)$ |
| **Merge Sort** | 2 subproblems of size $n/2$, $O(n)$ work | $T(n) = 2T(n/2) + \Theta(n)$ | $\Theta(n \log n)$ |
| **Binary Tree Traversal** | 2 subproblems of size $n/2$, $O(1)$ work | $T(n) = 2T(n/2) + \Theta(1)$ | $\Theta(n)$ |

---

## 5. Solution of Recurrence Equations — Iteration Method

The **Iteration Method** (also known as the **Substitution Method** or **Unrolling Method**) solves a recurrence by repeatedly substituting the recurrence equation into itself until a clear algebraic pattern emerges as a function of the iteration step $k$. We then set $k$ such that the subproblem size reduces to the base case.

### 5.1 General Steps for the Iteration Method:
1. **Unroll** the recurrence for $k = 1, 2, 3, \dots$ steps.
2. **Express** $T(n)$ as a general formula in terms of $k$.
3. **Determine** the value of $k$ at which the base case $T(1)$ or $T(0)$ is reached.
4. **Substitute** $k$ back into the general formula and simplify the algebraic summation.

---

### 5.2 Solved Worked Examples

#### Example 5.2.1: $T(n) = T(n-1) + c$ with $T(1) = 1$

**Step 1: Unroll the equation**
$$T(n) = T(n-1) + c \quad \text{--- (Equation 1)}$$

Substitute $T(n-1) = T(n-2) + c$:
$$T(n) = [T(n-2) + c] + c = T(n-2) + 2c \quad \text{--- (Equation 2)}$$

Substitute $T(n-2) = T(n-3) + c$:
$$T(n) = [T(n-3) + c] + 2c = T(n-3) + 3c \quad \text{--- (Equation 3)}$$

**Step 2: Express in terms of step $k$**
$$T(n) = T(n-k) + k \cdot c$$

**Step 3: Apply Base Case**
The base case is $T(1)$. Set $n - k = 1 \implies k = n - 1$.

**Step 4: Substitute $k$ back into the formula**
$$\begin{aligned}
T(n) &= T(1) + (n-1)c \\
&= 1 + c \cdot n - c \\
&= c \cdot n + (1 - c) = \Theta(n)
\end{aligned}$$

---

#### Example 5.2.2: $T(n) = T(n-1) + n$ with $T(1) = 1$

**Step 1: Unroll the equation**
$$T(n) = T(n-1) + n$$

Substitute $T(n-1) = T(n-2) + (n-1)$:
$$T(n) = [T(n-2) + (n-1)] + n = T(n-2) + (n-1) + n$$

Substitute $T(n-2) = T(n-3) + (n-2)$:
$$T(n) = T(n-3) + (n-2) + (n-1) + n$$

**Step 2: Express in terms of step $k$**
$$T(n) = T(n-k) + \sum_{j=0}^{k-1} (n - j)$$

**Step 3: Apply Base Case**
Set $n - k = 1 \implies k = n - 1$.

**Step 4: Evaluate Summation**
$$\begin{aligned}
T(n) &= T(1) + 2 + 3 + \dots + (n-1) + n \\
&= 1 + 2 + 3 + \dots + n \\
&= \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \Theta(n^2)
\end{aligned}$$

---

#### Example 5.2.3: $T(n) = 2T(n-1) + 1$ with $T(0) = 1$ (Tower of Hanoi)

**Step 1: Unroll the equation**
$$T(n) = 2T(n-1) + 1$$
$$T(n) = 2[2T(n-2) + 1] + 1 = 2^2 T(n-2) + 2 + 1$$
$$T(n) = 2^2[2T(n-3) + 1] + 2 + 1 = 2^3 T(n-3) + 2^2 + 2^1 + 2^0$$

**Step 2: General formula for step $k$**
$$T(n) = 2^k T(n-k) + \sum_{j=0}^{k-1} 2^j$$

**Step 3: Apply Base Case**
Set $n - k = 0 \implies k = n$.

**Step 4: Substitute and evaluate Geometric Series**
$$\begin{aligned}
T(n) &= 2^n T(0) + \sum_{j=0}^{n-1} 2^j \\
&= 2^n(1) + (2^n - 1) \quad \left[\text{since } \sum_{j=0}^{n-1} 2^j = \frac{2^n - 1}{2-1}\right] \\
&= 2 \cdot 2^n - 1 = 2^{n+1} - 1 = \Theta(2^n)
\end{aligned}$$

---

#### Example 5.2.4: $T(n) = T(n/2) + c$ with $T(1) = 1$ (Binary Search)

**Step 1: Unroll the equation**
$$T(n) = T(n/2) + c$$
$$T(n) = [T(n/4) + c] + c = T(n/2^2) + 2c$$
$$T(n) = [T(n/8) + c] + 2c = T(n/2^3) + 3c$$

**Step 2: General formula for step $k$**
$$T(n) = T\left(\frac{n}{2^k}\right) + k \cdot c$$

**Step 3: Apply Base Case**
Set $\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$.

**Step 4: Substitute $k$ back**
$$\begin{aligned}
T(n) &= T(1) + (\log_2 n) \cdot c \\
&= 1 + c \log_2 n = \Theta(\log n)
\end{aligned}$$

---

#### Example 5.2.5: $T(n) = 2T(n/2) + cn$ with $T(1) = c$ (Merge Sort)

**Step 1: Unroll the equation**
$$T(n) = 2T(n/2) + cn$$
$$T(n) = 2\left[2T\left(\frac{n}{4}\right) + c\left(\frac{n}{2}\right)\right] + cn = 2^2 T\left(\frac{n}{2^2}\right) + cn + cn = 2^2 T\left(\frac{n}{2^2}\right) + 2cn$$
$$T(n) = 2^2\left[2T\left(\frac{n}{8}\right) + c\left(\frac{n}{4}\right)\right] + 2cn = 2^3 T\left(\frac{n}{2^3}\right) + 3cn$$

**Step 2: General formula for step $k$**
$$T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot cn$$

**Step 3: Apply Base Case**
Set $\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$.

**Step 4: Substitute $k$ back**
$$\begin{aligned}
T(n) &= n \cdot T(1) + (\log_2 n) \cdot cn \\
&= n \cdot c + c n \log_2 n \\
&= c n \log_2 n + c n = \Theta(n \log n)
\end{aligned}$$

---

## 6. Solution of Recurrence Equations — Recursion Tree Method

The **Recursion Tree Method** visualizes recursive calls as a tree structure. Each node represents the cost of a single subproblem. We compute the total runtime by:
1. Calculating the cost of work done at each node.
2. Summing costs across each level of the tree.
3. Summing level costs over all levels from root to leaves.

---

### 6.1 Structure of a Recursion Tree

For a recurrence $T(n) = a T(n/b) + f(n)$:

```
 Level 0 (Root)               f(n)                      ---> Cost: f(n)
                             /  |  \
                            /   |   \  (a branches)
 Level 1               f(n/b) f(n/b) f(n/b)             ---> Cost: a * f(n/b)
                        /   \
                       /     \
 Level 2           f(n/b²)  f(n/b²) ...                 ---> Cost: a² * f(n/b²)
   :                  :        :
 Level h (Leaves)    T(1)     T(1) ... T(1)             ---> Cost: Number of leaves * T(1)
```

#### Key Properties of the Recursion Tree:
1. **Root Cost** (Level 0): $f(n)$
2. **Subproblem Size at Level $i$**: $\frac{n}{b^i}$
3. **Number of Nodes at Level $i$**: $a^i$
4. **Cost per Level $i$**: $a^i \cdot f\left(\frac{n}{b^i}\right)$
5. **Tree Height $h$**: Reached when subproblem size is $1$:
   $$\frac{n}{b^h} = 1 \implies b^h = n \implies h = \log_b n$$
6. **Total Number of Leaves**:
   $$\text{Leaves} = a^h = a^{\log_b n} = n^{\log_b a}$$
7. **Total Cost Equation**:
   $$T(n) = \sum_{i=0}^{h-1} a^i f\left(\frac{n}{b^i}\right) + \Theta(n^{\log_b a})$$

---

### 6.2 Solved Worked Examples

#### Example 6.2.1: $T(n) = 2T(n/2) + cn$ (Merge Sort Tree)

```
 Level 0:                      cn                      ---> Cost: cn
                             /    \
 Level 1:              c(n/2)      c(n/2)              ---> Cost: 2 * c(n/2) = cn
                      /     \      /     \
 Level 2:        c(n/4)  c(n/4)  c(n/4)  c(n/4)        ---> Cost: 4 * c(n/4) = cn
                    :       :       :       :
 Level h:        T(1)    T(1)    T(1) ...  T(1)        ---> Cost: n * T(1) = cn
```

- **Height of Tree $h$**: $\frac{n}{2^h} = 1 \implies h = \log_2 n$.
- **Number of levels**: $h + 1 = \log_2 n + 1$.
- **Cost per level**: $cn$ for every level $i \in [0, h]$.
- **Total Cost**:
  $$T(n) = \sum_{i=0}^{\log_2 n} cn = cn \cdot (\log_2 n + 1) = cn \log_2 n + cn = \Theta(n \log n)$$

---

#### Example 6.2.2: Asymmetric Recurrence Tree: $T(n) = T(n/3) + T(2n/3) + cn$

This recurrence models algorithms like **QuickSort** with an unbalanced split ($1/3 : 2/3$).

```
 Level 0:                      cn                             ---> Cost: cn
                             /    \
 Level 1:              c(n/3)      c(2n/3)                    ---> Cost: cn/3 + 2cn/3 = cn
                      /     \      /      \
 Level 2:        c(n/9) c(2n/9) c(2n/9)  c(4n/9)             ---> Cost: cn
```

- **Shortest Path to a Leaf** (Leftmost branch):
  $$n \to \frac{n}{3} \to \frac{n}{9} \to \dots \to 1 \implies \frac{n}{3^{h_{\min}}} = 1 \implies h_{\min} = \log_3 n$$
- **Longest Path to a Leaf** (Rightmost branch):
  $$n \to \frac{2n}{3} \to \left(\frac{2}{3}\right)^2 n \to \dots \to 1 \implies \left(\frac{2}{3}\right)^{h_{\max}} n = 1 \implies h_{\max} = \log_{3/2} n$$

- **Cost Analysis**:
  - For levels up to $h_{\min} = \log_3 n$, every level has a total cost of **exactly $cn$**.
  - Beyond $h_{\min}$ up to $h_{\max}$, levels have partial nodes, so the level cost is **$\le cn$**.
- **Upper Bound**:
  $$T(n) \le \sum_{i=0}^{\log_{3/2} n} cn = cn \cdot \log_{3/2} n = \Theta(n \log n)$$
- **Lower Bound**:
  $$T(n) \ge \sum_{i=0}^{\log_{3} n} cn = cn \cdot \log_3 n = \Theta(n \log n)$$

**Conclusion**: $T(n) = \Theta(n \log n)$.

---

#### Example 6.2.3: Geometrically Decreasing Tree: $T(n) = 3T(n/4) + cn^2$

```
 Level 0:                      cn²                            ---> Cost: cn²
                             /  |  \
 Level 1:            c(n/4)² c(n/4)² c(n/4)²                  ---> Cost: 3 * c(n/4)² = (3/16) cn²
                      / | \   / | \   / | \
 Level 2:                 9 nodes at c(n/16)²                 ---> Cost: 9 * c(n/16)² = (9/256) cn² = (3/16)² cn²
```

- **Cost at Level $i$**:
  $$\text{Cost}_i = 3^i \cdot c \left(\frac{n}{4^i}\right)^2 = c n^2 \left(\frac{3}{16}\right)^i$$

- **Total Cost Summation**:
  $$T(n) = \sum_{i=0}^{\log_4 n - 1} c n^2 \left(\frac{3}{16}\right)^i + \Theta(n^{\log_4 3})$$

Since $\frac{3}{16} < 1$, this is a **geometrically decreasing series**. The sum of an infinite geometric series $\sum_{i=0}^{\infty} r^i = \frac{1}{1-r}$ for $r < 1$:

$$T(n) < c n^2 \sum_{i=0}^{\infty} \left(\frac{3}{16}\right)^i = c n^2 \left(\frac{1}{1 - 3/16}\right) = c n^2 \left(\frac{16}{13}\right) = \Theta(n^2)$$

> [!TIP]
> **Tree Cost Dominance Rule**:
> - If cost **decreases** exponentially across levels ($r < 1$), the **root node dominates** the runtime: $T(n) = \Theta(\text{Root Cost})$.
> - If cost stays **constant** across levels ($r = 1$), runtime is **Height $\times$ Level Cost**: $T(n) = \Theta(f(n) \cdot \log n)$.
> - If cost **increases** exponentially across levels ($r > 1$), the **leaves dominate** the runtime: $T(n) = \Theta(\text{Leaf Count})$.

---

## 8. Real-World Engineering Trade-offs & CS Architecture Insights

### 8.1 Auxiliary Space vs. Space Complexity in Real Systems
In production systems, algorithms that use additional memory incur cache overhead.

```
       CPU Cache Line (64 Bytes)
  +-----------------------------------+
  | A[0] | A[1] | A[2] | A[3] | A[4]  |  ---> Contiguous Array (Spatial Locality)
  +-----------------------------------+
```

- **Iterative vs Recursive Trade-off**:
  - Recursive algorithms (e.g., recursive DFS, Merge Sort) allocate stack frames on the system call stack.
  - Recursion depth of $h$ requires $O(h)$ auxiliary stack memory. Deep recursion risks **StackOverflowError**.
- **Cache Locality**:
  - Sequential array traversals access contiguous memory blocks, maximizing CPU $L1/L2$ cache hits.
  - Dynamic pointer chasing (e.g., trees, linked lists) causes frequent cache misses, making them slower in practice despite having identical Big-O time complexity.

---

## 9. KTU Exam Practice Problems & Solved Numericals

### Problem 1 (Analytical): 
**Compute the time complexity of the following code snippet:**

```c
int count = 0;
for (int i = 1; i <= n; i = i * 2) {
    for (int j = 1; j <= i; j++) {
        count++;
    }
}
```

**Detailed Solution**:
- Outer loop variable $i$ takes values: $1, 2, 4, 8, \dots, 2^k$ where $2^k \le n \implies k = \lfloor \log_2 n \rfloor$.
- For a fixed $i$, the inner loop executes $i$ times.
- Total count is the sum of inner loop iterations over all values of $i$:

$$\begin{aligned}
T(n) &= \sum_{m=0}^{\lfloor \log_2 n \rfloor} 2^m \\
&= 2^0 + 2^1 + 2^2 + \dots + 2^{\lfloor \log_2 n \rfloor} \\
&= \frac{2^{\lfloor \log_2 n \rfloor + 1} - 1}{2 - 1} \\
&\approx 2 \cdot 2^{\log_2 n} - 1 = 2n - 1 = \Theta(n)
\end{aligned}$$

**Answer**: $T(n) = \Theta(n)$.

---

### Problem 2 (Numerical Recurrence):
**Solve the recurrence $T(n) = 2T(n/2) + n^2$ using the Recursion Tree Method.**

**Detailed Solution**:
- Root cost: $n^2$
- Level 1: $2 \cdot (n/2)^2 = 2 \cdot \frac{n^2}{4} = \frac{n^2}{2}$
- Level 2: $4 \cdot (n/4)^2 = 4 \cdot \frac{n^2}{16} = \frac{n^2}{4}$
- Level $i$: $2^i \cdot \left(\frac{n}{2^i}\right)^2 = \frac{n^2}{2^i}$
- Total Sum:
  $$T(n) = \sum_{i=0}^{\log_2 n - 1} \frac{n^2}{2^i} = n^2 \sum_{i=0}^{\log_2 n - 1} \left(\frac{1}{2}\right)^i$$
  Since $\sum_{i=0}^{\infty} (1/2)^i = 2$:
  $$T(n) = n^2 \cdot 2 = \Theta(n^2)$$

**Answer**: $T(n) = \Theta(n^2)$.
