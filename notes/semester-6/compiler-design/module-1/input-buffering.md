# Input Buffering

## 1. Explanation
In lexical analysis, reading the source program character by character from the hard drive (via system calls) is extremely slow and inefficient. To overcome this I/O bottleneck, **Input Buffering** is employed. The source code is read in large blocks into a buffer in main memory.

**Two-Buffer Scheme:**
A common implementation is the two-buffer scheme, where an array of size $2N$ (where $N$ is the size of a disk block, e.g., 4096 bytes) is used.
Two pointers are maintained:
1. **`lexemeBegin`:** Points to the beginning of the current lexeme being discovered.
2. **`forward`:** Scans ahead until a pattern match is found.

When the `forward` pointer reaches the end of the first buffer, the second buffer is loaded from disk. When it reaches the end of the second buffer, it wraps around to the beginning of the first buffer (which is reloaded).

**Sentinels:**
To avoid checking if the `forward` pointer has reached the end of a buffer on *every single character read*, a sentinel character (usually `EOF`) is placed at the end of each buffer half. This reduces the number of conditional branches in the inner loop of the scanner, significantly speeding up lexical analysis.

## 2. Example
Imagine a buffer of size $N=4$. We are reading `int sum = 0;`

```
Buffer 1: [ i ] [ n ] [ t ] [ EOF ]
Buffer 2: [   ] [ s ] [ u ] [ m ] [ EOF ]
```
1. `lexemeBegin` and `forward` start at `i`.
2. `forward` moves to `EOF`. The sentinel is hit!
3. The system intercepts the sentinel, loads ` sum` into Buffer 2, and moves `forward` to the space.
4. The lexeme `int` is identified. `lexemeBegin` is moved to match `forward`.

## 3. Applications & Use Cases
- **High-Performance Compilers:** Fast scanning is critical because lexical analysis often takes up to 50% of the total compilation time (since it is the only phase that looks at every single character).
- **Network Packet Processing / File Parsers:** Any system that streams large amounts of text (like a JSON parser or XML parser) uses similar double-buffering techniques to avoid stalling on disk or network I/O.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Number of tests without a sentinel**
*Problem:* If a lexeme is 50 characters long, how many checks does the `forward` pointer do without a sentinel vs with a sentinel?
*Solution:* 
Without sentinel: 2 checks per character (check for end-of-buffer AND check the character value). Total = 100 checks.
With sentinel: 1 check per character (check if it equals `EOF`). If it is `EOF`, then we do the end-of-buffer logic. Total = 50 + 1 (when it hits the sentinel) = 51 checks.
*Result:* Sentinels cut the inner loop branching overhead in half.

**Example 2: Lookahead**
*Problem:* Why does the scanner need a `forward` pointer that looks ahead of `lexemeBegin`?
*Solution:* The scanner often cannot determine the token without looking ahead. For example, in FORTRAN, `DO 5 I = 1.25` is an assignment to variable `DO5I`. The lexer doesn't know it's an assignment (and not a `DO` loop) until it sees the decimal point `.`. Therefore, `forward` must scan ahead while `lexemeBegin` anchors the start.

**Example 3: Buffer Wrap-around**
*Problem:* What happens if a single string literal or identifier is larger than the buffer size $N$?
*Solution:* The two-buffer scheme fails because the `forward` pointer will wrap around and overwrite the beginning of the lexeme where `lexemeBegin` is pointing. Modern lexers handle this by dynamically reallocating and growing the buffer if `forward - lexemeBegin > 2N`.

## 5. Previous Year Questions & Solutions
[December 2018]
**Question:** Explain the use of sentinels in input buffering. (4 marks)
**Solution:**
In lexical analysis, characters are read from a buffer using a `forward` pointer. Without a sentinel, the lexer must perform two tests for every character read:
1. Is the `forward` pointer at the end of the buffer?
2. What is the character pointed to by `forward`?

To optimize this, a sentinel character (a special character that cannot be part of the source program, usually `EOF`) is placed at the end of the buffer. By doing this, the lexer only needs to perform a single test in its inner loop: `if (*forward == EOF)`. If it matches, the lexer then does a secondary check to see if it's the end of the buffer or the actual end of the file. This simple optimization significantly speeds up the lexical analysis phase.
