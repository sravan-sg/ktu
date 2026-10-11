# Stream Ciphers and RC4

## 1. Explanation
A **stream cipher** encrypts plaintext digits (typically characters or bits) one at a time continuously using a time-varying pseudorandom keystream $k_i$.
In contrast to a block cipher which operates on large stationary data blocks (64 or 128 bits), a stream cipher operates like an automated One-Time Pad, where a short secret seed key $K$ is expanded into an infinite pseudo-random bit stream $k_i$:
$$c_i = p_i \oplus k_i, \quad p_i = c_i \oplus k_i$$

### Stream Cipher Architecture & Design Requirements
According to William Stallings (*Cryptography and Network Security*, Chapter 7), an effective stream cipher must satisfy four essential criteria:
1. **Long Period**: The pseudo-random bit sequence must have an extremely large period before repeating to prevent known-plaintext keystream reuse attacks.
2. **Pseudorandomness**: The keystream must pass all statistical tests for randomness (NIST SP 800-22 tests, equal distribution of 0s and 1s, run tests).
3. **Key Length**: The seed key must be sufficiently long ($\ge 128$ bits) to withstand exhaustive brute-force search.
4. **Resilience to State Reconstruction**: Knowledge of portions of the keystream must not allow an attacker to reconstruct the internal state of the generator.

```
                    Secret Key K
                         │
                         ▼
             [ Pseudo-Random Keystream ]
             [      Generator (PRG)    ]
                         │
                         ▼ Keystream k_i
Plaintext p_i ───────► (XOR) ───────► Ciphertext c_i
```

### The RC4 Stream Cipher
Designed by Ron Rivest of RSA Security in 1987, RC4 was long the world's most widely deployed stream cipher (used in SSL/TLS, WEP, and WPA).
- **Core State**: An internal 256-byte array $S = (S[0], S[1], \dots, S[255])$ that contains a permutation of all 8-bit numbers from $0$ to $255$.
- **Two State Pointers**: Two 8-bit integer indices $i$ and $j$.
- **Variable Key Length**: Key size ranges from 1 to 256 bytes (8 to 2048 bits), typically 40 to 128 bits.

RC4 operates in two distinct phases:
1. **Phase 1: Key-Scheduling Algorithm (KSA)**
2. **Phase 2: Pseudo-Random Generation Algorithm (PRGA)**

#### 1. Key-Scheduling Algorithm (KSA)
Initializes and scrambles the state permutation array $S$ using the secret key $K$ of length $L$ bytes ($1 \le L \le 256$):
```
// Step 1: Initialize S array with identity permutation
for i = 0 to 255:
    S[i] = i
    T[i] = K[i mod L]

// Step 2: Initial Permutation of S
j = 0
for i = 0 to 255:
    j = (j + S[i] + T[i]) mod 256
    swap(S[i], S[j])
```

#### 2. Pseudo-Random Generation Algorithm (PRGA)
Once $S$ is initialized, KSA terminates, and PRGA continuously emits pseudo-random bytes $k$:
```
i = 0
j = 0
while generating_bytes:
    i = (i + 1) mod 256
    j = (j + S[i]) mod 256
    swap(S[i], S[j])
    t = (S[i] + S[j]) mod 256
    k = S[t]   // Output keystream byte
```
Encryption and decryption XOR the output byte $k$ with the plaintext/ciphertext byte:
$$c = p \oplus k, \quad p = c \oplus k$$

### Security Strengths and Vulnerabilities
- **Strengths**: Extremely compact, simple implementation, requires minimal CPU cycles (only table swaps and 8-bit modular additions), runs at high speeds in both software and hardware.
- **Weaknesses & The WEP Vulnerability**:
  - **Invariance Bias (Fluhrer, Mantin, and Shamir - FMS Attack, 2001)**: The second byte output by RC4 is biased toward 0 with probability $1/128$ instead of $1/256$.
  - **Key Reuse Catastrophe in 802.11 WEP**: WEP concatenated a static 104-bit secret key with a small 24-bit Initialization Vector ($IV$) to form the RC4 key: $K = IV \parallel K_{\text{master}}$. Because 24 bits wrap around after $2^{24} \approx 16.7$ million packets (a few hours on a busy Wi-Fi network), identical keys were reused, allowing passive eavesdroppers to recover plaintext and reconstruct the master key via the FMS attack.
  - **Current Status**: Deprecated in TLS by RFC 7465 in 2015.

---

## 2. Example: 8-Element State Model of RC4
To illustrate RC4 mechanics clearly, consider an educational 8-element state ($N = 8$ instead of 256):
- State array: $S = [0, 1, 2, 3, 4, 5, 6, 7]$.
- Let key $K = [1, 2, 3]$ (Length $L = 3$).
- **KSA Step**:
  - Initially: $T = [1, 2, 3, 1, 2, 3, 1, 2]$.
  - $i=0$: $j = (0 + S[0] + T[0]) \bmod 8 = (0 + 0 + 1) \bmod 8 = 1$. Swap $S[0]$ and $S[1]$: $S = [1, 0, 2, 3, 4, 5, 6, 7]$.
  - $i=1$: $j = (1 + S[1] + T[1]) \bmod 8 = (1 + 0 + 2) \bmod 8 = 3$. Swap $S[1]$ and $S[3]$: $S = [1, 3, 2, 0, 4, 5, 6, 7]$.
  - Process continues for all 8 elements.
- **PRGA Step**:
  - $i = (0 + 1) \bmod 8 = 1$.
  - $j = (0 + S[1]) \bmod 8 = (0 + 3) \bmod 8 = 3$.
  - Swap $S[1]$ and $S[3]$: $S[1] = 0, S[3] = 3$.
  - $t = (S[1] + S[3]) \bmod 8 = (0 + 3) \bmod 8 = 3$.
  - Keystream byte: $k_1 = S[3] = 3$.

---

## 3. Applications & Use Cases
1. **Legacy IEEE 802.11b/g Wi-Fi (WEP and WPA-TKIP)**: Deployed RC4 as the core stream cipher engine before replacement by AES-CCMP in 802.11i.
2. **Microsoft Remote Desktop Protocol (RDP)**: Used RC4 for lightweight, low-latency encryption of interactive terminal keystrokes and screen redraws.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Full RC4 Hand-Trace on a 4-Element State
**Problem**:
Trace the complete KSA and generate the first 2 keystream bytes using a 4-element RC4 model ($N = 4$) with secret key $K = [2, 3]$ of length $L = 2$.

**Step-by-step Solution**:
1. **KSA Initialization**:
   - $S = [0, 1, 2, 3]$.
   - $T = [2, 3, 2, 3]$.
   - $j = 0$.
2. **KSA Scrambling Loop**:
   - $i = 0$: $j = (0 + S[0] + T[0]) \bmod 4 = (0 + 0 + 2) \bmod 4 = 2$.
     Swap $S[0]$ and $S[2]$:
     $$S = [2, 1, 0, 3]$$
   - $i = 1$: $j = (2 + S[1] + T[1]) \bmod 4 = (2 + 1 + 3) \bmod 4 = 6 \bmod 4 = 2$.
     Swap $S[1]$ and $S[2]$:
     $$S = [2, 0, 1, 3]$$
   - $i = 2$: $j = (2 + S[2] + T[2]) \bmod 4 = (2 + 1 + 2) \bmod 4 = 5 \bmod 4 = 1$.
     Swap $S[2]$ and $S[1]$:
     $$S = [2, 1, 0, 3]$$
   - $i = 3$: $j = (1 + S[3] + T[3]) \bmod 4 = (1 + 3 + 3) \bmod 4 = 7 \bmod 4 = 3$.
     Swap $S[3]$ and $S[3]$ (no change):
     $$S = [2, 1, 0, 3]$$
   KSA Complete! Initialized permutation: $S = [2, 1, 0, 3]$.

3. **PRGA Loop**:
   - Start with $i = 0, j = 0$.
   - **Byte 1**:
     - $i = (0 + 1) \bmod 4 = 1$.
     - $j = (0 + S[1]) \bmod 4 = (0 + 1) \bmod 4 = 1$.
     - Swap $S[1]$ and $S[1]$: $S = [2, 1, 0, 3]$.
     - $t = (S[1] + S[1]) \bmod 4 = (1 + 1) \bmod 4 = 2$.
     - **Keystream Byte 1**: $k_1 = S[2] = \mathbf{0}$.
   - **Byte 2**:
     - $i = (1 + 1) \bmod 4 = 2$.
     - $j = (1 + S[2]) \bmod 4 = (1 + 0) \bmod 4 = 1$.
     - Swap $S[2]$ and $S[1]$:
       $$S = [2, 0, 1, 3]$$
     - $t = (S[2] + S[1]) \bmod 4 = (1 + 0) \bmod 4 = 1$.
     - **Keystream Byte 2**: $k_2 = S[1] = \mathbf{0}$.

---

### Example 2: Stream Cipher Two-Time Pad Vulnerability
**Problem**:
In a stream cipher, if the same keystream $K$ is accidentally reused to encrypt two plaintexts $P_1$ and $P_2$, show how an adversary can extract information about the plaintexts.

**Step-by-step Solution**:
- Ciphertexts:
  $$C_1 = P_1 \oplus K$$
  $$C_2 = P_2 \oplus K$$
- The adversary intercepts both $C_1$ and $C_2$ and computes their bitwise XOR:
  $$C_1 \oplus C_2 = (P_1 \oplus K) \oplus (P_2 \oplus K) = P_1 \oplus P_2$$
- The key $K$ completely cancels out!
- The resulting value $P_1 \oplus P_2$ is the XOR of two natural language plaintexts. Using statistical properties (e.g., spaces XORed with letters produce known case flips), linguistics, and dictionary matching, both $P_1$ and $P_2$ can be recovered without discovering the key.

---

### Example 3: Calculation of RC4 Internal State Space
**Problem**:
What is the total number of possible internal states of the RC4 permutation array $S$?

**Step-by-step Solution**:
- The state array $S$ is a permutation of the 256 bytes $\{0, 1, \dots, 255\}$.
- The number of permutations of 256 distinct elements is:
  $$256! \approx 8.57 \times 10^{506} \approx 2^{1684}$$
- The pointers $i$ and $j$ each take $256 = 2^8$ values, giving $2^{16}$ pointer configurations.
- Total internal state space:
  $$\text{States} \approx 256! \times 2^{16} \approx 2^{1700}$$
- This immense internal state space prevents any brute-force search of the generator's state.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU January 2023, Part A, Q3 - 4 Marks]
**Question**: Describe the initialization, initial permutation and key stream generation of RC4.

**Solution**:
1. **Initialization of State Array $S$ and Temporary Vector $T$**:
   - RC4 maintains an internal state consisting of a 256-byte array $S$ containing numbers from $0$ to $255$, and two pointer indices $i$ and $j$.
   - A variable-length key $K$ of length $L$ bytes ($1 \le L \le 256$) is supplied.
   - Array $S$ is initialized with the identity permutation, and array $T$ is filled by repeating key $K$:
     ```
     for i = 0 to 255:
         S[i] = i
         T[i] = K[i mod L]
     ```

2. **Initial Permutation of $S$ (Key-Scheduling Algorithm - KSA)**:
   - Index $j$ is initialized to $0$.
   - The state array $S$ is permuted using bytes from $T$:
     ```
     j = 0
     for i = 0 to 255:
         j = (j + S[i] + T[i]) mod 256
         swap(S[i], S[j])
     ```
   - At the completion of this loop, $S$ contains a pseudo-random permutation of the numbers $0 \dots 255$ uniquely determined by the key $K$.

3. **Keystream Generation (Pseudo-Random Generation Algorithm - PRGA)**:
   - Both pointers $i$ and $j$ are reset to $0$.
   - To generate each keystream byte $k$:
     ```
     i = (i + 1) mod 256
     j = (j + S[i]) mod 256
     swap(S[i], S[j])
     t = (S[i] + S[j]) mod 256
     k = S[t]
     ```
   - The generated byte $k$ is XORed with a plaintext byte $p$ to produce ciphertext byte $c = p \oplus k$.
   - For decryption, the receiver runs the identical PRGA and XORs $c$ with $k$ to recover $p = c \oplus k$.

---

### Question 2 [KTU June 2022, Part B, Q12(b) - 4 Marks]
**Question**: Explain the primitive operations of RC4 algorithm.

**Solution**:
The RC4 stream cipher relies on three exceptionally simple primitive operations executed on 8-bit unsigned bytes:

1. **Modular Pointer Increment & Accumulation**:
   - Pointer $i$ advances by 1 modulo 256: $i = (i + 1) \bmod 256$.
   - Pointer $j$ accumulates the value in state array $S[i]$ modulo 256: $j = (j + S[i]) \bmod 256$.
   - In hardware or software, addition modulo 256 is achieved automatically by unsigned 8-bit integer overflow without explicit division.

2. **Permutation Swap (`swap(S[i], S[j])`)**:
   - The two bytes located at array indices $i$ and $j$ are swapped:
     ```
     temp = S[i]
     S[i] = S[j]
     S[j] = temp
     ```
   - This constantly shuffles the internal permutation array $S$ with every byte emitted, ensuring that the internal state continuously evolves.

3. **Indirection Lookup & XOR Masking**:
   - A lookup index $t$ is computed by summing the newly swapped state elements:
     $$t = (S[i] + S[j]) \bmod 256$$
   - The output keystream byte is the element at position $t$: $k = S[t]$.
   - Encryption/decryption is performed via bitwise Exclusive-OR:
     $$C = P \oplus k, \quad P = C \oplus k$$
   These operations require no multipliers, no modular exponentiations, and no large S-boxes, making RC4 remarkably fast in software execution.
