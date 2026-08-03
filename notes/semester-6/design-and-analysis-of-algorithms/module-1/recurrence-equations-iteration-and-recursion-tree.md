# Module 1 — Topic 4: Recurrence Equations (Iteration & Recursion Tree Methods)

> **Module 1**: Introduction to Algorithm Analysis & Recurrences  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
When an algorithm uses a **Divide-and-Conquer** strategy (like calling itself to solve a smaller piece of the same problem), its time complexity cannot be expressed with simple loops. Instead, it forms a **Recurrence Equation**.
A recurrence equation defines the total time $T(n)$ needed to solve a problem of size $n$ in terms of the time needed to solve smaller subproblems $T(n/b)$, plus the extra cost $f(n)$ to divide the problem and combine the results. 
To find the final Big-O time complexity, we must "solve" this recurrence using methods like the **Iteration (Unrolling) Method** (expanding the math algebraically) or the **Recursion Tree Method** (drawing the recursive calls as a tree and summing the work done at each level).

### Example
Imagine a boss telling you to sort 1,000 files. You find it too hard, so you divide the pile into two piles of 500 and give them to two assistants. They split them into 250 each and hand them to their assistants, and so on.
The total time taken to sort the 1,000 files is the time your assistants took, plus the time you took to staple the two sorted halves back together. This is a real-world recursive recurrence: $T(\text{1000}) = 2 \times T(\text{500}) + \text{Time to combine}$.

### Applications & Use Cases
- **Merge Sort & Quick Sort**: Standard library sorting algorithms rely heavily on recurrence equations to prove their $O(n \log n)$ bounds.
- **Fast Fourier Transform (FFT)**: Audio processing, image compression (JPEG), and wireless communication (LTE/5G) rely on the FFT algorithm, whose speed is strictly defined and proven via the recurrence $T(n) = 2T(n/2) + O(n)$.
- **Parallel Computing**: When designing distributed systems like Hadoop MapReduce, architects use recurrence models to calculate the overhead cost of network communication versus the speedup from splitting data among multiple servers.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Solving $T(n) = T(n-1) + c$ (Iteration Method)
**Problem:** Solve the recurrence $T(n) = T(n-1) + c$ with base case $T(1) = 1$.
**Step-by-step Solution:**
1. **Unroll the equation:**
   $T(n) = T(n-1) + c$
   Substitute $T(n-1) = T(n-2) + c$:
   $T(n) = [T(n-2) + c] + c = T(n-2) + 2c$
   Substitute $T(n-2) = T(n-3) + c$:
   $T(n) = [T(n-3) + c] + 2c = T(n-3) + 3c$
2. **Find the pattern for $k$ steps:**
   $T(n) = T(n-k) + k \cdot c$
3. **Apply the Base Case:**
   We hit the base case when $n - k = 1 \implies k = n - 1$.
4. **Substitute $k$ back into the pattern:**
   $T(n) = T(1) + (n-1)c$
   $T(n) = 1 + cn - c$.
5. **Conclusion:** Since the highest term is $cn$, the complexity is $O(n)$.

### Example 2: Solving $T(n) = T(n/2) + c$ (Iteration Method for Binary Search)
**Problem:** Solve the recurrence $T(n) = T(n/2) + c$ with base case $T(1) = 1$.
**Step-by-step Solution:**
1. **Unroll the equation:**
   $T(n) = T(n/2) + c$
   Substitute $T(n/2) = T(n/2^2) + c$:
   $T(n) = [T(n/2^2) + c] + c = T(n/2^2) + 2c$
   $T(n) = [T(n/2^3) + c] + 2c = T(n/2^3) + 3c$
2. **Find the pattern for $k$ steps:**
   $T(n) = T(n/2^k) + k \cdot c$
3. **Apply the Base Case:**
   We hit the base case when $n/2^k = 1 \implies 2^k = n$.
   Taking $\log_2$ on both sides: $k = \log_2 n$.
4. **Substitute $k$ back into the pattern:**
   $T(n) = T(1) + (\log_2 n)c$.
5. **Conclusion:** The complexity is $O(\log n)$.

### Example 3: Solving $T(n) = 2T(n/2) + cn$ (Recursion Tree Method for Merge Sort)
**Problem:** Use the recursion tree method to solve $T(n) = 2T(n/2) + cn$ with base case $T(1) = c$.
**Step-by-step Solution:**
1. **Draw the Tree:**
   The root is the non-recursive work $cn$. It splits into 2 children, each of size $n/2$.
   ```text
   Level 0:              cn                     Cost = cn
                       /    \
   Level 1:        c(n/2)   c(n/2)              Cost = 2 * c(n/2) = cn
                  /    \    /    \
   Level 2:   c(n/4) c(n/4) c(n/4) c(n/4)       Cost = 4 * c(n/4) = cn
                 :      :      :      :
   Level h:    T(1)   T(1)   T(1)...T(1)        Cost = n * c = cn
   ```
2. **Calculate the Tree Height ($h$):**
   The problem size halves at each level until it reaches 1. 
   $n/2^h = 1 \implies h = \log_2 n$.
3. **Sum the Level Costs:**
   Every single level of the tree has a total cost of $cn$.
   There are $(\log_2 n + 1)$ total levels (from 0 to $\log_2 n$).
4. **Total Work:**
   Total Cost $= \sum (\text{Level Costs}) = cn \times (\log_2 n + 1) = cn \log_2 n + cn$.
5. **Conclusion:** Dropping the lower order term $cn$, the complexity is $O(n \log n)$.
