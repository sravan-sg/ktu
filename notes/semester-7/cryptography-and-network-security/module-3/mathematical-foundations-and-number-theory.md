# Mathematical Foundations and Number Theory

## 1. Explanation

### 1.1 Why Number Theory? — The Deep Intuition

Public-key cryptography is fundamentally **number theory applied to secrecy**. The reason we use number theory — rather than, say, complex geometric constructions — is rooted in a beautiful asymmetry: some arithmetic operations are trivially easy to do in one direction but computationally infeasible to reverse. This "trap-door" property is what makes modern cryptography possible.

All of the following topics exist because RSA, Diffie-Hellman, and ECC need them:

| Math Concept | Cryptographic Purpose |
|---|---|
| Modular Arithmetic | Defines the finite algebraic field where all crypto operations live |
| GCD & Euclidean Algorithm | Determines invertibility; generates encryption/decryption keys |
| Extended Euclidean Algorithm | Computes modular multiplicative inverses (used in RSA key gen) |
| Euler's Totient $\phi(n)$ | Defines the exponent group order for RSA |
| Fermat's & Euler's Theorems | Prove that RSA decryption reverses encryption ($M^{ed} \equiv M \pmod n$) |
| Primitive Roots & Discrete Log | Foundation of Diffie-Hellman and DSA security |

---

### 1.2 Fundamental Theorem of Arithmetic

Every integer $n > 1$ can be **uniquely** represented as a product of prime numbers (up to ordering):
$$n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k} = \prod_{i=1}^k p_i^{e_i}$$
where $p_1 < p_2 < \dots < p_k$ are distinct primes and $e_i \ge 1$.

**Why this matters for cryptography**: RSA's security directly relies on the fact that factoring $n = pq$ (a product of two large primes) is computationally intractable. The Fundamental Theorem guarantees that if an attacker factors $n$, they recover the *unique* primes $p$ and $q$ — there is no ambiguity. Conversely, *generating* $n$ by multiplying two chosen primes $p$ and $q$ is trivially easy ($O(\log^2 n)$ bit operations).

**Size illustration**: A 2048-bit RSA modulus has approximately $2^{2048} \approx 10^{616}$ candidate factor pairs. State-of-the-art factoring algorithms (GNFS) require $O(e^{c(\ln n)^{1/3}(\ln \ln n)^{2/3}})$ operations — still infeasible for $n \ge 2048$ bits.

---

### 1.3 Divisibility and Modular Arithmetic

**Divisibility**: An integer $b$ **divides** $a$ (written $b \mid a$) if there exists an integer $c$ such that $a = b \cdot c$. If $b$ does not divide $a$, we write $b \nmid a$.

**Congruence Modulo $n$**: Two integers $a$ and $b$ are **congruent modulo $n$** (written $a \equiv b \pmod n$) if $n \mid (a - b)$. Equivalently, $a$ and $b$ leave the same remainder when divided by $n$.

**Intuition**: Working modulo $n$ is like arithmetic on a "clock face" with $n$ positions. After reaching $n-1$, you wrap back to $0$. For a modulus of $n = 26$ (the alphabet), $27 \equiv 1 \pmod{26}$ because $27 = 1 \times 26 + 1$.

**Fundamental Properties** (closed under ring operations):
1. **Reflexive**: $a \equiv a \pmod n$
2. **Symmetric**: $a \equiv b \pmod n \implies b \equiv a \pmod n$
3. **Transitive**: $a \equiv b$ and $b \equiv c \pmod n \implies a \equiv c \pmod n$
4. **Addition**: $(a + b) \bmod n = [(a \bmod n) + (b \bmod n)] \bmod n$
5. **Multiplication**: $(a \cdot b) \bmod n = [(a \bmod n) \cdot (b \bmod n)] \bmod n$
6. **Substitution**: $a \equiv b \pmod n$ and $c \equiv d \pmod n \implies a+c \equiv b+d$ and $ac \equiv bd \pmod n$

**The Residue Class**: For modulus $n$, the **complete set of residues** $\mathbb{Z}_n = \{0, 1, 2, \dots, n-1\}$ forms a ring under addition and multiplication modulo $n$. This ring has $n$ elements.

**Multiplicative Inverse** in $\mathbb{Z}_n$: An element $a \in \mathbb{Z}_n$ has a multiplicative inverse $a^{-1}$ (i.e., $a \cdot a^{-1} \equiv 1 \pmod n$) **if and only if** $\gcd(a, n) = 1$.

> **Critical cryptographic implication**: In RSA, the private key $d$ is the multiplicative inverse of the public exponent $e$ modulo $\phi(n)$. The Extended Euclidean Algorithm computes this inverse. The inverse exists only because we ensure $\gcd(e, \phi(n)) = 1$ during key generation.

**The Reduced Residue System**: $\mathbb{Z}_n^* = \{a \in \mathbb{Z}_n : \gcd(a, n) = 1\}$ forms a **multiplicative group** under multiplication modulo $n$. Its order is $|\mathbb{Z}_n^*| = \phi(n)$.

---

### 1.4 Greatest Common Divisor ($\gcd$) and the Euclidean Algorithm

**Definition**: The **greatest common divisor** $\gcd(a, b)$ is the largest positive integer that divides both $a$ and $b$. If $\gcd(a, b) = 1$, the integers are **relatively prime** or **coprime**.

**Euclidean Algorithm**: Based on the key identity $\gcd(a, b) = \gcd(b, a \bmod b)$, applied recursively:

```
gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a mod b)
```

**Why it terminates**: Each step strictly decreases the second argument (since $a \bmod b < b$). The algorithm terminates in $O(\log \min(a,b))$ steps.

**Worked trace** for $\gcd(252, 105)$:
```
gcd(252, 105):  252 = 2×105 + 42       → gcd(105, 42)
gcd(105, 42):   105 = 2×42 + 21        → gcd(42, 21)
gcd(42, 21):     42 = 2×21 + 0         → gcd(21, 0) = 21
```
Result: $\gcd(252, 105) = 21$.

**Properties**:
- $\gcd(a, 0) = a$
- $\gcd(a, b) = \gcd(b, a)$
- If $p$ is prime: $\gcd(a, p) \in \{1, p\}$
- **Euclid's Lemma**: If $p \mid ab$ and $p$ is prime, then $p \mid a$ or $p \mid b$ (or both).

---

### 1.5 Extended Euclidean Algorithm (Bézout's Identity)

**Bézout's Theorem**: For any integers $a, b$, there exist integers $x, y$ such that:
$$a \cdot x + b \cdot y = \gcd(a, b)$$

The Extended Euclidean Algorithm computes $\gcd(a, b)$ **and** the Bézout coefficients $x, y$ simultaneously.

**Tabular Method (Recommended for Exam)**:

Maintain columns $(r, s, t)$ where $r = as + bt$ (Bézout relation is maintained throughout):

| Step | $r$ (remainder) | $s$ (coeff of $a$) | $t$ (coeff of $b$) | Quotient $q$ |
|---|---|---|---|---|
| 0 | $a$ | 1 | 0 | — |
| 1 | $b$ | 0 | 1 | — |
| $i$ | $r_{i-2} - q \cdot r_{i-1}$ | $s_{i-2} - q \cdot s_{i-1}$ | $t_{i-2} - q \cdot t_{i-1}$ | $\lfloor r_{i-2}/r_{i-1} \rfloor$ |

**Application — Computing Modular Multiplicative Inverse**:

When $\gcd(a, m) = 1$, Bézout's identity gives $a \cdot x + m \cdot y = 1$. Reducing modulo $m$:
$$a \cdot x \equiv 1 \pmod m \implies x \equiv a^{-1} \pmod m$$

If $x$ is negative, add $m$: $a^{-1} = (x \bmod m + m) \bmod m$.

**Why this is crucial for RSA**: RSA private key $d = e^{-1} \bmod \phi(n)$ is computed **exactly** by the Extended Euclidean Algorithm on inputs $e$ and $\phi(n)$.

---

### 1.6 Euler's Totient Function $\phi(n)$

**Definition**: $\phi(n)$ counts the positive integers $\le n$ that are coprime to $n$:
$$\phi(n) = |\{k : 1 \le k \le n,\ \gcd(k, n) = 1\}|$$

**Intuition**: $\phi(n)$ is the size of the multiplicative group $\mathbb{Z}_n^*$ — the set of elements that have multiplicative inverses modulo $n$. By Euler's theorem, every element $a \in \mathbb{Z}_n^*$ satisfies $a^{\phi(n)} \equiv 1 \pmod n$.

**Key Formulas**:

| Case | Formula | Example |
|---|---|---|
| $n = p$ (prime) | $\phi(p) = p - 1$ | $\phi(7) = 6$ |
| $n = p^k$ | $\phi(p^k) = p^k - p^{k-1} = p^{k-1}(p-1)$ | $\phi(8) = \phi(2^3) = 4$ |
| $n = pq$ (distinct primes) | $\phi(pq) = (p-1)(q-1)$ | $\phi(15) = 4 \times 2 = 8$ |
| $n = p_1^{e_1} \cdots p_k^{e_k}$ | $\phi(n) = n \prod_{p \mid n}\left(1 - \frac{1}{p}\right)$ | $\phi(12) = 12 \cdot \frac{1}{2} \cdot \frac{2}{3} = 4$ |

**Multiplicative Property**: If $\gcd(a, b) = 1$, then $\phi(ab) = \phi(a)\phi(b)$.

**Manual verification of $\phi(12)$**:
Integers from 1 to 12: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$.
Coprime to 12: $\{1, 5, 7, 11\}$ → $\phi(12) = 4$. ✓

**RSA Connection**: The private key $d \equiv e^{-1} \pmod{\phi(n)}$ and the correctness proof uses $M^{\phi(n)} \equiv 1 \pmod n$ (Euler's theorem). This is why $\phi(n) = (p-1)(q-1)$ — the "magic number" of RSA key generation — is so critical: it is the exponent of the group $\mathbb{Z}_n^*$.

---

### 1.7 Fermat's Little Theorem

**Statement** (Stallings §8.4): If $p$ is prime and $\gcd(a, p) = 1$:
$$a^{p-1} \equiv 1 \pmod p$$

Alternative form valid for all integers $a$:
$$a^p \equiv a \pmod p$$

**Intuition**: The multiplicative group $\mathbb{Z}_p^*$ has order $p-1$. By Lagrange's theorem in group theory, the order of any element divides the group order. So $a^{p-1} \equiv (a^{\text{ord}(a)})^{(p-1)/\text{ord}(a)} \equiv 1^{(p-1)/\text{ord}(a)} \equiv 1 \pmod p$.

**Complete Proof** (by permutation argument):

Consider the set $S = \{1 \cdot a,\ 2 \cdot a,\ 3 \cdot a,\ \dots,\ (p-1) \cdot a\} \pmod p$.

**Claim 1 — No element is 0 mod p**: If $ka \equiv 0 \pmod p$ for some $1 \le k \le p-1$, then $p \mid ka$. Since $p$ is prime and $\gcd(a,p)=1$, this forces $p \mid k$. But $1 \le k \le p-1$, so $p \nmid k$. Contradiction. ✗

**Claim 2 — All elements are distinct mod p**: If $j \cdot a \equiv k \cdot a \pmod p$ with $1 \le j < k \le p-1$, then $(k-j)a \equiv 0 \pmod p$. By the same argument, $p \mid (k-j)$. But $0 < k-j < p$, so impossible. ✗

Therefore, the set $S \pmod p$ is a **permutation of** $\{1, 2, \dots, p-1\}$.

Multiplying all elements together:
$$(1 \cdot a)(2 \cdot a) \cdots ((p-1) \cdot a) \equiv 1 \cdot 2 \cdots (p-1) \pmod p$$
$$a^{p-1} \cdot (p-1)! \equiv (p-1)! \pmod p$$

Since $\gcd((p-1)!, p) = 1$ (as $p$ is prime and each factor $< p$), we cancel $(p-1)!$:
$$\boxed{a^{p-1} \equiv 1 \pmod p} \quad \text{Q.E.D.}$$

**Computational application — Fast Modular Exponentiation**:
To compute $a^k \bmod p$ for large $k$:
1. Reduce: $a^k = a^{q(p-1) + r}$ where $r = k \bmod (p-1)$.
2. Then: $a^k \equiv a^{q(p-1)} \cdot a^r \equiv 1^q \cdot a^r \equiv a^r \pmod p$.
3. Compute only $a^r \bmod p$ where $r < p-1$.

**Fermat Primality Test**: If $a^{n-1} \not\equiv 1 \pmod n$ for some $a$ with $\gcd(a,n)=1$, then $n$ is composite. (Beware Carmichael numbers — composite numbers that pass Fermat's test for all $a$; use Miller-Rabin instead.)

---

### 1.8 Euler's Theorem (Generalization of Fermat's Theorem)

**Statement**: For any integer $a$ with $\gcd(a, n) = 1$:
$$a^{\phi(n)} \equiv 1 \pmod n$$

**Relationship to Fermat's Theorem**: When $n = p$ is prime, $\phi(p) = p-1$, and Euler's theorem reduces exactly to Fermat's Little Theorem.

**Alternative form**:
$$a^{\phi(n)+1} \equiv a \pmod n$$

This is the **exact statement underlying RSA correctness**. In RSA, $ed \equiv 1 \pmod{\phi(n)}$, so $ed = k\phi(n) + 1$ for some integer $k$. Then:
$$M^{ed} = M^{k\phi(n)+1} = (M^{\phi(n)})^k \cdot M \equiv 1^k \cdot M \equiv M \pmod n$$

The full RSA correctness proof using Fermat's theorem (for both $\pmod p$ and $\pmod q$) combined with the Chinese Remainder Theorem is given in the RSA topic notes.

---

### 1.9 Primitive Roots and Discrete Logarithms

**Primitive Root Modulo $p$**: An integer $g$ is a **primitive root** modulo prime $p$ if the powers:
$$g^1, g^2, g^3, \dots, g^{p-1} \pmod p$$
generate **all** $p-1$ distinct non-zero residues $\{1, 2, \dots, p-1\}$.

Equivalently, the **multiplicative order** of $g$ modulo $p$ equals $\phi(p) = p-1$: $\text{ord}_p(g) = p-1$.

**Existence Guarantee**: Every prime $p$ has at least one primitive root. There are exactly $\phi(p-1)$ distinct primitive roots modulo $p$.

**Example** ($p = 11$, $g = 2$):
| $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $2^k \bmod 11$ | 2 | 4 | 8 | 5 | 10 | 9 | 7 | 3 | 6 | 1 |

All residues $\{1,\dots,10\}$ appear exactly once → **2 is a primitive root of 11**.

**Discrete Logarithm Problem (DLP)**: Given $g, p, Y$ with $Y \equiv g^X \pmod p$, find $X$.

$$X = \log_g Y \pmod p \quad \text{(Discrete Logarithm)}$$

- **Forward direction** (easy): Compute $Y = g^X \bmod p$ using repeated squaring in $O(\log X)$ multiplications.
- **Reverse direction** (hard): No polynomial-time algorithm is known for the DLP for large primes. Best known: Index Calculus with sub-exponential complexity $L_p[1/3, c]$.

**Security requirement**: For DLP-based schemes (DH, DSA, ElGamal), use primes $p \ge 2048$ bits. For ECDLP (ECC), 256 bits suffice because elliptic curve group structures have no known sub-exponential attacks.

**Why the DLP is one-way**: Computing $g^X \bmod p$ mixes the regular arithmetic progression of the exponent with the highly irregular pattern of discrete powers modulo $p$. There is no known efficient "shortcut" that exploits the structure of both simultaneously.

---

## 2. Examples

### 2.1 Computing $\phi(360)$

Prime factorization: $360 = 2^3 \times 3^2 \times 5^1$

Using the product formula:
$$\phi(360) = 360 \times \left(1 - \frac{1}{2}\right) \times \left(1 - \frac{1}{3}\right) \times \left(1 - \frac{1}{5}\right) = 360 \times \frac{1}{2} \times \frac{2}{3} \times \frac{4}{5} = \frac{360 \times 8}{30} = 96$$

**Interpretation**: Exactly 96 integers between 1 and 359 share no common factor with 360.

### 2.2 Primitive Root Check for $p = 7$, $g = 3$

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $3^k \bmod 7$ | 3 | 2 | 6 | 4 | 5 | 1 |

All 6 non-zero residues appear → **3 is a primitive root of 7**.

Check $g = 2$: $2^1=2, 2^2=4, 2^3=1 \pmod 7$. Order = 3 ≠ 6. **2 is NOT a primitive root of 7**.

---

## 3. Applications & Use Cases

1. **RSA Key Generation**: $\phi(n) = (p-1)(q-1)$ and the Extended Euclidean Algorithm compute $d = e^{-1} \bmod \phi(n)$. Euler's theorem guarantees $M^{ed} \equiv M \pmod n$, making decryption possible.

2. **Diffie-Hellman and DSA**: Security depends on the DLP in $\mathbb{Z}_p^*$. Primitive roots are used as generators so the discrete exponential map is a bijection over the entire group — maximizing the keyspace.

3. **Miller-Rabin Primality Test**: Generates the large primes $p, q$ needed by RSA. Based on Fermat's Little Theorem (false witnesses identified by repeated squaring), it runs in $O(k \log^2 n \log \log n)$ time.

4. **Chinese Remainder Theorem (CRT) Optimization**: RSA decryption using CRT decomposes $M = C^d \bmod n$ into $M_p = C^{d \bmod (p-1)} \bmod p$ and $M_q = C^{d \bmod (q-1)} \bmod q$, then reconstructs using Bézout coefficients. This gives a **4× speedup** over naive RSA decryption.

5. **Hash-based commitments**: Number-theoretic functions and quadratic residues form the basis of commitment schemes used in zero-knowledge proofs and blockchain voting systems.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Extended Euclidean Algorithm — Full Tabular Method [KTU May 2019, Q14(a)]

**Problem**: Find $\gcd(240, 46)$ and express it as a linear combination $240x + 46y = \gcd(240, 46)$.

**Step 1 — Forward Division (Euclidean)**:

| Step | Equation | Remainder |
|---|---|---|
| 1 | $240 = 5 \times 46 + 10$ | $r_1 = 10$ |
| 2 | $46 = 4 \times 10 + 6$ | $r_2 = 6$ |
| 3 | $10 = 1 \times 6 + 4$ | $r_3 = 4$ |
| 4 | $6 = 1 \times 4 + 2$ | $r_4 = 2$ |
| 5 | $4 = 2 \times 2 + 0$ | $r_5 = 0$ → stop |

$$\gcd(240, 46) = 2$$

**Step 2 — Backward Substitution**:

$$2 = 6 - 1 \times 4 \quad \text{(from Step 4)}$$

Substitute $4 = 10 - 1 \times 6$ (from Step 3):
$$2 = 6 - (10 - 6) = 2 \times 6 - 10$$

Substitute $6 = 46 - 4 \times 10$ (from Step 2):
$$2 = 2(46 - 4 \times 10) - 10 = 2 \times 46 - 9 \times 10$$

Substitute $10 = 240 - 5 \times 46$ (from Step 1):
$$2 = 2 \times 46 - 9(240 - 5 \times 46) = 2 \times 46 + 45 \times 46 - 9 \times 240$$

$$\boxed{2 = (-9) \times 240 + 47 \times 46}$$

**Verification**: $(-9)(240) + 47(46) = -2160 + 2162 = 2$ ✓

**Modular Inverse Check**: Since $\gcd(240, 46) = 2 \neq 1$, the modular inverse of $46 \bmod 240$ **does not exist** (non-coprime integers are not invertible).

---

### Example 2: Euclidean Algorithm for $\gcd(2740, 1760)$ [KTU June 2022, Q Part A]

| Step | Equation |
|---|---|
| 1 | $2740 = 1 \times 1760 + 980$ |
| 2 | $1760 = 1 \times 980 + 780$ |
| 3 | $980 = 1 \times 780 + 200$ |
| 4 | $780 = 3 \times 200 + 180$ |
| 5 | $200 = 1 \times 180 + 20$ |
| 6 | $180 = 9 \times 20 + 0$ |

$$\boxed{\gcd(2740, 1760) = 20}$$

---

### Example 3: Modular Exponentiation via Fermat's Little Theorem [KTU June 2022, Part A]

**Problem**: Evaluate (a) $1^{68} \bmod 73$ and (b) $5^{146} \bmod 73$.

**Setup**: $p = 73$ is prime. By Fermat: $a^{72} \equiv 1 \pmod{73}$ for $\gcd(a, 73) = 1$.

**(a) $1^{68} \bmod 73$**:
$$1^{68} = 1 \equiv \mathbf{1} \pmod{73}$$

**(b) $5^{146} \bmod 73$**:

Divide exponent by $p-1 = 72$:
$$146 = 2 \times 72 + 2 \implies 5^{146} = (5^{72})^2 \times 5^2$$

By Fermat's theorem: $5^{72} \equiv 1 \pmod{73}$

$$5^{146} \equiv 1^2 \times 25 \equiv \mathbf{25} \pmod{73}$$

---

### Example 4: Finding Modular Inverse using Extended Euclidean [Exam-Pattern Problem]

**Problem**: Find $17^{-1} \bmod 43$.

We need $17x \equiv 1 \pmod{43}$. Apply Extended Euclidean to $(43, 17)$:

| Step | Equation | Remainder |
|---|---|---|
| 1 | $43 = 2 \times 17 + 9$ | 9 |
| 2 | $17 = 1 \times 9 + 8$ | 8 |
| 3 | $9 = 1 \times 8 + 1$ | 1 |
| 4 | $8 = 8 \times 1 + 0$ | 0 → stop |

Back-substitute:
$$1 = 9 - 1 \times 8 = 9 - (17 - 9) = 2 \times 9 - 17 = 2(43 - 2 \times 17) - 17 = 2 \times 43 - 5 \times 17$$

$$-5 \times 17 \equiv 1 \pmod{43} \implies 17^{-1} \equiv -5 \equiv 38 \pmod{43}$$

**Verification**: $17 \times 38 = 646 = 15 \times 43 + 1 \equiv 1 \pmod{43}$ ✓

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q4 — 4 Marks]
**Question**: State and prove Fermat's Theorem.

**Solution**:

**Statement**: If $p$ is prime and $\gcd(a, p) = 1$, then $a^{p-1} \equiv 1 \pmod p$.

**Proof**:

Consider the set $S = \{1 \cdot a,\ 2 \cdot a,\ \dots,\ (p-1) \cdot a\} \pmod p$.

**Lemma 1 (No zeros)**: For any $k \in \{1, \dots, p-1\}$, $ka \not\equiv 0 \pmod p$.
*Proof*: If $ka \equiv 0 \pmod p$, then $p \mid ka$. Since $p$ is prime and $\gcd(a,p)=1$, Euclid's Lemma gives $p \mid k$. But $1 \le k \le p-1$, contradiction.

**Lemma 2 (All distinct)**: For $1 \le j < k \le p-1$, $ja \not\equiv ka \pmod p$.
*Proof*: If $ja \equiv ka \pmod p$, then $p \mid (k-j)a$. Since $\gcd(a,p)=1$, $p \mid (k-j)$. But $0 < k-j < p$, contradiction.

**Conclusion**: $S \pmod p$ is a permutation of $\{1, 2, \dots, p-1\}$.

Multiply all elements:
$$a^{p-1} \cdot (p-1)! \equiv (p-1)! \pmod p$$

Cancel $(p-1)!$ (valid since $\gcd((p-1)!, p) = 1$):
$$a^{p-1} \equiv 1 \pmod p \quad \square$$

---

### Question 2 [KTU May 2019, Part C, Q14(a) — 4 Marks]
**Question**: Find $\gcd(240, 46)$ using Extended Euclid's Algorithm.

**Solution**: (Full working shown in Example 1 above — reproduced in self-contained form below.)

**Division Steps**:
- $240 = 5 \times 46 + 10 \implies 10 = 240 - 5 \times 46$
- $46 = 4 \times 10 + 6 \implies 6 = 46 - 4 \times 10$
- $10 = 1 \times 6 + 4 \implies 4 = 10 - 1 \times 6$
- $6 = 1 \times 4 + 2 \implies 2 = 6 - 1 \times 4$
- $4 = 2 \times 2 + 0$ → last nonzero remainder is 2.

$$\gcd(240, 46) = 2$$

**Linear Combination**:
- $2 = 6 - 4 = 6 - (10 - 6) = 2(6) - 10$
- $= 2(46 - 4 \times 10) - 10 = 2 \times 46 - 9 \times 10$
- $= 2 \times 46 - 9(240 - 5 \times 46) = 47 \times 46 - 9 \times 240$

$$\mathbf{2 = 240 \times (-9) + 46 \times 47}$$

Coefficients: $x = -9,\ y = 47$. Since $\gcd(240, 46) = 2 \ne 1$, no multiplicative inverse exists for 46 modulo 240.

---

### Question 3 [KTU June 2022, Part C, Q16(b) — 5 Marks]
**Question**: Define Euler Totient Function. Prove that $\phi(pq) = (p-1)(q-1)$ for distinct primes $p, q$.

**Solution**:

**Definition**: $\phi(n)$ is the count of positive integers $k$ with $1 \le k \le n$ and $\gcd(k, n) = 1$:
$$\phi(n) = |\{k \in \mathbb{Z}^+ : 1 \le k \le n,\ \gcd(k,n) = 1\}|$$

**Proof of $\phi(pq) = (p-1)(q-1)$**:

Let $n = pq$ for distinct primes $p \ne q$.

The integers in $\{1, \dots, pq\}$ that are **NOT** coprime to $n$ must share a factor with $pq$. Since $p$ and $q$ are the only prime factors:

- **Multiples of $p$** in $\{1, \dots, pq\}$: $\{p, 2p, \dots, qp\}$ → count $= q$
- **Multiples of $q$** in $\{1, \dots, pq\}$: $\{q, 2q, \dots, pq\}$ → count $= p$
- **Multiples of both $pq$** (intersection): $\{pq\}$ → count $= 1$

By **Inclusion-Exclusion**:
$$|\text{not coprime}| = q + p - 1$$

Therefore:
$$\phi(pq) = pq - (p + q - 1) = pq - p - q + 1 = (p-1)(q-1) \quad \square$$

**Numerical check**: $p=5, q=7 \implies \phi(35) = 4 \times 6 = 24$.
Verify: integers coprime to 35 in $\{1,\dots,35\}$ — skip multiples of 5 (5,10,15,20,25,30,35) and multiples of 7 (7,14,21,28,35), avoiding double-counting 35. Count = 35 - 7 - 5 + 1 = 24. ✓

---

### Question 4 [KTU January 2023, Part A — 4 Marks]
**Question**: State Euler's theorem. Show how it is used in RSA cryptosystem.

**Solution**:

**Euler's Theorem Statement**: For any integer $a$ and positive integer $n$ with $\gcd(a, n) = 1$:
$$a^{\phi(n)} \equiv 1 \pmod n$$

**Application to RSA Correctness**:

In RSA, the public and private keys satisfy $e \cdot d \equiv 1 \pmod{\phi(n)}$, meaning:
$$ed = k \cdot \phi(n) + 1 \quad \text{for some integer } k \ge 1$$

**Proof of $M^{ed} \equiv M \pmod n$** (assuming $\gcd(M, n) = 1$):

$$M^{ed} = M^{k\phi(n)+1} = (M^{\phi(n)})^k \cdot M^1$$

By Euler's theorem (since $\gcd(M,n)=1$ and $\phi(n) = (p-1)(q-1)$):
$$M^{\phi(n)} \equiv 1 \pmod n$$

Therefore:
$$M^{ed} \equiv 1^k \cdot M = M \pmod n$$

**Conclusion**: Encryption $C = M^e \bmod n$ followed by decryption $C^d \bmod n$ exactly recovers $M$, because Euler's theorem guarantees that $M^{ed} \equiv M \pmod n$. This mathematical guarantee is the entire basis of RSA correctness.
