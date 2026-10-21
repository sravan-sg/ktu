# Cryptographic Hash Functions: MD5 and SHA-1

## 1. Explanation

### 1.1 What Is a Cryptographic Hash Function? — Deep Intuition

A **cryptographic hash function** $H$ is a mathematical algorithm that collapses an arbitrarily large message $M$ into a compact, fixed-size **fingerprint** $h = H(M)$ called the **message digest** or **hash value**.

The core intuition: a good hash function is a **one-way blender**. You can easily blend a message into its digest — but you cannot reconstruct the original message from the digest, nor can you find a different message that blends into the same digest. This one-wayness, combined with determinism, is what makes hash functions cryptographically useful.

**Contrast with encryption**:
| Property | Encryption | Hash Function |
|---|---|---|
| Key | Yes (symmetric or asymmetric) | None (public function) |
| Reversibility | Yes ($D_K(E_K(M)) = M$) | No (one-way; $H^{-1}(h)$ infeasible) |
| Variable input | Yes | Yes |
| Fixed output | No (ciphertext ≈ plaintext size) | Yes |
| Secrecy | Requires key | Public; no secrets |

**Why the fixed-size output matters**: A 256-bit digest represents any message — a 1-byte ping packet or a 10 GB movie file — with equal-sized output. This enables:
- Comparing huge files by comparing 32 bytes
- Signing documents by signing a 32-byte digest rather than the document itself
- Committing to a value without revealing it (hash commitment)

---

### 1.2 Six Essential Requirements for Cryptographic Hash Functions

Stallings (*CNS*, Chapter 11) defines the six properties a hash function $H$ must satisfy to be cryptographically secure:

| # | Property | Formal Definition | Security Implication |
|---|---|---|---|
| 1 | **Variable Input Size** | $H$ accepts input of any length $\|M\|$ | Practical: handles any message |
| 2 | **Fixed Output Size** | $H(M)$ is always $m$ bits long | Enables efficient comparison |
| 3 | **Efficiency** | $H(x)$ is fast to compute for any $x$ | Must not be a performance bottleneck |
| 4 | **Pre-image Resistance** (One-Way) | Given $h$, infeasible to find any $x$ with $H(x) = h$ | Protects against inverting hash to recover message |
| 5 | **Second Pre-image Resistance** (Weak Collision Resistance) | Given $x$, infeasible to find $y \ne x$ with $H(y) = H(x)$ | Prevents forging a substitute for a known document |
| 6 | **Collision Resistance** (Strong Collision Resistance) | Infeasible to find *any* pair $(x, y)$ with $x \ne y$ and $H(x) = H(y)$ | Prevents birthday attacks on digital signature schemes |

**The distinction between 5 and 6** is subtle but critical:

- **Second pre-image resistance** (property 5): I give you a specific message $M$; find any other message $M'$ that hashes to the same value. The attacker's starting point is fixed. Complexity: $O(2^m)$.
- **Collision resistance** (property 6): Find *any* pair $(M, M')$ with $H(M) = H(M')$. The attacker can choose both messages freely. Complexity: $O(2^{m/2})$ due to the Birthday Paradox.

**Why property 6 is harder to satisfy**: The Birthday Paradox dramatically reduces the search space for collision finding. Property 6 requires $m/2$ more bits of output than property 5 for the same security level.

---

### 1.3 The Birthday Paradox and Birthday Attack

#### The Statistical Foundation

**Birthday Paradox**: In a group of just 23 people, the probability that at least two share a birthday exceeds 50% — despite 365 possible birthdays. This counterintuitive result occurs because we're asking about *any* pair, not a specific match.

**Formal derivation**:
The probability that $k$ randomly chosen elements from a set of $N$ are all distinct:
$$P(\text{no collision}) = \prod_{i=0}^{k-1}\left(1 - \frac{i}{N}\right) \approx e^{-k^2/(2N)}$$

Setting $P(\text{collision}) = 1 - e^{-k^2/(2N)} \ge 0.5$:
$$e^{-k^2/(2N)} \le 0.5 \implies k^2 \ge 2N \ln 2 \implies k \ge \sqrt{2N \ln 2} \approx 1.177\sqrt{N}$$

#### Birthday Attack on Hash Functions

For a hash function with $m$-bit output, there are $N = 2^m$ possible digests. To find a collision with probability $\ge 50\%$:
$$k \approx 1.177 \times \sqrt{2^m} = 1.177 \times 2^{m/2}$$

**Practical consequences**:

| Hash | Digest Size ($m$) | Collision Attack Work | Status |
|---|---|---|---|
| MD5 | 128 bits | $2^{64}$ hash computations | **Broken** (practical in minutes, 2004) |
| SHA-1 | 160 bits | $2^{80}$ hash computations | **Broken** (SHAttered, 2017: $2^{63.1}$) |
| SHA-256 | 256 bits | $2^{128}$ hash computations | Secure |
| SHA-3 (Keccak) | 256 bits | $2^{128}$ hash computations | Secure |

**Real collision found**: In 2017, CWI Amsterdam and Google produced two PDF documents with identical SHA-1 hashes (the **SHAttered attack**) — demonstrating that SHA-1 is completely broken for collision resistance. Git's object model (which uses SHA-1) is now migrating to SHA-256.

#### Birthday Attack on Digital Signatures

The birthday attack motivates why digital signatures must use long-enough hash functions. If an attacker can generate $2^{80}$ document variants of a "good" contract and $2^{80}$ variants of a "malicious" contract, the birthday paradox guarantees a collision with 50% probability — and the attacker gets the victim to sign the "good" version while fraudulently applying the signature to the "malicious" version.

**Mitigation**: Use SHA-256 or SHA-3 (256-bit minimum) for all digital signature schemes. SHA-1 must not be used for new signatures.

---

### 1.4 The Merkle-Damgård Construction

Both MD5 and SHA-1 follow the **Merkle-Damgård** iterated construction for building hash functions from smaller **compression functions**:

```
Message M (padded to multiple of block size)
       │
       ├── M₁ ──► [  f  ] ──► CV₁
       │          ▲
       │         IV
       │
       ├── M₂ ──► [  f  ] ──► CV₂
       │          ▲
       │         CV₁
       │
      ...
       │
       └── Mₗ ──► [  f  ] ──► Final Hash h = H(M)
                  ▲
                 CV_{L-1}
```

Where:
- $IV$ = Initialization Vector (fixed constant)
- $M_i$ = $i$-th message block (512 bits for MD5 and SHA-1)
- $f$ = compression function mapping $(CV_{i-1}, M_i) \to CV_i$
- $CV_i$ = Chaining Variable (running state after block $i$)

**Merkle-Damgård security theorem**: If the compression function $f$ is collision-resistant, the full iterated hash $H$ is also collision-resistant.

**Length Strengthening (Merkle-Damgård Strengthening)**: The last block always includes a 64-bit encoding of the **original message length** (before padding). This prevents **length extension attacks** from trivially exploiting the internal structure by appending blocks — the length field would mismatch.

**Why Merkle-Damgård is still vulnerable to length extension**: Despite the length field, $H(K \| M)$ (secret-prefix MAC) is still vulnerable because an attacker who knows $H(K \| M) = h$ can compute $H(K \| M \| \text{pad} \| M')$ by initializing the compression function at state $h$ and appending new blocks. This is why HMAC uses the nested two-pass construction instead.

---

### 1.5 MD5 Message Digest Algorithm (RFC 1321)

**Designed by**: Ron Rivest, 1991. **Produces**: 128-bit digest. **Processes**: 512-bit blocks.

**Security status**: **BROKEN** — practical chosen-prefix collision attacks in seconds. Do not use for security. Legacy use in checksums (non-security applications) persists.

#### 1.5.1 MD5 Input Preparation (Steps 1–2)

**Step 1 — Append Padding Bits**:

The message is padded to length $\equiv 448 \pmod{512}$ bits:
- Append a single `1` bit.
- Append `0` bits until length $\equiv 448 \pmod{512}$.
- Padding always occurs (even if already $\equiv 448$: add 512 bits of padding).
- Total padding: 1 to 512 bits.

**Step 2 — Append 64-bit Length**:

Append the **original message length** modulo $2^{64}$ as a 64-bit little-endian integer. After this step, total length is an exact multiple of 512 bits: $N \times 512$ bits.

**Padding Example**: Message of 1000 bits.
- Need length $\equiv 448 \pmod{512}$.
- $1000 + 1 = 1001$ bits after the `1` bit.
- $1001 \bmod 512 = 489$.
- Need $448 - 489 = -41 \equiv 471 \pmod{512}$ zero bits.
- After padding: $1000 + 1 + 471 = 1472$ bits.
- After length: $1472 + 64 = 1536 = 3 \times 512$ bits → **3 blocks**.

#### 1.5.2 MD5 Buffer Initialization (Step 3)

A 128-bit buffer represented by four 32-bit registers $(A, B, C, D)$ initialized to little-endian fixed constants:
$$A = \texttt{0x67452301},\quad B = \texttt{0xEFCDAB89},\quad C = \texttt{0x98BADCFE},\quad D = \texttt{0x10325476}$$

These initialization constants were chosen to provide a balanced starting state with no obvious mathematical structure that could be exploited.

#### 1.5.3 MD5 Compression Function — 4 Rounds of 16 Steps (Step 4)

Each 512-bit block $Y_q$ is split into sixteen 32-bit sub-words $X[0 \dots 15]$.

The compression function applies **4 rounds of 16 steps** (64 steps total). Each round uses a different non-linear **auxiliary function**:

| Round | Steps | Auxiliary Function $F$ | Purpose |
|---|---|---|---|
| 1 | 0–15 | $F(B,C,D) = (B \wedge C) \vee (\neg B \wedge D)$ | "If B then C else D" — conditional selection |
| 2 | 16–31 | $G(B,C,D) = (B \wedge D) \vee (C \wedge \neg D)$ | Different conditional selection |
| 3 | 32–47 | $H(B,C,D) = B \oplus C \oplus D$ | XOR parity |
| 4 | 48–63 | $I(B,C,D) = C \oplus (B \vee \neg D)$ | Majority variant |

**Single Step Operation** (register update):
$$A = B + \Big((A + \text{Func}(B,C,D) + X[k] + T[i]) \lll s\Big)$$

After each step, registers rotate cyclically: $(A, B, C, D) \leftarrow (D, A, B, C)$.

**Where**:
- $+$ = addition modulo $2^{32}$
- $\lll s$ = circular left shift by $s$ bits (different $s$ for each step)
- $X[k]$ = 32-bit word from current block (access pattern differs per round)
- $T[i] = \lfloor 2^{32} \cdot |\sin(i)| \rfloor$ = sine-derived table constant for step $i$

**Round 1 message word order** (sequential): $X[0], X[1], \dots, X[15]$
**Round 2 message word order** (stride 5): $X[1], X[6], X[11], X[0], X[5], \dots$
**Round 3 message word order** (stride 3): $X[5], X[8], X[11], X[14], \dots$
**Round 4 message word order** (stride 7): $X[0], X[7], X[14], X[5], \dots$

**Why the sine constants?** The values $T[i] = \lfloor 2^{32} |\sin(i)| \rfloor$ provide pseudo-random constants with no special mathematical structure — preventing "nothing-up-my-sleeve" attacks where fixed constants might hide trapdoors.

#### 1.5.4 MD5 Additive Chaining and Output (Step 5)

After all 64 steps process block $Y_q$, the output is added to the **input values** of the block (not to the previous chaining variable $CV_{q-1}$, but to the values $A, B, C, D$ at the *start of processing block $q$*):

$$CV_q.A = A + CV_{q-1}.A \pmod{2^{32}}$$
$$CV_q.B = B + CV_{q-1}.B \pmod{2^{32}}$$
$$CV_q.C = C + CV_{q-1}.C \pmod{2^{32}}$$
$$CV_q.D = D + CV_{q-1}.D \pmod{2^{32}}$$

After processing all $L$ blocks: concatenate the four 32-bit words $A \| B \| C \| D$ in **little-endian** order to produce the **128-bit MD5 digest**.

**Why additive chaining?** The additive step ensures that even if an adversary can invert the compression function steps, they cannot propagate backward through the chaining without knowing all intermediate states. It provides the "Davies-Meyer" feed-forward design.

---

### 1.6 SHA-1 (Secure Hash Algorithm 1)

**Designed by**: NIST/NSA, 1995. **Standard**: FIPS PUB 180-1. **Produces**: 160-bit digest. **Processes**: 512-bit blocks.

**Security status**: **BROKEN** for collision resistance (SHAttered, 2017). Deprecated by NIST since 2011. Still used in legacy systems (TLS 1.2, Git). Must not be used for new systems requiring collision resistance.

#### 1.6.1 SHA-1 Differences from MD5

| Feature | MD5 | SHA-1 |
|---|---|---|
| Digest length | 128 bits | 160 bits |
| Registers | 4 × 32-bit ($A,B,C,D$) | 5 × 32-bit ($A,B,C,D,E$) |
| Steps | 64 (4 rounds × 16) | 80 (4 rounds × 20) |
| Message schedule | Reuses 16 words directly | Expands 16 → 80 words (LSFR recurrence) |
| Constants | 64 sine-derived values $T[i]$ | 4 round constants $K_t$ |
| Shift direction | Left shift (variable) | Left shift (fixed 5 and 30) |
| Output endianness | Little-endian | Big-endian |
| Chaining | Davies-Meyer add | Davies-Meyer add |

#### 1.6.2 SHA-1 Input Preparation (Steps 1–2)

**Identical to MD5** but the 64-bit length field is stored in **big-endian** format.

#### 1.6.3 SHA-1 Buffer Initialization (Step 3)

Five 32-bit registers $(A, B, C, D, E)$ initialized to big-endian constants:
$$A = \texttt{0x67452301},\quad B = \texttt{0xEFCDAB89},\quad C = \texttt{0x98BADCFE}$$
$$D = \texttt{0x10325476},\quad E = \texttt{0xC3D2E1F0}$$

Note: $A, B, C, D$ share the same initialization values as MD5; $E$ is the extra register.

#### 1.6.4 SHA-1 Message Schedule — Word Expansion (Step 4)

This is SHA-1's key differentiator from MD5. The sixteen 32-bit message words $W_0, \dots, W_{15}$ from the 512-bit block are **expanded** into 80 words using a linear recurrence:

$$W_t = (W_{t-3} \oplus W_{t-8} \oplus W_{t-14} \oplus W_{t-16}) \lll 1 \quad \text{for } 16 \le t \le 79$$

**Why expand to 80 words?** The linear expansion (an LFSR) ensures that all 80 steps are influenced by all 16 original message words, providing better **avalanche** (bit mixing) than MD5's direct word reuse. In SHA-2, this expansion uses additional XOR terms and rotations for even stronger mixing.

**SHA-256 improvement over SHA-1's schedule**: SHA-256 uses:
$$W_t = \sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16}$$
where $\sigma_0, \sigma_1$ are nonlinear word operations — providing much better diffusion than SHA-1's simple XOR+rotate.

#### 1.6.5 SHA-1 Compression Function — 4 Rounds of 20 Steps (Step 5)

| Round | Steps | Logical Function $f_t$ | Constant $K_t$ |
|---|---|---|---|
| 1 | 0–19 | $f_t = (B \wedge C) \vee (\neg B \wedge D)$ | `0x5A827999` $= \lfloor 2^{30} \sqrt{2} \rfloor$ |
| 2 | 20–39 | $f_t = B \oplus C \oplus D$ | `0x6ED9EBA1` $= \lfloor 2^{30} \sqrt{3} \rfloor$ |
| 3 | 40–59 | $f_t = (B \wedge C) \vee (B \wedge D) \vee (C \wedge D)$ | `0x8F1BBCDC` $= \lfloor 2^{30} \sqrt{5} \rfloor$ |
| 4 | 60–79 | $f_t = B \oplus C \oplus D$ | `0xCA62C1D6` $= \lfloor 2^{30} \sqrt{10} \rfloor$ |

The constants are the fractional parts of square roots of small primes scaled to $2^{30}$ — **nothing-up-my-sleeve numbers** that provide mathematical legitimacy.

**Round 3 function** $(B \wedge C) \vee (B \wedge D) \vee (C \wedge D)$ is the **majority function**: returns the majority bit among $B, C, D$. This differs from Round 1 and introduces a new non-linear structure.

**Step Update Equation**:
$$TEMP = (A \lll 5) + f_t(B,C,D) + E + W_t + K_t \pmod{2^{32}}$$
$$E = D$$
$$D = C$$
$$C = B \lll 30$$
$$B = A$$
$$A = TEMP$$

**Key difference from MD5**: SHA-1 rotates register $B$ by 30 bits (fixed), while MD5 uses variable left shifts per step. The 5-bit rotation in the $A$ update creates a fixed **5-bit diffusion fan** each round.

#### 1.6.6 SHA-1 Chaining and Output (Step 6)

After 80 steps, add the output registers to their initial values for that block (modulo $2^{32}$):
$$CV_q.A = A + CV_{q-1}.A,\quad \dots,\quad CV_q.E = E + CV_{q-1}.E \pmod{2^{32}}$$

After all $L$ blocks: concatenate $A \| B \| C \| D \| E$ in **big-endian** to produce the **160-bit SHA-1 digest**.

---

### 1.7 Comparative Analysis: MD5 vs SHA Family

| Feature | MD5 | SHA-1 | SHA-256 | SHA-3 (Keccak) |
|---|---|---|---|---|
| **Year** | 1991 | 1995 | 2001 | 2015 |
| **Digest bits** | 128 | 160 | 256 | 256 (variable) |
| **Block size** | 512 bits | 512 bits | 512 bits | 1088 bits (r for 256) |
| **State size** | 128 bits | 160 bits | 256 bits | 1600 bits |
| **Rounds/Steps** | 64 | 80 | 64 | 24 |
| **Pre-image** | Theoretically broken | Theoretically 2^161 | $2^{256}$ | $2^{256}$ |
| **Collision** | **Broken** (seconds) | **Broken** ($2^{63.1}$) | $2^{128}$ | $2^{128}$ |
| **Speed** | Fastest | Fast | ~50% of MD5 speed | Sponge — different |
| **Construction** | Merkle-Damgård | Merkle-Damgård | Merkle-Damgård | Sponge |
| **Status** | **Deprecated** | **Deprecated** | **Recommended** | **Recommended** |

**SHA-3 Design Philosophy** (Keccak, selected 2012): Uses a completely different **sponge construction** — not Merkle-Damgård — providing inherent resistance to length extension attacks without requiring HMAC-style double hashing.

---

### 1.8 Security Analysis and Known Attacks

#### MD5 Weaknesses

1. **Wang-Feng-Lai-Yu Collision Attack (2004)**: First practical collision attack on MD5 (published at CRYPTO 2004). Found two 1024-bit messages with identical MD5 hashes in under 1 hour on standard hardware.
2. **Chosen-Prefix Collisions**: By 2008, researchers created two different SSL certificates with the same MD5 hash — enabling a fraudulent CA certificate. Demonstrated by Sotirov et al. at 25C3.
3. **Flame malware (2012)**: Nation-state malware forged a Microsoft code-signing certificate using a real-time MD5 chosen-prefix collision on the Windows update infrastructure.
4. **Speed**: MD5 runs at ~8 GB/s on modern GPUs — making rainbow table and preimage attacks extremely fast.

#### SHA-1 Weaknesses

1. **Theoretical weaknesses (Wang et al., 2005)**: Differential cryptanalysis reduced SHA-1 collision search from $2^{80}$ (birthday bound) to $2^{69}$ — a factor of 2000 improvement.
2. **Subsequent improvements**: By 2012, estimated at $2^{61}$ operations.
3. **SHAttered Attack (2017)**: CWI Amsterdam and Google found a practical SHA-1 collision using $\approx 2^{63.1}$ SHA-1 evaluations — 100,000 GPU-hours. Produced two PDF documents with identical SHA-1 hashes.
4. **Impact**: Git (which indexes commits by SHA-1) has been updating to SHA-256. GitHub, Subversion, and other SHA-1-dependent systems required updates.

#### Why SHA-256 Remains Secure

SHA-256's message schedule uses nonlinear word operations ($\sigma_0, \sigma_1$) rather than SHA-1's simple XOR+rotate, breaking the linear algebraic structure that Wang et al. exploited. No collision attacks are known against SHA-256. NIST recommends SHA-256 as the minimum for new systems.

---

## 2. Example: Merkle-Damgård Construction Flow

```
Padded Message: M₁ ‖ M₂ ‖ M₃   (each 512 bits)

IV ──► [  f  ] ──► CV₁ ──► [  f  ] ──► CV₂ ──► [  f  ] ──► h = H(M)
        ▲ M₁               ▲ M₂               ▲ M₃

f: one-way compression function mapping (512-bit block, 128-bit or 160-bit state) → (new state)
```

**Key properties**:
- **Cascading**: Each block's output feeds the next block's input — corruption of any block changes all subsequent outputs.
- **Avalanche**: A 1-bit change in any input block propagates through all subsequent compression rounds to affect approximately half the bits of the final digest.
- **Length strengthening**: The final block always encodes the original message length — different-length messages with the same prefix produce different hashes.

---

## 3. Applications & Use Cases

1. **Git Version Control (SHA-1 → SHA-256 migration)**: Git uses hash values as the primary keys for all objects (commits, trees, blobs). SHA-1's deprecation after SHAttered forced the Git community to implement SHA-256 support (git 2.29+). Historical repositories use SHA-1; all new repositories should use SHA-256.

2. **Digital Signatures (RSA-PSS-SHA256, ECDSA-SHA256)**: Hash functions are used to "compress" documents before signing. A 4 MB PDF is hashed to 32 bytes; RSA signs those 32 bytes. Without hashing, RSA could only sign messages shorter than its key size.

3. **Password Hashing (NOT MD5/SHA-1)**: Raw MD5/SHA-1 are broken for password storage. Proper password hashing requires **deliberately slow** functions: bcrypt (cost-adjusted), scrypt (memory-hard), or Argon2 (2015 PHC winner). These are built to resist GPU-accelerated dictionary attacks.

4. **Certificate Transparency (SHA-256 Merkle Trees)**: Browser certificate trust is audited using Merkle trees of SHA-256 hashes. The Certificate Transparency log structure is a hash tree where each parent = SHA-256(left_child ‖ right_child), enabling $O(\log n)$ inclusion proofs.

5. **Blockchain Hash Chains**: Bitcoin uses SHA-256d (double SHA-256) for block hashes and Merkle trees. Ethereum uses Keccak-256 (SHA-3 variant) for state trees. The hash chain property ensures that altering any historical block invalidates all subsequent block hashes.

6. **Intrusion Detection / File Integrity Monitoring (AIDE, Tripwire)**: Security tools store SHA-256 hashes of system files at a known-good state and periodically recompute to detect unauthorized modifications. Rootkits cannot hide file modifications if the hash database is stored offline.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Message Padding Calculation for SHA-1 [KTU Exam Pattern]

**Problem**: A message has a length of 1000 bits. Compute:
(a) The number of padding bits added.
(b) The total number of 512-bit blocks produced.

**Setup**: SHA-1 requires padded length $\equiv 448 \pmod{512}$.

**Part (a) — Padding bits**:

After appending the `1` bit: $1000 + 1 = 1001$ bits.

Find $P$ (zero-bits) such that $(1001 + P) \equiv 448 \pmod{512}$:

$$1001 \bmod 512 = 1001 - 512 = 489$$
$$489 + P \equiv 448 \pmod{512}$$
$$P \equiv 448 - 489 \equiv -41 \equiv 471 \pmod{512}$$

**Number of padding bits (zeros): $P = 471$**

Total after padding step: $1000 + 1 + 471 = 1472$ bits.

**Part (b) — Number of 512-bit blocks**:

After appending 64-bit length field: $1472 + 64 = 1536$ bits.

$$\text{Number of blocks} = \frac{1536}{512} = \mathbf{3 \text{ blocks}}$$

**Verify**: $3 \times 512 = 1536$ bits. ✓

---

### Example 2: Birthday Attack Computation [KTU Exam Pattern]

**Problem**: How many random messages must be hashed to find an MD5 collision with probability $\ge 50\%$? How long at $10^9$ hashes/second?

**Solution**:

**Formula**: $k \approx 1.177 \times 2^{m/2}$ where $m = 128$ (MD5 digest size).

$$k \approx 1.177 \times 2^{64} \approx 1.177 \times 1.844 \times 10^{19} \approx 2.17 \times 10^{19} \text{ hashes}$$

**Time at $10^9$ hashes/second**:
$$t = \frac{2.17 \times 10^{19}}{10^9} = 2.17 \times 10^{10} \text{ seconds} \approx 688 \text{ years}$$

But with $10^{13}$ hashes/second (modern GPU cluster):
$$t = \frac{2.17 \times 10^{19}}{10^{13}} = 2.17 \times 10^6 \text{ seconds} \approx 25 \text{ days}$$

In practice, Wang et al. (2004) found collisions much faster (in hours) by exploiting **differential properties** of MD5 — the birthday attack is the worst-case theoretical bound, not the actual attack complexity.

**SHA-1 ($m = 160$ bits)**:
$$k \approx 1.177 \times 2^{80} \approx 1.42 \times 10^{24} \text{ hashes}$$

SHAttered (2017) used $\approx 2^{63.1}$ evaluations — dramatically less than the $2^{80}$ birthday bound — by exploiting differential characteristics in SHA-1's compression function.

---

### Example 3: MD5 vs SHA-1 Comparative Analysis [KTU June 2022, Q5]

**Problem**: Summarize key differences between MD5 and SHA-1.

| Feature | MD5 | SHA-1 |
|---|---|---|
| **Designed by** | Ron Rivest (1991, RFC 1321) | NIST/NSA (1995, FIPS 180-1) |
| **Digest Size** | 128 bits | 160 bits |
| **Registers** | 4 × 32-bit (A, B, C, D) | 5 × 32-bit (A, B, C, D, E) |
| **Block Size** | 512 bits | 512 bits |
| **Processing Steps** | 64 steps (4 rounds × 16) | 80 steps (4 rounds × 20) |
| **Message Schedule** | 16 words reused directly per round | 16 words expanded to 80 via LFSR recurrence |
| **Round Constants** | 64 sine-based values $T[i]$ | 4 square-root constants $K_t$ |
| **Output Endianness** | Little-endian | Big-endian |
| **Collision Resistance** | **Broken**: practical in seconds | **Broken**: $2^{63.1}$ ops (SHAttered 2017) |
| **Pre-image Resistance** | Theoretically broken | $2^{161.0}$ (still $>2^{160}$) |
| **Speed** | Faster | ~80% of MD5 speed |
| **Status** | **Do not use** | **Deprecated; migrate to SHA-256** |

---

### Example 4: SHA-1 Step Calculation (Exam-Pattern Manual Trace)

**Problem**: For the first step ($t=0$) of SHA-1 Round 1, given:
$A = \texttt{0x67452301}$, $B = \texttt{0xEFCDAB89}$, $C = \texttt{0x98BADCFE}$, $D = \texttt{0x10325476}$, $E = \texttt{0xC3D2E1F0}$, $W_0 = \texttt{0x61626364}$, $K_0 = \texttt{0x5A827999}$.

Compute $TEMP$ and the new register values.

**Step 1 — Round 1 function**:
$$f_0(B,C,D) = (B \wedge C) \vee (\neg B \wedge D)$$
$B = \texttt{0xEFCDAB89}$, $C = \texttt{0x98BADCFE}$, $D = \texttt{0x10325476}$:
- $B \wedge C = \texttt{0x88884888}$
- $\neg B = \texttt{0x10325476}$, $\neg B \wedge D = \texttt{0x00000476}$
- $f_0 = \texttt{0x88884888} \vee \texttt{0x00000476} = \texttt{0x888848CE}$

**Step 2 — Compute TEMP**:
$$TEMP = (A \lll 5) + f_0(B,C,D) + E + W_0 + K_0 \pmod{2^{32}}$$

- $A \lll 5$: $A = \texttt{0x67452301}$. Shift left 5: $\texttt{0xE8A46020} + (\texttt{0x67452301} \gg 27)$ = $\texttt{0xE8A46023}$... (exact computation skipped for brevity; result: $\texttt{0xE8A46023}$)

**Step 3 — Update registers**:
$$E' = D = \texttt{0x10325476}$$
$$D' = C = \texttt{0x98BADCFE}$$
$$C' = B \lll 30 = \texttt{0xBF36AE22}$$
$$B' = A = \texttt{0x67452301}$$
$$A' = TEMP$$

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part C, Q15 — 9 Marks]
**Question**: Illustrate MD5 hash algorithm in detail.

**Solution**:

**1. Overview**: MD5 (Message Digest 5) by Ron Rivest (1991) produces a **128-bit digest** from any input message. It processes 512-bit blocks using an iterated Merkle-Damgård compression structure with 4 rounds of 16 steps each.

**2. Algorithm Flow**:
```
Input Message (any length)
        │
        ▼
[ Step 1: Pad to ≡ 448 (mod 512) bits ]
   (Append '1' bit, then '0' bits)
        │
        ▼
[ Step 2: Append 64-bit original length ]
   (Total length = multiple of 512 bits)
        │
        ▼
[ Step 3: Initialize 4 Registers (A,B,C,D) ]
   A=0x67452301  B=0xEFCDAB89
   C=0x98BADCFE  D=0x10325476
        │
        ▼ for each 512-bit block Y_q
[ Step 4: Apply 64-step Compression ]
   4 Rounds × 16 steps each:
   Round 1: F(B,C,D) = (B∧C)∨(¬B∧D)
   Round 2: G(B,C,D) = (B∧D)∨(C∧¬D)
   Round 3: H(B,C,D) = B⊕C⊕D
   Round 4: I(B,C,D) = C⊕(B∨¬D)
   Step: A = B + ((A+F(B,C,D)+X[k]+T[i]) <<< s)
   Then: (A,B,C,D) ← (D,A,B,C)
   After block: Add results to input registers
        │
        ▼
[ Step 5: Output A‖B‖C‖D (little-endian) ]
   128-bit MD5 Digest
```

**3. Detailed Steps**:

**Step 1 (Padding)**: Message padded so length $\equiv 448 \pmod{512}$ bits. Padding = single `1` bit followed by `0` bits. Minimum 1 bit, maximum 512 bits padding.

**Step 2 (Length Field)**: Append original message length (mod $2^{64}$) as 64-bit little-endian integer. Total length becomes a multiple of 512.

**Step 3 (Buffer Init)**: Four 32-bit words $A, B, C, D$ set to above hex constants.

**Step 4 (Compression)**:
- Each 512-bit block split into sixteen 32-bit words $X[0..15]$.
- 4 rounds × 16 steps = 64 steps.
- Each step: $A = B + ((A + \text{Func}(B,C,D) + X[k] + T[i]) \lll s)$, then cyclic rotation.
- After block complete: $A += A_{\text{prev}}$, $B += B_{\text{prev}}$, $C += C_{\text{prev}}$, $D += D_{\text{prev}}$ (mod $2^{32}$).

**Step 5 (Output)**: After all blocks, concatenate $A \| B \| C \| D$ in little-endian byte order → 128-bit digest.

**Security**: MD5 is cryptographically broken. Practical chosen-prefix collision attacks produce collisions in seconds on modern hardware. Do not use for security-critical applications.

---

### Question 2 [KTU June 2022, Part A, Q5 — 4 Marks]
**Question**: What are the requirements of a good hash function?

**Solution**:

A cryptographic hash function $H$ must satisfy **six core requirements**:

**1. Variable Input Length**: $H$ must accept input $M$ of any length — from 0 bits to several gigabytes.

**2. Fixed Output Length**: $H$ must always produce an $m$-bit output regardless of input length. (MD5: 128 bits, SHA-1: 160 bits, SHA-256: 256 bits.)

**3. Efficiency**: For any input $x$, $H(x)$ must be fast to compute in both hardware and software. Hash functions are widely deployed in high-throughput systems.

**4. Pre-image Resistance (One-Way Property)**: Given only a hash $h = H(x)$, it must be computationally infeasible to find any $x$ satisfying $H(x) = h$. Complexity: $O(2^m)$ for brute force.

*Why critical*: If reversible, digital signatures could be forged by finding a message that hashes to the target value.

**5. Second Pre-image Resistance (Weak Collision Resistance)**: Given a specific input $x$, it must be computationally infeasible to find any different input $y \ne x$ such that $H(y) = H(x)$. Complexity: $O(2^m)$.

*Why critical*: Prevents substituting a document (e.g., changing terms in a signed contract) while keeping the same hash.

**6. Collision Resistance (Strong Collision Resistance)**: It must be computationally infeasible to find *any* pair of distinct inputs $(x, y)$ with $H(x) = H(y)$. Complexity: $O(2^{m/2})$ due to birthday attack.

*Why critical*: Prevents birthday attacks on digital signature schemes — an attacker who can find any collision can force a signer to unknowingly sign a malicious document.

---

### Question 3 [KTU June 2022, Part C, Q15 — 9 Marks]
**Question**: Illustrate the working of SHA-1 algorithm.

**Solution**:

**1. Overview**: SHA-1 (FIPS PUB 180-1, 1995) produces a **160-bit digest** from input messages up to $2^{64}-1$ bits. Processes 512-bit blocks using an 80-step iterated compression function. Has 5 registers instead of MD5's 4, and expands 16 input words to 80 words before processing.

**2. Parameters**:
| | Value |
|---|---|
| Digest length | 160 bits (5 × 32-bit words) |
| Block size | 512 bits |
| Steps per block | 80 (4 rounds × 20) |
| Constants | 4 round constants from $\lfloor 2^{30}\sqrt{p} \rfloor$ |
| Max message | $< 2^{64}$ bits |

**3. Step-by-Step Execution**:

**Step 1 (Message Padding)**: Pad message to length $\equiv 448 \pmod{512}$. Append `1` bit, then `0` bits, then 64-bit big-endian length.

**Step 2 (Buffer Initialization)**: Five 32-bit registers:
$$A=\texttt{0x67452301},\; B=\texttt{0xEFCDAB89},\; C=\texttt{0x98BADCFE},\; D=\texttt{0x10325476},\; E=\texttt{0xC3D2E1F0}$$

**Step 3 (Word Expansion — Message Schedule)**: Split each 512-bit block into 16 words $W_0..W_{15}$. Expand to 80 words:
$$W_t = (W_{t-3} \oplus W_{t-8} \oplus W_{t-14} \oplus W_{t-16}) \lll 1 \quad (16 \le t \le 79)$$

**Step 4 (80-Step Round Processing)**: For each step $t$:
$$TEMP = (A \lll 5) + f_t(B,C,D) + E + W_t + K_t \pmod{2^{32}}$$
$$E=D;\quad D=C;\quad C=B \lll 30;\quad B=A;\quad A=TEMP$$

Round functions and constants:
- **Round 1 ($t=0..19$)**: $f_t = (B \wedge C) \vee (\neg B \wedge D)$; $K_t = \texttt{0x5A827999}$
- **Round 2 ($t=20..39$)**: $f_t = B \oplus C \oplus D$; $K_t = \texttt{0x6ED9EBA1}$
- **Round 3 ($t=40..59$)**: $f_t = (B \wedge C) \vee (B \wedge D) \vee (C \wedge D)$; $K_t = \texttt{0x8F1BBCDC}$
- **Round 4 ($t=60..79$)**: $f_t = B \oplus C \oplus D$; $K_t = \texttt{0xCA62C1D6}$

**Step 5 (Chaining and Output)**: After 80 steps, add results to block-input values (mod $2^{32}$). After all blocks, concatenate $A\|B\|C\|D\|E$ big-endian → **160-bit SHA-1 digest**.

**4. Diagram**:
```
 512-bit block ─►[W₀..W₁₅] ─► [Expand to W₀..W₇₉]
                                       │
    IV: A,B,C,D,E ──────────────►  ┌──┴──────────────────┐
                                   │   80 Step Rounds:   │
                                   │  TEMP=(A<<<5)+f+E+W+K│
                                   │  E=D, D=C, C=B<<<30 │
                                   │  B=A, A=TEMP         │
                                   └──────────────────────┘
                                            │
                             Add IV to result (mod 2^32) → CV_q
                                            │
                                    (feed to next block)
                                            │
                               After last block: A‖B‖C‖D‖E
                                            │
                                    160-bit SHA-1 Digest
```

**5. Security**: SHA-1 is broken for collision resistance (SHAttered attack, 2017, $2^{63.1}$ operations). NIST deprecated SHA-1 in 2011. Migrate to SHA-256 or SHA-3 for all new systems.
