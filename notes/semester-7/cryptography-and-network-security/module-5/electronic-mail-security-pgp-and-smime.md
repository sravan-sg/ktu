# Electronic Mail Security: Pretty Good Privacy (PGP) and S/MIME

## 1. Explanation
Electronic mail (email) is historically the most widely used network application. However, traditional email protocols (SMTP, POP3, IMAP) transmit messages in plaintext across intermediary mail transfer agents (MTAs) without built-in confidentiality, origin authentication, or integrity checks. Two major protocols were developed to secure email: **Pretty Good Privacy (PGP)** and **Secure/Multipurpose Internet Mail Extensions (S/MIME)**.

### Pretty Good Privacy (PGP)
Created by Philip Zimmermann in 1991, PGP is an open-source, decentralized email security package that provides confidentiality, authentication, data compression, and email compatibility.

#### The Five Core Cryptographic Services in PGP
According to William Stallings (*Cryptography and Network Security*, Chapter 18), PGP provides:
1. **Digital Signature (Authentication & Non-Repudiation)**:
   - Sender generates a SHA-1 message digest of the plaintext.
   - The digest is encrypted with the sender's private key ($PR_A$) using RSA or DSS.
   - The resulting signature is prepended to the message.
2. **Confidentiality (Privacy)**:
   - The message (plus signature if present) is encrypted using a symmetric session key $K_s$ (CAST-128, IDEA, or 3DES).
   - The session key $K_s$ is encrypted with the recipient's public key ($PU_B$) using RSA or ElGamal.
   - The encrypted session key is prepended to the ciphertext.
3. **Compression (ZIP / Deflate Algorithm)**:
   - PGP applies ZIP data compression before encryption.
   - **Why Compression is Done BEFORE Encryption**:
     - *Storage & Bandwidth Savings*: Reduces email size across network links and mailboxes.
     - *Cryptographic Hardening*: Encryption works best on high-entropy data. Natural language text contains significant statistical redundancy. Compressing the plaintext flattens the frequency distribution and eliminates statistical patterns before encryption, significantly strengthening the ciphertext against cryptanalysis. (Note: Encrypting first and then compressing is futile, because strong ciphertext has maximum entropy and cannot be compressed!).
4. **Email Compatibility (Radix-64 / Base64 Conversion)**:
   - Many legacy mail servers and gateways only transmit 7-bit ASCII characters (MIME quoted-printable). Raw binary ciphertext would be corrupted by gateways stripping the 8th bit.
   - PGP maps arbitrary binary streams into 6-bit chunks, encoding each into one of 64 printable ASCII characters (letters, numbers, `+`, `/`), with `=` for padding.
5. **Segmentation and Reassembly**:
   - Automatically splits large messages exceeding size limits into smaller segments that fit within maximum transmission unit (MTU) restrictions, reassembled at the receiver.

```
       PGP Message Generation and Transmission
  Plaintext M ──► [ Hash SHA-1 ] ──► Encrypt with PR_A ──► Signature
       │                                                      │
       └─────────────────────────┬────────────────────────────┘
                                 ▼
                     ( Message || Signature )
                                 │
                                 ▼
                         [ ZIP Compression ]
                                 │
                                 ▼
                  [ Symmetric Encrypt with K_s ]
                                 │
       ┌─────────────────────────┴─────────────────────────┐
       ▼                                                   ▼
   Ciphertext                                    [ Encrypt K_s with PU_B ]
       │                                                   │
       └─────────────────────────┬─────────────────────────┘
                                 ▼
                     ( Encrypted K_s || Ciphertext )
                                 │
                                 ▼
                       [ Radix-64 Conversion ]
                                 │
                                 ▼
                       Transmitted PGP Message
```

#### PGP Key Rings
Every PGP user maintains two local key data structures:
1. **Private Key Ring**: Stores the user's own public/private key pairs, encrypted under a passphrase using symmetric encryption (CAST-128/SHA-1 hash of passphrase).
2. **Public Key Ring**: Stores the public keys of other known communicating correspondents, along with Owner Trust, Key Legitimacy, and Signatures (Web of Trust).

### S/MIME (Secure/Multipurpose Internet Mail Extensions)
S/MIME is an industry-standard security enhancement based on the official MIME specification (RFC 2045-2049, RFC 3850-3852) backed by RSA Security and standardized by the IETF. Unlike PGP's decentralized "Web of Trust", S/MIME relies on a hierarchical Public Key Infrastructure (PKI) with X.509 v3 certificates issued by trusted Certificate Authorities (CAs).

#### The Five MIME Header Fields
To transport non-ASCII and multimedia contents over standard 7-bit SMTP:
1. `MIME-Version`: Identifies the MIME compliance version (e.g., `MIME-Version: 1.0`).
2. `Content-Type`: Describes the data format of the body (e.g., `text/plain`, `multipart/signed`, `application/pkcs7-mime`).
3. `Content-Transfer-Encoding`: Specifies the transformation applied to the body to pass 7-bit mail transports (e.g., `base64`, `7bit`, `quoted-printable`).
4. `Content-ID`: Unique message identifier for cross-referencing between multipart objects.
5. `Content-Description`: Optional human-readable explanation of the content.

#### Four Core S/MIME Functions
1. **Enveloped Data**: Provides confidentiality. Consists of encrypted content of any type and encrypted content-encryption symmetric keys for one or more recipients.
2. **Signed Data**: Provides authentication and integrity. Formed by taking the message digest of the content and encrypting it with the signer's private key. Both the content and signature are encoded using base64.
3. **Clear-Signed Data**: Only the digital signature is encoded. The message body remains readable as standard text for non-MIME-capable mail readers.
4. **Signed and Enveloped Data**: Signed data and enveloped data can be nested so that an encrypted message may be signed, or a signed message may be encrypted.

---

## 2. Example: PGP Radix-64 Conversion
- Radix-64 takes three 8-bit bytes (24 bits) and breaks them into four 6-bit groups (each representing a value from 0 to 63):
  $$\text{Bytes: } \text{"Cat"} = 0x43, 0x61, 0x74 = (01000011 \ 01100001 \ 01110100)_2$$
- Split into four 6-bit values:
  1. $010000_2 = 16 \rightarrow \text{'Q'}$
  2. $110110_2 = 54 \rightarrow \text{'2'}$
  3. $000101_2 = 5 \rightarrow \text{'F'}$
  4. $110100_2 = 52 \rightarrow \text{'0'}$
- Resulting Base64 string: `"Q2F0"`.

---

## 3. Applications & Use Cases
1. **Enterprise Automated Email Encryption**: Corporate Microsoft Outlook environments enforce S/MIME certificates to secure confidential HR, healthcare (HIPAA compliance), and financial communications.
2. **Whistleblower & Investigative Journalism Channels**: Tools like SecureDrop and Tor rely on GnuPG (GPG - the open-source implementation of PGP) to receive leaked documents anonymously and securely.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: PGP Message Reception and Decryption Walkthrough
**Problem**:
Trace the exact mathematical steps performed by Bob upon receiving a transmitted PGP message containing enveloped and signed data.

**Step-by-step Solution**:
1. **Radix-64 Decoding**: Bob's PGP client decodes the ASCII Radix-64 stream into the raw binary packet $(E_{PU_B}(K_s) \parallel C)$.
2. **Recovering Session Key $K_s$**:
   - Bob extracts the encrypted session key block $E_{PU_B}(K_s)$.
   - Bob reads the recipient Key ID to identify which private key to use from his Private Key Ring.
   - Bob decrypts the session key using his private key $PR_B$:
     $$K_s = D(PR_B, E_{PU_B}(K_s))$$
3. **Decrypting the Ciphertext Block**:
   - Bob uses symmetric key $K_s$ with CAST-128 or AES to decrypt ciphertext $C$:
     $$\text{Decompressed Block} = D(K_s, C)$$
4. **Decompression**:
   - The decrypted stream is decompressed via ZIP to yield the original $(M \parallel S_{PR_A})$.
5. **Verifying the Digital Signature**:
   - Bob extracts the signer's Key ID and fetches Alice's public key $PU_A$ from his Public Key Ring.
   - Bob decrypts the signature using Alice's public key:
     $$h = D(PU_A, S_{PR_A})$$
   - Bob independently hashes the extracted plaintext message $M$ using SHA-1:
     $$h' = H(M)$$
   - If $h == h'$, the signature is authenticated, verifying Alice's identity and proving message integrity.

---

### Example 2: MIME Multi-Part Boundary Parsing
**Problem**:
Explain how an S/MIME client delineates and parses a `multipart/signed` email entity.

**Step-by-step Solution**:
- An S/MIME signed email defines a unique boundary string in its `Content-Type` header:
  ```
  Content-Type: multipart/signed; protocol="application/pkcs7-signature";
                micalg=sha-256; boundary="----=_NextPart_001_12345"
  ```
- The body contains two distinct parts separated by `-- ----=_NextPart_001_12345`:
  - Part 1: The original message text or attachment.
  - Part 2: The cryptographic PKCS #7 signature (`application/pkcs7-signature`) encoded in base64.
- An email client without S/MIME displays Part 1 cleanly and displays Part 2 as an unreadable attachment (`smime.p7s`), maintaining backward compatibility.

---

### Example 3: Space Efficiency of Radix-64 Encoding
**Problem**:
Calculate the exact bandwidth overhead introduced when applying Radix-64 encoding to a 1500-byte encrypted email payload.

**Step-by-step Solution**:
1. Radix-64 takes every 3 bytes (24 bits) and converts them into 4 printable ASCII characters (4 bytes = 32 bits).
2. Number of 3-byte blocks: $1500 / 3 = 500$ blocks.
3. Encoded size: $500 \times 4 = 2000$ bytes.
4. Line formatting: RFC 2045 inserts a newline (`\r\n` = 2 bytes) every 76 characters.
   - Number of lines: $\lceil 2000 / 76 \rceil = 27$ lines.
   - Newline overhead: $27 \times 2 = 54$ bytes.
5. Total transmitted size: $2000 + 54 = 2054$ bytes.
6. Overhead: $\frac{2054 - 1500}{1500} \approx 36.9\%$ bandwidth increase.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part D, Q17(a) - 6 Marks]
**Question**: What are the steps used for preparing an enveloped data and signed data in MIME entity?

**Solution**:
In S/MIME, preparing secure email involves standard cryptographic procedures formatted into MIME entities:

1. **Steps for Preparing Enveloped Data (Confidentiality)**:
   Enveloped data consists of encrypted content along with encrypted symmetric keys for one or more recipients:
   - **Step 1: Generate Pseudorandom Session Key**: The sender generates a temporary, pseudorandom symmetric content-encryption key $K_s$ (e.g., AES-128 or Triple-DES).
   - **Step 2: Encrypt Content**: The message content is encrypted using symmetric key $K_s$ in CBC mode.
   - **Step 3: Encrypt Session Key for Each Recipient**: For each intended recipient, the session key $K_s$ is encrypted with that recipient's public key derived from their X.509 certificate ($PU_i$):
     $$E_{PU_i}(K_s)$$
   - **Step 4: Construct `RecipientInfo` Blocks**: A `RecipientInfo` structure is generated for each recipient containing the recipient's certificate issuer/serial number, key encryption algorithm identifier, and the encrypted session key.
   - **Step 5: Package MIME Entity**: The encrypted content, content encryption algorithm identifier, and all `RecipientInfo` blocks are packaged into a single PKCS #7 object, base64 encoded, and tagged with `Content-Type: application/pkcs7-mime; smime-type=enveloped-data`.

2. **Steps for Preparing Signed Data (Integrity and Authentication)**:
   - **Step 1: Compute Message Digest**: The sender calculates a cryptographic hash over the message content using SHA-256 or SHA-1:
     $$h = H(M)$$
   - **Step 2: Generate Digital Signature**: The digest $h$ is encrypted with the sender's private key $PR_A$ using RSA or DSA to generate the signature:
     $$S = E_{PR_A}(h)$$
   - **Step 3: Assemble `SignerInfo` Block**: A `SignerInfo` block is constructed containing the signer's certificate issuer and serial number, the digest algorithm identifier, authenticated attributes (such as signing timestamp), the digital signature $S$, and the signature algorithm identifier.
   - **Step 4: Package MIME Entity**: The original content, the sender's X.509 certificate chain, and the `SignerInfo` block are combined into a PKCS #7 structure, base64 encoded, and wrapped with MIME headers (`multipart/signed` or `application/pkcs7-mime; smime-type=signed-data`).

---

### Question 2 [KTU May 2019, Part D, Q17(b) / January 2023, Part D, Q17(a,b) - 6 Marks]
**Question**: Discuss the message format of PGP and list and explain the services offered by PGP.

**Solution**:
1. **The Message Format of PGP**:
   A complete PGP transmission consists of three concatenated logical packet structures:
```
  ┌──────────────────────────────────────────────────────────────┐
  │                      PGP Message Format                      │
  ├──────────────────────────────────────────────────────────────┤
  │ 1. Key Component:                                            │
  │    - Recipient's Key ID (Least significant 64 bits of PU_B)  │
  │    - Encrypted Session Key: E_{PU_B}(K_s)                    │
  ├──────────────────────────────────────────────────────────────┤
  │ 2. Signature Component (Optional):                           │
  │    - Signer's Key ID (Least significant 64 bits of PR_A)     │
  │    - Leading 2 octets of message digest (for fast checking)  │
  │    - Encrypted Message Digest: E_{PR_A}(H(M))                │
  │    - Timestamp of signing                                    │
  ├──────────────────────────────────────────────────────────────┤
  │ 3. Data Component:                                           │
  │    - Filename and Date/Time stamp                            │
  │    - Plaintext message content M                             │
  └──────────────────────────────────────────────────────────────┘
  (Note: The Signature and Data components are compressed together
   via ZIP and encrypted under symmetric key K_s).
```

2. **Services Offered by PGP**:
   - **Confidentiality**: Provides message privacy by encrypting the message with a one-time symmetric session key $K_s$ (CAST-128, IDEA, AES), which is itself encrypted with the recipient's public key.
   - **Authentication (Digital Signature)**: Guarantees origin authenticity and integrity by signing a SHA-1 hash of the message with the sender's private key.
   - **Compression**: Compresses the message using ZIP prior to encryption to reduce transmission size and eliminate natural language statistical redundancy.
   - **E-mail Compatibility (Radix-64)**: Translates raw binary ciphertext into printable 7-bit ASCII characters (Base64) to prevent corruption across legacy mail gateways.
   - **Segmentation & Reassembly**: Automatically fragments large files exceeding size limits into standard packet segments and reassembles them at destination.

---

### Question 3 [KTU May 2019, Part D, Q19(b) - 2 Marks]
**Question**: Why compression is done before encryption in PGP?

**Solution**:
Compression is performed before encryption in PGP for two critical reasons:
1. **Cryptographic Strengthening (Eliminating Statistical Redundancy)**:
   Natural language text contains high statistical redundancy and non-uniform letter frequencies. Compressing the plaintext flattens the frequency distribution and eliminates repetitive patterns. Encrypting the compressed file makes cryptanalysis (such as frequency analysis and known-plaintext attacks) vastly more difficult.
2. **Infeasibility of Compressing Ciphertext**:
   A strong encryption algorithm produces ciphertext that closely approximates a truly random, high-entropy sequence of bits. A random sequence contains zero redundancy and cannot be compressed by any lossless compression algorithm. Therefore, attempting compression after encryption yields zero space savings.

---

### Question 4 [KTU January 2023, Part A, Q7 - 4 Marks]
**Question**: List and explain the five header fields supported by MIME.

**Solution**:
The Multipurpose Internet Mail Extensions (MIME) standard defines five header fields that extend the traditional RFC 822 email format to support arbitrary binary, multimedia, and international character sets:

1. **`MIME-Version`**:
   - Indicates the version of the MIME standard to which the message conforms.
   - Example: `MIME-Version: 1.0`. Informs the receiving mail user agent (MUA) that the message contains MIME extensions.
2. **`Content-Type`**:
   - Describes the nature of the data in the message body, allowing the receiving MUA to select an appropriate display mechanism or handler.
   - Specified as a `type/subtype` pair with optional parameters.
   - Examples: `text/plain; charset=utf-8`, `image/jpeg`, `multipart/mixed`, `application/pkcs7-mime`.
3. **`Content-Transfer-Encoding`**:
   - Specifies the transformation algorithm used to encode the body into a format safe for 7-bit ASCII SMTP mail transfer agents.
   - Standard values: `base64` (encodes arbitrary binary data into 6-bit ASCII), `quoted-printable` (encodes non-ASCII characters as `=XX`), `7bit`, `8bit`, `binary`.
4. **`Content-ID`**:
   - Provides a unique World-Wide identifier for a specific MIME entity or subpart, allowing body parts to cross-reference each other (e.g., an HTML email referencing an inline embedded image).
   - Formatted identically to the standard `Message-ID` header.
5. **`Content-Description`**:
   - An optional free-text ASCII string providing a human-readable description of an otherwise opaque object (e.g., `Content-Description: Quarterly Financial Spreadsheet in PDF format`).
