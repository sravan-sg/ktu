# Module 1: Symmetric Ciphers, Classical Encryption, and DES — Detailed Notes Index

This directory contains in-depth study notes, algorithmic traces, and complete previous year university question solutions for **Module 1: Symmetric Cipher Models, Classical Encryption Techniques, DES, and Block Cipher Operation** of CS409 Cryptography and Network Security.

---

## Topic Detailed Notes Directory

1. [Symmetric Cipher Models and Classical Encryption Techniques](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/symmetric-cipher-models-and-classical-encryption-techniques.md)
   - Symmetric cipher model, 5 core components.
   - Substitution techniques: Caesar cipher, Monoalphabetic cipher, Playfair cipher ($5 \times 5$ matrix rules), Hill cipher ($2 \times 2$ matrix algebra modulo 26), Polyalphabetic / Vigenère cipher, One-Time Pad.
   - Transposition techniques: Rail Fence cipher, Row Columnar transposition.
   - Rotor machines (Enigma principles) & Steganography (LSB insertion).
   - Solved numerical examples and full KTU PYQ solutions.

2. [Data Encryption Standard (DES) and Simplified DES (S-DES)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/data-encryption-standard-and-simplified-des.md)
   - Feistel cipher network architecture, Claude Shannon's Confusion and Diffusion.
   - 16-round Data Encryption Standard (DES), Initial Permutation, Round Function $F$, Expansion permutation $E$, Non-linear S-boxes ($S_1 \dots S_8$), Permutation $P$, Key schedule ($PC-1$, shifts, $PC-2$).
   - Simplified DES (S-DES): 10-bit key generation, $P_{10}$, $P_8$, 2 Feistel rounds, S-box lookups ($S_0, S_1$), switch function.
   - Strength of DES, 56-bit key exhaustibility, Differential and Linear Cryptanalysis.
   - Solved numerical examples and full KTU PYQ solutions.

3. [Block Cipher Design Principles and Modes of Operation](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/block-cipher-design-principles-and-modes-of-operation.md)
   - Design criteria: Number of rounds, S-box non-linearity (Strict Avalanche Criterion, Bit Independence Criterion), diffusion layers.
   - Five standard modes of operation: Electronic Codebook (ECB), Cipher Block Chaining (CBC), Cipher Feedback (CFB), Output Feedback (OFB), Counter (CTR).
   - Error propagation analysis and hardware/software parallelism comparison.
   - Solved numerical examples and full KTU PYQ solutions.

---

## Module Revision Guide
- For quick exam revision, formulas, and key summaries, refer to [Module 1 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/revision-notes.md).
