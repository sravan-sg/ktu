# Module 2: Revision Notes — Quick Review & High-Yield Summary

## Submodule 1: International Data Encryption Algorithm (IDEA)
- **Parameters**: 64-bit plaintext block, 128-bit key, 8 rounds + 1 output transformation.
- **Algebraic Primitives**: 
  1. $\oplus$: Bitwise XOR (addition in $GF(2)^{16}$).
  2. $\boxplus$: Addition modulo $2^{16}$ (additive group $\mathbb{Z}_{2^{16}}$).
  3. $\odot$: Multiplication modulo $2^{16}+1 = 65,537$ (prime field $GF(65537)$). Value $0x0000$ represents $2^{16} = 65,536$.
- **Key Expansion**: 128-bit key produces 52 subkeys of 16 bits each. Key is partitioned into 8 subkeys, then rotated left cyclically by 25 bits repeatedly.
- **Round Keys**: Rounds 1 to 8 use 6 subkeys each ($8 \times 6 = 48$). Output transformation uses 4 subkeys ($48 + 4 = 52$).
- **Decryption**: Uses identical structure with inverse subkeys:
  - Additive inverse: $U = (2^{16} - Z) \bmod 2^{16}$.
  - Multiplicative inverse: $U \odot Z \equiv 1 \pmod{65537}$ via Extended Euclidean Algorithm.
  - XOR subkeys: $U = Z$.

---

## Submodule 2: Advanced Encryption Standard (AES)
- **Parameters**: SPN network, 128-bit block, State matrix is $4 \times 4$ bytes.
  - AES-128: 10 rounds, 44 key words ($W[0 \dots 43]$).
  - AES-192: 12 rounds, 52 key words.
  - AES-256: 14 rounds, 60 key words.
- **Four Round Transformations**:
  1. `SubBytes`: Byte-by-byte non-linear S-box lookup. Multiplicative inverse in $GF(2^8)$ with polynomial $m(x) = x^8 + x^4 + x^3 + x + 1$ ($0x11B$) + affine transformation.
  2. `ShiftRows`: Cyclically shifts row $r$ left by $r$ bytes ($r \in \{0, 1, 2, 3\}$).
  3. `MixColumns`: Multiplies each column by MDS circulant matrix over $GF(2^8)$. Omitted in final round 10!
  4. `AddRoundKey`: Bitwise XOR of State with 128-bit round subkey.
- **Key Schedule**:
  $$W[i] = W[i-4] \oplus T$$
  If $i \bmod 4 == 0$: $T = \text{SubWord}(\text{RotWord}(W[i-1])) \oplus Rcon[i/4]$.

---

## Submodule 3: Stream Ciphers & RC4
- **Stream Cipher Model**: $C_i = P_i \oplus k_i$, $P_i = C_i \oplus k_i$. Emulates one-time pad with pseudorandom keystream generator.
- **RC4 State**: 256-byte permutation array $S$, pointers $i, j \in \{0 \dots 255\}$.
- **KSA (Key-Scheduling Algorithm)**:
  - Initialize $S[i] = i$.
  - $j = (j + S[i] + K[i \bmod L]) \bmod 256$, `swap(S[i], S[j])`.
- **PRGA (Keystream Generation)**:
  - $i = (i + 1) \bmod 256$, $j = (j + S[i]) \bmod 256$, `swap(S[i], S[j])`.
  - $t = (S[i] + S[j]) \bmod 256$, Keystream byte $k = S[t]$.
- **Weaknesses**: Fluhrer-Mantin-Shamir (FMS) bias in initial bytes; WEP 24-bit IV reuse vulnerability. Deprecated in modern TLS.

---

## Submodule 4: High-Yield Formulas & Exam Cheatsheet
- Multiplicative inverse in IDEA:
  $$Z \cdot U \equiv 1 \pmod{65537}$$
- AES `MixColumns` byte multiplication:
  $$\{02\} \odot b = \begin{cases} b \ll 1 & \text{if MSB}(b) = 0 \\ (b \ll 1) \oplus 0x1B & \text{if MSB}(b) = 1 \end{cases}$$
  $$\{03\} \odot b = (\{02\} \odot b) \oplus b$$
- AES Inverse S-Box: Inverse affine mapping followed by multiplicative inversion in $GF(2^8)$.
- RC4 PRGA byte emission: $t = (S[i] + S[j]) \bmod 256$, $k = S[t]$.
