# Module 5: Revision Notes — Quick Review & High-Yield Summary

## Submodule 1: Email Security (PGP & S/MIME)
- **PGP Core Services**:
  1. Digital Signature: $E_{PR_A}(H(M))$.
  2. Confidentiality: $E_{K_s}(M) \parallel E_{PU_B}(K_s)$.
  3. Compression: ZIP applied *before* encryption (flattens statistical redundancy; ciphertext is high-entropy and cannot be compressed).
  4. Radix-64: Converts 3 binary bytes to 4 ASCII characters (33% size expansion).
  5. Segmentation & Reassembly.
- **Key Rings**: Private Key Ring (passphrase encrypted) and Public Key Ring (Web of Trust).
- **MIME Headers**: `MIME-Version`, `Content-Type`, `Content-Transfer-Encoding`, `Content-ID`, `Content-Description`.
- **S/MIME Functions**: Enveloped Data (privacy), Signed Data (integrity), Clear-Signed Data (readable body + signature), Signed & Enveloped Data.

---

## Submodule 2: IPsec Architecture & Protocols
- **Benefits**: Transparency to applications, perimeter defense, eliminates address spoofing, transparent VPNs.
- **Key Structures**:
  - **SA (Security Association)**: One-way connection identified by $(\text{SPI}, \text{Dest IP}, \text{Protocol})$.
  - **SAD**: Stores active SA parameters and keys.
  - **SPD**: Policy database linking packet selectors (IPs, Ports, Protocol) to actions (Discard, Bypass, Protect).
- **AH (Protocol 51)**: Integrity and authentication; zero confidentiality. ICV calculated over immutable fields (zeros mutable fields like TTL, TOS, Checksum).
- **ESP (Protocol 50)**: Confidentiality, integrity, anti-replay. Format: SPI (32), Seq No (32), Payload, Padding, Pad Length (8), Next Header (8), ICV.
- **Modes**:
  - **Transport Mode**: Host-to-Host. Protects transport payload. Uses original IP header.
  - **Tunnel Mode**: Gateway-to-Gateway. Protects entire IP packet. Adds new outer IP header.

---

## Submodule 3: Key Management & IKE
- **Oakley Protocol**: Authenticated Diffie-Hellman. Anti-clogging cookies, supports multiple groups, Perfect Forward Secrecy.
  - **Three Authentication Methods**: Digital Signatures, Public-Key Encryption, Pre-Shared Keys (PSK).
- **ISAKMP**: Framework defining message payloads and state machines.
- **IKE Operation**:
  - **Phase 1 (IKE SA)**: Main Mode (6 messages, protects identities) or Aggressive Mode (3 messages, faster).
  - **Phase 2 (IPsec SA)**: Quick Mode (3 messages, encrypted under IKE SA).
- **Anti-Replay**: 32-bit sequence number with 64-packet sliding window.

---

## Submodule 4: High-Yield Formulas & Exam Cheatsheet
- PGP Transmission: $\text{Packet} = \text{Radix64}\Big(E_{PU_B}(K_s) \parallel E_{K_s}(\text{ZIP}(M \parallel E_{PR_A}(H(M))))\Big)$.
- ESP Padding Rule: $(\text{Payload} + 2 + \text{Pad}) \equiv 0 \pmod{\text{BlockSize}}$.
- AH ICV Coverage: Entire packet with mutable fields zeroed.
- Oakley Cookie: $\text{Cookie} = \text{HMAC}(K_{\text{secret}}, \text{SrcIP} \parallel \text{DstIP} \parallel \text{SrcPort} \parallel \text{DstPort} \parallel \text{Time})$.
