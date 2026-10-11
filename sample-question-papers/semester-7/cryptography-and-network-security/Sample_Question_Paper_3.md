# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SEVENTH SEMESTER B.TECH DEGREE EXAMINATION
### CS409: CRYPTOGRAPHY AND NETWORK SECURITY
**Time: 3 Hours** | **Max. Marks: 100**

---

### PART A
*(Answer all questions. Each carries 4 marks.)*

1. Explain the rotor machine concept used in historical ciphers (e.g. Enigma) and describe how polyalphabetic substitution is achieved through cascading rotors. `(4)`
2. Differentiate between Symmetric Key and Asymmetric Key Cryptosystems in terms of key distribution complexity, computation cost, and secrecy requirements. `(4)`
3. Explain the odd-round and even-round operations in the IDEA block cipher. `(4)`
4. Find the greatest common divisor $\gcd(2740, 1760)$ using the Euclidean Algorithm. `(4)`
5. Define Primitive Root in modular arithmetic. Show that $2$ is a primitive root of the prime $11$. `(4)`
6. Explain why digital signatures provide non-repudiation while Message Authentication Codes (MACs) do not. `(4)`
7. Explain why compression is performed prior to encryption in Pretty Good Privacy (PGP). `(4)`
8. Distinguish between Transport Mode and Tunnel Mode in IPsec. `(4)`
9. Explain the purpose of the `ChangeCipherSpec` and `Alert` protocols in the SSL/TLS architecture. `(4)`
10. Describe the concept and configuration of a Screened Subnet (DMZ) architecture. `(4)`

---

### PART B
*(Answer any TWO full questions. Each carries 9 marks.)*

11. (a) Encrypt the plaintext message `"CRYPTOGRAPHY"` using the Row Transposition Cipher with the key permutation `[3, 1, 4, 2]`. Show the complete rectangular array and columnar readout. `(5)`  
    (b) Describe Steganography. Explain Least Significant Bit (LSB) image steganography and audio masking techniques with their detection challenges. `(4)`

12. (a) In the Simplified DES (S-DES) cipher:
    - Master key $K = (1010000010)_2$
    - Plaintext $P = (11010111)_2$
    Given the standard S-Boxes $S_0$ and $S_1$ and initial permutation $IP$:
    Perform the complete Round 1 transformation and derive the intermediate 8-bit output. `(5)`  
    (b) Discuss the design principles of modern block ciphers with special emphasis on the number of rounds, S-box non-linearity criteria, and diffusion layer designs. `(4)`

13. (a) Explain the AES Key Expansion algorithm. How does a 128-bit key generate 11 round keys of 128 bits each? Detail the role of `RotWord`, `SubWord`, and the Round Constant ($Rcon$). `(5)`  
    (b) Explain the RC4 stream cipher pseudo-random generator. Discuss the weaknesses associated with biased early bytes (Fluhrer-Mantin-Shamir attack) and how WEP was compromised as a result. `(4)`

---

### PART C
*(Answer any TWO full questions. Each carries 9 marks.)*

14. (a) In an RSA cryptosystem:
    - Let $p = 11$, $q = 13$, and encryption exponent $e = 7$.
    (i) Compute the modulus $n$ and Euler's totient $\phi(n)$.  
    (ii) Compute the private key $d$ using the Extended Euclidean Algorithm.  
    (iii) Encrypt the message $M = 5$ to obtain ciphertext $C$.  
    (iv) Decrypt $C$ to recover $M$. `(5)`  
    (b) Explain the Chinese Remainder Theorem (CRT) and demonstrate how it is used to speed up RSA decryption computations. `(4)`

15. (a) Consider Diffie-Hellman Key Exchange with common parameters $q = 11$ and primitive root $\alpha = 2$.
    (i) If user Alice has public key $Y_A = 9$, find Alice's private key $X_A$.  
    (ii) If user Bob has public key $Y_B = 3$, find the shared secret key $K$ shared between Alice and Bob. `(5)`  
    (b) Explain the mathematical foundation of Elliptic Curve Diffie-Hellman (ECDH) key exchange. Write the point multiplication and point addition equations over a prime field $\mathbb{F}_p$. `(4)`

16. (a) Explain the Digital Signature Standard (DSS). Illustrate with block diagrams the signing and verifying process using the Digital Signature Algorithm (DSA). `(5)`  
    (b) Explain Mutual Authentication Protocols based on symmetric encryption. Analyze the Needham-Schroeder protocol and explain how the Denning-Sacco replay vulnerability is resolved. `(4)`

---

### PART D
*(Answer any TWO full questions. Each carries 12 marks.)*

17. (a) With clear diagrams, describe the complete PGP message generation and transmission process, as well as the message reception and decryption process. Explain the structure and purpose of the Private Key Ring and Public Key Ring in PGP. `(6)`  
    (b) Detail the IPsec Architecture. Explain the format of the Security Parameter Index (SPI), sequence number verification for anti-replay defense, and how Security Associations are combined into SA bundles. `(6)`

18. (a) Explain the SSL/TLS protocol suite. Describe the four protocols: Handshake Protocol, ChangeCipherSpec Protocol, Alert Protocol, and Record Protocol. Detail how session states and connection states are managed. `(6)`  
    (b) Explain the Secure Electronic Transaction (SET) protocol. Describe the Dual Signature generation and verification equations:
    $$DS = E_{PR_C}[H(H(PI) \parallel H(OI))]$$
    Explain how the merchant verifies authorization without seeing card numbers, and the bank verifies payment without seeing item descriptions. `(6)`

19. (a) Design a Packet Filter Firewall rule set for an enterprise network to:
    (i) Allow inbound SMTP to the enterprise mail server ($192.168.1.10$).  
    (ii) Allow internal clients to browse web servers outside on port 80 and 443.  
    (iii) Deny and log all other incoming traffic (Default Deny).
    Present the rule table with Interface, Direction, Source IP, Destination IP, Protocol, Source Port, Destination Port, and Action. `(6)`  
    (b) Explain Encrypted Tunnels. Describe how IPsec in Tunnel Mode creates a Virtual Private Network (VPN) connecting remote branch offices through untrusted public internet backbones. `(6)`
