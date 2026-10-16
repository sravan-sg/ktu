# Diffie-Hellman Key Exchange and Elliptic Curve Cryptography

## 1. Explanation

### 1.1 The Core Problem — Why Key Exchange Matters

Every symmetric encryption session needs a **shared secret key**. The fundamental challenge: how do two parties who have never met before agree on a secret key over an **insecure, public channel**, in the presence of eavesdroppers?

Before Diffie and Hellman (1976), this problem had no known solution. The only options were:
1. Meet in person and exchange a key physically.
2. Use a trusted courier.
3. Use a Key Distribution Center (KDC) — a single point of failure.

**Diffie and Hellman's insight**: It is possible for two parties to compute the **same value independently**, using only public exchanges, if the mathematical operation is non-commutative in an asymmetric way — specifically, if discrete exponentiation mixes information in a way that only the party with the private exponent can "combine" correctly.

This is the mathematical magic: **$g^{ab} = (g^a)^b = (g^b)^a \pmod p$**. Alice uses $g^b$ (Bob's public key) and her private $a$ to compute the shared secret $g^{ab}$. Bob uses $g^a$ (Alice's public key) and his private $b$. An eavesdropper sees only $g^a$ and $g^b$ — and cannot compute $g^{ab}$ without solving the Discrete Logarithm Problem.

---

### 1.2 Mathematical Basis: The Discrete Logarithm Problem

**The Discrete Logarithm Problem (DLP)**: Given a prime $q$, a primitive root $\alpha$ modulo $q$, and a value $Y$, find the integer $X$ such that:
$$Y \equiv \alpha^X \pmod q$$

**Why it is hard**:
- **Forward** (easy): $Y = \alpha^X \bmod q$ computed via repeated squaring in $O(\log X)$ modular multiplications.
- **Reverse** (hard): No efficient classical algorithm exists. Best known: Pohlig-Hellman and Index Calculus are sub-exponential but still infeasible for primes $q \ge 2048$ bits.

**Illustration**: With $q = 2^{2048}$-bit prime, finding $X$ from $Y = 3^X \bmod q$ would require more operations than there are atoms in the observable universe using current algorithms.

---

### 1.3 The Diffie-Hellman Key Exchange Protocol

#### System Setup (Public Parameters)
- A **large prime** $q$ (at least 2048 bits for security).
- A **primitive root** $\alpha$ modulo $q$ (a generator of the cyclic group $\mathbb{Z}_q^*$).
- Both $q$ and $\alpha$ are published publicly. Knowledge of them does not compromise security.

#### Protocol Steps

```
PUBLIC PARAMETERS: prime q, primitive root α mod q
                                                      
Alice (private: X_A)              Bob (private: X_B)
      │                                   │
      │  Compute Y_A = α^{X_A} mod q      │  Compute Y_B = α^{X_B} mod q
      │                                   │
      │ ──────── Send Y_A ──────────────► │
      │ ◄──────── Send Y_B ──────────────│
      │                                   │
      │  K = (Y_B)^{X_A} mod q            │  K = (Y_A)^{X_B} mod q
      │    = (α^{X_B})^{X_A} mod q        │    = (α^{X_A})^{X_B} mod q
      │    = α^{X_A X_B} mod q            │    = α^{X_A X_B} mod q
      ▼                                   ▼
      Both derive IDENTICAL shared secret K = α^{X_A X_B} mod q
```

**Mathematical Equality**:
$$(Y_B)^{X_A} = (\alpha^{X_B})^{X_A} = \alpha^{X_B X_A} = \alpha^{X_A X_B} = (\alpha^{X_A})^{X_B} = (Y_A)^{X_B} \pmod q$$

**Security**: An eavesdropper Eve observes the public channel and knows $q, \alpha, Y_A, Y_B$. To compute $K = \alpha^{X_A X_B} \bmod q$, she needs either $X_A$ or $X_B$ — which requires solving the DLP.

**Key Point**: The DH shared secret $K$ is not directly used as an encryption key. Instead, $K$ is passed through a **Key Derivation Function** (KDF, e.g., HKDF) to produce one or more symmetric keys with proper length and uniformity.

---

### 1.4 The Man-in-the-Middle (MITM) Attack on DH

**Critical Vulnerability**: Basic DH provides no **authentication**. Alice and Bob cannot verify they are communicating with each other versus a network attacker.

**Attack Scenario** (Darth is the active attacker):

```
Alice (X_A)              Darth (X_D1, X_D2)              Bob (X_B)
     │                          │                              │
     │── Y_A ──────intercepted──►│                              │
     │                          │── Y_D1 (fake Alice key) ────►│
     │                          │◄── Y_B ──────intercepted ────│
     │◄── Y_D2 (fake Bob key) ──│                              │
     │                          │                              │
K1 = Y_D2^{X_A} mod q       Darth has:                  K2 = Y_D1^{X_B} mod q
                             K1 = Y_A^{X_D2} mod q
                             K2 = Y_B^{X_D1} mod q
```

**Result**:
- Alice thinks she shares key $K_1$ with Bob → actually shares it with Darth.
- Bob thinks he shares key $K_2$ with Alice → actually shares it with Darth.
- Darth decrypts Alice's messages with $K_1$, reads/modifies them, re-encrypts with $K_2$, forwards to Bob.
- Neither Alice nor Bob detects the intrusion.

**Concrete Numerical Example** (Stallings §10.3):
- $q = 353$, $\alpha = 3$
- Alice: $X_A = 97$, $Y_A = 3^{97} \bmod 353 = 40$
- Bob: $X_B = 233$, $Y_B = 3^{233} \bmod 353 = 248$
- Darth: $X_{D1} = 150$, $X_{D2} = 210$
  - $Y_{D1} = 3^{150} \bmod 353 = 180$
  - $Y_{D2} = 3^{210} \bmod 353 = 270$
- Darth intercepts $Y_A=40$, sends $Y_{D1}=180$ to Bob; intercepts $Y_B=248$, sends $Y_{D2}=270$ to Alice
- $K_1 = 270^{97} \bmod 353 = 40^{210} \bmod 353 = 160$ (Alice and Darth agree)
- $K_2 = 180^{233} \bmod 353 = 248^{150} \bmod 353 = 219$ (Bob and Darth agree)

**Countermeasures**:
1. **Station-to-Station (STS) Protocol**: Each party signs their DH public key using a long-term DSA/RSA key. The signature proves the public key came from the authenticated party.
2. **Public Key Infrastructure (PKI)**: DH public keys are embedded in X.509 certificates signed by a Certificate Authority.
3. **Pre-shared Keys (PSK)**: In constrained environments (IoT, VPN), pre-shared symmetric keys authenticate DH.

---

### 1.5 Elliptic Curve Cryptography (ECC)

#### 1.5.1 Why ECC? — The Key Size Advantage

ECC achieves the same security level as RSA/DH with dramatically smaller keys. This is because the **Elliptic Curve Discrete Logarithm Problem (ECDLP)** is significantly harder than the integer DLP for equal key sizes — no sub-exponential algorithms are known for ECDLP.

| Security Level | RSA Key Size | DH Key Size | ECC Key Size | Ratio |
|---|---|---|---|---|
| 80-bit | 1024 bits | 1024 bits | 160 bits | ~6:1 |
| 112-bit | 2048 bits | 2048 bits | 224 bits | ~9:1 |
| 128-bit | 3072 bits | 3072 bits | 256 bits | ~12:1 |
| 192-bit | 7680 bits | 7680 bits | 384 bits | ~20:1 |
| 256-bit | 15360 bits | 15360 bits | 521 bits | ~29:1 |

**Practical benefits**: Smaller keys mean faster computation, less bandwidth, lower memory, and reduced energy consumption — critical for mobile phones, IoT devices, smart cards, and embedded systems.

#### 1.5.2 Mathematical Foundation — Elliptic Curves over Finite Fields

An **elliptic curve** over the prime field $\mathbb{F}_p$ (where $p > 3$ is prime) is defined by the **Weierstrass equation**:
$$y^2 \equiv x^3 + ax + b \pmod p$$

where constants $a, b \in \mathbb{F}_p$ satisfy the **non-singularity condition** (no cusps or self-intersections):
$$4a^3 + 27b^2 \not\equiv 0 \pmod p$$

The set $E_p(a,b)$ consists of all points $(x, y)$ satisfying the equation, plus an abstract **point at infinity** $\mathcal{O}$ which serves as the group identity.

**Why elliptic curves?** The set of points $E_p(a,b) \cup \{\mathcal{O}\}$ forms an **abelian group** under point addition. This group has a large cyclic subgroup of prime order, making it ideal for DLP-based cryptography. The curve provides a different algebraic structure from $\mathbb{Z}_p^*$ where different (harder) DLP attacks apply.

**Number of points** (Hasse's Theorem): The number of points $|E_p(a,b)|$ satisfies:
$$|p + 1 - |E_p(a,b)|| \le 2\sqrt{p}$$

This is approximately $p$, ensuring a large group.

#### 1.5.3 Elliptic Curve Group Operations

The group law on an elliptic curve is defined geometrically (over $\mathbb{R}$) and algebraically (over $\mathbb{F}_p$):

**1. Identity Element**: $\mathcal{O}$ is the point at infinity. For all $P$: $P + \mathcal{O} = P$.

**2. Negation**: The negative of $P = (x, y)$ is $-P = (x, -y \bmod p) = (x, p - y)$.
$$P + (-P) = \mathcal{O}$$

**3. Point Addition ($P \ne Q$, $x_1 \ne x_2$)**:

Let $P = (x_1, y_1)$, $Q = (x_2, y_2)$. The sum $R = P + Q = (x_3, y_3)$ is:
$$\lambda = \frac{y_2 - y_1}{x_2 - x_1} \pmod p \quad \text{(slope of secant line PQ)}$$
$$x_3 = (\lambda^2 - x_1 - x_2) \bmod p$$
$$y_3 = (\lambda(x_1 - x_3) - y_1) \bmod p$$

*Geometric interpretation*: Draw the line through $P$ and $Q$; it intersects the curve at a third point $R'$; reflect $R'$ over the x-axis to get $R = P + Q$.

**4. Point Doubling ($P = Q$, $y_1 \ne 0$)**:

The sum $2P = (x_3, y_3)$ uses the tangent line at $P$:
$$\lambda = \frac{3x_1^2 + a}{2y_1} \pmod p \quad \text{(slope of tangent at P)}$$
$$x_3 = (\lambda^2 - 2x_1) \bmod p$$
$$y_3 = (\lambda(x_1 - x_3) - y_1) \bmod p$$

**5. Scalar Multiplication** (Point multiplication): $kP = P + P + \cdots + P$ ($k$ times) — computed via Double-and-Add (analogous to square-and-multiply):
```
Result = O (point at infinity)
For each bit b of k from MSB to LSB:
    Result = 2 × Result (point doubling)
    If b == 1: Result = Result + P (point addition)
```
Complexity: $O(\log k)$ point operations.

**The ECDLP**: Given $P$ and $Q = kP$, find $k$. This is computationally infeasible for large prime-order groups (~256-bit). Best known attack (Pollard's rho): $O(\sqrt{n})$ where $n$ is the group order.

#### 1.5.4 Standard ECC Curves

| Curve Name | Field Size | Use Cases |
|---|---|---|
| **P-256 (secp256r1, NIST)** | 256 bits | TLS 1.3, HTTPS, X.509 |
| **P-384 (secp384r1, NIST)** | 384 bits | NSA Suite B, government |
| **secp256k1** | 256 bits | Bitcoin, Ethereum ECDSA |
| **Curve25519 (X25519)** | 255 bits | TLS 1.3 key exchange, Signal Protocol |
| **Ed25519** | 255 bits | SSH, TLS, OpenSSH |

Curve25519 is notable for its **security by design**: parameters were chosen verifiably without any possibility of backdoors (all constants are deterministic hashes of the string "expand 32-byte k").

#### 1.5.5 Elliptic Curve Diffie-Hellman (ECDH)

**Global Domain Parameters** (public, agreed upon by both parties):
- Prime $p$ defining $\mathbb{F}_p$
- Curve coefficients $a, b$
- Base point (generator) $G = (x_G, y_G)$ on $E_p(a,b)$ with large prime order $n$ (meaning $n \cdot G = \mathcal{O}$)

**Protocol**:

```
Alice (private: n_A)                    Bob (private: n_B)
     │                                        │
     │  P_A = n_A · G                         │  P_B = n_B · G
     │ ─────────── Send P_A ────────────────►│
     │ ◄────────── Send P_B ─────────────────│
     │                                        │
     │  K = n_A · P_B                         │  K = n_B · P_A
     │    = n_A (n_B · G)                     │    = n_B (n_A · G)
     │    = n_A n_B · G                       │    = n_A n_B · G
     ▼                                        ▼
     Shared secret point K = (x_K, y_K)
     Symmetric key = KDF(x_K) [x-coordinate of K]
```

**Security**: An attacker knowing $G, P_A, P_B$ must solve $n_A$ from $P_A = n_A \cdot G$ (the ECDLP). For Curve25519, the best known attack requires $\approx 2^{128}$ operations.

**ECDHE (Ephemeral ECDH)**: Each session uses freshly generated $n_A, n_B$ — providing **Perfect Forward Secrecy** (PFS). Even if the server's long-term private key is compromised in the future, past session keys remain secure because the ephemeral keys are discarded after each session.

---

## 2. Example

### 2.1 Elliptic Curve Point Verification: $E_{23}(1, 1)$

Curve: $y^2 \equiv x^3 + x + 1 \pmod{23}$. Test point $P = (3, 10)$.

- **LHS**: $y^2 = 10^2 = 100 \equiv 100 - 4 \times 23 = 100 - 92 = 8 \pmod{23}$
- **RHS**: $x^3 + x + 1 = 27 + 3 + 1 = 31 \equiv 31 - 23 = 8 \pmod{23}$

LHS = RHS = 8. **Point $P(3, 10)$ lies on $E_{23}(1,1)$** ✓

### 2.2 Finding All Points on $E_5(1, 1)$: $y^2 \equiv x^3 + x + 1 \pmod 5$

Non-singularity: $4(1)^3 + 27(1)^2 = 31 \equiv 1 \pmod 5 \ne 0$ ✓

Test each $x \in \{0,1,2,3,4\}$:

| $x$ | $x^3 + x + 1 \bmod 5$ | Is it a QR mod 5? | $y$ values |
|---|---|---|---|
| 0 | 1 | Yes ($1 = 1^2$) | $(0,1), (0,4)$ |
| 1 | 3 | No | — |
| 2 | 11 ≡ 1 | Yes | $(2,1), (2,4)$ |
| 3 | 31 ≡ 1 | Yes | $(3,1), (3,4)$ |
| 4 | 69 ≡ 4 | Yes ($4 = 2^2$) | $(4,2), (4,3)$ |

Points: $\{(0,1), (0,4), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), \mathcal{O}\}$ → $|E_5(1,1)| = 9$.

---

## 3. Applications & Use Cases

1. **TLS 1.3 Key Exchange (ECDHE)**: Modern HTTPS connections use Curve25519 ECDHE for key exchange, providing forward secrecy. TLS 1.3 deprecated all non-forward-secure key exchange methods, making ECDHE mandatory for all new TLS connections.

2. **Bitcoin and Ethereum (secp256k1 ECDSA)**: Cryptocurrency wallets use ECC key pairs. The private key is a 256-bit random integer; the public key is the corresponding curve point. Bitcoin addresses are RIPEMD-160(SHA-256(public key)). ECDSA signs transactions, proving ownership without revealing the private key.

3. **Signal Protocol and Messaging Security**: Signal's X3DH (Extended Triple Diffie-Hellman) key agreement and the Double Ratchet use Curve25519 ECDH for Perfect Forward Secrecy. Used in WhatsApp, Facebook Messenger, Google Messages.

4. **Embedded Systems and IoT**: Smart cards (EMV payment cards), RFID chips, and IoT sensors use ECC because small key sizes minimize computation time, power, and silicon area — critical for battery-powered or passively-powered devices.

5. **TLS Client Authentication (mTLS)**: Kubernetes, service meshes (Istio), and zero-trust architectures use ECDSA client certificates for mutual TLS authentication between microservices.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Full Diffie-Hellman with Primitive Root Proof [KTU May 2019, Q16(a)]

**Problem**: DH scheme with $q = 11$, primitive root $\alpha = 2$.
1. Show 2 is a primitive root of 11.
2. If $Y_A = 9$, find $X_A$.
3. If $Y_B = 3$, find shared secret key $K$.

**Part 1 — Primitive Root Verification**:

Compute $2^k \bmod 11$ for $k = 1, \dots, 10$:

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $2^k \bmod 11$ | 2 | 4 | 8 | 5 | 10 | 9 | 7 | 3 | 6 | 1 |

The set $\{2, 4, 8, 5, 10, 9, 7, 3, 6, 1\}$ = $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$ — all non-zero residues mod 11. The order of 2 modulo 11 is $10 = \phi(11)$.

**Therefore, 2 is a primitive root of 11.** ✓

**Part 2 — Find $X_A$**:

$Y_A = \alpha^{X_A} \bmod q \implies 2^{X_A} \equiv 9 \pmod{11}$

From the table: $2^6 \equiv 9 \pmod{11}$

**$X_A = 6$**

**Part 3 — Shared Secret Key**:

$K = (Y_B)^{X_A} \bmod q = 3^6 \bmod 11$

- $3^2 = 9 \equiv -2 \pmod{11}$
- $3^4 = (-2)^2 = 4 \pmod{11}$
- $3^6 = 3^4 \times 3^2 = 4 \times (-2) = -8 \equiv 3 \pmod{11}$

**Shared secret $K = 3$**

*Verification*: If Bob has $X_B = 8$ (since $2^8 \equiv 3 \pmod{11}$), then $K = (Y_A)^{X_B} = 9^8 \bmod 11$. $9 \equiv -2 \pmod{11}$. $(-2)^8 = 256 = 23 \times 11 + 3 \equiv 3 \pmod{11}$. ✓ Both parties compute $K = 3$.

---

### Example 2: DH Key Exchange Verification with Computation [Standard Exam Pattern]

**Problem**: $q = 23$, $\alpha = 5$, Alice: $X_A = 6$, Bob: $X_B = 15$. Compute all public and shared keys.

**Alice's public key**:
$$Y_A = 5^6 \bmod 23$$
$5^2 = 25 \equiv 2 \pmod{23}$
$5^4 = 4 \pmod{23}$
$5^6 = 5^4 \times 5^2 = 4 \times 2 = 8 \pmod{23}$
$$Y_A = 8$$

**Bob's public key**:
$$Y_B = 5^{15} \bmod 23$$
$5^8 = (5^4)^2 = 16 \pmod{23}$
$5^{14} = 5^8 \times 5^4 \times 5^2 = 16 \times 4 \times 2 = 128 \equiv 128 - 5 \times 23 = 13 \pmod{23}$
$5^{15} = 13 \times 5 = 65 = 2 \times 23 + 19 \equiv 19 \pmod{23}$
$$Y_B = 19$$

**Shared secret — Alice computes**:
$$K = (Y_B)^{X_A} \bmod 23 = 19^6 \bmod 23$$
$19 \equiv -4 \pmod{23}$
$(-4)^2 = 16$, $(-4)^4 = 16^2 = 256 = 11 \times 23 + 3 \equiv 3$, $(-4)^6 = 3 \times 16 = 48 \equiv 2 \pmod{23}$
$$K = 2$$

**Shared secret — Bob computes**:
$$K = (Y_A)^{X_B} \bmod 23 = 8^{15} \bmod 23$$
$8^2 = 64 = 2 \times 23 + 18 \equiv -5$
$8^4 = (-5)^2 = 25 \equiv 2$, $8^8 \equiv 4$
$8^{15} = 8^8 \times 8^4 \times 8^2 \times 8 = 4 \times 2 \times (-5) \times 8 = -320$
$-320 \bmod 23$: $320 = 13 \times 23 + 21$, so $-320 \equiv -21 \equiv 2 \pmod{23}$
$$K = 2$$

**Both Alice and Bob compute the same shared secret $K = 2$.** ✓

---

### Example 3: ECC Point Doubling on $E_{23}(1,1)$ [KTU May 2019, Q14(b)]

**Problem**: On curve $y^2 \equiv x^3 + x + 1 \pmod{23}$, compute $2P$ for $P = (3, 10)$.

**Step 1 — Compute slope $\lambda$ (point doubling formula)**:
$$\lambda = \frac{3x_1^2 + a}{2y_1} \pmod p = \frac{3(9) + 1}{20} = \frac{28}{20} \pmod{23}$$

$28 \bmod 23 = 5$, so $\lambda = \frac{5}{20} = 5 \times (20)^{-1} \pmod{23}$

Find $20^{-1} \bmod 23$:
Extended Euclidean: $23 = 1 \times 20 + 3$; $20 = 6 \times 3 + 2$; $3 = 1 \times 2 + 1$.
Back-sub: $1 = 3 - 2 = 3 - (20 - 6 \times 3) = 7 \times 3 - 20 = 7(23 - 20) - 20 = 7 \times 23 - 8 \times 20$.
$20^{-1} \equiv -8 \equiv 15 \pmod{23}$.

Verify: $20 \times 15 = 300 = 13 \times 23 + 1$ ✓

$$\lambda = 5 \times 15 \bmod 23 = 75 \bmod 23 = 75 - 3 \times 23 = 6$$

**Step 2 — Compute $x_3$**:
$$x_3 = (\lambda^2 - 2x_1) \bmod 23 = (36 - 6) \bmod 23 = 30 \bmod 23 = 7$$

**Step 3 — Compute $y_3$**:
$$y_3 = (\lambda(x_1 - x_3) - y_1) \bmod 23 = (6(3 - 7) - 10) \bmod 23 = (-24 - 10) \bmod 23 = -34 \bmod 23$$
$-34 + 2 \times 23 = -34 + 46 = 12$

$$2P = (7, 12)$$

**Verification**: $12^2 = 144 = 6 \times 23 + 6 \equiv 6 \pmod{23}$. $7^3 + 7 + 1 = 343 + 8 = 351 = 15 \times 23 + 6 \equiv 6 \pmod{23}$. LHS = RHS = 6. ✓ Point $(7, 12)$ lies on $E_{23}(1,1)$.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part C, Q16(a) — 5 Marks]
**Question**: DH scheme with $q=11$, $\alpha=2$. (i) Show 2 is primitive root of 11. (ii) If $Y_A=9$, find $X_A$. (iii) If $Y_B=3$, find shared secret $K$.

**Solution**: (Complete numerical solution in Example 1 above.)

**(i)** Powers of 2 mod 11: $\{2,4,8,5,10,9,7,3,6,1\}$ = all non-zero residues. Order = 10 = $\phi(11)$. **2 is a primitive root.** ✓

**(ii)** From the power table: $2^6 \equiv 9 \pmod{11}$. **$X_A = 6$.**

**(iii)** $K = 3^6 \bmod 11 = 4 \times (-2) = -8 \equiv \mathbf{3} \pmod{11}$.

---

### Question 2 [KTU May 2019, Part C, Q14(b) — 5 Marks]
**Question**: Discuss the key exchange procedure using Elliptic Curves.

**Solution**:

**Elliptic Curve Diffie-Hellman (ECDH)** is the elliptic curve analogue of classical DH. It establishes a shared secret by scalar-multiplying a generator point with private integers.

**1. Global Domain Parameters** (publicly agreed):
- Prime $p$ defining finite field $\mathbb{F}_p$.
- Curve $E_p(a,b): y^2 \equiv x^3 + ax + b \pmod p$ satisfying $4a^3 + 27b^2 \ne 0$.
- Base point (generator) $G$ on $E_p(a,b)$ of large prime order $n$ (i.e., $n \cdot G = \mathcal{O}$).

**2. Key Generation**:
- Alice: Select random private integer $n_A \in [1, n-1]$. Public key: $P_A = n_A \cdot G$.
- Bob: Select random private integer $n_B \in [1, n-1]$. Public key: $P_B = n_B \cdot G$.
- Exchange: Alice sends $P_A$ to Bob; Bob sends $P_B$ to Alice (over insecure channel).

**3. Shared Secret Computation**:
- Alice computes: $K = n_A \cdot P_B = n_A(n_B \cdot G) = n_A n_B \cdot G$
- Bob computes: $K = n_B \cdot P_A = n_B(n_A \cdot G) = n_A n_B \cdot G$
- Both arrive at identical point $K = (x_K, y_K)$.
- Symmetric key = KDF($x_K$) (x-coordinate passed through key derivation function).

**4. Security Guarantee**:
An attacker knowing $G, P_A, P_B$ must find $n_A$ from $P_A = n_A \cdot G$ — the **ECDLP**. For 256-bit curves, best known attacks require $O(2^{128})$ operations (Pollard's rho), making it computationally infeasible.

**5. Efficiency vs. RSA**:
- A 256-bit ECC key provides the same security as a 3072-bit RSA key.
- ECDH key generation and key agreement are ~10× faster than DH at equivalent security.
- Used in TLS 1.3 (X25519), SSH, Signal, WhatsApp, iMessage.

---

### Question 3 [KTU January 2023, Part C, Q14 — 9 Marks]
**Question**: Discuss the Diffie-Hellman Key Exchange Algorithm. Explain with an example how it is vulnerable to man-in-middle attack.

**Solution**:

**Part A — DH Algorithm**:

**System Parameters**: Large prime $q$ and primitive root $\alpha$ modulo $q$ (public).

**Protocol**:
- **Alice**: Selects private $X_A < q$. Computes $Y_A = \alpha^{X_A} \bmod q$. Sends $Y_A$ to Bob.
- **Bob**: Selects private $X_B < q$. Computes $Y_B = \alpha^{X_B} \bmod q$. Sends $Y_B$ to Alice.
- **Alice**: $K = (Y_B)^{X_A} \bmod q$. **Bob**: $K = (Y_A)^{X_B} \bmod q$.
- Equality holds because $(Y_B)^{X_A} = \alpha^{X_B X_A} = \alpha^{X_A X_B} = (Y_A)^{X_B} \pmod q$.

**Security**: Eavesdropper knowing $q, \alpha, Y_A, Y_B$ cannot compute $\alpha^{X_A X_B}$ without solving the DLP.

**Part B — MITM Attack on DH**:

The basic DH protocol provides **zero endpoint authentication**. An active adversary (Darth) can intercept and substitute public keys:

```
Alice             Darth                    Bob
  │── Y_A ────intercepted────►│                │
  │                           │── Y_D1 ───────►│
  │                           │◄── Y_B ────────│
  │◄── Y_D2 ──────────────────│                │
  K1 = Y_D2^{X_A}         K1 = Y_A^{X_D2}    K2 = Y_D1^{X_B}
                           K2 = Y_B^{X_D1}
```

**Numerical Walkthrough** ($q = 353$, $\alpha = 3$):

| Party | Private | Public | Shared |
|---|---|---|---|
| Alice | $X_A = 97$ | $Y_A = 3^{97} \bmod 353 = 40$ | $K_1 = 270^{97} \bmod 353 = 160$ |
| Bob | $X_B = 233$ | $Y_B = 3^{233} \bmod 353 = 248$ | $K_2 = 180^{233} \bmod 353 = 219$ |
| Darth | $X_{D1}=150, X_{D2}=210$ | $Y_{D1}=180, Y_{D2}=270$ | $K_1 = 40^{210} \bmod 353 = 160$; $K_2 = 248^{150} \bmod 353 = 219$ |

Darth decrypts Alice's messages with $K_1$, re-encrypts with $K_2$, sends to Bob. Both endpoints believe they are communicating securely.

**Countermeasure**: Station-to-Station (STS) protocol — each party digitally signs their DH public value using a long-term asymmetric key. The signature is verified before the shared secret is used, binding the DH exchange to authenticated identities.
