# Module IV: Memory/IO Interfacing, 8255, 8279, 8257 — Revision Notes

> **Quick Revision Guide for Internal & University Exams** | CS305 Semester 5

---

## 1. High-Yield Core Concepts & Formulae

### 1. 8086 Memory Banking Architecture
- **Bank Organization**: 1 MB address space split into Even Bank ($512\text{ KB}$, $A_0 = 0$, $D_7 - D_0$) and Odd Bank ($512\text{ KB}$, $\overline{\text{BHE}} = 0$, $D_{15} - D_8$).
- **Bank Selection**:
  - Even Byte: $A_0 = 0, \overline{\text{BHE}} = 1$ (1 cycle, $D_7 - D_0$).
  - Odd Byte: $A_0 = 1, \overline{\text{BHE}} = 0$ (1 cycle, $D_{15} - D_8$).
  - Aligned Word: $A_0 = 0, \overline{\text{BHE}} = 0$ (1 cycle, $D_{15} - D_0$).
  - Misaligned Word: Starts at odd address; takes **2 consecutive cycles** (8 T-states total).
- **Chip Address Line Rule**: An $N$-byte memory chip uses CPU address lines $A_k - A_1$ (NOT $A_0$). $A_0$ is used exclusively for bank enabling.

### 2. Isolated I/O vs. Memory-Mapped I/O
- **Isolated I/O**: Separate 64 KB port space, accessed via `IN`/`OUT`, uses $M/\overline{\text{IO}} = 0$ and $\overline{\text{IOR}} / \overline{\text{IOW}}$, faster execution, simpler decoding.
- **Memory-Mapped I/O**: Shares 1 MB memory space, accessed via standard memory instructions (`MOV`, `TEST`, etc.), uses $M/\overline{\text{IO}} = 1$ and $\overline{\text{MEMR}} / \overline{\text{MEMW}}$, flexible addressing, larger decoder logic.

### 3. 8255 PPI Control Words Summary
- **Mode Definition Word ($D_7 = 1$)**:
  - $D_6 D_5$: Port A Mode (`00` = Mode 0, `01` = Mode 1, `1X` = Mode 2).
  - $D_4$: Port A Direction ($1 = \text{In}, 0 = \text{Out}$).
  - $D_3$: Port C Upper Direction ($1 = \text{In}, 0 = \text{Out}$).
  - $D_2$: Port B Mode ($0 = \text{Mode 0}, 1 = \text{Mode 1}$).
  - $D_1$: Port B Direction ($1 = \text{In}, 0 = \text{Out}$).
  - $D_0$: Port C Lower Direction ($1 = \text{In}, 0 = \text{Out}$).
- **BSR Mode ($D_7 = 0$)**: Modifies single Port C bit. Bits $D_3 D_2 D_1$ select bit ($0-7$); $D_0 = 1$ (Set), $0$ (Reset).

### 4. 8255 Mode 1 Handshake Signals
- **Strobed Input**: $\overline{\text{STB}}$ (strobe from device), $\text{IBF}$ (input buffer full), $\text{INTR}$ (interrupt to CPU).
- **Strobed Output**: $\overline{\text{OBF}}$ (output buffer full), $\overline{\text{ACK}}$ (acknowledge from device), $\text{INTR}$ (buffer empty interrupt).

### 5. 8279 & 8257 Key Parameters
- **8279**: 64-key matrix ($8 \times 8$), 10 ms debouncing, 8-byte FIFO, 16-character Display RAM, Left vs Right entry.
- **8257 DMA**: 4 channels, DAR (16-bit address), TCR (14-bit count + 2-bit mode), `HOLD`/`HLDA` arbitration, single-cycle Memory $\leftrightarrow$ I/O transfer.

---

## 2. Frequently Asked Exam Questions & Diagram Pitfalls

1. **8255 Interfacing & Control Word Problem**: Part D of the KTU exam consistently features a 9-mark problem asking to calculate the control word for a specified I/O configuration (e.g., Port A input, Port B output, Port C Upper output) and write an assembly program. Always verify bit $D_7 = 1$ for Mode Set.

2. **Memory Banking Aligned vs. Misaligned**: When asked why a misaligned 16-bit word takes 2 bus cycles, draw the two cycles explicitly: Cycle 1 reads the low byte at the odd address over $D_{15} - D_8$, and Cycle 2 reads the high byte at the next even address over $D_7 - D_0$.

3. **8257 DMA Timing**: Show clearly that during DMA transfer, the CPU address and data lines are in High-Z, `AEN` disables CPU buffers, and the 8257 asserts $\overline{\text{IOR}}$ and $\overline{\text{MEMW}}$ simultaneously so data flows directly from peripheral to memory in 1 clock cycle without entering any CPU register.

---

## 3. Comparison Cheat Sheets

### 8255 Modes Comparison

| Feature | Mode 0 | Mode 1 | Mode 2 |
|---|---|---|---|
| **Description** | Basic I/O | Strobed Handshake I/O | Bidirectional Strobed Bus |
| **Ports Supported** | Port A, Port B, Port C | Port A, Port B | Port A only |
| **Handshake Used?** | No | Yes (via Port C pins) | Yes (via 5 Port C pins) |
| **Latching** | Outputs latched; Inputs unlatched | Inputs & Outputs latched | Inputs & Outputs latched |
| **Interrupts** | None | Hardware `INTR` line | Hardware `INTR` line |

---

## 4. 10-Minute Rapid Revision Checklist

- [ ] Can you write down the 8255 control word for Port A Mode 0 In, Port B Mode 0 Out, Port C Upper Out, Port C Lower In? (`91H`).
- [ ] What is the BSR command byte to set pin $\text{PC}_6$? (`0000 1101B = 0DH`).
- [ ] Why doesn't the 8086 connect address line $A_0$ to memory chip address inputs? (Because $A_0$ is used exclusively to enable the Even Bank).
- [ ] What are the functions of $\overline{\text{STB}}$ and $\text{IBF}$ in 8255 Mode 1 Input? ($\overline{\text{STB}}$ latches data from peripheral; $\text{IBF}$ warns peripheral not to send more).
- [ ] How does the 8257 DMA controller take control of the system bus? (Asserts `HOLD` to CPU; CPU responds with `HLDA` and floats its bus).

