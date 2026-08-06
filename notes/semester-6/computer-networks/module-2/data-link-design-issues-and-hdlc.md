# Module 2 — Topic 1: Data Link Layer Design Issues & HDLC Protocol

> **Module 2**: Data Link Layer & Medium Access Control  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Data Link Layer (DLL)** is responsible for transmitting raw bits from the Physical Layer into reliable, error-free **frames** across a single physical link between two directly connected nodes.

**Primary Design Functions**:
1. **Framing**: Grouping bits into distinct frames. Methods include:
   - *Character Count*: Uses a length field (vulnerable to count corruption).
   - *Byte Stuffing (Character Stuffing)*: Inserts `DLE` escape bytes before flag-like control data.
   - *Bit Stuffing*: In flag sequence `01111110` (6 consecutive 1s), sender automatically inserts a `0` bit after any sequence of 5 consecutive `1`s. Receiver strips the stuffed `0`.
2. **Error Control**: Detecting and correcting errors using Checksums and **Cyclic Redundancy Checks (CRC)** using generator polynomials.
3. **Flow Control**: Preventing sender from overflowing receiver buffers.
4. **HDLC (High-Level Data Link Control)**: A bit-oriented protocol specifying three frame types:
   - **Information (I-frame)**: Carries user data and piggybacked ACKs.
   - **Supervisory (S-frame)**: Carries flow/error control (RR, RNR, REJ, SREJ).
   - **Unnumbered (U-frame)**: Connection management (SABM, DISC, UA).

### Example
Think of Bit Stuffing like sending a telegram:
If the codeword "STOP" is used to end a telegram message, but your message text contains the word "STOP", the operator adds "ESCAPE STOP" (stuffing) so the recipient doesn't prematurely assume the message ended.

### Applications & Use Cases
- **Point-to-Point Protocol (PPP)**: Used by ISPs over DSL lines, relying on HDLC framing rules and bit stuffing.
- **Ethernet Frame Check Sequence (FCS)**: Uses CRC-32 polynomials to detect transmission bit flips.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Bit Stuffing Algorithm Trace
**Problem:** Given the raw data bit stream `011111100011111111110010`, perform bit stuffing according to HDLC rules (flag = `01111110`).
**Step-by-step Solution:**
1. Rule: Whenever 5 consecutive `1`s are encountered in data, insert a stuffed `0`.
2. Scan data stream:
   - `0`
   - `11111` $\rightarrow$ 5 ones! Insert stuffed `0` $\rightarrow$ `0111110`
   - `1`
   - `000`
   - `11111` $\rightarrow$ 5 ones! Insert stuffed `0` $\rightarrow$ `0111110`
   - `11111` $\rightarrow$ 5 ones! Insert stuffed `0` $\rightarrow$ `0111110`
   - `0010`
3. **Stuffed Output Stream:** `011111010001111101111100010`
4. **Total Stuffed Bits:** 3 zeros stuffed. Frame is framed between flags: `01111110 [011111010001111101111100010] 01111110`.

### Example 2: Cyclic Redundancy Check (CRC) Generation
**Problem:** A sender wants to transmit data bit pattern $D = 110101$ using generator polynomial $G(x) = x^3 + x + 1$ (binary $1011$). Calculate the 3-bit CRC checksum $R$ and the final frame transmitted.
**Step-by-step Solution:**
1. **Identify Generator Parameters:**
   - Generator $G = 1011$ (Degree $r = 3$).
2. **Append $r = 3$ zeros to Data:**
   - Appended Data $D' = 110101000$.
3. **Perform Polynomial Modulo-2 Division ($D' / G$ using XOR):**
   ```text
   110101000 / 1011
   110101000
   1011
   -----
   011001000
    1011
    ----
    01111000
     1011
     ----
     0100000
      1011
      ----
      001100
       1011
       ----
       0111 (Remainder R = 111)
   ```
4. **CRC Checksum $R$:** `111`.
5. **Final Transmitted Frame ($D + R$):** `110101111`.

### Example 3: HDLC Frame Structure and Control Field Decoding
**Problem:** Decode the following HDLC control field byte: `10010010`. Identify the frame type, $N(R)$, $N(S)$, or S-frame function.
**Step-by-step Solution:**
1. **Examine First Bits:**
   - Bit 1 is `1` $\implies$ Not an I-frame (I-frames start with `0`).
   - Bit 2 is `0` $\implies$ Control byte starting with `10` represents a **Supervisory Frame (S-frame)**.
2. **Decode S-Frame Functions:**
   - Bits 3-4 (`01`) $\implies$ Code `01` represents **REJ (Reject)** command/response.
   - Bit 5 (`0`) $\implies$ Poll/Final (P/F) bit is `0`.
   - Bits 6-8 (`010` = decimal 2) $\implies$ $N(R) = 2$ (acknowledges frames up to 1, expects frame 2).
3. **Conclusion:** It is a **Supervisory REJ Frame** requesting retransmission starting from frame 2.

---

## 3. Previous Year Questions & Solutions

1. **"Explain Bit Stuffing and Byte Stuffing with suitable examples." [May 2019]**
   - **Solution:**
     - **Bit Stuffing:** Used in bit-oriented protocols (HDLC). To prevent data containing flag patterns (`01111110`) from truncating frames, the sender inserts a `0` after any sequence of 5 consecutive `1`s. Receiver deletes `0` after 5 ones. Example: `111111` becomes `1111101`.
     - **Byte Stuffing:** Used in byte-oriented protocols. Inserts a special `DLE` (Data Link Escape) byte before any control byte appearing inside user payload. Example: `DLE STX Data DLE DLE Data DLE ETX`.

2. **"Generate CRC for message 1100101 using generator polynomial x^3 + x^2 + 1." [Dec 2019]**
   - **Solution:**
     1. $G(x) = x^3 + x^2 + 0x + 1 \implies 1101$ ($r = 3$).
     2. Appended Data: $1100101000$.
     3. Modulo-2 Division:
        - $1100101000 \oplus 1101000000 \implies 0001101000$
        - Divide $11010000$ by $1101 \implies$ Remainder $R = 001$.
     4. Transmitted Frame: `1100101001`.
