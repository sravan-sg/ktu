# RSA Algorithm and Public Key Cryptography Principles

## 1. Explanation
In 1976, Whitfield Diffie and Martin Hellman introduced the concept of **Public-Key Cryptography** (asymmetric cryptography), revolutionizing the field by solving the dual problems of secure key exchange and digital authentication. In 1977, Ron Rivest, Adi Shamir, and Leonard Adleman created the **RSA Cryptosystem**, which remains the most foundational public-key algorithm in computing history.

### Principles of Public-Key Cryptosystems
Conventional symmetric ciphers use the same key for encryption and decryption. A public-key cryptosystem uses an **asymmetric key pair**:
1. **Public Key ($PU$)**: Disseminated openly to everyone.
2. **Private Key ($PR$)**: Kept strictly confidential by the owner.

```
       Public-Key Cryptography Principles
   Alice                                Bob
[ Message M ]                       [ Receiver ]
      │                                  ▲
      ▼                                  │
[ Encrypt with Bob's PU ]           [ Decrypt with Bob's PR ]
      │                                  │
      ▼                                  │
[ Ciphertext C ] ──────── Internet ──────┘
```

#### Dual Modes of Operation
- **Confidentiality (Encryption)**: Sender encrypts using recipient's public key ($PU_B$):
  $$C = E(PU_B, M)$$
  Recipient decrypts using their private key ($PR_B$):
  $$M = D(PR_B, C)$$
  Only Bob can decrypt because only Bob possesses $PR_B$.
- **Authentication / Digital Signature**: Sender encrypts using their own private key ($PR_A$):
  $$S = E(PR_A, M)$$
  Anyone can verify and read using sender's public key ($PU_A$):
  $$M = D(PU_A, S)$$
  Provides non-repudiation and proof of origin.

#### One-Way Trapdoor Functions
Public-key schemes are built on **one-way trapdoor functions** $f$:
- Given $x$, computing $y = f(x)$ is computationally easy.
- Given $y$, computing $x = f^{-1}(y)$ is computationally infeasible *unless* a secret piece of information (the "trapdoor" $k$) is known, in which case computing $x = f^{-1}(y, k)$ is easy.
- In RSA, the trapdoor is the prime factorization of the modulus $n = p \cdot q$.

### The RSA Algorithm
RSA is a block cipher in which the plaintext and ciphertext are integers between $0$ and $n - 1$ for some modulus $n$.

#### 1. Key Generation
1. Select two large distinct prime numbers $p$ and $q$ ($p \neq q$).
2. Compute the modulus $n = p \cdot q$.
3. Compute Euler's totient function:
   $$\phi(n) = (p - 1)(q - 1)$$
4. Select an integer $e$ (public exponent) such that:
   $$\gcd(e, \phi(n)) = 1 \quad \text{and} \quad 1 < e < \phi(n)$$
5. Calculate the private exponent $d$ such that:
   $$d \cdot e \equiv 1 \pmod{\phi(n)} \iff d \equiv e^{-1} \pmod{\phi(n)}$$
   (Computed using the Extended Euclidean Algorithm).
6. **Public Key**: $PU = \{e, n\}$.
7. **Private Key**: $PR = \{d, n\}$.

#### 2. Encryption
Given plaintext message $M$ where $0 \le M < n$:
$$C = M^e \bmod n$$

#### 3. Decryption
Given ciphertext $C$:
$$M = C^d \bmod n$$

### Mathematical Proof of Correctness
We must prove that for all $M < n$:
$$C^d \equiv (M^e)^d \equiv M^{ed} \equiv M \pmod n$$
Since $e \cdot d \equiv 1 \pmod{\phi(n)}$, there exists an integer $k$ such that:
$$ed = k \cdot \phi(n) + 1 = k(p - 1)(q - 1) + 1$$
We prove that $M^{k(p-1)(q-1) + 1} \equiv M \pmod p$ and modulo $q$:
- **Case 1**: If $\gcd(M, p) = 1$, by Fermat's Little Theorem $M^{p-1} \equiv 1 \pmod p$.
  $$M^{ed} = (M^{p-1})^{k(q-1)} \cdot M \equiv 1^{k(q-1)} \cdot M \equiv M \pmod p$$
- **Case 2**: If $\gcd(M, p) \neq 1$, then since $p$ is prime, $p \mid M \implies M \equiv 0 \pmod p$.
  $$M^{ed} \equiv 0^{ed} \equiv 0 \equiv M \pmod p$$
Thus, in all cases, $M^{ed} \equiv M \pmod p$.
By identical reasoning: $M^{ed} \equiv M \pmod q$.
Since $p$ and $q$ are distinct primes, by the Chinese Remainder Theorem:
$$M^{ed} \equiv M \pmod{p \cdot q} \implies M^{ed} \equiv M \pmod n$$
Q.E.D.

### Security and Attacks on RSA
1. **Factorization of $n$**: If an adversary factors $n = p \cdot q$, they easily compute $\phi(n) = (p - 1)(q - 1)$ and then determine $d \equiv e^{-1} \pmod{\phi(n)}$. For security, $n$ must be at least 2048 to 3072 bits.
2. **Mathematical Attacks**: Computing $\phi(n)$ directly without factoring $n$ is equivalent in difficulty to factoring $n$.
3. **Small Encryption Exponent ($e = 3$)**: Vulnerable to Coppersmith's theorem or broadcast attacks if identical messages are sent to multiple recipients. Modern implementations use $e = 65,537 = 2^{16} + 1$.
4. **Padding Schemes (OAEP)**: "Textbook RSA" is deterministic and vulnerable to chosen-ciphertext attacks. Practical RSA uses **Optimal Asymmetric Encryption Padding (OAEP - PKCS #1 v2.1)** to introduce randomized padding.

---

## 2. Example: Small-Scale RSA Setup
- Choose $p = 3$, $q = 11$.
- Modulus $n = 3 \times 11 = 33$.
- $\phi(n) = (3 - 1)(11 - 1) = 2 \times 10 = 20$.
- Choose $e = 7$ (since $\gcd(7, 20) = 1$).
- Calculate $d$: $7d \equiv 1 \pmod{20} \implies 7 \times 3 = 21 \equiv 1 \pmod{20} \implies d = 3$.
- Public key: $(e=7, n=33)$, Private key: $(d=3, n=33)$.
- Encrypt $M = 2$: $C = 2^7 \bmod 33 = 128 \bmod 33 = 29$.
- Decrypt $C = 29$: $M = 29^3 \bmod 33 = 24389 \bmod 33 = 2$. Recovered!

---

## 3. Applications & Use Cases
1. **Digital Certificates and Public Key Infrastructure (PKI)**: X.509 digital certificates rely on RSA signatures to validate the authenticity of domain names and SSL/TLS web servers.
2. **Secure Software Updates & Code Signing**: Operating system kernels (Linux kernel modules, Windows Authenticode) verify RSA signatures embedded in executable binaries prior to installation.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Full RSA Cryptanalysis & Decryption [KTU May 2019]
**Problem**:
In a public key system using RSA, you intercept the ciphertext $C = 8$ sent to a user whose public key is $e = 13, n = 33$. What is the plaintext $M$?

**Step-by-step Solution**:
1. **Factor the Modulus $n = 33$**:
   - $n = 33 = 3 \times 11$.
   - Thus, $p = 3, q = 11$.
2. **Compute Euler's Totient $\phi(n)$**:
   $$\phi(n) = (p - 1)(q - 1) = (3 - 1)(11 - 1) = 2 \times 10 = 20$$
3. **Compute the Private Decryption Key $d$**:
   $$d \cdot e \equiv 1 \pmod{\phi(n)} \implies 13 \cdot d \equiv 1 \pmod{20}$$
   Using the Extended Euclidean Algorithm:
   - $20 = 13 \times 1 + 7 \implies 7 = 20 - 13 \times 1$
   - $13 = 7 \times 1 + 6 \implies 6 = 13 - 7 \times 1$
   - $7 = 6 \times 1 + 1 \implies 1 = 7 - 6 \times 1$
   Backward substitution:
   - $1 = 7 - (13 - 7) = 2 \times 7 - 13$
   - $1 = 2 \times (20 - 13) - 13 = 2 \times 20 - 3 \times 13$
   Therefore:
   $$-3 \times 13 \equiv 1 \pmod{20}$$
   $$d \equiv -3 \equiv 20 - 3 = \mathbf{17} \pmod{20}$$
   Check: $13 \times 17 = 221 = 11 \times 20 + 1 \equiv 1 \pmod{20}$.
4. **Decrypt Ciphertext $C = 8$**:
   $$M = C^d \bmod n = 8^{17} \bmod 33$$
   Using Square-and-Multiply (binary of 17 is $10001_2$):
   - $8^1 \bmod 33 = 8$
   - $8^2 \bmod 33 = 64 \bmod 33 = 31 \equiv -2 \pmod{33}$
   - $8^4 \equiv (-2)^2 \equiv 4 \pmod{33}$
   - $8^8 \equiv 4^2 \equiv 16 \pmod{33}$
   - $8^{16} \equiv 16^2 = 256 = 7 \times 33 + 25 = 25 \equiv -8 \pmod{33}$
   - $8^{17} = 8^{16} \times 8^1 \equiv (-8) \times 8 = -64 \pmod{33}$
   $$-64 \bmod 33 = -64 + 2 \times 33 = -64 + 66 = \mathbf{2}$$
   **Plaintext**: $\mathbf{M = 2}$.

---

### Example 2: RSA Decryption with Given Primes [KTU January 2023]
**Problem**:
Using the RSA algorithm, find the plaintext if ciphertext $C = 58$, given primes $p = 7, q = 11$ and public key $e = 17$.

**Step-by-step Solution**:
1. Modulus $n = p \times q = 7 \times 11 = 77$.
2. $\phi(n) = (7 - 1)(11 - 1) = 6 \times 10 = 60$.
3. Compute private key $d$:
   $$17 \cdot d \equiv 1 \pmod{60}$$
   Extended Euclidean division:
   - $60 = 17 \times 3 + 9 \implies 9 = 60 - 17 \times 3$
   - $17 = 9 \times 1 + 8 \implies 8 = 17 - 9 \times 1$
   - $9 = 8 \times 1 + 1 \implies 1 = 9 - 8 \times 1$
   Substitute back:
   - $1 = 9 - (17 - 9) = 2 \times 9 - 17$
   - $1 = 2 \times (60 - 17 \times 3) - 17 = 2 \times 60 - 7 \times 17$
   $$-7 \times 17 \equiv 1 \pmod{60} \implies d = 60 - 7 = \mathbf{53}$$
   Check: $17 \times 53 = 901 = 15 \times 60 + 1 \equiv 1 \pmod{60}$.
4. Decrypt $C = 58$:
   $$M = 58^{53} \bmod 77$$
   Notice $58 \equiv -19 \pmod{77}$.
   Using Chinese Remainder Theorem:
   - Modulo $p = 7$: $58 \equiv 2 \pmod 7$.
     By Fermat's Little Theorem: $2^6 \equiv 1 \pmod 7$.
     $M_p = 2^{53 \bmod 6} = 2^5 = 32 \equiv 4 \pmod 7$.
   - Modulo $q = 11$: $58 \equiv 3 \pmod{11}$.
     By Fermat's Little Theorem: $3^{10} \equiv 1 \pmod{11}$.
     $M_q = 3^{53 \bmod 10} = 3^3 = 27 \equiv 5 \pmod{11}$.
   Combine:
   $$M \equiv 4 \pmod 7, \quad M \equiv 5 \pmod{11}$$
   Test multiples of 11:
   - $k=0: 5 \equiv 5 \pmod 7$ (No)
   - $k=1: 5 + 11 = 16 \equiv 2 \pmod 7$ (No)
   - $k=2: 5 + 22 = 27 \equiv 6 \pmod 7$ (No)
   - $k=3: 5 + 33 = 38 \equiv 3 \pmod 7$ (No)
   - $k=4: 5 + 44 = 49 \equiv 0 \pmod 7$ (No)
   - $k=5: 5 + 55 = 60 \equiv 4 \pmod 7$ (Yes! $60 = 8 \times 7 + 4$).
   **Plaintext**: $\mathbf{M = 60}$.

---

### Example 3: Finding Decryption Key for $p=7, q=17, e=5$
**Problem**:
Given $p = 7$, $q = 17$, $e = 5$, determine the private decryption key $d$.

**Step-by-step Solution**:
1. $\phi(n) = (7 - 1)(17 - 1) = 6 \times 16 = 96$.
2. Solve $5d \equiv 1 \pmod{96}$:
   $$96 = 5 \times 19 + 1 \implies 1 = 96 - 5 \times 19$$
   $$-19 \times 5 \equiv 1 \pmod{96}$$
   $$d = 96 - 19 = \mathbf{77}$$
3. Verification: $5 \times 77 = 385 = 4 \times 96 + 1 \equiv 1 \pmod{96}$.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q5 - 4 Marks]
**Question**: In a public key system using RSA, you intercept the cipher text C=8 sent to a user whose public key is e=13, n=33. What is the plain text M?

**Solution**:
1. **Step 1: Factorize the Modulus $n$**:
   Given $n = 33$.
   Since 33 is small, it factorizes directly into primes:
   $$p = 3, \quad q = 11$$

2. **Step 2: Calculate Euler's Totient Function $\phi(n)$**:
   $$\phi(n) = (p - 1)(q - 1) = (3 - 1)(11 - 1) = 2 \times 10 = 20$$

3. **Step 3: Determine Private Decryption Key $d$**:
   The private key $d$ is the multiplicative inverse of $e = 13$ modulo $\phi(n) = 20$:
   $$e \cdot d \equiv 1 \pmod{\phi(n)} \implies 13 \cdot d \equiv 1 \pmod{20}$$
   Applying the Euclidean algorithm:
   $$20 = 13 \times 1 + 7$$
   $$13 = 7 \times 1 + 6$$
   $$7 = 6 \times 1 + 1$$
   Back-substitution:
   $$1 = 7 - 6 = 7 - (13 - 7) = 2 \times 7 - 13$$
   $$1 = 2 \times (20 - 13) - 13 = 2 \times 20 - 3 \times 13$$
   $$-3 \times 13 \equiv 1 \pmod{20}$$
   $$d \equiv -3 \equiv 20 - 3 = \mathbf{17}$$
   Verification: $13 \times 17 = 221 = 20 \times 11 + 1 \equiv 1 \pmod{20}$.

4. **Step 4: Decrypt Ciphertext $C = 8$ to Obtain Plaintext $M$**:
   $$M = C^d \bmod n = 8^{17} \bmod 33$$
   Using modular exponentiation:
   - $8^2 = 64 \equiv 31 \equiv -2 \pmod{33}$
   - $8^4 \equiv (-2)^2 = 4 \pmod{33}$
   - $8^8 \equiv 4^2 = 16 \pmod{33}$
   - $8^{16} \equiv 16^2 = 256 = 7 \times 33 + 25 \equiv -8 \pmod{33}$
   - $8^{17} = 8^{16} \cdot 8^1 \equiv (-8) \cdot 8 = -64 \pmod{33}$
   - Adding $2 \times 33 = 66$:
     $$-64 + 66 = \mathbf{2}$$

**Result**:
- The plaintext is **$M = 2$**.

---

### Question 2 [KTU January 2023, Part A, Q5 / June 2022, Part C, Q14(b) - 4 Marks]
**Question**: Differentiate Conventional (Symmetric) and Public Key Cryptosystems.

**Solution**:

| Comparison Attribute | Conventional (Symmetric) Cryptosystem | Public Key (Asymmetric) Cryptosystem |
|---|---|---|
| **Number of Keys** | Single shared secret key used for both encryption and decryption. | Pair of mathematically related keys: one Public Key and one Private Key. |
| **Key Secrecy** | Key must remain strictly confidential between both communicating parties. | Public key is openly published; only the private key must be kept secret. |
| **Mathematical Basis** | Permutations (transpositions), non-linear substitutions (S-boxes), XOR operations. | Number-theoretic one-way trapdoor functions (factoring, discrete logs, elliptic curves). |
| **Key Distribution Complexity** | Requires a secure out-of-band channel or KDC. An $N$-user network requires $\frac{N(N-1)}{2}$ shared keys. | Solves key distribution. An $N$-user network requires only $2N$ keys ($N$ pairs). |
| **Computational Speed** | Extremely fast. Throughput reaches gigabits/second in software and hardware. | Computationally intensive. Typically 1,000 to 10,000 times slower than symmetric ciphers. |
| **Digital Signatures & Non-Repudiation** | Cannot provide non-repudiation (both sender and receiver share the same key). | Inherently provides non-repudiation and legal authenticity via digital signatures. |
| **Typical Algorithms** | AES, DES, 3DES, IDEA, RC4. | RSA, Diffie-Hellman, ECC (ECDSA), DSA. |

---

### Question 3 [KTU January 2023, Part C, Q15(a) - 5 Marks]
**Question**: Using RSA algorithm find the plaintext if the ciphertext is 58. Assume the values for $p = 7, q = 11$ and $e = 17$.

**Solution**:
1. **Compute Modulus $n$ and Totient $\phi(n)$**:
   $$n = p \times q = 7 \times 11 = 77$$
   $$\phi(n) = (p - 1)(q - 1) = (7 - 1)(11 - 1) = 6 \times 10 = 60$$

2. **Compute Private Decryption Exponent $d$**:
   $$e \cdot d \equiv 1 \pmod{\phi(n)} \implies 17 \cdot d \equiv 1 \pmod{60}$$
   Applying Euclidean algorithm:
   - $60 = 17 \times 3 + 9 \implies 9 = 60 - 3 \times 17$
   - $17 = 9 \times 1 + 8 \implies 8 = 17 - 1 \times 9$
   - $9 = 8 \times 1 + 1 \implies 1 = 9 - 1 \times 8$
   Backward substitution:
   - $1 = 9 - (17 - 9) = 2 \times 9 - 17$
   - $1 = 2 \times (60 - 3 \times 17) - 17 = 2 \times 60 - 7 \times 17$
   $$-7 \times 17 \equiv 1 \pmod{60}$$
   $$d \equiv -7 \equiv 60 - 7 = \mathbf{53}$$
   Verification: $17 \times 53 = 901 = 15 \times 60 + 1 \equiv 1 \pmod{60}$.

3. **Decrypt Ciphertext $C = 58$ to Recover Plaintext $M$**:
   $$M = C^d \bmod n = 58^{53} \bmod 77$$
   Using Chinese Remainder Theorem:
   - Modulo 7:
     $$58 \equiv 2 \pmod 7$$
     By Fermat's theorem ($2^6 \equiv 1 \pmod 7$):
     $$58^{53} \equiv 2^{53 \bmod 6} = 2^5 = 32 \equiv 4 \pmod 7$$
   - Modulo 11:
     $$58 \equiv 3 \pmod{11}$$
     By Fermat's theorem ($3^{10} \equiv 1 \pmod{11}$):
     $$58^{53} \equiv 3^{53 \bmod 10} = 3^3 = 27 \equiv 5 \pmod{11}$$
   - Solving system:
     $$M \equiv 4 \pmod 7$$
     $$M \equiv 5 \pmod{11}$$
     $M = 11k + 5$:
     For $k=5$: $M = 11(5) + 5 = 60$.
     $60 \bmod 7 = 4$. Both congruences satisfied!

**Result**:
- The plaintext is **$M = 60$**.
