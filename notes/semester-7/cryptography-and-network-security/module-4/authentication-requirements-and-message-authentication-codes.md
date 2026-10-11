# Authentication Requirements and Message Authentication Codes (MAC)

## 1. Explanation
In network and computer security, **message authentication** is a mechanism or service that verifies the integrity of transmitted data (confirming that data has not been modified, inserted, deleted, or replayed) and confirms the authentic identity of the sender.

### Security Threats in Communication
According to William Stallings (*Cryptography and Network Security*, Chapter 11 & 12), unauthenticated communication channels face seven major security attacks:
1. **Disclosure**: Release of message contents to unauthorized interceptors (attack on confidentiality).
2. **Traffic Analysis**: Discovery of transmission patterns, communication frequency, and network identities.
3. **Masquerade (Impersonation)**: An attacker injects false messages purporting to originate from an authorized entity.
4. **Content Modification**: Alteration, insertion, or deletion of portions of a valid message.
5. **Sequence Modification**: Insertion, deletion, or reordering of a sequence of messages.
6. **Timing Modification**: Replay of valid messages or delaying message delivery.
7. **Repudiation**: Denial of receipt by receiver or denial of transmission by sender.

Authentication addresses attacks 3 through 6, while digital signatures address attack 7.

### Authentication Functions
Message authentication mechanisms rely on three classes of mathematical functions:
1. **Message Encryption**: The ciphertext itself acts as an authenticator.
   - *Symmetric Encryption*: Only the sender and recipient possess the shared secret key $K$. The fact that the receiver successfully decrypts ciphertext into intelligible plaintext verifies that it must have come from the sender and was not altered in transit.
   - *Public-Key Encryption*: Encrypting a message with the sender's private key $PR_A$ provides authentication and digital signature, as only the sender possesses $PR_A$.
2. **Message Authentication Code (MAC)**: A small, fixed-length block of authentication data (also known as a cryptographic checksum) generated using a secret key $K$ and appended to the message:
   $$\text{MAC} = C(K, M)$$
   The message $M$ is transmitted in plaintext alongside the MAC: $(M \parallel \text{MAC})$.
3. **Cryptographic Hash Function**: A public mathematical function $H$ that maps a variable-length message $M$ into a fixed-length hash value (digest) $h = H(M)$ without using a secret key. Authentication is achieved by encrypting the digest or combining it with a shared secret.

```
       Message Authentication Code (MAC) Flow
  Sender (Key K)                               Receiver (Key K)
  Message M ────────────────── Message M ────────────► Message M
      │                                                     │
      ▼                                                     ▼
  [ MAC C(K, M) ] ──────────── Tag MAC ──────────────► [ MAC C(K, M) ]
                                                            │
                                                            ▼
                                                    Check Tag == MAC?
                                                    (Accept if match)
```

### Message Authentication Codes (MAC) Architecture
A MAC function takes a variable-length message $M$ and a secret symmetric key $K$, and outputs a fixed-length authentication tag:
$$\text{Tag} = \text{MAC}_K(M)$$
- **Verification**: The recipient, possessing the identical shared key $K$, recalculates the MAC over the received message $M$ and compares it bit-for-bit with the received tag. If they match:
  1. The receiver is assured that the message was not altered (Integrity).
  2. The receiver is assured that the sender possesses the shared secret key $K$ (Authenticity).
  3. If sequence numbers are included in $M$, proper sequence is assured (Anti-replay).

#### MAC for Authentication and Confidentiality
A MAC can be combined with symmetric encryption to provide both message authenticity and confidentiality. Three main paradigms exist:
1. **Encrypt-and-MAC**: $C = E(K_1, M)$ and $T = \text{MAC}(K_2, M)$. Transmit $(C \parallel T)$ (Used in SSH).
2. **MAC-then-Encrypt**: $T = \text{MAC}(K_1, M)$ and $C = E(K_2, M \parallel T)$. Transmit $C$ (Used in SSL/TLS).
3. **Encrypt-then-MAC**: $C = E(K_1, M)$ and $T = \text{MAC}(K_2, C)$. Transmit $(C \parallel T)$ (Used in IPsec, cryptographically most robust).

### HMAC (Hash-Based Message Authentication Code)
Standardized in RFC 2104 and FIPS PUB 198, HMAC constructs a secure MAC by wrapping an existing cryptographic hash function (such as SHA-256 or SHA-1) with a secret key $K$ without modifying the underlying compression function.

#### Mathematical Construction of HMAC
$$\text{HMAC}_K(M) = H\Big((K^+ \oplus \text{opad}) \parallel H\big((K^+ \oplus \text{ipad}) \parallel M\big)\Big)$$
- **Parameters**:
  - $H$: Underlying hash function (e.g., SHA-1, SHA-256).
  - $B$: Block length of the hash function (for SHA-1/MD5/SHA-256, $B = 64$ bytes = 512 bits).
  - $L$: Output hash length (for SHA-1, $L = 20$ bytes; for SHA-256, $L = 32$ bytes).
  - $K$: Shared secret key.
  - $K^+$: Secret key padded to length $B$ bytes by appending zeros if key length $< B$ (or hashed if length $> B$).
  - $\text{ipad}$ (inner pad): A fixed constant byte `0x36` repeated $B$ times (`0x3636...36`).
  - $\text{opad}$ (outer pad): A fixed constant byte `0x5C` repeated $B$ times (`0x5C5C...5C`).

#### Why HMAC is Secure
1. **Length Extension Resistance**: Simple keyed hashes of the form $H(K \parallel M)$ are vulnerable to **length extension attacks** in Merkle-Damgård hash functions. An attacker can append arbitrary data $M'$ and compute $H(K \parallel M \parallel M')$ from the known hash output without knowing $K$. The nested two-pass hashing of HMAC completely defeats length extension attacks.
2. **Speed & Portability**: Reuses optimized software/hardware hash libraries with zero modifications.

---

## 2. Example: HMAC Inner and Outer Hashing Flow
```
        Secret Key K
             │
             ▼
      [ Pad to B bits: K^+ ]
             │
      ┌──────┴──────┐
      ▼             ▼
  (XOR ipad)    (XOR opad)
      │             │
      ▼             │
   S_i (B bits)     │
      │             │
      ▼             │
 [ Append M ]       │
      │             │
      ▼             │
[ Hash H (Pass 1) ] │
      │             │
      ▼             ▼
  h_1 (L bits)   S_o (B bits)
      │             │
      └──────┬──────┘
             ▼
        [ Append ]
             │
             ▼
      [ Hash H (Pass 2) ]
             │
             ▼
         HMAC Tag
```

---

## 3. Applications & Use Cases
1. **API Authentication (Amazon AWS & GitHub REST APIs)**: Web APIs verify incoming client HTTP requests using HMAC-SHA256 signatures passed inside HTTP `Authorization` headers.
2. **JSON Web Tokens (JWT)**: Secure identity assertions in Single Sign-On (SSO) systems using `HS256` (HMAC with SHA-256) to sign claims and user payloads.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Brute-Force Work Factor Comparison: MAC vs. Encryption [KTU May 2019]
**Problem**:
Compare the theoretical and practical strength of a Message Authentication Code (MAC) against brute-force attacks compared to conventional Symmetric Encryption.

**Step-by-step Solution**:
1. **Brute-Force Key Search on Symmetric Encryption**:
   - Given an encryption scheme with key length $k$ bits and ciphertext $C = E_K(P)$.
   - An attacker tests candidate keys $K_i$.
   - Because plaintext $P$ has recognizable structure (e.g., ASCII text, recognizable header bytes), checking whether $D(K_i, C)$ yields intelligible plaintext requires only **1 or 2 known plaintext-ciphertext blocks**.
   - Complexity: $2^k$ operations to find the single unique key $K$.
2. **Brute-Force Attack on a MAC**:
   - Let MAC key length be $k$ bits and MAC tag length be $m$ bits: $\text{Tag} = C(K, M)$.
   - An attacker wants to find $K$ or forge a valid MAC for a modified message $M^*$.
   - **Case A: Finding the Key $K$**:
     - For a given $(M_1, T_1)$, an attacker tests all $2^k$ keys.
     - On average, $2^{k-m}$ keys will produce the matching tag $T_1$ purely by coincidence!
     - To isolate the unique true key, the attacker needs $\lceil k/m \rceil$ independent message-tag pairs.
     - Total effort: $2^k \cdot \lceil k/m \rceil$ operations.
   - **Case B: Forging a Tag without Finding the Key**:
     - The attacker randomly guesses an $m$-bit tag for message $M^*$.
     - The probability of a successful forgery on any given trial is $2^{-m}$.
     - Expected trials required: $2^m$.
   - **Conclusion**:
     - While encryption strength is dictated solely by key length $k$ ($2^k$), MAC strength is dictated by $\min(2^k, 2^m)$.
     - If $m \ll k$ (e.g., a 32-bit tag with a 128-bit key), an attacker can forge a tag with only $2^{32}$ trials without ever recovering the key! Hence, standard MACs use tags $\ge 96$ to $128$ bits.

---

### Example 2: HMAC-SHA1 Padding and Intermediate State Calculation
**Problem**:
Given a 160-bit key $K$, show the step-by-step preparation of $K^+$, $S_i$, and $S_o$ for HMAC-SHA1.

**Step-by-step Solution**:
1. For SHA-1, block size $B = 64$ bytes (512 bits) and digest length $L = 20$ bytes (160 bits).
2. Key length is 160 bits = 20 bytes.
   Since length $< B$ (20 bytes $< 64$ bytes), pad key $K$ with 44 zero bytes:
   $$K^+ = K \parallel 0x0000\dots00 \quad (64 \text{ bytes})$$
3. Compute inner key block $S_i$:
   $$S_i = K^+ \oplus \text{ipad}$$
   where $\text{ipad}$ is 64 bytes of `0x36`.
   - First 20 bytes: $K_i \oplus 0x36$.
   - Remaining 44 bytes: $0x00 \oplus 0x36 = 0x36$.
4. Compute outer key block $S_o$:
   $$S_o = K^+ \oplus \text{opad}$$
   where $\text{opad}$ is 64 bytes of `0x5C`.
   - First 20 bytes: $K_i \oplus 0x5C$.
   - Remaining 44 bytes: $0x00 \oplus 0x5C = 0x5C$.

---

### Example 3: Authentication and Confidentiality Modes Comparison
**Problem**:
State why the "Encrypt-then-MAC" paradigm is cryptographically superior to "MAC-then-Encrypt" and "Encrypt-and-MAC".

**Step-by-step Solution**:
- In **MAC-then-Encrypt** (used in SSL 3.0 / TLS 1.0):
  The receiver must decrypt the ciphertext before it can verify the MAC tag. If the ciphertext has been modified in transit, decryption produces corrupted plaintext or invalid padding. This enabled fatal **Padding Oracle attacks** (such as the POODLE and Lucky Thirteen attacks), where attackers inferred plaintext bytes from decryption timing errors.
- In **Encrypt-then-MAC** (used in IPsec and modern TLS 1.3 AEAD):
  The MAC is computed directly over the ciphertext. Upon receiving a packet, the recipient validates the MAC tag *before* running any decryption operations. If the tag is invalid, the packet is instantly dropped, completely eliminating padding oracle side channels!

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q6 - 4 Marks]
**Question**: Compare the strength of MAC and Encryption against brute-force attack.

**Solution**:
A brute-force attack against an encryption scheme differs substantially in mechanics, requirements, and work factor from a brute-force attack against a Message Authentication Code (MAC):

| Comparative Attribute | Conventional Encryption Scheme | Message Authentication Code (MAC) |
|---|---|---|
| **Goal of Brute-Force** | Find the secret key $K$ to decrypt all past and future ciphertexts. | Either (1) discover secret key $K$, OR (2) forge a valid authentication tag for an arbitrary message without knowing $K$. |
| **Effort to Recover Key** | Requires trying candidate keys against a single known $(P, C)$ block. Work factor is $2^k$ (where $k$ is key size). The correct key is recognized immediately by checking plaintext formatting. | Finding the key requires testing candidate keys against multiple pairs $(M_i, T_i)$. Because tag length $m < k$, testing one pair yields $2^{k-m}$ candidate keys. At least $\lceil k/m \rceil$ message-tag pairs are needed to isolate $K$. Work factor is $2^k \cdot \lceil k/m \rceil$. |
| **Effort to Forge Valid Output** | Infeasible without the key. Guessing a full 64-bit or 128-bit ciphertext corresponding to desired plaintext has negligible probability $2^{-b}$. | An adversary does **not** need to find the key to compromise integrity. They can generate a random $m$-bit tag for message $M^*$. The probability of an unauthorized message passing validation is $2^{-m}$, requiring on average $2^m$ forgery attempts. |
| **Governing Parameter** | Determined strictly by **Key Length $k$** ($2^k$). | Governed by $\min(2^k, 2^m)$. If the MAC tag length $m$ is small (e.g., 32 or 48 bits), the MAC can be broken by online tag guessing long before the key space ($2^k$) is exhausted. |

---

### Question 2 [KTU January 2023, Part A, Q6 - 4 Marks]
**Question**: Explain the different message authentication functions.

**Solution**:
Message authentication functions are mathematical mechanisms used to generate authenticators that verify message integrity and sender identity. They fall into three primary categories:

1. **Message Encryption (Symmetric & Asymmetric)**:
   - The ciphertext itself serves as the authenticator.
   - **Symmetric Encryption**: When a sender encrypts message $M$ using shared secret key $K$ ($C = E_K(M)$), the recipient's successful decryption to intelligible plaintext proves that only the authentic peer possessing $K$ could have created the message, and that it was not modified.
   - **Asymmetric Encryption**: The sender encrypts $M$ with their private key $PR_A$ ($C = E_{PR_A}(M)$). Any entity can verify it using public key $PU_A$, confirming origin and providing non-repudiation.

2. **Message Authentication Code (MAC)**:
   - A public function parameterised by a shared secret key $K$ that takes a variable-length message $M$ and produces a fixed-length authentication code:
     $$\text{Tag} = C(K, M)$$
   - The message is sent together with the tag: $(M \parallel \text{Tag})$.
   - The recipient re-computes the code using shared key $K$ and compares it to the received tag. Provides integrity and endpoint authentication without requiring confidentiality.

3. **Cryptographic Hash Functions**:
   - A public, keyless one-way function $H$ that maps a message of arbitrary length to a fixed-length message digest $h = H(M)$.
   - Hash functions alone do not provide authentication (an attacker can alter $M$ and recompute $H(M)$). Authentication is achieved by combining the hash with a secret:
     - Encrypting the hash value with symmetric key: $E_K(H(M))$.
     - Encrypting the hash value with sender's private key: $E_{PR_A}(H(M))$ (Digital Signature).
     - Incorporating a shared secret into the hash input (e.g., HMAC: $H(K \parallel H(K \parallel M))$).

---

### Question 3 [KTU June 2022, Part C, Q16(a) - 4 Marks]
**Question**: Explain how MAC can be used to provide authentication only and authentication and confidentiality.

**Solution**:
1. **Providing Authentication Only**:
   - When confidentiality is not required (e.g., broadcast messages, public software distribution, network routing updates, or when performance is critical), the message $M$ is transmitted in plaintext alongside the MAC tag.
   - **Sender**: Computes $\text{Tag} = \text{MAC}_K(M)$ and transmits:
     $$\text{Packet} = M \parallel \text{MAC}_K(M)$$
   - **Receiver**: Extracts $M$, calculates $\text{MAC}_K(M)$ using shared key $K$, and verifies equality with the received tag.
   - **Security Properties**:
     - Guarantees message integrity (any modification to $M$ causes tag mismatch).
     - Guarantees sender authenticity (only the holder of $K$ could generate the tag).
     - Zero confidentiality (anyone intercepting the channel can read $M$).

2. **Providing Authentication and Confidentiality**:
   To achieve both secrecy and integrity, the MAC is coupled with a symmetric encryption algorithm. There are three approaches:
   - **Approach 1: MAC-then-Encrypt (Used in SSL/TLS)**:
     - Sender computes tag $T = \text{MAC}_{K_1}(M)$.
     - Sender encrypts concatenated plaintext and tag using encryption key $K_2$:
       $$C = E_{K_2}(M \parallel T)$$
     - Receiver decrypts $C$ to recover $M \parallel T$, then recalculates the MAC over $M$ and verifies against $T$.
   - **Approach 2: Encrypt-then-MAC (Used in IPsec, standard in modern cryptography)**:
     - Sender encrypts message: $C = E_{K_1}(M)$.
     - Sender computes MAC over the ciphertext: $T = \text{MAC}_{K_2}(C)$.
     - Transmits: $C \parallel T$.
     - Receiver checks tag $T$ over $C$ *before* decryption. If the tag is invalid, the packet is immediately dropped, defending against chosen-ciphertext and padding oracle attacks.
