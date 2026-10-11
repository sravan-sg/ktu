# Module 6: Web Security, E-Commerce, and Perimeter Defense — Detailed Notes Index

This directory contains in-depth study notes, architectural models, comparative analyses, and complete previous year university question solutions for **Module 6: Web Security Considerations, SSL/TLS, Secure Electronic Transaction (SET), Firewalls, and Encrypted Tunnels** of CS409 Cryptography and Network Security.

---

## Topic Detailed Notes Directory

1. [Web Security Considerations and SSL / TLS](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/web-security-considerations-and-ssl-tls.md)
   - Web traffic security threats: Integrity, confidentiality, authentication, and availability (DoS) threats.
   - Placement of security in the network stack (Layer 3 IPsec, Layer 4 TLS, Layer 7 Application).
   - SSL/TLS Architecture: Session state vs. Connection state.
   - The four SSL/TLS sub-protocols: SSL Record Protocol (5 steps: fragmentation, compression, MAC calculation, encryption, header prepend), Handshake Protocol (4 phases, Master Secret derivation), ChangeCipherSpec Protocol, Alert Protocol.
   - Detailed comparison of SSL vs. TLS and TLS 1.3 latency optimizations.
   - Solved numerical examples and full KTU PYQ solutions.

2. [Secure Electronic Transaction (SET)](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/secure-electronic-transaction-set.md)
   - SET business environment & participants: Cardholder, Merchant, Issuer, Acquirer, Payment Gateway, Certificate Authority.
   - The fundamental privacy dilemma in e-commerce: Merchant order fulfillment vs. Bank payment authorization.
   - Dual Signature ($DS$) mechanism: Mathematical construction, SHA-1 digest concatenation, and signing with cardholder private key.
   - Independent verification of the Dual Signature by the Merchant and the Payment Gateway.
   - Complete 6-phase sequence of operations in a SET transaction.
   - Comparison of SET vs. SSL/TLS.
   - Solved numerical examples and full KTU PYQ solutions.

3. [Firewalls and Encrypted Tunnels](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/firewalls-and-encrypted-tunnels.md)
   - Firewall design principles: Single choke point, policy enforcement, bastion hardening. Default Deny vs. Default Permit.
   - Four classes of firewalls: Packet filtering (stateless), Stateful Packet Inspection (SPI), Application-Level Gateways (Proxy), Circuit-Level Gateways.
   - Three standard firewall configurations: Screened Host (Single-homed), Screened Host (Dual-homed), Screened Subnet (DMZ architecture).
   - Encrypted Tunnels and Virtual Private Networks (VPNs): Technical requirements and IPsec Tunnel Mode operation.
   - Fundamental operational limitations of firewalls.
   - Solved numerical examples and full KTU PYQ solutions.

---

## Module Revision Guide
- For quick exam revision, formulas, and key summaries, refer to [Module 6 Revision Notes](file:///home/sravan/ktu/notes/semester-7/cryptography-and-network-security/module-6/revision-notes.md).
