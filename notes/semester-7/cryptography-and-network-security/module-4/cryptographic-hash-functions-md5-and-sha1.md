# Cryptographic Hash Functions: MD5 and SHA-1

## 1. Explanation
A **cryptographic hash function** $H$ is a mathematical algorithm that maps an arbitrary, variable-length block of data $M$ into a fixed-size bit string $h = H(M)$, called the **message digest** or **hash value**.

### Essential Cryptographic Hash Requirements
According to William Stallings (*Cryptography and Network Security*, Chapter 11), to be cryptographically secure, a hash function $H$ must satisfy six core properties:
1. **Variable Input Size**: Can be applied to a block of data of any size.
2. **Fixed Output Size**: Produces a fixed-length output ($m$ bits).
3. **Efficiency (Ease of Computation)**: $H(x)$ is relatively easy to compute in hardware and software for any given $x$.
4. **Pre-image Resistance (One-Way Property)**: For any given code $h$, it is computationally infeasible to find an $x$ such that $H(x) = h$. Requires $2^m$ operations.
5. **Second Pre-image Resistance (Weak Collision Resistance)**: For any given block $x$, it is computationally infeasible to find $y \neq x$ such that $H(y) = H(x)$. Requires $2^m$ operations.
6. **Collision Resistance (Strong Collision Resistance)**: It is computationally infeasible to find *any* pair $(x, y)$ such that $x \neq y$ and $H(x) = H(y)$. Requires $2^{m/2}$ operations due to the Birthday Attack.

```
                   Arbitrary Length Message M
                               │
                               ▼
        ┌──────────────────────────────────────────────┐
        │   Cryptographic Hash Function H(M)           │
        │   (Iterated Compression Function -           │
        │    Merkle-Damgård Construction)              │
        └──────────────────────┬───────────────────────┘
                               │
                               ▼
             Fixed-Size Message Digest (e.g., 160 bits)
```

### The Birthday Attack
The Birthday Paradox demonstrates that in a group of just 23 randomly chosen people, the probability that at least two share the same birthday exceeds 50% ($P > 0.5$).
- In cryptography, if a hash function produces an $m$-bit digest, there are $2^m$ possible hash values.
- To find a collision (two messages $x \neq y$ with $H(x) = H(y)$), an attacker does not need to search $2^m$ values.
- By generating $k$ random messages, the number of distinct message pairs is $\binom{k}{2} = \frac{k(k-1)}{2} \approx \frac{k^2}{2}$.
- Setting the probability of a collision to $0.5$:
  $$1 - e^{-k^2 / (2 \cdot 2^m)} \ge 0.5 \implies k \approx \sqrt{2 \ln 2 \cdot 2^m} \approx 1.177 \sqrt{2^m} = 2^{m/2}$$
- Therefore, a 64-bit hash requires only $2^{32}$ operations to find a collision; a 128-bit hash (MD5) requires only $2^{64}$ operations.

### MD5 Message Digest Algorithm (RFC 1321)
Developed by Ron Rivest in 1991, MD5 processes 512-bit blocks and produces a **128-bit message digest** (represented by four 32-bit registers $A, B, C, D$).

#### Step-by-Step MD5 Algorithm
1. **Append Padding Bits**: The message is padded so that its length in bits is congruent to $448 \pmod{512}$. Padding consists of a single '1' bit followed by necessary '0' bits (1 to 512 bits of padding).
2. **Append Length**: A 64-bit unsigned integer representing the original message length modulo $2^{64}$ is appended. The total padded length is now an exact multiple of 512 bits ($L \times 512$).
3. **Initialize MD Buffer**: Four 32-bit registers initialized to standard hexadecimal constants:
   $$A = \text{0x67452301}, \ B = \text{0xEFCDAB89}, \ C = \text{0x98BADCFE}, \ D = \text{0x10325476}$$
4. **Process Message in 512-Bit Blocks (Compression Function)**:
   Each 512-bit block $Y_q$ is divided into sixteen 32-bit sub-words $X[0 \dots 15]$.
   The compression function consists of **4 rounds**, each having 16 operational steps (total 64 steps):
   - **Round 1**: $F(b, c, d) = (b \wedge c) \vee (\neg b \wedge d)$
   - **Round 2**: $G(b, c, d) = (b \wedge d) \vee (c \wedge \neg d)$
   - **Round 3**: $H(b, c, d) = b \oplus c \oplus d$
   - **Round 4**: $I(b, c, d) = c \oplus (b \vee \neg d)$
   Each step updates the registers using:
   $$a = b + ((a + \text{Func}(b, c, d) + X[k] + T[i]) \lll s)$$
   where $T[i] = \lfloor 2^{32} \cdot |\sin(i)| \rfloor$ is a sine-derived constant, and $\lll s$ denotes circular left shift.
   Registers are rotated cyclically: $(a, b, c, d) \rightarrow (d, a, b, c)$.
5. **Output**: After all $L$ blocks are processed, the registers $A, B, C, D$ are concatenated to produce the 128-bit digest.

### SHA-1 (Secure Hash Algorithm 1)
Standardized by NIST and NSA in 1995 (FIPS PUB 180-1), SHA-1 produces a **160-bit message digest** (five 32-bit registers $A, B, C, D, E$) from 512-bit blocks.

#### Step-by-Step SHA-1 Algorithm
1. **Padding & Length**: Identical to MD5. Padded with a '1' bit, followed by zeros to length $\equiv 448 \pmod{512}$, then 64-bit original length appended.
2. **Initialize Buffer**: Five 32-bit words:
   $$A = \text{0x67452301}, \ B = \text{0xEFCDAB89}, \ C = \text{0x98BADCFE}, \ D = \text{0x10325476}, \ E = \text{0xC3D2E1F0}$$
3. **Word Expansion**: The sixteen 32-bit words $W_0 \dots W_{15}$ of each 512-bit block are expanded into **80 words** ($W_0 \dots W_{79}$) via:
   $$W_t = (W_{t-3} \oplus W_{t-8} \oplus W_{t-14} \oplus W_{t-16}) \lll 1 \quad \text{for } 16 \le t \le 79$$
4. **80 Step Processing**: Divided into 4 rounds of 20 steps each, utilizing four round constants $K_t$ and non-linear functions $f_t$:
   - Steps $0 \dots 19$: $f_t = (B \wedge C) \vee (\neg B \wedge D)$, $K_t = \text{0x5A827999}$
   - Steps $20 \dots 39$: $f_t = B \oplus C \oplus D$, $K_t = \text{0x6ED9EBA1}$
   - Steps $40 \dots 59$: $f_t = (B \wedge C) \vee (B \wedge D) \vee (C \wedge D)$, $K_t = \text{0x8F1BBCDC}$
   - Steps $60 \dots 79$: $f_t = B \oplus C \oplus D$, $K_t = \text{0xCA62C1D6}$
   Step equation:
   $$TEMP = (A \lll 5) + f_t(B, C, D) + E + W_t + K_t$$
   $$E = D; \quad D = C; \quad C = B \lll 30; \quad B = A; \quad A = TEMP$$
5. **Output**: The five registers are added to their initial state modulo $2^{32}$, yielding the final 160-bit digest.

---

## 2. Example: Merkle-Damgård Construction
Both MD5 and SHA-1 follow the Merkle-Damgård iterated hash construction:
```
           M_1                  M_2                  M_L
            │                    │                    │
            ▼                    ▼                    ▼
IV ────► [ f ] ────► CV_1 ────► [ f ] ────► CV_2 ──► [ f ] ────► Final Hash
```
If the one-way compression function $f$ is collision-resistant, the iterated hash $H$ is provably collision-resistant.

---

## 3. Applications & Use Cases
1. **Git Version Control**: Uses SHA-1 (and transitioning to SHA-256) object IDs to index file trees, commits, and tags cryptographically.
2. **File Integrity Verification (Checksums)**: Linux package distributions (APT/RPM) provide SHA-256 digests to ensure ISO images and binaries were not corrupted during mirror downloads.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Calculation of Birthday Attack Effort for MD5 and SHA-1
**Problem**:
Calculate the number of random messages an attacker must hash to find a collision with probability $\ge 0.5$ for MD5 (128 bits) and SHA-1 (160 bits).

**Step-by-step Solution**:
- Formula from the Birthday Paradox:
  $$N \approx 1.177 \times 2^{m/2}$$
- **For MD5 ($m = 128$)**:
  $$N \approx 1.177 \times 2^{128/2} = 1.177 \times 2^{64} \approx 2.17 \times 10^{19} \text{ hashes}$$
  This is feasible on modern GPU clusters and botnets (Xiaoyun Wang demonstrated practical MD5 collisions in 2004).
- **For SHA-1 ($m = 160$)**:
  $$N \approx 1.177 \times 2^{160/2} = 1.177 \times 2^{80} \approx 1.42 \times 10^{24} \text{ hashes}$$
  In 2017, CWI Amsterdam and Google performed the SHAttered attack, finding the first practical collision using $2^{63.1}$ evaluations.

---

### Example 2: SHA-1 Message Padding Example
**Problem**:
A message has a length of 1000 bits. Calculate:
1. The number of padding bits added.
2. The total number of 512-bit blocks produced.

**Step-by-step Solution**:
1. Padded message length must satisfy:
   $$(L + 1 + P) \equiv 448 \pmod{512}$$
   where $L = 1000$ bits, 1 is the '1' bit, and $P$ is the count of '0' bits.
2. Calculate:
   $$(1000 + 1 + P) \equiv 448 \pmod{512}$$
   $$1001 + P \equiv 448 \pmod{512}$$
   Since $1001 = 1 \times 512 + 489$:
   $$489 + P \equiv 448 \pmod{512}$$
   $$P \equiv (448 - 489) \equiv -41 \equiv 512 - 41 = 471 \text{ bits}$$
3. Append 64-bit length:
   Total bits = $1000 \text{ (message)} + 1 \text{ ('1' bit)} + 471 \text{ (zeros)} + 64 \text{ (length)} = 1536 \text{ bits}$.
4. Number of 512-bit blocks:
   $$\text{Blocks} = \frac{1536}{512} = \mathbf{3 \text{ blocks}}$$

---

### Example 3: Comparative Analysis of MD5 vs. SHA-1
**Problem**:
Summarize the key differences between MD5 and SHA-1 in tabular format.

**Solution**:
| Feature | MD5 | SHA-1 |
|---|---|---|
| **Digest Length** | 128 bits | 160 bits |
| **State Registers** | 4 registers ($A, B, C, D$) of 32 bits | 5 registers ($A, B, C, D, E$) of 32 bits |
| **Input Block Size** | 512 bits | 512 bits |
| **Number of Steps** | 64 steps (4 rounds of 16 steps) | 80 steps (4 rounds of 20 steps) |
| **Word Expansion** | Reuses 16 words directly in each round | Expands 16 words into 80 words via XOR and circular shift |
| **Collision Resistance** | Completely broken (practical collisions in seconds) | Academically broken ($2^{63}$ effort); deprecated |
| **Maximum Message Length** | $\infty$ (practically $< 2^{64}$ bits) | $< 2^{64}$ bits |

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part C, Q15 - 9 Marks]
**Question**: Illustrate MD 5 hash algorithm in detail.

**Solution**:
1. **Overview & Objective**:
   The MD5 (Message Digest 5) algorithm was designed by Ron Rivest in 1991 (RFC 1321). It accepts a message of arbitrary length and produces a **128-bit message digest**. The algorithm processes the input message in 512-bit blocks using an iterated Merkle-Damgård compression structure.

2. **Step-by-Step Algorithm Execution**:
```
                        Input Message
                              │
                              ▼
                 [ Step 1: Append Padding Bits ]
                 (1 followed by 0s until ≡ 448 mod 512)
                              │
                              ▼
                 [ Step 2: Append 64-bit Length ]
                 (Total length is multiple of 512 bits)
                              │
                              ▼
     [ Step 3: Initialize 4 MD Buffer Registers (A, B, C, D) ]
                              │
                              ▼
                 [ Step 4: Process 512-bit Blocks ]
                   For each block Y_q (16 words):
                     - Round 1 (16 steps with function F)
                     - Round 2 (16 steps with function G)
                     - Round 3 (16 steps with function H)
                     - Round 4 (16 steps with function I)
                     - Additive chaining with previous buffer
                              │
                              ▼
                 [ Step 5: Output 128-bit Digest ]
```

3. **Detailed Steps**:
   - **Step 1: Append Padding Bits**: The message is padded so that its length in bits is congruent to $448 \pmod{512}$. Padding always occurs, even if the length is already 448 (adding 512 bits). It consists of a single `1` bit followed by `0` bits.
   - **Step 2: Append Length**: A 64-bit representation of the original message length modulo $2^{64}$ is appended to the message. The resulting message length is an exact multiple of 512 bits: $N \times 512$ bits.
   - **Step 3: Initialize MD Buffer**: A 128-bit buffer represented by four 32-bit registers $(A, B, C, D)$ is initialized:
     $$A = \text{0x67452301}, \quad B = \text{0xEFCDAB89}$$
     $$C = \text{0x98BADCFE}, \quad D = \text{0x10325476}$$
   - **Step 4: Process Message in 512-Bit Blocks**:
     Each 512-bit block is parsed into sixteen 32-bit words $X[0 \dots 15]$.
     Processing involves **4 rounds**, each having 16 steps (64 steps total).
     Each round utilizes a different non-linear logic function:
     - Round 1: $F(B, C, D) = (B \wedge C) \vee (\neg B \wedge D)$
     - Round 2: $G(B, C, D) = (B \wedge D) \vee (C \wedge \neg D)$
     - Round 3: $H(B, C, D) = B \oplus C \oplus D$
     - Round 4: $I(B, C, D) = C \oplus (B \vee \neg D)$
     **Single Step Operation**:
     Each step updates register $A$ according to the formula:
     $$A = B + ((A + \text{Func}(B, C, D) + X[k] + T[i]) \lll s)$$
     where:
     - $+$ denotes addition modulo $2^{32}$.
     - $X[k]$ is a 32-bit word from the current 512-bit block.
     - $T[i] = \lfloor 2^{32} \cdot |\sin(i)| \rfloor$ is an entry from a 64-element table of constants.
     - $\lll s$ denotes circular left shift by $s$ bits.
     After the step, the registers undergo cyclic rotation: $(A, B, C, D) \leftarrow (D, A, B, C)$.
   - **Step 5: Output**:
     After all 512-bit blocks are processed, the registers $A, B, C, D$ are concatenated to form the 128-bit digest.

---

### Question 2 [KTU June 2022, Part A, Q5 - 4 Marks]
**Question**: What are the requirements of a good hash function?

**Solution**:
A cryptographic hash function $H$ must satisfy six core requirements to guarantee security:
1. **Variable Input Length**: $H$ must accept an input message $x$ of any arbitrary length.
2. **Fixed Output Length**: $H$ must produce a fixed-length output message digest $h = H(x)$ (e.g., 160 bits for SHA-1, 256 bits for SHA-256).
3. **Efficiency (Fast Computation)**: Computing $H(x)$ must be computationally inexpensive in both software and hardware for any message $x$.
4. **Pre-image Resistance (One-Way Property)**: Given only a hash digest $h$, it must be computationally infeasible to find any message $x$ such that $H(x) = h$. Complexity is $O(2^m)$ where $m$ is the output bit length.
5. **Second Pre-image Resistance (Weak Collision Resistance)**: Given an input $x$, it must be computationally infeasible to find a different message $y \neq x$ such that $H(x) = H(y)$. Complexity is $O(2^m)$.
6. **Collision Resistance (Strong Collision Resistance)**: It must be computationally infeasible to find *any* pair of distinct messages $x$ and $y$ such that $H(x) = H(y)$. Complexity is $O(2^{m/2})$ due to the Birthday Attack.

---

### Question 3 [KTU June 2022, Part C, Q15 - 9 Marks]
**Question**: Illustrate the working of SHA-1 algorithm.

**Solution**:
1. **Overview & Parameters**:
   The Secure Hash Algorithm 1 (SHA-1) is a 160-bit cryptographic hash function developed by NIST/NSA.
   - Digest Length: 160 bits (five 32-bit words $A, B, C, D, E$).
   - Block Size: 512 bits.
   - Max Message Length: $< 2^{64}$ bits.
   - Number of Steps: 80 steps (4 rounds of 20 steps each).

2. **Step-by-Step SHA-1 Execution**:
   - **Step 1: Message Padding**:
     The message is padded so that its length in bits is congruent to $448 \pmod{512}$.
     Padding consists of one '1' bit followed by zero or more '0' bits.
   - **Step 2: Append Message Length**:
     A 64-bit integer containing the length of the original message before padding is appended to the message. The resulting length is an exact multiple of 512 bits ($N \times 512$).
   - **Step 3: Buffer Initialization**:
     Five 32-bit registers $(A, B, C, D, E)$ are initialized:
     $$A = \text{0x67452301}, \ B = \text{0xEFCDAB89}, \ C = \text{0x98BADCFE}, \ D = \text{0x10325476}, \ E = \text{0xC3D2E1F0}$$
   - **Step 4: Word Expansion (Message Schedule)**:
     Each 512-bit block is partitioned into sixteen 32-bit words $W_0, W_1, \dots, W_{15}$.
     These are expanded into an array of **80 words** ($W_0 \dots W_{79}$) using the linear recurrence:
     $$W_t = (W_{t-3} \oplus W_{t-8} \oplus W_{t-14} \oplus W_{t-16}) \lll 1 \quad (16 \le t \le 79)$$
   - **Step 5: 80-Step Round Processing**:
     The compression function runs 80 steps grouped into 4 rounds of 20 steps.
     Each step updates the buffer using round constants $K_t$ and logical functions $f_t$:
     - Round 1 ($0 \le t \le 19$): $f_t = (B \wedge C) \vee (\neg B \wedge D)$, $K_t = \text{0x5A827999}$
     - Round 2 ($20 \le t \le 39$): $f_t = B \oplus C \oplus D$, $K_t = \text{0x6ED9EBA1}$
     - Round 3 ($40 \le t \le 59$): $f_t = (B \wedge C) \vee (B \wedge D) \vee (C \wedge D)$, $K_t = \text{0x8F1BBCDC}$
     - Round 4 ($60 \le t \le 79$): $f_t = B \oplus C \oplus D$, $K_t = \text{0xCA62C1D6}$
     **The Single Step Logic**:
     $$TEMP = (A \lll 5) + f_t(B, C, D) + E + W_t + K_t \pmod{2^{32}}$$
     $$E = D$$
     $$D = C$$
     $$C = B \lll 30$$
     $$B = A$$
     $$A = TEMP$$
   - **Step 6: Chaining & Output**:
     After 80 steps, the output values of $A, B, C, D, E$ are added to the input values of the block modulo $2^{32}$.
     After the final block, concatenating $A \parallel B \parallel C \parallel D \parallel E$ produces the 160-bit message digest.
