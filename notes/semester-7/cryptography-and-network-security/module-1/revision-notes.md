# Module 1: Revision Notes — Quick Review & High-Yield Summary

## Submodule 1: Symmetric Cipher Models & Classical Ciphers
- **Symmetric Model**: $C = E(K, P)$, $P = D(K, C)$. Five components: Plaintext, Encryption Algorithm, Secret Key, Ciphertext, Decryption Algorithm.
- **Caesar Cipher**: $C = (P + k) \bmod 26$, key space $|K| = 25$. Easily broken via brute force.
- **Monoalphabetic Substitution**: Arbitrary mapping of 26 letters ($26!$ keys). Broken by frequency analysis ('E' is most common English letter).
- **Playfair Cipher**: $5 \times 5$ grid constructed from keyword (I/J combined). Encrypts digraphs. Rules: same row $\rightarrow$ right; same column $\rightarrow$ down; rectangle $\rightarrow$ opposite corners; identical letters $\rightarrow$ insert filler 'X'.
- **Hill Cipher**: $\mathbf{C} = \mathbf{P} \cdot \mathbf{K} \pmod{26}$. Invertible if $\gcd(\det(\mathbf{K}), 26) = 1$. $\mathbf{K}^{-1} = (\det \mathbf{K})^{-1} \cdot \text{adj}(\mathbf{K}) \pmod{26}$.
- **Vigenère Cipher**: Polyalphabetic cipher using repeating key: $C_i = (P_i + K_{i \bmod m}) \bmod 26$. Broken by Kasiski method.
- **One-Time Pad**: Truly random key of message length used once. Perfect secrecy (unconditionally secure).
- **Transposition**: Rail fence (zigzag depth), Columnar transposition (permutation matrix).
- **Steganography**: Hiding existence of message. LSB image/audio manipulation.

---

## Submodule 2: Feistel Principles & Data Encryption Standard (DES)
- **Claude Shannon Principles**:
  - **Confusion**: Obscures key-ciphertext relation via non-linear substitution (S-boxes).
  - **Diffusion**: Spreads plaintext statistics across ciphertext via permutation/transposition (Avalanche effect).
- **Feistel Architecture**: Split block into $L_0, R_0$. In round $i$: $L_i = R_{i-1}$, $R_i = L_{i-1} \oplus F(R_{i-1}, K_i)$. Decryption runs same algorithm with reversed subkeys.
- **DES Specifications**: 64-bit block size, 56-bit effective key (64 bits with 8 parity bits), 16 Feistel rounds.
  - Round function: Expansion $E$ ($32 \rightarrow 48$ bits), XOR with 48-bit subkey $K_i$, eight $6 \times 4$ S-boxes ($48 \rightarrow 32$ bits), Permutation $P$ (32 bits).
  - **Non-linearity**: S-boxes are the *only* non-linear component in DES.
- **Simplified DES (S-DES)**: 8-bit block, 10-bit key, 2 rounds.
  - Subkey generation: $P_{10} = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]$, split, $LS-1$, $P_8$ gives $K_1$; $LS-2$, $P_8$ gives $K_2$.
  - Round function: $E/P = [4, 1, 2, 3, 2, 3, 4, 1]$, $S_0, S_1$, $P_4 = [2, 4, 3, 1]$.
- **Cryptanalysis**: Exhaustive brute force ($2^{56}$ operations), Differential Cryptanalysis ($2^{47}$ chosen plaintexts), Linear Cryptanalysis ($2^{43}$ known plaintexts).

---

## Submodule 3: Block Cipher Design Principles & Modes of Operation
- **Design Principles**: SAC (Strict Avalanche Criterion), BIC (Bit Independence Criterion), high non-linearity in S-boxes, sufficient rounds to exceed brute-force complexity.
- **Five Standard Modes**:
  1. **ECB (Electronic Codebook)**: $C_i = E_K(P_i)$. Leaks data repetition patterns.
  2. **CBC (Cipher Block Chaining)**: $C_i = E_K(P_i \oplus C_{i-1})$, $C_0 = IV$. Sequential, 1-bit ciphertext error scrambles $P_i$ and inverts 1 bit in $P_{i+1}$.
  3. **CFB (Cipher Feedback)**: Stream cipher mode using block cipher encryption primitive.
  4. **OFB (Output Feedback)**: Keystream generated independently of plaintext. Zero error propagation.
  5. **CTR (Counter)**: $C_i = P_i \oplus E_K(T_i)$. Fully parallelizable in hardware/software, allows random access, zero error propagation.

---

## Submodule 4: High-Yield Formulas & Exam Cheatsheet
- Modular inverse of determinant for Hill Cipher:
  $$(\det \mathbf{K}) \cdot x \equiv 1 \pmod{26}$$
  Common inverses mod 26: $1^{-1}=1, 3^{-1}=9, 5^{-1}=21, 7^{-1}=15, 9^{-1}=3, 11^{-1}=19, 15^{-1}=7, 17^{-1}=23, 19^{-1}=11, 21^{-1}=5, 23^{-1}=17, 25^{-1}=25$.
- S-DES Subkey Steps:
  $$K \xrightarrow{P_{10}} (L_0, R_0) \xrightarrow{LS-1} (L_1, R_1) \xrightarrow{P_8} K_1$$
  $$(L_1, R_1) \xrightarrow{LS-2} (L_2, R_2) \xrightarrow{P_8} K_2$$
- S-Box coordinates: Row $= \text{bit}_1 \parallel \text{bit}_n$, Column $= \text{middle bits}$.
