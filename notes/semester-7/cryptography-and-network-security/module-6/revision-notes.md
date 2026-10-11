# Module 6: Revision Notes — Quick Review & High-Yield Summary

## Submodule 1: Web Security & SSL/TLS
- **Web Threats**: Integrity (tampering), Confidentiality (eavesdropping), Authentication (impersonation), Availability (DoS).
- **Security Placement**: Layer 3 (IPsec), Layer 4 (SSL/TLS - HTTPS port 443), Layer 7 (Application - SET/PGP).
- **SSL/TLS Structure**:
  - **SSL Record Protocol**: Fragmentation ($\le 16$ KB), optional compression, MAC generation, symmetric encryption, 5-byte header prepend (`Content-Type`, `Version`, `Length`).
  - **SSL Handshake Protocol**: 4 phases. Client/Server Hello $\rightarrow$ Server Certificate & Key Exchange $\rightarrow$ Client Key Exchange (Pre-Master Secret) $\rightarrow$ Finished. Derives 48-byte Master Secret.
  - **ChangeCipherSpec**: Single byte `1` signaling transition to newly negotiated cipher parameters.
  - **Alert**: 2 bytes (Level: Warning/Fatal; Description code).
- **SSL vs. TLS**: TLS uses standard HMAC, formal PRF/HKDF, granular alerts, and removes broken ciphers.

---

## Submodule 2: Secure Electronic Transaction (SET)
- **Participants**: Cardholder (wallet), Merchant, Payment Gateway, Acquirer (merchant bank), Issuer (cardholder bank).
- **The E-Commerce Problem**: Merchant must see Order Info ($OI$) but not credit card details ($PI$). Bank must see $PI$ but not $OI$. Both must be linked to prevent fraud.
- **Dual Signature ($DS$) Formula**:
  $$DS = E_{PR_C}\Big(H\big(H(PI) \parallel H(OI)\big)\Big)$$
- **Dual Verification**:
  - Merchant verifies: $H(H(PI) \parallel H(OI)) \stackrel{?}{=} D(PU_C, DS)$ using received $OI$ and hash $H(PI)$.
  - Gateway verifies: $H(H(PI) \parallel H(OI)) \stackrel{?}{=} D(PU_C, DS)$ using decrypted $PI$ and hash $H(OI)$.
- **SET Flow**: Cardholder order request $\rightarrow$ Merchant authorization request to Payment Gateway $\rightarrow$ Gateway clears with issuing bank $\rightarrow$ Merchant ships goods $\rightarrow$ Payment captured.

---

## Submodule 3: Firewalls & Encrypted Tunnels
- **Design Goals**: Single choke point, enforce local security policy, bastion host immunity. Default Deny vs. Default Permit.
- **Four Firewall Types**:
  1. **Packet Filtering**: Stateless, L3/L4 headers. Vulnerable to IP spoofing.
  2. **Stateful Inspection (SPI)**: Maintains in-memory connection state table. Inbound allowed only if matching active outbound connection.
  3. **Application Gateway (Proxy)**: Reassembles L7 application protocols (HTTP, SMTP). High security, slower.
  4. **Circuit-Level Gateway**: Relays TCP connections at L4 without parsing application payload (SOCKS).
- **Three Firewall Architectures**:
  1. Screened Host (Single-homed bastion).
  2. Screened Host (Dual-homed bastion, IP forwarding disabled).
  3. Screened Subnet (DMZ): Two packet filters flanking public DMZ buffer network. Defense-in-depth.
- **Encrypted Tunnels (VPN)**: End-to-end IPsec Tunnel Mode encapsulation across untrusted backbones.
- **Firewall Limitations**: Cannot protect against insider attacks, rogue out-of-band links, social engineering/phishing, or encrypted malicious traffic.

---

## Submodule 4: High-Yield Formulas & Exam Cheatsheet
- Dual Signature: $DS = E_{PR_C}(H(H(PI) \parallel H(OI)))$.
- SSL Record Header: 5 bytes (`0x17` = Application Data, `0x0303` = TLS 1.2, 2 bytes length).
- TLS Master Secret: $\text{PRF}(\text{Pre-Master}, \text{"master secret"}, \text{ClientRandom} \parallel \text{ServerRandom})$.
- SPI State Table: Inbound packet matched to $(\text{SrcIP}, \text{DstIP}, \text{SrcPort}, \text{DstPort}, \text{State})$.
