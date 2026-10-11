# Diffie-Hellman Key Exchange and Elliptic Curve Cryptography

## 1. Explanation
The **Diffie-Hellman Key Exchange** (1976) was the first practical method for two communicating parties to establish a shared secret key across an insecure public communications channel without any prior secret exchange. The resulting shared key is subsequently used in symmetric ciphers (e.g., AES) for high-speed bulk encryption.

### Mathematical Basis: The Discrete Logarithm Problem
The security of Diffie-Hellman depends on the computational difficulty of calculating **discrete logarithms** in a finite cyclic group $\mathbb{Z}_q^*$:
- Given base $\alpha$, exponent $X$, and prime $q$, computing:
  $$Y = \alpha^X \bmod q$$
  is computationally straightforward using the square-and-multiply algorithm ($O(\log X)$ operations).
- However, given public values $Y$, $\alpha$, and $q$, computing the private exponent:
  $$X = \text{dlog}_{\alpha, q}(Y)$$
  is computationally infeasible for large primes ($q \ge 2048$ bits) using classical computers.

### The Diffie-Hellman Protocol Steps
1. **Public Parameter Agreement**:
   Alice and Bob publicly agree on a large prime $q$ and an integer $\alpha$ that is a **primitive root** modulo $q$.
2. **Key Generation**:
   - **Alice**:
     - Chooses a secret private key: $X_A < q$.
     - Computes public key: $Y_A = \alpha^{X_A} \bmod q$.
     - Sends $Y_A$ to Bob over the network.
   - **Bob**:
     - Chooses a secret private key: $X_B < q$.
     - Computes public key: $Y_B = \alpha^{X_B} \bmod q$.
     - Sends $Y_B$ to Alice over the network.
3. **Shared Secret Key Computation**:
   - Alice computes: $K = (Y_B)^{X_A} \bmod q$.
   - Bob computes: $K = (Y_A)^{X_B} \bmod q$.
   - Mathematical equality:
     $$(Y_B)^{X_A} \equiv (\alpha^{X_B})^{X_A} \equiv \alpha^{X_A X_B} \equiv (\alpha^{X_A})^{X_B} \equiv (Y_A)^{X_B} \pmod q$$
   Both parties arrive at the identical shared secret key $K = \alpha^{X_A X_B} \bmod q$.
   An eavesdropper (Eve) who intercepts $q, \alpha, Y_A, Y_B$ cannot compute $K$ without solving the Diffie-Hellman problem.

```
       Diffie-Hellman Protocol Flow
  Alice (Private: X_A)                    Bob (Private: X_B)
         │                                       │
  Computes Y_A = α^{X_A} mod q            Computes Y_B = α^{X_B} mod q
         │─────────────── Y_A ──────────────────►│
         │◄────────────── Y_B ───────────────────│
  Computes K = (Y_B)^{X_A} mod q          Computes K = (Y_A)^{X_B} mod q
         │                                       │
         ▼                                       ▼
  Shared Secret K                         Shared Secret K
```

### The Man-in-the-Middle (MITM) Attack
The original Diffie-Hellman exchange is **unauthenticated**, making it vulnerable to an active adversary (Darth / Eve):
1. Alice sends $Y_A$ intended for Bob. Darth intercepts $Y_A$ and sends his own rogue public key $Y_{D1}$ to Bob.
2. Bob receives $Y_{D1}$, assumes it came from Alice, and replies with $Y_B$. Darth intercepts $Y_B$ and sends his own rogue public key $Y_{D2}$ to Alice.
3. Alice computes shared key: $K_1 = (Y_{D2})^{X_A} \bmod q$.
4. Bob computes shared key: $K_2 = (Y_{D1})^{X_B} \bmod q$.
5. Darth computes both keys: $K_1 = (Y_A)^{X_{D2}} \bmod q$ and $K_2 = (Y_B)^{X_{D1}} \bmod q$.
6. When Alice sends an encrypted message, Darth intercepts it, decrypts with $K_1$, reads or modifies the message, re-encrypts with $K_2$, and forwards it to Bob. Neither Alice nor Bob detects the breach!
- **Countermeasure**: Authentication via Digital Signatures (e.g., Station-to-Station protocol) or Public-Key Certificates.

### Elliptic Curve Cryptography (ECC)
Introduced independently by Neal Koblitz and Victor Miller in 1985, ECC provides equivalent security to RSA and traditional Diffie-Hellman with **substantially smaller key sizes**:
- 256-bit ECC key offers security equivalent to 3072-bit RSA.
- Smaller keys reduce bandwidth, storage, memory, and power consumption, making ECC ideal for mobile and IoT devices.

#### Mathematical Foundation of Elliptic Curves over $\mathbb{F}_p$
An elliptic curve $E$ over a prime field $\mathbb{F}_p$ (where $p > 3$) is defined by the **Weierstrass equation**:
$$y^2 \equiv x^3 + a x + b \pmod p$$
where constants $a, b \in \mathbb{F}_p$ satisfy the non-singularity condition (no cusps or self-intersections):
$$4a^3 + 27b^2 \not\equiv 0 \pmod p$$
The set $E_p(a, b)$ consists of all points $(x, y)$ satisfying the equation plus an abstract **point at infinity** denoted $\mathcal{O}$ (the group identity).

#### Elliptic Curve Group Operations
1. **Identity**: $P + \mathcal{O} = P$.
2. **Negative of a Point**: The negative of $P = (x, y)$ is $-P = (x, -y \bmod p) = (x, p - y)$.
   $$P + (-P) = \mathcal{O}$$
3. **Point Addition ($P \neq Q$)**:
   Let $P = (x_1, y_1)$ and $Q = (x_2, y_2)$ with $x_1 \neq x_2$. The sum $R = P + Q = (x_3, y_3)$ is:
   $$\lambda = \frac{y_2 - y_1}{x_2 - x_1} \pmod p$$
   $$x_3 = (\lambda^2 - x_1 - x_2) \bmod p$$
   $$y_3 = (\lambda(x_1 - x_3) - y_1) \bmod p$$
4. **Point Doubling ($P = Q$)**:
   When $P = (x_1, y_1)$ is added to itself ($2P = (x_3, y_3)$ with $y_1 \neq 0$):
   $$\lambda = \frac{3x_1^2 + a}{2y_1} \pmod p$$
   $$x_3 = (\lambda^2 - 2x_1) \bmod p$$
   $$y_3 = (\lambda(x_1 - x_3) - y_1) \bmod p$$

#### Elliptic Curve Diffie-Hellman (ECDH) Key Exchange
1. Globally agreed parameters: Prime $p$, curve coefficients $a, b$, and a base generator point $G \in E_p(a, b)$ of large prime order $n$.
2. Alice selects private key $n_A < n$ and computes public point: $P_A = n_A \cdot G$.
3. Bob selects private key $n_B < n$ and computes public point: $P_B = n_B \cdot G$.
4. Shared Secret Point:
   - Alice computes: $K = n_A \cdot P_B = n_A(n_B \cdot G)$.
   - Bob computes: $K = n_B \cdot P_A = n_B(n_A \cdot G)$.
   - $K = n_A n_B \cdot G$. The $x$-coordinate of $K$ is used as the shared symmetric key.

---

## 2. Example: Elliptic Curve Point Verification
- Let curve be $E_{23}(1, 1): y^2 \equiv x^3 + x + 1 \pmod{23}$.
- Test point $P = (3, 10)$:
  - Left side: $y^2 = 10^2 = 100 \equiv 100 - 4 \times 23 = 8 \pmod{23}$.
  - Right side: $x^3 + x + 1 = 3^3 + 3 + 1 = 27 + 3 + 1 = 31 \equiv 8 \pmod{23}$.
  - Both sides equal $8$. Point $P(3, 10)$ lies on the curve!

---

## 3. Applications & Use Cases
1. **TLS 1.3 Key Exchange**: Uses ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) with Curve25519 (X25519) to provide Perfect Forward Secrecy (PFS).
2. **Blockchain & Cryptocurrency Wallets**: Bitcoin and Ethereum rely on the secp256k1 elliptic curve for wallet address derivation and transaction signing (ECDSA).

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Full Diffie-Hellman Computation with Primitive Root Proof [KTU May 2019]
**Problem**:
Consider a Diffie-Hellman scheme with common prime $q = 11$ and primitive root $\alpha = 2$.
1. Show that 2 is a primitive root of 11.
2. If user A has public key $Y_A = 9$, what is A's private key $X_A$?
3. If user B has public key $Y_B = 3$, what is the shared secret key $K$?

**Step-by-step Solution**:
1. **Show that 2 is a primitive root of 11**:
   We compute powers $2^k \bmod 11$ for $k = 1, 2, \dots, 10$:
   - $2^1 \bmod 11 = 2$
   - $2^2 \bmod 11 = 4$
   - $2^3 \bmod 11 = 8$
   - $2^4 \bmod 11 = 16 \bmod 11 = 5$
   - $2^5 \bmod 11 = 32 \bmod 11 = 10$
   - $2^6 \bmod 11 = 20 \bmod 11 = 9$
   - $2^7 \bmod 11 = 18 \bmod 11 = 7$
   - $2^8 \bmod 11 = 14 \bmod 11 = 3$
   - $2^9 \bmod 11 = 6 \bmod 11 = 6$
   - $2^{10} \bmod 11 = 12 \bmod 11 = 1$
   The powers generate the set $\{2, 4, 8, 5, 10, 9, 7, 3, 6, 1\}$, which contains all 10 integers from 1 to 10 with period 10. **Thus, 2 is a primitive root of 11.**

2. **Find A's Private Key $X_A$ given $Y_A = 9$**:
   We have $Y_A = \alpha^{X_A} \bmod q \implies 2^{X_A} \equiv 9 \pmod{11}$.
   Looking up our power table:
   $$2^6 \equiv 9 \pmod{11}$$
   Therefore, A's private key is **$X_A = 6$**.

3. **Compute the Shared Secret Key $K$ with $Y_B = 3$**:
   Alice computes:
   $$K = (Y_B)^{X_A} \bmod q = 3^6 \bmod 11$$
   - $3^1 \bmod 11 = 3$
   - $3^2 \bmod 11 = 9 \equiv -2 \pmod{11}$
   - $3^4 \equiv (-2)^2 = 4 \pmod{11}$
   - $3^6 = 3^4 \times 3^2 \equiv 4 \times (-2) = -8 \pmod{11}$
   $$-8 + 11 = \mathbf{3}$$
   The shared secret key is **$K = 3$**.

---

### Example 2: Diffie-Hellman Key Exchange Verification
**Problem**:
Let $q = 23$, $\alpha = 5$. Alice chooses $X_A = 6$, Bob chooses $X_B = 15$. Compute public keys and the shared secret key.

**Step-by-step Solution**:
1. **Alice's Public Key**:
   $$Y_A = 5^6 \bmod 23$$
   $5^2 = 25 \equiv 2 \pmod{23}$, $5^6 = (5^2)^3 \equiv 2^3 = 8 \pmod{23}$.
   $$Y_A = 8$$
2. **Bob's Public Key**:
   $$Y_B = 5^{15} \bmod 23$$
   $5^2 \equiv 2 \pmod{23}$, $5^4 \equiv 4 \pmod{23}$, $5^8 \equiv 16 \equiv -7 \pmod{23}$.
   $5^{14} = 5^8 \times 5^4 \times 5^2 \equiv (-7) \times 4 \times 2 = -56 \equiv 13 \pmod{23}$.
   $5^{15} = 13 \times 5 = 65 \equiv 19 \pmod{23}$.
   $$Y_B = 19$$
3. **Shared Secret Key**:
   - Alice: $K = (Y_B)^{X_A} \bmod 23 = 19^6 \bmod 23$.
     $19 \equiv -4 \pmod{23} \implies 19^6 \equiv (-4)^6 = 4096 = 178 \times 23 + 2 = 2$.
   - Bob: $K = (Y_A)^{X_B} \bmod 23 = 8^{15} \bmod 23$.
     $8^2 = 64 \equiv 18 \equiv -5 \pmod{23}$.
     $8^4 \equiv 25 \equiv 2 \pmod{23}$, $8^8 \equiv 4 \pmod{23}$.
     $8^{15} = 8^8 \times 8^4 \times 8^2 \times 8^1 \equiv 4 \times 2 \times (-5) \times 8 = -320 \equiv 2 \pmod{23}$.
   Both compute **$K = 2$**.

---

### Example 3: Elliptic Curve Point Doubling Calculation
**Problem**:
On the curve $E_{23}(1, 1): y^2 \equiv x^3 + x + 1 \pmod{23}$, double the point $P = (3, 10)$ to find $2P$.

**Step-by-step Solution**:
1. Here $a = 1, p = 23, x_1 = 3, y_1 = 10$.
2. Compute slope $\lambda$:
   $$\lambda = \frac{3x_1^2 + a}{2y_1} \pmod{23} = \frac{3(3)^2 + 1}{2(10)} = \frac{3(9) + 1}{20} = \frac{28}{20} \equiv \frac{5}{-3} \pmod{23}$$
   Since $-3 \equiv 20 \pmod{23}$:
   $$\lambda \equiv 5 \times (20)^{-1} \pmod{23}$$
   Find $20^{-1} \bmod 23$: $20 \times 15 = 300 = 13 \times 23 + 1 \implies 20^{-1} \equiv 15 \pmod{23}$.
   $$\lambda = (5 \times 15) \bmod 23 = 75 \bmod 23 = 6$$
3. Compute $x_3$:
   $$x_3 = (\lambda^2 - 2x_1) \bmod 23 = (6^2 - 2(3)) \bmod 23 = (36 - 6) \bmod 23 = 30 \bmod 23 = \mathbf{7}$$
4. Compute $y_3$:
   $$y_3 = (\lambda(x_1 - x_3) - y_1) \bmod 23 = (6(3 - 7) - 10) \bmod 23 = (6(-4) - 10) = -34 \bmod 23$$
   $$-34 + 2 \times 23 = -34 + 46 = \mathbf{12}$$
5. Result: **$2P = (7, 12)$**.
   Verification: $12^2 = 144 \equiv 6 \pmod{23}$.
   $x^3 + x + 1 = 7^3 + 7 + 1 = 343 + 8 = 351 = 15 \times 23 + 6 \equiv 6 \pmod{23}$. Matches!

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part C, Q16(a) - 5 Marks]
**Question**: Consider a Diffie Hellman scheme with a common prime $q = 11$ and primitive root $\alpha = 2$.
(i) Show that 2 is a primitive root of 11.
(ii) If user A has public key $Y_A = 9$, what is A’s private key?
(iii) If user B has public key $Y_B = 3$, what is the shared secret key $K$, shared with A?

**Solution**:
1. **Part (i): Verification of Primitive Root**:
   An integer $\alpha$ is a primitive root of a prime $q$ if its powers modulo $q$ generate all non-zero integers $\{1, 2, \dots, q-1\}$.
   For $q = 11$ and $\alpha = 2$:
   - $2^1 \bmod 11 = 2$
   - $2^2 \bmod 11 = 4$
   - $2^3 \bmod 11 = 8$
   - $2^4 \bmod 11 = 16 \bmod 11 = 5$
   - $2^5 \bmod 11 = 32 \bmod 11 = 10$
   - $2^6 \bmod 11 = 64 \bmod 11 = 9$
   - $2^7 \bmod 11 = 128 \bmod 11 = 7$
   - $2^8 \bmod 11 = 256 \bmod 11 = 3$
   - $2^9 \bmod 11 = 512 \bmod 11 = 6$
   - $2^{10} \bmod 11 = 1024 \bmod 11 = 1$
   The order of $2$ modulo 11 is $10 = \phi(11)$, and the residues $\{2, 4, 8, 5, 10, 9, 7, 3, 6, 1\}$ form the complete reduced residue system modulo 11. Thus, **2 is indeed a primitive root of 11**.

2. **Part (ii): Determining User A's Private Key $X_A$**:
   Alice's public key equation is:
   $$Y_A = \alpha^{X_A} \bmod q \implies 2^{X_A} \equiv 9 \pmod{11}$$
   Consulting our power table computed above:
   $$2^6 \equiv 9 \pmod{11}$$
   Therefore, User A's private key is **$X_A = 6$**.

3. **Part (iii): Computing the Shared Secret Key $K$**:
   User B's public key is $Y_B = 3$.
   Alice computes the shared key using her private key $X_A = 6$:
   $$K = (Y_B)^{X_A} \bmod q = 3^6 \bmod 11$$
   Evaluating $3^6 \bmod 11$:
   - $3^2 = 9 \equiv -2 \pmod{11}$
   - $3^4 = (-2)^2 = 4 \pmod{11}$
   - $3^6 = 3^4 \cdot 3^2 \equiv 4 \cdot (-2) = -8 \pmod{11}$
   - Reducing to positive residue: $-8 + 11 = 3$.
   The shared secret key is **$K = 3$**.

---

### Question 2 [KTU May 2019, Part C, Q14(b) - 5 Marks]
**Question**: Discuss the key exchange procedure using Elliptic Curves.

**Solution**:
1. **Elliptic Curve Diffie-Hellman (ECDH) Overview**:
   ECDH is the elliptic curve analogue of the classical Diffie-Hellman protocol. It allows two communicating entities to establish a shared secret key by multiplying private scalar integers with points on an elliptic curve.

2. **Global Public Domain Parameters**:
   Alice and Bob agree upon a public set of curve parameters:
   - A prime number $p$ defining the finite field $\mathbb{F}_p$.
   - Curve equation coefficients $a, b \in \mathbb{F}_p$ defining curve $E_p(a, b): y^2 \equiv x^3 + ax + b \pmod p$.
   - A base generator point $G = (x_G, y_G)$ on the curve having large prime order $n$ (where $n \cdot G = \mathcal{O}$).

3. **Protocol Key Exchange Steps**:
   - **Step 1: Alice's Key Generation**:
     Alice selects a random private key integer $n_A$ from the range $[1, n - 1]$.
     Alice computes her public key point on the curve:
     $$P_A = n_A \cdot G$$
     Alice sends point $P_A = (x_A, y_A)$ to Bob.
   - **Step 2: Bob's Key Generation**:
     Bob selects a random private key integer $n_B$ from the range $[1, n - 1]$.
     Bob computes his public key point on the curve:
     $$P_B = n_B \cdot G$$
     Bob sends point $P_B = (x_B, y_B)$ to Alice.
   - **Step 3: Secret Point Computation**:
     - Alice computes the shared point:
       $$K = n_A \cdot P_B = n_A \cdot (n_B \cdot G) = n_A n_B \cdot G$$
     - Bob computes the shared point:
       $$K = n_B \cdot P_A = n_B \cdot (n_A \cdot G) = n_A n_B \cdot G$$
     Both parties arrive at the identical curve point $K = (x_K, y_K)$.
   - **Step 4: Symmetric Key Extraction**:
     The shared secret symmetric key is derived from the $x$-coordinate $x_K$ (or by passing $x_K$ through a key derivation function such as HKDF).

4. **Security Strength**:
   An attacker who intercepts $G, P_A,$ and $P_B$ cannot compute $K = n_A n_B \cdot G$ without solving the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**: finding $n_A$ from $P_A = n_A \cdot G$. The best known algorithms for ECDLP (Pollard's rho) have exponential time complexity $O(\sqrt{n})$, enabling ECC to achieve equal security with a 256-bit key compared to a 3072-bit RSA/DH modulus.

---

### Question 3 [KTU January 2023, Part C, Q14 - 9 Marks]
**Question**: Discuss the Diffie Hellman Key exchange Algorithm. Explain with an example how it is vulnerable to man-in middle attack.

**Solution**:
1. **The Diffie-Hellman Key Exchange Algorithm**:
   - **System Parameters**: A large prime number $q$ and a primitive root $\alpha$ modulo $q$ known publicly.
   - **Alice**:
     1. Selects private key $X_A < q$.
     2. Computes public key $Y_A = \alpha^{X_A} \bmod q$.
     3. Transmits $Y_A$ to Bob.
   - **Bob**:
     1. Selects private key $X_B < q$.
     2. Computes public key $Y_B = \alpha^{X_B} \bmod q$.
     3. Transmits $Y_B$ to Alice.
   - **Shared Key Generation**:
     - Alice computes: $K = (Y_B)^{X_A} \bmod q$.
     - Bob computes: $K = (Y_A)^{X_B} \bmod q$.
     - Since $(Y_B)^{X_A} \equiv (\alpha^{X_B})^{X_A} \equiv (\alpha^{X_A})^{X_B} \equiv (Y_A)^{X_B} \equiv \alpha^{X_A X_B} \pmod q$, both derive the identical symmetric key $K$.

2. **Man-in-the-Middle (MITM) Attack Vulnerability**:
   The basic Diffie-Hellman protocol provides zero authentication of the endpoints. An active adversary (Darth) stationed on the network path can intercept and substitute keys without Alice or Bob knowing.

```
 Alice (X_A)                     Darth (X_D1, X_D2)                  Bob (X_B)
      │                                  │                               │
      │─── Y_A (intercepted) ───────────►│                               │
      │                                  │─── Y_D1 (sent to Bob) ───────►│
      │                                  │◄── Y_B (intercepted) ─────────│
      │◄── Y_D2 (sent to Alice) ─────────│                               │
      │                                  │                               │
 Computes K_1                       Computes K_1 & K_2              Computes K_2
```

3. **Concrete Numerical Walkthrough of the MITM Attack**:
   - **Public Parameters**: Let $q = 353$, $\alpha = 3$.
   - **Legitimate Setup**:
     - Alice chooses private key $X_A = 97$. Computes $Y_A = 3^{97} \bmod 353 = 40$.
     - Bob chooses private key $X_B = 233$. Computes $Y_B = 3^{233} \bmod 353 = 248$.
   - **Darth's Active Interception**:
     - Darth chooses two secret private keys: $X_{D1} = 150$ and $X_{D2} = 210$.
     - Darth calculates public keys:
       $$Y_{D1} = 3^{150} \bmod 353 = 180$$
       $$Y_{D2} = 3^{210} \bmod 353 = 270$$
   - **Message Manipulation**:
     - Alice transmits $Y_A = 40$ intended for Bob. Darth intercepts it, suppresses it, and sends $Y_{D1} = 180$ to Bob.
     - Bob transmits $Y_B = 248$ intended for Alice. Darth intercepts it, suppresses it, and sends $Y_{D2} = 270$ to Alice.
   - **Key Calculation**:
     - Alice computes:
       $$K_1 = (Y_{D2})^{X_A} \bmod 353 = 270^{97} \bmod 353 = \mathbf{160}$$
     - Bob computes:
       $$K_2 = (Y_{D1})^{X_B} \bmod 353 = 180^{233} \bmod 353 = \mathbf{219}$$
     - Darth computes both keys:
       $$K_1 = (Y_A)^{X_{D2}} \bmod 353 = 40^{210} \bmod 353 = \mathbf{160}$$
       $$K_2 = (Y_B)^{X_{D1}} \bmod 353 = 248^{150} \bmod 353 = \mathbf{219}$$
   - **The Compromise**:
     When Alice encrypts data with $K_1 = 160$, Darth intercepts it, decrypts with $K_1$, reads/alters the plaintext, re-encrypts with $K_2 = 219$, and forwards it to Bob. Bob decrypts with $K_2$ without raising any alerts.
   - **Resolution**: Use digital signatures, pre-shared public keys, or digital certificates (e.g., Station-to-Station protocol).
