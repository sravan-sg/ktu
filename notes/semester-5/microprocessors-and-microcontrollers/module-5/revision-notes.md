# Module V: 8051 Microcontroller Architecture — Revision Notes

> **Quick Revision Guide for Internal & University Exams** | CS305 Semester 5

---

## 1. High-Yield Core Concepts & Formulae

### 1. Microprocessor vs. Microcontroller
- **Microprocessor**: CPU only on silicon; needs external RAM, ROM, I/O, timers; Von Neumann architecture; general-purpose computing.
- **Microcontroller**: Single silicon chip integrating CPU, RAM, Flash/ROM, I/O ports, timers, UART, ADC; Harvard architecture; dedicated real-time control.

### 2. 8051 Internal Memory Map (Crucial Exam Topic!)
- **Program Memory (ROM)**: 4 KB on-chip ($0000\text{H} - 0\text{FFF}\text{H}$). If $\overline{\text{EA}} = 0$, CPU executes exclusively from external ROM ($0000\text{H} - \text{FFFF}\text{H}$). If $\overline{\text{EA}} = 1$, executes internal ROM first, then external ROM ($1000\text{H} - \text{FFFF}\text{H}$).
- **Data Memory (RAM — 128 Bytes total, $00\text{H} - 7\text{F}\text{H}$)**:
  1. **Bank 0 to Bank 3 ($00\text{H} - 1\text{F}\text{H}$)**: 4 banks of 8 registers each ($R_0 - R_7$). Selected by bits `RS1:RS0` in PSW.
  2. **Bit-Addressable RAM ($20\text{H} - 2\text{F}\text{H}$)**: 16 bytes = 128 individually addressable bits (bit addresses $00\text{H} - 7\text{F}\text{H}$).
  3. **General-Purpose Scratchpad RAM ($30\text{H} - 7\text{F}\text{H}$)**: 80 bytes for variables and stack.
- **SFR Area ($80\text{H} - \text{FF}\text{H}$)**: Direct addressing only. Addresses ending in $0\text{H}$ or $8\text{H}$ are bit-addressable (`ACC`, `B`, `PSW`, `P0-P3`, `IE`, `IP`, `TCON`, `SCON`).

### 3. Program Status Word (PSW) Register
- Bits: $\text{CY} (D_7), \text{AC} (D_6), \text{F0} (D_5), \text{RS1} (D_4), \text{RS0} (D_3), \text{OV} (D_2), \text{F1} (D_1), \text{P} (D_0)$.
- `RS1:RS0`: `00` = Bank 0 (`00H-07H`), `01` = Bank 1 (`08H-0FH`), `10` = Bank 2 (`10H-17H`), `11` = Bank 3 (`18H-1FH`).
- `P` (Parity): 1 if Accumulator has an odd number of 1s (odd parity flag); 0 if even number of 1s.

### 4. 8051 I/O Ports
- **Port 0**: Open-drain bidirectional port. Requires external pull-up resistors for GPIO; acts as multiplexed address/data bus ($AD_0 - AD_7$) when accessing external memory.
- **Port 1**: True quasi-bidirectional port with internal pull-ups. Dedicated GPIO.
- **Port 2**: Quasi-bidirectional port; emits high address byte ($A_8 - A_{15}$) during external memory access.
- **Port 3**: Quasi-bidirectional with critical alternate functions:
  - $\text{P3.0} = \text{RXD}$, $\text{P3.1} = \text{TXD}$
  - $\text{P3.2} = \overline{\text{INT0}}$, $\text{P3.3} = \overline{\text{INT1}}$
  - $\text{P3.4} = \text{T0}$ (Timer 0 external input), $\text{P3.5} = \text{T1}$ (Timer 1 external input)
  - $\text{P3.6} = \overline{\text{WR}}$, $\text{P3.7} = \overline{\text{RD}}$

### 5. Interrupt Structure (5 Sources & Vector Addresses)
1. **$\overline{\text{INT0}}$ (External 0)**: `0003H` (Highest priority by default)
2. **Timer 0 Overflow ($\text{TF0}$)**: `000BH`
3. **$\overline{\text{INT1}}$ (External 1)**: `0013H`
4. **Timer 1 Overflow ($\text{TF1}$)**: `001BH`
5. **Serial Port ($\text{RI} / \text{TI}$)**: `0023H`

---

## 2. Frequently Asked Exam Questions & Diagram Pitfalls

1. **8051 Architecture Diagram**: Always draw the CPU core, ALU, Accumulator, B register, PSW, PC, DPTR, internal RAM/ROM, 4 I/O ports, Timers, and Serial port.
2. **RAM Map Diagram**: Clearly demarcate the three sections: Register Banks ($00\text{H}-1\text{F}\text{H}$), Bit-Addressable RAM ($20\text{H}-2\text{F}\text{H}$), and Scratchpad RAM ($30\text{H}-7\text{F}\text{H}$).
3. **External Memory Interfacing Diagram**: Show Port 0 connected to 74LS373 latch with `ALE` creating $A_0 - A_7$, Port 2 emitting $A_8 - A_{15}$, $\overline{\text{PSEN}}$ connected to ROM $\overline{\text{OE}}$, and $\overline{\text{RD}} / \overline{\text{WR}}$ connected to RAM $\overline{\text{OE}} / \overline{\text{WE}}$.

---

## 3. Comparison Cheat Sheets

### 8051 Memory Spaces

| Space | Size | Addressing Mode | Control Signal |
|---|---|---|---|
| **Internal RAM** | 128 Bytes | Direct & Indirect (`@R0, @R1`) | Internal bus |
| **SFR Area** | 128 Bytes ($80\text{H}-\text{FF}\text{H}$) | Direct addressing only | Internal bus |
| **Internal ROM** | 4 KB ($0000\text{H}-0\text{FFF}\text{H}$) | Indexed (`MOVC A, @A+PC / @A+DPTR`) | Internal |
| **External ROM** | Up to 64 KB | Indexed (`MOVC A, @A+DPTR`) | $\overline{\text{PSEN}} = 0$ |
| **External RAM** | Up to 64 KB | External (`MOVX A, @DPTR`) | $\overline{\text{RD}} = 0, \overline{\text{WR}} = 0$ |

---

## 4. 10-Minute Rapid Revision Checklist

- [ ] Can you list the 5 interrupt vector addresses of the 8051 from memory? (`03H, 0BH, 13H, 1BH, 23H`).
- [ ] What is the initial value of the Stack Pointer (SP) upon reset? (`07H`, pointing to $R_7$ of Bank 0).
- [ ] What is the function of the $\overline{\text{EA}}$ pin? ($\overline{\text{EA}}=1$ executes internal ROM; $\overline{\text{EA}}=0$ forces external ROM execution).
- [ ] How do you select Register Bank 2 in software? (`SETB RS1`, `CLR RS0` in PSW).
- [ ] Which I/O port of the 8051 requires external pull-up resistors to function as an output port? (Port 0).

