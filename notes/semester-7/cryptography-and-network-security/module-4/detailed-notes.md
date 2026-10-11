# Module 4: Authentication, Hash Functions, and Digital Signatures — Detailed Notes Index

This directory contains in-depth study notes, architectural diagrams, mathematical proofs, and complete previous year university question solutions for **Module 4: Authentication Requirements, MACs, Cryptographic Hash Functions, SHA-1, MD5, Authentication Protocols, and Digital Signatures** of CS409 Cryptography and Network Security.

---

## Topic Detailed Notes Directory

1. [Authentication Requirements and Message Authentication Codes (MAC)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/authentication-requirements-and-message-authentication-codes.md)
   - Security threats in communication: Disclosure, masquerade, content/sequence modification, replay, repudiation.
   - Authentication functions: Message encryption, Message Authentication Codes (MAC), Hash functions.
   - Brute-force work factor comparison: MAC vs. Encryption.
   - Authentication only vs. Authentication with confidentiality (Encrypt-then-MAC, MAC-then-Encrypt).
   - HMAC architecture, mathematical formulation, ipad/opad constants, and length extension defense.
   - Solved numerical examples and full KTU PYQ solutions.

2. [Cryptographic Hash Functions: MD5 and SHA-1](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/cryptographic-hash-functions-md5-and-sha1.md)
   - Core requirements of cryptographic hash functions (one-way, weak collision resistance, strong collision resistance).
   - The Birthday Attack: mathematical derivation ($2^{m/2}$ complexity).
   - MD5 algorithm: Padding, 64-bit length append, 4 buffer registers, 4 rounds (64 steps), non-linear functions ($F, G, H, I$), and output digest.
   - SHA-1 algorithm: Padding, 5 buffer registers, 80-word expansion schedule, 80 steps, round constants, and output digest.
   - Comparative evaluation of MD5 vs. SHA-1.
   - Solved numerical examples and full KTU PYQ solutions.

3. [Authentication Protocols and Digital Signatures](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/authentication-protocols-and-digital-signatures.md)
   - Digital signatures: Authenticity, integrity, non-repudiation, unforgeability.
   - Direct vs. Arbitrated digital signatures.
   - Digital Signature Standard (DSS) & Digital Signature Algorithm (DSA): Public parameters ($p, q, g$), keys ($x, y$).
   - DSA Signing ($r, s$) and Verification ($w, u_1, u_2, v$) with complete mathematical proof.
   - Security hazards of per-message secret $k$ reuse in DSA.
   - Mutual authentication protocols, Kerberos, and replay attack defenses.
   - Solved numerical examples and full KTU PYQ solutions.

---

## Module Revision Guide
- For quick exam revision, formulas, and key summaries, refer to [Module 4 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/revision-notes.md).
