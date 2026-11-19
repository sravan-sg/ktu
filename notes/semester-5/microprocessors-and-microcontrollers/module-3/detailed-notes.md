# Module III: Interrupts & 8259 PIC — Master Detailed Notes

> **CS305 Microprocessors and Microcontrollers** | Semester 5 | KTU Scheme

---

## Module Overview

Module III covers the complete interrupt structure of the 8086 microprocessor and the architecture, programming, and cascading of the Intel 8259A Programmable Interrupt Controller (PIC).

---

## Detailed Topic Guides

1. [Interrupts and Interrupt Handling](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-3/interrupts-and-interrupt-handling.md)
   - Classification of 8086 interrupts (Hardware, Software, Internal/Dedicated).
   - Detailed breakdown of Dedicated Interrupts (Types 0, 1, 2, 3, 4).
   - Interrupt Vector Table (IVT) 1KB physical organization and address calculation ($00000\text{H} - 003\text{FF}\text{H}$).
   - Hardware interrupt processing sequence (two-cycle INTA# bus protocol).
   - Step-by-step ISR execution cycle: PUSH FLAGS, clear IF/TF, PUSH CS, PUSH IP, fetch new CS:IP, execute, IRET restoration.
   - Comprehensive numerical and analytical examples with fully worked KTU past exam problems.

2. [8259 Programmable Interrupt Controller](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-3/8259-programmable-interrupt-controller.md)
   - Why an external interrupt controller is essential: eliminating polling latency and hardware priority arbitration.
   - Internal architecture and detailed functional blocks: IRR, ISR, IMR, Priority Resolver, Cascade Buffer/Comparator, Data Bus Buffer, Read/Write Control Logic.
   - Two-cycle INTA# handshake protocol between 8086 and 8259.
   - Initialization Command Words (ICW1, ICW2, ICW3, ICW4) state machine and bit formats.
   - Operational Command Words (OCW1, OCW2, OCW3): masking, non-specific/specific EOI, priority rotation, register status reading, and polled mode.
   - Master-Slave cascading topology for expanding up to 64 prioritized interrupts.
   - 3 solved numerical examples (calculating ICWs for Master and Slaves, vector address derivation, and OCW decoding) and complete self-contained PYQ solutions.

---

## Quick Navigation

- [Module III Revision Notes](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/module-3/revision-notes.md)
- [Subject Root Index](file:///home/sravan/ktu/notes/semester-5/microprocessors-and-microcontrollers/README.md)

