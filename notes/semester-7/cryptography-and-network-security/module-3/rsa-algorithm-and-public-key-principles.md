# RSA Algorithm and Public Key Cryptography Principles

## 1. Explanation

### 1.1 The Revolution of Public-Key Cryptography — Deep Intuition

Before 1976, every cryptographic system in history required a **shared secret** to be exchanged before any secure communication could begin. This created an insurmountable bootstrapping problem: *to communicate securely, you already needed a secure channel*. For militaries and governments with couriers and secure facilities, this was manageable. For internet-scale communication between strangers, it was impossible.

**Whitfield Diffie and Martin Hellman** (1976) solved this with a radical insight: mathematically, it is possible to build **pairs of keys** where knowledge of one (the public key) does not compromise the other (the private key), even though the two keys are mathematically related. This means anyone can **lock** a message for you (using your public key), but only you can **unlock** it (using your private key) — and you never have to share your private key with anyone.

**Ron Rivest, Adi Shamir, and Leonard Adleman** (1977) made this concrete with RSA — a specific, practical public-key cryptosystem based on the computational hardness of integer factorization.

---

### 1.2 Principles of Public-Key Cryptosystems

A public-key cryptosystem uses an **asymmetric key pair** $(PU, PR)$:
- **Public Key $PU$**: Derived mathematically from the private key. Disseminated openly; can be published in directories, embedded in certificates, sent over insecure channels.
- **Private Key $PR$**: Generated first; never shared. All security rests on keeping this secret.

The fundamental relationship: $D(PR, E(PU, M)) = M$ and $D(PU, E(PR, M)) = M$.

**Five Essential Requirements for Public-Key Cryptosystems** (Stallings §9.1):

1. It must be computationally easy for a party B to generate the pair $(PU_B, PR_B)$.
2. It must be computationally easy for sender A to compute ciphertext $C = E(PU_B, M)$.
3. It must be computationally easy for receiver B to decrypt $M = D(PR_B, C)$.
4. It must be computationally infeasible for an adversary knowing $PU_B$ to determine $PR_B$.
5. It must be computationally infeasible for an adversary knowing $PU_B$ and ciphertext $C$ to recover $M$.

An optional sixth requirement enables digital signatures: it must be computationally feasible to apply $E$ and $D$ in either order: $D(PU, E(PR, M)) = M$.

#### Dual Operational Modes

```
MODE 1: CONFIDENTIALITY (Encryption)
─────────────────────────────────────
Alice sends private message M to Bob:
  Encrypt: C = E(PU_Bob, M)    [Alice uses Bob's PUBLIC key]
  Decrypt: M = D(PR_Bob, C)    [Bob uses his own PRIVATE key]

Only Bob (the private key holder) can decrypt. Even Alice cannot 
re-decrypt after sending!

MODE 2: AUTHENTICATION (Digital Signature)
──────────────────────────────────────────
Alice proves she sent message M (non-repudiation):
  Sign:   S = E(PR_Alice, H(M))   [Alice uses her own PRIVATE key]
  Verify: H(M) = D(PU_Alice, S)   [Anyone uses Alice's PUBLIC key]

Anyone can verify the signature. Only Alice could have created it
because only she holds PR_Alice.
```

**Combined Mode (Confidentiality + Authentication)**:
```
  S = E(PR_Alice, H(M))           [Sign: proves origin]
  C = E(PU_Bob, M || S)           [Encrypt: ensures confidentiality]
  Transmit C to Bob
  Bob: M || S = D(PR_Bob, C)      [Decrypt]
  Bob: Verify D(PU_Alice, S) == H(M)  [Verify signature]
```

#### One-Way Trapdoor Functions

Public-key schemes are built on **one-way trapdoor functions** $f$ satisfying:
1. **Easy forward**: Given $x$, compute $y = f(x)$ efficiently.
2. **Hard inverse**: Given $y$, recover $x = f^{-1}(y)$ is computationally infeasible without special "trapdoor" information $k$.
3. **Easy inverse with trapdoor**: Given $y$ and $k$, compute $x = f^{-1}(y, k)$ efficiently.

| Scheme | One-Way Function | Trapdoor |
|---|---|---|
| **RSA** | $f(M) = M^e \bmod n$ | Prime factorization of $n = pq$ |
| **Diffie-Hellman** | $f(x) = g^x \bmod p$ | Discrete logarithm $x$ |
| **ECC** | $f(k) = k \cdot G$ (point multiplication) | Scalar $k$ (ECDLP) |

---

### 1.3 The RSA Algorithm — Full Technical Specification

RSA is a **block cipher** where plaintext and ciphertext are integers in $\{0, 1, \dots, n-1\}$.

#### 1.3.1 Key Generation

| Step | Operation | Explanation |
|---|---|---|
| 1 | Select large distinct primes $p, q$ | Each typically 1024 bits for a 2048-bit RSA key. Use Miller-Rabin primality test. |
| 2 | Compute $n = p \cdot q$ | The **RSA modulus**. Made public. Security depends on difficulty of factoring $n$. |
| 3 | Compute $\phi(n) = (p-1)(q-1)$ | The Euler totient — the exponent group size. **Kept secret**. |
| 4 | Choose $e$ with $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$ | **Public exponent**. Common choices: $e = 3$ (fast encryption, risky), $e = 65537 = 2^{16}+1$ (standard). |
| 5 | Compute $d = e^{-1} \bmod \phi(n)$ | **Private exponent**. Computed via Extended Euclidean Algorithm. |
| 6 | **Public Key**: $PU = \{e, n\}$ | Published. Used for encryption and signature verification. |
| 7 | **Private Key**: $PR = \{d, n\}$ | Secret. $p, q, \phi(n)$ are also destroyed after key generation. |

#### 1.3.2 Encryption

Given plaintext $M$ where $0 \le M < n$:
$$\boxed{C = M^e \bmod n}$$

#### 1.3.3 Decryption

Given ciphertext $C$:
$$\boxed{M = C^d \bmod n}$$

**Fast Modular Exponentiation** (Square-and-Multiply):
To compute $M^e \bmod n$ efficiently, expand $e$ in binary and apply repeated squaring:
```
Result = 1
For each bit b of e from MSB to LSB:
    Result = Result² mod n
    If b == 1: Result = Result × M mod n
```
Complexity: $O(\log e)$ multiplications. For $e = 65537 = 10000000000000001_2$: only 17 squarings + 2 multiplications.

---

### 1.4 Mathematical Proof of RSA Correctness

**Theorem**: For all $M$ with $0 \le M < n$, $C^d \equiv M \pmod n$, where $C = M^e \bmod n$.

**Proof**:

Since $ed \equiv 1 \pmod{\phi(n)}$, there exists integer $k \ge 1$ such that:
$$ed = k\phi(n) + 1 = k(p-1)(q-1) + 1$$

We prove $M^{ed} \equiv M \pmod p$ (and by symmetry, $\pmod q$), then combine using CRT.

**Case 1: $\gcd(M, p) = 1$ (M is not a multiple of p)**:

By Fermat's Little Theorem: $M^{p-1} \equiv 1 \pmod p$.

$$M^{ed} = M^{k(p-1)(q-1)+1} = \left(M^{p-1}\right)^{k(q-1)} \cdot M \equiv 1^{k(q-1)} \cdot M \equiv M \pmod p$$

**Case 2: $p \mid M$ (M is a multiple of p)**:

Then $M \equiv 0 \pmod p$, so $M^{ed} \equiv 0 \equiv M \pmod p$.

In both cases: $M^{ed} \equiv M \pmod p$.

By identical reasoning (swapping $p$ and $q$): $M^{ed} \equiv M \pmod q$.

Since $p$ and $q$ are **distinct primes** and $M^{ed} \equiv M$ for both, the **Chinese Remainder Theorem** gives:
$$M^{ed} \equiv M \pmod{pq} \equiv M \pmod n \quad \square$$

---

### 1.5 Security Analysis of RSA

#### 1.5.1 Factorization Attack (Primary Security Threat)

If an adversary factors $n = pq$, they immediately compute $\phi(n) = (p-1)(q-1)$ and then $d = e^{-1} \bmod \phi(n)$ using the Extended Euclidean Algorithm. The entire private key is recovered.

**RSA modulus size requirements** (NIST 2020):
| Security Level | RSA Modulus Size | Equivalent ECC | Symmetric (AES) |
|---|---|---|---|
| 80-bit | 1024 bits (deprecated) | 160-bit | AES-80 |
| 112-bit | 2048 bits (minimum) | 224-bit | AES-112 |
| 128-bit | 3072 bits (recommended) | 256-bit | AES-128 |
| 192-bit | 7680 bits | 384-bit | AES-192 |
| 256-bit | 15360 bits | 521-bit | AES-256 |

Best known factoring algorithm (General Number Field Sieve) for 2048-bit: estimated $2^{112}$ operations.

#### 1.5.2 Mathematical Equivalence Attacks

Computing $\phi(n)$ directly without factoring $n$ is **computationally equivalent** to factoring $n$. Similarly, finding $d$ from $e$ and $n$ without knowing $\phi(n)$ is also equivalent to factoring.

#### 1.5.3 Small Encryption Exponent Attacks

Using $e = 3$ introduces vulnerabilities:
- **Coppersmith's attack**: If $M^3 < n$ (e.g., very short messages), $C = M^3$ in plain integers, and cube-root recovery gives $M$ directly.
- **Broadcast attack**: If the same message $M$ is sent to 3 different parties with $e_1 = e_2 = e_3 = 3$, the attacker obtains $C_1, C_2, C_3$ and applies CRT to recover $M^3$ (which is exactly $M^3$ since $M^3 < n_1 n_2 n_3$), then extracts $M$ via integer cube root.

**Mitigation**: Use $e = 65537$ and always pad messages before encryption.

#### 1.5.4 Timing Attacks

By measuring the precise time taken to decrypt ciphertexts, an attacker can recover bits of $d$ (Kocher, 1996). **Countermeasure**: Blinding — multiply ciphertext by a random value $r^e \bmod n$ before decryption, then divide the result by $r$.

#### 1.5.5 Chosen-Ciphertext Attacks and RSA-OAEP

**Textbook RSA** (raw $M^e \bmod n$) is **deterministic** and **malleable**:
- Deterministic: Same message always produces same ciphertext → enables dictionary attacks.
- Malleable: If $C = M^e \bmod n$, then $2^e C \bmod n = (2M)^e \bmod n$ — an attacker can systematically modify ciphertexts without knowing the plaintext.

**RSA-OAEP** (Optimal Asymmetric Encryption Padding, PKCS#1 v2.1, RFC 8017):
- Pads message with random data before encryption: $C = (M \| r \| \text{hash})^e \bmod n$.
- Randomized: Same message encrypted twice gives different ciphertexts.
- Proven secure against adaptive chosen-ciphertext attacks (IND-CCA2) in the random oracle model.
- Used in all modern TLS and PGP implementations.

#### 1.5.6 Quantum Computing Threat

**Shor's Algorithm** (1994) can factor $n = pq$ in polynomial time $O((\log n)^3)$ on a quantum computer. RSA is therefore **quantum-vulnerable**. NIST's Post-Quantum Cryptography (PQC) standardization process (2016–2024) selected lattice-based algorithms (CRYSTALS-Kyber, CRYSTALS-Dilithium) and hash-based signatures (SPHINCS+) as quantum-resistant replacements.

---

### 1.6 Comparison: Symmetric vs. Public-Key Cryptosystems

| Attribute | Symmetric (Conventional) | Public-Key (Asymmetric) |
|---|---|---|
| **Keys** | Single shared secret key | Key pair: public + private |
| **Key distribution** | Requires secure pre-shared channel; $O(N^2)$ keys for $N$ users | Public key published openly; $O(N)$ key pairs total |
| **Speed** | Very fast (AES: ~10 GB/s in hardware) | Slow (RSA-2048: ~10 KB/s for decryption in software) |
| **Key size** | 128–256 bits | 2048–4096 bits |
| **Basis** | S-boxes, permutations, XOR | Number-theoretic one-way trapdoor functions |
| **Digital signatures** | Not naturally supported | Core feature |
| **Non-repudiation** | Cannot provide (both parties share key) | Inherent — private key is unique to signer |
| **Typical use** | Bulk data encryption (AES-GCM, AES-CBC) | Key exchange, signatures, authentication |
| **Hybrid systems** | Used together: RSA/DH for key exchange, AES for data | Combined in TLS, PGP, IPsec, Signal Protocol |

> **Real-world practice**: Public-key cryptography is 1000–10,000 times slower than symmetric encryption. In practice, RSA is used only to **encrypt the symmetric session key** (a.k.a. key encapsulation), and then AES encrypts the actual data. This is the design of TLS, PGP, and Signal.

---

## 2. Example: Small-Scale RSA Full Demonstration

**Setup**: $p = 5$, $q = 11$.

| Step | Computation | Result |
|---|---|---|
| Modulus | $n = 5 \times 11$ | $n = 55$ |
| Totient | $\phi(n) = (5-1)(11-1)$ | $\phi(n) = 40$ |
| Choose $e$ | $\gcd(3, 40) = 1$ | $e = 3$ |
| Private key | $3d \equiv 1 \pmod{40}$: $40 = 13 \times 3 + 1 \implies 1 = 40 - 13 \times 3 \implies d = -13 \equiv 27 \pmod{40}$ | $d = 27$ |
| Public key | $\{e=3, n=55\}$ | |
| Private key | $\{d=27, n=55\}$ | |

**Encrypt** $M = 9$:
$$C = 9^3 \bmod 55 = 729 \bmod 55 = 729 - 13 \times 55 = 729 - 715 = 14$$

**Decrypt** $C = 14$:
$$M = 14^{27} \bmod 55$$

Using CRT: $14 \bmod 5 = 4$, $14 \bmod 11 = 3$.
- $\pmod 5$: $4^{27} = 4^{4 \times 6 + 3} = (4^4)^6 \times 4^3 \equiv 1^6 \times 64 \equiv 4 \pmod 5$
- $\pmod{11}$: $3^{27} = 3^{10 \times 2 + 7} = (3^{10})^2 \times 3^7 \equiv 1^2 \times 2187 \equiv 2187 \bmod 11$. $2187 = 198 \times 11 + 9 \implies \equiv 9 \pmod{11}$

CRT: $M \equiv 4 \pmod 5$ and $M \equiv 9 \pmod{11}$. Try $M = 11k + 9$: For $k=0: 9 \bmod 5 = 4$ ✓. **$M = 9$** ✓

---

## 3. Applications & Use Cases

1. **TLS/HTTPS Server Certificates**: RSA-2048 or RSA-4096 digital certificates sign the server's public key and domain name. Every HTTPS connection verifies this signature to prevent MITM attacks. X.509 certificate chains use RSA for root CA trust.

2. **SSH Authentication**: RSA key pairs authenticate system administrators. The client signs a session challenge with the private key; the server verifies with the stored public key. Eliminates password transmission entirely.

3. **PGP Email Encryption**: RSA encrypts the AES session key that encrypts the email body. RSA signs the message digest to provide non-repudiation. GNU Privacy Guard (GPG) supports RSA-4096.

4. **Digital Certificates and PKI**: Certificate Authorities (CAs like DigiCert, Let's Encrypt) issue RSA-signed X.509 certificates binding domain names to public keys. Browsers ship with ~150 root CA certificates pre-installed as trust anchors.

5. **Smart Cards and Hardware Security Modules**: RSA signing runs on hardware-isolated chips (TPM, Yubikey, SIM card). The private key never leaves the secure enclave — even the host OS cannot access it.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Full RSA Cryptanalysis [KTU May 2019, Part A, Q5]

**Problem**: Intercepted ciphertext $C = 8$. Public key: $e = 13$, $n = 33$. Find plaintext $M$.

**Step 1 — Factor $n = 33$**:
$$33 = 3 \times 11 \implies p = 3,\ q = 11$$

**Step 2 — Compute $\phi(n)$**:
$$\phi(33) = (3-1)(11-1) = 2 \times 10 = 20$$

**Step 3 — Compute private key $d = 13^{-1} \bmod 20$**:

Extended Euclidean on $(20, 13)$:
- $20 = 1 \times 13 + 7 \implies 7 = 20 - 13$
- $13 = 1 \times 7 + 6 \implies 6 = 13 - 7$
- $7 = 1 \times 6 + 1 \implies 1 = 7 - 6$

Back-substitute:
- $1 = 7 - (13 - 7) = 2 \times 7 - 13 = 2(20 - 13) - 13 = 2 \times 20 - 3 \times 13$

$$-3 \times 13 \equiv 1 \pmod{20} \implies d = -3 \equiv 17 \pmod{20}$$

Verify: $13 \times 17 = 221 = 11 \times 20 + 1 \equiv 1 \pmod{20}$ ✓

**Step 4 — Decrypt $C = 8$: compute $8^{17} \bmod 33$**:

Binary of 17 = $10001_2$.

| Step | Computation | Intermediate |
|---|---|---|
| $8^1 \bmod 33$ | $= 8$ | 8 |
| $8^2 \bmod 33$ | $= 64 - 33 = 31 \equiv -2$ | 31 |
| $8^4 \bmod 33$ | $= (-2)^2 = 4$ | 4 |
| $8^8 \bmod 33$ | $= 4^2 = 16$ | 16 |
| $8^{16} \bmod 33$ | $= 16^2 = 256 = 7 \times 33 + 25 \equiv -8$ | 25 |
| $8^{17} = 8^{16} \times 8^1$ | $= (-8) \times 8 = -64 \equiv -64 + 2 \times 33 = 2$ | **2** |

$$\boxed{M = 2}$$

---

### Example 2: RSA Decryption with Given Primes [KTU January 2023, Q15(a)]

**Problem**: $p=7$, $q=11$, $e=17$, ciphertext $C=58$. Find plaintext $M$.

**Key generation**:
- $n = 7 \times 11 = 77$
- $\phi(77) = 6 \times 10 = 60$

**Private key** $d = 17^{-1} \bmod 60$:

- $60 = 3 \times 17 + 9$
- $17 = 1 \times 9 + 8$
- $9 = 1 \times 8 + 1$

Back-substitute: $1 = 9 - 8 = 9 - (17 - 9) = 2 \times 9 - 17 = 2(60 - 3 \times 17) - 17 = 2 \times 60 - 7 \times 17$

$$d = -7 \equiv 53 \pmod{60}$$

Verify: $17 \times 53 = 901 = 15 \times 60 + 1$ ✓

**Decrypt** $M = 58^{53} \bmod 77$ via CRT:

**Mod 7**: $58 \equiv 2 \pmod 7$. Fermat: $2^6 \equiv 1 \pmod 7$. $53 = 8 \times 6 + 5$. $2^5 = 32 \equiv 4 \pmod 7$.

**Mod 11**: $58 \equiv 3 \pmod{11}$. Fermat: $3^{10} \equiv 1 \pmod{11}$. $53 = 5 \times 10 + 3$. $3^3 = 27 \equiv 5 \pmod{11}$.

**CRT solve**: $M \equiv 4 \pmod 7$ and $M \equiv 5 \pmod{11}$.

Try $M = 11k + 5$: $k=0 \to 5 \bmod 7 = 5$ (No). $k=1 \to 16 \bmod 7 = 2$ (No). $k=2 \to 27 \bmod 7 = 6$ (No). $k=3 \to 38 \bmod 7 = 3$ (No). $k=4 \to 49 \bmod 7 = 0$ (No). $k=5 \to 60 \bmod 7 = 4$ ✓

$$\boxed{M = 60}$$

---

### Example 3: RSA Key Generation — Full Computation

**Problem**: Given $p=7$, $q=17$, $e=5$. Find private key $d$ and encrypt $M=6$.

**Key generation**:
- $n = 7 \times 17 = 119$
- $\phi(119) = 6 \times 16 = 96$
- Find $d$: $5d \equiv 1 \pmod{96}$.

$96 = 19 \times 5 + 1 \implies 1 = 96 - 19 \times 5 \implies d = -19 \equiv 77 \pmod{96}$

Verify: $5 \times 77 = 385 = 4 \times 96 + 1$ ✓

**Encrypt** $M = 6$: $C = 6^5 \bmod 119$
$6^2 = 36$, $6^4 = 36^2 = 1296 = 10 \times 119 + 106 \equiv 106 \pmod{119}$
$6^5 = 106 \times 6 = 636 = 5 \times 119 + 41$

$$C = 41$$

**Decrypt** $C = 41$: $M = 41^{77} \bmod 119$

Via CRT:
- $\pmod 7$: $41 \equiv 6 \pmod 7$. $77 = 12 \times 6 + 5$. $6^5 = 7776 = 1110 \times 7 + 6 \equiv 6 \pmod 7$. ✓
- $\pmod{17}$: $41 \equiv 7 \pmod{17}$. $77 = 4 \times 16 + 13$. $7^{13} \pmod{17}$: $7^2=49\equiv15, 7^4\equiv15^2=225\equiv 225-13\times17=4, 7^8\equiv16, 7^{12}=7^8\cdot7^4\equiv16\times4=64\equiv 64-3\times17=13, 7^{13}=13\times7=91\equiv91-5\times17=6 \pmod{17}$. ✓

CRT: $M \equiv 6 \pmod 7$ and $M \equiv 6 \pmod{17}$. Since both are 6: $M = 6$ ✓

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q5 — 4 Marks]
*(Full solution already given in Example 1 above — reproduced for completeness.)*

**Question**: In a public key system using RSA, you intercept ciphertext $C=8$ sent to a user whose public key is $e=13, n=33$. What is the plaintext $M$?

**Answer**:
1. Factor: $n=33 \implies p=3, q=11$
2. $\phi(33) = (2)(10) = 20$
3. $d = 13^{-1} \bmod 20 = 17$ (since $13 \times 17 = 221 = 11 \times 20 + 1$)
4. $M = 8^{17} \bmod 33 = \mathbf{2}$ (computed via repeated squaring as shown above)

---

### Question 2 [KTU June 2022, Part C, Q14(b) / January 2023, Part A, Q5 — 4 Marks]
**Question**: Differentiate Conventional (Symmetric) and Public Key Cryptosystems.

**Solution**:

| Attribute | Symmetric (Conventional) | Public Key (Asymmetric) |
|---|---|---|
| **Number of Keys** | One shared secret key | Key pair: Public Key + Private Key |
| **Key Secrecy Requirement** | Entire key secret between both parties | Only private key secret; public key openly distributed |
| **Key Distribution** | Requires secure channel; $N(N-1)/2$ keys for $N$ users | Each user needs 1 key pair; $N$-user network: $2N$ keys |
| **Computational Speed** | Very fast (hardware: gigabits/second) | 1,000–10,000× slower than symmetric |
| **Mathematical Basis** | Permutations, S-boxes, XOR | Integer factorization, discrete logarithm, elliptic curves |
| **Digital Signatures** | Cannot provide non-repudiation | Inherent feature via private key signing |
| **Practical Application** | Bulk data encryption (AES-GCM) | Key exchange, authentication, signatures |
| **Standard Algorithms** | AES, 3DES, IDEA, RC4, ChaCha20 | RSA, ECDSA, Diffie-Hellman, DSA |

---

### Question 3 [KTU January 2023, Part C, Q15(a) — 5 Marks]
**Question**: Using RSA, find the plaintext for ciphertext $C=58$, given $p=7$, $q=11$, $e=17$.

**Solution**: (Full working in Example 2 above.)

1. $n = 77$, $\phi(n) = 60$
2. $d = 53$ (since $17 \times 53 = 901 \equiv 1 \pmod{60}$)
3. $M = 58^{53} \bmod 77$
   - Via CRT: $58^{53} \equiv 4 \pmod 7$ and $\equiv 5 \pmod{11}$
   - Solving: $M = 60$

$$\boxed{M = 60}$$
