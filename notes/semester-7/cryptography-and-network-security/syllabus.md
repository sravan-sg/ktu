# CS409 Cryptography and Network Security — Syllabus & Study Guide

## Course Overview
- **Course Code**: CS409
- **Course Name**: Cryptography and Network Security
- **Semester**: Semester 7 (Derivation: `CS409` → $2 \times 4 - 1 = 7$, odd digit $\rightarrow$ S7)
- **L-T-P-Credits**: 3-0-0-3
- **Year of Introduction**: 2016
- **Exam Pattern**: End Semester Exam (100 Marks, 3 Hours), at least 60% analytical/numerical questions.

---

## Course Objectives & Expected Outcomes
### Objectives
1. To introduce fundamental concepts of symmetric and asymmetric cipher models.
2. To introduce fundamental concepts of authentication and cryptographic primitives.
3. To introduce network security, web security protocols, and perimeter defense systems.

### Expected Outcomes
- Summarize classical encryption techniques and modern symmetric ciphers.
- Apply mathematical number theory concepts for cryptographic algorithms.
- Demonstrate cryptographic algorithms for encryption, integrity, and key exchange.
- Summarize authentication architectures, hash functions, and digital signature schemes.
- Identify security issues across network, transport, and application layers and evaluate countermeasure protocols.

---

## Prescribed Textbooks & References
### Textbooks
1. **Behrouz A. Forouzan**, *Cryptography and Network Security*, Tata McGraw-Hill, 2010.
2. **William Stallings**, *Cryptography and Network Security: Principles and Practice*, Pearson Education, 2014.

### Reference Books
1. **Bruce Schneier**, *Applied Cryptography: Protocols, Algorithms, and Source Code in C*, 2nd Edn, Wiley, 1995.
2. **Charlie Kaufman, Radia Perlman, Mike Speciner**, *Network Security: Private Communication in a Public World*, PHI, 2002.

---

## Detailed Module Breakdown

### Module I: Symmetric Ciphers, Classical Encryption, and DES (7 Hours | 15% Marks)
- [Symmetric Cipher Models and Classical Encryption Techniques](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/symmetric-cipher-models-and-classical-encryption-techniques.md): Symmetric cipher models, Substitution techniques (Caesar, Monoalphabetic, Playfair, Hill, Polyalphabetic, One-Time Pad), Transposition techniques (Rail fence, Row transposition), Rotor machines, Steganography.
- [Data Encryption Standard (DES) and Simplified DES (S-DES)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/data-encryption-standard-and-simplified-des.md): Simplified DES (S-DES key generation, round structure, S-boxes), Block cipher principles (Feistel architecture, diffusion and confusion), The Data Encryption Standard (DES), Strength of DES, Differential and Linear Cryptanalysis concepts.
- [Block Cipher Design Principles and Modes of Operation](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/block-cipher-design-principles-and-modes-of-operation.md): Block cipher design principles, Modes of operation (ECB, CBC, CFB, OFB, CTR).
- *Study Materials*: [Module 1 Detailed Notes Index](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/detailed-notes.md) | [Module 1 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/revision-notes.md)

### Module II: Modern Symmetric Ciphers: IDEA, AES, and Stream Ciphers (7 Hours | 15% Marks)
- [IDEA Cipher Principles and Operations](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/idea-cipher-principles-and-operations.md): Design philosophy, Primitive algebraic operations (XOR $\oplus$, Addition modulo $2^{16}$, Multiplication modulo $2^{16}+1$), 128-bit key expansion into 52 subkeys, Structure of one round, odd rounds, even rounds, Output transformation, Inverse subkeys derivation for decryption.
- [Advanced Encryption Standard (AES)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/advanced-encryption-standard-aes.md): Basic structure, Non-Feistel SPN (Substitution-Permutation Network), Primitive byte/word operations (`SubBytes`, `ShiftRows`, `MixColumns`, `AddRoundKey`), Inverse cipher transformations, Key expansion algorithm (RotWord, SubWord, Rcon), Standard round execution vs. Final round.
- [Stream Ciphers and RC4](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/stream-ciphers-and-rc4.md): Stream cipher architecture vs. block ciphers, RC4 algorithm (KSA - Key Scheduling Algorithm, PRGA - Pseudo-Random Generation Algorithm), strengths and known vulnerabilities.
- *Study Materials*: [Module 2 Detailed Notes Index](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/detailed-notes.md) | [Module 2 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/revision-notes.md)

### Module III: Number Theory & Asymmetric / Public Key Cryptography (7 Hours | 15% Marks)
- [Mathematical Foundations of Asymmetric Cryptography](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/mathematical-foundations-and-number-theory.md): Fundamental Theorem of Arithmetic, Divisibility and primes, Modular arithmetic properties, Extended Euclidean Algorithm (computing multiplicative modular inverses), Fermat's Little Theorem, Euler's Totient Function $\phi(n)$, Euler's Theorem.
- [Public Key Cryptosystems & RSA Algorithm](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/rsa-algorithm-and-public-key-principles.md): Principles of Public Key Cryptography, One-way trapdoor functions, RSA Key generation, Encryption, Decryption, Mathematical proof of correctness, Computational efficiency and attacks on RSA.
- [Diffie-Hellman Key Exchange & Elliptic Curve Cryptography](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/diffie-hellman-key-exchange-and-elliptic-curve-cryptography.md): Diffie-Hellman Key Exchange algorithm (discrete logarithm problem, Man-in-the-Middle attack), Elliptic Curve Cryptography (ECC) fundamentals, Weierstrass equation, Elliptic curve group laws, Point addition and doubling, ECDH.
- *Study Materials*: [Module 3 Detailed Notes Index](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/detailed-notes.md) | [Module 3 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/revision-notes.md)

### Module IV: Authentication, Hash Functions, and Digital Signatures (7 Hours | 15% Marks)
- [Message Integrity & Authentication Codes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/authentication-requirements-and-message-authentication-codes.md): Authentication requirements, Security threats, Authentication functions, Message Authentication Codes (MAC), HMAC architecture.
- [Cryptographic Hash Functions: MD5 & SHA-1](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/cryptographic-hash-functions-md5-and-sha1.md): Requirements for cryptographic hash functions (pre-image resistance, second pre-image resistance, collision resistance), Birthday attack, MD5 message digest architecture, SHA-1 message digest architecture (padding, compression function, logic operations), Security comparison of MD5 and SHA family.
- [Authentication Protocols & Digital Signatures](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/authentication-protocols-and-digital-signatures.md): Mutual authentication protocols, Kerberos, Digital Signatures (properties and requirements), Digital Signature Standard (DSS / DSA algorithm and signature verification).
- *Study Materials*: [Module 4 Detailed Notes Index](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/detailed-notes.md) | [Module 4 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/revision-notes.md)


### Module V: Network Security & Email Security (7 Hours | 20% Marks)
- [Electronic Mail Security: PGP & S/MIME](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/electronic-mail-security-pgp-and-smime.md): Security vulnerabilities in traditional email (SMTP), Pretty Good Privacy (PGP) operational flow (confidentiality, digital signatures, compression, radix-64 conversion, key rings), S/MIME functionality and certificates.
- [IP Security (IPsec) Architecture & Protocols](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/ip-security-architecture-and-protocols.md): IPsec architecture and benefits, Security Associations (SA), Security Association Database (SAD) and Security Policy Database (SPD), Authentication Header (AH) in Transport and Tunnel modes, Encapsulating Security Payload (ESP) in Transport and Tunnel modes, Combining Security Associations.
- [IPsec Key Management & IKE](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/ipsec-key-management-and-ike.md): Key management (Oakley algorithm, ISAKMP, Internet Key Exchange - IKE).
- *Study Materials*: [Module 5 Detailed Notes Index](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/detailed-notes.md) | [Module 5 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/revision-notes.md)

### Module VI: Web Security, E-Commerce, and Perimeter Defense (7 Hours | 20% Marks)
- [Web Security Considerations & SSL / TLS](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/web-security-considerations-and-ssl-tls.md): Web Security considerations, Web traffic security threats and countermeasure placement, Secure Socket Layer (SSL) and Transport Layer Security (TLS), SSL Record Protocol, Handshake Protocol, Change Cipher Spec Protocol, Alert Protocol, Session state vs. Connection state.
- [Secure Electronic Transaction (SET)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/secure-electronic-transaction-set.md): Business participants, Dual Signature concept, transaction verification process.
- [Perimeter Defense, Firewalls & Encrypted Tunnels](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/firewalls-and-encrypted-tunnels.md): Firewalls, Packet filters, Stateful inspection, Application Level Gateway, Circuit Level Gateway, Bastion hosts, Encrypted tunnels.
- *Study Materials*: [Module 6 Detailed Notes Index](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/detailed-notes.md) | [Module 6 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/revision-notes.md)

---

## Exam Pattern & Scoring Strategy
- **Total Marks**: 100 Marks | **Duration**: 3 Hours
- **Part A (40 Marks)**: 10 compulsory questions of 4 marks each.
  - Module I & II: 3 questions (12 marks)
  - Module III & IV: 3 questions (12 marks)
  - Module V & VI: 4 questions (16 marks)
- **Part B (18 Marks - Answer any 2 out of 3, 9 marks each)**:
  - Q1: Module I | Q2: Module II | Q3: Module I & II uniform coverage.
- **Part C (18 Marks - Answer any 2 out of 3, 9 marks each)**:
  - Q1: Module III | Q2: Module IV | Q3: Module III & IV uniform coverage.
- **Part D (24 Marks - Answer any 2 out of 3, 12 marks each)**:
  - Q1: Module V | Q2: Module VI | Q3: Module V & VI uniform coverage.
- **Analytical / Numerical Quota**: At least 60% of question choices require rigorous step-by-step calculations (Modular arithmetic, Hill cipher matrix inversions, RSA computations, Diffie-Hellman key exchanges, IDEA algebraic operations, S-DES / AES round calculations).

---

## Exam Focus — What to Prioritize
1. **Module I & II High Yield**:
   - S-DES complete round tracing and subkey generation.
   - Hill Cipher encryption and decryption using $2 \times 2$ matrix inversion modulo 26.
   - Block cipher modes of operations (CBC vs. CTR diagrams, error propagation).
   - AES transformations (`SubBytes`, `ShiftRows`, `MixColumns`, `AddRoundKey`) and key schedule logic.
   - IDEA algebraic primitives and subkey assignment across rounds.
   - RC4 Key Scheduling Algorithm (KSA) and PRGA trace.
2. **Module III & IV High Yield**:
   - Extended Euclidean algorithm for multiplicative inverses: $ax \equiv 1 \pmod m$.
   - RSA end-to-end numerical computation ($p, q, n, \phi(n), e, d, C = M^e \bmod n, M = C^d \bmod n$).
   - Diffie-Hellman numerical exchange and Man-in-the-Middle attack scenario.
   - Elliptic Curve point addition and doubling formulas.
   - HMAC structure and inner/outer hashing equations.
   - SHA-1 vs. MD5 round structure, padding rules, and security vulnerabilities.
   - DSA key generation, signing, and verification mathematics.
3. **Module V & VI High Yield**:
   - PGP cryptographic services: why compress before encrypting, key ring structures.
   - IPsec AH vs. ESP in Transport Mode vs. Tunnel Mode (complete packet diagrams).
   - SSL/TLS Handshake Protocol step-by-step message exchange with Master Secret derivation.
   - Dual Signature in SET: why it is needed and mathematical verification.
   - Packet filter firewall rule tables (default permit vs. default deny) and Application Gateway proxying.
