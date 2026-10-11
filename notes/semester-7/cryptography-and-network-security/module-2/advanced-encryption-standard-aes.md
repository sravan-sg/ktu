# Advanced Encryption Standard (AES)

## 1. Explanation
The **Advanced Encryption Standard (AES)** was standardized by NIST in 2001 (FIPS PUB 197) following a multi-year global competition won by the **Rijndael** cipher, designed by Belgian cryptographers Joan Daemen and Vincent Rijmen. AES replaced DES and 3DES as the worldwide symmetric standard.

### AES Architectural Principles
Unlike DES, AES is **not a Feistel network**. Instead, it is a **Substitution-Permutation Network (SPN)** that processes the entire 128-bit block in parallel in every round.
- **Block Size**: Fixed at 128 bits (16 bytes), organized as a $4 \times 4$ column-major matrix of bytes termed the **State Matrix**:
  $$\text{State} = \begin{pmatrix} s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\ s_{1,0} & s_{1,1} & s_{1,2} & s_{1,3} \\ s_{2,0} & s_{2,1} & s_{2,2} & s_{2,3} \\ s_{3,0} & s_{3,1} & s_{3,2} & s_{3,3} \end{pmatrix}$$
- **Key Sizes & Round Counts**:
  - 128-bit key ($N_k = 4$ words) $\rightarrow$ **10 rounds** ($N_r = 10$).
  - 192-bit key ($N_k = 6$ words) $\rightarrow$ **12 rounds** ($N_r = 12$).
  - 256-bit key ($N_k = 8$ words) $\rightarrow$ **14 rounds** ($N_r = 14$).

```
             AES-128 Encryption Structure
                   128-bit Plaintext
                          │
                          ▼
                  [ AddRoundKey ] ◄── Subkey W[0..3]
                          │
         ┌────────────────┴────────────────┐
         │ Rounds 1 to 9:                  │
         │   1. SubBytes (Non-linear)      │
         │   2. ShiftRows (Permutation)    │
         │   3. MixColumns (Diffusion)     │
         │   4. AddRoundKey                │
         └────────────────┬────────────────┘
                          │
         ┌────────────────┴────────────────┐
         │ Round 10 (Final Round):         │
         │   1. SubBytes                   │
         │   2. ShiftRows                  │
         │   (MixColumns is OMITTED!)      │
         │   3. AddRoundKey                │
         └────────────────┬────────────────┘
                          │
                          ▼
                  128-bit Ciphertext
```

### The Four Primitive Transformations in One Round

#### 1. `SubBytes` (Byte Substitution)
- A non-linear byte-by-byte substitution operating independently on each byte of the state matrix.
- Each byte $a \in GF(2^8)$ is transformed mathematically:
  1. Take the multiplicative inverse of $a$ in the Galois Field $GF(2^8)$ with irreducible reduction polynomial:
     $$m(x) = x^8 + x^4 + x^3 + x + 1 \quad (\text{0x11B})$$
     (with mapping $0x00 \rightarrow 0x00$).
  2. Apply an affine transformation over $GF(2)$:
     $$b_i' = b_i \oplus b_{(i+4) \bmod 8} \oplus b_{(i+5) \bmod 8} \oplus b_{(i+6) \bmod 8} \oplus b_{(i+7) \bmod 8} \oplus c_i$$
     where $c = 0x63 = (01100011)_2$.
- The Inverse S-Box (`InvSubBytes`) applies the inverse affine transformation followed by the multiplicative inverse in $GF(2^8)$.

#### 2. `ShiftRows` (Row Permutation)
- Performs a cyclically shifted permutation on the rows of the state matrix to provide diffusion across columns:
  - Row 0: No shift (shifted left by 0 bytes).
  - Row 1: Circular left shift by 1 byte: $(s_{1,0}, s_{1,1}, s_{1,2}, s_{1,3}) \rightarrow (s_{1,1}, s_{1,2}, s_{1,3}, s_{1,0})$.
  - Row 2: Circular left shift by 2 bytes: $(s_{2,0}, s_{2,1}, s_{2,2}, s_{2,3}) \rightarrow (s_{2,2}, s_{2,3}, s_{2,0}, s_{2,1})$.
  - Row 3: Circular left shift by 3 bytes: $(s_{3,0}, s_{3,1}, s_{3,2}, s_{3,3}) \rightarrow (s_{3,3}, s_{3,0}, s_{3,1}, s_{3,2})$.
- `InvShiftRows` shifts rows cyclically to the right by 0, 1, 2, and 3 bytes respectively.

#### 3. `MixColumns` (Column Mixing)
- Operates on each column of the state matrix independently, treating each 4-byte column as a 4-term polynomial over $GF(2^8)$ multiplied modulo $(x^4 + 1)$ by a fixed maximum distance separable (MDS) matrix:
  $$\begin{pmatrix} s_{0,c}' \\ s_{1,c}' \\ s_{2,c}' \\ s_{3,c}' \end{pmatrix} = \begin{pmatrix} 02 & 03 & 01 & 01 \\ 01 & 02 & 03 & 01 \\ 01 & 01 & 02 & 03 \\ 03 & 01 & 01 & 02 \end{pmatrix} \begin{pmatrix} s_{0,c} \\ s_{1,c} \\ s_{2,c} \\ s_{3,c} \end{pmatrix}$$
- All multiplications are performed in $GF(2^8)$ modulo $(x^8 + x^4 + x^3 + x + 1)$.
- In the inverse transformation (`InvMixColumns`), the inverse polynomial matrix is:
  $$\begin{pmatrix} 0E & 0B & 0D & 09 \\ 09 & 0E & 0B & 0D \\ 0D & 09 & 0E & 0B \\ 0B & 0D & 09 & 0E \end{pmatrix}$$
- **Omission in Final Round**: `MixColumns` is excluded from the final round ($N_r = 10$) so that the cipher structure allows the encryption and decryption transformations to be mirror-symmetric.

#### 4. `AddRoundKey`
- The 128-bit state matrix is bitwise XORed with the 128-bit round subkey (represented as 4 columns of 32-bit words $W[4i]$ to $W[4i+3]$):
  $$s_{r,c}' = s_{r,c} \oplus w_{c,r}$$
- `AddRoundKey` is its own inverse ($A \oplus K \oplus K = A$).

### Key Expansion Algorithm
The AES key expansion takes the 128-bit key ($N_k = 4$ words) and produces a linear array of $4(N_r + 1) = 44$ words (each 32 bits, denoted $W[0]$ to $W[43]$).
- For $i = 0$ to $3$: $W[i]$ contains the master key bytes directly.
- For $i = 4$ to $43$:
  - Let $T = W[i-1]$.
  - If $i \equiv 0 \pmod 4$:
    - $T = \text{SubWord}(\text{RotWord}(T)) \oplus Rcon[i/4]$
    - `RotWord`: Circular left shift of the 4 bytes in word $T$: $(b_0, b_1, b_2, b_3) \rightarrow (b_1, b_2, b_3, b_0)$.
    - `SubWord`: Applies the AES S-box substitution independently to each of the 4 bytes in word $T$.
    - $Rcon[j]$: Round constant word defined as $(RC[j], 0x00, 0x00, 0x00)$ where $RC[1] = 0x01$, $RC[2] = 0x02$, $RC[3] = 0x04$, $RC[4] = 0x08$, $RC[5] = 0x10$, $RC[6] = 0x20$, $RC[7] = 0x40$, $RC[8] = 0x80$, $RC[9] = 0x1B$, $RC[10] = 0x36$.
  - $W[i] = W[i - 4] \oplus T$.

---

## 2. Example: Multiplication by $02$ in $GF(2^8)$
In AES `MixColumns`, multiplication by $02$ (denoted `xtime(b)`) corresponds to multiplying by $x$ in $GF(2^8)$:
- Shift $b$ left by 1 bit ($b \ll 1$).
- If the original most significant bit of $b$ was 1:
  XOR the shifted result with the reduction byte `0x1B` ($x^4 + x^3 + x + 1$).
- **Example**: Calculate $02 \odot 0x57$:
  - $0x57 = (01010111)_2$. Most significant bit is $0$.
  - Shift left by 1: $(10101110)_2 = 0xAE$.
  - Result: $0xAE$.
- **Example**: Calculate $02 \odot 0xAE$:
  - $0xAE = (10101110)_2$. Most significant bit is $1$.
  - Shift left by 1: $(01011100)_2 = 0x5C$.
  - XOR with `0x1B`: $0x5C \oplus 0x1B = (01011100)_2 \oplus (00011011)_2 = (01000111)_2 = 0x47$.
  - Result: $0x47$.

---

## 3. Applications & Use Cases
1. **TLS 1.3 / HTTPS**: AES-GCM (Galois/Counter Mode) with 128-bit or 256-bit keys encrypts over 90% of global web traffic, offering authenticated symmetric encryption.
2. **Hardware Acceleration (Intel AES-NI & ARMv8 Crypto Extensions)**: Modern CPU instruction sets implement single-cycle hardware instructions (`AESENC`, `AESENCLAST`, `AESDEC`, `AESIMC`) executing AES at over 10 GB/s per core.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: `MixColumns` First Element Computation [KTU Analytical Model]
**Problem**:
Given a state column $C = \begin{pmatrix} 0x02 \\ 0x01 \\ 0x01 \\ 0x03 \end{pmatrix}$, compute the first output byte $s_{0}'$ after `MixColumns`.

**Step-by-step Solution**:
- MixColumns matrix row 0 is: $\begin{pmatrix} 02 & 03 & 01 & 01 \end{pmatrix}$.
- Formula:
  $$s_{0}' = (02 \odot 0x02) \oplus (03 \odot 0x01) \oplus (01 \odot 0x01) \oplus (01 \odot 0x03)$$
- Compute each term in $GF(2^8)$:
  1. $02 \odot 0x02 = (00000010)_2 \ll 1 = (00000100)_2 = 0x04$.
  2. $03 \odot 0x01 = (02 \oplus 01) \odot 0x01 = (02 \odot 0x01) \oplus 0x01 = 0x02 \oplus 0x01 = 0x03$.
  3. $01 \odot 0x01 = 0x01$.
  4. $01 \odot 0x03 = 0x03$.
- XOR all terms:
  $$s_{0}' = 0x04 \oplus 0x03 \oplus 0x01 \oplus 0x03$$
  $$0x04 \oplus 0x03 = (00000100)_2 \oplus (00000011)_2 = (00000111)_2 = 0x07$$
  $$0x07 \oplus 0x01 = 0x06$$
  $$0x06 \oplus 0x03 = (00000110)_2 \oplus (00000011)_2 = (00000101)_2 = 0x05$$
- **Output byte**: $\mathbf{s_{0}' = 0x05}$.

---

### Example 2: `ShiftRows` State Transformation
**Problem**:
Given the $4 \times 4$ AES state matrix:
$$\begin{pmatrix} 01 & 05 & 09 & 0D \\ 02 & 06 & 0A & 0E \\ 03 & 07 & 0B & 0F \\ 04 & 08 & 0C & 10 \end{pmatrix}$$
Apply `ShiftRows` and display the resulting state matrix.

**Step-by-step Solution**:
- Row 0 (Shift 0): $(01, 05, 09, 0D) \rightarrow (01, 05, 09, 0D)$.
- Row 1 (Shift 1 left): $(02, 06, 0A, 0E) \rightarrow (06, 0A, 0E, 02)$.
- Row 2 (Shift 2 left): $(03, 07, 0B, 0F) \rightarrow (0B, 0F, 03, 07)$.
- Row 3 (Shift 3 left): $(04, 08, 0C, 10) \rightarrow (10, 04, 08, 0C)$.
- Resulting State Matrix:
$$\begin{pmatrix} 01 & 05 & 09 & 0D \\ 06 & 0A & 0E & 02 \\ 0B & 0F & 03 & 07 \\ 10 & 04 & 08 & 0C \end{pmatrix}$$

---

### Example 3: Key Expansion Word $W[4]$ Calculation
**Problem**:
Let the master key words be:
$W[0] = \text{0x2B7E1516}$, $W[1] = \text{0x28AED2A6}$, $W[2] = \text{0xABF71588}$, $W[3] = \text{0x09CF4F3C}$.
Compute $W[4]$ using the AES Key Expansion algorithm.
(Given: S-box lookup values: $\text{S-box}(4F) = 84$, $\text{S-box}(3C) = EB$, $\text{S-box}(09) = 01$, $\text{S-box}(CF) = 8A$).

**Step-by-step Solution**:
1. Since $i = 4 \equiv 0 \pmod 4$:
   - Let $T = W[3] = \text{0x09CF4F3C} = (09, CF, 4F, 3C)$.
2. Apply `RotWord`:
   $$\text{RotWord}(09, CF, 4F, 3C) = (CF, 4F, 3C, 09)$$
3. Apply `SubWord`:
   - $\text{S-box}(CF) = 8A$
   - $\text{S-box}(4F) = 84$
   - $\text{S-box}(3C) = EB$
   - $\text{S-box}(09) = 01$
   $$\text{SubWord} = (8A, 84, EB, 01) = \text{0x8A84EB01}$$
4. XOR with Round Constant $Rcon[1] = \text{0x01000000}$:
   $$\text{0x8A84EB01} \oplus \text{0x01000000} = \text{0x8B84EB01}$$
5. Compute $W[4] = W[0] \oplus T$:
   $$W[4] = \text{0x2B7E1516} \oplus \text{0x8B84EB01}$$
   $$\begin{array}{r@{\quad}l}
     2B7E1516 & = 00101011 \ 01111110 \ 00010101 \ 00010110 \\
   \oplus \ 8B84EB01 & = 10001011 \ 10000100 \ 11101011 \ 00000001 \\
   \hline
     A0FAFE17 & = 10100000 \ 11111010 \ 11111110 \ 00010111
   \end{array}$$
   $$\mathbf{W[4] = \text{0xA0FAFE17}}$$

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q3 - 4 Marks]
**Question**: Discuss the key expansion procedure in AES.

**Solution**:
1. **Objective & Output**:
   The AES key expansion takes the original cipher key of $N_k$ 32-bit words (for AES-128, $N_k = 4$ words, 16 bytes) and expands it into an expanded key schedule consisting of $N_b \times (N_r + 1) = 4 \times 11 = 44$ words (each 32 bits, denoted $W[0]$ to $W[43]$).
   Each round uses 4 consecutive words ($16 \text{ bytes} = 128 \text{ bits}$) as its round subkey.

2. **Algorithm Execution**:
   - **Base Initialization**: The first $N_k$ words ($W[0], W[1], W[2], W[3]$) are initialized directly with the 16 bytes of the master cipher key.
   - **Recursive Generation Loop**: For $i$ from 4 to 43:
     - Set temporary word $T = W[i-1]$.
     - If $i$ is a multiple of 4 ($i \bmod 4 == 0$):
       1. **RotWord**: Performs a 1-byte cyclic left shift on the 4 bytes of $T$:
          $$(b_0, b_1, b_2, b_3) \xrightarrow{\text{RotWord}} (b_1, b_2, b_3, b_0)$$
       2. **SubWord**: Replaces each byte in $T$ with its non-linear substitution byte using the AES S-box lookup table.
       3. **Rcon Addition**: XORs the result with a round-dependent constant word $Rcon[i/4]$:
          $$Rcon[j] = (RC[j], 0x00, 0x00, 0x00)$$
          where $RC[1] = 0x01$, $RC[2] = 0x02$, $RC[3] = 0x04$, $RC[4] = 0x08$, $RC[5] = 0x10$, $RC[6] = 0x20$, etc.
     - Finally, word $W[i]$ is computed by XORing $W[i - 4]$ with $T$:
       $$W[i] = W[i - 4] \oplus T$$

3. **Cryptographic Strength of Key Schedule**:
   - High diffusion: Knowledge of a part of the key schedule does not easily yield the other subkeys.
   - Non-linearity: The use of `SubWord` introduces non-linearity, preventing slide and related-key attacks.

---

### Question 2 [KTU May 2019, Part B, Q12(b) - 5 Marks]
**Question**: Discuss Mix Column transformation in AES.

**Solution**:
1. **Overview & Role**:
   `MixColumns` is the primary diffusion mechanism in AES. It operates column-by-column on the $4 \times 4$ State Matrix, mixing all 4 bytes of each column so that after a single round, any change to a single byte in the input spreads across all 4 bytes of the column.

2. **Mathematical Definition**:
   Each column of the state matrix is treated as a four-term polynomial over the Galois Field $GF(2^8)$ and is multiplied modulo $(x^4 + 1)$ with a fixed polynomial:
   $$c(x) = \{03\}x^3 + \{01\}x^2 + \{01\}x + \{02\}$$
   In matrix multiplication form:
   $$\begin{pmatrix} s_{0,c}' \\ s_{1,c}' \\ s_{2,c}' \\ s_{3,c}' \end{pmatrix} = \begin{pmatrix} 02 & 03 & 01 & 01 \\ 01 & 02 & 03 & 01 \\ 01 & 01 & 02 & 03 \\ 03 & 01 & 01 & 02 \end{pmatrix} \begin{pmatrix} s_{0,c} \\ s_{1,c} \\ s_{2,c} \\ s_{3,c} \end{pmatrix}$$

3. **Field Arithmetic in $GF(2^8)$**:
   - Addition is bitwise XOR ($\oplus$).
   - Multiplication by $01$: $01 \odot b = b$.
   - Multiplication by $02$: Corresponds to a 1-bit left shift ($b \ll 1$). If the high-order bit before the shift was 1, the result is XORed with the irreducible reduction byte `0x1B` ($x^8 + x^4 + x^3 + x + 1$):
     $$\{02\} \odot b = \begin{cases} b \ll 1 & \text{if MSB}(b) = 0 \\ (b \ll 1) \oplus 0x1B & \text{if MSB}(b) = 1 \end{cases}$$
   - Multiplication by $03$: $\{03\} \odot b = (\{02\} \odot b) \oplus b$.

4. **Maximum Distance Separable (MDS) Property**:
   The fixed circulant matrix is a Maximum Distance Separable (MDS) matrix with branch number 5. This guarantees that if one byte in a column is changed, at least four output bytes change after `MixColumns`.

---

### Question 3 [KTU May 2019, Part B, Q13(b) - 5 Marks]
**Question**: Illustrate inverse S box creation in AES.

**Solution**:
1. **Theoretical Foundations of AES S-Box**:
   The AES S-Box is an algebraic mapping $S: GF(2^8) \rightarrow GF(2^8)$ constructed via two distinct mathematical operations:
   - **Step 1**: Non-linear multiplicative inversion in the Galois Field $GF(2^8)$ modulo the irreducible polynomial $m(x) = x^8 + x^4 + x^3 + x + 1$ ($0x11B$). The byte $0x00$ maps to itself.
   - **Step 2**: An affine transformation over $GF(2)$:
     $$\mathbf{b}' = \mathbf{A} \cdot \mathbf{b} \oplus \mathbf{c}$$
     where $\mathbf{A}$ is a fixed $8 \times 8$ binary circulant matrix and $\mathbf{c} = (01100011)_2 = 0x63$.

2. **Inverse S-Box Creation Procedure**:
   To create the **Inverse S-Box ($S^{-1}$)**, the two transformations are reversed in exact opposite order:
   - **Step 1 (Inverse Affine Transformation)**:
     Apply the inverse affine mapping to the output byte $\mathbf{y}$:
     $$\mathbf{b} = \mathbf{A}^{-1} \cdot (\mathbf{y} \oplus \mathbf{c}) = \mathbf{A}^{-1} \cdot \mathbf{y} \oplus \mathbf{d}$$
     where the inverse constant vector is $\mathbf{d} = (00000101)_2 = 0x05$, and $\mathbf{A}^{-1}$ is the matrix:
     $$\mathbf{A}^{-1} = \begin{pmatrix}
     0 & 0 & 1 & 0 & 0 & 1 & 0 & 1 \\
     1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
     0 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\
     1 & 0 & 1 & 0 & 0 & 1 & 0 & 0 \\
     0 & 1 & 0 & 1 & 0 & 0 & 1 & 0 \\
     0 & 0 & 1 & 0 & 1 & 0 & 0 & 1 \\
     1 & 0 & 0 & 1 & 0 & 1 & 0 & 0 \\
     0 & 1 & 0 & 0 & 1 & 0 & 1 & 0
     \end{pmatrix}$$
     Expressed coordinate-wise for bit $i \in \{0 \dots 7\}$:
     $$b_i = y_{(i+2) \bmod 8} \oplus y_{(i+5) \bmod 8} \oplus y_{(i+7) \bmod 8} \oplus d_i$$
   - **Step 2 (Multiplicative Inversion in $GF(2^8)$)**:
     Compute the multiplicative inverse of the resulting byte $\mathbf{b}$ in $GF(2^8)$ modulo $m(x) = x^8 + x^4 + x^3 + x + 1$ using the Extended Euclidean Algorithm for polynomials:
     $$x = \mathbf{b}^{-1} \in GF(2^8) \quad (\text{with } 0x00 \rightarrow 0x00)$$

3. **Verification**:
   For any byte $a \in GF(2^8)$:
   $$S^{-1}(S(a)) = a$$
   This generates the 256-byte lookup table for `InvSubBytes`.

---

### Question 4 [KTU January 2023, Part B, Q13 / June 2022, Part B, Q13 - 9 Marks]
**Question**: With neat sketch describe the AES encryption and decryption process. Illustrate the single round transformations of AES.

**Solution**:
1. **Overall AES Block Diagram (128-bit Key, 10 Rounds)**:
```
         ENCRYPTION                              DECRYPTION
      128-bit Plaintext                       128-bit Ciphertext
             │                                       │
             ▼                                       ▼
     [ AddRoundKey ] (K_0)                   [ AddRoundKey ] (K_10)
             │                                       │
      ┌──────┴──────┐                         ┌──────┴──────┐
      │   Round 1   │                         │   Round 1   │
      │ 1. SubBytes │                         │ 1. InvShiftRows
      │ 2. ShiftRows│                         │ 2. InvSubBytes
      │ 3. MixCols  │                         │ 3. AddRoundKey (K_9)
      │ 4. AddKey(K1)                         │ 4. InvMixCols
      └──────┬──────┘                         └──────┬──────┘
             │                                       │
             ▼                                       ▼
      [ Rounds 2-9 ]                          [ Rounds 2-9 ]
             │                                       │
      ┌──────┴──────┐                         ┌──────┴──────┐
      │  Round 10   │                         │  Round 10   │
      │ 1. SubBytes │                         │ 1. InvShiftRows
      │ 2. ShiftRows│                         │ 2. InvSubBytes
      │(No MixCols!)│                         │(No InvMixCols!)
      │ 3. AddKey(K10)                        │ 3. AddRoundKey (K_0)
      └──────┬──────┘                         └──────┬──────┘
             │                                       │
             ▼                                       ▼
     128-bit Ciphertext                       128-bit Plaintext
```

2. **Detailed Single-Round Transformations**:
   - **`SubBytes`**: Replaces each state byte with its S-box entry (multiplicative inverse in $GF(2^8)$ followed by affine mapping). Provides Shannon's Confusion.
   - **`ShiftRows`**: Row 0 shifted by 0, Row 1 shifted left by 1, Row 2 by 2, Row 3 by 3 bytes. Provides intra-column to inter-column diffusion.
   - **`MixColumns`**: Multiplies each column by the fixed MDS matrix over $GF(2^8)$ modulo $(x^4+1)$. Disperses each byte's impact across 4 bytes.
   - **`AddRoundKey`**: Bitwise XOR of the 128-bit state with the 128-bit round subkey derived from the key expansion schedule.

3. **Equivalent Decryption Transformations**:
   - Decryption performs the exact inverse operations: `InvShiftRows`, `InvSubBytes`, `AddRoundKey`, and `InvMixColumns`.
   - In Round 10 of encryption and Round 1 of decryption, the column mixing step is omitted, maintaining exact structural balance between encryption and decryption paths.
