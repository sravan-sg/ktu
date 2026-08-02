# Module 1 — Topic 3: Complexity Calculation of Simple Algorithms

> **Module 1**: Introduction to Algorithm Analysis & Recurrences  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Loop Pattern Lookup Table

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

## 2. Walkthrough Derivations for Common Loops

### Example 2.1: Logarithmic Multiplication Loop
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

### Example 2.2: Insertion Sort Step-Count Analysis
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

## 3. Real-World Engineering Trade-offs & Hardware Insights

### Array Locality vs. Linked List Memory Traversal
Why do algorithms operating on contiguous arrays run faster in real life than those operating on linked lists or binary trees, even if both have the same theoretical Big-O complexity?

```
CPU Cache Line (64 Bytes)
+---------------------------------------------------+
| A[0] | A[1] | A[2] | A[3] | A[4] | A[5] | A[6] |  ---> Array (Sequential Memory)
+---------------------------------------------------+
```

- **CPU Cache Hits (Array)**: Modern computer CPUs load data from RAM in 64-byte chunks into high-speed **L1/L2 Cache**. Reading `A[0]` automatically fetches `A[1]` through `A[7]` into the cache. This makes array loops lightning fast.
- **CPU Cache Misses (Linked List / Pointer Chasing)**: Linked list nodes and tree nodes are scattered randomly across RAM. Moving to `node.next` requires jumping to a new RAM address, causing a **cache miss** and slowing down execution.
