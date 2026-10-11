# Module 4: Revision Notes — Quick Review & High-Yield Summary

## Submodule 1: Message Authentication & MAC
- **Security Threats**: Disclosure (confidentiality), Masquerade, Content Modification, Sequence Modification, Timing/Replay, Repudiation.
- **Three Authentication Functions**:
  1. Symmetric / Asymmetric Message Encryption.
  2. Message Authentication Code (MAC): $\text{Tag} = C(K, M)$.
  3. Hash Functions: Keyless digest $H(M)$.
- **MAC vs. Encryption Brute Force**:
  - Encryption key recovery: $2^k$.
  - MAC key recovery: $2^k \cdot \lceil k/m \rceil$.
  - MAC tag forgery effort: $2^m$ without discovering key.
- **HMAC Formula**:
  $$\text{HMAC}_K(M) = H\Big((K^+ \oplus \text{opad}) \parallel H\big((K^+ \oplus \text{ipad}) \parallel M\big)\Big)$$
  where $\text{ipad} = \text{0x36}$ and $\text{opad} = \text{0x5C}$. Resists length-extension attacks.

---

## Submodule 2: Cryptographic Hash Functions (MD5 & SHA-1)
- **Hash Properties**: Pre-image resistance (one-way, $2^m$), Second pre-image resistance ($2^m$), Collision resistance ($2^{m/2}$).
- **Birthday Attack**: Finding a collision among $2^m$ values requires only $\approx 1.177 \times 2^{m/2}$ random samples ($P \ge 0.5$).
- **MD5**: 128-bit digest, 512-bit block. Padded to $448 \bmod 512$ + 64-bit length. 4 registers ($A, B, C, D$), 4 rounds of 16 steps (64 steps total). Completely broken.
- **SHA-1**: 160-bit digest, 512-bit block. Padded to $448 \bmod 512$ + 64-bit length. 5 registers ($A, B, C, D, E$). 16 words expanded to 80 words ($W_t = (W_{t-3} \oplus W_{t-8} \oplus W_{t-14} \oplus W_{t-16}) \lll 1$). 80 steps (4 rounds of 20 steps). Deprecated.

---

## Submodule 3: Digital Signatures & DSA
- **Digital Signature**: Provides authenticity, integrity, non-repudiation, unforgeability.
- **Digital Signature Algorithm (DSA)**:
  - Global parameters: $p$ prime, $q \mid (p - 1)$, $g = h^{(p-1)/q} \bmod p$.
  - Private key: $x \in [1, q-1]$. Public key: $y = g^x \bmod p$.
  - **Signing**: Random $k \in (0, q)$:
    $$r = (g^k \bmod p) \bmod q$$
    $$s = k^{-1}(H(M) + x \cdot r) \bmod q$$
    Signature: $(r, s)$.
  - **Verifying**:
    $$w = (s')^{-1} \bmod q, \quad u_1 = (H(M') \cdot w) \bmod q, \quad u_2 = (r' \cdot w) \bmod q$$
    $$v = \Big((g^{u_1} \cdot y^{u_2}) \bmod p\Big) \bmod q$$
    Valid if $v == r'$.
  - **Critical Rule**: $k$ must NEVER be reused across messages; reuse exposes private key $x$ directly.

---

## Submodule 4: High-Yield Formulas & Exam Cheatsheet
- Birthday collision bound: $N \approx 2^{m/2}$.
- Padding bit count: $P = (448 - 1 - L) \bmod 512$.
- DSA verification equality: $g^{u_1} y^{u_2} \equiv g^{w H(M) + w x r} \equiv g^k \pmod p \implies v = r$.
- Encrypt-then-MAC: $C = E_{K_1}(M)$, $T = \text{MAC}_{K_2}(C)$. Immune to padding oracle attacks.
