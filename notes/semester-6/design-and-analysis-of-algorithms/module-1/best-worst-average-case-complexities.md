# Module 1 — Topic 2: Best, Worst, and Average Case Complexities

> **Module 1**: Introduction to Algorithm Analysis & Recurrences  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Complexity Frameworks Overview

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

## 2. Detailed Example: Linear Search Case Analysis

Let's search for a target value $x$ in an array of $n$ numbers:

```python
def linear_search(A, n, x):
    for i in range(n):
        if A[i] == x:
            return i     # Found! Return index
    return -1            # Not found!
```

### Case Derivations:

- **Best Case**: The value $x$ happens to be at the very first slot ($A[0]$).
  - Loop runs 1 time.
  - $T_{\text{best}}(n) = O(1)$ (Constant time).

- **Worst Case**: The value $x$ is at the very last slot ($A[n-1]$) or is missing completely.
  - Loop runs all $n$ times.
  - $T_{\text{worst}}(n) = O(n)$ (Linear time).

- **Average Case Analysis**:
  - Suppose $x$ is present in the array with probability $p = 1$, and is equally likely to be at any index from $0$ to $n-1$.
  - If $x$ is at index $0$, it takes $1$ check.
  - If $x$ is at index $1$, it takes $2$ checks.
  - If $x$ is at index $i$, it takes $i + 1$ checks.

$$\text{Average checks} = \frac{1 + 2 + 3 + \dots + n}{n} = \frac{\frac{n(n+1)}{2}}{n} = \frac{n+1}{2}$$

For large $n$, $\frac{n+1}{2} \approx \frac{n}{2}$, which is still proportional to $n$. Therefore, $T_{\text{avg}}(n) = \Theta(n)$.

---

## 3. Asymptotic Cases Summary Reference

| Case | Definition | Math Representation | Practical Usage |
| :--- | :--- | :--- | :--- |
| **Worst-Case** | Maximum time over all inputs of size $n$ | $T_{\text{worst}}(n) = \max T(I)$ | Guaranteed safety limit (Critical systems) |
| **Best-Case** | Minimum time over all inputs of size $n$ | $T_{\text{best}}(n) = \min T(I)$ | Rarely useful (Optimistic scenario) |
| **Average-Case** | Expected time averaged over all inputs | $T_{\text{avg}}(n) = E[T(I)]$ | Predicts real-world typical performance |
