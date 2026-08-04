# Module 1 — Topic 3: Complexity Calculation of Simple Algorithms

> **Module 1**: Introduction to Algorithm Analysis & Recurrences  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
Calculating the complexity of simple algorithms is the process of translating source code (loops, recursive calls, basic math operations) into a mathematical function $f(n)$, which describes the algorithm's performance as the input size $n$ grows. Instead of executing the code, we perform static analysis by identifying the fundamental structure of the loops:
- **Sequential Statements**: Time adds up ($O(1) + O(1) = O(1)$).
- **Independent Loops**: Time scales linearly ($O(n)$).
- **Nested Loops**: Time multiplies ($O(n) \times O(n) = O(n^2)$).
- **Logarithmic Loops**: The loop counter doubles or halves at each step ($O(\log n)$).

### Example
Think of calculating complexity like estimating the time to read a library. 
- Reading one specific book's title on a shelf is a **Sequential Statement** ($O(1)$).
- Scanning every book on one shelf is a **Linear Loop** ($O(n)$).
- If for *every* book on the shelf you must also check *every* page in the book, that is a **Nested Loop** ($O(n \times m)$).

### Applications & Use Cases
- **Compiler Optimization**: Modern compilers like GCC or Clang analyze the complexity of loops to decide whether to unroll them for hardware acceleration.
- **API Rate Limiting & Backend Design**: When engineers build REST APIs, they must calculate the complexity of their database queries. An $O(n^2)$ nested loop to match users with their transactions will crash the backend server when millions of users hit the API at the same time.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Dependent Nested Loops (Triangular Loop)
**Problem:** Calculate the time complexity of the following dependent nested loops.
```text
count = 0
for i = 1 to n do:
    for j = 1 to i do:
        count = count + 1
```
**Step-by-step Solution:**
1. Notice that the inner loop's bound depends on the outer loop's current value `i`.
2. When `i=1`, inner loop runs 1 time.
3. When `i=2`, inner loop runs 2 times.
4. When `i=n`, inner loop runs $n$ times.
5. The total number of times `count = count + 1` executes is the sum of the first $n$ integers:
   $$\text{Total Executions} = 1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2} = \frac{n^2 + n}{2}$$
6. Dropping the constants and lower-order terms, the time complexity is $O(n^2)$.

### Example 2: Logarithmic Stepped Loop
**Problem:** Calculate the time complexity of a loop where the iterator multiplies.
```text
i = 1
while i < n do:
    print(i)
    i = i * 3
```
**Step-by-step Solution:**
1. Let's trace the value of `i` at each step $k$.
2. Step 0: $i = 1 = 3^0$
3. Step 1: $i = 3 = 3^1$
4. Step 2: $i = 9 = 3^2$
5. Step $k$: $i = 3^k$
6. The loop stops when $i \ge n$, meaning $3^k \ge n$.
7. Solving for $k$ (the number of steps), we take the base-3 logarithm of both sides:
   $k \ge \log_3(n)$
8. Since logarithms of different bases only differ by a constant multiplier ($\log_3(n) = \frac{\log_2(n)}{\log_2(3)}$), we ignore the base in Big-O notation. The time complexity is $O(\log n)$.

### Example 3: Mixed Independent and Dependent Loops
**Problem:** Calculate the overall time complexity of this code block.
```text
// Loop Block A
for i = 1 to n do:
    for j = 1 to n do:
        x = x + 1

// Loop Block B
k = n
while k > 1 do:
    k = k / 2
```
**Step-by-step Solution:**
1. **Analyze Loop Block A**: 
   The outer loop runs $n$ times. The inner loop runs exactly $n$ times for *every* outer loop iteration. 
   Total executions for Block A = $n \times n = n^2$. Thus, $T_A(n) = O(n^2)$.
2. **Analyze Loop Block B**:
   The loop variable `k` starts at $n$ and halves at every step until it reaches 1. 
   The sequence of values is $n, n/2, n/4, \dots, n/2^m$.
   The loop stops when $n/2^m \le 1 \implies 2^m \ge n \implies m \ge \log_2(n)$.
   Total executions for Block B = $\log_2(n)$. Thus, $T_B(n) = O(\log n)$.
3. **Combine Complexities**:
   Since the blocks run sequentially (one after the other), we add their complexities.
   $T(n) = T_A(n) + T_B(n) = O(n^2) + O(\log n)$.
4. According to the rules of asymptotic notation, we only keep the fastest-growing term. Since $n^2$ grows much faster than $\log n$, the final complexity is $O(n^2)$.

---

### Previous Year Questions & Solutions

1. **"Analyse the complexity of the following function..." [July 2021]**
   - **Solution:** To analyze any given function, follow the static analysis approach outlined in **Section 1**. Identify independent loops ($O(N)$), nested dependent loops ($O(N^2)$), and logarithmic stepped loops ($O(\log N)$). Combine them by taking the highest-order term. See **Examples 1, 2, and 3** for standard loop trace solutions.

2. **"Express the return value of the function "mystery" in theta - notation." [September 2020]**
   - **Solution:** The Theta ($\Theta$) notation requires calculating both the upper bound ($O$) and the lower bound ($\Omega$). Trace the loop iterations of the `mystery` function mathematically. If the loop invariably executes $\frac{n(n-1)}{2}$ times (like Example 1), the exact return value scales strictly quadratically, making it $\Theta(n^2)$.
