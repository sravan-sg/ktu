# Module 1 — Topic 1: Time and Space Complexity & Elementary Operations

> **Module 1**: Introduction to Algorithm Analysis & Recurrences  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
An **algorithm** is a precise, step-by-step set of instructions to convert a given input into a desired output. Just like a cooking recipe, it must have clear steps (definiteness), it must finish eventually (finiteness), and each step must be doable (effectiveness).
When we write algorithms, we need a mathematical way to compare them *before* running them on a computer. This is **Algorithm Analysis**. 
- **Time Complexity** measures how the number of basic operations grows as the input size $n$ increases. 
- **Space Complexity** measures how much extra memory (RAM) the algorithm requires as $n$ increases, combining fixed space (code, constants) and auxiliary space (temporary variables, call stacks).

### Example
Suppose two programmers write a program to search a database of 1 million users. 
- **Programmer A** checks every user one by one (Linear Time).
- **Programmer B** uses binary search to repeatedly cut the search space in half (Logarithmic Time).
On a supercomputer with 5 users, both are instant. But on a mobile phone with 1 million users, A takes 1,000,000 steps, while B takes only $\sim 20$ steps. Analysis proves B's algorithm is vastly superior purely by mathematical growth rates.

### Applications & Use Cases
- **Database Indexing**: Search engines and databases strictly evaluate time complexity to ensure they can retrieve records in milliseconds, even when scaling to billions of rows.
- **Embedded Systems**: In microcontrollers with strict 4KB RAM limits, evaluating Space Complexity is critical to ensure the software does not crash due to memory overflow.
- **High-Frequency Trading**: Financial algorithms require absolute minimal time complexity to execute trades fractions of a second faster than competitors.

---

## 2. Elementary Operations & Frequency Count Method

An **elementary operation** is a basic step (addition, assignment, comparison) that executes in $O(1)$ constant time on a Random Access Machine (RAM). The **Frequency Count Method** calculates total time by summing how many times each basic instruction executes.

### 3 Solved Numerical/Analytical Examples

#### Example 1: Simple Variable Swap
**Problem:** Calculate the time and space complexity of swapping two variables.
```text
Algorithm Swap(a, b):
1. temp = a     // Cost c1, executes 1 time
2. a = b        // Cost c2, executes 1 time
3. b = temp     // Cost c3, executes 1 time
```
**Step-by-step Solution:**
- **Time Analysis:** Total Time $T(n) = c_1(1) + c_2(1) + c_3(1) = c_1 + c_2 + c_3$. Since this is a constant independent of $n$, $T(n) = O(1)$.
- **Space Analysis:** The algorithm uses three variables (`a`, `b`, `temp`). Fixed space is required, but no arrays or recursive stacks depend on an input size $n$. Thus, Space Complexity $S(n) = O(1)$.

#### Example 2: Iterating Through an Array
**Problem:** Calculate the time complexity of summing an array of size $n$.
```text
Algorithm Sum(A, n):
1. total = 0             // Cost c1, executes 1 time
2. for i = 1 to n do     // Cost c2, executes (n + 1) times (includes exit check)
3.     total = total + A[i] // Cost c3, executes n times
4. return total          // Cost c4, executes 1 time
```
**Step-by-step Solution:**
- **Time Analysis:** 
  $T(n) = c_1(1) + c_2(n+1) + c_3(n) + c_4(1)$
  $T(n) = (c_2 + c_3)n + (c_1 + c_2 + c_4)$
  Let $a = (c_2 + c_3)$ and $b = (c_1 + c_2 + c_4)$. Then $T(n) = an + b$.
  Since it grows linearly, $T(n) = O(n)$.
- **Space Analysis:** Only variables `total` and `i` are used in auxiliary space. $S(n) = O(1)$ auxiliary space.

#### Example 3: Nested Loops (Matrix Addition)
**Problem:** Calculate the time complexity of adding two $n \times n$ matrices.
```text
Algorithm MatrixAdd(A, B, n):
1. for i = 1 to n do                // Cost c1, executes (n + 1) times
2.     for j = 1 to n do            // Cost c2, executes n*(n + 1) times
3.         C[i][j] = A[i][j] + B[i][j] // Cost c3, executes n*n times
```
**Step-by-step Solution:**
- **Time Analysis:**
  Line 1 runs $n+1$ times.
  Line 2 runs $(n+1)$ times *for each* of the $n$ iterations of the outer loop $\Rightarrow n(n+1) = n^2 + n$.
  Line 3 runs $n$ times *for each* of the $n$ iterations of the outer loop $\Rightarrow n \times n = n^2$.
  $T(n) = c_1(n+1) + c_2(n^2 + n) + c_3(n^2)$
  $T(n) = (c_2 + c_3)n^2 + (c_1 + c_2)n + c_1$
  Since the highest degree term is $n^2$, $T(n) = O(n^2)$.
- **Space Analysis:** We create a new matrix $C$ of size $n \times n$. Therefore, auxiliary space is $O(n^2)$.
