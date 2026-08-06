# Module 2 — Topic 1: Data Link Layer Design Issues & HDLC Protocol

> **Module 2**: Data Link Layer & Medium Access Control  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Data Link Layer (DLL)** converts raw bit streams received from the Physical Layer into distinct, error-free **Frames** across a single physical communication link between two adjacent nodes.

---

### Primary Functions of Data Link Layer

#### 1. Framing Methods
Framing partitions the bit stream into discrete, recognizable units:
- **Character Count**: Uses a length field in the header specifying total characters in the frame. Vulnerable because a single corrupted length byte desynchronizes all subsequent frames.
- **Byte Stuffing (Character Stuffing)**: Used in byte-oriented protocols. Wraps frames in flag bytes (e.g. `STX` / `ETX`). If a data payload contains a byte matching a flag, the sender prepends a `DLE` (Data Link Escape) byte.
- **Bit Stuffing**: Used in bit-oriented protocols (HDLC, SDLC).
  - Frames are bounded by flag bit pattern `01111110` (6 consecutive `1`s).
  - **Sender Rule**: Whenever 5 consecutive `1`s appear in user payload, the sender automatically inserts a stuffed `0` bit after the 5th `1`.
  - **Receiver Rule**: Whenever 5 consecutive `1`s followed by a `0` are received, the receiver automatically strips the `0` bit. If 6 consecutive `1`s appear, it marks the end flag.

---

#### 2. Error Control & Cyclic Redundancy Check (CRC)
- Detects bit flips caused by physical channel noise using generator polynomials $G(x)$ of degree $r$:
  - Generator polynomial $G(x) = x^3 + x + 1 \implies 1011$ ($r = 3$).
  - Appends $r$ zeros to data $D$, divides $(D \cdot 2^r)$ by $G$ using modulo-2 binary division (XOR operations).
  - Transmits $D$ concatenated with remainder $R$. If receiver's division yields remainder $0$, frame is error-free.

---

#### 3. HDLC Protocol Architecture (High-Level Data Link Control)
Bit-oriented standard defining 3 node configurations (Primary, Secondary, Combined), 2 transfer modes (Normal Response Mode NRM, Asynchronous Balanced Mode ABM), and 3 frame types:

```text
  Information (I-frame)  │ 0 │   N(S)   │ P/F │   N(R)   │
                         ├───┴──────────┼─────┼──────────┤
  Supervisory (S-frame)  │ 1 0 │ Type   │ P/F │   N(R)   │
                         ──────┴────────┼─────┼──────────┤
  Unnumbered (U-frame)   │ 1 1 │ Type   │ P/F │ Type     │
```

- **Information Frame (I-frame)**: Transmits user payload data; piggybacks sequence number $N(S)$ and ACK number $N(R)$.
- **Supervisory Frame (S-frame)**: Transmits flow and error control commands:
  - `RR` (Receive Ready - `00`): Acknowledges frames up to $N(R)-1$.
  - `RNR` (Receive Not Ready - `10`): Acknowledges frames, requests sender to pause.
  - `REJ` (Reject - `01`): Go-Back-N negative ACK requesting retransmission from $N(R)$.
  - `SREJ` (Selective Reject - `11`): Selective Repeat negative ACK requesting single frame $N(R)$.
- **Unnumbered Frame (U-frame)**: Connection management (e.g. `SABM` set asynchronous balanced mode, `DISC` disconnect, `UA` unnumbered ACK).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Bit Stuffing & Destuffing Trace
**Problem:** A sender wants to transmit raw data bit stream `011111100011111111110010`.
(a) Perform bit stuffing according to HDLC rules.
(b) Show the destuffing operation at the receiver.
**Step-by-step Solution:**
1. **Bit Stuffing at Sender:**
   - Scan data: `0` `11111` $\rightarrow$ insert `0` $\rightarrow$ `0111110` `1000` `11111` $\rightarrow$ insert `0` $\rightarrow$ `0111110` `11111` $\rightarrow$ insert `0` $\rightarrow$ `0111110` `010`.
   - Stuffed Payload: `011111010001111101111100010`.
   - Transmitted Frame: `01111110` [ `011111010001111101111100010` ] `01111110`.
2. **Bit Destuffing at Receiver:**
   - Detects flag boundaries `01111110`.
   - Strips stuffed zeros after 5 consecutive ones $\implies$ Restores original data `011111100011111111110010`.

### Example 2: Cyclic Redundancy Check (CRC-32) Generation Math
**Problem:** Data $D = 110101$. Generator polynomial $G(x) = x^3 + x + 1$ (binary $1011$).
Calculate 3-bit CRC checksum $R$ and show receiver error verification when bit 3 flips during transmission.
**Step-by-step Solution:**
1. **Sender CRC Generation:**
   - Append $r = 3$ zeros: $D' = 110101000$.
   - Modulo-2 Division $110101000 / 1011 \implies$ Remainder $R = 111$.
   - Transmitted Frame $T = 110101111$.
2. **Receiver Error Verification (No Error):**
   - Modulo-2 Division $110101111 / 1011 \implies$ Remainder $= 000 \implies \mathbf{Accepted}$.
3. **Receiver Error Verification (Bit 3 Flips to `111101111`):**
   - Modulo-2 Division $111101111 / 1011 \implies$ Remainder $= 110 \neq 000 \implies \mathbf{Corrupted! Discarded}$.

### Example 3: HDLC Control Field Decoding
**Problem:** Decode HDLC control field byte `10010010`. Identify frame type, P/F bit, and ACK number $N(R)$.
**Step-by-step Solution:**
1. Bits 1-2 are `10` $\implies$ **Supervisory Frame (S-frame)**.
2. Bits 3-4 are `01` $\implies$ Type code `01` represents **REJ (Reject)** command.
3. Bit 5 is `0` $\implies$ Poll/Final (P/F) bit is `0`.
4. Bits 6-8 are `010` $= 2_{10} \implies N(R) = 2$.
5. **Meaning:** S-frame REJ requesting Go-Back-N retransmission starting from frame 2.

---

## 3. Previous Year Questions & Solutions

1. **"Explain Bit Stuffing and Byte Stuffing with suitable examples." [May 2019]**
   - **Solution:**
     - **Bit Stuffing:** In bit-oriented protocols (HDLC), sender inserts a `0` bit after any 5 consecutive `1`s in payload to prevent premature flag (`01111110`) detection. Receiver strips `0` after 5 ones. Example: `111111` becomes `1111101`.
     - **Byte Stuffing:** In byte-oriented protocols, sender inserts a `DLE` escape byte before any control byte appearing inside payload. Example: `DLE STX Data DLE DLE Data DLE ETX`.

2. **"Explain HDLC frame format and frame types (I-frame, S-frame, U-frame)." [Dec 2019]**
   - **Solution:**
     - **I-frame (Information)**: Starts with `0`. Carries payload data, $N(S)$ sequence number, and $N(R)$ ACK number.
     - **S-frame (Supervisory)**: Starts with `10`. Carries flow/error control: `RR` (Receive Ready), `RNR` (Receive Not Ready), `REJ` (Reject), `SREJ` (Selective Reject).
     - **U-frame (Unnumbered)**: Starts with `11`. Carries link setup/teardown commands (`SABM`, `DISC`, `UA`).
