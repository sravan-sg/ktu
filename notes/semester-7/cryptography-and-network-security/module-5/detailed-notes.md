# Module 5: Network Security & Electronic Mail Security — Detailed Notes Index

This directory contains in-depth study notes, architectural models, operational packet layouts, and complete previous year university question solutions for **Module 5: Electronic Mail Security (PGP, S/MIME) and IP Security (IPsec Architecture, AH, ESP, and IKE)** of CS409 Cryptography and Network Security.

---

## Topic Detailed Notes Directory

1. [Electronic Mail Security: Pretty Good Privacy (PGP) and S/MIME](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/electronic-mail-security-pgp-and-smime.md)
   - Email vulnerabilities and traditional SMTP limitations.
   - PGP's five core services: Digital signatures, confidentiality, compression, Radix-64 conversion, segmentation.
   - Comprehensive analysis of why compression is performed *before* encryption.
   - PGP Private Key Ring and Public Key Ring data structures.
   - S/MIME specification, 5 MIME header fields (`MIME-Version`, `Content-Type`, `Content-Transfer-Encoding`, `Content-ID`, `Content-Description`).
   - S/MIME four core functions: Enveloped Data, Signed Data, Clear-Signed Data, Signed & Enveloped Data.
   - Solved numerical examples and full KTU PYQ solutions.

2. [IP Security: Architecture, Protocols, and Operating Modes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/ip-security-architecture-and-protocols.md)
   - Benefits of Layer 3 IPsec protection.
   - IPsec architectural components: Security Associations (SA), Security Association Database (SAD), Security Policy Database (SPD), SA Selectors.
   - Authentication Header (AH): Packet layout, mutable vs immutable fields, Integrity Check Value (ICV) calculation.
   - Encapsulating Security Payload (ESP): Header format (SPI, Seq No, Payload, Padding, Pad Length, Next Header, ICV).
   - Operating Modes: Transport Mode vs. Tunnel Mode (complete packet wrapping diagrams).
   - Combining Security Associations (SA Bundles).
   - Solved numerical examples and full KTU PYQ solutions.

3. [IPsec Key Management, Oakley, and Internet Key Exchange (IKE)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/ipsec-key-management-and-ike.md)
   - Limitations of manual keying and necessity of automated key management.
   - Oakley Key Determination Protocol: Cookie anti-clogging defense, mathematical groups, Perfect Forward Secrecy.
   - Three authentication methods in Oakley: Digital signatures, public-key encryption, pre-shared symmetric keys.
   - ISAKMP architectural framework and payload types.
   - Internet Key Exchange (IKE): Two-phase operation, Phase 1 (Main Mode vs Aggressive Mode), Phase 2 (Quick Mode).
   - Anti-replay sliding window mechanics.
   - Solved numerical examples and full KTU PYQ solutions.

---

## Module Revision Guide
- For quick exam revision, formulas, and key summaries, refer to [Module 5 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-5/revision-notes.md).
