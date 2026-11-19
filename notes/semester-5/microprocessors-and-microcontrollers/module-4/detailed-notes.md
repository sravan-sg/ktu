# Module IV: Memory/IO Interfacing, 8255, 8279, 8257 — Master Detailed Notes

> **CS305 Microprocessors and Microcontrollers** | Semester 5 | KTU Scheme

---

## Module Overview

Module IV explores how the 8086 microprocessor bridges the high-speed system bus to physical semiconductor memory and peripheral hardware. It covers memory banking (even/odd banks), address decoding techniques, isolated vs memory-mapped I/O, and three primary Intel LSI interface chips: 8255A (PPI), 8279 (Keyboard/Display), and 8257 (DMA Controller).

---

## Detailed Topic Guides

1. [Memory and I/O Interfacing with 8086](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-4/memory-and-io-interfacing.md)
   - 8086 1 MB physical memory architecture split into $512\text{ KB}$ Even Bank ($A_0 = 0, D_7 - D_0$) and $512\text{ KB}$ Odd Bank ($\overline{\text{BHE}} = 0, D_{15} - D_8$).
   - Aligned vs. misaligned word access bus cycles and performance penalties.
   - Address decoding principles: Full decoding vs Partial decoding (address aliasing).
   - 74LS138 3-to-8 decoder operation and truth table.
   - Comparative architectural analysis: Memory-Mapped I/O vs. Isolated (I/O-Mapped) I/O.
   - 3 solved numerical examples (64 KB EPROM/SRAM design, wait state insertion calculations, and isolated I/O decoder design) and full KTU examination solutions.

2. [8255 Programmable Peripheral Interface (PPI)](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-4/8255-programmable-peripheral-interface.md)
   - Internal architecture: Port A, Port B, Port C Upper/Lower, Group A/B control blocks, Read/Write control logic.
   - Operating Modes: Mode 0 (Basic I/O), Mode 1 (Strobed Handshake I/O: $\overline{\text{STB}}, \text{IBF}, \overline{\text{OBF}}, \overline{\text{ACK}}, \text{INTR}$), Mode 2 (Strobed Bidirectional Bus on Port A).
   - Control word formats: Mode Set definition word ($D_7 = 1$) and Bit Set/Reset (BSR) word ($D_7 = 0$).
   - 3 complete solved numerical and assembly examples (Control word computation, DIP switch to LED bar interface driver, and 2-phase stepper motor sequence controller) with step-by-step PYQ solutions.

3. [8279 and 8257 Interfacing](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-4/8279-and-8257-interfacing.md)
   - **8279 Programmable Keyboard/Display Controller**: Keyboard matrix scanning ($8 \times 8 = 64$ keys), 10 ms debouncing, 2-Key Lockout vs. N-Key Rollover, 8-byte FIFO RAM, 16-character Display RAM, Left vs. Right entry modes.
   - **8257 Direct Memory Access (DMA) Controller**: DMA principles and bus arbitration handshake (`HOLD` / `HLDA`), 4 channels with DMA Address Registers and Terminal Count Registers, single-cycle direct transfers, transfer modes (Read, Write, Verify).
   - 3 solved analytical problems (Terminal Count calculation, 8279 clock prescaler derivation, and Cycle-Stealing vs. Burst mode throughput comparison) and detailed KTU PYQ solutions.

---

## Quick Navigation

- [Module IV Revision Notes](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-4/revision-notes.md)
- [Subject Root Index](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/README.md)

