# Module V: 8051 Microcontroller Architecture — Master Detailed Notes

> **CS305 Microprocessors and Microcontrollers** | Semester 5 | KTU Scheme

---

## Module Overview

Module V introduces microcontroller fundamentals, selection criteria, and an exhaustive examination of the **Intel 8051 Microcontroller Architecture**. This module represents a substantial component (**20% course weightage**, forming part of the 40-mark Part E in the university examination).

---

## Detailed Topic Guides

1. [Microcontroller Fundamentals and Selection Criteria](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-5/microcontroller-fundamentals-and-selection.md)
   - Conceptual definition of microcontrollers as single-chip microcomputers.
   - Microprocessor vs. Microcontroller comprehensive architectural comparison (Von Neumann vs. Harvard, bus layout, instruction sets, power, packaging).
   - Microcontroller classification by bit-width (4-bit, 8-bit, 16-bit, 32-bit ARM Cortex-M).
   - Selection criteria for commercial designs (word length, clock speed, Flash/RAM sizing, I/O pin count, analog/digital peripherals, power consumption, BOM cost).
   - 3 solved numerical examples (battery lifetime derivation for IoT nodes, memory sizing with headroom, and board-level BOM cost trade-off) with full KTU PYQ solutions.

2. [8051 Microcontroller Architecture](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-5/8051-architecture.md)
   - Complete 8051 block diagram: CPU, 8-bit Accumulator (A), B register, Program Status Word (PSW).
   - Internal memory organization:
     - 4 KB on-chip ROM ($0000\text{H} - 0\text{FFF}\text{H}$) and external memory expansion up to 64 KB using $\overline{\text{EA}}$ and $\overline{\text{PSEN}}$.
     - 128 bytes on-chip RAM: 4 Register Banks ($00\text{H}-1\text{F}\text{H}$), Bit-addressable area ($20\text{H}-2\text{F}\text{H}$, 128 individual bits), General-purpose RAM ($30\text{H}-7\text{F}\text{H}$).
     - Special Function Register (SFR) area ($80\text{H}-\text{FF}\text{H}$).
   - Four 8-bit I/O Ports: Port 0 (open-drain, multiplexed $AD_0-AD_7$), Port 1 (quasi-bidirectional GPIO), Port 2 (high address bus $A_8-A_{15}$), Port 3 (dual-function lines: TXD, RXD, $\overline{\text{INT0}}, \overline{\text{INT1}}$, T0, T1, $\overline{\text{WR}}, \overline{\text{RD}}$).
   - Hardware Timers (Timer 0, Timer 1) and operating modes (Modes 0, 1, 2, 3) using `TMOD` and `TCON`.
   - Serial communication UART and `SCON` register.
   - 5-source interrupt structure (Vector addresses, `IE`, `IP` priority registers).
   - 3 detailed analytical examples and university exam solutions.

---

## Quick Navigation

- [Module V Revision Notes](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-5/revision-notes.md)
- [Subject Root Index](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/README.md)

