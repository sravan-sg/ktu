# Web Security Considerations and SSL / TLS

## 1. Explanation
The World Wide Web is an inherently distributed, client-server system communicating over untrusted public networks. Web servers and web browsers are exposed to a wide variety of security threats ranging from network eavesdropping and session hijacking to server compromise and database theft.

### Web Traffic Security Threats
According to William Stallings (*Cryptography and Network Security*, Chapter 17), web security threats are categorized across four distinct dimensions:
1. **Integrity Threats**: Modification of user data, altering transaction amounts in transit, insertion of malicious JavaScript (Cross-Site Scripting - XSS), or trojanizing web pages.
   - *Countermeasure*: Cryptographic message authentication codes (MACs) and digital signatures.
2. **Confidentiality Threats**: Eavesdropping on credit card numbers, passwords, session tokens, or observing traffic flows.
   - *Countermeasure*: Symmetric encryption (AES) of communication channels.
3. **Authentication Threats**: Impersonation of legitimate users, theft of authentication cookies, phishing, or spoofing DNS domain names.
   - *Countermeasure*: Public-key certificates (X.509) and mutual authentication handshakes.
4. **Availability Threats (Denial of Service - DoS)**: SYN floods, HTTP request flooding, or crashing web servers through memory exhaustion.
   - *Countermeasure*: SYN cookies, rate limiting, and filtering firewalls.

### Placement of Security in the Network Stack
Web security can be applied at three different layers of the TCP/IP protocol hierarchy:
- **Network Layer (IPsec)**: Transparent to all applications; protects all traffic across hosts, but cannot enforce application-specific user privileges.
- **Transport Layer (SSL / TLS)**: Implemented directly above TCP and below Application protocols (HTTP $\rightarrow$ HTTPS, FTP $\rightarrow$ FTPS, SMTP $\rightarrow$ SMTPS). Provides end-to-end transport security, easily integrated into standard browsers without modifying the operating system kernel.
- **Application Layer (S/MIME, PGP, Kerberos, SET)**: Tailored to specific application semantics, but requires custom integration inside every individual application.

```
       Security Placement in the Protocol Stack
  ┌─────────────────────────────────────────────────────────┐
  │ Application Layer : HTTP, FTP, SMTP (Security: SET, PGP)│
  ├─────────────────────────────────────────────────────────┤
  │ Transport Layer   : SSL / TLS (Security: HTTPS)         │
  ├─────────────────────────────────────────────────────────┤
  │ Network Layer     : IP (Security: IPsec)                │
  ├─────────────────────────────────────────────────────────┤
  │ Link / Physical   : Ethernet, Wi-Fi                     │
  └─────────────────────────────────────────────────────────┘
```

### The SSL / TLS Architecture
Originally developed by Netscape as **Secure Sockets Layer (SSL 2.0 and 3.0)** and standardized by the IETF as **Transport Layer Security (TLS 1.0, 1.1, 1.2, 1.3)** (RFC 5246, RFC 8446).
SSL/TLS is not a single protocol; it is a layered framework consisting of four distinct sub-protocols operating in two tiers:

```
  ┌─────────────────────── Upper Layer ────────────────────────┐
  │ SSL Handshake   │ SSL ChangeCipherSpec │ SSL Alert │ HTTP  │
  ├─────────────────┴──────────────────────┴───────────┴───────┤
  │                  SSL Record Protocol                       │
  ├────────────────────────────────────────────────────────────┤
  │                          TCP                               │
  ├────────────────────────────────────────────────────────────┤
  │                           IP                               │
  └────────────────────────────────────────────────────────────┘
```

#### Session State vs. Connection State
- **SSL Session**: An association between a client and a server created by the Handshake Protocol. Sessions define a set of cryptographic parameters (Master Secret, peer certificates, compression method, cipher spec) that can be shared among multiple secure connections to avoid expensive renegotiations.
- **SSL Connection**: A transient, peer-to-peer communications link (a specific TCP connection) carrying data. Every connection belongs to an active session and derives its own read/write encryption and MAC keys from the session's Master Secret.

### The Four SSL/TLS Protocols

#### 1. The SSL Record Protocol
The foundational protocol operating directly on top of TCP. It provides two essential services:
- **Confidentiality**: Encrypts the payload using symmetric keys agreed during the handshake (AES, 3DES).
- **Message Integrity**: Calculates a keyed MAC over the data.

**The Five Operational Steps of the SSL Record Protocol**:
1. **Fragmentation**: The upper-layer application stream is divided into manageable fragments of $2^{14}$ bytes (16,384 bytes = 16 KB) or less.
2. **Compression (Optional)**: Each fragment is compressed using an agreed lossless compression algorithm (typically disabled in modern TLS to defeat CRIME/BREACH compression leakage).
3. **MAC Calculation**: A Message Authentication Code is computed over the compressed fragment using the shared MAC secret key and a 64-bit sequence number:
   $$\text{MAC} = H\Big(\text{MAC\_secret} \parallel \text{pad\_2} \parallel H(\text{MAC\_secret} \parallel \text{pad\_1} \parallel \text{Seq\_Num} \parallel \text{Type} \parallel \text{Length} \parallel \text{Fragment})\Big)$$
   The MAC is appended to the fragment.
4. **Encryption**: The compressed fragment plus MAC is encrypted using the shared symmetric encryption key.
5. **Prepend SSL Record Header**: A 5-byte header is prepended consisting of:
   - `Content Type` (8 bits): Handshake (22), ChangeCipherSpec (20), Alert (21), or Application Data (23).
   - `Major Version` (8 bits): e.g., 3 for SSL 3.0 / TLS.
   - `Minor Version` (8 bits): e.g., 1 for TLS 1.0, 3 for TLS 1.2.
   - `Compressed Length` (16 bits): Length in bytes of the plaintext fragment.

```
       SSL Record Protocol Operation
  Application Data ────────► [ Fragment (≤ 16 KB) ]
                                    │
                                    ▼
                             [ Optional Compression ]
                                    │
                                    ▼
                             [ Append MAC Tag ]
                                    │
                                    ▼
                             [ Symmetric Encryption ]
                                    │
                                    ▼
                             [ Prepend 5-Byte Record Header ]
                                    │
                                    ▼
                             Transmit via TCP
```

#### 2. The SSL Handshake Protocol
Allows the server and client to authenticate each other, negotiate an encryption and MAC algorithm, and establish a shared **Master Secret** before the application protocol transmits any data:
- **Phase 1: Establish Security Capabilities**:
  - `ClientHello`: Client transmits supported TLS version, 32-byte `ClientRandom`, Session ID, and supported Cipher Suites (e.g., `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`).
  - `ServerHello`: Server chooses the TLS version, 32-byte `ServerRandom`, Session ID, and selected Cipher Suite.
- **Phase 2: Server Authentication and Key Exchange**:
  - `Certificate`: Server transmits its X.509 digital certificate chain containing its public key.
  - `ServerKeyExchange` (Optional): Server sends Diffie-Hellman public parameters signed by its private key.
  - `CertificateRequest` (Optional): Sent if mutual authentication is required.
  - `ServerHelloDone`: Indicates the server has completed its hello phase.
- **Phase 3: Client Authentication and Key Exchange**:
  - `Certificate` (Optional): Client sends its certificate if requested.
  - `ClientKeyExchange`: Client sends the 48-byte `Pre-Master Secret` encrypted with the server's public RSA key (or sends ECDH public parameters).
  - `CertificateVerify` (Optional): Client signs a hash of all previous handshake messages with its private key.
- **Phase 4: Finish and Transition to Protected Channel**:
  Both compute the 48-byte **Master Secret**:
  $$\text{Master Secret} = \text{PRF}(\text{Pre-Master Secret}, \text{"master secret"}, \text{ClientRandom} \parallel \text{ServerRandom})$$
  - Client sends `ChangeCipherSpec` (signals transition to newly negotiated cipher parameters).
  - Client sends `Finished` (encrypted message verifying the integrity of the entire handshake).
  - Server sends `ChangeCipherSpec`.
  - Server sends `Finished`.
  Handshake complete! Secure application data transmission begins.

#### 3. ChangeCipherSpec Protocol
Consists of a single message containing a single byte with value `1`. Its purpose is to cause the pending cipher state to be copied into the current cipher state, signaling that all subsequent records will be protected under the newly negotiated cipher spec.

#### 4. Alert Protocol
Transmits session alerts and error notices. Each alert message is 2 bytes:
- Level: `Warning (1)` or `Fatal (2)` (Fatal alerts instantly terminate the connection).
- Description: Specific error code (`unexpected_message`, `bad_record_mac`, `decompression_failure`, `handshake_failure`, `certificate_revoked`, `close_notify`).

---

## 2. Example: Differences between SSL and TLS
| Feature | SSL 3.0 (1996) | TLS 1.0 - 1.2 (RFC 2246, 5246) | TLS 1.3 (RFC 8446 - 2018) |
|---|---|---|---|
| **Standardization** | Proprietary (Netscape) | IETF Standard | Modern IETF Standard |
| **MAC Construction** | Custom keyed hash | Standard HMAC | Authenticated Encryption (AEAD: GCM/ChaCha20) |
| **Key Derivation** | Concatenation of MD5 and SHA-1 | Pseudorandom Function (PRF) based on HMAC | HKDF (HMAC-based Key Derivation Function) |
| **Handshake Latency** | 2 Round Trips (2-RTT) | 2 Round Trips (2-RTT) | 1 Round Trip (1-RTT) or 0-RTT resumption |
| **Obsolete Primitives** | RC4, MD5, DES, CBC mode | Deprecated RC4, MD5 | Completely removes RSA key exchange, CBC, RC4, SHA-1 |

---

## 3. Applications & Use Cases
1. **HTTPS (HTTP over TLS - Port 443)**: Secures electronic banking, ecommerce shopping carts, and private web portal logins against eavesdropping and man-in-the-middle attacks.
2. **Encrypted Database Connectors**: MySQL and PostgreSQL clients establish TLS-encrypted transport tunnels to database clusters, safeguarding SQL queries containing personally identifiable information (PII).

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Master Secret and Key Block Expansion
**Problem**:
In TLS, explain how the 48-byte Master Secret is expanded into the operational keys for encryption and message integrity.

**Step-by-step Solution**:
- The Master Secret is expanded into a continuous stream of key material using the TLS Pseudorandom Function (PRF):
  $$\text{Key Block} = \text{PRF}(\text{Master Secret}, \text{"key expansion"}, \text{ServerRandom} \parallel \text{ClientRandom})$$
- The resulting byte sequence is partitioned sequentially into six operational keys:
  1. `client_write_MAC_key`: Used by client to authenticate outgoing records.
  2. `server_write_MAC_key`: Used by server to authenticate outgoing records.
  3. `client_write_key`: Symmetric key used by client to encrypt data.
  4. `server_write_key`: Symmetric key used by server to encrypt data.
  5. `client_write_IV`: Initialization Vector for client CBC/GCM encryption.
  6. `server_write_IV`: Initialization Vector for server CBC/GCM encryption.

---

### Example 2: SSL Record Header Parsing
**Problem**:
Given an intercepted 5-byte hexadecimal record header `17 03 03 00 30`, decode each field.

**Step-by-step Solution**:
1. Byte 1 = `0x17` ($23_{10}$): Content Type is **Application Data**.
2. Byte 2 = `0x03`: Major Version is **3**.
3. Byte 3 = `0x03`: Minor Version is **3** (Represents **TLS 1.2**).
4. Bytes 4 & 5 = `0x0030` ($48_{10}$): Payload length is **48 bytes**.

---

### Example 3: Handshake Latency Optimization in TLS 1.3
**Problem**:
Calculate the round-trip time (RTT) savings of TLS 1.3 compared to TLS 1.2 during initial session establishment over a 100 ms latency link.

**Step-by-step Solution**:
- **TLS 1.2**: Requires 2 full round-trips (2-RTT) for the handshake before application data can be sent.
  - $2 \times 100\text{ ms} = 200\text{ ms}$ handshake latency.
- **TLS 1.3**: Incorporates Diffie-Hellman key shares directly into the `ClientHello` message, completing the handshake in only 1 round-trip (1-RTT).
  - $1 \times 100\text{ ms} = 100\text{ ms}$ latency.
- **Savings**: $200\text{ ms} - 100\text{ ms} = 100\text{ ms}$ (50% reduction in connection setup delay).

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q9 / January 2023, Part D, Q19(a) - 6 Marks]
**Question**: What are the services provided by Record Layer Protocol for Secure Socket Layer connections? With figure explain the operation of SSL Record Protocol.

**Solution**:
1. **Services Provided by SSL Record Protocol**:
   The SSL Record Protocol provides two fundamental security services for upper-layer application protocols:
   - **Confidentiality**: The entire upper-layer message fragment, along with its MAC tag, is encrypted using a shared symmetric key (AES, 3DES) negotiated during the handshake.
   - **Message Integrity**: The protocol calculates a Message Authentication Code (MAC) using a shared secret MAC key and a 64-bit monotonic sequence number, guaranteeing that records cannot be altered, inserted, deleted, or replayed in transit.

2. **Diagram of SSL Record Protocol Operation**:
```
  Application Data
         │
         ▼
  [ 1. Fragmentation ] ────────► Slices stream into blocks ≤ 16,384 bytes
         │
         ▼
  [ 2. Compression ]   ────────► Optional lossless compression (typically null)
         │
         ▼
  [ 3. Add MAC ]       ────────► Computes keyed MAC using MAC secret & Seq No
         │
         ▼
  [ 4. Encrypt ]       ────────► Symmetric encryption of (Compressed Data || MAC)
         │
         ▼
  [ 5. Prepend Header ] ───────► Adds 5-byte SSL Record Header:
                                 - Content Type (8 bits)
                                 - Major Version (8 bits)
                                 - Minor Version (8 bits)
                                 - Compressed Length (16 bits)
         │
         ▼
     TCP Packet
```

3. **Step-by-Step Execution**:
   - **Step 1 (Fragmentation)**: Divides the application data into blocks of $2^{14}$ bytes (16 KB) or less.
   - **Step 2 (Compression)**: Compresses the fragment without data loss. (In modern TLS, compression is disabled to eliminate side-channel compression attacks).
   - **Step 3 (MAC Generation)**: Computes a message authentication code over the data, the packet sequence number, and the header fields using the shared write MAC secret.
   - **Step 4 (Encryption)**: Encrypts the combined compressed fragment and MAC tag using the symmetric encryption key (AES in CBC or GCM mode).
   - **Step 5 (Header Prepend)**: Formats the final record by adding a 5-byte cleartext header specifying Content-Type, Protocol Version, and Length, then transmits the record over the underlying TCP connection.

---

### Question 2 [KTU June 2022, Part A, Q10 - 4 Marks]
**Question**: Differentiate between SSL and TLS.

**Solution**:

| Comparison Attribute | Secure Sockets Layer (SSL 3.0) | Transport Layer Security (TLS 1.0 - 1.3) |
|---|---|---|
| **Origin & Governance** | Developed privately by Netscape Communications (1996). | Standardized by the Internet Engineering Task Force (IETF) via RFC 2246 (TLS 1.0) and RFC 8446 (TLS 1.3). |
| **Protocol Versioning** | Major version 3, minor version 0 (3.0). | TLS 1.0 is internally version 3.1; TLS 1.2 is 3.3; TLS 1.3 is 3.4. |
| **Message Authentication** | Employs an older custom keyed-hash construction based on concatenation: $H(K \parallel \text{pad}_2 \parallel H(K \parallel \text{pad}_1 \parallel M))$. | Mandates standardized **HMAC** (RFC 2104) in TLS 1.0-1.2, and AEAD authenticated ciphers in TLS 1.3. |
| **Key Derivation** | Derives master secret by hashing with MD5 and SHA-1 in ad-hoc combinations. | Uses a formal Pseudorandom Function (PRF) based on HMAC (TLS 1.2) or HKDF (TLS 1.3). |
| **Alert Error Codes** | Supports a limited set of error codes; does not support `no_certificate` or `record_overflow`. | Defines comprehensive, granular alert codes (`bad_record_mac`, `unrecognized_name`, `unknown_ca`). |
| **Current Security Status** | **Completely Insecure & Deprecated** (vulnerable to POODLE attack; banned across all major browsers). | TLS 1.2 and TLS 1.3 are the current global standards for web security. |

---

### Question 3 [KTU January 2023, Part A, Q9 - 4 Marks]
**Question**: Discuss the various Web security threats.

**Solution**:
Web security threats encompass risks across the communication channel, client browsers, and web servers. They are categorized into four classes:

1. **Integrity Threats**:
   - **Eavesdropper Manipulation**: Unauthorized alteration of user account balances, shopping cart items, or transaction recipient accounts in transit.
   - **Cross-Site Scripting (XSS)**: Injection of malicious scripts into trusted websites that execute in victim browsers to steal session tokens.
   - **SQL Injection (SQLi)**: Subversion of back-end database queries allowing attackers to modify database records.
   - *Countermeasures*: Message Authentication Codes (HMAC), digital signatures, input sanitization.

2. **Confidentiality Threats**:
   - **Eavesdropping / Sniffing**: Interception of plaintext HTTP traffic, credit card numbers, passwords, and sensitive medical/financial data.
   - **Session Hijacking**: Intercepting unencrypted session cookies to impersonate authenticated users.
   - *Countermeasures*: HTTPS (TLS encryption), HSTS (HTTP Strict Transport Security), secure cookie flags.

3. **Authentication Threats**:
   - **Masquerading / Phishing**: Creating fraudulent look-alike websites to deceive users into disclosing passwords and keys.
   - **DNS Spoofing / Cache Poisoning**: Redirecting valid web URLs to malicious servers.
   - *Countermeasures*: X.509 digital certificates with Extended Validation (EV), DNSSEC, mutual certificate authentication.

4. **Availability (Denial of Service - DoS) Threats**:
   - **TCP SYN Floods**: Exhausting web server connection queues by initiating incomplete TCP handshakes.
   - **DDoS Attacks**: Flooding server bandwidth with millions of requests from distributed botnets.
   - *Countermeasures*: SYN cookies, content delivery networks (CDNs), intrusion prevention systems, rate limiting firewalls.
