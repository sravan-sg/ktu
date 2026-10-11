# IDEA Cipher Principles and Operations

## 1. Explanation
The **International Data Encryption Algorithm (IDEA)** was designed by Xuejia Lai and James Massey at ETH Zurich in 1991 as an improved replacement for DES. It is a symmetric block cipher that operates on 64-bit plaintext blocks under a 128-bit key.

### Design Philosophy & The MA Structure
Unlike DES and AES, IDEA **does not use S-boxes**. Instead, its strength and cryptographic security rely entirely on the **mixing of three incompatible algebraic operations** from three different mathematical groups acting on 16-bit sub-blocks:
1. **Bitwise Exclusive-OR ($\oplus$)**: Addition in the vector space $GF(2)^{16}$.
2. **Addition modulo $2^{16}$ ($\boxplus$)**: Addition in the ring of integers $\mathbb{Z}_{2^{16}}$. Carry bits propagate from right to left.
3. **Multiplication modulo $2^{16} + 1$ ($\odot$)**: Multiplication in the finite field $GF(2^{16}+1)$. Note that $2^{16}+1 = 65,537$ is a Fermat prime!
   - Special convention: The 16-bit block representing zero ($0000_{16}$) is treated as $2^{16} = 65,536$.

These three algebraic operations are incompatible in that neither distributes over the other, providing exceptional confusion and diffusion without requiring lookup tables.

```
       Three Incompatible Algebraic Operations in IDEA
  ┌─────────────────────────────────────────────────────────┐
  │  1. Bitwise XOR (⊕)             : Linear in GF(2)^16    │
  │  2. Addition mod 2^16 (⊞)       : Ring arithmetic       │
  │  3. Multiplication mod 2^16+1 (⊙): Prime field GF(65537) │
  └─────────────────────────────────────────────────────────┘
```

### Key Schedule and Subkey Generation
- **Master Key Length**: 128 bits.
- Total Subkeys Required: 52 subkeys of 16 bits each ($Z_1$ to $Z_{52}$).
- Generation algorithm:
  1. The 128-bit master key is partitioned into eight 16-bit subkeys ($Z_1 \dots Z_8$).
  2. The 128-bit key is rotated left circularly by 25 bits.
  3. The shifted 128 bits are partitioned into the next eight 16-bit subkeys ($Z_9 \dots Z_{16}$).
  4. This cycle (circular left shift by 25 bits and extraction of eight 16-bit subkeys) repeats until all 52 subkeys are produced (6 full shifts produce 48 subkeys, and a final shift produces the remaining 4 subkeys).

### Overall Cipher Structure
IDEA consists of **8 computational rounds** followed by an **Output Transformation** (often referred to as Round 9 or the half-round).
- The 64-bit plaintext is divided into four 16-bit sub-blocks: $X_1, X_2, X_3, X_4$.
- Each round $r \in \{1, 2, \dots, 8\}$ uses 6 subkeys ($Z_{6r-5}$ through $Z_{6r}$). Total for 8 rounds: $8 \times 6 = 48$ subkeys.
- The Output Transformation uses 4 subkeys ($Z_{49}, Z_{50}, Z_{51}, Z_{52}$). Total subkeys: $48 + 4 = 52$.

#### Internal Round Execution (The 14 Steps of One Round)
For an input $(X_1, X_2, X_3, X_4)$ and subkeys $(Z_1, Z_2, Z_3, Z_4, Z_5, Z_6)$:
1. $Y_1 = X_1 \odot Z_1$
2. $Y_2 = X_2 \boxplus Z_2$
3. $Y_3 = X_3 \boxplus Z_3$
4. $Y_4 = X_4 \odot Z_4$
5. $p = Y_1 \oplus Y_3$
6. $q = Y_2 \oplus Y_4$
7. $r = p \odot Z_5$
8. $s = (q \boxplus r) \odot Z_6$
9. $t = r \boxplus s$
10. $u = Y_1 \oplus s$
11. $v = Y_3 \oplus s$
12. $w = Y_2 \oplus t$
13. $x = Y_4 \oplus t$
14. The round output is: $(u, w, v, x)$. Note that the middle two blocks ($w$ and $v$) are swapped at the end of each round (except the final round before the output transformation).

#### Output Transformation
At the end of round 8, the four sub-blocks undergo a half-round using the final 4 subkeys:
$$Y_1 = X_1 \odot Z_{49}, \quad Y_2 = X_2 \boxplus Z_{50}, \quad Y_3 = X_3 \boxplus Z_{51}, \quad Y_4 = X_4 \odot Z_{52}$$
Concatenating $(Y_1 \parallel Y_2 \parallel Y_3 \parallel Y_4)$ yields the 64-bit ciphertext.

### Decryption and Inverse Key Derivation
Decryption follows the exact same computational structure as encryption. However, decryption requires inverse subkeys $U_i$ derived from encryption subkeys $Z_i$:
- For additive subkeys ($Z_2, Z_3$): Inverted using additive inverse modulo $2^{16}$:
  $$U = -Z \bmod 2^{16} = (2^{16} - Z) \bmod 2^{16}$$
- For multiplicative subkeys ($Z_1, Z_4$): Inverted using multiplicative inverse modulo $(2^{16}+1)$ via the Extended Euclidean Algorithm:
  $$U \odot Z \equiv 1 \pmod{2^{16}+1}$$
- Subkeys $Z_5, Z_6$ in the MA structure are used for XOR operations and remain identical ($U = Z$).

---

## 2. Example: Multiplication Modulo $2^{16}+1$
- Let $A = 0x0003$, $B = 0x0005$.
- Product $P = A \times B = 15$.
- Since $P < 65537$, $P \bmod 65537 = 15 = 0x000F$.
- If $A = 0x0000$, it represents $2^{16} = 65,536$.
- $A \odot B = 65536 \times 5 \bmod 65537 = -5 \equiv 65532 = 0xFFFC$.

---

## 3. Applications & Use Cases
1. **PGP (Pretty Good Privacy)**: Philip Zimmermann chose IDEA as the default symmetric cipher in early versions of PGP (PGP 2.x) due to its resistance against differential cryptanalysis.
2. **Resource-Constrained Cryptographic Microcontrollers**: Because IDEA uses only basic ALU arithmetic (16-bit add, multiply, XOR) without large S-box lookup tables in RAM/ROM, it runs efficiently on 16-bit embedded hardware.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Additive and Multiplicative Inverses in IDEA [KTU Analytical Model]
**Problem**:
In IDEA subkey derivation, given 16-bit encryption subkeys $Z_A = 0x0005$ (used in addition modulo $2^{16}$) and $Z_M = 0x0003$ (used in multiplication modulo $2^{16}+1 = 65537$), compute the corresponding decryption subkeys $U_A$ and $U_M$.

**Step-by-step Solution**:
1. **Additive Inverse $U_A$**:
   $$U_A = -Z_A \bmod 2^{16} = (65536 - 5) \bmod 65536 = 65531$$
   Converting to hexadecimal:
   $$65531 = 0xFFFB$$
   Verification: $(5 + 65531) \bmod 65536 = 65536 \equiv 0 \pmod{65536}$.

2. **Multiplicative Inverse $U_M$**:
   $$Z_M \cdot U_M \equiv 1 \pmod{65537} \implies 3 \cdot U_M \equiv 1 \pmod{65537}$$
   Using Extended Euclidean Algorithm:
   $$65537 = 3 \times 21845 + 2$$
   $$3 = 2 \times 1 + 1$$
   Backward substitution:
   $$1 = 3 - 2 = 3 - (65537 - 3 \times 21845) = 3 \times 21846 - 65537$$
   Therefore:
   $$U_M = 21846$$
   Converting to hexadecimal:
   $$21846 = 0x5556$$
   Verification:
   $$3 \times 21846 = 65538 = 1 \times 65537 + 1 \equiv 1 \pmod{65537}$$.

---

### Example 2: IDEA Key Expansion Tracing
**Problem**:
A 128-bit key in hexadecimal is:
`K = 0x0001 0002 0003 0004 0005 0006 0007 0008`
Compute subkeys $Z_1$ through $Z_9$.

**Step-by-step Solution**:
1. Directly extract the first 8 subkeys from the unshifted key:
   - $Z_1 = 0x0001$
   - $Z_2 = 0x0002$
   - $Z_3 = 0x0003$
   - $Z_4 = 0x0004$
   - $Z_5 = 0x0005$
   - $Z_6 = 0x0006$
   - $Z_7 = 0x0007$
   - $Z_8 = 0x0008$
2. Rotate the 128-bit key left circularly by 25 bits:
   - The first 16-bit block after rotation starts at bit position 26.
   - Bit position 25 is within the second 16-bit word ($0x0002$).
   - Rotating left by 25 bits brings bits 25..40 to the most significant 16 bits.
   - Word 2 shifted left: $(0x0002 \ll 9) \mid (0x0003 \gg 7) = 0x0400 \mid 0x0000 = 0x0400$.
   - Thus, $Z_9 = 0x0400$.

---

### Example 3: Multiplication Modulo $2^{16}+1$ with Zero Input
**Problem**:
Evaluate $X \odot Z$ when $X = 0x0000$ and $Z = 0x0002$ in IDEA arithmetic.

**Step-by-step Solution**:
- By IDEA definition, $0x0000$ represents $2^{16} = 65536$.
- Product: $65536 \times 2 = 131072$.
- Divide by $65537$:
  $$131072 = 1 \times 65537 + 65535$$
- The remainder is $65535 = 0xFFFF$.
- Output: $0xFFFF$.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part B, Q12(a) / June 2022, Part A, Q3 - 4 Marks]
**Question**: How key generation is performed in IDEA? Explain the key expansion procedure of IDEA.

**Solution**:
1. **Master Key & Subkey Requirements**:
   - Master Key Length: **128 bits**.
   - Subkey Word Size: **16 bits**.
   - Total Subkeys Required: **52 subkeys** ($Z_1$ through $Z_{52}$).
     - Rounds 1 through 8: 6 subkeys per round $\times 8 = 48$ subkeys.
     - Output Transformation (Round 9): 4 subkeys.
     - Total: $48 + 4 = 52$ subkeys.

2. **Step-by-Step Key Expansion Algorithm**:
   - **Step 1 (Subkeys 1 to 8)**: The 128-bit master key is directly divided into eight 16-bit blocks:
     $$Z_1 = K[127:112], \ Z_2 = K[111:96], \ \dots, \ Z_8 = K[15:0]$$
   - **Step 2 (Circular Left Shift)**: The entire 128-bit master key is shifted cyclically to the left by **25 bits**:
     $$K' = \text{ROTL}_{25}(K)$$
   - **Step 3 (Subkeys 9 to 16)**: The newly shifted 128-bit key $K'$ is divided into the next eight 16-bit subkeys ($Z_9$ through $Z_{16}$).
   - **Step 4 (Repetition)**: The 128-bit register is repeatedly shifted left by 25 bits, generating 8 new subkeys after each shift.
     - 1st 25-bit shift $\rightarrow$ generates $Z_9 \dots Z_{16}$
     - 2nd 25-bit shift $\rightarrow$ generates $Z_{17} \dots Z_{24}$
     - 3rd 25-bit shift $\rightarrow$ generates $Z_{25} \dots Z_{32}$
     - 4th 25-bit shift $\rightarrow$ generates $Z_{33} \dots Z_{40}$
     - 5th 25-bit shift $\rightarrow$ generates $Z_{41} \dots Z_{48}$
     - 6th 25-bit shift $\rightarrow$ the first 4 blocks of 16 bits form $Z_{49}, Z_{50}, Z_{51}, Z_{52}$. The remaining 4 blocks are discarded.
   This completes the generation of all 52 subkeys.

---

### Question 2 [KTU January 2023, Part B, Q12(b) - 4 Marks]
**Question**: Discuss the primitive operations used in IDEA.

**Solution**:
The design of the IDEA cipher deliberately avoids S-boxes (lookup tables) by combining three distinct, mathematically incompatible algebraic operations on 16-bit words. Each operation is performed on pairs of 16-bit unsigned integers:

1. **Bitwise Exclusive-OR ($\oplus$)**:
   - Bitwise XOR between two 16-bit words ($A \oplus B$).
   - Corresponds to vector addition in the finite field $GF(2)^{16}$.
   - Characteristics: Linear, bit-independent, carries do not propagate between positions. Self-inverse ($A \oplus A = 0$).

2. **Addition Modulo $2^{16}$ ($\boxplus$)**:
   - Integer addition modulo 65,536: $(A + B) \bmod 2^{16}$.
   - Forms an abelian group under addition in $\mathbb{Z}_{2^{16}}$.
   - Characteristics: Carries propagate from least significant bit to most significant bit, disrupting bit independence.
   - Inverse operation for decryption is the additive inverse: $(-Z) \bmod 2^{16} = (2^{16} - Z) \bmod 2^{16}$.

3. **Multiplication Modulo $2^{16} + 1$ ($\odot$)**:
   - Integer multiplication modulo 65,537: $(A \times B) \bmod (2^{16} + 1)$.
   - Because $2^{16} + 1 = 65,537$ is a Fermat prime, the set of non-zero integers modulo 65,537 forms a multiplicative finite field $GF(65537)$.
   - **Zero Handling**: The 16-bit word $0x0000$ represents $2^{16} = 65,536$. If the multiplication yields a result of $65,536$, it is encoded back as $0x0000$.
   - Inverse operation for decryption is the multiplicative inverse modulo 65,537 calculated via the Extended Euclidean Algorithm: $Z \odot Z^{-1} \equiv 1 \pmod{65537}$.

**Cryptographic Synergy**:
These three operations are completely incompatible in algebraic structure:
- $\oplus$ does not distribute over $\boxplus$.
- $\boxplus$ does not distribute over $\odot$.
- $\oplus$ does not distribute over $\odot$.
Interleaving these three operations across 8 rounds generates high non-linearity and complete diffusion, rendering IDEA immune to differential and linear cryptanalysis.
