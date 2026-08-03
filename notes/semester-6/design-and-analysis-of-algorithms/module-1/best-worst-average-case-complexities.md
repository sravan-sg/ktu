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

### Example 3: Adding an Element to a Dynamic Array (Vector)
**Problem:** Analyze the Best and Worst case time complexity of appending an element to a dynamic array that doubles its capacity when full.
**Step-by-step Solution:**
1. **Best/Average Case (Capacity not reached):** The dynamic array has empty slots remaining. We simply place the element at the next available index `n`.
   Time taken = 1 assignment operation.
   $T_{\text{best}}(n) = T_{\text{avg}}(n) = O(1)$.
2. **Worst Case (Capacity reached):** The array is full. The algorithm must:
   - Allocate a new array of size $2n$.
   - Copy all $n$ existing elements to the new array.
   - Insert the new element.
   Time taken = $O(n)$ copies + 1 insertion.
   $T_{\text{worst}}(n) = O(n)$.
*(Note: Across $n$ insertions, this averages out to $O(1)$ amortized time).*
