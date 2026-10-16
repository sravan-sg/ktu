# Authentication Requirements and Message Authentication Codes (MAC)

## 1. Explanation

### 1.1 Why Authentication? — The Deep Intuition

Encryption alone provides **confidentiality** — only the intended recipient can read the message. But it provides **no guarantee that the message is genuine**. An active adversary who cannot read the plaintext can still:

- **Replay** a captured ciphertext at a different time.
- **Modify** ciphertext bits (especially in stream modes like CTR or CBC without MAC).
- **Inject** fake ciphertexts that didn't come from the legitimate sender.
- **Reorder** a sequence of valid messages.

**Authentication** is the mechanism that answers two distinct questions:
1. **Origin authentication**: Did this message actually come from the claimed sender?
2. **Integrity authentication**: Was the message modified in transit?

This is fundamentally different from confidentiality. A secure system deployed in the real world needs **both** — and the mechanisms are often independent. In fact, modern cryptographic wisdom says: **encrypt-then-MAC**, not **MAC-then-encrypt**.

---

### 1.2 Security Threats in Communication

Stallings (*CNS*, Chapter 11) classifies attacks into those against **passive** opponents (observing traffic) and **active** opponents (modifying traffic). Unauthenticated communication channels face seven major attack classes:

| # | Attack | Description | Authentication Can Prevent? |
|---|---|---|---|
| 1 | **Disclosure** | Release of message contents to unauthorized parties. | No (this is a confidentiality attack) |
| 2 | **Traffic Analysis** | Inferring communication patterns, identities, and frequency from ciphertext. | No (traffic analysis is a passive attack on metadata) |
| 3 | **Masquerade (Impersonation)** | Attacker sends messages purporting to originate from an authorized entity. | **Yes** — MAC binds messages to key holders |
| 4 | **Content Modification** | Alteration, insertion, deletion, or transposition of parts of a valid message. | **Yes** — any modification changes the MAC |
| 5 | **Sequence Modification** | Insertion, deletion, or reordering of messages in a multi-message exchange. | **Yes** — if sequence numbers are included in MAC input |
| 6 | **Timing Modification** | Replay of valid messages, or delay/reorder delivery beyond acceptable time. | **Yes** — if timestamps or nonces are included in MAC input |
| 7 | **Repudiation** | Sender denies having sent a message; receiver denies having received it. | **Partially** — shared-key MACs cannot prove to third parties; digital signatures are needed |

> **Key insight**: A shared-key MAC proves to the receiver that "whoever computed this MAC knows the shared key $K$" — which is the sender, if key distribution was secure. But it does NOT prove this to a third-party arbiter, because both sender and receiver know $K$ (either could have generated the MAC). For non-repudiation to a third party, you need digital signatures (asymmetric cryptography).

---

### 1.3 Authentication Functions — Three Categories

Stallings identifies three classes of functions that provide message authentication:

#### Category 1: Message Encryption as Authenticator

The ciphertext itself functions as the authenticator. The assumption: only a legitimate party who knows the key could produce a ciphertext that decrypts to intelligible (grammatically valid, properly structured) plaintext.

**Symmetric Encryption for Authentication**:
$$C = E_K(M)$$
- Receiver decrypts $C$ to $M' = D_K(C)$.
- If $M'$ has recognizable structure (language patterns, format markers, checksum), authentication is achieved — a modified ciphertext would decrypt to gibberish.
- **Weakness**: Provides only weak authentication. Certain types of modification (especially in stream cipher modes) may produce "valid-looking" garbage. Better to use explicit MACs.

**Asymmetric Encryption for Authentication (Digital Signature)**:
$$S = E_{PR_A}(M) \quad \text{(Sign with private key)}$$
$$M = D_{PU_A}(S) \quad \text{(Verify with public key)}$$
- Provides **non-repudiation**: only $A$ (holder of $PR_A$) could have created $S$.
- Any party with $PU_A$ can verify.

**Internal Error Detection**: Adding a structured field to the plaintext (e.g., a fixed header, FCS/checksum) before encryption provides a verification mechanism: if decryption produces a valid internal structure, the message is authentic. This is weak — not all modifications destroy structure.

#### Category 2: Message Authentication Code (MAC)

A MAC function takes:
- A variable-length message $M$
- A shared secret key $K$

And produces a **fixed-length authentication tag** (cryptographic checksum):
$$\text{Tag} = C(K, M)$$

The message and tag are transmitted together: $(M \| \text{Tag})$.

**Verification by receiver**: Recompute $C(K, M)$ and compare to received Tag bit-by-bit.

If they match, the receiver concludes:
1. **Integrity**: $M$ was not modified (any modification changes Tag).
2. **Authenticity**: The sender possessed key $K$ (which only the legitimate parties share).
3. **Anti-replay** (if sequence numbers in $M$): The message is in proper order.

**Key distinction from encryption**: A MAC does NOT encrypt the message. $M$ is transmitted in plaintext alongside Tag. This is appropriate when **confidentiality is not required** but integrity/authenticity is (e.g., broadcast messages, public software updates, routing table updates, firmware images).

**MAC vs. Hash function**: A MAC requires a **secret key** — the tag cannot be forged without knowing $K$. A hash function alone is public and keyless — anyone can compute $H(M)$, so it provides integrity but not authenticity on its own.

#### Category 3: Cryptographic Hash Functions

A hash function $H$ maps arbitrary-length messages to a fixed-length digest $h = H(M)$:
- **Public function**: No secret key.
- Provides **integrity** (a modified message produces a different hash) but NOT authenticity alone.
- Authentication is achieved by combining $H$ with a secret:

| Method | Formula | Protocol | Security |
|---|---|---|---|
| Encrypted hash | $C = E_K(H(M))$ | Sender encrypts hash | Requires symmetric key |
| Digital signature | $S = E_{PR_A}(H(M))$ | Sender signs hash | Non-repudiation |
| HMAC | $H((K \oplus \text{opad}) \| H((K \oplus \text{ipad}) \| M))$ | Nested keyed hash | Standardized, secure |
| Keyed hash (insecure) | $H(K \| M)$ | NOT RECOMMENDED | Vulnerable to length extension |

---

### 1.4 Message Authentication Codes — Detailed Architecture

#### 1.4.1 MAC Properties (Formal Security Requirements)

A MAC function $C(K, M)$ must satisfy:
1. **Computation resistance**: Given a sequence of pairs $(M_i, T_i)$, it must be computationally infeasible to compute a valid pair $(M, T)$ for any new message $M \notin \{M_i\}$, even with chosen-message capability.
2. **Uniformity**: A valid authentication tag should be uniformly distributed over $\{0,1\}^m$ — an adversary guessing a tag for a new message succeeds with probability $2^{-m}$ for tag length $m$.
3. **Key non-dependence of output**: Different keys must produce outputs that appear independent — no key $K$ "leaks" from the tags.

#### 1.4.2 MAC for Authentication Only

When **confidentiality is NOT needed** (e.g., integrity of firmware images, router advertisement packets, software release signatures):

```
Sender:   Tag = C(K, M)      Transmit: (M ‖ Tag)
Receiver: Tag' = C(K, M)     Verify: Tag' == Tag?
```

Use cases:
- **RFC 4822 (RIPv2 authentication)**: Route updates authenticated with HMAC-MD5.
- **Software distribution**: Linux package managers (apt, rpm) verify SHA-256 hashes signed by the repository key.
- **SCADA/ICS control messages**: Operator commands to RTUs authenticated but not encrypted for latency reasons.

#### 1.4.3 MAC for Authentication and Confidentiality — Three Paradigms

When both authentication and confidentiality are needed, the MAC and encryption must be combined. Three approaches exist:

**Approach 1: Encrypt-and-MAC (E&M)**
$$C = E(K_1, M),\quad T = C(K_2, M),\quad \text{Send } (C \| T)$$
- Used in: **SSH (RFC 4253)**.
- Vulnerability: The MAC $T$ is computed over plaintext $M$. This can **leak information** about $M$ — the MAC might reveal whether two plaintexts are identical even if ciphertexts differ.

**Approach 2: MAC-then-Encrypt (MtE)**
$$T = C(K_1, M),\quad C = E(K_2, M \| T),\quad \text{Send } C$$
- Used in: **SSL 3.0, TLS 1.0, TLS 1.1**.
- Fatal vulnerability: The receiver must **decrypt before verifying** the MAC. If decryption fails with a padding error, the error message is returned before MAC verification completes. This creates a **Padding Oracle** — an attacker can decrypt any ciphertext block by observing which decryptions produce valid padding. Exploited by: POODLE (SSLv3), Lucky Thirteen (TLS), BEAST (TLS 1.0).

**Approach 3: Encrypt-then-MAC (EtM) — Cryptographically Recommended**
$$C = E(K_1, M),\quad T = C(K_2, C),\quad \text{Send } (C \| T)$$
- Used in: **IPsec (RFC 4303 ESP), TLS 1.3 (AEAD), Signal Protocol**.
- Security: Receiver verifies $T$ over $C$ **before any decryption**. Invalid tag → packet dropped immediately, no decryption oracle possible.
- Provably secure: If either the cipher or the MAC is secure, EtM composition is secure (Krawczyk's "Authenticated Encryption" result).
- **TLS 1.3** mandates Authenticated Encryption with Associated Data (AEAD) ciphers (AES-GCM, ChaCha20-Poly1305) which implement EtM internally in a single pass.

> **Why EtM wins**: Padding oracles, timing side-channels on decryption, and buffer overflows in the decryption path are all eliminated because invalid-MAC packets never reach the decryption code path.

---

### 1.5 HMAC (Hash-Based Message Authentication Code)

#### 1.5.1 Overview and Motivation

**HMAC** (RFC 2104, FIPS PUB 198) was designed to solve a critical weakness: simple keyed hash constructions of the form $H(K \| M)$ or $H(M \| K)$ are vulnerable to **length extension attacks** in Merkle-Damgård hash functions (MD5, SHA-1, SHA-256).

**Length Extension Attack on $H(K \| M)$**:
- The Merkle-Damgård construction makes $H(K \| M)$ computable from $H(K \| M \| M')$ for arbitrary $M'$, **without knowing $K$**.
- An attacker who sees $H(K \| M)$ can compute $H(K \| M \| \text{padding} \| M')$ for any $M'$ of their choice.
- This allows tag forgery for extended messages — catastrophic for API authentication.

**HMAC defeats length extension** by nesting two hash invocations with different key derivatives:
$$\text{HMAC}_K(M) = H\Big((K^+ \oplus \text{opad}) \| H\big((K^+ \oplus \text{ipad}) \| M\big)\Big)$$

The inner hash output is only an **intermediate value** — an attacker cannot extend it because the outer hash applies a different key transform before finalizing.

#### 1.5.2 HMAC Parameters

| Parameter | Symbol | Value for SHA-1 | Value for SHA-256 | Meaning |
|---|---|---|---|---|
| Block length | $B$ | 64 bytes | 64 bytes | Hash function's internal block size |
| Digest length | $L$ | 20 bytes | 32 bytes | Hash output length |
| Key | $K$ | Any length | Any length | Shared secret |
| Padded key | $K^+$ | 64 bytes | 64 bytes | Key padded with zeros to length $B$ |
| Inner pad | ipad | `0x36` × 64 | `0x36` × 64 | Fixed constant byte repeated $B$ times |
| Outer pad | opad | `0x5C` × 64 | `0x5C` × 64 | Fixed constant byte repeated $B$ times |

**Key padding rule**:
- If $|K| < B$: Pad $K$ with zeros on the right to get $K^+$.
- If $|K| > B$: Replace $K$ with $H(K)$, then pad to $B$ bytes.

#### 1.5.3 HMAC Step-by-Step Execution

```
INPUT: Key K, Message M

Step 1: Prepare K+ (pad key to B bytes)
        If |K| < B: K+ = K ‖ 0x00...00
        If |K| = B: K+ = K
        If |K| > B: K+ = H(K) ‖ 0x00...00

Step 2: Compute inner key block
        S_i = K+ XOR ipad     (XOR each byte with 0x36)

Step 3: Compute outer key block
        S_o = K+ XOR opad     (XOR each byte with 0x5C)

Step 4: Inner hash (Pass 1)
        inner_hash = H(S_i ‖ M)

Step 5: Outer hash (Pass 2)
        HMAC = H(S_o ‖ inner_hash)

OUTPUT: HMAC tag (L bytes)
```

#### 1.5.4 Why ipad = 0x36 and opad = 0x5C?

These constants ensure that $S_i = K^+ \oplus \text{ipad}$ and $S_o = K^+ \oplus \text{opad}$ differ in **every bit position** (since $0x36 \oplus 0x5C = 0x6A$, which has all bits set in the right pattern). This ensures the inner and outer hash computations use maximally different initial key material — preventing attacks that exploit similar inner/outer key values.

#### 1.5.5 Security Properties of HMAC

1. **Length Extension Resistance**: The nested structure prevents length extension — the inner hash is only an intermediate and is re-processed by the outer hash with a different key.
2. **Keyed PRF (Pseudorandom Function)**: HMAC is a secure PRF if the underlying hash is a secure PRF. Even if a compression function collision is found, HMAC security is maintained.
3. **Collision Resistance**: HMAC inherits the collision resistance of the underlying hash function. MD5 is broken for direct use but HMAC-MD5 remains secure for MAC purposes (though deprecated).
4. **Speed**: HMAC-SHA256 runs at ~400 MB/s on modern hardware (compared to raw SHA256 at ~500 MB/s) — the overhead is minimal (only two extra hash block computations per message, regardless of message length).

---

### 1.6 Brute-Force Attacks on MACs

#### 1.6.1 Two Attack Modes

**Attack 1: Key Recovery**

An adversary has access to $n_0$ valid $(M_i, T_i)$ pairs and wants to find $K$.

- Try all $2^k$ possible keys.
- For any single pair $(M_1, T_1)$: On average $2^{k-m}$ keys produce the correct tag $T_1$ by coincidence.
- To isolate the true key: Need $\lceil k/m \rceil$ independent $(M_i, T_i)$ pairs to reduce false positives.
- **Total work**: $2^k$ tests, with $\lceil k/m \rceil$ pairs required.

**Attack 2: Tag Forgery (Without Key Recovery)**

Given a new message $M^*$ (not in the observed pairs), the adversary generates a random guess for the tag.
- The probability any guess is correct is $2^{-m}$.
- Expected attempts to forge: $2^m$.
- This is the **minimum effort** to break a MAC — hence tag length must be $\ge 96$ bits (NIST SP 800-107 recommends $\ge 128$-bit MACs).

**Governing Security Parameter**: $\min(2^k, 2^m)$.

| MAC Tag Length ($m$) | Key Length ($k$) | Governing Security | Practical Safety |
|---|---|---|---|
| 32 bits | 128 bits | $2^{32}$ (tag forgery) | Broken in milliseconds |
| 64 bits | 128 bits | $2^{64}$ | Borderline |
| 96 bits | 128 bits | $2^{96}$ | Acceptable |
| 128 bits | 256 bits | $2^{128}$ (key recovery) | Recommended |

**Key lesson**: If the MAC tag is short (say 32 bits for performance), the MAC can be broken by online guessing attacks in $2^{32}$ attempts — regardless of how large the key is. The tag length is the binding security constraint, not just the key length (unlike symmetric encryption where key length alone determines security).

---

## 2. Example: HMAC Inner and Outer Hashing Visualization

```
Secret Key K (arbitrary length)
       │
       ▼ [If |K| < B: pad; if |K| > B: hash + pad]
       K+ (exactly B bytes)
       │
   ┌───┴───────────────┐
   │                   │
   XOR ipad (0x36×B)   XOR opad (0x5C×B)
   │                   │
   S_i (B bytes)       S_o (B bytes)
   │                   │
   ▼                   │
[Append M]             │
   │                   │
   ▼                   │
[Hash H — Pass 1]      │
   │                   │
   inner_hash (L bytes)│
   │                   │
   └──── Append ───────┘
              │
              ▼
         [Append inner_hash to S_o]
              │
              ▼
         [Hash H — Pass 2]
              │
              ▼
         HMAC Tag (L bytes)
```

---

## 3. Applications & Use Cases

1. **REST API Authentication (AWS Signature Version 4, GitHub)**: HTTP requests are authenticated using `HMAC-SHA256(secret_key, canonical_request)`. The server recomputes the HMAC and rejects any request with a mismatched tag — preventing replay, modification, and impersonation attacks without requiring TLS client certificates.

2. **JWT (JSON Web Tokens) in SSO Systems**: JWT `HS256` algorithm uses HMAC-SHA256 to sign claims. The signature field = `HMAC-SHA256(secret, base64url(header) + "." + base64url(payload))`. Used in OAuth 2.0, OpenID Connect.

3. **Cookie Integrity (CSRF Protection)**: Web frameworks (Django, Rails, Express) sign session cookies with HMAC — any tampered cookie is rejected, preventing session hijacking.

4. **Disk Encryption Integrity (LUKS/dm-crypt)**: Full-disk encryption systems use HMAC-SHA256 to authenticate sector headers. Without integrity checking, an attacker with physical access could silently flip encrypted bits.

5. **Protocol Message Authentication**: TLS 1.2 uses HMAC-SHA256 for record authentication. Network protocols (BGP, OSPF) use HMAC-MD5/SHA1 to authenticate routing updates and prevent route injection attacks.

6. **VPN Authentication (IPsec ESP)**: IPsec ESP uses HMAC-SHA256-128 (128-bit truncated HMAC-SHA256) to authenticate encrypted IP packets — the Encrypt-then-MAC paradigm for maximum security.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: MAC vs. Encryption Brute-Force Work Factor Comparison [KTU May 2019, Q6]

**Problem**: Compare brute-force attack effort against MAC and symmetric encryption.

**Setup**: Key length $k = 128$ bits. MAC tag length $m = 32$ bits (short, for illustration). 1 million messages authenticated per second.

**Part 1 — Brute-Force on Symmetric Encryption ($k = 128$)**:
- Adversary needs to find the unique key $K$ from $(M, C)$ pairs.
- Since plaintext has recognizable structure, 1–2 $(M, C)$ pairs are sufficient to identify the correct key.
- Work: $2^{128} \approx 3.4 \times 10^{38}$ key trials.
- At $10^{15}$ trials/second (modern GPU cluster): $2^{128} / 10^{15} \approx 3.4 \times 10^{23}$ seconds — astronomically long.
- **Security dominated by key length $k$: $O(2^k) = O(2^{128})$**.

**Part 2 — Brute-Force on MAC (k = 128, m = 32)**:

*Attack A — Key Recovery*:
- For a single $(M_1, T_1)$, test all $2^{128}$ candidate keys.
- Expected false positives per test: $2^{128-32} = 2^{96}$ spurious keys produce $T_1$ for $M_1$ by coincidence.
- Need $\lceil 128/32 \rceil = 4$ pairs to isolate the unique key.
- Total work: $4 \times 2^{128}$ — similar to symmetric encryption.

*Attack B — Tag Forgery (No key recovery needed)*:
- Adversary guesses a 32-bit tag for a forged message $M^*$.
- Probability of success per guess: $2^{-32} \approx 2.3 \times 10^{-10}$.
- Expected trials for successful forgery: $2^{32} \approx 4.3 \times 10^9$.
- At $10^6$ online guesses/second (rate-limited by server): $4294$ seconds ≈ **71 minutes** to forge a valid MAC!

**Conclusion**: MAC with 32-bit tag provides only $2^{32}$ security against forgery — trivially broken. The key length is irrelevant. **Use $m \ge 128$ bits for production MACs.**

| Scheme | Key Length | Tag Length | Security Measure | Work to Break |
|---|---|---|---|---|
| Symmetric encryption | 128 bits | N/A | $2^{128}$ (key recovery) | $\approx 2^{128}$ |
| MAC (short tag) | 128 bits | 32 bits | $\min(2^{128}, 2^{32}) = 2^{32}$ | **71 minutes online** |
| MAC (recommended) | 256 bits | 128 bits | $2^{128}$ | $\approx 2^{128}$ |

---

### Example 2: HMAC-SHA1 — Complete Key Padding Walkthrough

**Problem**: Given a 128-bit (16-byte) key $K$, trace through HMAC-SHA1 parameter preparation.

**Setup**: SHA-1 block size $B = 64$ bytes, digest $L = 20$ bytes. Key = `0x000102030405060708090A0B0C0D0E0F` (16 bytes).

**Step 1 — Pad key $K$ to $B = 64$ bytes**:
$$K^+ = K \| \underbrace{0x00 \cdots 00}_{48 \text{ zero bytes}} \quad \text{(total 64 bytes)}$$

**Step 2 — Compute $S_i = K^+ \oplus \text{ipad}$** (ipad = `0x36` repeated 64 times):
- First 16 bytes: $K_i \oplus 0x36$ (e.g., byte 0: $0x00 \oplus 0x36 = 0x36$; byte 1: $0x01 \oplus 0x36 = 0x37$; ...)
- Remaining 48 bytes: $0x00 \oplus 0x36 = 0x36$ (all become `0x36`)

**Step 3 — Compute $S_o = K^+ \oplus \text{opad}$** (opad = `0x5C` repeated 64 times):
- First 16 bytes: $K_i \oplus 0x5C$ (byte 0: $0x00 \oplus 0x5C = 0x5C$; byte 1: $0x01 \oplus 0x5C = 0x5D$; ...)
- Remaining 48 bytes: $0x00 \oplus 0x5C = 0x5C$ (all become `0x5C`)

**Step 4 — Inner hash** (Pass 1):
$$\text{inner} = \text{SHA1}(S_i \| M) \quad \text{(64-byte } S_i \text{ + variable-length message M)}$$

**Step 5 — Outer hash** (Pass 2):
$$\text{HMAC} = \text{SHA1}(S_o \| \text{inner}) \quad \text{(64-byte } S_o \text{ + 20-byte inner)}$$

Final HMAC tag: 20 bytes (160 bits).

---

### Example 3: Why Encrypt-then-MAC Defeats Padding Oracle

**Problem**: Explain why MAC-then-Encrypt (MtE) is vulnerable to padding oracle attacks while Encrypt-then-MAC (EtM) is not.

**Setup**: CBC-mode encryption with PKCS#7 padding. Tag = HMAC, appended inside the encrypted block.

**MtE (MAC-then-Encrypt) Attack**:
1. Attacker intercepts ciphertext $C = E(K_1, M \| T)$ where $T = \text{MAC}(K_2, M)$.
2. Receiver **decrypts first**: $M \| T \| \text{padding} = D(K_1, C)$.
3. If padding is invalid: server returns `400 Bad Padding Error`.
4. If padding valid but MAC mismatch: server returns `403 MAC Verification Failed`.
5. **Oracle**: The attacker can distinguish between padding errors and MAC errors. By flipping bits in $C$ block by block, the attacker can determine when padding becomes valid — which reveals the plaintext one byte at a time. (Lucky Thirteen, POODLE — practical attacks against TLS 1.0, 1.1, SSLv3.)

**EtM (Encrypt-then-MAC) Secure Design**:
1. Ciphertext $C = E(K_1, M)$, tag $T = \text{MAC}(K_2, C)$.
2. Receiver **verifies MAC first**: recompute $T' = \text{MAC}(K_2, C)$ and compare $T' == T$ in constant time.
3. If $T' \ne T$: **immediately discard the packet**, return a single generic "Authentication Failed" error.
4. **No decryption is attempted** if the MAC is invalid. The decryption code path is completely bypassed.
5. **No oracle**: the attacker gets identical error responses regardless of padding validity — the decryption oracle is eliminated.

**Constant-time comparison is also critical**: Use `hmac.compare_digest()` (Python), `crypto_verify_32()` (NaCl) — NOT naive `==` which may short-circuit on first mismatched byte and leak timing information about where the mismatch occurs.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q6 — 4 Marks]
**Question**: Compare the strength of MAC and Encryption against brute-force attack.

**Solution**:

| Attribute | Symmetric Encryption | MAC |
|---|---|---|
| **Attacker Goal** | Find key $K$ to decrypt all past and future ciphertexts | Either recover key $K$ OR forge a valid tag $T$ for an arbitrary message $M^*$ |
| **Work to Find Key** | $2^k$ trials (one known plaintext-ciphertext pair suffices to uniquely identify the key) | $2^k$ trials per pair, but $2^{k-m}$ false positives per pair; need $\lceil k/m \rceil$ pairs; total: $2^k \cdot \lceil k/m \rceil$ |
| **Work to Forge Output** | Infeasible without key — guessing $b$-bit ciphertext correctly has probability $2^{-b}$ | Adversary guesses $m$-bit tag; probability $2^{-m}$; expected $2^m$ forgery attempts — NO KEY RECOVERY NEEDED |
| **Governing Security** | Solely key length $k$: $O(2^k)$ | $\min(2^k, 2^m)$ — whichever is smaller governs |
| **Practical Implication** | AES-128 ($k=128$): infeasible with $2^{128}$ work | MAC with 32-bit tag: breakable in $\approx 4 \times 10^9$ guesses regardless of key size |

**Conclusion**: The security of a MAC is governed by $\min(2^k, 2^m)$. Using a short tag (e.g., 32 bits) allows tag forgery with $2^{32}$ online queries — the key length provides no benefit. Minimum recommended tag length: 128 bits.

---

### Question 2 [KTU January 2023, Part A, Q6 — 4 Marks]
**Question**: Explain the different message authentication functions.

**Solution**:

Message authentication functions are the mathematical mechanisms used to generate authenticators that verify both message integrity and sender authenticity. There are three primary categories:

**1. Message Encryption**:
- The ciphertext itself is the authenticator.
- **Symmetric**: $C = E_K(M)$. Receiver decrypts and verifies intelligibility. Both parties must share key $K$.
- **Asymmetric (Digital Signature)**: $S = E_{PR_A}(H(M))$. Any party verifies using $PU_A$. Provides non-repudiation.
- **Limitation**: Does not separate integrity from confidentiality; structured-plaintext requirement is fragile.

**2. Message Authentication Code (MAC)**:
- A function $C(K, M) \to T$ of message and secret key producing a fixed-length tag.
- Transmit $(M \| T)$; receiver recomputes $T' = C(K, M)$ and checks $T' == T$.
- Provides **integrity** (modification changes $T$) and **authenticity** (requires knowledge of $K$).
- Does NOT encrypt $M$ — plaintext is transmitted openly alongside the tag.
- Example: HMAC-SHA256.

**3. Hash Functions (Combined with Secret)**:
- A keyless, public one-way function $H$ producing fixed-length digest $h = H(M)$.
- Hash alone provides integrity only (public — anyone can recompute).
- Authentication requires combining with a secret:
  - $E_K(H(M))$: Encrypt the digest — provides both integrity and authenticity.
  - $E_{PR_A}(H(M))$: Sign the digest — digital signature, provides non-repudiation.
  - HMAC: $H((K \oplus \text{opad}) \| H((K \oplus \text{ipad}) \| M))$ — standardized keyed hash.

---

### Question 3 [KTU June 2022, Part C, Q16(a) — 4 Marks]
**Question**: Explain how MAC can be used to provide authentication only and authentication + confidentiality.

**Solution**:

**Case 1: Authentication Only**:

When confidentiality is not required (public software updates, network routing, broadcast messages):

```
Sender:   Tag = MAC_K(M)         Transmit: (M ‖ Tag)
Receiver: Tag' = MAC_K(M)        Check: Tag' == Tag? [constant-time compare]
```

Security properties:
- ✓ **Integrity**: Any modification to $M$ changes Tag (Tag ≠ Tag').
- ✓ **Authenticity**: Only the holder of $K$ can compute the correct Tag.
- ✗ **Confidentiality**: $M$ is plaintext — anyone can read it.

**Case 2: Authentication and Confidentiality**:

Combine MAC with symmetric encryption. The recommended paradigm is **Encrypt-then-MAC**:

```
Sender:   C = E(K₁, M)           [Encrypt with key K₁]
          T = MAC(K₂, C)          [MAC over CIPHERTEXT with key K₂]
          Transmit: (C ‖ T)

Receiver: T' = MAC(K₂, C)         [Verify MAC first]
          If T' ≠ T: DISCARD → no decryption attempted
          If T' = T: M = D(K₁, C) [Decrypt only if MAC valid]
```

Security advantages of EtM:
- ✓ **Integrity**: Any ciphertext modification changes Tag.
- ✓ **Confidentiality**: $M$ is encrypted.
- ✓ **No padding oracle**: Decryption never happens for invalid-tag packets.
- ✓ **Proven secure**: If either cipher or MAC is secure, the composition is secure.

**Alternative paradigms** (for completeness):

MAC-then-Encrypt (MtE — used by SSL/TLS ≤ 1.2):
```
T = MAC(K₁, M);  C = E(K₂, M ‖ T)
```
Vulnerable to padding oracle attacks — receiver decrypts before verifying MAC.

Encrypt-and-MAC (E&M — used by SSH):
```
C = E(K₁, M);  T = MAC(K₂, M)
```
MAC computed over plaintext may leak information about $M$.
