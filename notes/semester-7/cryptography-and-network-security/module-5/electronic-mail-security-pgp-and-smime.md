# Electronic Mail Security: Pretty Good Privacy (PGP) and S/MIME

## 1. Explanation

### 1.1 The Email Security Problem — Why Plain SMTP Is Insecure

Email was designed in the early ARPANET era (1970s) with **zero security assumptions**. The Simple Mail Transfer Protocol (SMTP, RFC 821, 1982) was built for a trusted academic network where everyone knew each other. The underlying design decisions that make SMTP fundamentally insecure:

1. **Cleartext transmission**: Every SMTP connection sends message headers and bodies as plaintext ASCII. Any router, ISP, or network monitor between sender and recipient can read every word.

2. **No sender authentication**: SMTP allows any server to claim any `From:` address. Spoofing `From: president@whitehouse.gov` requires no special access — just an SMTP server.

3. **Store-and-forward relaying**: Email transits through multiple intermediate **Mail Transfer Agents (MTAs)**, each of which receives, queues, and forwards the message. Any MTA in the chain can read, modify, or silently drop messages.

4. **No message integrity**: There is no mechanism in base SMTP to detect whether a message was altered in transit by an MTA or a network adversary.

5. **No non-repudiation**: The sender can later deny having sent a message — SMTP has no cryptographic proof of origin.

**The consequence**: Without additional security layers, email is equivalent to sending postcards through the mail — the postal carrier (and every handler) can read it.

**What attackers can do against unprotected email**:

| Attack | Mechanism | Impact |
|---|---|---|
| **Eavesdropping** | Capture SMTP packets on any network segment | Read all email contents |
| **Sender spoofing** | Set arbitrary `From:` header | Phishing, business email compromise (BEC) |
| **Content modification** | MTA replaces message body in transit | Fraudulent wire transfer instructions |
| **Replay attack** | Re-deliver a captured email at a later time | Re-submit payment authorizations |
| **Repudiation** | Sender denies having sent the email | Contract and compliance disputes |

**Modern partial mitigations** (SMTP layer, incomplete):
- **STARTTLS**: Opportunistic TLS between MTAs. Only protects hop-by-hop; each MTA decrypts and re-encrypts. Does not provide end-to-end security.
- **SPF**: Validates sending server IP against DNS records. Prevents some domain spoofing.
- **DKIM**: Adds a server-level signature to headers. Proves the email left the signing domain intact but does not provide content encryption.
- **DMARC**: Policy layer over SPF and DKIM. Still no end-to-end encryption.

**What is needed**: **End-to-end security** where only the intended recipient can decrypt, and where the sender's identity is cryptographically proven. This is what PGP and S/MIME provide.

---

### 1.2 Pretty Good Privacy (PGP)

**Created by**: Philip Zimmermann, 1991.
**Motivation**: Zimmermann was concerned about surveillance of political activists and created PGP as "human rights software" — strong encryption freely available to individuals.
**Standardized as**: OpenPGP (RFC 4880, 2007), updated RFC 9580 (2024). GNU Privacy Guard (GPG/GnuPG) is the primary open-source implementation.
**Model**: **Decentralized Web of Trust** — no central certificate authority.

PGP provides **five core cryptographic services** that can be applied individually or combined:

#### Service 1: Digital Signature (Authentication + Non-Repudiation)

**Goal**: Prove the message came from the claimed sender and was not modified.

**Process**:

```
SENDER (Alice):
  1. Compute message digest:  h = SHA-1(M) or SHA-256(M)
  2. Sign the digest:         S = RSA_Encrypt(PR_Alice, h)
     OR DSS sign:             (r, s) = DSA_Sign(x_Alice, h, k)
  3. Prepend: Signature_Component = { Algorithm_ID ‖ Key_ID(PR_Alice) ‖ S ‖ Timestamp }
  4. Compress: ZIP(M ‖ Signature_Component)
  5. Radix-64 encode → send

RECEIVER (Bob):
  1. Radix-64 decode
  2. Decompress
  3. Separate M from Signature_Component
  4. Compute:  h' = SHA-1(M)
  5. Recover: h  = RSA_Decrypt(PU_Alice, S)  [from Alice's public key]
  6. Compare: h' == h? → Valid signature, authenticated and integrity confirmed
```

**Key ID inclusion**: The message includes the Key ID (lower 64 bits of Alice's public key fingerprint) so the receiver can look up the correct public key from their keyring without having to try all known keys.

**Timestamp**: Included in the signed data so recipients know when the signature was created, enabling replay detection.

**PGP Signing Algorithm Choices** (RFC 4880):
- RSA: Sign the hash with $d$, verify with $e$. Most widely supported.
- DSS/DSA: Produces $(r, s)$ pair based on discrete log. Signature-only.
- ECDSA: Elliptic-curve equivalent of DSA. Compact signatures (secp256k1, NIST P-256).
- EdDSA: Ed25519 — fastest modern signature algorithm. Default in newer GnuPG.

#### Service 2: Confidentiality (Message Encryption)

**Goal**: Only the intended recipient can read the message.

**Hybrid encryption design** (combines symmetric efficiency with asymmetric key distribution):

```
SENDER (Alice, encrypting for Bob):
  1. Generate random 128-bit session key Ks
  2. Encrypt message:      C_M = Symmetric_Encrypt(Ks, M)
                           Algorithms: CAST-128, IDEA, 3DES, AES-128/256
  3. Encrypt session key:  C_K = RSA_Encrypt(PU_Bob, Ks)
                           OR ElGamal_Encrypt(PU_Bob, Ks)
  4. Transmit: { C_K ‖ Key_ID(PU_Bob) ‖ C_M }

RECEIVER (Bob):
  1. Use Key_ID to locate PR_Bob on keyring
  2. Recover:   Ks = RSA_Decrypt(PR_Bob, C_K)
  3. Decrypt:   M  = Symmetric_Decrypt(Ks, C_M)
```

**Why hybrid encryption?**
- RSA/ElGamal: Computationally expensive, can only directly encrypt small data (shorter than key size).
- Symmetric (AES/CAST): Extremely fast, handles arbitrary-length data.
- The hybrid approach uses RSA only to encrypt a small 128-bit key, while AES encrypts the actual message. This gets the key distribution benefit of RSA at near-AES performance.

**Multi-recipient support**: For an email to $n$ recipients, PGP generates **one** $K_s$ and encrypts it $n$ times with each recipient's public key: $\{(C_{K_1}, \text{KeyID}_1), (C_{K_2}, \text{KeyID}_2), \dots, (C_{K_n}, \text{KeyID}_n)\} \| C_M$. Only the actual message ciphertext is stored once — not $n$ copies.

#### Service 3: Compression

**Goal**: Reduce message size and increase cryptographic strength.

**PGP applies ZIP compression BEFORE encryption** (not after). This is a critical design decision:

```
Correct PGP Order:
M (raw text) ──► ZIP(M) ──► Encrypt(Ks, ZIP(M)) ──► Transmit

WRONG order (would be useless):
M (raw text) ──► Encrypt(Ks, M) ──► ZIP(C) ──► Transmit (ZIP produces ~0% savings)
```

**Reasons why compression precedes encryption**:

1. **Compression effectiveness**: Natural language (English email) has ~2 bits/character of information entropy, despite occupying 8 bits. ZIP achieves 60–70% size reduction on typical text. After AES encryption, output is pseudo-random (maximum ~8 bits/byte entropy) — ZIP cannot compress it (0% savings).

2. **Cryptographic hardening**: Compression removes statistical redundancy from the plaintext. Natural language has known letter frequencies (English: 'E' is 12.7%, 'Z' is 0.07%). An uncompressed plaintext encrypted with a stream cipher leaks these patterns. Compressed plaintext has near-uniform byte distribution — known-plaintext and chosen-plaintext attacks become harder.

3. **Order relative to signing**: Compression happens AFTER signing and BEFORE encryption:
   - Sign first (with hash of uncompressed plaintext) — ensures the signature covers the actual content.
   - Compress second — reduces size before symmetric encryption.
   - Encrypt third — protects the compressed signed content.

**Limitation of compression in modern cryptography**: The CRIME and BREACH attacks (2012–2013) showed that combining TLS compression with chosen-plaintext injection (HTTPS POST requests) allows attackers to recover session cookies byte-by-byte by observing ciphertext length changes. PGP's one-shot email encryption avoids this attack model, but TLS-level compression was disabled in TLS 1.3 as a result.

#### Service 4: Email Compatibility (Radix-64 / Base64 Encoding)

**Goal**: Make binary cryptographic output transmittable over 7-bit ASCII email infrastructure.

**The problem**: PGP produces binary ciphertext (arbitrary byte values 0x00–0xFF). Legacy email servers (and some MIME implementations) only handle 7-bit ASCII (0x00–0x7F). Non-ASCII bytes are either:
- Stripped (the 8th bit is zeroed) — corrupts ciphertext.
- Rejected — message bounced.
- Modified (CR/LF handling) — corrupts byte sequences.

**Base64 / Radix-64 encoding**:

The encoding table maps 6-bit values (0–63) to ASCII characters:
```
Values 0–25:  'A'–'Z'
Values 26–51: 'a'–'z'
Values 52–61: '0'–'9'
Value 62:     '+'
Value 63:     '/'
Padding:      '='
```

**Encoding algorithm**:
1. Take 3 bytes (24 bits) of binary input at a time.
2. Split into four 6-bit groups.
3. Map each 6-bit group to its Base64 character.
4. If fewer than 3 bytes remain, pad with `=` characters.

**Size overhead**: 4 Base64 chars encode 3 binary bytes → **33.3% size increase**. For a 1000-byte ciphertext: becomes 1333 ASCII characters.

**PGP Radix-64 addition**: PGP's Radix-64 format adds a **24-bit CRC** (Cyclic Redundancy Check) at the end of the Base64 block to detect transmission errors (e.g., mail server mangling). This is beyond standard Base64 (RFC 4648) and specific to OpenPGP (RFC 4880 §6.1).

**The OpenPGP ASCII Armor format** (human-readable wrapper):
```
-----BEGIN PGP MESSAGE-----
Version: GnuPG v2

hQEMA...  (Base64-encoded ciphertext)
...
=XXXX    (24-bit CRC as 4 Base64 chars)
-----END PGP MESSAGE-----
```

The `-----BEGIN ... -----` and `-----END ... -----` delimiters ("armor headers") allow PGP data to be embedded in plain text emails, forum posts, or paste sites without confusion with surrounding text.

#### Service 5: Key Management — The Web of Trust

**Goal**: Distribute and authenticate public keys without a central Certificate Authority.

**The key authentication problem**: If Alice receives Bob's public key, how does she know it really belongs to Bob and not to an attacker (Eve) impersonating Bob? This is the same Man-in-the-Middle problem DH faces.

**PGP's Solution — Web of Trust**:

Instead of a central CA, PGP uses **mutual, chain-of-trust certification**:
- Users **sign each other's public keys** with their own private key.
- A key signed by a trusted person inherits some level of trust.
- Trust is **transitive** and **decentralized** — like social trust in the real world.

**PGP key certification levels**:
- **No trust**: Key received but not verified.
- **Marginal trust** (partial): Signed by one or more partially trusted signers.
- **Full trust**: Signed by a fully trusted party, or signed by multiple marginally trusted parties.
- **Ultimate trust**: The key is your own.

**Key validity rule** (GnuPG default):
$$\text{VALID} \iff \text{signed by 1 fully trusted key} \lor \text{signed by} \ge 3 \text{ marginally trusted keys}$$

**Example Web of Trust chain**:
```
Alice (ultimate) ──signs──► Bob (full trust) ──signs──► Carol (full trust)
                  ──signs──► Dave (full trust) ──signs──► Eve (marginal trust)
                                              Carol also signs Eve → Eve gets full trust
```

**PGP Key Rings** (internal data structures):
- **Public Key Ring** (`pubring.gpg`): Stores public keys of all known parties, each with associated trust levels and signatures.
- **Private Key Ring** (`secring.gpg`): Stores the user's own private key(s), encrypted with a symmetric passphrase-derived key for protection at rest.

**Key Server Infrastructure**: Rather than manually exchanging public keys, PGP users upload their public keys to **key servers** (e.g., `keys.openpgp.org`, `keyserver.ubuntu.com`). Receivers search by email address or Key ID. Key servers do NOT verify email ownership — this is PGP's trust model weakness vs. PKI.

---

### 1.3 PGP Cryptographic Message Processing Order

The **transmission** sequence combining all five services (authentication + confidentiality):

```
INPUT: Plaintext Message M, Alice's Private Key PR_A, Bob's Public Key PU_B

Step 1 — SIGN:
  h = H(M)                        [SHA-256 hash of plaintext]
  S = RSA(PR_A, h)                 [RSA signature on hash]
  M₁ = M ‖ S                       [signed message]

Step 2 — COMPRESS:
  M₂ = ZIP(M₁)                     [deflate compression]

Step 3 — SYMMETRIC ENCRYPT:
  Ks = random_128_bit()            [ephemeral session key]
  C_M = AES(Ks, M₂)               [encrypt signed+compressed message]
  C_K = RSA(PU_B, Ks)             [encrypt session key with Bob's public key]
  M₃ = C_K ‖ C_M                  [encrypted session key + encrypted message]

Step 4 — RADIX-64 ENCODE:
  Output = Base64(M₃) + CRC       [ASCII-safe encoding for SMTP]

OUTPUT: ASCII-armored PGP email ready for SMTP transmission
```

**Reception** (reverse, with reverse order):

```
Step 1 — RADIX-64 DECODE:
  M₃ = Base64_Decode(input)        [recover binary]

Step 2 — SYMMETRIC DECRYPT:
  Ks = RSA(PR_B, C_K)             [recover session key using Bob's private key]
  M₂ = AES_Decrypt(Ks, C_M)      [decrypt to signed+compressed content]

Step 3 — DECOMPRESS:
  M₁ = UNZIP(M₂)                  [restore signed message]

Step 4 — VERIFY SIGNATURE:
  Separate M and S from M₁
  h' = H(M)                        [recompute hash]
  h  = RSA_Decrypt(PU_A, S)       [recover signed hash using Alice's public key]
  h == h' ?                        [if yes: authentic and unmodified]
```

---

### 1.4 S/MIME (Secure/Multipurpose Internet Mail Extensions)

**S/MIME** (RFC 5751) is the PKI-based email security standard used in corporate email (Microsoft Outlook, Apple Mail, IBM Notes). Unlike PGP's decentralized Web of Trust, S/MIME uses **hierarchical X.509 certificates** issued by Certificate Authorities (CAs).

**Key differences from PGP**:

| Attribute | PGP / OpenPGP | S/MIME |
|---|---|---|
| **Key distribution** | Web of Trust (decentralized) | X.509 certificates from CAs (hierarchical PKI) |
| **Trust model** | User-to-user key signing | Third-party CA validates identities |
| **Certificate format** | OpenPGP key format (RFC 4880) | X.509 v3 (RFC 5280) |
| **Revocation** | Key server removal (manual) | CRL / OCSP (Online Certificate Status Protocol) |
| **Adoption** | Individual users, security researchers, activists | Enterprise email, governments, regulated industries |
| **Client support** | Requires PGP plugin (Thunderbird+Enigmail, CLI tools) | Native in Outlook, Apple Mail, most corporate clients |
| **Cost** | Free (public key infrastructure not needed) | CAs typically charge for S/MIME certificates |

#### S/MIME Cryptographic Services

**1. Enveloped Data** (Confidentiality — `EnvelopedData` CMS type):

```
Sender:
  1. Generate random session key Ks (AES-128, 3DES)
  2. Encrypt content:  C = Encrypt(Ks, M) in CBC mode
  3. For each recipient i:  C_Ki = RSA_Encrypt(PU_i, Ks)
  4. Build RecipientInfo for each recipient:
     { IssuerName, SerialNumber, KeyEncryptionAlgorithm, EncryptedKey }
  5. Package into PKCS#7 / CMS EnvelopedData structure:
     { RecipientInfos ‖ EncryptedContentInfo }
  6. Base64 encode + MIME-wrap:
     Content-Type: application/pkcs7-mime; smime-type=enveloped-data
```

**2. Signed Data** (Authentication + Integrity — `SignedData` CMS type):

```
Sender:
  1. Compute:  h = SHA-256(M)
  2. Sign:     S = RSA_Sign(PR_Sender, h)
  3. Build SignerInfo:
     { IssuerName, SerialNumber, DigestAlgorithm,
       AuthenticatedAttributes, SignatureAlgorithm, Signature }
  4. Package SignedData:
     { Certificates ‖ CRLs ‖ SignerInfos ‖ EncapsulatedContent }
  5. Two MIME representations:
     a. "application/pkcs7-mime; smime-type=signed-data" (opaque signing)
     b. "multipart/signed" (clear signing — body readable without S/MIME client)
```

**3. Clear Signing** (widely used for mail lists):

In `multipart/signed`, the original message body is in the first MIME part (readable by any mail client), and the signature is in the second part. Non-S/MIME clients display the message content but cannot verify the signature. S/MIME clients verify both parts.

```
Content-Type: multipart/signed; protocol="application/pkcs7-signature"; 
              micalg="sha-256"; boundary="boundary_string"

--boundary_string
Content-Type: text/plain

This is the signed message body — readable by everyone.

--boundary_string
Content-Type: application/pkcs7-signature; name="smime.p7s"
Content-Disposition: attachment; filename="smime.p7s"

[Base64-encoded PKCS#7 signature]
--boundary_string--
```

**4. Compressed Data** (`CompressedData` CMS type): S/MIME supports optional compression using zlib (RFC 3274), applied before encryption (same rationale as PGP).

**5. Certificate Management**: S/MIME includes the sender's X.509 certificate in the `SignedData` structure so the receiver can immediately verify the signature without pre-exchanging public keys. The certificate chain is verified against trusted root CAs installed in the mail client.

---

### 1.5 S/MIME Certificate Infrastructure

**X.509 Certificate Components relevant to S/MIME**:

```
X.509 v3 Certificate for S/MIME:
  Subject: CN=Alice Smith, E=alice@company.com
  Issuer:  CN=Company Email CA, O=Trusted CA Inc
  Serial:  0x1234567890ABCDEF
  Validity: 2024-01-01 to 2025-01-01
  Subject Public Key: RSA-2048 (or ECDSA P-256)
  Extensions:
    Key Usage: digitalSignature, keyEncipherment
    Extended Key Usage: emailProtection (OID 1.3.6.1.5.5.7.3.4)
    Subject Alternative Name: rfc822Name=alice@company.com
  Signature: [CA's RSA signature over all above fields]
```

The **`emailProtection` Extended Key Usage** is mandatory for S/MIME certificates — it restricts the certificate to email security and prevents it from being misused for TLS server authentication.

**Certificate revocation**:
- **CRL** (Certificate Revocation List): Periodically published list of revoked serial numbers. Mail client downloads and caches CRL.
- **OCSP** (Online Certificate Status Protocol, RFC 6960): Real-time revocation check. Mail client queries OCSP responder with certificate serial number; gets `good`, `revoked`, or `unknown`.
- **OCSP Stapling**: Server pre-fetches and includes signed OCSP response in the certificate validation payload — reduces latency and privacy concerns.

---

### 1.6 PGP vs. S/MIME — Detailed Comparison

| Feature | PGP / OpenPGP | S/MIME |
|---|---|---|
| **Standard** | RFC 4880 (OpenPGP), RFC 9580 (2024) | RFC 5751 (S/MIME v3.2) |
| **Trust model** | Decentralized Web of Trust | Hierarchical PKI (X.509 + CA) |
| **Key format** | OpenPGP binary format | X.509 DER/PEM certificates |
| **Signature algorithm** | RSA, DSA, ECDSA, EdDSA | RSA, ECDSA |
| **Encryption algorithm** | CAST-128, IDEA, 3DES, AES | 3DES, AES-128, AES-256 |
| **Hash algorithm** | MD5 (legacy), SHA-1 (legacy), SHA-256/512 | SHA-1 (legacy), SHA-256, SHA-384, SHA-512 |
| **Compression** | ZIP (before encrypt) | zlib optional (before encrypt) |
| **ASCII encoding** | Radix-64 with CRC | Base64 (standard MIME) |
| **Key revocation** | Key server removal (no real-time) | CRL / OCSP (real-time available) |
| **Multi-recipient** | Yes — one Ks, multiple RSA-wrapped copies | Yes — RecipientInfo per recipient |
| **Non-repudiation** | Yes — sender signs with private key | Yes — sender signs with private key |
| **Corporate deployment** | Difficult (no CA infrastructure) | Easy (integrates with corporate PKI/AD) |
| **Government use** | Limited (trust model complexity) | Widely used (NIST FIPS compliant) |
| **Privacy (metadata)** | Leaks sender/recipient email addresses | Same; X.509 cert reveals identity |

---

## 2. Example: Base64 Radix-64 Encoding

**Problem**: Encode the 3-byte ASCII sequence "Man" (ASCII: M=77, a=97, n=110) in Base64.

**Binary representation**:
```
M = 01001101
a = 01100001
n = 01101110
```

**Concatenate all 24 bits**:
```
010011010110000101101110
```

**Split into four 6-bit groups**:
```
010011 | 010110 | 000101 | 101110
  19   |   22   |    5   |   46
```

**Map to Base64 alphabet**:
```
Index 19 → 'T'
Index 22 → 'W'
Index 5  → 'F'
Index 46 → 'u'
```

**Result**: `"Man"` → `"TWFu"` (4 characters encoding 3 bytes, 33% overhead)

**For 1 remaining byte** (padding example with `"M"`):
```
M = 01001101 → 010011 | 01(0000) → index 19='T', index 16='Q'
Result: "TQ==" (two '=' padding characters)
```

**For 2 remaining bytes** (padding example with `"Ma"`):
```
Ma → 010011 | 010110 | 0001(00) → 'T', 'W', 'F', then '='
Result: "TWF=" (one '=' padding character)
```

---

## 3. Applications & Use Cases

1. **Journalist-Source Communication (PGP)**: Organizations like The New York Times, The Guardian, and WikiLeaks publish PGP public keys so whistleblowers can send encrypted tips that no server operator, court order, or network tap can compromise. Edward Snowden used PGP to communicate with journalists Laura Poitras and Glenn Greenwald in 2013.

2. **Corporate Email Compliance (S/MIME)**: Financial institutions, law firms, healthcare providers (HIPAA compliance), and defense contractors mandate S/MIME for emails containing PII, financial data, or classified information. Microsoft Exchange Server and Outlook natively support S/MIME with Active Directory Certificate Services (AD CS) acting as the CA.

3. **Software Package Signing (GPG)**: Ubuntu, Fedora, Debian, and other Linux distributions sign software packages with GPG. The `apt` package manager verifies signatures before installing software — preventing supply-chain attacks (e.g., a compromised mirror serving malicious packages).

4. **Code Signing on GitHub (GPG Verified Commits)**: Developers sign Git commits with their GPG key (`git commit -S`). GitHub displays a "Verified" badge on signed commits, giving users confidence that commits actually came from the claimed developer and were not injected via a compromised account or supply chain.

5. **Government Secure Email (S/MIME with PIV)**: US federal government employees use Personal Identity Verification (PIV) smart cards containing X.509 certificates issued by the Federal Bridge Certification Authority (FBCA). S/MIME with PIV provides signed and encrypted email that meets FIPS 140-2 requirements.

6. **Encrypted Mailing Lists (PGP)**: Privacy-focused communities (security researchers, journalists, activists) use PGP-encrypted mailing lists (e.g., via listserv with symmetric re-encryption) to distribute information only to verified members.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: PGP Full Message Processing — Step-by-Step [KTU Exam Pattern]

**Problem**: Alice wants to send a signed, encrypted email to Bob using PGP with:
- Plaintext: `M = "Attack at dawn"`
- Alice's private key: RSA-2048, $PR_A$
- Bob's public key: RSA-2048, $PU_B$
- Session key: $K_s$ = randomly generated 128-bit AES key

Trace the complete PGP transmission and reception flow.

**TRANSMISSION PROCESS**:

**Step 1 — Authentication (Digital Signature)**:
```
h = SHA-256("Attack at dawn")
  = e.g., 0x3F7A...C2B1  [32-byte hash]
S = RSA_Encrypt(PR_A, h) [2048-bit RSA signature over hash]
Signed_Msg = M ‖ { Algorithm: SHA-256+RSA ‖ KeyID(PR_A) ‖ S ‖ Timestamp }
```

**Step 2 — Compression**:
```
Compressed = ZIP(Signed_Msg)
[ZIP applies DEFLATE algorithm; typical reduction 40-60% for text]
```

**Step 3 — Symmetric Encryption**:
```
Ks = generate_random_128_bits()   [e.g., 0xA3B4C5D6E7F80192...]
C_M = AES_128_CFB_Encrypt(Ks, Compressed)
C_K = RSA_Encrypt(PU_B, Ks)       [Bob's 2048-bit RSA encrypts 128-bit Ks]
PGP_Binary = { KeyID(PU_B) ‖ C_K ‖ C_M }
```

**Step 4 — Radix-64 Encoding**:
```
ASCII_Output = Base64_Encode(PGP_Binary) + CRC_24
Wrapped in armor:
-----BEGIN PGP MESSAGE-----
[Base64 lines of 76 chars each]
=XXXX [CRC checksum]
-----END PGP MESSAGE-----
```

**RECEPTION PROCESS** (Bob receives the armored message):

**Step 1 — Radix-64 Decode**:
```
PGP_Binary = Base64_Decode(armored_input)
Verify CRC_24 — reject if transmission error detected
Locate KeyID(PU_B) → Bob knows to use his own private key PR_B
```

**Step 2 — Symmetric Decryption**:
```
Ks = RSA_Decrypt(PR_B, C_K)
Compressed = AES_128_CFB_Decrypt(Ks, C_M)
```

**Step 3 — Decompression**:
```
Signed_Msg = UNZIP(Compressed)
```

**Step 4 — Signature Verification**:
```
Separate: M and Signature_Component from Signed_Msg
Extract: { Algorithm, KeyID(PR_A), S, Timestamp }
h' = SHA-256(M)                     [recompute hash of received message]
h  = RSA_Decrypt(PU_A, S)          [recover signed hash using Alice's public key]
Compare: h' == h?
  YES → Message authenticated (from Alice) and unmodified. Display to Bob.
  NO  → REJECT — either modified in transit or not from Alice.
```

---

### Example 2: Why Compression Must Precede Encryption [Conceptual Analysis]

**Problem**: Analyze what happens to compression effectiveness (a) before encryption and (b) after encryption. Show with entropy analysis why order matters.

**Analysis**:

**(a) Compress Before Encrypt (Correct PGP Order)**:

A 1000-character English email has approximately:
- Shannon entropy of English ≈ 1.3 bits/character (with long-range correlations).
- ZIP compression achieves ≈ 60% reduction.
- After ZIP: ≈ 400 bytes with near-uniform byte distribution (high entropy ≈ 7.5 bits/byte).
- After AES encryption: ≈ 400 bytes of uniform random bytes (≈ 8.0 bits/byte).

Total transmitted: **≈ 400 bytes** (compressed + encrypted).

**(b) Encrypt Before Compress (Incorrect, Useless Order)**:

- After AES encryption of 1000-byte email: 1000 bytes of pseudo-random output.
- AES output has entropy ≈ 8.0 bits/byte — indistinguishable from random.
- ZIP applied to random data: typically INCREASES size slightly (ZIP header overhead, no patterns to exploit).
- After ZIP: ≈ **1005–1020 bytes** (marginally larger than before compression!).

Total transmitted: **≈ 1005 bytes** — 2.5× larger than correct order, with zero compression benefit.

**(c) Cryptographic Security Benefit of Compressing First**:

Plain "Attack at dawn" — letter frequencies match English (A: 3×, T: 2×, etc.). A perfect compression algorithm would encode this as ~50 bits. After compression:

| Property | Before Compression | After Compression |
|---|---|---|
| Size | 112 bits (14 chars × 8 bits) | ≈ 50 bits (estimated) |
| Entropy | 1.3 bits/char (English) | ≈ 6–7 bits/char (near-uniform) |
| Known patterns | Yes — 'A' most common | No — compression eliminates patterns |
| Vulnerability to statistical attacks | Higher | Lower |

**Conclusion**: Compressing before encrypting provides both bandwidth savings AND cryptographic hardening. The order is mandated by PGP's protocol design and the mathematical properties of entropy.

---

### Example 3: Radix-64 CRC Computation [Exam Pattern]

**Problem**: Explain the role of the 24-bit CRC in PGP Radix-64 encoding and how it differs from standard Base64.

**Solution**:

**Standard Base64 (RFC 4648)**:
- Maps binary data to ASCII-printable characters.
- Uses alphabet: `A-Z a-z 0-9 + /` and `=` for padding.
- Provides NO error detection — a corrupted Base64 stream decodes to corrupted binary silently.
- Used in: HTML email (MIME), JWT, HTTP Basic Auth headers.

**PGP Radix-64 (RFC 4880 §6)**:
- Uses identical character alphabet as Base64.
- Appends a **24-bit CRC** checksum as 4 Base64 characters after `=`.
- CRC is computed over the **raw binary data** before Base64 encoding.
- CRC polynomial: $x^{24} + x^{23} + x^6 + x^5 + x + 1$ (0xB704CE).

**Why the PGP CRC matters**:
Email relaying can corrupt binary data via:
- Line length reformatting (some MTAs wrap lines differently).
- CR/LF conversion (Unix `\n` vs. Windows `\r\n`).
- Character set re-encoding (Latin-1 misinterpreted as UTF-8).
- Trailing whitespace stripping.

If any of these corruptions occur, the decoded binary would be silently wrong — a corrupted signature or a corrupted ciphertext would produce garbage. The 24-bit CRC detects virtually all 1-byte transmission errors (error detection probability for a random error = $1 - 2^{-24} \approx 99.999994\%$).

**Format in the armor**:
```
-----BEGIN PGP MESSAGE-----

hQEMA...Base64 content...
...more Base64 lines...
=ABCD     ← The 4 chars "ABCD" are the 24-bit CRC in Base64
-----END PGP MESSAGE-----
```

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU June 2022, Part A, Q8 — 4 Marks]
**Question**: Explain the cryptographic services offered by PGP.

**Solution**:

PGP (Pretty Good Privacy) provides **five cryptographic services** for email security:

**1. Digital Signature (Authentication + Non-Repudiation)**:
- Sender computes $h = H(M)$ (SHA-256 hash of message).
- Sender signs: $S = E(PR_A, h)$ (RSA or DSA with sender's private key).
- Any recipient verifies using sender's public key $PU_A$.
- Non-repudiation: only the holder of $PR_A$ could generate the valid signature.

**2. Confidentiality (Symmetric + Asymmetric Hybrid Encryption)**:
- Sender generates random session key $K_s$ (AES-128 or CAST-128).
- Message encrypted: $C_M = E(K_s, M)$ (fast symmetric encryption).
- Session key encrypted: $C_K = E(PU_B, K_s)$ (RSA with recipient's public key).
- Recipient recovers $K_s = D(PR_B, C_K)$, then decrypts $M = D(K_s, C_M)$.

**3. Compression**:
- PGP applies ZIP compression to message+signature **before encryption**.
- Reduces transmission size (typically 40–60% for text).
- Increases cryptographic security by removing statistical redundancy from plaintext before encryption.
- (Compressing after encryption is useless — ciphertext cannot be compressed.)

**4. Email Compatibility (Radix-64 / Base64 Encoding)**:
- PGP produces binary ciphertext; legacy email servers require 7-bit ASCII.
- Radix-64 maps each 3 bytes of binary to 4 printable ASCII characters.
- PGP's Radix-64 adds a 24-bit CRC for transmission error detection.
- Overhead: 33% size increase for ASCII encoding.

**5. Key Management (Web of Trust)**:
- No central CA. Users maintain public and private key rings.
- Trust established by mutual key signing between users.
- Trust is transitive: if Alice trusts Bob and Bob certifies Carol's key, Alice can validate Carol.
- Keys published to public key servers (e.g., keys.openpgp.org).

---

### Question 2 [KTU May 2019, Part C, Q17(a) — 5 Marks]
**Question**: Describe the operational steps of PGP in detail with diagram.

**Solution**:

**PGP Operational Flow** (for signed + encrypted message):

```
ALICE (Sender)                              BOB (Receiver)
──────────────                              ──────────────
M (Plaintext)                               ↓
    │                                    ASCII Armor Strip
    ▼                                       │
[1] H = SHA-256(M)                          ▼ Radix-64 Decode
    │                                    Binary PGP Packet
    ▼                                       │
[2] S = RSA(PR_A, H) ← signs               ▼ [7] Ks=RSA(PR_B, C_K)
    │   with Alice's                    Session key recovered
    ▼   private key                         │
    M ‖ S = Signed Content                  ▼ [8] Decompress+Decrypt
    │                                    M ‖ S (signed content)
    ▼                                       │
[3] ZIP(M ‖ S)                              ▼ [9] Separate M and S
    │ ← Compress BEFORE encrypt             │
    ▼                                       ▼
[4] Ks = random_128()             h' = SHA-256(M)
    C_M = AES(Ks, ZIP(M‖S))           h = RSA_Decrypt(PU_A, S)
    C_K = RSA(PU_B, Ks)             h' == h? → Accept/Reject
    │                                       │
    ▼                                       ▼
[5] Radix-64 Encode              [10] If valid: Display M to Bob
    │   + CRC-24
    ▼
[6] -----BEGIN PGP MESSAGE-----
    [Base64 lines]
    =CRC4
    -----END PGP MESSAGE-----
    → Send via SMTP
```

**Steps summarized**:
1. Hash plaintext: $h = SHA\text{-}256(M)$
2. Sign: $S = E(PR_A, h)$
3. Compress: $ZIP(M \| S)$
4. Encrypt: $K_s = \text{random}()$; $C_M = AES(K_s, ZIP(M\|S))$; $C_K = RSA(PU_B, K_s)$
5. Radix-64 encode with CRC
6. Transmit via SMTP

On reception (reverse): Decode → Decrypt → Decompress → Verify signature.

---

### Question 3 [KTU January 2023, Part C, Q17 — 9 Marks]
**Question**: Describe Pretty Good Privacy (PGP). Explain its key management approach.

**Solution**:

**Part A — PGP Overview**:

PGP (Pretty Good Privacy), created by Philip Zimmermann in 1991, is an open-source email security system that provides **confidentiality, authentication, compression, and email compatibility**. Standardized as OpenPGP (RFC 4880), it is the most widely used personal email encryption system worldwide. GNU Privacy Guard (GnuPG/GPG) is its primary open-source implementation.

**Five PGP Services** (brief — full detail in Q1 solution above):
1. Digital signature (SHA-256 hash + RSA/ECDSA sign with private key).
2. Confidentiality (AES/CAST-128 symmetric encrypt; RSA-encrypt session key for recipient).
3. Compression (ZIP before encryption — removes statistical redundancy).
4. Email compatibility (Radix-64 / Base64 encoding for 7-bit SMTP; CRC for error detection).
5. Key management (Web of Trust).

**Part B — PGP Key Management**:

PGP's key management is fundamentally different from PKI:

**Key Generation**: Each user generates their own RSA/ECDSA key pair. Private key is encrypted with a passphrase-derived key and stored in the private keyring. Public key is published to key servers.

**Key Identification**: Each PGP key has:
- **Fingerprint**: SHA-256 (or SHA-1) hash of the entire public key — 40 hex characters. Used for manual key verification (e.g., read over phone).
- **Key ID**: Lower 64 bits of fingerprint. Used in PGP messages to identify which key to use.

**Web of Trust**:

The central idea: instead of a CA vouching for key-identity bindings, *users sign each other's keys*. If Alice signs Bob's key (certifying "I verified Bob owns this key"), Alice's signature on Bob's key increases the trust level of Bob's key for anyone who trusts Alice.

```
Trust levels in GnuPG:
  Unknown      → Key received, no trust assigned
  Marginal (m) → Key signed by ≤2 marginally trusted parties
  Full (f)     → Key signed by ≥1 fully trusted key 
                  OR signed by ≥3 marginally trusted keys
  Ultimate (u) → Own key (you trust yourself completely)
```

**Validity rules** for Bob's key $K_B$ to be considered valid for Alice:
- $K_B$ signed by Alice directly → valid.
- $K_B$ signed by one `full` trusted key in Alice's keyring → valid.
- $K_B$ signed by $\ge 3$ `marginal` trusted keys in Alice's keyring → valid.

**Key Rings** (internal PGP data structures):
1. **Public Key Ring**: Stores all known public keys, each with:
   - Key ID, public key material (modulus $n$, exponent $e$ for RSA).
   - Owner trust level (assigned by user).
   - Key legitimacy (computed from signatures + trust levels).
   - Bound email addresses and names (User IDs).
   - Signatures from other PGP users.

2. **Private Key Ring**: Stores user's own private key, encrypted with:
   $K_{ring} = MD5(\text{passphrase})$ (legacy), or Argon2/bcrypt-derived key (modern).

**Key Server Infrastructure**: Public keys are published to distributed key servers (`keys.openpgp.org`, `keyserver.ubuntu.com`). Lookups by email address or Key ID. Key servers replicate among themselves. **Limitation**: Key servers do not verify email ownership — anyone can upload a key claiming any email address. This is an inherent limitation of PGP's decentralized model.

**Key Revocation**: A user can generate a **revocation certificate** for their key pair and upload it to key servers. Revocation should be generated when the private key is compromised. **Limitation**: No real-time revocation checking — PGP clients must manually refresh keys from servers.

**Comparison with S/MIME PKI**:
- PGP: grassroots trust; scalable for individuals; complex to establish trust in enterprise settings.
- S/MIME: institutional trust via CA hierarchy; integrated with corporate directories (LDAP); real-time revocation via OCSP; legally recognized in regulated industries.

---

### Question 4 [KTU June 2022, Part C, Q17 — 9 Marks]
**Question**: What is S/MIME? How does S/MIME provide secure email services? Explain with the steps for preparing enveloped data and signed data.

**Solution**:

**Part A — S/MIME Overview**:

S/MIME (Secure/Multipurpose Internet Mail Extensions, RFC 5751) is a standard for public-key-based email security using **X.509 certificates** and **PKCS#7/CMS** (Cryptographic Message Syntax) data structures. It is natively integrated into Microsoft Outlook, Apple Mail, IBM Notes, and most enterprise email clients.

S/MIME provides four core security services:
1. **Confidentiality** — Symmetric encryption of email body with per-recipient encrypted session key.
2. **Authentication** — Digital signatures using sender's X.509-certified private key.
3. **Integrity** — Cryptographic hash over signed content; any modification detected.
4. **Non-repudiation** — Valid signature with private key proves origin; cannot be repudiated.

**Part B — Preparing Enveloped Data (Confidentiality)**:

Enveloped data provides **encryption** so only intended recipients can read the message.

**Step 1 — Generate Session Key**:
$$K_s = \text{CSPRNG}(128\text{ or }256\text{ bits}) \quad \text{e.g., AES-128}$$

**Step 2 — Encrypt Message Content**:
$$C = E(K_s, M) \quad \text{using AES-128-CBC or 3DES-CBC}$$

**Step 3 — Encrypt Session Key for Each Recipient**:

For each recipient $i$ with X.509 certificate (public key $PU_i$):
$$C_{Ki} = E(PU_i, K_s) \quad \text{(RSA-OAEP encryption of } K_s\text{)}$$

Build `RecipientInfo` structure for each recipient:
```
RecipientInfo {
  version: 0,
  issuerAndSerialNumber: { issuer: "CN=Company CA", serialNumber: 0xABC... },
  keyEncryptionAlgorithm: { algorithm: rsaEncryption },
  encryptedKey: C_Ki
}
```

**Step 4 — Build EnvelopedData Structure**:
```
EnvelopedData {
  version: 0,
  recipientInfos: [ RecipientInfo_1, ..., RecipientInfo_n ],
  encryptedContentInfo: {
    contentType: data,
    contentEncryptionAlgorithm: { algorithm: aes128-CBC, iv: [random IV] },
    encryptedContent: C
  }
}
```

**Step 5 — MIME Wrapping**:
```
Content-Type: application/pkcs7-mime; smime-type=enveloped-data; name="smime.p7m"
Content-Transfer-Encoding: base64

[Base64-encoded EnvelopedData DER encoding]
```

**Part C — Preparing Signed Data (Authentication)**:

Signed data provides **authentication and integrity** via a digital signature.

**Step 1 — Compute Message Digest**:
$$h = SHA\text{-}256(M)$$

**Step 2 — Generate Digital Signature**:
$$S = E(PR_{\text{sender}}, h) \quad \text{(RSA-PSS or ECDSA)}$$

**Step 3 — Build SignerInfo Structure**:
```
SignerInfo {
  version: 1,
  issuerAndSerialNumber: { issuer, serialNumber of sender's cert },
  digestAlgorithm: sha256,
  authenticatedAttributes: [
    contentType: data,
    signingTime: "2024-10-17T12:00:00Z",
    messageDigest: h
  ],
  signatureAlgorithm: rsaEncryption,
  signature: S,
  unauthenticatedAttributes: [...]
}
```

**Step 4 — Build SignedData Structure**:
```
SignedData {
  version: 1,
  digestAlgorithms: [ sha256 ],
  encapsulatedContentInfo: { contentType: data, content: M },
  certificates: [ sender_cert, intermediate_CA_cert ],
  signerInfos: [ SignerInfo ]
}
```

**Step 5 — MIME Wrapping** (two options):

*Opaque signing* (body unreadable without S/MIME):
```
Content-Type: application/pkcs7-mime; smime-type=signed-data; name="smime.p7m"
Content-Transfer-Encoding: base64

[Base64 DER-encoded SignedData with message embedded]
```

*Clear signing* (body readable by all; signature separate):
```
Content-Type: multipart/signed; protocol="application/pkcs7-signature";
              micalg="sha-256"; boundary="----BOUNDARY"

------BOUNDARY
Content-Type: text/plain

[Original message body — readable by all mail clients]

------BOUNDARY
Content-Type: application/pkcs7-signature; name="smime.p7s"

[Base64 DER-encoded SignedData (signature only, no message body)]
------BOUNDARY--
```

**S/MIME vs. PGP key management summary**:
- S/MIME uses X.509 certificates from trusted CAs — easier for enterprises (integrated with Active Directory, LDAP).
- PGP uses Web of Trust — better for individuals and decentralized communities.
- S/MIME provides real-time revocation (OCSP); PGP relies on manual key server updates.
