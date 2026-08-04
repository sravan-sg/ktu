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

### Example 2: Solving $T(n) = 2T(n/2) + n$ (Iteration Method) [Dec 2019]
**Problem:** Solve the recurrence $T(n) = 2T(n/2) + n$, with base case $T(1) = 1$ using the iteration method.
**Step-by-step Solution:**
1. **Unroll the equation:**
   $T(n) = 2T(n/2) + n$
   Substitute $T(n/2) = 2T(n/4) + n/2$:
   $T(n) = 2[2T(n/4) + n/2] + n = 4T(n/4) + n + n = 4T(n/4) + 2n$
   Substitute $T(n/4) = 2T(n/8) + n/4$:
   $T(n) = 4[2T(n/8) + n/4] + 2n = 8T(n/8) + n + 2n = 8T(n/8) + 3n$
2. **Find the pattern for $k$ steps:**
   $T(n) = 2^k T(n/2^k) + k \cdot n$
3. **Apply the Base Case:**
   We hit the base case when $n/2^k = 1 \implies 2^k = n$.
   Taking $\log_2$ on both sides: $k = \log_2 n$.
4. **Substitute $k$ back into the pattern:**
   $T(n) = 2^{\log_2 n} T(1) + (\log_2 n) \cdot n$
   Since $2^{\log_2 n} = n$ and $T(1) = 1$:
   $T(n) = n(1) + n \log_2 n$.
5. **Conclusion:** The complexity is $O(n \log n)$.

### Example 3: Solving $T(n) = 2T(n/2) + cn$ (Recursion Tree Method) [Dec 2019]
**Problem:** Use the recursion tree method to solve $T(n) = 2T(n/2) + cn$ (e.g., Merge Sort) with base case $T(1) = c$.
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

---

### Previous Year Questions & Solutions

1. **"Solve using Iteration method $T(n)=2T(n/2)+n, T(1)=1$" [Dec 2019, July 2021]**
   - **Solution:**
     - **Step 1: Express $T(n/2)$ and $T(n/4)$:**
       $T(n/2) = 2T(n/4) + n/2$
       $T(n/4) = 2T(n/8) + n/4$
     - **Step 2: Substitute recursively (Unroll):**
       - 1st substitution: $T(n) = 2[2T(n/4) + n/2] + n = 4T(n/4) + 2n$
       - 2nd substitution: $T(n) = 4[2T(n/8) + n/4] + 2n = 8T(n/8) + 3n$
     - **Step 3: Establish pattern after $k$ steps:**
       $T(n) = 2^k T(n/2^k) + k \cdot n$
     - **Step 4: Base case substitution:**
       Set $n/2^k = 1 \implies 2^k = n \implies k = \log_2 n$.
       $T(n) = n \cdot T(1) + (\log_2 n) \cdot n = n(1) + n \log_2 n = n \log_2 n + n$.
     - **Final Bound:** **$T(n) = \Theta(n \log n)$**.

2. **"Using iteration solve the recurrence equation $T(n) = T(n-1) + n, T(1) = 1$." [April 2018]**
   - **Solution:**
     - **Step 1: Unroll the recurrence:**
       $T(n) = T(n-1) + n$
       $T(n-1) = T(n-2) + (n-1)$
       $T(n-2) = T(n-3) + (n-2)$
     - **Step 2: Substitute back:**
       $T(n) = [T(n-2) + (n-1)] + n = T(n-2) + (n-1) + n$
       $T(n) = T(n-3) + (n-2) + (n-1) + n$
     - **Step 3: $k^{th}$ step pattern:**
       $T(n) = T(n-k) + \sum_{j=0}^{k-1} (n - j)$
     - **Step 4: Set to base case:**
       $n - k = 1 \implies k = n - 1$.
       $T(n) = T(1) + \sum_{i=2}^{n} i = 1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$.
     - **Final Bound:** **$T(n) = \Theta(n^2)$**.

3. **"Solve using Recursion Tree method $T(n) = 2T(n/2) + cn, T(1) = c$." [Dec 2019]**
   - **Solution:**
     - **Tree Structure:**
       - Level 0 (Root): Cost $= cn$, Nodes $= 1$.
       - Level 1: 2 nodes of size $n/2$, Cost $= 2 \times c(n/2) = cn$.
       - Level 2: 4 nodes of size $n/4$, Cost $= 4 \times c(n/4) = cn$.
       - Level $i$: $2^i$ nodes of size $n/2^i$, Cost $= 2^i \times c(n/2^i) = cn$.
     - **Tree Height:** Halving problem size down to 1 gives $n/2^h = 1 \implies h = \log_2 n$.
     - **Total Cost Summation:**
       Total Cost $= \sum_{i=0}^{\log_2 n} (\text{Cost per level}) = \sum_{i=0}^{\log_2 n} cn = cn \times (\log_2 n + 1) = cn \log_2 n + cn$.
     - **Final Bound:** **$T(n) = O(n \log n)$**.
