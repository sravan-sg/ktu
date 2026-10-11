# Module 2: Modern Symmetric Ciphers — Detailed Notes Index

This directory contains in-depth study notes, algebraic analyses, algorithmic walkthroughs, and complete previous year university question solutions for **Module 2: Modern Symmetric Ciphers: IDEA, AES, and Stream Ciphers** of CS409 Cryptography and Network Security.

---

## Topic Detailed Notes Directory

1. [IDEA Cipher Principles and Operations](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/idea-cipher-principles-and-operations.md)
   - Design philosophy: No S-boxes, mixing 3 incompatible algebraic groups on 16-bit sub-blocks (XOR $\oplus$, Addition mod $2^{16}$, Multiplication mod $2^{16}+1$).
   - 128-bit master key expansion into 52 subkeys via 25-bit circular left shifts.
   - Internal round structure: 14 steps of one round, odd/even rounds, Output Transformation (half-round).
   - Decryption inverse keys derivation (additive inverse mod $2^{16}$, multiplicative inverse mod $65537$).
   - Solved numerical examples and full KTU PYQ solutions.

2. [Advanced Encryption Standard (AES)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/advanced-encryption-standard-aes.md)
   - Substitution-Permutation Network (SPN) architecture vs. Feistel ciphers.
   - 128-bit block, State Matrix, 10/12/14 rounds for 128/192/256-bit keys.
   - Four primitive transformations: `SubBytes` (multiplicative inverse in $GF(2^8)$ + affine mapping), `ShiftRows`, `MixColumns` (MDS matrix multiplication in $GF(2^8)$ mod $x^4+1$), `AddRoundKey`.
   - Key Expansion algorithm: `RotWord`, `SubWord`, Round Constant $Rcon$, 44 subkey words.
   - Inverse Cipher transformations and Inverse S-Box creation.
   - Solved numerical examples and full KTU PYQ solutions.

3. [Stream Ciphers and RC4](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/stream-ciphers-and-rc4.md)
   - Stream cipher architecture vs. block ciphers, pseudorandom keystream generator requirements.
   - RC4 internal state: 256-byte permutation array $S$, pointers $i$ and $j$.
   - Key-Scheduling Algorithm (KSA) and Pseudo-Random Generation Algorithm (PRGA).
   - Primitive operations: byte swaps, 8-bit modular addition, indirection lookup.
   - Security evaluation: Invariance bias, WEP 802.11 key reuse catastrophe, FMS attack.
   - Solved numerical examples and full KTU PYQ solutions.

---

## Module Revision Guide
- For quick exam revision, formulas, and key summaries, refer to [Module 2 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/revision-notes.md).
