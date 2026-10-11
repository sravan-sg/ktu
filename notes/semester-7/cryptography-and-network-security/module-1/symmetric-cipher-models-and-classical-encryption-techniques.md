# Symmetric Cipher Models and Classical Encryption Techniques

## 1. Explanation
In symmetric-key cryptography (also called conventional, private-key, or single-key encryption), communicating entities share a single secret key $K$. The same key is utilized both for encrypting plaintext $P$ into ciphertext $C$ and for decrypting $C$ back into $P$. Formally:
$$C = E(K, P)$$
$$P = D(K, C) = D(K, E(K, P))$$

### Core Symmetric Model Components
According to William Stallings (*Cryptography and Network Security*, Chapter 2) and Behrouz Forouzan, any symmetric cryptosystem consists of five distinct components:
1. **Plaintext ($P$)**: The original unencrypted message or data that feeds into the algorithm.
2. **Encryption Algorithm ($E$)**: A mathematical transformation performing substitutions and transpositions on the plaintext.
3. **Secret Key ($K$)**: A value independent of the plaintext that dictates the exact transformation.
4. **Ciphertext ($C$)**: The scrambled output produced by the encryption algorithm.
5. **Decryption Algorithm ($D$)**: The inverse operation running $E$ backward with the identical key $K$.

```
                 Secret Key K                         Secret Key K
                      │                                    │
                      ▼                                    ▼
Plaintext P ───► [ Encryption E ] ───► Ciphertext C ───► [ Decryption D ] ───► Plaintext P
```

### Classical Cryptographic Techniques

#### 1. Substitution Techniques
In substitution ciphers, characters, bit sequences, or blocks of plaintext are replaced by other characters, bit sequences, or blocks.
- **Caesar Cipher (Shift Cipher)**: Replaces each plaintext character $p$ with character $c$ shifted by $k$ positions:
  $$c = (p + k) \bmod 26, \quad p = (c - k) \bmod 26$$
  With an alphabet of 26 letters, the key space $|K| = 25$, making it vulnerable to exhaustive brute-force search.
- **Monoalphabetic Substitution Cipher**: Replaces each alphabet character with an arbitrary fixed mapping from a 26-letter permutation. Key space is $26! \approx 4 \times 10^{26}$. Despite this large key space, it is readily broken by **frequency analysis** because language letter frequencies (e.g., 'E', 'T', 'A', 'O', 'I', 'N' in English) and digraph/trigraph patterns are directly preserved in the ciphertext.
- **Playfair Cipher**: The best-known multiple-letter substitution cipher, treating digraphs (letter pairs) as single units using a $5 \times 5$ matrix generated from a keyword. 
  - Fill the $5 \times 5$ matrix with keyword letters (omitting duplicates), then fill remaining slots with remaining alphabet (treating I and J as the same cell).
  - Rules for digraph encryption:
    1. If both letters are in the same row, replace each with the letter immediately to its right (wrapping around to the left).
    2. If both letters are in the same column, replace each with the letter immediately below it (wrapping around to the top).
    3. If they form opposite corners of a rectangle, replace each letter with the letter in the same row and the column of the other letter.
    4. If both letters are identical (e.g., "balloon" $\rightarrow$ "ba", "ll", "oo", "n"), insert a filler letter (typically 'X').
- **Hill Cipher**: An analytical polygraphic substitution cipher invented by Lester Hill (1929) utilizing linear algebra over modular arithmetic $\mathbb{Z}_{26}$. Plaintext blocks of length $m$ are represented as row vectors and multiplied by an $m \times m$ invertible key matrix $\mathbf{K}$:
  $$\mathbf{C} = \mathbf{P} \cdot \mathbf{K} \pmod{26}$$
  $$\mathbf{P} = \mathbf{C} \cdot \mathbf{K}^{-1} \pmod{26}$$
  A key matrix $\mathbf{K}$ is invertible modulo 26 if and only if $\gcd(\det(\mathbf{K}), 26) = 1$. The inverse matrix is:
  $$\mathbf{K}^{-1} = (\det(\mathbf{K}))^{-1} \cdot \text{adj}(\mathbf{K}) \pmod{26}$$
- **Polyalphabetic Ciphers (Vigenère Cipher)**: Uses different monoalphabetic substitutions throughout the message governed by a repeating keyword. If keyword length is $m$, the ciphertext character $c_i$ for plaintext $p_i$ is:
  $$c_i = (p_i + k_{i \bmod m}) \bmod 26$$
  It flattens frequency distribution spikes, but is broken via Kasiski examination and the Index of Coincidence to determine key length $m$.
- **One-Time Pad (Vernam Cipher)**: Invented by Gilbert Vernam and proven unconditionally secure (perfect secrecy) by Claude Shannon (1949). It uses a truly random, non-repeating key stream of length equal to the message. The key is used only once:
  $$c_i = p_i \oplus k_i, \quad p_i = c_i \oplus k_i$$

#### 2. Transposition Techniques
Transposition ciphers do not alter the identity of characters; instead, they permute their physical order, redistributing letter positions.
- **Rail Fence Cipher**: Writes plaintext as a sequence of diagonals down and up across a given depth $d$ of rails, then reads off horizontally row by row.
- **Row Transposition Cipher (Columnar Transposition)**: Writes the plaintext in a rectangular grid of fixed column width $w$ row by row, and reads off column by column governed by a numerical permutation key.

#### 3. Rotor Machines
Mechanical devices (such as the German Enigma and Hebern machine) using cascaded physical rotating cylinders with internal electrical wiring. Each cylinder provides a distinct monoalphabetic substitution. As a key is pressed, one or more rotors rotate, continuously shifting the electrical circuit so that the cipher effectively behaves as a polyalphabetic substitution with an astronomical period ($26^3 = 17,576$ for 3 rotors).

#### 4. Steganography
Steganography ("covered writing") conceals the very existence of the communication, contrasting with cryptography which conceals the meaning of a message.
- **Techniques**:
  1. *Least Significant Bit (LSB) Insertion*: Overwrites the low-order bit of digital pixels (in 24-bit RGB BMP/PNG images) or audio samples. A change of 1 LSB in color intensity is imperceptible to the human eye.
  2. *Invisible Inks & Microdots*: Physical chemical methods.
  3. *Whitespace and Linguistic Steganography*: Inserting imperceptible tabs or spaces at line ends in source code or text files.
  4. *Covert Channels*: Hiding payload data inside unused IP header fields or TCP sequence numbers.

---

## 2. Example
### Playfair Cipher Example
- **Keyword**: `"MONARCHY"`
- **Matrix construction** (combining I and J):
```
M  O  N  A  R
C  H  Y  B  D
E  F  G  I  K
L  P  Q  S  T
U  V  W  X  Z
```
- **Plaintext**: `"INSTRUMENT"`
- Form digraphs: `IN`, `ST`, `RU`, `ME`, `NT`
- **Encryption**:
  - `IN`: `I` (row 3, col 4) and `N` (row 1, col 3) $\rightarrow$ Rectangle corners $\rightarrow$ `A` and `G` $\rightarrow$ `AG`
  - `ST`: `S` (row 4, col 4) and `T` (row 4, col 5) $\rightarrow$ Same row $\rightarrow$ Shift right $\rightarrow$ `TL`
  - `RU`: `R` (row 1, col 5) and `U` (row 5, col 1) $\rightarrow$ Rectangle corners $\rightarrow$ `M` and `Z` $\rightarrow$ `MZ`
  - `ME`: `M` (row 1, col 1) and `E` (row 3, col 1) $\rightarrow$ Same column $\rightarrow$ Shift down $\rightarrow$ `CL`
  - `NT`: `N` (row 1, col 3) and `T` (row 4, col 5) $\rightarrow$ Rectangle corners $\rightarrow$ `R` and `Q` $\rightarrow$ `RQ`
- **Resulting Ciphertext**: `"AGTLMZCLRQ"`

---

## 3. Applications & Use Cases
1. **Network Packet Anonymization & Metadata Scrubbing**: Modern protocols utilize transposition-based permutation layers (P-boxes in AES/DES) to disperse protocol headers across frames.
2. **Digital Watermarking**: LSB image and audio steganography is applied commercially to embed copyright hashes, ownership signatures, and transaction IDs inside media streams without perceptual distortion.
3. **Hardened Defense Against Side-Channel Leakage**: Permutation matrices derived from transposition theory are deployed inside hardware cryptoprocessors to shuffle instruction pipelines and mask power consumption traces.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Hill Cipher $2 \times 2$ Matrix Encryption and Decryption [KTU Analytical Model]
**Problem**:
Given key matrix $\mathbf{K} = \begin{pmatrix} 9 & 4 \\ 5 & 7 \end{pmatrix} \pmod{26}$, encrypt plaintext `"MEET"` and show the complete decryption steps.

**Step-by-step Solution**:
1. Numerical encoding ($A=0, B=1, \dots, Z=25$):
   $$\text{"ME"} = (12, 4), \quad \text{"ET"} = (4, 19)$$
2. Encrypt first block $(12, 4)$:
   $$\mathbf{C}_1 = (12, 4) \begin{pmatrix} 9 & 4 \\ 5 & 7 \end{pmatrix} = (12 \times 9 + 4 \times 5, \quad 12 \times 4 + 4 \times 7) = (108 + 20, \quad 48 + 28) = (128, 76)$$
   Reducing modulo 26:
   $$128 \bmod 26 = 24 \ (\text{'Y'}), \quad 76 \bmod 26 = 24 \ (\text{'Y'})$$
3. Encrypt second block $(4, 19)$:
   $$\mathbf{C}_2 = (4, 19) \begin{pmatrix} 9 & 4 \\ 5 & 7 \end{pmatrix} = (4 \times 9 + 19 \times 5, \quad 4 \times 4 + 19 \times 7) = (36 + 95, \quad 16 + 133) = (131, 149)$$
   Reducing modulo 26:
   $$131 \bmod 26 = 1 \ (\text{'B'}), \quad 149 \bmod 26 = 19 \ (\text{'T'})$$
   **Ciphertext**: `"YYBT"`.

4. **Decryption (Matrix Inversion)**:
   $$\det(\mathbf{K}) = (9 \times 7 - 4 \times 5) = 63 - 20 = 43 \equiv 17 \pmod{26}$$
   Find multiplicative inverse of $17 \bmod 26$:
   $$17 \times x \equiv 1 \pmod{26} \implies 17 \times 23 = 391 = 15 \times 26 + 1 \implies (\det(\mathbf{K}))^{-1} = 23$$
   Adjugate matrix:
   $$\text{adj}(\mathbf{K}) = \begin{pmatrix} 7 & -4 \\ -5 & 9 \end{pmatrix} \equiv \begin{pmatrix} 7 & 22 \\ 21 & 9 \end{pmatrix} \pmod{26}$$
   $$\mathbf{K}^{-1} = 23 \begin{pmatrix} 7 & 22 \\ 21 & 9 \end{pmatrix} = \begin{pmatrix} 161 & 506 \\ 483 & 207 \end{pmatrix} \pmod{26} = \begin{pmatrix} 5 & 12 \\ 15 & 25 \end{pmatrix}$$
5. Decrypt first block $(24, 24)$:
   $$\mathbf{P}_1 = (24, 24) \begin{pmatrix} 5 & 12 \\ 15 & 25 \end{pmatrix} = (24 \times 5 + 24 \times 15, \quad 24 \times 12 + 24 \times 25) = (480, 888)$$
   $$480 \bmod 26 = 12 \ (\text{'M'}), \quad 888 \bmod 26 = 4 \ (\text{'E'})$$
   Plaintext `"ME"` successfully recovered!

---

### Example 2: Rail Fence Cipher Tracing [KTU May 2019 Adapted]
**Problem**:
Using a Rail Fence cipher with depth $3$, encrypt the message `"MEET ME AFTER THE TOGA PARTY"`.

**Step-by-step Solution**:
1. Remove spaces from plaintext: `"MEETMEAFTERTHETOGAPARTY"` (Length = 23).
2. Distribute letters down and up across 3 rails:
```
Rail 1: M . . . M . . . E . . . T . . . G . . . R . . . (Indices: 0, 4, 8, 12, 16, 20)
Rail 2: . E . T . E . F . R . H . T . O . A . A . T . (Indices: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21)
Rail 3: . . E . . . A . . . T . . . E . . . P . . . Y (Indices: 2, 6, 10, 14, 18, 22)
```
3. Read row-by-row:
   - Rail 1: `M`, `M`, `E`, `T`, `G`, `R` $\rightarrow$ `"MMETGR"`
   - Rail 2: `E`, `T`, `E`, `F`, `R`, `H`, `T`, `O`, `A`, `A`, `T` $\rightarrow$ `"ETEFHTOAAT"`
   - Rail 3: `E`, `A`, `T`, `E`, `P`, `Y` $\rightarrow$ `"EATEPY"`
4. Concatenated Ciphertext: `"MMETGRETTEFRHTOAATEATEPY"`.

---

### Example 3: Vigenère Cipher Encryption and Decryption [KTU June 2022]
**Problem**:
Encrypt message `"LIFE IS FULL OF SURPRISES"` using the Vigenère cipher with keyword `"HEALTH"`.

**Step-by-step Solution**:
1. Plaintext (no spaces): `"LIFEISFULLOFSURPRISES"` (21 letters).
2. Repeat keyword:
```
Plaintext:  L  I  F  E  I  S  F  U  L  L  O  F  S  U  R  P  R  I  S  E  S
Key:        H  E  A  L  T  H  H  E  A  L  T  H  H  E  A  L  T  H  H  E  A
```
3. Numerical mapping ($A=0, B=1, \dots$):
   - $P = [11, 8, 5, 4, 8, 18, 5, 20, 11, 11, 14, 5, 18, 20, 17, 15, 17, 8, 18, 4, 18]$
   - $K = [7, 4, 0, 11, 19, 7, 7, 4, 0, 11, 19, 7, 7, 4, 0, 11, 19, 7, 7, 4, 0]$
4. Addition modulo 26 ($C_i = (P_i + K_i) \bmod 26$):
   - $11 + 7 = 18 \rightarrow \text{'S'}$
   - $8 + 4 = 12 \rightarrow \text{'M'}$
   - $5 + 0 = 5 \rightarrow \text{'F'}$
   - $4 + 11 = 15 \rightarrow \text{'P'}$
   - $8 + 19 = 27 \equiv 1 \rightarrow \text{'B'}$
   - $18 + 7 = 25 \rightarrow \text{'Z'}$
   - $5 + 7 = 12 \rightarrow \text{'M'}$
   - $20 + 4 = 24 \rightarrow \text{'Y'}$
   - $11 + 0 = 11 \rightarrow \text{'L'}$
   - $11 + 11 = 22 \rightarrow \text{'W'}$
   - $14 + 19 = 33 \equiv 7 \rightarrow \text{'H'}$
   - $5 + 7 = 12 \rightarrow \text{'M'}$
   - $18 + 7 = 25 \rightarrow \text{'Z'}$
   - $20 + 4 = 24 \rightarrow \text{'Y'}$
   - $17 + 0 = 17 \rightarrow \text{'R'}$
   - $15 + 11 = 26 \equiv 0 \rightarrow \text{'A'}$
   - $17 + 19 = 36 \equiv 10 \rightarrow \text{'K'}$
   - $8 + 7 = 15 \rightarrow \text{'P'}$
   - $18 + 7 = 25 \rightarrow \text{'Z'}$
   - $4 + 4 = 8 \rightarrow \text{'I'}$
   - $18 + 0 = 18 \rightarrow \text{'S'}$
5. Ciphertext: `"SMFPBZMYLWHMZYRAKPZIS"`.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part B, Q11(a) - 5 Marks]
**Question**: Differentiate between monoalphabetic ciphers and polyalphabetic ciphers and give one example for each.

**Solution**:
Monoalphabetic and polyalphabetic ciphers represent two distinct paradigms in classical substitution cryptography:

| Comparison Attribute | Monoalphabetic Cipher | Polyalphabetic Cipher |
|---|---|---|
| **Mapping Rule** | Each character in the plaintext alphabet maps to a fixed, unique character in the ciphertext alphabet across the entire message. | A single plaintext character can map to multiple distinct ciphertext characters depending on its position within the message. |
| **Cipher Keys** | Uses a single fixed substitution alphabet or a static shift value $k$. | Uses a sequence of distinct substitution alphabets governed by a periodic key or key stream. |
| **Frequency Analysis Vulnerability** | Highly vulnerable. The natural letter frequency distribution of the source language (e.g., 'E' is 12.7%, 'T' is 9.1%) is directly preserved in the ciphertext. | Resists single-letter frequency analysis. The letter frequency distribution is flattened because each plaintext letter is mapped to different ciphertext letters. |
| **Cryptanalysis Method** | Solved easily via frequency counts, digraph/trigraph identification, and vowel detection. | Requires determining key length first (via Kasiski examination or Index of Coincidence), followed by solving independent monoalphabetic streams. |
| **Classic Example** | **Caesar Cipher**: $C = (P + 3) \bmod 26$. For example, every 'E' always maps to 'H'. | **Vigenère Cipher**: $C_i = (P_i + K_{i \bmod m}) \bmod 26$. With key `"KEY"`, an 'E' at position 0 maps to 'O', but at position 1 maps to 'I'. |

---

### Question 2 [KTU May 2019, Part B, Q11(b) / June 2022, Part A, Q1 - 4 Marks]
**Question**: Differentiate cryptography and steganography. Give different techniques used in steganography.

**Solution**:
1. **Distinction between Cryptography and Steganography**:
   - **Cryptography** scrambles a message to conceal its semantic meaning, converting intelligible plaintext into unintelligible ciphertext. An interceptor is aware that an encrypted message exists, but cannot read it without the key.
   - **Steganography** ("covered writing") conceals the very existence of the communication. The sensitive payload is invisibly embedded inside an innocuous cover medium (such as a carrier image, audio track, or video). An interceptor does not even suspect that secret communication is taking place.

2. **Core Steganographic Techniques**:
   - **Least Significant Bit (LSB) Insertion**: The least significant bit of each color byte in a digital carrier image (e.g., 24-bit RGB) or audio sample is replaced with secret payload bits. Because changes in the least significant bit cause negligible intensity shifts ($< 1/256$ luminance variation), human sensory organs cannot detect the presence of the data.
   - **Audio Steganography (Phase Coding and Echo Hiding)**: Secret bits are embedded by introducing imperceptible echoes (varying the delay between sound waves) or slightly altering the phase of discrete audio frequencies.
   - **Linguistic / Text Steganography**: Information is encoded by manipulating whitespace (inserting varying counts of non-printable spaces and tabs at ends of lines) or using specific word synonym substitutions according to a pre-shared dictionary.
   - **Covert Channels in Network Protocols**: Hiding data inside unused, optional, or padding fields of transport/network headers, such as the IP Identification field, TCP Urgent Pointer, or ICMP payload bytes.

---

### Question 3 [KTU January 2023, Part A, Q1 - 4 Marks]
**Question**: Using Caesar cipher apply brute force attack on the ciphertext `"xjhwjybwnynsl"` and recover the plaintext and the key.

**Solution**:
In the Caesar cipher, encryption is $C = (P + k) \bmod 26$, and decryption is $P = (C - k) \bmod 26$. Because the key space consists of only 25 possible shifts ($k \in \{1, 2, \dots, 25\}$), we apply an exhaustive brute-force search by testing each shift value:

- Ciphertext $C$: `"xjhwjybwnynsl"`
- Let each letter be converted to index $0 \dots 25$:
  `x=23, j=9, h=7, w=22, j=9, y=24, b=1, w=22, n=13, y=24, n=13, s=18, l=11`

Testing candidate shift keys $k$:
- $k = 1$: `w igvixavmxmrk` (Incoherent)
- $k = 2$: `v hfuhwzulwlqj` (Incoherent)
- $k = 3$: `u getgvyktvkpi` (Incoherent)
- $k = 4$: `t fdsfuxjsujoh` (Incoherent)
- $k = 5$: `s ecretwriting` $\rightarrow$ **`"secretwriting"`** (Valid English Plaintext!)

**Verification for $k = 5$**:
- `'x' (23) - 5 = 18 = 's'`
- `'j' (9) - 5 = 4 = 'e'`
- `'h' (7) - 5 = 2 = 'c'`
- `'w' (22) - 5 = 17 = 'r'`
- `'j' (9) - 5 = 4 = 'e'`
- `'y' (24) - 5 = 19 = 't'`
- `'b' (1) - 5 = -4 \equiv 22 = 'w'`
- `'w' (22) - 5 = 17 = 'r'`
- `'n' (13) - 5 = 8 = 'i'`
- `'y' (24) - 5 = 19 = 't'`
- `'n' (13) - 5 = 8 = 'i'`
- `'s' (18) - 5 = 13 = 'n'`
- `'l' (11) - 5 = 6 = 'g'`

**Result**:
- **Recovered Plaintext**: `"secretwriting"`
- **Encryption Key ($k$)**: $5$ (Shift of 5)

---

### Question 4 [KTU January 2023, Part B, Q12(a) - 5 Marks]
**Question**: Using Playfair cipher encrypt the data `"confidential"` with keyword `"security"`.

**Solution**:
1. **Keyword Matrix Construction**:
   - Keyword: `"security"`
   - Unique letters in order: `S, E, C, U, R, I, T, Y` (treating `I` and `J` as one entry).
   - Remaining letters of alphabet: `A, B, D, F, G, H, K, L, M, N, O, P, Q, V, W, X, Z`
   - $5 \times 5$ Playfair Matrix:
```
S    E    C    U    R
I/J  T    Y    A    B
D    F    G    H    K
L    M    N    O    P
Q    V    W    X    Z
```

2. **Plaintext Preparation**:
   - Plaintext: `"confidential"`
   - Digraph segmentation:
     - `co` $\rightarrow$ valid pair
     - `nf` $\rightarrow$ valid pair
     - `id` $\rightarrow$ valid pair
     - `en` $\rightarrow$ valid pair
     - `ti` $\rightarrow$ valid pair
     - `al` $\rightarrow$ valid pair
   - Plaintext pairs: `CO`, `NF`, `ID`, `EN`, `TI`, `AL`

3. **Applying Playfair Rules**:
   - Pair 1: `CO`
     - `C` (Row 1, Col 3), `O` (Row 4, Col 4) $\rightarrow$ Rectangle corners
     - Replace with `U` (Row 1, Col 4) and `N` (Row 4, Col 3) $\rightarrow$ **`UN`**
   - Pair 2: `NF`
     - `N` (Row 4, Col 3), `F` (Row 3, Col 2) $\rightarrow$ Rectangle corners
     - Replace with `M` (Row 4, Col 2) and `G` (Row 3, Col 3) $\rightarrow$ **`MG`**
   - Pair 3: `ID`
     - `I` (Row 2, Col 1), `D` (Row 3, Col 1) $\rightarrow$ Same column (Col 1)
     - Shift down: `I` $\rightarrow$ `D`, `D` $\rightarrow$ `L` $\rightarrow$ **`DL`**
   - Pair 4: `EN`
     - `E` (Row 1, Col 2), `N` (Row 4, Col 3) $\rightarrow$ Rectangle corners
     - Replace with `C` (Row 1, Col 3) and `M` (Row 4, Col 2) $\rightarrow$ **`CM`**
   - Pair 5: `TI`
     - `T` (Row 2, Col 2), `I` (Row 2, Col 1) $\rightarrow$ Same row (Row 2)
     - Shift right: `T` $\rightarrow$ `Y`, `I` $\rightarrow$ `T` $\rightarrow$ **`YT`**
   - Pair 6: `AL`
     - `A` (Row 2, Col 4), `L` (Row 4, Col 1) $\rightarrow$ Rectangle corners
     - Replace with `I` (Row 2, Col 1) and `O` (Row 4, Col 4) $\rightarrow$ **`IO`** (or **`JO`**)

4. **Final Ciphertext**:
   $$\text{"UNMGMDLCMYTIO"}$$
