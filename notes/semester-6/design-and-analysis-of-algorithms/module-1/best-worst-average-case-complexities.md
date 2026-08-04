# Module 1 — Topic 2: Best, Worst, and Average Case Complexities

> **Module 1**: Introduction to Algorithm Analysis & Recurrences  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
An algorithm's running time doesn't just depend on the size of the input $n$, but also on **how the input data is arranged**.
- **Worst-Case Complexity $T_{\text{worst}}(n)$**: The maximum time the algorithm could possibly take for any input of size $n$. This provides an absolute upper bound guarantee.
- **Best-Case Complexity $T_{\text{best}}(n)$**: The minimum time the algorithm could take for an input of size $n$. It represents the "luckiest" possible scenario.
- **Average-Case Complexity $T_{\text{avg}}(n)$**: The expected running time averaged over all possible inputs of size $n$, based on the probability distribution of inputs.

### Example
Imagine searching for your car in a large parking lot containing $n$ cars:
- **Best Case:** Your car is the very first one you check. (Time: $O(1)$)
- **Worst Case:** You check every single car, and yours is the very last one (or isn't there at all). (Time: $O(n)$)
- **Average Case:** You check about half the cars before finding yours. (Time: $O(n)$)

### Applications & Use Cases
- **Safety-Critical Systems:** Air traffic control or self-driving cars *must* know the **worst-case** execution time to guarantee decisions are made before a collision.
- **Database Query Optimizers:** Databases use **average-case** analysis when generating execution plans, assuming queries reflect typical user distributions.
- **Sorting in Libraries:** Many programming languages use quicksort by default because its **average-case** is extremely fast ($O(n \log n)$), even though its worst-case is slow ($O(n^2)$).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Linear Search
**Problem:** Analyze the Best, Worst, and Average case time complexities for searching element $x$ in an array of $n$ elements.
**Step-by-step Solution:**
1. **Best Case:** The element $x$ is found at index $0$. The loop executes 1 time.
   $T_{\text{best}}(n) = O(1)$.
2. **Worst Case:** The element $x$ is at index $n-1$ or not present. The loop executes $n$ times.
   $T_{\text{worst}}(n) = O(n)$.
3. **Average Case:** Assume $x$ is uniformly distributed. The probability of finding $x$ at any index $i$ is $1/n$. Number of checks for index $i$ is $i+1$.
   $T_{\text{avg}}(n) = \sum_{i=0}^{n-1} \frac{1}{n} \times (i+1) = \frac{1}{n} \left( \frac{n(n+1)}{2} \right) = \frac{n+1}{2}$.
   Since $(n+1)/2$ scales linearly, $T_{\text{avg}}(n) = O(n)$.

### Example 2: Insertion Sort
**Problem:** Trace the Best and Worst cases for sorting an array of size $n$ using Insertion Sort.
**Step-by-step Solution:**
1. **Best Case (Already Sorted Array):** For an array like `[1, 2, 3, 4, 5]`, the inner `while` loop condition immediately fails for every element because each new element is already greater than the previous one. 
   Total comparisons = $n - 1$.
   $T_{\text{best}}(n) = O(n)$.
2. **Worst Case (Reverse Sorted Array):** For an array like `[5, 4, 3, 2, 1]`, every new element must be compared and swapped past *all* previously sorted elements.
   Total comparisons = $1 + 2 + 3 + \dots + (n-1) = \frac{n(n-1)}{2}$.
   $T_{\text{worst}}(n) = O(n^2)$.
3. **Average Case (Random Array):** On average, an element needs to be shifted past half of the already sorted elements.
   Total comparisons $\approx \frac{1}{2} \times \frac{n(n-1)}{2} = \frac{n^2 - n}{4}$.
   $T_{\text{avg}}(n) = O(n^2)$.

### Example 3: Analytical Justification of Asymptotic Growth [April 2018]
**Problem:** Is $2^{n+1} = O(2^n)$? Is $2^{2n} = O(2^n)$? Justify your answer.
**Step-by-step Solution:**
1. **Part A: $2^{n+1} = O(2^n)$**
   - By definition of Big-O, $f(n) = O(g(n))$ if there exists constants $c > 0, n_0 \ge 0$ such that $f(n) \le c \cdot g(n)$ for all $n \ge n_0$.
   - $2^{n+1} = 2^1 \cdot 2^n = 2 \cdot 2^n$.
   - If we choose $c = 2$ and $n_0 = 1$, then $2 \cdot 2^n \le 2 \cdot 2^n$ holds true.
   - **Conclusion:** Yes, $2^{n+1} = O(2^n)$.
2. **Part B: $2^{2n} = O(2^n)$**
   - $2^{2n} = (2^n)^2 = 2^n \cdot 2^n$.
   - For $2^{2n} \le c \cdot 2^n$ to be true, dividing both sides by $2^n$ gives $2^n \le c$.
   - Since $2^n$ grows to infinity as $n$ increases, there is no constant $c$ that can bound it.
   - **Conclusion:** No, $2^{2n} \neq O(2^n)$.

---

### Previous Year Questions & Solutions

1. **"Is $2^{n+1} = O(2^n)$? Is $2^{2n} = O(2^n)$? Justify your answer." [April 2018, Sept 2020]**
   - **Solution:**
     - **Part A: Is $2^{n+1} = O(2^n)$?**
       - **Definition:** $f(n) = O(g(n))$ if $\exists c > 0, n_0 \ge 0$ such that $f(n) \le c \cdot g(n)$ for all $n \ge n_0$.
       - $2^{n+1} = 2^1 \cdot 2^n = 2 \cdot 2^n$.
       - Choose constant $c = 2$ and $n_0 = 1$.
       - Since $2 \cdot 2^n \le 2 \cdot 2^n$ holds for all $n \ge 1$, the condition is satisfied.
       - **Verdict:** **YES**, $2^{n+1} = O(2^n)$.
     - **Part B: Is $2^{2n} = O(2^n)$?**
       - $2^{2n} = (2^n)^2 = 2^n \cdot 2^n$.
       - Assume $2^{2n} \le c \cdot 2^n$ for some constant $c$.
       - Dividing both sides by $2^n$ yields $2^n \le c$.
       - As $n \to \infty$, $2^n$ grows without bound, so no fixed constant $c$ can bound it.
       - **Verdict:** **NO**, $2^{2n} \ne O(2^n)$.

2. **"Explain Asymptotic notations in algorithm analysis." [Dec 2019]**
   - **Solution:** Asymptotic notations are mathematical tools used to describe the limiting behavior of a function when the input size $n \to \infty$:
     - **Big-O Notation ($O$)**: Represents the **Upper Bound** (worst-case performance). $f(n) = O(g(n))$ means $f(n) \le c \cdot g(n)$ for $n \ge n_0$.
     - **Big-Omega Notation ($\Omega$)**: Represents the **Lower Bound** (best-case performance). $f(n) = \Omega(g(n))$ means $f(n) \ge c \cdot g(n)$ for $n \ge n_0$.
     - **Big-Theta Notation ($\Theta$)**: Represents the **Tight Bound** (exact growth rate). $f(n) = \Theta(g(n))$ means $c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n)$ for $n \ge n_0$.

3. **"Define the terms Best case, Worst case and Average case time complexities." [July 2021]**
   - **Solution:**
     - **Worst-Case Complexity $T_{\text{worst}}(n)$**: The maximum number of operations an algorithm performs over all inputs of size $n$. It provides a guaranteed upper bound on execution time.
     - **Best-Case Complexity $T_{\text{best}}(n)$**: The minimum number of operations performed over all inputs of size $n$, representing the most favorable scenario.
     - **Average-Case Complexity $T_{\text{avg}}(n)$**: The expected number of operations averaged over all possible inputs of size $n$, weighted by their probability distribution: $T_{\text{avg}}(n) = \sum P(I) \cdot T(I)$.
