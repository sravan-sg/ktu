# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SEVENTH SEMESTER B.TECH DEGREE EXAMINATION
### CS409: CRYPTOGRAPHY AND NETWORK SECURITY
**Time: 3 Hours** | **Max. Marks: 100**

---

### PART A
*(Answer all questions. Each carries 4 marks.)*

1. Differentiate between active and passive security attacks with two realistic network examples for each. `(4)`
2. Differentiate between Confusion and Diffusion as defined by Claude Shannon. How does S-DES implement both properties? `(4)`
3. Explain the byte-level transformation `SubBytes` in AES. How is non-linearity ensured using Galois Field $GF(2^8)$ arithmetic? `(4)`
4. State Fermat's Little Theorem. Using it, evaluate $3^{201} \bmod 11$. `(4)`
5. In an RSA cryptosystem, given primes $p = 7$, $q = 17$, and public exponent $e = 5$, find the private decryption key $d$. `(4)`
6. State the three fundamental security properties required of a cryptographic hash function (pre-image resistance, second pre-image resistance, and collision resistance). `(4)`
7. Explain the function of the Security Association (SA) and Security Parameter Index (SPI) in IPsec. `(4)`
8. Describe how Pretty Good Privacy (PGP) achieves message authentication and sender non-repudiation. `(4)`
9. What are the key services provided by the SSL Record Protocol? `(4)`
10. Differentiate between Packet Filtering Firewalls and Stateful Inspection Firewalls. `(4)`

---

### PART B
*(Answer any TWO full questions. Each carries 9 marks.)*

11. (a) Encrypt the plaintext message `"INFORMATIONSECURITY"` using the Playfair cipher with key `"MONARCHY"`. State all three Playfair encryption rules clearly. `(5)`  
    (b) Using the Rail Fence transposition cipher with depth 3, encrypt the message `"DEFEND THE EAST WALL"`. Show the intermediate rail layout. `(4)`

12. (a) Illustrate the Simplified DES (S-DES) key generation process. Given a 10-bit master key $K = 1010000010$, calculate the two 8-bit subkeys $K_1$ and $K_2$ using standard permutation vectors $P_{10}$ and $P_8$. `(5)`  
    (b) Describe the primitive algebraic operations employed in the IDEA (International Data Encryption Algorithm) cipher and explain why they make IDEA cryptographically strong without S-boxes. `(4)`

13. (a) With a neat schematic diagram, explain the single round structure of AES (Advanced Encryption Standard). Detail the four transformations (`SubBytes`, `ShiftRows`, `MixColumns`, `AddRoundKey`). `(5)`  
    (b) Describe the initialization and pseudo-random byte generation steps of the RC4 stream cipher (KSA and PRGA algorithms). `(4)`

---

### PART C
*(Answer any TWO full questions. Each carries 9 marks.)*

14. (a) Using the Extended Euclidean Algorithm, calculate the greatest common divisor $\gcd(240, 46)$ and find integer coefficients $x$ and $y$ such that $240x + 46y = \gcd(240, 46)$. Also find the modular multiplicative inverse of $46 \bmod 240$ if it exists. `(5)`  
    (b) Alice and Bob use the Diffie-Hellman Key Exchange protocol with common prime $q = 23$ and primitive root $\alpha = 5$. Alice chooses private key $X_A = 6$ and Bob chooses private key $X_B = 15$.  
    (i) Calculate Alice's public key $Y_A$ and Bob's public key $Y_B$.  
    (ii) Compute the shared symmetric key $K$. `(4)`

15. (a) In an RSA cryptosystem, user Bob has public key $(e = 13, n = 33)$. Alice sends ciphertext $C = 8$ to Bob.  
    (i) Determine Bob's private key $d$.  
    (ii) Recover the plaintext message $M$ using modular exponentiation. `(5)`  
    (b) Explain the step-by-step mathematical signing and signature verification process in the Digital Signature Algorithm (DSA) under DSS. `(4)`

16. (a) With an architectural block diagram, explain the MD5 message digest generation process, detailing message padding, the 512-bit block compression function, and the four non-linear auxiliary functions. `(5)`  
    (b) Explain HMAC (Hash-based Message Authentication Code). Write its mathematical formulation and explain why it is computationally more secure against extension attacks than simple keyed hashing. `(4)`

---

### PART D
*(Answer any TWO full questions. Each carries 12 marks.)*

17. (a) Explain the cryptographic services and operational workflow of PGP (Pretty Good Privacy) for message transmission and reception. Include clear diagrams showing digital signing, symmetric encryption, compression, and Radix-64 encoding. `(6)`  
    (b) Explain the structure of IPsec Encapsulating Security Payload (ESP). Illustrate how ESP packet formatting differs between Transport Mode and Tunnel Mode. `(6)`

18. (a) Detail the SSL/TLS Handshake Protocol message exchange sequence between a client and server. Explain how the Master Secret is derived and used to generate symmetric session keys. `(6)`  
    (b) What is a Dual Signature in Secure Electronic Transaction (SET)? Explain why it is essential to link Payment Information (PI) and Order Information (OI) while preserving customer privacy from the merchant and the bank. `(6)`

19. (a) Explain the architecture, working, and comparative trade-offs of the following firewall architectures:  
    (i) Screened Host Firewall (Single-homed and Dual-homed bastion)  
    (ii) Screened Subnet Firewall (Demilitarized Zone - DMZ). `(6)`  
    (b) What are Encrypted Tunnels? Explain how VPN gateways establish encrypted tunnels across public IP networks to protect corporate intranet traffic. `(6)`
