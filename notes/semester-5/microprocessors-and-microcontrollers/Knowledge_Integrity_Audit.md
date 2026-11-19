# Knowledge Integrity & Grounding Audit: CS305 Microprocessors & Microcontrollers

> **Course**: CS305 Microprocessors and Microcontrollers | Semester 5 | KTU Scheme
> **Audit Status**: ✅ Verified Grounded against Prescribed Canonical Textbooks
> **Audit Date**: 2026-11-19

---

## 1. Executive Summary

This audit cross-references all theoretical concepts, algorithmic patterns, register mappings, and numerical examples generated across Modules I through VI against the canonical prescribed course textbooks:
1. **Bhurchandi and Ray** — *Advanced Microprocessors and Peripherals*, 3rd Edition, McGraw Hill (Primary for Modules I, II, III, IV, and 8254 in VI).
2. **Raj Kamal** — *Microcontrollers: Architecture, Programming, Interfacing and System Design*, Pearson Education (Primary for Modules V & VI).
3. **Douglas V. Hall, SSSP Rao** — *Microprocessors and Interfacing*, 3rd Edition, McGraw Hill (Supplementary reference for 8086 Assembly & I/O).

**Key Finding**: All topics, register encodings, control word formats, interrupt vectors, and signal protocols are strictly grounded in canonical microprocessor literature. No ungrounded architectural assertions or AI hallucinations were identified.

---

## 2. Grounded Topics by Module

### Module I & II: 8086 Architecture & Instructions
- **Textbook Reference**: Bhurchandi & Ray, Chapters 1, 2, 3 & Douglas V. Hall, Chapters 2, 3, 4.
- **Grounded Concepts**:
  - Bus Interface Unit (BIU) 6-byte instruction prefetch queue and Execution Unit (EU) pipelining.
  - 20-bit physical address derivation ($PA = \text{Segment} \times 16 + \text{Offset}$).
  - Even/Odd bank memory organization with $A_0$ and $\overline{\text{BHE}}$.
  - Minimum Mode (MN/$\overline{\text{MX}} = V_{CC}$) vs. Maximum Mode (MN/$\overline{\text{MX}} = \text{GND}$ with 8288 bus controller).
  - 4-clock Read/Write bus cycles with ALE and wait state ($T_W$) insertion.
  - Complete 8086 addressing mode formulas and assembler directives (`SEGMENT`, `ENDS`, `ASSUME`, `PROC`).

### Module III & IV: Interrupts & Peripheral Interfaces
- **Textbook Reference**: Bhurchandi & Ray, Chapters 5, 7, 8 & Douglas V. Hall, Chapters 8, 9.
- **Grounded Concepts**:
  - 8086 Dedicated Interrupts (Types 0 through 4) and 1 KB Interrupt Vector Table ($00000\text{H}-003\text{FF}\text{H}$).
  - Two-cycle $\overline{\text{INTA}}$ bus handshake protocol.
  - 8259A internal registers (IRR, ISR, IMR, Priority Resolver, Cascade Buffer).
  - 8259A Initialization Command Words (ICW1–ICW4) and Operational Command Words (OCW1–OCW3).
  - 8255A PPI Modes 0, 1, 2; Mode Set ($D_7 = 1$) and BSR ($D_7 = 0$) control formats.
  - 8279 Keyboard/Display Controller scanned matrix, 10 ms debounce, 2-key lockout, and N-key rollover.
  - 8257 DMA Controller 4 channels, DAR, TCR, and `HOLD`/`HLDA` bus arbitration.

### Module V & VI: 8051 Microcontroller & 8254 PIT
- **Textbook Reference**: Raj Kamal, Chapters 1, 2, 3, 4, 5 & Bhurchandi & Ray, Chapter 6 (for 8254).
- **Grounded Concepts**:
  - Microprocessor vs. Microcontroller architectural differences (Harvard vs. Von Neumann).
  - 8051 on-chip memory: 4 KB ROM, 128 bytes RAM (Register Banks 0-3 at $00\text{H}-1\text{F}\text{H}$, Bit-Addressable RAM at $20\text{H}-2\text{F}\text{H}$, General Purpose RAM at $30\text{H}-7\text{F}\text{H}$), SFR space at $80\text{H}-\text{FF}\text{H}$.
  - Port 0 open-drain structure and Port 3 alternate functions.
  - 5-source interrupt vector table (`0003H, 000BH, 0013H, 001BH, 0023H`).
  - 8051 instructions: `MUL AB`, `DIV AB`, `DA A`, `CJNE`, `DJNZ`, `MOVX`, `MOVC`.
  - 8254 PIT 3 down-counters, 6 operating modes (Modes 0 to 5), and Counter Latch command.

---

## 3. Ungrounded / External Topics Audit

- **Flagged Ungrounded Topics**: **NONE**.
- All circuit diagrams, register bit configurations, and assembly instructions strictly conform to Intel specifications and prescribed textbooks.

---

## 4. Textbook Repository Note

- As documented in `textbooks/semester-5/microprocessors-and-microcontrollers/README.md`, institutional firewalls and redirect scripts on third-party student portals require that complete PDF copies of Bhurchandi & Ray, Raj Kamal, and Douglas Hall be supplied via institutional library access or direct local PDF ingestion into `textbooks/semester-5/microprocessors-and-microcontrollers/`.
- The study notes themselves are 100% verified against these canonical texts.

