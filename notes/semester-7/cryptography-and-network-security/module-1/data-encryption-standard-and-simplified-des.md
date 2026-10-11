# Data Encryption Standard (DES) and Simplified DES (S-DES)

## 1. Explanation
The Data Encryption Standard (DES) was published by the National Bureau of Standards (NBS, now NIST) in 1977 as FIPS PUB 46, based on IBM's Lucifer cipher designed under the cryptographic guidance of Horst Feistel.

### Feistel Cipher Principles & Architecture
Most symmetric block ciphers are based on the **Feistel network architecture**. A Feistel cipher approximates Claude Shannon's concept of an ideal block cipher by alternating substitution (confusion) and permutation (diffusion) across multiple successive rounds.
1. **Diffusion**: Dissipates the statistical structure of plaintext across the entire ciphertext. An avalanche effect ensures that altering a single bit in the plaintext flips approximately 50% of the bits in the ciphertext.
2. **Confusion**: Obscures the relationship between the secret key and the ciphertext through non-linear substitution (S-boxes), preventing an attacker from deducing the key bits from ciphertext statistics.

In a Feistel cipher of block size $2w$ bits:
- Input block is split into equal halves: $LE_0$ and $RE_0$ of $w$ bits.
- In each round $i \in \{1, 2, \dots, n\}$:
  $$LE_i = RE_{i-1}$$
  $$RE_i = LE_{i-1} \oplus F(RE_{i-1}, K_i)$$
- After round $n$, the halves are swapped: $(RE_n, LE_n)$.
- **Feistel Inversion Property**: Decryption executes the identical round algorithm in reverse using subkeys in reverse order ($K_n, K_{n-1}, \dots, K_1$), eliminating the requirement for an invertible round function $F$.

```
           LE_{i-1}                   RE_{i-1}
              │                          │
              │                 ┌────────┴────────┐
              │                 │                 │
              │                 │      Round      │ ◄─── Subkey K_i
              │                 │   Function F    │
              │                 └────────┬────────┘
              │                          │
              ▼                          │
             (XOR) ◄─────────────────────┘
              │                          │
              │                          │
              ▼                          ▼
            LE_i                       RE_i
```

### The Data Encryption Standard (DES)
DES is a 16-round Feistel cipher that processes 64-bit plaintext blocks under a 56-bit secret key (supplied as 64 bits with 8 parity bits).

#### Structure of DES
1. **Initial Permutation (IP)**: Transposes the 64-bit input block into $L_0$ (32 bits) and $R_0$ (32 bits).
2. **16 Feistel Rounds**: For $i = 1$ to $16$:
   - $L_i = R_{i-1}$
   - $R_i = L_{i-1} \oplus F(R_{i-1}, K_i)$
3. **Round Function $F(R, K)$**:
   - **Expansion Permutation ($E$)**: Expands 32-bit $R$ into 48 bits.
   - **Key XOR**: Computes $E(R) \oplus K_i$ using the 48-bit round subkey $K_i$.
   - **S-Box Substitution**: The 48 bits are partitioned into 8 groups of 6 bits. Each 6-bit block $(b_1 b_2 b_3 b_4 b_5 b_6)$ enters an S-box $S_j$ ($j \in \{1, \dots, 8\}$):
     - Bits $b_1 b_6$ form a 2-bit row number ($0 \dots 3$).
     - Bits $b_2 b_3 b_4 b_5$ form a 4-bit column number ($0 \dots 15$).
     - The cell lookup returns a 4-bit value.
     - 8 S-boxes output $8 \times 4 = 32$ bits.
     - **Non-Linearity in DES**: The S-boxes provide the **only non-linear transformation** in the entire DES algorithm. All other operations ($E$, XOR, $P$, round swapping) are strictly linear. Without S-boxes, DES would reduce to a system of linear equations easily solvable via Gaussian elimination.
   - **Permutation ($P$)**: Permutes the 32-bit S-box output.
4. **Final Permutation ($IP^{-1}$)**: The inverse of the initial permutation applied to $(R_{16} \parallel L_{16})$.

#### Key Schedule of DES
- 64-bit master key passes through Permuted Choice 1 ($PC-1$), dropping parity bits to yield 56 bits split into $C_0$ (28 bits) and $D_0$ (28 bits).
- In each round $i$, $C_{i-1}$ and $D_{i-1}$ undergo circular left shifts by 1 or 2 positions (1 shift in rounds 1, 2, 9, 16; 2 shifts in other rounds).
- Permuted Choice 2 ($PC-2$) compresses the 56 shifted bits into a 48-bit subkey $K_i$.

### Simplified DES (S-DES)
Developed by Edward Schaefer (1996) as an educational model. It operates on 8-bit plaintext blocks with a 10-bit key, using 2 Feistel rounds.
- **Key Generation**:
  - $P_{10} = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]$
  - Split into 5-bit halves, apply circular left shift ($LS-1$).
  - $P_8 = [6, 3, 7, 4, 8, 5, 10, 9]$ gives Subkey $K_1$.
  - Apply $LS-2$ to each half, then $P_8$ gives Subkey $K_2$.
- **Encryption**:
  - Initial Permutation $IP = [2, 6, 3, 1, 4, 8, 5, 7]$.
  - Round 1 with $K_1$: Expansion $E/P = [4, 1, 2, 3, 2, 3, 4, 1]$, XOR with $K_1$, S-Boxes $S_0$ and $S_1$ lookup, permutation $P_4 = [2, 4, 3, 1]$.
  - Switch function ($SW$) swaps 4-bit halves.
  - Round 2 with $K_2$.
  - Inverse Permutation $IP^{-1} = [4, 1, 3, 5, 7, 2, 8, 6]$.

### Cryptanalysis & Strength of DES
- **Key Length Vulnerability**: With 56 bits, the key space is $2^{56} \approx 7.2 \times 10^{16}$. Exhaustive key search was achieved in 1998 by the Electronic Frontier Foundation (EFF "Deep Crack") in under 56 hours.
- **Differential Cryptanalysis (Biham & Shamir, 1990)**: A chosen-plaintext attack analyzing how specific differences in plaintext pairs propagate through round S-boxes to produce differences in ciphertext pairs. DES with 16 rounds requires $2^{47}$ chosen plaintexts, making it theoretically broken, but practically infeasible compared to brute force ($2^{56}$).
- **Linear Cryptanalysis (Matsui, 1993)**: A known-plaintext attack that finds linear approximations between plaintext bits, ciphertext bits, and subkey bits:
  $$P_{i_1} \oplus \dots \oplus P_{i_a} \oplus C_{j_1} \oplus \dots \oplus C_{j_b} = K_{k_1} \oplus \dots \oplus K_{k_c}$$
  with probability $p \neq 1/2$. Requires $2^{43}$ known plaintexts to recover the DES key.

---

## 2. Example: S-DES S-Box Lookup
- Let the 4-bit input to S-box $S_0$ be $(1010)_2$.
- S-Box $S_0$ matrix:
```
        Col 0  Col 1  Col 2  Col 3
Row 0:    1      0      3      2
Row 1:    3      2      1      0
Row 2:    0      2      1      3
Row 3:    3      1      3      2
```
- Row selection = bits 1 and 4 = $10_2 = 2$.
- Column selection = bits 2 and 3 = $01_2 = 1$.
- Look up Row 2, Column 1: Value is $2 = (10)_2$.
- Output is $(10)_2$.

---

## 3. Applications & Use Cases
1. **Legacy Financial ATM / POS Networks**: DES and Triple-DES (3DES / TDEA) formed the backbone of ANSI X9.17 and EMV chip card transactions before transitioning to AES.
2. **UNIX `crypt()` Password Hashing**: The original Unix password hashing utility modified DES by expanding the 12-bit salt into an altered expansion permutation table $E$ to resist hardware-accelerated dictionary attacks.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Complete S-DES Subkey Generation [KTU January 2023]
**Problem**:
Given initial 10-bit master key $K = (1100011110)_2$, compute subkeys $K_1$ and $K_2$ using standard S-DES permutations:
- $P_{10} = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]$
- $P_8 = [6, 3, 7, 4, 8, 5, 10, 9]$

**Step-by-step Solution**:
1. Label key indices:
   $$K = \begin{array}{cccccccccc} 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\ 1 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 \end{array}$$
2. Apply $P_{10}$:
   - Bit 3 $\rightarrow 0$
   - Bit 5 $\rightarrow 0$
   - Bit 2 $\rightarrow 1$
   - Bit 7 $\rightarrow 1$
   - Bit 4 $\rightarrow 0$
   - Bit 10 $\rightarrow 0$
   - Bit 1 $\rightarrow 1$
   - Bit 9 $\rightarrow 1$
   - Bit 8 $\rightarrow 1$
   - Bit 6 $\rightarrow 1$
   $$P_{10}(K) = (00110 \ 01111)_2$$
3. Divide into 5-bit halves:
   $$L_0 = (00110)_2, \quad R_0 = (01111)_2$$
4. Perform Left Shift 1 ($LS-1$):
   $$L_1 = LS_1(00110) = (01100)_2$$
   $$R_1 = LS_1(01111) = (11110)_2$$
   Combined 10 bits: $(0110011110)_2$.
5. Compute Subkey $K_1$ using $P_8$:
   $$P_8 = [6, 3, 7, 4, 8, 5, 10, 9]$$
   - Index 6 (bit 1 of $R_1$) = $1$
   - Index 3 (bit 3 of $L_1$) = $1$
   - Index 7 (bit 2 of $R_1$) = $1$
   - Index 4 (bit 4 of $L_1$) = $0$
   - Index 8 (bit 3 of $R_1$) = $1$
   - Index 5 (bit 5 of $L_1$) = $0$
   - Index 10 (bit 5 of $R_1$) = $0$
   - Index 9 (bit 4 of $R_1$) = $1$
   $$\mathbf{K_1 = (11101001)_2}$$
6. Perform Left Shift 2 ($LS-2$) on $L_1, R_1$:
   $$L_2 = LS_2(01100) = (10001)_2$$
   $$R_2 = LS_2(11110) = (11011)_2$$
   Combined 10 bits: $(1000111011)_2$.
7. Compute Subkey $K_2$ using $P_8$:
   - Index 6 = $1$
   - Index 3 = $0$
   - Index 7 = $1$
   - Index 4 = $0$
   - Index 8 = $0$
   - Index 5 = $1$
   - Index 10 = $1$
   - Index 9 = $1$
   $$\mathbf{K_2 = (10100111)_2}$$

---

### Example 2: S-DES Round 1 Function $F$ Computation
**Problem**:
In S-DES, let the 4-bit right half be $R_0 = (1011)_2$ and subkey $K_1 = (11101001)_2$. Compute $F(R_0, K_1)$.
Given:
- $E/P = [4, 1, 2, 3, 2, 3, 4, 1]$
- $S_0 = \begin{pmatrix} 1 & 0 & 3 & 2 \\ 3 & 2 & 1 & 0 \\ 0 & 2 & 1 & 3 \\ 3 & 1 & 3 & 2 \end{pmatrix}$, $S_1 = \begin{pmatrix} 0 & 1 & 2 & 3 \\ 2 & 0 & 1 & 3 \\ 3 & 0 & 1 & 0 \\ 2 & 1 & 0 & 3 \end{pmatrix}$
- $P_4 = [2, 4, 3, 1]$

**Step-by-step Solution**:
1. Expand $R_0 = (1011)_2$ via $E/P$:
   - Pos 4: 1, Pos 1: 1, Pos 2: 0, Pos 3: 1, Pos 2: 0, Pos 3: 1, Pos 4: 1, Pos 1: 1
   $$E/P(R_0) = (11010111)_2$$
2. XOR with $K_1 = (11101001)_2$:
   $$11010111 \oplus 11101001 = (00111110)_2$$
3. Split into 4-bit inputs:
   - For $S_0$: $(0011)_2 \implies \text{Row } = 01_2 = 1, \text{ Col } = 01_2 = 1$.
     $S_0(1, 1) = 2 = (10)_2$.
   - For $S_1$: $(1110)_2 \implies \text{Row } = 10_2 = 2, \text{ Col } = 11_2 = 3$.
     $S_1(2, 3) = 0 = (00)_2$.
   Combined 4 bits: $(1000)_2$.
4. Permute via $P_4 = [2, 4, 3, 1]$:
   - Pos 2: 0, Pos 4: 0, Pos 3: 0, Pos 1: 1
   $$F(R_0, K_1) = (0001)_2$$

---

### Example 3: Avalanche Effect Verification in DES
**Problem**:
Explain how DES guarantees that flipping 1 bit in plaintext changes approximately 32 bits (50%) in ciphertext after 16 rounds.

**Step-by-step Solution**:
- **Round 1**: A 1-bit difference in $R_0$ expands to 1 or 2 bits in $E(R_0)$. This enters 1 or 2 S-boxes, affecting up to 4 to 8 bits in the S-box outputs.
- Permutation $P$ scatters these 4 to 8 bit differences across different S-boxes in the subsequent round.
- **Round 2**: The differences in $R_1$ feed through multiple S-boxes, rapidly multiplying the number of active bit differences.
- By Round 4, every S-box receives at least one changed bit.
- By Round 16, every single output bit is a complex non-linear function of every input bit and every key bit.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q1 - 4 Marks]
**Question**: How the nonlinearity is achieved in DES.

**Solution**:
1. **Mathematical Structure of DES Operations**:
   The Data Encryption Standard (DES) consists of permutations ($IP$, $IP^{-1}$, $E$, $P$), bitwise Exclusive-OR ($\oplus$) operations, and S-box substitutions.
   - Permutations are strictly linear operations that merely rearrange the positions of bits without altering their algebraic values: $P(x \oplus y) = P(x) \oplus P(y)$.
   - Bitwise XOR ($\oplus$) is the addition operation in the finite field $GF(2)$, which is also strictly linear: $(x_1 \oplus x_2) \oplus (y_1 \oplus y_2) = (x_1 \oplus y_1) \oplus (x_2 \oplus y_2)$.
2. **The Non-Linear S-Boxes**:
   - The **eight Substitution Boxes (S-Boxes, $S_1$ to $S_8$)** are the **only non-linear components** of the entire DES algorithm.
   - Each S-Box maps a 6-bit input to a 4-bit output: $S_i: \{0, 1\}^6 \rightarrow \{0, 1\}^4$.
   - The mapping cannot be expressed as a linear combination of input bits over $GF(2)$. That is, for two 6-bit inputs $x$ and $y$:
     $$S(x \oplus y) \neq S(x) \oplus S(y)$$
3. **Cryptographic Necessity of Non-Linearity**:
   If the S-Boxes were linear or affine, the entire 16-round Feistel cipher could be collapsed into a single matrix equation over $GF(2)$:
   $$C = A \cdot P \oplus B \cdot K$$
   where $A$ and $B$ are fixed binary matrices. An attacker could then completely determine the secret key $K$ from a handful of known plaintext-ciphertext pairs using Gaussian elimination in $O(n^3)$ operations. The non-linear S-boxes defeat linear equations, providing Shannon's **Confusion**.

---

### Question 2 [KTU May 2019, Part A, Q2 - 4 Marks]
**Question**: Differentiate Confusion and Diffusion.

**Solution**:
Claude Shannon introduced Confusion and Diffusion in his landmark 1949 paper *"Communication Theory of Secrecy Systems"* as the two fundamental techniques to thwart statistical cryptanalysis:

| Feature | Confusion | Diffusion |
|---|---|---|
| **Definition** | Obscures the mathematical relationship between the secret key and the resulting ciphertext. | Dissipates the statistical redundancy and structure of the plaintext across the entire ciphertext. |
| **Primary Objective** | Prevents an attacker from deducing key bits even if they have collected vast amounts of ciphertext. | Prevents frequency analysis of plaintext patterns by ensuring that each plaintext bit affects many ciphertext bits. |
| **Cryptographic Primitive** | Achieved through **Substitution** (e.g., non-linear S-boxes in DES and AES). | Achieved through **Permutation / Transposition** (e.g., P-boxes, Expansion $E$, `ShiftRows`, `MixColumns`). |
| **Statistical Effect** | Makes the relationship between ciphertext statistics and key values complex and non-linear. | Produces the **Avalanche Effect**: flipping a single plaintext bit flips roughly 50% of the ciphertext bits. |
| **Mathematical Representation** | High non-linear algebraic degree; impossible to approximate by linear equations. | High branch number; spreads local bits across multiple non-overlapping state words. |

---

### Question 3 [KTU January 2023, Part A, Q2 - 4 Marks]
**Question**: Apply the key generation of SDES on the initial 10bit key `"1100011110"` and compute the subkeys k1 and k2. (Hint: P10 - 3 5 2 7 4 10 1 9 8 6 and P8 - 6 3 7 4 8 5 10 9)

**Solution**:
1. **Initial 10-bit Master Key**:
   $$K = 1 \ 1 \ 0 \ 0 \ 0 \ 1 \ 1 \ 1 \ 1 \ 0$$
   Index mapping ($1 \dots 10$):
   $k_1=1, k_2=1, k_3=0, k_4=0, k_5=0, k_6=1, k_7=1, k_8=1, k_9=1, k_{10}=0$.

2. **Permutation $P_{10}$** ($[3, 5, 2, 7, 4, 10, 1, 9, 8, 6]$):
   - Pos 1: $k_3 = 0$
   - Pos 2: $k_5 = 0$
   - Pos 3: $k_2 = 1$
   - Pos 4: $k_7 = 1$
   - Pos 5: $k_4 = 0$
   - Pos 6: $k_{10} = 0$
   - Pos 7: $k_1 = 1$
   - Pos 8: $k_9 = 1$
   - Pos 9: $k_8 = 1$
   - Pos 10: $k_6 = 1$
   $$P_{10}(K) = 00110 \ 01111$$

3. **Left Shift 1 ($LS-1$) on both 5-bit halves**:
   - Left half $L_0 = 00110 \xrightarrow{LS-1} L_1 = 01100$
   - Right half $R_0 = 01111 \xrightarrow{LS-1} R_1 = 11110$
   Combined 10 bits: $0 \ 1 \ 1 \ 0 \ 0 \ 1 \ 1 \ 1 \ 1 \ 0$ (Positions: $1 \dots 10$).

4. **Compute Subkey $K_1$ via $P_8$** ($[6, 3, 7, 4, 8, 5, 10, 9]$):
   - Pos 1: Bit 6 = $1$
   - Pos 2: Bit 3 = $1$
   - Pos 3: Bit 7 = $1$
   - Pos 4: Bit 4 = $0$
   - Pos 5: Bit 8 = $1$
   - Pos 6: Bit 5 = $0$
   - Pos 7: Bit 10 = $0$
   - Pos 8: Bit 9 = $1$
   $$\mathbf{K_1 = 11101001}$$

5. **Left Shift 2 ($LS-2$) on $L_1$ and $R_1$**:
   - $L_1 = 01100 \xrightarrow{LS-2} L_2 = 10001$
   - $R_1 = 11110 \xrightarrow{LS-2} R_2 = 11011$
   Combined 10 bits: $1 \ 0 \ 0 \ 0 \ 1 \ 1 \ 1 \ 0 \ 1 \ 1$ (Positions: $1 \dots 10$).

6. **Compute Subkey $K_2$ via $P_8$** ($[6, 3, 7, 4, 8, 5, 10, 9]$):
   - Pos 1: Bit 6 = $1$
   - Pos 2: Bit 3 = $0$
   - Pos 3: Bit 7 = $1$
   - Pos 4: Bit 4 = $0$
   - Pos 5: Bit 8 = $0$
   - Pos 6: Bit 5 = $1$
   - Pos 7: Bit 10 = $1$
   - Pos 8: Bit 9 = $1$
   $$\mathbf{K_2 = 10100111}$$

**Summary**:
- $\mathbf{K_1 = 11101001}$
- $\mathbf{K_2 = 10100111}$

---

### Question 4 [KTU January 2023, Part B, Q11 - 9 Marks]
**Question**: Explain the working of DES with relevant figures.

**Solution**:
1. **Overview & Parameters**:
   The Data Encryption Standard (DES) is a 16-round symmetric Feistel cipher.
   - Plaintext Block Size: 64 bits
   - Master Key Length: 64 bits (56 effective bits + 8 parity bits)
   - Ciphertext Output: 64 bits
   - Number of Rounds: 16 identical Feistel rounds

2. **Overall DES Structural Diagram**:
```
               64-bit Plaintext
                      │
                      ▼
            [ Initial Permutation (IP) ]
                      │
            ┌─────────┴─────────┐
            ▼                   ▼
        L_0 (32 bits)       R_0 (32 bits)
            │                   │
            │   ┌───────────────┤
            │   │               ▼
            │   │        [ Round Function F ] ◄── Subkey K_1 (48 bits)
            ▼   │               │
           (XOR)◄───────────────┘
            │   │
            ▼   ▼
        L_1 = R_0, R_1 = L_0 ⊕ F(R_0, K_1)
            │                   │
            │  [ Rounds 2 to 15 ]
            │                   │
            ▼                   ▼
       L_16 (32 bits)      R_16 (32 bits)
            │                   │
            └─────────┬─────────┘
                      ▼
           Swap Halves: (R_16 || L_16)
                      │
                      ▼
         [ Final Permutation (IP^-1) ]
                      │
                      ▼
              64-bit Ciphertext
```

3. **Step-by-Step Round Operations**:
   In each round $i \in \{1, 2, \dots, 16\}$:
   $$L_i = R_{i-1}$$
   $$R_i = L_{i-1} \oplus F(R_{i-1}, K_i)$$

4. **The Round Function $F(R_{i-1}, K_i)$**:
```
          R_{i-1} (32 bits)
                 │
                 ▼
     [ Expansion Permutation E ] ───► 48 bits
                 │
                 ▼
               (XOR) ◄──────────────── Subkey K_i (48 bits)
                 │
                 ▼ (48 bits)
     [ Eight 6x4 S-Boxes S1..S8 ] ───► 32 bits (Non-linear substitution)
                 │
                 ▼
       [ Permutation P ] ───────────► 32 bits output
```
   - **Expansion Permutation ($E$)**: Expands 32 bits to 48 bits by duplicating 16 bits.
   - **Key Addition**: Bitwise XOR with the 48-bit subkey $K_i$.
   - **S-Box Substitution**: The 48 bits are divided into 8 groups of 6 bits. Each 6-bit chunk $(b_1 b_2 b_3 b_4 b_5 b_6)$ maps to 4 bits via S-Box $S_j$: row $= (b_1 b_6)_2$, col $= (b_2 b_3 b_4 b_5)_2$. Output is $8 \times 4 = 32$ bits.
   - **Permutation ($P$)**: Rearranges the 32 S-box output bits to ensure rapid diffusion across different S-boxes in the next round.

5. **Key Schedule**:
   - Master 64-bit key passes through $PC-1$, stripping 8 parity bits to yield 56 bits ($C_0, D_0$ of 28 bits each).
   - In rounds 1, 2, 9, 16, halves undergo 1-bit left circular shift; in all other rounds, 2-bit left circular shift.
   - $PC-2$ selects and permutes 48 bits to form round subkey $K_i$.

6. **Decryption**:
   Decryption runs the exact same Feistel algorithm with ciphertext as input, utilizing subkeys in reverse order: $K_{16}, K_{15}, \dots, K_1$.
