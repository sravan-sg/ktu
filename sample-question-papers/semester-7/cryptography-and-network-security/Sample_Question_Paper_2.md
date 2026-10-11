# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SEVENTH SEMESTER B.TECH DEGREE EXAMINATION
### CS409: CRYPTOGRAPHY AND NETWORK SECURITY
**Time: 3 Hours** | **Max. Marks: 100**

---

### PART A
*(Answer all questions. Each carries 4 marks.)*

1. Explain the Caesar cipher and show how brute-force cryptanalysis can recover the plaintext and shift key from the ciphertext `"KHOOR ZRUOG"`. `(4)`
2. Differentiate between Block ciphers and Stream ciphers. Give two distinguishing architectural attributes. `(4)`
3. Explain the key expansion mechanism in the IDEA cipher. How are the 52 subkeys generated from a 128-bit master key? `(4)`
4. Define Euler's Totient function $\phi(n)$. Calculate $\phi(360)$ and explain the totient formula for composite numbers with prime factorizations. `(4)`
5. Explain the Discrete Logarithm Problem and discuss its cryptographic significance in public-key key exchange protocols. `(4)`
6. What is the Birthday Attack on cryptographic hash functions? Explain why an $m$-bit hash function requires only $2^{m/2}$ trials to find a collision. `(4)`
7. List and explain the primary header fields used in the MIME specification for electronic mail. `(4)`
8. What is the role of the Authentication Header (AH) in IPsec? List the fields included in the AH format. `(4)`
9. What are the major Web security threats categorized by passive eavesdropping vs. active impersonation? `(4)`
10. Describe the working principle and primary operational limitations of an Application-Level Gateway (Proxy Firewall). `(4)`

---

### PART B
*(Answer any TWO full questions. Each carries 9 marks.)*

11. (a) Encrypt the plaintext `"EXAMINATION"` using the Hill Cipher with the key matrix:
    $$K = \begin{pmatrix} 9 & 4 \\ 5 & 7 \end{pmatrix} \pmod{26}$$
    Show the vector-matrix multiplications step-by-step. `(5)`  
    (b) Find the inverse key matrix $K^{-1} \pmod{26}$ and decrypt the first two characters of the resulting ciphertext to verify correctness. `(4)`

12. (a) With a complete architectural diagram, explain the Feistel cipher network structure used in the Data Encryption Standard (DES). Explain why decryption uses the exact same algorithm as encryption by reversing the subkey sequence. `(5)`  
    (b) Compare the strengths and weaknesses of DES against Differential Cryptanalysis and Linear Cryptanalysis. `(4)`

13. (a) Describe the mathematical details of the `MixColumns` transformation in AES. Compute the first column output of a state matrix multiplied by the standard MDS polynomial matrix in $GF(2^8)$. `(5)`  
    (b) Explain the Block Cipher Modes of Operation: Cipher Block Chaining (CBC) vs. Counter (CTR) mode. Detail their encryption equations and error propagation characteristics. `(4)`

---

### PART C
*(Answer any TWO full questions. Each carries 9 marks.)*

14. (a) State and prove Euler's Generalization of Fermat's Theorem ($a^{\phi(n)} \equiv 1 \pmod n$ where $\gcd(a, n) = 1$). `(4)`  
    (b) Using the Extended Euclidean Algorithm, solve the linear congruence:
    $$17x \equiv 1 \pmod{43}$$
    Show the complete tabular division and backward substitution steps. `(5)`

15. (a) Explain the Diffie-Hellman Key Exchange algorithm. Illustrate with a concrete diagram how an active adversary can execute a Man-in-the-Middle (MITM) attack when messages are unauthenticated. `(5)`  
    (b) In an Elliptic Curve Cryptosystem over $E_{23}(1, 1)$ defined by the equation $y^2 = x^3 + x + 1 \pmod{23}$:  
    (i) Verify that the point $P = (3, 10)$ lies on the curve.  
    (ii) Compute the doubled point $2P = (x_3, y_3)$ using the tangent slope formula. `(4)`

16. (a) Detail the SHA-1 cryptographic hash algorithm. Explain the message padding scheme, parsing into 512-bit blocks, message expansion into 80 words ($W_t$), and the structure of each round compression function. `(5)`  
    (b) Compare MD5 and SHA-1 across digest length, security margin, collision resistance, and processing speed. `(4)`

---

### PART D
*(Answer any TWO full questions. Each carries 12 marks.)*

17. (a) Describe S/MIME (Secure/Multipurpose Internet Mail Extensions). Detail the four core S/MIME functions: Enveloped Data, Signed Data, Clear-Signed Data, and Signed & Enveloped Data. `(6)`  
    (b) Explain the IPsec Architecture. Contrast the roles of the Security Policy Database (SPD) and the Security Association Database (SAD) during outbound and inbound packet processing. `(6)`

18. (a) Explain how SSL/TLS achieves confidentiality and message integrity via the SSL Record Protocol. Illustrate the packet segmentation, compression, MAC calculation, encryption, and SSL record header assembly. `(6)`  
    (b) With a clear sequence diagram, describe the complete transaction flow in Secure Electronic Transaction (SET) involving Cardholder, Merchant, Payment Gateway, and Issuing Bank. `(6)`

19. (a) Write a comprehensive comparative analysis of:  
    (i) Packet Filtering Firewalls  
    (ii) Circuit-Level Gateways  
    (iii) Stateful Packet Inspection (SPI) Firewalls  
    (iv) Next-Generation Application Firewalls (NGFW). `(6)`  
    (b) Explain the concept of Bastion Hosts. What hardening procedures must be applied to configure a secure bastion host on an organization's perimeter? `(6)`
