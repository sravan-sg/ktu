# Module 3: Revision Notes — Quick Review & High-Yield Summary

## Submodule 1: Number Theory Foundations
- **Euclidean Algorithm**: $\gcd(a, b) = \gcd(b, a \bmod b)$.
- **Extended Euclidean Algorithm**: Solves $a \cdot x + b \cdot y = \gcd(a, b)$. If $\gcd(a, m) = 1$, then $x \equiv a^{-1} \pmod m$.
- **Euler's Totient $\phi(n)$**:
  - $\phi(p) = p - 1$ for prime $p$.
  - $\phi(pq) = (p - 1)(q - 1)$ for distinct primes $p, q$.
  - General formula: $\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$.
- **Fermat's Little Theorem**: If $p$ is prime and $\gcd(a, p) = 1$, then:
  $$a^{p-1} \equiv 1 \pmod p \iff a^p \equiv a \pmod p$$
- **Euler's Theorem**: If $\gcd(a, n) = 1$, then:
  $$a^{\phi(n)} \equiv 1 \pmod n \iff a^{\phi(n)+1} \equiv a \pmod n$$
- **Primitive Root**: $g$ has order $p-1$ modulo prime $p$. Powers $g^1, \dots, g^{p-1} \bmod p$ generate $\{1, 2, \dots, p-1\}$.

---

## Submodule 2: RSA Cryptosystem
- **Key Generation**:
  1. Choose large primes $p, q$.
  2. Modulus $n = p \cdot q$.
  3. $\phi(n) = (p - 1)(q - 1)$.
  4. Select $e$ such that $\gcd(e, \phi(n)) = 1$ and $1 < e < \phi(n)$.
  5. Calculate $d \equiv e^{-1} \pmod{\phi(n)}$ ($e \cdot d \equiv 1 \pmod{\phi(n)}$).
  6. Public Key: $PU = \{e, n\}$, Private Key: $PR = \{d, n\}$.
- **Encryption**: $C = M^e \bmod n$.
- **Decryption**: $M = C^d \bmod n$.
- **Proof**: Relies on $ed = k\phi(n) + 1$, Fermat's Little Theorem, and Chinese Remainder Theorem: $M^{ed} \equiv M \pmod n$.
- **Security**: Based on difficulty of factoring $n$ into $p \cdot q$.

---

## Submodule 3: Diffie-Hellman & Elliptic Curve Cryptography (ECC)
- **Diffie-Hellman Key Exchange**:
  - Public parameters: Prime $q$, primitive root $\alpha$.
  - Alice: Private $X_A$, Public $Y_A = \alpha^{X_A} \bmod q$.
  - Bob: Private $X_B$, Public $Y_B = \alpha^{X_B} \bmod q$.
  - Shared Key: $K = (Y_B)^{X_A} \bmod q = (Y_A)^{X_B} \bmod q = \alpha^{X_A X_B} \bmod q$.
  - Vulnerability: Man-in-the-Middle (MITM) attack due to lack of authentication.
- **Elliptic Curves over $\mathbb{F}_p$**:
  - Weierstrass equation: $y^2 \equiv x^3 + ax + b \pmod p$ with $4a^3 + 27b^2 \not\equiv 0 \pmod p$.
  - Point addition ($P \neq Q$): $\lambda = \frac{y_2 - y_1}{x_2 - x_1} \pmod p$, $x_3 = \lambda^2 - x_1 - x_2$, $y_3 = \lambda(x_1 - x_3) - y_1$.
  - Point doubling ($P = Q$): $\lambda = \frac{3x_1^2 + a}{2y_1} \pmod p$, $x_3 = \lambda^2 - 2x_1$, $y_3 = \lambda(x_1 - x_3) - y_1$.
  - **ECDH**: Alice sends $P_A = n_A \cdot G$, Bob sends $P_B = n_B \cdot G$. Shared point $K = n_A n_B \cdot G$.

---

## Submodule 4: High-Yield Formulas & Exam Cheatsheet
- Modular Inverses via Extended Euclid:
  $$r_{i-2} = q_i \cdot r_{i-1} + r_i \implies \text{back-substitute to find } ax \equiv 1 \pmod m$$
- Fast RSA Decryption check:
  $$M \equiv C^d \pmod p \quad \text{and} \quad M \equiv C^d \pmod q$$
- Primitive root check for small primes: compute all powers $g^1, g^2, \dots, g^{p-1} \bmod p$. All must be distinct.
- ECC Non-Singularity condition: $4a^3 + 27b^2 \not\equiv 0 \pmod p$.
