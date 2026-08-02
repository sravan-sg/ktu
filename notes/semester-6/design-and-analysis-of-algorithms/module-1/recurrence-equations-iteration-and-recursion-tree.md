# Module 1 — Topic 4: Recurrence Equations (Iteration & Recursion Tree Methods)

> **Module 1**: Introduction to Algorithm Analysis & Recurrences  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. What is a Recurrence Equation?
When an algorithm solves a problem by calling itself recursively on smaller pieces (using **Divide-and-Conquer**), we write its running time as a mathematical equation called a **Recurrence Equation**.

A recurrence equation expresses $T(n)$ (the time needed for input size $n$) in terms of $T(\text{smaller size})$ and a base case.

### General Form:
$$T(n) = \begin{cases}
c & \text{if } n = 1 \text{ (Base case: easy small problem)} \\
a T(n/b) + f(n) & \text{if } n > 1 \text{ (Recursive case)}
\end{cases}$$

- $a$: Number of smaller subproblems generated.
- $n/b$: Size of each subproblem.
- $f(n)$: Extra time spent dividing the problem and combining the results.

---

## 2. Standard Recurrences Reference

| Algorithm | How it breaks the problem down | Recurrence Equation | Solution |
| :--- | :--- | :--- | :--- |
| **Factorial / Linear Search** | 1 subproblem of size $n-1$, constant work | $T(n) = T(n-1) + O(1)$ | $\Theta(n)$ |
| **Binary Search** | 1 subproblem of size $n/2$, constant work | $T(n) = T(n/2) + O(1)$ | $\Theta(\log n)$ |
| **Tower of Hanoi** | 2 subproblems of size $n-1$, constant work | $T(n) = 2T(n-1) + O(1)$ | $\Theta(2^n)$ |
| **Merge Sort** | 2 subproblems of size $n/2$, linear combining work | $T(n) = 2T(n/2) + O(n)$ | $\Theta(n \log n)$ |
| **Binary Tree Traversal** | 2 subproblems of size $n/2$, constant root work | $T(n) = 2T(n/2) + O(1)$ | $\Theta(n)$ |

---

## 3. Solution of Recurrences — Iteration Method

The **Iteration Method** (also called the **Unrolling Method**) solves a recurrence by expanding $T(n)$ again and again until a pattern appears, then solving down to the base case.

### 4-Step Recipe:
1. **Unroll**: Replace $T(n-1)$ or $T(n/2)$ using the formula 2 or 3 times.
2. **Find Pattern**: Write the equation after $k$ unrolling steps.
3. **Set Base Case**: Find the value of $k$ where the input reaches the base case (e.g. $n - k = 1$ or $n/2^k = 1$).
4. **Substitute & Simplify**: Plug $k$ back in and solve the basic algebra.

---

### Solved Examples:

#### Example 3.1: Solve $T(n) = T(n-1) + c$ with $T(1) = 1$
- **Step 1: Unroll**: $T(n) = [T(n-2) + c] + c = T(n-2) + 2c = T(n-3) + 3c$
- **Step 2: Pattern after $k$ steps**: $T(n) = T(n-k) + k \cdot c$
- **Step 3: Base Case**: $n - k = 1 \implies k = n - 1$.
- **Step 4: Substitute $k$**: $T(n) = T(1) + (n-1)c = 1 + c n - c = \Theta(n)$.

#### Example 3.2: Solve $T(n) = T(n/2) + c$ with $T(1) = 1$ (Binary Search)
- **Step 1: Unroll**: $T(n) = T(n/2^2) + 2c = T(n/2^3) + 3c$
- **Step 2: Pattern after $k$ steps**: $T(n) = T\left(\frac{n}{2^k}\right) + k \cdot c$
- **Step 3: Base Case**: $\frac{n}{2^k} = 1 \implies k = \log_2 n$.
- **Step 4: Substitute $k$**: $T(n) = T(1) + (\log_2 n) \cdot c = \Theta(\log n)$.

#### Example 3.3: Solve $T(n) = 2T(n/2) + cn$ with $T(1) = c$ (Merge Sort)
- **Step 1: Unroll**: $T(n) = 2^2 T(n/2^2) + 2cn = 2^3 T(n/2^3) + 3cn$
- **Step 2: Pattern after $k$ steps**: $T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot cn$
- **Step 3: Base Case**: $\frac{n}{2^k} = 1 \implies k = \log_2 n$.
- **Step 4: Substitute $k$**: $T(n) = n \cdot T(1) + (\log_2 n) \cdot cn = \Theta(n \log n)$.

---

## 4. Solution of Recurrences — Recursion Tree Method

The **Recursion Tree Method** visualizes recursive calls as a tree structure. Each node in the tree shows the work done at that single step.

### 4.1 Layout & Tree Dominance Rules

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

- **Tree Height ($h$)**: $h = \log_2 n$.
- **Level Cost**: $cn$.
- **Total Tree Cost**: $cn \times (\log_2 n + 1) = \Theta(n \log n)$.

### Dominance Rules:
1. **Equal Level Costs**: $\text{Total Time} = \text{Level Cost} \times \text{Height} = \Theta(f(n) \cdot \log n)$.
2. **Decreasing Level Costs**: **Root node dominates** $\implies \Theta(\text{Root Cost})$.
3. **Increasing Level Costs**: **Leaves dominate** $\implies \Theta(\text{Leaf Count})$.

---

## 5. KTU Exam Solved Practice Numericals

### Problem 1: Step-Count Calculation for Nested Loops
**Question**: Find the exact step count and time complexity of:
```c
int count = 0;
for (int i = 1; i <= n; i = i * 2) {
    for (int j = 1; j <= i; j++) {
        count++;
    }
}
```
**Solution**:
1. Inner loop runs $i$ times. $i$ takes values $1, 2, 4, 8, \dots, 2^k \le n$.
2. $\text{Total } T(n) = 1 + 2 + 4 + \dots + 2^{\log_2 n} = \frac{2^{\log_2 n + 1} - 1}{2 - 1} = 2n - 1$.
3. **Answer**: Exact count $= 2n - 1$, Time Complexity $= \Theta(n)$.

---

### Problem 2: Solving Recurrence $T(n) = T(n-1) + n^2$
**Solution**:
1. Unroll: $T(n) = T(n-k) + \sum_{j=0}^{k-1} (n-j)^2$.
2. Base case $n - k = 1 \implies k = n - 1$.
3. $T(n) = T(1) + \sum_{i=2}^n i^2 = \frac{n(n+1)(2n+1)}{6} = \Theta(n^3)$.
4. **Answer**: $T(n) = \Theta(n^3)$.
