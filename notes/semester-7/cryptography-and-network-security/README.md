# CS409 Cryptography and Network Security — Complete Course Guide & Study Notes

## Course Overview
- **Course Code**: CS409
- **Course Title**: Cryptography and Network Security
- **Semester**: Semester 7 (Derivation: `CS409` $\rightarrow 2 \times 4 - 1 = 7$, odd digit $\rightarrow$ S7)
- **Credits & L-T-P**: 3-0-0-3 (3 Credits)
- **Examination Scheme**: End Semester Examination (100 Marks, 3 Hours) — at least 60% analytical/numerical questions.

---

## Course Navigation & Modules Map

### [Module 1: Symmetric Cipher Models, Classical Encryption, and DES](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/detailed-notes.md)
- [Symmetric Cipher Models and Classical Encryption Techniques](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/symmetric-cipher-models-and-classical-encryption-techniques.md)
  - 5-part symmetric model, Caesar, Monoalphabetic, Playfair, Hill cipher ($2 \times 2$ matrix inversion), Vigenère, One-Time Pad, Rail Fence, Columnar transposition, Rotor machines, Steganography.
- [Data Encryption Standard (DES) and Simplified DES (S-DES)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/data-encryption-standard-and-simplified-des.md)
  - Feistel network principles, Shannon's confusion & diffusion, 16-round DES, non-linear S-boxes, S-DES subkey generation ($P_{10}, P_8$), Differential & Linear cryptanalysis.
- [Block Cipher Design Principles and Modes of Operation](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/block-cipher-design-principles-and-modes-of-operation.md)
  - SAC & BIC criteria, ECB, CBC, CFB, OFB, CTR modes, error propagation, and hardware parallelism.
- [Module 1 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-1/revision-notes.md)

---

### [Module 2: Modern Symmetric Ciphers: IDEA, AES, and Stream Ciphers](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/detailed-notes.md)
- [IDEA Cipher Principles and Operations](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/idea-cipher-principles-and-operations.md)
  - Mixing of 3 incompatible algebraic groups ($\oplus, \boxplus, \odot$ modulo $65537$), 52 subkeys via 25-bit circular shifts, 14-step round logic, inverse decryption keys.
- [Advanced Encryption Standard (AES)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/advanced-encryption-standard-aes.md)
  - SPN architecture, 128-bit state matrix, `SubBytes` (Galois field $GF(2^8)$ inverse + affine mapping), `ShiftRows`, `MixColumns` (MDS matrix), `AddRoundKey`, key expansion schedule.
- [Stream Ciphers and RC4](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/stream-ciphers-and-rc4.md)
  - Stream cipher principles, RC4 Key-Scheduling Algorithm (KSA), Pseudo-Random Generation Algorithm (PRGA), WEP key reuse vulnerability and FMS bias.
- [Module 2 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-2/revision-notes.md)

---

### [Module 3: Number Theory & Asymmetric / Public Key Cryptography](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/detailed-notes.md)
- [Mathematical Foundations and Number Theory](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/mathematical-foundations-and-number-theory.md)
  - Fundamental theorem of arithmetic, Extended Euclidean algorithm, Euler's totient function $\phi(n)$, Fermat's Little Theorem (full rigorous proof), Euler's theorem, primitive roots.
- [RSA Algorithm and Public Key Cryptography Principles](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/rsa-algorithm-and-public-key-principles.md)
  - Principles of public key cryptography, trapdoor one-way functions, RSA key generation, encryption, decryption, proof of correctness, and factorization attacks.
- [Diffie-Hellman Key Exchange and Elliptic Curve Cryptography](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/diffie-hellman-key-exchange-and-elliptic-curve-cryptography.md)
  - Diffie-Hellman protocol, discrete logarithm problem, Man-in-the-Middle attack, Elliptic curves over $\mathbb{F}_p$, point addition/doubling, ECDH.
- [Module 3 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-3/revision-notes.md)

---

### [Module 4: Authentication, Hash Functions, and Digital Signatures](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/detailed-notes.md)
- [Authentication Requirements and Message Authentication Codes (MAC)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/authentication-requirements-and-message-authentication-codes.md)
  - Communication threats, authentication functions, MAC vs. encryption brute-force work factors, Encrypt-then-MAC, HMAC structure.
- [Cryptographic Hash Functions: MD5 and SHA-1](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/cryptographic-hash-functions-md5-and-sha1.md)
  - Hash properties, Birthday attack derivation ($2^{m/2}$), MD5 128-bit 4-round architecture, SHA-1 160-bit 80-step word expansion architecture.
- [Authentication Protocols and Digital Signatures](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/authentication-protocols-and-digital-signatures.md)
  - Properties of digital signatures, Digital Signature Algorithm (DSA) signing & verification with proof, hazards of $k$ reuse, Kerberos mutual authentication.
- [Module 4 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-4/revision-notes.md)

---

### [Module 5: Network Security & Electronic Mail Security](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/detailed-notes.md)
- [Electronic Mail Security: Pretty Good Privacy (PGP) and S/MIME](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/electronic-mail-security-pgp-and-smime.md)
  - PGP five core services, why compression precedes encryption, key rings, MIME header fields, S/MIME four functions (Enveloped, Signed, Clear-Signed Data).
- [IP Security: Architecture, Protocols, and Operating Modes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/ip-security-architecture-and-protocols.md)
  - Benefits of IPsec, SA, SAD, SPD, SA selectors, AH format and mutable ICV calculation, ESP packet format, Transport Mode vs. Tunnel Mode.
- [IPsec Key Management, Oakley, and Internet Key Exchange (IKE)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/ipsec-key-management-and-ike.md)
  - Oakley key determination, anti-clogging cookies, 3 authentication methods, ISAKMP framework, IKE Phase 1 (Main/Aggressive Mode) and Phase 2 (Quick Mode).
- [Module 5 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/revision-notes.md)

---

### [Module 6: Web Security, E-Commerce, and Perimeter Defense](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/detailed-notes.md)
- [Web Security Considerations and SSL / TLS](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/web-security-considerations-and-ssl-tls.md)
  - Web security threat taxonomy, placement in protocol stack, SSL/TLS architecture, SSL Record Protocol 5-step operation, Handshake Protocol, SSL vs. TLS.
- [Secure Electronic Transaction (SET)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/secure-electronic-transaction-set.md)
  - E-commerce privacy dilemma, Dual Signature mathematical construction $DS = E_{PR_C}(H(H(PI) \parallel H(OI)))$, independent verification by merchant and gateway, 6-phase SET transaction sequence.
- [Firewalls and Encrypted Tunnels](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/firewalls-and-encrypted-tunnels.md)
  - Design goals, 4 firewall classes (Packet filters, Stateful inspection, Application proxy, Circuit-level gateway), 3 architectures (Screened Host, Screened Subnet DMZ), Encrypted Tunnels, firewall limitations.
- [Module 6 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/revision-notes.md)

---

## Repository Reference Resources
- **Syllabus Study Guide**: [`notes/semester-7/cryptography-and-network-security/syllabus.md`](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/syllabus.md)
- **Textbooks**: [`textbooks/semester-7/cryptography-and-network-security/README.md`](file:///home/sravan/ktu/textbooks/semester-7/cryptography-and-network-security/README.md)
  - *William Stallings: Cryptography and Network Security 6th Ed (2014)*
  - *MRCET Notes / Forouzan Synthesis*
- **Textbook Knowledge Bases**: [`notes/semester-7/cryptography-and-network-security/knowledge/README.md`](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/knowledge/README.md)
- **Previous Question Papers**:
  - [`May 2019`](file:///home/sravan/ktu/previous-question-papers/semester-7/cryptography-and-network-security/May_2019.txt)
  - [`June 2022`](file:///home/sravan/ktu/previous-question-papers/semester-7/cryptography-and-network-security/June_2022.txt)
  - [`January 2023`](file:///home/sravan/ktu/previous-question-papers/semester-7/cryptography-and-network-security/January_2023.txt)
- **Sample Question Papers**:
  - [Sample Question Paper 1](file:///home/sravan/ktu/sample-question-papers/semester-7/cryptography-and-network-security/Sample_Question_Paper_1.md)
  - [Sample Question Paper 2](file:///home/sravan/ktu/sample-question-papers/semester-7/cryptography-and-network-security/Sample_Question_Paper_2.md)
  - [Sample Question Paper 3](file:///home/sravan/ktu/sample-question-papers/semester-7/cryptography-and-network-security/Sample_Question_Paper_3.md)
