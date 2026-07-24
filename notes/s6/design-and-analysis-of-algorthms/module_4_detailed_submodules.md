# CS302 Design and Analysis of Algorithms
## Module IV: Divide and Conquer & Dynamic Programming

### 1. The Divide and Conquer Strategy
#### Explanation
**refferal video:**https://youtu.be/PfEmF07S4hw?si=uWmM6WL5EN_N5tlV

Divide and Conquer is a top-down algorithm design paradigm based on multi-branched recursion. It works by breaking a complex, massive problem into several smaller, manageable sub-problems of the exact same type.

The methodology strictly follows three steps:
- **Divide**: Partition the original problem into a set of smaller sub-problems.
- **Conquer**: Solve every sub-problem individually and recursively. If a sub-problem is small enough (the "base case"), solve it directly without further division.
- **Combine**: Merge the solutions of the smaller sub-problems together to form the final solution to the original, massive problem.

#### The Control Abstraction
A "Control Abstraction" is the general pseudocode template that all algorithms of this type follow.
```
Algorithm DivideAndConquer(P) {
    if (Small(P)) {
        return Solve(P);
    } else {
        Divide P into smaller instances P1, P2, ..., Pk
        Apply DivideAndConquer to each of these subproblems
        return Combine(DivideAndConquer(P1), ..., DivideAndConquer(Pk));
    }
}
```

#### Applications & Use Cases
- **Fast Sorting**: Standard library sorting functions (like Java's Arrays.sort()) often use algorithms built on this paradigm, such as Quick Sort and Merge Sort, which drastically outperform basic sorts on large datasets.
- **Big Data Processing**: Frameworks like Apache Hadoop (MapReduce) literally "divide" terabytes of data across thousands of servers, "conquer" the data locally, and "combine" the results.
- **Computational Geometry**: Finding the closest pair of points on a 2D plane (used in air traffic control collision detection).

### Binary Search
#### Explanation
https://youtu.be/ureoWZPDxI8?si=7kCYOCKt5r4C8698
Binary Search is a highly efficient searching algorithm that works by repeatedly dividing in half the portion of the sorted array that could contain the target element. Think of it like looking for a word in a dictionary: instead of reading page by page, you open the book to the middle, check if the word is before or after, and then split the remaining half again.

- **Time Complexity**: O(log n) in the worst and average cases.
- **Space Complexity**: O(1) for the iterative approach, O(log n) for the recursive approach (due to the call stack).

#### Code Implementation


**Golang:**
```go
func binarySearch(arr []int, target int) int {
    low, high := 0, len(arr)-1
    for low <= high {
        mid := low + (high-low)/2
        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return -1
}
```

### 2. 2-Way Merge Sort
#### Explanation
**refference video:**https://youtu.be/SpxhCumLqBU?si=ohiDc7nKZVtkBgC1
Merge Sort is the textbook example of Divide and Conquer. It takes an unsorted array, recursively cuts it perfectly in half until every element is isolated in its own single-element array (which is technically sorted). Then, it systematically "merges" those tiny arrays back together in sorted order.
- **Time Complexity**: Θ(n log n) in all cases (Best, Worst, and Average).
- **Space Complexity**: O(n) because it requires a temporary secondary array during the "Combine" (merge) phase.

#### Code Implementation


**Golang:**
```go
func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    mid := len(arr) / 2
    left := mergeSort(arr[:mid])
    right := mergeSort(arr[mid:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    res := make([]int, 0, len(left)+len(right))
    i, j := 0, 0
    for i < len(left) && j < len(right) {
        if left[i] < right[j] {
            res = append(res, left[i])
            i++
        } else {
            res = append(res, right[j])
            j++
        }
    }
    res = append(res, left[i:]...)
    res = append(res, right[j:]...)
    return res
}
```

#### 3. Solved Examples
**Example 2.1: Step-by-Step Execution Trace**
- **Problem**: Sort the array [38, 27, 43, 3, 9, 82, 10].
- **Solution**:
    - Divide: Split into [38, 27, 43, 3] and [9, 82, 10].
    - Divide: Split further: [38, 27], [43, 3], [9, 82], [10].
    - Divide (Base Cases): [38], [27], [43], [3], [9], [82], [10].
    - Conquer & Combine (Level 1): Merge adjacent pairs in sorted order: [27, 38], [3, 43], [9, 82], [10].
    - Combine (Level 2): Merge adjacent blocks: [3, 27, 38, 43] and [9, 10, 82].
    - Combine (Final): Merge the two halves using the two-pointer technique: [3, 9, 10, 27, 38, 43, 82].

**Example 2.2: The Merge Operation (Two Pointers)**
- **Problem**: Demonstrate the mechanics of merging two already sorted sub-arrays: L = [2, 5, 8] and R = [1, 6, 7].
- **Solution**:
    - Initialize pointers: i = 0 (for L), j = 0 (for R), and a new array M = [].
    - Compare L[0] (2) and R[0] (1). 1 < 2. Append 1. Increment j. (M = [1])
    - Compare L[0] (2) and R[1] (6). 2 < 6. Append 2. Increment i. (M = [1, 2])
    - Compare L[1] (5) and R[1] (6). 5 < 6. Append 5. Increment i. (M = [1, 2, 5])
    - Compare L[2] (8) and R[1] (6). 6 < 8. Append 6. Increment j. (M = [1, 2, 5, 6])
    - Compare L[2] (8) and R[2] (7). 7 < 8. Append 7. Increment j. (M = [1, 2, 5, 6, 7])
    - List R is exhausted. Append all remaining elements from L.
    - Final Array: M = [1, 2, 5, 6, 7, 8].

**Example 2.3: Mathematical Analysis (Recurrence Relation)**
- **Problem**: Formulate and solve the recurrence relation for Merge Sort.
- **Solution**:
    - Formulation: The algorithm splits the array of size n into 2 halves, each taking T(n/2) time. Merging them back together takes O(n) time. Therefore:
    T(n) = 2T(n/2) + cn
    - Solve via Master Theorem:
    a = 2, b = 2, f(n) = n^1
    Calculate n^(log_b a) = n^(log_2 2) = n^1.
    Since f(n) = Θ(n^(log_b a)), this falls exactly into Case 2 of the Master Theorem.
    - Result: The complexity is Θ(n^(log_b a) * log n) = Θ(n log n).

### Quick Sort
**reference video:**https://youtu.be/K_qoLz6Fv7M?si=pS9HUg5LY3iw7h4m
#### Explanation
Quick Sort is a highly efficient, in-place sorting algorithm based on the Divide and Conquer strategy. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

- **Time Complexity**: O(n log n) average case, O(n^2) worst case (which happens when the array is already sorted and we pick the first/last element as the pivot).
- **Space Complexity**: O(log n) average due to recursion stack.

#### Code Implementation


**Golang:**
```go
func quickSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    pivot := arr[len(arr)/2]
    var left, middle, right []int
    for _, v := range arr {
        if v < pivot {
            left = append(left, v)
        } else if v == pivot {
            middle = append(middle, v)
        } else {
            right = append(right, v)
        }
    }
    left = quickSort(left)
    right = quickSort(right)
    return append(append(left, middle...), right...)
}
```

### 3. Strassen’s Matrix Multiplication
#### Explanation
Standard matrix multiplication for two n x n matrices involves three nested loops, giving it a cubic time complexity of O(n^3).
Volker Strassen discovered a Divide and Conquer approach. He proved that you don't need 8 recursive multiplication calls to multiply the 4 quadrants of a split matrix. By using clever algebraic combinations, you only need 7 multiplication calls. Because multiplication operations are far more computationally expensive than additions, dropping from 8 to 7 recursive calls drastically improves the algorithm's performance on massive matrices.
- **Time Complexity**: Reduced from O(n^3) to exactly O(n^(log_2 7)) ≈ O(n^2.81).

#### Solved Examples
**Example 3.1: The Standard vs. Strassen Sub-problem Count**
- **Problem**: If you divide an 8x8 matrix into four 4x4 quadrants, how many 4x4 multiplications does the standard divide-and-conquer algorithm perform versus Strassen's algorithm?
- **Solution**:
    - Standard: Requires 8 recursive sub-multiplications.
    - Strassen: Requires 7 recursive sub-multiplications.
    - Conclusion: While 1 less operation seems small, as recursion goes deeper (e.g., 1024x1024 matrices), the savings multiply exponentially (8^k vs 7^k).

**Example 3.2: Strassen's 7 Formulas**
- **Problem**: Define the 7 core multiplications (P1 through P7) used in Strassen's method for matrices A and B split into quadrants A_11, A_12, etc.
- **Solution**:
    P1 = A_11 x (B_12 - B_22)
    P2 = (A_11 + A_12) x B_22
    P3 = (A_21 + A_22) x B_11
    P4 = A_22 x (B_21 - B_11)
    P5 = (A_11 + A_22) x (B_11 + B_22)
    P6 = (A_12 - A_22) x (B_21 + B_22)
    P7 = (A_11 - A_21) x (B_11 + B_12)
    (Note: You combine these 7 values using specific additions/subtractions to yield the 4 quadrants of the final matrix C).

**Example 3.3: Analysis via Recurrence Relation**
- **Problem**: Formulate and solve the recurrence relation for Strassen's Algorithm.
- **Solution**:
    1. Formulation: We divide the n x n matrix into four n/2 x n/2 matrices. We perform 7 multiplications on these sub-matrices. The additions/subtractions take O(n^2) time. Therefore: T(n) = 7T(n/2) + O(n^2)
    2. Solve via Master Theorem:
       - a = 7, b = 2, f(n) = n^2
       - Calculate n^(log_b a) = n^(log_2 7) ≈ n^2.81.
       - Since f(n) = O(n^(log_b a - ε)) (because n^2 is polynomially smaller than n^2.81), this is Case 1.
    3. Result: The complexity is firmly Θ(n^(log_2 7)), proving it is asymptotically faster than O(n^3).

### 4. Dynamic Programming (DP) & The Optimality Principle
#### Explanation
Dynamic Programming is a bottom-up algorithm design strategy. Like Divide and Conquer, it breaks problems into smaller sub-problems.
The Critical Difference: In Divide and Conquer, sub-problems are independent. In Dynamic Programming, sub-problems overlap. DP algorithms solve each sub-problem exactly once and store the answer in a memory table (an array or matrix). If the same sub-problem is encountered again, it simply looks up the answer instead of recalculating it. This memory-saving technique is called Memoization or Tabulation.

#### The Principle of Optimality
Formulated by Richard Bellman, this principle states: An optimal policy has the property that whatever the initial state and initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision. In simpler terms: A globally optimal solution can only be constructed from locally optimal sub-solutions. If a problem does not possess this property, Dynamic Programming cannot be used.

#### The Control Abstraction (Tabulation Approach)
```
Algorithm DynamicProgramming(n) {
    Create a table/array T to store solutions
    for i = 0 to n {
        if (i is a base case) {
            T[i] = Base value
        } else {
            // The mathematical relationship linking current state to past states
            T[i] = RecurrenceRelation(T[past_states])
        }
    }
    return T[n] // The final answer is built at the end
}
```

#### Applications & Use Cases
- **Bioinformatics**: Sequence alignment (comparing DNA or RNA strings) using algorithms like Needleman-Wunsch.
- **Natural Language Processing**: Spell checkers use the Levenshtein Distance (a DP algorithm) to find the minimum edits required to fix a typo.

### 5. Optimal Matrix Chain Multiplication
#### Explanation
When multiplying a long sequence (chain) of matrices, matrix multiplication is associative: (A x B) x C = A x (B x C). The final mathematical answer is the same, but the number of scalar multiplications required can vary massively depending on where you place the parentheses.
The Matrix Chain Multiplication algorithm uses Dynamic Programming to find the absolute most efficient way to parenthesize a chain of matrices.
- **Time Complexity**: O(n^3) to fill the DP table.

#### Solved Examples
**Example 5.1: The Cost Discrepancy**
- **Problem**: You have 3 matrices with dimensions: A(10 x 100), B(100 x 5), and C(5 x 50). Calculate the total scalar multiplications required for (A x B) x C versus A x (B x C).
- **Solution**:
    - Option 1: (A x B) x C
      - Cost of A x B = 10 x 100 x 5 = 5,000. (Resulting matrix AB is 10 x 5).
      - Cost of AB x C = 10 x 5 x 50 = 2,500.
      - Total = 5,000 + 2,500 = 7,500.
    - Option 2: A x (B x C)
      - Cost of B x C = 100 x 5 x 50 = 25,000. (Resulting matrix BC is 100 x 50).
      - Cost of A x BC = 10 x 100 x 50 = 50,000.
      - Total = 25,000 + 50,000 = 75,000.
    Conclusion: Option 1 is exactly 10 times faster.

**Example 5.2: The DP Recurrence Relation**
- **Problem**: Define the mathematical formula (the DP state transition) used to fill the cost table m[i, j]. Let p be an array of the matrix dimensions.
- **Solution**:
    1. Let m[i, j] be the minimum cost of multiplying matrices from index i to j.
    2. If i = j (only one matrix), the cost is 0. So, m[i, i] = 0.
    3. If i < j, we test splitting the chain at every possible point k (where i <= k < j).
    4. Formula: m[i, j] = min_{i<=k<j} ( m[i, k] + m[k+1, j] + p_{i-1} p_k p_j )

**Example 5.3: Base Case Table Initialization**
- **Problem**: If we are given 4 matrices (A_1, A_2, A_3, A_4), how is the 2D DP cost table initialized before the complex calculations begin?
- **Solution**:
    1. The algorithm creates a 4 x 4 table.
    2. It identifies the base cases: multiplying a matrix by itself costs 0 operations.
    3. It sets the entire main diagonal to 0: m[1, 1] = 0, m[2, 2] = 0, m[3, 3] = 0, and m[4, 4] = 0.
    4. It will then compute chains of length 2 (the diagonal just above), then length 3, until reaching m[1, 4] (the top right corner), which holds the final answer.

### 6. Bellman-Ford Algorithm
While Dijkstra's algorithm (Module III) finds the shortest path, it mathematically fails if a graph contains negative weight edges. The Bellman-Ford algorithm solves this problem using Dynamic Programming.
It works by "relaxing" (updating) every single edge in the graph exactly V - 1 times (where V is the number of vertices). By the Principle of Optimality, any shortest path in a graph without negative cycles can have at most V - 1 edges.
- **Negative Cycle Detection**: After V - 1 iterations, it runs one final check. If any edge can still be relaxed and made shorter, it proves the graph contains a negative weight cycle (meaning no shortest path exists because you could just loop the negative cycle forever to reach -∞).
- **Time Complexity**: O(V · E). Slower than Dijkstra, but far more robust.

#### Solved Examples
**Example 6.1: The Relaxation Logic**
- **Problem**: In Bellman-Ford, distance to Node A is 10. Distance to Node B is ∞. Evaluate the edge A → B with a weight of -3.
- **Solution**:
    1. Formula: if dist[A] + weight < dist[B] then update dist[B].
    2. Check: 10 + (-3) = 7.
    3. Compare: 7 < ∞.
    4. Result: The distance to B is updated to exactly 7.

**Example 6.2: Iteration Constraint**
- **Problem**: You have a graph with 5 vertices. How many times must the Bellman-Ford outer loop iterate over all edges to guarantee the shortest paths are found?
- **Solution**:
    1. Identify the number of vertices: V = 5.
    2. A valid shortest path without loops can contain a maximum of V - 1 edges.
    3. Calculation: 5 - 1 = 4.
    4. Result: The outer loop must run exactly 4 times.

**Example 6.3: Negative Cycle Proof**
- **Problem**: After completing the required V - 1 iterations on a 3-node graph, the distances are S = 0, X = 5, Y = 2. You run the final 1-iteration safety check. You look at edge X → Y, which has a weight of -5. Does this graph contain a negative cycle?
- **Solution**:
    1. Check the relaxation formula one final time.
    2. Path through X: dist[X] + weight → 5 + (-5) = 0.
    3. Current known distance to Y is 2.
    4. Compare: 0 < 2. The distance can be optimized further.
    5. Result: Yes. Because a path shortened after V - 1 iterations, we have mathematically proven a negative cycle exists.
