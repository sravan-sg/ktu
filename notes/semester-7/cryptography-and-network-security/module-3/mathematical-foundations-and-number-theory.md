# Mathematical Foundations and Number Theory

## 1. Explanation
Public-key (asymmetric) cryptography relies fundamentally on mathematical concepts from number theory and computational algebra. Unlike symmetric ciphers which rely on complex confusion-diffusion permutations, public-key schemes rely on computationally intractable algebraic problems (e.g., integer factorization, discrete logarithms, and elliptic curve discrete logarithms).

### Fundamental Theorem of Arithmetic
Every integer $n > 1$ can be uniquely represented as a product of prime numbers (up to the order of factors):
$$n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k} = \prod_{i=1}^k p_i^{e_i}$$
where $p_1 < p_2 < \dots < p_k$ are distinct prime numbers, and $e_i \ge 1$.

### Divisibility and Modular Arithmetic
- **Divisibility**: An integer $b$ divides $a$ (written $b \mid a$) if there exists an integer $c$ such that $a = b \cdot c$.
- **Congruence Modulo $n$**: Two integers $a$ and $b$ are congruent modulo $n$ (written $a \equiv b \pmod n$) if $n \mid (a - b)$.
- **Properties**:
  1. $a \equiv b \pmod n \iff (a \bmod n) = (b \bmod n)$
  2. $(a + b) \bmod n = [(a \bmod n) + (b \bmod n)] \bmod n$
  3. $(a \cdot b) \bmod n = [(a \bmod n) \cdot (b \bmod n)] \bmod n$

### Greatest Common Divisor ($\gcd$) & The Euclidean Algorithm
The $\gcd(a, b)$ is the largest integer dividing both $a$ and $b$. If $\gcd(a, b) = 1$, $a$ and $b$ are said to be **relatively prime (coprime)**.
The Euclidean Algorithm computes $\gcd(a, b)$ efficiently using repeated division with remainder:
$$\gcd(a, b) = \gcd(b, a \bmod b)$$

### Extended Euclidean Algorithm
Computes the greatest common divisor and simultaneously finds integer coefficients $x$ and $y$ (Bézout's identity) such that:
$$a \cdot x + b \cdot y = \gcd(a, b)$$
- **Application in Cryptography**: Used to calculate the modular multiplicative inverse of an integer $a$ modulo $m$.
  If $\gcd(a, m) = 1$, then:
  $$a \cdot x + m \cdot y = 1 \implies a \cdot x \equiv 1 \pmod m$$
  Thus, $x = a^{-1} \bmod m$.

### Euler's Totient Function $\phi(n)$
$\phi(n)$ is defined as the number of positive integers less than $n$ that are relatively prime to $n$:
$$\phi(n) = |\{a \in \mathbb{Z} : 1 \le a < n \text{ and } \gcd(a, n) = 1\}|$$
- **Properties**:
  1. For any prime $p$: $\phi(p) = p - 1$.
  2. For a prime power $p^k$: $\phi(p^k) = p^k - p^{k-1} = p^k \left(1 - \frac{1}{p}\right)$.
  3. **Multiplicative Property**: If $\gcd(a, b) = 1$, then $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$.
  4. For the product of two distinct primes $n = p \cdot q$:
     $$\phi(n) = \phi(p) \cdot \phi(q) = (p - 1)(q - 1)$$
  5. For any general integer $n = \prod p_i^{e_i}$:
     $$\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$$

### Fermat's Little Theorem
**Statement**: If $p$ is a prime number and $a$ is an integer such that $\gcd(a, p) = 1$ (i.e., $p \nmid a$), then:
$$a^{p-1} \equiv 1 \pmod p$$
An alternative formulation valid for all integers $a$:
$$a^p \equiv a \pmod p$$

**Mathematical Proof**:
1. Consider the set of multiples: $S = \{1a, 2a, 3a, \dots, (p-1)a\}$.
2. None of these elements is congruent to $0 \bmod p$ because $\gcd(a, p) = 1$ and $1 \le k \le p-1$.
3. All $(p-1)$ elements are mutually distinct modulo $p$. For if $j \cdot a \equiv k \cdot a \pmod p$ with $1 \le j < k \le p-1$, then $(k - j)a \equiv 0 \pmod p$. Since $\gcd(a, p) = 1$, this requires $p \mid (k - j)$, which is impossible since $0 < k - j < p$.
4. Therefore, the set of remainders of $S \bmod p$ is precisely a permutation of $\{1, 2, 3, \dots, p-1\}$.
5. Multiplying all elements together:
   $$\prod_{k=1}^{p-1} (k \cdot a) \equiv \prod_{k=1}^{p-1} k \pmod p$$
   $$a^{p-1} \cdot (p-1)! \equiv (p-1)! \pmod p$$
6. Since $\gcd((p-1)!, p) = 1$, we can cancel $(p-1)!$ from both sides:
   $$a^{p-1} \equiv 1 \pmod p$$
   Q.E.D.

### Euler's Theorem (Euler's Generalization)
**Statement**: For every integer $a$ and positive integer $n$ such that $\gcd(a, n) = 1$:
$$a^{\phi(n)} \equiv 1 \pmod n$$
- Notice that when $n$ is prime, $\phi(n) = p - 1$, and Euler's Theorem simplifies directly to Fermat's Little Theorem.
- An alternative formulation:
  $$a^{\phi(n) + 1} \equiv a \pmod n$$

### Primitive Roots and Discrete Logarithms
- An integer $g$ is a **primitive root** modulo $p$ if the powers of $g$:
  $$g^1 \bmod p, \ g^2 \bmod p, \ \dots, \ g^{p-1} \bmod p$$
  generate all distinct integers in the set $\{1, 2, \dots, p-1\}$. That is, the multiplicative order of $g$ modulo $p$ is $\text{ord}_p(g) = \phi(p) = p - 1$.
- **Discrete Logarithm Problem (DLP)**: Given $y \equiv g^x \pmod p$, finding the exponent $x = \text{dlog}_{g, p}(y)$ is computationally intractable for large primes ($p > 2048$ bits).

---

## 2. Example: Computing Euler's Totient $\phi(360)$
- Prime factorization of 360:
  $$360 = 36 \times 10 = (2^2 \times 3^2) \times (2 \times 5) = 2^3 \times 3^2 \times 5^1$$
- Applying Euler's totient formula:
  $$\phi(360) = 360 \times \left(1 - \frac{1}{2}\right) \times \left(1 - \frac{1}{3}\right) \times \left(1 - \frac{1}{5}\right)$$
  $$\phi(360) = 360 \times \frac{1}{2} \times \frac{2}{3} \times \frac{4}{5} = 360 \times \frac{8}{30} = 12 \times 8 = 96$$
- Exactly 96 numbers between 1 and 359 are coprime to 360.

---

## 3. Applications & Use Cases
1. **RSA Key Generation & Decryption**: Relies directly on Euler's Totient function $\phi(n) = (p-1)(q-1)$ and Euler's theorem to compute the private key $d \equiv e^{-1} \pmod{\phi(n)}$ and decrypt ciphertexts via $C^d \equiv M^{ed} \equiv M \pmod n$.
2. **Diffie-Hellman Key Exchange**: Uses the algebraic properties of primitive roots in finite multiplicative groups $\mathbb{Z}_p^*$ to establish shared secrets across insecure networks.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Extended Euclidean Algorithm [KTU May 2019]
**Problem**:
Find $\gcd(240, 46)$ and integer coefficients $x$ and $y$ such that $240x + 46y = \gcd(240, 46)$ using the Extended Euclidean Algorithm. Also find the modular inverse of $46 \bmod 240$ if it exists.

**Step-by-step Solution**:
1. **Forward Euclidean Division**:
   - Step 1: $240 = 46 \times 5 + 10$ (Quotient $q_1 = 5$, Remainder $r_1 = 10$)
   - Step 2: $46 = 10 \times 4 + 6$ (Quotient $q_2 = 4$, Remainder $r_2 = 6$)
   - Step 3: $10 = 6 \times 1 + 4$ (Quotient $q_3 = 1$, Remainder $r_3 = 4$)
   - Step 4: $6 = 4 \times 1 + 2$ (Quotient $q_4 = 1$, Remainder $r_4 = 2$)
   - Step 5: $4 = 2 \times 2 + 0$ (Quotient $q_5 = 2$, Remainder $r_5 = 0$)
   $$\gcd(240, 46) = 2$$
2. **Backward Substitution**:
   From Step 4:
   $$2 = 6 - 4 \times 1$$
   Substitute 4 from Step 3 ($4 = 10 - 6 \times 1$):
   $$2 = 6 - (10 - 6 \times 1) = 6 \times 2 - 10 \times 1$$
   Substitute 6 from Step 2 ($6 = 46 - 10 \times 4$):
   $$2 = (46 - 10 \times 4) \times 2 - 10 \times 1 = 46 \times 2 - 10 \times 9$$
   Substitute 10 from Step 1 ($10 = 240 - 46 \times 5$):
   $$2 = 46 \times 2 - (240 - 46 \times 5) \times 9 = 46 \times 2 - 240 \times 9 + 46 \times 45$$
   $$2 = 240 \times (-9) + 46 \times (47)$$
3. **Verification**:
   $$240 \times (-9) + 46 \times 47 = -2160 + 2162 = 2$$
   Coefficients: $x = -9$, $y = 47$.
4. **Modular Inverse Check**:
   Since $\gcd(240, 46) = 2 \neq 1$, $46$ and $240$ are not coprime. **Therefore, the modular multiplicative inverse of $46 \bmod 240$ does NOT exist.**

---

### Example 2: Euclidean Algorithm for $\gcd(2740, 1760)$ [KTU June 2022]
**Problem**:
Find $\gcd(2740, 1760)$ using the Euclidean Algorithm.

**Step-by-step Solution**:
- Step 1: $2740 = 1760 \times 1 + 980$
- Step 2: $1760 = 980 \times 1 + 780$
- Step 3: $980 = 780 \times 1 + 200$
- Step 4: $780 = 200 \times 3 + 180$
- Step 5: $200 = 180 \times 1 + 20$
- Step 6: $180 = 20 \times 9 + 0$
The last non-zero remainder is $20$.
$$\mathbf{\gcd(2740, 1760) = 20}$$

---

### Example 3: Modular Exponentiation using Fermat's Little Theorem [KTU June 2022]
**Problem**:
Evaluate $1^{68} \bmod 73$ and $5^{146} \bmod 73$ using Fermat's Little Theorem.

**Step-by-step Solution**:
1. Check if the modulus $p = 73$ is prime: $73$ is prime.
2. By Fermat's Little Theorem: for any integer $a$ coprime to $73$:
   $$a^{73 - 1} \equiv a^{72} \equiv 1 \pmod{73}$$
3. For $1^{68} \bmod 73$:
   $$1^{68} = 1 \equiv 1 \pmod{73}$$
4. For $5^{146} \bmod 73$:
   Divide exponent 146 by 72:
   $$146 = 72 \times 2 + 2$$
   $$5^{146} = (5^{72})^2 \times 5^2 \pmod{73}$$
   Since $5^{72} \equiv 1 \pmod{73}$:
   $$5^{146} \equiv (1)^2 \times 25 \equiv 25 \pmod{73}$$
   Result: $\mathbf{25}$.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q4 - 4 Marks]
**Question**: State and prove Fermat’s Theorem.

**Solution**:
1. **Statement of Fermat's Little Theorem**:
   If $p$ is a prime number and $a$ is any positive integer such that $\gcd(a, p) = 1$ (that is, $p$ does not divide $a$), then:
   $$a^{p-1} \equiv 1 \pmod p$$
   Equivalently, for any integer $a$:
   $$a^p \equiv a \pmod p$$

2. **Proof**:
   - Consider the sequence of the first $(p - 1)$ positive integers multiplied by $a$:
     $$S = \{1a, 2a, 3a, \dots, (p - 1)a\}$$
   - **Lemma 1: None of these values is congruent to 0 modulo $p$**:
     For any $k \in \{1, 2, \dots, p - 1\}$, $k \cdot a \equiv 0 \pmod p$ would imply $p \mid (k \cdot a)$. But $p$ is prime and $\gcd(a, p) = 1$, which would mean $p \mid k$, impossible since $1 \le k \le p - 1$.
   - **Lemma 2: All elements in $S$ are mutually incongruent modulo $p$**:
     Suppose for integers $j, k$ with $1 \le j < k \le p - 1$:
     $$j \cdot a \equiv k \cdot a \pmod p$$
     $$(k - j)a \equiv 0 \pmod p$$
     Because $\gcd(a, p) = 1$, Euclid's lemma requires $p \mid (k - j)$. But $0 < k - j < p$, so $p$ cannot divide $(k - j)$. This is a contradiction.
   - **Permutation of Residues**:
     Because all $(p - 1)$ values are non-zero and distinct modulo $p$, their remainders modulo $p$ must be a permutation of the set of integers $\{1, 2, 3, \dots, p - 1\}$.
   - **Multiplication of Residues**:
     Multiplying all $(p - 1)$ congruences together:
     $$(1a) \cdot (2a) \cdot (3a) \cdots ((p - 1)a) \equiv 1 \cdot 2 \cdot 3 \cdots (p - 1) \pmod p$$
     $$a^{p-1} \cdot (p - 1)! \equiv (p - 1)! \pmod p$$
   - Since $p$ is prime, every integer $1, 2, \dots, p - 1$ is relatively prime to $p$, meaning $\gcd((p - 1)!, p) = 1$.
   - Dividing both sides by $(p - 1)!$:
     $$a^{p-1} \equiv 1 \pmod p$$
   Hence proved.

---

### Question 2 [KTU May 2019, Part C, Q14(a) - 4 Marks]
**Question**: Find $\gcd(240, 46)$ using Extended Euclid’s Algorithm.

**Solution**:
1. **Division Steps**:
   - $240 = 5 \times 46 + 10$  $\implies 10 = 240 - 5 \times 46$
   - $46 = 4 \times 10 + 6$    $\implies 6 = 46 - 4 \times 10$
   - $10 = 1 \times 6 + 4$     $\implies 4 = 10 - 1 \times 6$
   - $6 = 1 \times 4 + 2$      $\implies 2 = 6 - 1 \times 4$
   - $4 = 2 \times 2 + 0$
   Since the last non-zero remainder is 2:
   $$\mathbf{\gcd(240, 46) = 2}$$

2. **Expressing $\gcd(240, 46)$ as a Linear Combination ($240x + 46y = 2$)**:
   - $2 = 6 - 1 \times 4$
   - Substitute $4 = 10 - 1 \times 6$:
     $$2 = 6 - (10 - 6) = 2 \times 6 - 10$$
   - Substitute $6 = 46 - 4 \times 10$:
     $$2 = 2 \times (46 - 4 \times 10) - 10 = 2 \times 46 - 9 \times 10$$
   - Substitute $10 = 240 - 5 \times 46$:
     $$2 = 2 \times 46 - 9 \times (240 - 5 \times 46) = 2 \times 46 - 9 \times 240 + 45 \times 46$$
     $$2 = 240 \times (-9) + 46 \times (47)$$
   Thus: $x = -9$, $y = 47$.

---

### Question 3 [KTU June 2022, Part C, Q16(b) - 5 Marks]
**Question**: Define Euler Totient Function. Prove that $\phi(pq) = (p - 1)(q - 1)$ where $p$ and $q$ are prime numbers.

**Solution**:
1. **Definition of Euler's Totient Function**:
   Euler's Totient Function, denoted $\phi(n)$, is an arithmetic function defined for every positive integer $n$ that counts the number of positive integers strictly less than $n$ that are relatively prime to $n$:
   $$\phi(n) = |\{k \in \mathbb{Z} : 1 \le k < n \text{ and } \gcd(k, n) = 1\}|$$

2. **Proof that $\phi(pq) = (p - 1)(q - 1)$ for Distinct Primes $p$ and $q$**:
   - Let $n = p \cdot q$ where $p$ and $q$ are distinct prime numbers ($p \neq q$).
   - The total number of integers in the range $\{1, 2, 3, \dots, pq\}$ is $pq$.
   - An integer $k$ in this range is **not** relatively prime to $n$ if and only if it shares a common factor with $n$. Since $p$ and $q$ are distinct primes, $k$ must be a multiple of $p$, a multiple of $q$, or both.
   - **Multiples of $p$**:
     The integers divisible by $p$ in $\{1 \dots pq\}$ are:
     $$\{1p, 2p, 3p, \dots, q \cdot p\}$$
     Total count of multiples of $p$ = $q$.
   - **Multiples of $q$**:
     The integers divisible by $q$ in $\{1 \dots pq\}$ are:
     $$\{1q, 2q, 3q, \dots, p \cdot q\}$$
     Total count of multiples of $q$ = $p$.
   - **Multiples of both $p$ and $q$**:
     Since $\gcd(p, q) = 1$, integers divisible by both $p$ and $q$ must be multiples of $p \cdot q$.
     In the range $\{1 \dots pq\}$, the only multiple of $pq$ is $pq$ itself.
     Total count of common multiples = $1$.
   - **Applying the Principle of Inclusion-Exclusion**:
     The count of integers in $\{1 \dots pq\}$ that are NOT relatively prime to $pq$ is:
     $$|M_p \cup M_q| = |M_p| + |M_q| - |M_p \cap M_q| = q + p - 1$$
   - **Computing $\phi(pq)$**:
     Subtracting the count of non-coprime integers from the total $pq$:
     $$\phi(pq) = pq - (p + q - 1) = pq - p - q + 1 = p(q - 1) - 1(q - 1)$$
     $$\mathbf{\phi(pq) = (p - 1)(q - 1)}$$
   Q.E.D.
