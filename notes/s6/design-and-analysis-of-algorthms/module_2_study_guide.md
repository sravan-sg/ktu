# Module II: Asymptotic Analysis and Advanced Data Structures - Extended Study Guide

> [!NOTE]
> This is a comprehensive, textbook-level deep dive into Module II of the CS302 Design and Analysis of Algorithms syllabus. It provides rigorous mathematical definitions, exhaustive step-by-step algorithms, and detailed structural mechanics for advanced data structures.

---

## 1. Asymptotic Notations and Properties (Deep Dive)

### Detailed Explanation

asymptotic notations are mathematical tools used to describe the performance or complexity of an algorithm (usually time or space) as the input size ($n$) grows toward infinity.

#### Growth Rate
*   **What it means:** The growth rate (or order of growth) dictates how an algorithm's resource consumption (like time or space) scales with the size of the input. Comparing growth rates is the fundamental goal of asymptotic analysis.
*   **Common Growth Rates (from slowest to fastest growing):**
    *   **$O(1)$ - Constant:** Execution time does not change with input size. (e.g., Array index access)
    *   **$O(\log n)$ - Logarithmic:** Execution time increases very slowly. (e.g., Binary Search)
    *   **$O(n)$ - Linear:** Execution time increases directly proportional to input size. (e.g., Linear Search)
    *   **$O(n \log n)$ - Linearithmic:** Typical for optimal comparison-based sorting. (e.g., Merge Sort)
    *   **$O(n^2)$ - Quadratic:** Execution time grows with the square of the input size. (e.g., Bubble Sort)
    *   **$O(2^n)$ - Exponential:** Execution time doubles with each addition to input size. (e.g., Naive Recursive Fibonacci)
    *   **$O(n!)$ - Factorial:** Execution time grows unimaginably fast. (e.g., Traveling Salesperson brute force)

#### The Big-O Notation ($O$) - Asymptotic Upper Bound
*   **What it means:** It defines the worst-case scenario. It represents the maximum time an algorithm could possibly take to run.
*   **Analogy:** "I will finish grading these exams in no more than 5 hours." (It might take 2 hours, but it will absolutely not take more than 5).
*   **Example:** Searching for a specific number in an unsorted array of size $n$ takes $O(n)$ time because, in the absolute worst case, the number is at the very end of the array, and you have to check every single element

#### The Big-Omega Notation ($\Omega$) - Asymptotic Lower Bound
*   **What it means:** It defines the best-case scenario. It represents the minimum amount of time an algorithm will take.
*   **Analogy:** "It will take me at least 1 hour to grade these exams."
*   **Example:** In that same unsorted array search, the best-case scenario is finding the number on the very first try. The time complexity is $\Omega(1)$ (constant time).

#### The Big-Theta Notation ($\Theta$) - Asymptotically Tight Bound
*   **What it means:** It defines the exact growth rate. You can only use Big-Theta if the upper bound ($O$) and the lower bound ($\Omega$) are exactly the same. It means the algorithm will always take this specific amount of time, regardless of the best or worst cases.
*   **Analogy:** "It will take me exactly 3 hours to grade these exams."
*   **Example:** Printing every element in an array of size $n$ requires visiting every single item every time. The worst case is $n$ steps, and the best case is $n$ steps. Therefore, the exact time complexity is $\Theta(n)$.

### Applications & Use Cases
*   **Software Engineering SLA (Service Level Agreements):** When designing a high-frequency trading platform, engineers use worst-case Big-O bounds to mathematically guarantee that a trade order will be processed within micro-seconds regardless of the queue size.
*   **Database Query Optimization:** Database engines use asymptotic bounds to estimate the cost of different query execution plans and select the one with the lowest Big-O complexity.

**refference video:** https://youtu.be/b8Rc9INn6wY?si=-2hKLn2YaQCe5Sxq

*   **Big O notation** can definitely look like a confusing alphabet soup at first glance, but it is just a way for programmers to talk about how a piece of code scales when it gets a lot of data.Let's break down the mathematical terms into plain English.The Core Players: $n$, $f(n)$, and $g(n)$Imagine you are throwing a party and need to wash the dishes afterward.$n$ (The Input Size): This is the amount of data your code has to process. In our analogy, $n$ is the number of guests.$f(n)$ (The Actual Time): This is the exact number of steps your algorithm takes to finish the job. In reality, $f(n)$ is often a messy, complicated equation (like $3n^2 + 5n + 2$) because it accounts for every little detail, like setting up the soap or drying the plates.$g(n)$ (The Benchmark): This is a clean, simplified mathematical category (like $n$, $n^2$, or $\log n$). When input sizes get huge, the small details (like the $+ 5n + 2$) stop mattering. We use $g(n)$ to categorize the general "shape" of how $f(n)$ grows.The Greek Letters: Upper, Lower, and Tight BoundsWhen programmers compare the messy reality ($f(n)$) to the clean benchmark ($g(n)$), they use three main symbols to set expectations.1. Big O ($O$) — The Upper Bound (Worst-Case)What it means: "My code will run no slower than this."How it's used: If your algorithm is $O(g(n))$, it means that as your data grows, your actual time $f(n)$ will always stay beneath a ceiling created by $g(n)$. This is the most common term because engineers generally want to know the absolute worst-case scenario before deploying code. 
*   **Big Omega ($\Omega$)** — The Lower Bound (Best-Case)What it means: "My code will run no faster than this."How it's used: If your algorithm is $\Omega(g(n))$, it means your actual time $f(n)$ will never drop below the floor created by $g(n)$. Even if you get incredibly lucky with your data, it will still take at least this much time.
*   **Big Theta ($\Theta$)** — The Tight Bound (Exact Scaling)What it means: "My code scales exactly like this."How it's used: If your algorithm is $\Theta(g(n))$, it means $f(n)$ is sandwiched perfectly. Both the worst-case ceiling ($O$) and the best-case floor ($\Omega$) grow at the exact same rate. It gives you a highly accurate picture of performance.Here is an interactive visualization so you can see how an actual algorithm ($f(n)$) is "trapped" by these boundaries ($g(n)$) as the input size grows.
**refference document :** https://share.gemini.google/LBNZ2U6wFRuT



### 3 Solved Analytical Examples    
**Example 1: Rigorous proof that $3n^3 + 2n^2 \neq O(n^2)$.**
1. Assume the opposite: Suppose $3n^3 + 2n^2 \le c \cdot n^2$ for some constants $c > 0$ and all $n \ge n_0$.
2. Divide the entire inequality by $n^2$ (since $n > 0$).
3. We get: $3n + 2 \le c$.
4. Is it possible for $3n + 2$ to be less than or equal to a fixed constant $c$ for *all* large $n$? No. As $n \to \infty$, $3n + 2 \to \infty$, which will eventually exceed any finite constant $c$.
5. Therefore, the assumption is false. $3n^3 + 2n^2 \neq O(n^2)$.

**Example 2: Find tight bounds ($\Theta$) for $\log(n!)$.**
1. We use Stirling's Approximation or mathematical bounds.
2. **Upper Bound:** $n! = n \times (n-1) \times ... \times 1 \le n \times n \times ... \times n = n^n$. Thus, $\log(n!) \le \log(n^n) = n \log n$. So, $\log(n!) = O(n \log n)$.
3. **Lower Bound:** Consider the upper half of the terms in $n!$.
   $n! \ge (n/2) \times (n/2 + 1) \times ... \times n \ge (n/2)^{n/2}$.
   Thus, $\log(n!) \ge \log((n/2)^{n/2}) = (n/2) \log(n/2) = (n/2)(\log n - 1)$.
   For large $n$, $(n/2)(\log n - 1)$ grows proportionally to $n \log n$. So, $\log(n!) = \Omega(n \log n)$.
4. **Result:** Since it is both $O(n \log n)$ and $\Omega(n \log n)$, $\log(n!) = \Theta(n \log n)$.

**Example 3: Prove the transitivity of Big-O.**
1. Given $f(n) = O(g(n))$, there exist $c_1, n_1$ such that $f(n) \le c_1 g(n)$ for $n \ge n_1$.
2. Given $g(n) = O(h(n))$, there exist $c_2, n_2$ such that $g(n) \le c_2 h(n)$ for $n \ge n_2$.
3. Let $n_0 = \max(n_1, n_2)$. For all $n \ge n_0$, both inequalities hold.
4. Substitute $g(n)$ in the first inequality: $f(n) \le c_1 (c_2 h(n)) = (c_1 c_2) h(n)$.
5. Let $c_3 = c_1 c_2$. We have $f(n) \le c_3 h(n)$ for $n \ge n_0$.
6. **Result:** $f(n) = O(h(n))$.







## 2. Master's Theorem (Extended)

**refference video:**   https://youtu.be/BnbFEoEReiY?si=GQsZuhfi_fwuOnSp

### Detailed Explanation
The Master Theorem is derived from analyzing the recursion tree of the recurrence $T(n) = aT(n/b) + f(n)$.
*   **Tree Height:** $\log_b n$
*   **Number of Leaves:** $a^{\log_b n} = n^{\log_b a}$
*   **Work at the Leaves:** $\Theta(n^{\log_b a})$
*   **Work at Internal Nodes:** Evaluated by $f(n)$.

The theorem compares the work done at the root ($f(n)$) with the work done at the leaves ($n^{\log_b a}$).
*   **Case 1 (Heavy Leaves):** If the leaves do polynomially more work, the total time is determined by the leaves: $\Theta(n^{\log_b a})$.
*   **Case 2 (Evenly Distributed):** If work is equal across all levels, we multiply the work per level by the height of the tree ($\log n$): $\Theta(n^{\log_b a} \log^{k+1} n)$.
*   **Case 3 (Heavy Root):** If the root does polynomially more work, the total time is bounded by the root's work: $\Theta(f(n))$. *Requires regularity condition: $a f(n/b) \le c f(n)$ for $c < 1$.*

### 3 Solved Numerical Examples
**Example 1: Solve Strassen's Matrix Multiplication Recurrence $T(n) = 7T(n/2) + O(n^2)$.**
1. Identify constants: $a=7$ (7 recursive multiplications), $b=2$ (submatrices are half the size), $f(n) = n^2$ (addition operations).
2. Calculate leaf work: $n^{\log_b a} = n^{\log_2 7} \approx n^{2.81}$.
3. Compare: $f(n) = n^2$. We see that $n^2 = O(n^{2.81 - \epsilon})$ for $\epsilon = 0.81 > 0$.
4. This strictly matches **Case 1**.
5. **Result:** $T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.81})$.

**Example 2: Solve $T(n) = 2T(n/2) + \frac{n}{\log n}$.**
1. Identify constants: $a=2, b=2, f(n) = n \log^{-1} n$.
2. Calculate leaf work: $n^{\log_2 2} = n^1 = n$.
3. Compare: $f(n) = n \log^{-1} n$. This takes the form of Case 2 where $f(n) = \Theta(n^{\log_b a} \log^k n)$.
4. Here, $k = -1$.
5. *Special Sub-case of Master Theorem:* If $k = -1$, the sum is a harmonic series, and the result integrates to a $\log \log n$ factor.
6. **Result:** $T(n) = \Theta(n \log \log n)$.

**Example 3: Solve $T(n) = 4T(n/2) + n^3$.**
1. Identify constants: $a=4, b=2, f(n) = n^3$.
2. Calculate leaf work: $n^{\log_2 4} = n^2$.
3. Compare: $f(n) = n^3$. We see that $f(n) = \Omega(n^{2 + \epsilon})$ for $\epsilon = 1 > 0$.
4. Regularity check: Does $a f(n/b) \le c f(n)$?
   $4(n/2)^3 = 4(n^3/8) = (1/2)n^3$.
   This is $\le c n^3$ for $c = 1/2 < 1$. Condition holds.
5. This matches **Case 3**.
6. **Result:** $T(n) = \Theta(n^3)$.

---

## 3. AVL Trees (Rigorous Rotations)
### Why we usw al trees:https://share.gemini.google/TlZR04z0loAa
### Detailed Explanation
AVL trees enforce balance rigidly. A node contains: `Key`, `LeftChild`, `RightChild`, and `Height`.
The balance factor $BF = Height(Left) - Height(Right)$. Valid BFs are -1, 0, 1. If $BF$ becomes 2 or -2 after an insertion or deletion, a rotation is required.

**refference video :** https://youtu.be/YWqla0UX-38?si=OrzYuSC4Iu-I0CNC 
**The Four Rotations Details:**
1.  **LL (Left-Left) Imbalance:** Node X has BF=2, and its left child Y has BF=1 or 0.
    *   *Action:* **Right Rotation** around X. Y becomes the new root of the subtree, X becomes Y's right child. Y's original right child becomes X's new left child.
2.  **RR (Right-Right) Imbalance:** Node X has BF=-2, and its right child Y has BF=-1 or 0.
    *   *Action:* **Left Rotation** around X. Y becomes the new root, X becomes Y's left child.
3.  **LR (Left-Right) Imbalance:** Node X has BF=2, and its left child Y has BF=-1.
    *   *Action:* **Left-Right Rotation**. First, Left Rotate around Y (making the tree an LL imbalance). Second, Right Rotate around X.
4.  **RL (Right-Left) Imbalance:** Node X has BF=-2, and its right child Y has BF=1.
    *   *Action:* **Right-Left Rotation**. First, Right Rotate around Y. Second, Left Rotate around X.

### Applications & Use Cases
*   **Virtual Memory Areas:** In earlier Linux kernels, process memory maps (vm_area_struct) were managed using AVL trees to allow fast searching of unallocated memory regions.

### 3 Solved Analytical Examples
**refference link :**  https://share.gemini.google/zDTjV65q3aux
**Example 1: Construct an AVL tree by inserting 50, 25, 10, 5, 7.**
1.  Insert 50 (BF 0).
2.  Insert 25 (BF 1 at 50).
3.  Insert 10 (BF 2 at 50). **LL Imbalance.** Right Rotate around 50. Tree: 25(root) -> 10(L), 50(R).
4.  Insert 5. Attaches to 10. (Tree balanced).
5.  Insert 7. Attaches to 5. Path from 25 is 10 -> 5 -> 7. Node 10 has BF=2. Node 5 has BF=-1. **LR Imbalance at 10.**
    *   Left Rotate around 5: Tree becomes 10 -> 7 -> 5.
    *   Right Rotate around 10: 7 becomes root of subtree, 5 is L, 10 is R.
6.  **Final Tree:** 25(root), L-child: 7 (which has children 5, 10), R-child: 50.

**Example 2: Deletion causing a rebalance.**
1.  Take the Final Tree from Example 1. Delete 50.
2.  Node 25 now has a Left subtree of height 2 and a Right subtree of height 0. BF(25) = 2.
3.  Look at Left child (7). Its BF is 0 (heights of 5 and 10 are both 1).
4.  This is an **LL Imbalance** (when child BF is 0, we treat it as LL or RR depending on the side).
5.  Right Rotate around 25.
6.  **Final Tree:** 7 becomes the new overall root. L-child: 5. R-child: 25 (with L-child 10).

**Example 3: Time Complexity Proof for AVL Tree Search.**
1.  Let $N(h)$ be the minimum number of nodes in an AVL tree of height $h$.
2.  $N(h) = N(h-1) + N(h-2) + 1$.
3.  This closely relates to the Fibonacci sequence. It can be proven that $N(h) > F_{h+2} - 1$, where $F_i$ is the $i^{th}$ Fibonacci number.
4.  Since $F_h \approx \frac{1}{\sqrt{5}} \phi^h$ (where $\phi \approx 1.618$ is the golden ratio).
5.  $N > c \cdot 1.618^h$. Taking the log base 1.618 of both sides yields $h < 1.44 \log_2 N$.
6.  **Result:** The maximum height is tightly bounded by $1.44 \log_2 N$, proving that search operations are strictly $O(\log n)$.

---

## 4. Red-Black Trees (Deep Mechanics)
**refference link :** https://share.gemini.google/3xkCduVNCwcG

**refference video :** https://youtu.be/3RQtq7PDHog?si=zGbRxNMSiY7gR5Re

### Detailed Explanation
Red-Black trees use colors to maintain approximate balance. The longest path from root to leaf is no more than twice the length of the shortest path.
**Insertion Rules (Always insert as RED):**
Let $Z$ be the new node.
*   **Case 0:** $Z$ is root $\to$ color it BLACK.
*   **Case 1:** $Z$'s uncle is RED $\to$ Recolor Parent, Uncle to BLACK. Recolor Grandparent to RED. Move $Z$ pointer up to Grandparent and repeat.
*   **Case 2:** $Z$'s uncle is BLACK (Triangle shape) $\to$ Perform a rotation on Parent to transform into a "Line" shape (Case 3).
*   **Case 3:** $Z$'s uncle is BLACK (Line shape) $\to$ Perform a rotation on Grandparent. Swap colors of Parent and Grandparent.

### Applications & Use Cases
*   **Java's `TreeMap` and `TreeSet`:** Implemented internally using Red-Black trees because they guarantee $O(\log n)$ performance and suffer fewer rotation penalties on insertion than AVL trees.

### 3 Solved Analytical Examples
**refference video for deletion  :**https://youtu.be/CTvfzU_uNKE?si=EkzmM3zbgc3QwcTh
**refference video for insertion  :**https://share.gemini.google/SFAiIF4gt0pZ
**Example 1: Trace insertions: 10, 20, 30, 15.**
1.  Insert 10: Root, color Black. [10(B)]
2.  Insert 20: RED. [10(B) -> 20(R)]
3.  Insert 30: RED. [10(B) -> 20(R) -> 30(R)]. Parent(20) is RED, Uncle(NULL) is BLACK. **Case 3 (Line)**.
    *   Rotate Left around 10. Recolor 20 to B, 10 to R.
    *   Tree: 20(B) root. Children: 10(R), 30(R).
4.  Insert 15: RED, right child of 10. Parent(10) is RED. Uncle(30) is RED. **Case 1**.
    *   Recolor Parent(10) to B, Uncle(30) to B, Grandparent(20) to R.
    *   Check root: 20 is root, must be BLACK. Force 20 to B.
    *   Tree: 20(B). Children: 10(B), 30(B). 10 has child 15(R).

**Example 2: Complex Rotation (Triangle to Line).**
1.  Continuing from Example 1, insert 18.
2.  Goes left of 20, right of 10, right of 15.
3.  Tree branch: 10(B) -> 15(R) -> 18(R).
4.  Parent(15) is RED, Uncle(NULL, left of 10) is BLACK.
5.  This forms a Right-Left "Triangle". **Case 2**.
6.  Rotate Left around 15. The branch becomes 10(B) -> 18(R)->15(R) (where 15 is left child of 18).
7.  Now it's a "Line" (**Case 3**).
8.  Rotate Right around 10. Recolor 18 to B, 10 to R.
9.  Final Subtree under 20: 18(B) is the child, with children 10(R) and 15(R).

**Example 3: Prove that the path from root to farthest leaf is at most twice the shortest path.**
1.  By Property 5, every path has the same number of Black nodes, say $B$.
2.  The shortest possible path consists entirely of Black nodes. Length = $B$.
3.  By Property 4, no two Red nodes can be adjacent. The maximum number of Red nodes you can pack into a path without placing two together is by alternating: Black-Red-Black-Red...
4.  The longest path with $B$ Black nodes and alternating Red nodes has $B$ Red nodes. Length = $2B$.
5.  **Result:** Longest Path ($2B$) $\le 2 \times$ Shortest Path ($B$).

---

## 5. B-Trees (Disk-Oriented Structures)
**refference link :**https://share.gemini.google/LtvSNjSineq8
**refference video (basic introduction):**https://youtu.be/aZjYr87r1b8?si=US97F_Ks8OaCLA27
### Detailed Explanation
In the Design and Analysis of Algorithms (DAA), we often study trees like AVL Trees and Red-Black Trees. These are excellent $O(\log n)$ data structures when your entire dataset fits into your computer's lightning-fast RAM (Primary Memory).
However, DAA also forces us to think about the physical limitations of hardware. What happens when your dataset is so massive (like a database of 1 billion users) that it has to be stored on a Hard Drive (Secondary Storage)?
The Problem: Disk Access is Slow
Reading data from a physical hard drive is incredibly slow compared to RAM.
If you put a standard binary search tree on a hard drive, finding a record out of 1 billion might require traveling down 30 levels of the tree. That means 30 separate, slow "disk reads." The system would lag terribly.
The Solution: The B-Tree ("Short and Fat")
Instead of reading one single node at a time, a computer reads from a disk in large chunks called "Blocks" or "Pages."
A B-Tree is designed to perfectly match this hardware quirk. Instead of being a "tall and skinny" binary tree (with 2 children per node), a B-Tree is a multi-way tree that is "short and fat."
Massive Nodes: A single B-Tree node is exactly the size of a disk block.
Hundreds of Keys: Because the node is so big, it can hold hundreds of keys inside it (e.g., [10, 25, 40, 89...]).
Hundreds of Children: A node holding 100 keys will have 101 child pointers!

Because it branches out so widely, a B-Tree rarely gets deeper than 3 or 4 levels. You can search through billions of records and mathematically guarantee that it will take no more than 3 or 4 slow disk accesses.
A B-Tree is parameterized by its minimum degree $t \ge 2$.
*   Every node (other than root) must have at least $t-1$ keys.
*   Every node can have at most $2t-1$ keys.
*   An internal node with $k$ keys has $k+1$ children.

**Insertion (Proactive Splitting):**
To avoid a situation where a leaf overflows and causes a cascading split all the way to the root, B-trees usually perform proactive splitting. As we traverse down the tree to find the insertion point, if we encounter ANY node that is full ($2t-1$ keys), we immediately split it. This guarantees that when we reach the leaf, there will be room to insert.\
**refference video (insertion and deletion):**https://youtu.be/ownO77M4SWI?si=aWBYgmIROEtIDYVq


### Applications & Use Cases
*   **Database Clustered Indexes:** Standard implementation for indexing large volumes of data on SSDs/HDDs. Because sequential disk reads are fast and random access is slow, fitting an entire B-Tree node into a single 8KB disk sector minimizes random I/O head movements.

### 3 Solved Analytical Examples
**Example 1: Insert 10, 20, 30, 40, 50, 60 into an empty B-tree with $t=2$ (Max keys = 3).**
1.  Insert 10, 20, 30. Root node fills up: `[10, 20, 30]`.
2.  Insert 40. Root is full. Split root `[10, 20, 30]`. Median 20 goes up.
    *   New Root: `[20]`. Children: `[10]` and `[30]`.
    *   40 goes to the right child. Right child becomes `[30, 40]`.
3.  Insert 50. Goes to right child. Right child is full: `[30, 40, 50]`.
    *   Wait, the maximum is 3 keys ($2t-1 = 3$). Actually, `[30, 40, 50]` is full.
    *   Split it. 40 goes up to the root. Root becomes `[20, 40]`.
    *   Children become: `[10]`, `[30]`, `[50]`.
4.  Insert 60. Goes to rightmost child. Right child becomes `[50, 60]`.

**Example 2: Splitting a full Root.**
1.  Assume a B-tree with $t=3$ (Max keys = 5). Root is `[10, 20, 30, 40, 50]`.
2.  We want to insert 25.
3.  Because the root is full, we must proactively split it BEFORE traversing down.
4.  Split `[10, 20, 30, 40, 50]`. The median is 30.
5.  Create a new empty root. Promote 30 to it.
6.  The new root is `[30]`. It has two children: `[10, 20]` and `[40, 50]`.
7.  Now, compare 25 with 30. Go to the left child `[10, 20]`.
8.  Insert 25. Left child becomes `[10, 20, 25]`.

**Example 3: Calculate the maximum height of a B-Tree of degree $t$ with $N$ keys.**
1.  The root contains at least 1 key and has at least 2 children.
2.  Level 1 has at least 2 nodes, each with at least $t-1$ keys and $t$ children.
3.  Level 2 has at least $2t$ nodes.
4.  Level $h$ (leaves) has at least $2t^{h-1}$ nodes.
5.  Total keys $N \ge 1 + (t-1) \sum_{i=1}^{h} 2t^{i-1} = 1 + 2(t-1) \left[ \frac{t^h - 1}{t - 1} \right] = 1 + 2(t^h - 1)$.
6.  Solving for $h$: $t^h \le \frac{N+1}{2}$.
7.  **Result:** $h \le \log_t \left( \frac{N+1}{2} \right)$.

---

## 6. Disjoint Sets (Union-Find)

### Detailed Explanation
**refference link :**https://share.gemini.google/OrRAKUhINbvq
**refference video :** https://youtu.be/wU6udHRIkcc?si=k7Iyn2_j3Opw0wUr
Disjoint sets are beautifully simple yet mathematically profound. Represented as an array `parent[]` where `parent[i]` is the parent of element `i`. If `parent[i] == i`, `i` is the root of its set.

**Optimizations:**
1.  **Union by Rank:** We maintain a `rank[]` array (which approximates the height of the tree). When unioning two roots, the one with the smaller rank is made a child of the one with the larger rank. If ranks are equal, one is chosen arbitrarily, and its rank increases by 1.
2.  **Path Compression:** Inside the `find(x)` function, as we recursively traverse up to find the root, we update the parent pointer of every node along the path to point *directly* to the root.

With both optimizations, operations take $O(\alpha(n))$ amortized time, where $\alpha(n)$ is the inverse Ackermann function. $\alpha(n) \le 4$ for any computationally feasible value of $n$ (even greater than the number of atoms in the universe), making it effectively $O(1)$.

### Applications & Use Cases
*   **Network Connectivity:** Dynamically adding connections between computers in a network and querying if two specific computers can communicate.

### 3 Solved Analytical Examples
**Example 1: Initializing and Unioning.**
1.  Elements: 0, 1, 2, 3, 4. Initialize `parent = [0, 1, 2, 3, 4]`, `rank = [0, 0, 0, 0, 0]`.
2.  `Union(0, 1)`. Ranks are equal (0). Make 1 a child of 0. `parent = [0, 0, 2, 3, 4]`. `rank[0] = 1`.
3.  `Union(2, 3)`. Ranks are equal (0). Make 3 a child of 2. `parent = [0, 0, 2, 2, 4]`. `rank[2] = 1`.
4.  `Union(0, 2)`. Both are roots. Ranks are equal (1). Make 2 a child of 0. `parent = [0, 0, 0, 2, 4]`. `rank[0] = 2`.

**Example 2: Path Compression mechanics.**
1.  Using the array from Example 1: `parent = [0, 0, 0, 2, 4]`.
2.  Element 3 points to 2, which points to 0. Tree: 0 -> 2 -> 3.
3.  Call `Find(3)`.
    *   `find(3)` sees `parent[3] != 3`. It calls `find(2)`.
    *   `find(2)` sees `parent[2] != 2`. It calls `find(0)`.
    *   `find(0)` sees `parent[0] == 0`. Returns 0.
4.  As the recursion unwinds:
    *   `find(2)` sets `parent[2] = 0` (unchanged).
    *   `find(3)` sets `parent[3] = 0` (updated!).
5.  **Result:** `parent` array becomes `[0, 0, 0, 0, 4]`. Node 3 now points directly to root 0.

**Example 3: Kruskal's Algorithm integration.**
1.  Given edges: (1-2, weight 5), (2-3, weight 2), (1-3, weight 8).
2.  Sort edges by weight: (2-3), (1-2), (1-3).
3.  Initialize Disjoint Set for vertices {1, 2, 3}.
4.  Process (2-3, weight 2): `Find(2) != Find(3)`. Add edge to MST. `Union(2, 3)`.
5.  Process (1-2, weight 5): `Find(1) != Find(2)`. Add edge to MST. `Union(1, 2)`. All nodes are now in the same set.
6.  Process (1-3, weight 8): `Find(1) == Find(3)` (returns true, they are connected). Skip edge to avoid a cycle.
7.  **Result:** MST contains edges (2-3) and (1-2). Total weight = 7.
