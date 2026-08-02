# Module 1 — Topic 1: Time and Space Complexity & Elementary Operations

> **Module 1**: Introduction to Algorithm Analysis & Recurrences  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### 1.1 What is an Algorithm?
Imagine you are following a recipe to bake a cake. The recipe gives you exact, step-by-step instructions. If the instructions are vague, you might end up with a ruined cake. In computer science, an **algorithm** is just like a strict recipe for a computer: a clear, step-by-step set of instructions to convert a given **input** into a desired **output**.

To be a valid algorithm, five basic rules must be satisfied:
1. **Input**: It receives zero or more values from the outside world.
2. **Output**: It produces at least one result.
3. **Definiteness**: Every step is completely clear and has only one meaning.
4. **Finiteness**: It must eventually stop after a finite number of steps (it cannot run forever in an infinite loop).
5. **Effectiveness**: Every instruction must be simple enough to be done by hand with pencil and paper.

---

### 1.2 Why Do We Analyze Algorithms?
Suppose two programmers are asked to write a program to search for a user's ID in a database of 1 million users:
- **Programmer A** checks every user from the beginning to the end one by one.
- **Programmer B** uses a smart binary search that repeatedly cuts the search area in half.

If we test both programs on a supercomputer with 5 users, both will run instantly. But on a phone with 1 million users:
- Programmer A's code might take **1 million steps**.
- Programmer B's code takes only **20 steps** ($\log_2(1,000,000) \approx 20$).

**Algorithm Analysis** is the mathematical tool that lets us compare the efficiency of different solutions **on paper** before spending hours writing and testing code. It tells us how the running time and memory footprint will grow as the input size $n$ gets larger.

---

### 1.3 Time Complexity and Space Complexity

#### Time Complexity
**Time Complexity** is a measure of how the total running time of an algorithm grows as the size of the input data ($n$) increases. We measure time not in clock seconds (which depend on how fast your laptop CPU is), but in the **number of basic operations** executed.

#### Space Complexity
**Space Complexity** measures how much extra memory (RAM) an algorithm needs to run to completion as a function of input size $n$.

Memory needed by an algorithm comes in two parts:
$$\text{Total Space } S(n) = \text{Fixed Space} + \text{Auxiliary Space}$$

1. **Fixed Space**: Memory needed for the code instructions, simple constants, and simple variables. This memory does not change when the input grows larger.
2. **Auxiliary Space**: Temporary memory created while running the program, such as new arrays allocated on the heap or function call records saved on the stack during recursion.

```
+-------------------------------------------------------------+
|                      Total Memory S(n)                      |
+------------------------------------+------------------------+
|             Fixed Space            |    Auxiliary Space     |
| (Program code, fixed constants)    | (New arrays, recursion |
|                                    |   call stack frames)   |
+------------------------------------+------------------------+
```

---

### 1.4 The Computer Model: Random Access Machine (RAM)
To analyze algorithms fairly without worrying about whether you are running Mac, Windows, or Linux, computer scientists use a simplified model called the **Random Access Machine (RAM) model**:
- **One step at a time**: Instructions run sequentially, one after another (no multi-core parallelism).
- **Constant Cost for Basic Steps ($O(1)$)**: Simple operations take 1 unit of time:
  - Math: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`).
  - Logic & Checks: comparing numbers (`a < b`), boolean AND/OR.
  - Memory: reading or writing to a variable or array slot (`A[i] = x`).
- **Equal Access Speed**: Reading any memory location takes the exact same amount of time regardless of where it is stored.

---

## 2. Elementary Operations & Frequency Count Method

An **elementary operation** is a single basic action that takes a constant amount of time (1 unit of work). 

The **Frequency Count Method** calculates total time complexity by adding up how many times each line of code runs:

$$\text{Total Time } T(n) = \sum (\text{Cost of Line}) \times (\text{How many times line executes})$$

### Step-Count Walkthrough: Array Sum
Let me analyze a simple function that adds up $n$ numbers in an array:

```python
def compute_sum(A, n):
    total = 0            # Line 1: Runs 1 time
    for i in range(n):   # Line 2: Checks condition (n + 1) times
        total += A[i]    # Line 3: Runs n times
    return total         # Line 4: Runs 1 time
```

| Line | Statement | Cost per execution | Frequency (Times executed) | Total Line Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Line 1** | `total = 0` | $c_1$ | $1$ | $c_1$ |
| **Line 2** | `for i in range(n)` | $c_2$ | $n + 1$ *(extra check to stop)* | $c_2(n + 1)$ |
| **Line 3** | `total += A[i]` | $c_3$ | $n$ | $c_3 n$ |
| **Line 4** | `return total` | $c_4$ | $1$ | $c_4$ |

Adding up the total cost:
$$T(n) = c_1 + c_2(n+1) + c_3 n + c_4 = (c_2 + c_3)n + (c_1 + c_2 + c_4) = a \cdot n + b$$

Since $a \cdot n + b$ grows linearly with $n$, the time complexity is **linear**, written as $O(n)$ or $\Theta(n)$.
