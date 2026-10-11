# Secure Electronic Transaction (SET)

## 1. Explanation
The **Secure Electronic Transaction (SET)** standard was developed jointly in 1996 by Visa and MasterCard, in collaboration with IBM, Microsoft, Netscape, and RSA Security. It is an open encryption and security specification designed specifically to protect credit card transactions over the Internet.

### SET Business Environment and Participants
SET involves five distinct business entities:
1. **Cardholder**: An authorized credit card holder who wishes to purchase goods online from a merchant. The cardholder interacts using a secure SET-compliant digital wallet application.
2. **Merchant**: A vendor offering goods or services on the Web who accepts electronic payments.
3. **Issuer**: The financial institution (bank) that issued the credit card to the cardholder.
4. **Acquirer (Merchant's Bank)**: The financial institution that establishes an account with the merchant and processes payment card authorizations and clearings.
5. **Payment Gateway**: A secure server operated by the acquirer (or a trusted third-party processor) that interfaces directly between the Internet and the private financial clearing network (VisaNet/MasterCard BankNet).
6. **Certificate Authority (CA)**: Issues public-key X.509 certificates to cardholders, merchants, and payment gateways.

```
       SET Business Architecture
       Cardholder (Consumer)
        │                  │
        │ Order Info (OI)  │ Payment Info (PI)
        ▼                  │
    Merchant               │
        │                  │
        │ (Forwards PI)    │
        ▼                  ▼
    Payment Gateway ◄──────┘
        │
        ▼ (Private BankNet)
    Acquirer / Issuer Bank
```

### The Fundamental Problem in E-Commerce
In a standard retail e-commerce transaction:
- The **Merchant** needs to know the **Order Information (OI)** (what items the customer is buying, quantities, shipping address) to fulfill the order, but the merchant should **NOT** see the customer's credit card number or account details (to prevent credit card theft, unauthorized charges, or insider merchant fraud).
- The **Bank / Payment Gateway** needs to know the **Payment Information (PI)** (credit card number, expiration date, billing address, authorization charge amount) to debit the cardholder, but should **NOT** see the detailed list of items being purchased (to preserve customer purchase privacy).
- **The Challenge**: How can the customer link the Order Information (OI) and Payment Information (PI) together cryptographically so that neither party can alter the order or transfer the payment authorization to a different transaction?

### The Dual Signature Mechanism
To solve this exact problem, SET introduced the **Dual Signature**.
The dual signature links two separate messages intended for two different recipients in such a way that both recipients can independently verify that the signature is authentic without seeing the other recipient's plaintext message!

#### Mathematical Construction of the Dual Signature
1. Let $OI$ be the Order Information (intended for the merchant).
2. Let $PI$ be the Payment Information (intended for the payment gateway/bank).
3. The customer generates the message digest of both components using SHA-1:
   $$H(OI) = \text{Hash}(OI)$$
   $$H(PI) = \text{Hash}(PI)$$
4. The two digests are concatenated together:
   $$H(PI) \parallel H(OI)$$
5. The combined value is hashed again, and then encrypted with the customer's private signature key ($PR_C$):
   $$\mathbf{DS = E_{PR_C}\Big(H\big(H(PI) \parallel H(OI)\big)\Big)}$$
   This output $DS$ is the **Dual Signature**.

```
  Payment Info (PI)                     Order Info (OI)
         │                                     │
         ▼                                     ▼
     [ Hash ] ──► H(PI)                   [ Hash ] ──► H(OI)
         │            │                   │            │
         │            └─────────┬─────────┘            │
         │                      ▼                      │
         │             ( H(PI) || H(OI) )              │
         │                      │                      │
         │                      ▼                      │
         │                   [ Hash ]                  │
         │                      │                      │
         │                      ▼                      │
         │             [ Encrypt with PR_C ]           │
         │                      │                      │
         │                      ▼                      │
         │             Dual Signature (DS)             │
         │                      │                      │
         ▼                      ▼                      ▼
  Sent to Bank ◄───────────────────────────────── Sent to Merchant
```

#### Transmitted Packages
The customer sends:
- **To the Merchant**: $\Big(OI, \ H(PI), \ DS\Big)$
- **To the Payment Gateway (via the Merchant)**: $\Big(PI, \ H(OI), \ DS\Big)$
  *(Note: $PI$ is encrypted with the Payment Gateway's public key $PU_{PG}$ so that the merchant cannot read it).*

#### Independent Dual Signature Verification
- **Verification by the Merchant**:
  1. The merchant receives $OI$, the hash $H(PI)$, and $DS$.
  2. The merchant computes $H(OI)$ from the received $OI$.
  3. The merchant concatenates $H(PI) \parallel H(OI)$ and hashes it:
     $$\text{Digest}_{\text{merchant}} = H(H(PI) \parallel H(OI))$$
  4. The merchant decrypts the dual signature using the cardholder's public key ($PU_C$):
     $$\text{Decrypted Digest} = D(PU_C, DS)$$
  5. If $\text{Digest}_{\text{merchant}} == \text{Decrypted Digest}$, the merchant verifies that the customer authorized this exact order without ever learning the credit card number!
- **Verification by the Payment Gateway**:
  1. The payment gateway decrypts $PI$, receiving $PI$, the hash $H(OI)$, and $DS$.
  2. The gateway computes $H(PI)$ from the received $PI$.
  3. The gateway concatenates $H(PI) \parallel H(OI)$ and hashes it:
     $$\text{Digest}_{\text{gateway}} = H(H(PI) \parallel H(OI))$$
  4. The gateway decrypts $DS$ with customer's public key $PU_C$:
     $$\text{Decrypted Digest} = D(PU_C, DS)$$
  5. If $\text{Digest}_{\text{gateway}} == \text{Decrypted Digest}$, the gateway verifies that the customer authorized the payment for this specific order without ever learning what goods were bought!

### Sequence of Operations in a SET Transaction
1. **Cardholder Registration**: Cardholder obtains an X.509 digital certificate from a CA.
2. **Merchant Registration**: Merchant obtains business certificates for signing and key exchange.
3. **Purchase Request**:
   - Cardholder browses merchant website, selects items.
   - Merchant sends an invoice.
   - Cardholder generates $OI$, $PI$, and computes the Dual Signature $DS$.
   - Cardholder sends the order and payment instructions to the merchant.
4. **Payment Authorization**:
   - Merchant requests payment authorization from the Payment Gateway.
   - Merchant forwards the encrypted payment package to the Payment Gateway.
   - Payment Gateway decrypts $PI$, verifies the dual signature, and routes an authorization request across the private banking network (VisaNet) to the issuing bank.
   - Issuing bank checks credit limit and returns authorization approval.
   - Payment Gateway sends an authorization response to the merchant.
5. **Order Fulfillment**:
   - Merchant confirms the order and ships goods to the customer.
6. **Payment Capture**:
   - Merchant requests settlement and transfer of funds from the Payment Gateway.

---

## 2. Example: Mathematical Privacy Protection in Dual Signature
- Suppose an adversary intercepts the merchant's packet $(OI, H(PI), DS)$.
- Can the adversary recover $PI$?
  - No! Because $PI$ is protected by the pre-image resistance of SHA-1: finding $PI$ from $H(PI)$ requires $2^{160}$ operations.
- Can a rogue merchant alter $OI$ to order 10 expensive laptops instead of 1?
  - If the merchant changes $OI$ to $OI'$, then $H(OI') \neq H(OI)$.
  - When the bank verifies $H(H(PI) \parallel H(OI')) \neq D(PU_C, DS)$, the signature check fails immediately. Fraud is prevented!

---

## 3. Applications & Use Cases
1. **Modern 3D-Secure (3DS / EMV 3-D Secure)**: The foundational dual-party authorization concept pioneered by SET evolved directly into the modern 3D-Secure protocol (Visa Secure, Mastercard Identity Check) for multi-factor e-commerce authentication.
2. **Cryptographic Escrow & Privacy-Preserving Smart Contracts**: Blockchain payment channels utilize dual signature abstractions to separate transaction settlement logic from sensitive off-chain payload descriptions.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Dual Signature Verification Computation
**Problem**:
Given:
- Hash of Payment Info: $H(PI) = \text{0xAAAA}$
- Order Info: $OI = \text{"Purchase 1 Laptop for \$1000"}$
- Let hash function $H(X)$ be a simple hash: sum of ASCII bytes modulo $1000$.
- Verify the dual signature.

**Step-by-step Solution**:
1. Calculate $H(OI)$:
   - Compute character byte sum of $OI$: let $\text{Sum}(OI) \bmod 1000 = 450$.
   - Thus, $H(OI) = 450$.
2. Form concatenated block:
   $$\text{Block} = H(PI) \parallel H(OI) = \text{0xAAAA} \parallel 450$$
3. Compute master digest:
   $$\text{Digest} = H(\text{0xAAAA} \parallel 450) = 872$$
4. Check Dual Signature:
   - Verifier decrypts $DS$ with Cardholder's public key: $D(PU_C, DS) = 872$.
   - Since $872 == 872$, the dual signature is valid. Both $OI$ and $PI$ are authenticated as matching parts of the same transaction.

---

### Example 2: Comparison of SSL/TLS vs. SET in E-Commerce
**Problem**:
Why did mainstream e-commerce adopt SSL/TLS over SET despite SET offering superior privacy via Dual Signatures?

**Step-by-step Solution**:
| Comparison Attribute | SSL / TLS (HTTPS) | Secure Electronic Transaction (SET) |
|---|---|---|
| **Client Requirement** | Zero client setup. Supported natively in all browsers. | Required cardholders to install specialized digital wallet software and digital certificates. |
| **Merchant Requirement** | Merchant needs only a standard web server certificate. | Merchant required specialized SET gateway software. |
| **Cardholder Privacy** | Merchant sees credit card numbers in plaintext. | Merchant never sees credit card numbers (protected via Dual Signature). |
| **Computational Overhead** | Low (only 1 handshake per session). | Very high (multiple public-key signature operations and certificate validations per purchase). |
| **Commercial Adoption** | Universal standard. | Failed commercially due to high deployment complexity and customer friction. |

---

### Example 3: The Threat of Transaction Switching
**Problem**:
Explain how the Dual Signature prevents a malicious merchant from associating Bob's payment with Alice's expensive order.

**Step-by-step Solution**:
- Suppose a merchant attempts to take Bob's payment authorization $PI_{\text{Bob}}$ and attach it to Alice's unpaid order $OI_{\text{Alice}}$.
- To verify payment, the Payment Gateway must check:
  $$H\Big(H(PI_{\text{Bob}}) \parallel H(OI_{\text{Alice}})\Big) \stackrel{?}{=} D(PU_{\text{Bob}}, DS)$$
- But Bob's dual signature was computed as:
  $$DS = E_{PR_{\text{Bob}}}\Big(H\big(H(PI_{\text{Bob}}) \parallel H(OI_{\text{Bob}})\big)\Big)$$
- Because $H(OI_{\text{Alice}}) \neq H(OI_{\text{Bob}})$, the hashes do not match. The bank immediately rejects the transaction as fraudulent!

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part D, Q18(a) - 4 Marks]
**Question**: Illustrate the relevance of dual signature in SET.

**Solution**:
1. **Relevance and The Problem in E-Commerce**:
   In electronic commerce, a customer purchases goods from an online merchant using a credit card issued by a bank. Two competing privacy requirements exist:
   - **Merchant Privacy**: The merchant must receive the Order Information ($OI$) to know what items to ship, but the merchant should **NOT** see the customer's credit card number ($PI$) to avoid exposing the customer to credit card theft or insider fraud.
   - **Bank Privacy**: The bank (Payment Gateway) must receive the Payment Information ($PI$) to authorize payment, but the bank should **NOT** know the detailed contents of the customer's purchase ($OI$) to preserve customer privacy.
   - **The Linkage Need**: The customer must prove to the bank that the payment authorization is tied to this specific order, and prove to the merchant that the payment was authorized for these specific goods, without either party seeing the other's data.

2. **How Dual Signature Solves the Problem**:
   The customer creates a **Dual Signature ($DS$)** by computing the hash of both messages separately, concatenating the two hashes, and signing the combined hash with their private key:
   $$\mathbf{DS = E_{PR_C}\Big(H\big(H(PI) \parallel H(OI)\big)\Big)}$$
   - The merchant receives $(OI, H(PI), DS)$. The merchant can compute $H(OI)$, combine it with $H(PI)$, and verify $DS$ using the customer's public key $PU_C$ without ever learning $PI$!
   - The bank receives $(PI, H(OI), DS)$. The bank can compute $H(PI)$, combine it with $H(OI)$, and verify $DS$ using $PU_C$ without ever learning $OI$!
   - Neither party can modify their portion of the transaction because any change to $OI$ or $PI$ alters the hash and invalidates the dual signature.

---

### Question 2 [KTU January 2023, Part D, Q19(b) / June 2022, Part D, Q19(b) - 6 Marks]
**Question**: Explain the sequence of operations required for Secure Electronic Transaction (SET).

**Solution**:
A complete Secure Electronic Transaction (SET) encompasses six chronological phases across the Cardholder, Merchant, and Payment Gateway:

1. **Phase 1: Cardholder Registration & Cardholder Account Setup**:
   The cardholder applies for and obtains a digital certificate from a Certificate Authority (CA) associated with the payment brand (Visa/MasterCard). The public key in the certificate is bound to the cardholder's credit card account.
2. **Phase 2: Merchant Registration**:
   The merchant establishes an account with an acquiring bank and obtains two digital certificates: one for public-key encryption and one for digital signatures.
3. **Phase 3: Purchase Request & Order Placement**:
   - The cardholder browses the merchant website, selects items, and requests an order invoice.
   - The merchant sends an invoice containing order details and transaction identifiers.
   - The cardholder's wallet software prepares the Order Information ($OI$) and Payment Information ($PI$).
   - The cardholder generates the **Dual Signature ($DS$)**:
     $$DS = E_{PR_C}\Big(H\big(H(PI) \parallel H(OI)\big)\Big)$$
   - The cardholder encrypts $PI$ with the Payment Gateway's public key.
   - The cardholder sends the package to the merchant: $(OI, H(PI), DS)$ and the encrypted $PI$ block.
4. **Phase 4: Payment Authorization Request**:
   - The merchant verifies the cardholder's certificate and verifies the Dual Signature over $OI$ and $H(PI)$.
   - The merchant generates an authorization request message and forwards the encrypted payment package to the Payment Gateway.
5. **Phase 5: Payment Authorization & Banking Verification**:
   - The Payment Gateway decrypts $PI$ using its private key.
   - The Payment Gateway verifies the cardholder's certificate and verifies the Dual Signature over $PI$ and $H(OI)$.
   - The Payment Gateway connects over the private financial network (VisaNet/MasterCard BankNet) to the cardholder's issuing bank to verify account standing and reserve credit.
   - Upon approval from the issuing bank, the Payment Gateway returns an encrypted authorization response to the merchant.
6. **Phase 6: Order Fulfillment & Payment Capture**:
   - The merchant receives the authorization confirmation and sends an order confirmation message to the cardholder.
   - The merchant ships the purchased goods.
   - At settlement time, the merchant sends a capture request to the Payment Gateway to transfer funds from the cardholder's account to the merchant's account.
