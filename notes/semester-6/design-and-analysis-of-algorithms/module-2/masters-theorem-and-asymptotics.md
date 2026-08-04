# Module 2 — Topic 1: Master's Theorem, Asymptotic Notations & Functions

> **Module 2**: Master's Theorem, Asymptotics & Balanced Structures  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
When analyzing algorithms, we don't care about the exact number of seconds a program takes, because that changes based on the computer's speed. Instead, we care about the **growth rate**: how does the running time increase as the input size $n$ gets massively large? **Asymptotic notations** ($O, \Omega, \Theta$) are mathematical tools that let us classify algorithms based on their growth rates, ignoring small constant factors and lower-order terms. 
When algorithms use recursion (specifically Divide-and-Conquer), their time complexity forms a recurrence relation like $T(n) = aT(n/b) + f(n)$. Solving these from scratch is painful. The **Master's Theorem** is a "cookbook formula" that lets you instantly find the time complexity by comparing the time spent dividing/combining $f(n)$ against the time spent solving the subproblems $n^{\log_b a}$.

### Example
Think of asymptotic notation like describing the wealth of a billionaire. If a billionaire gains $10, we ignore it. We only care about the billions (the highest-order term). 
Think of the Master's Theorem like a factory assembly line. 
- $a$ is the number of workers.
- $n/b$ is the size of the piece each worker handles.
- $f(n)$ is the time the manager takes to combine the pieces.
The theorem just asks: Who is the bottleneck? The workers (Case 1), the manager (Case 3), or are they perfectly balanced (Case 2)?

### Applications & Use Cases
- **Algorithm Design & Benchmarking**: Every standard algorithm library (like Python's `list.sort()`) relies heavily on asymptotic notation bounds to guarantee performance on vast datasets.
- **Compiler Optimizations**: When compiling recursive functions, a compiler might analyze the recurrence mathematically to determine if it can be unrolled or if it requires tail-call optimization.
- **System Architecture**: High-level system design relies on Master's Theorem to predict how a distributed Divide-and-Conquer framework (like Apache Hadoop) will perform as the data partition size $b$ and parallel nodes $a$ increase.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Case 1 (Subproblem Heavy - Leaves Dominate) [April 2018]
**Problem:** Solve the recurrence $T(n) = 9T(n/3) + n$ using the Master's Theorem.
**Step-by-step Solution:**
1. **Identify Variables:** Compare to $T(n) = aT(n/b) + f(n)$. 
   $a = 9$, $b = 3$, $f(n) = n$.
2. **Calculate Critical Threshold:** $n^{\log_b a} = n^{\log_3 9} = n^2$.
3. **Compare $f(n)$ and Threshold:**
   $f(n) = n^1$ and the threshold is $n^2$.
   Since $n$ grows polynomially slower than $n^2$ by a factor of $n^1$ ($\epsilon = 1$), this falls into **Case 1**.
   The work done at the leaves (subproblems) vastly outweighs the work done at the root.
4. **Result:** $T(n) = \Theta(n^{\log_b a}) = \Theta(n^2)$.

### Example 2: Case 2 (Balanced Work) [Dec 2019]
**Problem:** Solve the recurrence $T(n) = 2T(n/2) + n$ using the Master's Theorem (This is Merge Sort).
**Step-by-step Solution:**
1. **Identify Variables:** 
   $a = 2$, $b = 2$, $f(n) = n$.
2. **Calculate Critical Threshold:** $n^{\log_b a} = n^{\log_2 2} = n^1 = n$.
3. **Compare $f(n)$ and Threshold:**
   $f(n) = n$ and the threshold is $n$.
   Since $f(n) = \Theta(n^{\log_b a} \log^k n)$ where $k = 0$, this falls into **Case 2**.
   The work is perfectly balanced across all levels of the recursion tree.
4. **Result:** We simply multiply the threshold by an extra logarithmic factor:
   $T(n) = \Theta(n^{\log_b a} \log^{k+1} n) = \Theta(n \log n)$.

### Example 3: Case 3 (Combine Heavy - Root Dominates)
**Problem:** Solve the recurrence $T(n) = 3T(n/4) + n \log n$ using the Master's Theorem.
**Step-by-step Solution:**
1. **Identify Variables:** 
   $a = 3$, $b = 4$, $f(n) = n \log n$.
2. **Calculate Critical Threshold:** $n^{\log_b a} = n^{\log_4 3} \approx n^{0.793}$.
3. **Compare $f(n)$ and Threshold:**
   $f(n) = n \log n$ and the threshold is roughly $n^{0.79}$.
   Since $n \log n$ grows polynomially faster than $n^{0.79}$ by at least a factor of $n^{0.2}$, this falls into **Case 3**.
   The work done combining the subproblems at the root dominates the total time.
4. **Check Regularity Condition:** We must ensure $a f(n/b) \le c f(n)$ for some $c < 1$.
   $3 (n/4) \log(n/4) \le c (n \log n)$.
   $(3/4) n \log(n/4) \le (3/4) n \log n$. This holds true for $c = 3/4$.
5. **Result:** $T(n) = \Theta(f(n)) = \Theta(n \log n)$.

---

### Previous Year Questions & Solutions

1. **"State Master's Theorem. Find the solution to the recurrence equation $T(n) = 4T(n/2) + n$." [April 2018, July 2021]**
   - **Solution:**
     - **Statement of Master's Theorem:** Let $a \ge 1$ and $b > 1$ be constants, let $f(n)$ be a function, and let $T(n) = aT(n/b) + f(n)$.
       1. **Case 1:** If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a})$.
       2. **Case 2:** If $f(n) = \Theta(n^{\log_b a})$, then $T(n) = \Theta(n^{\log_b a} \log n)$.
       3. **Case 3:** If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$ and $a f(n/b) \le c f(n)$ for $c < 1$, then $T(n) = \Theta(f(n))$.
     - **Solving $T(n) = 4T(n/2) + n$:**
       1. Extract parameters: $a = 4$, $b = 2$, $f(n) = n$.
       2. Calculate threshold: $n^{\log_b a} = n^{\log_2 4} = n^2$.
       3. Compare $f(n) = n^1$ with $n^2$: $n = O(n^{2 - 1})$ where $\epsilon = 1 > 0$.
       4. Leaves cost $n^2$ dominates $f(n)$. By Case 1, **$T(n) = \Theta(n^2)$**.

2. **"Solve $T(n) = 2T(n/2) + \Theta(n)$ using Master's Theorem." [Dec 2019, Sept 2020]**
   - **Solution:**
     1. Extract parameters: $a = 2$, $b = 2$, $f(n) = \Theta(n)$.
     2. Calculate threshold: $n^{\log_b a} = n^{\log_2 2} = n^1$.
     3. Compare $f(n) = \Theta(n^1)$ with threshold $n^1$: $f(n) = \Theta(n^{\log_b a})$.
     4. Work at each level is balanced. By Case 2, **$T(n) = \Theta(n \log n)$**.
