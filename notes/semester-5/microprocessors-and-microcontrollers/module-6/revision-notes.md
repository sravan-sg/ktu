# Module VI: 8051 Instruction Set, Programming & 8254 — Revision Notes

> **Quick Revision Guide for Internal & University Exams** | CS305 Semester 5

---

## 1. High-Yield Core Concepts & Formulae

### 1. 8051 Addressing Modes
- **Immediate**: `MOV A, #55H` (data preceded by `#`).
- **Register**: `MOV A, R0` (data in register $R_0 - R_7$).
- **Direct**: `MOV A, 30H` (data from RAM address `30H` or SFR).
- **Register Indirect**: `MOV A, @R0` ($R_0$ or $R_1$ holds 8-bit RAM pointer).
- **Indexed**: `MOVC A, @A+DPTR` or `MOVC A, @A+PC` (fetches constant from ROM).
- **External Data**: `MOVX A, @DPTR` (16-bit address) or `MOVX A, @R0` (8-bit address).
- **Bit Addressing**: `SETB 07H`, `CLR P1.0`, `MOV C, 25H.2`.

### 2. Crucial 8051 Instructions
- `MUL AB`: Multiplies $A \times B$. Low byte in $A$, high byte in $B$. If result $> 255$, $\text{OV}=1$, else $\text{OV}=0$. Always clears Carry ($\text{CY}=0$).
- `DIV AB`: Divides $A / B$. Integer quotient in $A$, remainder in $B$. If $B=0$, $\text{OV}=1$ (division by zero error).
- `DA A`: Decimal Adjust Accumulator. Converts binary addition result into packed BCD. If lower nibble $> 9$ or $\text{AC}=1$, adds `06H`. If upper nibble $> 9$ or $\text{CY}=1$, adds `60H`.
- `CJNE A, #data, rel`: Compare and Jump if Not Equal. If $A < \text{data}$, sets $\text{CY}=1$; if $A \ge \text{data}$, clears $\text{CY}=0$.
- `DJNZ Rn, rel`: Decrement register and Jump if Not Zero. Standard loop construct!

### 3. 8254 PIT Operating Modes Summary
- **Mode 0 (Interrupt on Terminal Count)**: `OUT` initially LOW; transitions HIGH when count reaches 0. GATE=1 enables count.
- **Mode 1 (Hardware Retriggerable One-Shot)**: Rising edge on GATE pulls `OUT` LOW for $N$ clocks.
- **Mode 2 (Rate Generator)**: Divide-by-$N$. `OUT` HIGH for $N-1$ clocks, LOW for 1 clock. Automatically reloads.
- **Mode 3 (Square Wave Generator)**: Symmetrical square wave ($N/2$ high, $N/2$ low).
- **Mode 4 (Software Triggered Strobe)**: `OUT` HIGH; emits 1-clock negative strobe when count expires.
- **Mode 5 (Hardware Triggered Strobe)**: Rising edge on GATE starts countdown; emits 1-clock negative strobe at terminal count.

### 4. 8254 Control Word Quick Formula
- Format: `[SC1 SC0] [RW1 RW0] [M2 M1 M0] [BCD]`
- Counter 0: `00`, Counter 1: `01`, Counter 2: `10`.
- Read/Write: LSB only = `01`, MSB only = `10`, LSB then MSB = `11`, Counter Latch = `00`.
- Modes: Mode 0 = `000`, Mode 1 = `001`, Mode 2 = `010`, Mode 3 = `011`, Mode 4 = `100`, Mode 5 = `101`.
- Binary count = `0`, BCD count = `1`.

---

## 2. Frequently Asked Exam Questions & Diagram Pitfalls

1. **8254 Modes and Waveforms**: In Part E, questions frequently ask for the 6 operating modes of the 8254 with waveforms. Always draw the relationship between `CLK`, `GATE`, and `OUT` for each mode.
2. **8051 Assembly Programs**: The exam almost always asks for one program from: (a) Finding largest/smallest in an array, (b) Sum of $N$ numbers with carry, or (c) BCD to ASCII conversion. Always initialize pointers (`MOV R0, #30H` or `MOV DPTR, #2000H`) and loop counter (`MOV R2, #count`).
3. **8254 Count Calculation**: Count $N = \frac{f_{\text{CLK}}}{f_{\text{out}}}$. Remember to convert decimal to hex and load LSB first, then MSB.

---

## 3. Comparison Cheat Sheets

### 8051 Jump Instructions

| Instruction | Encoding Size | Range | Target Calculation |
|---|---|---|---|
| **SJMP** (Short Jump) | 2 Bytes | $-128 \text{ to } +127$ bytes | Relative to next PC ($PC + \text{offset}$) |
| **AJMP** (Absolute Jump) | 2 Bytes | Within same 2 KB page | $PC_{15-11} : \text{addr}_{10-0}$ |
| **LJMP** (Long Jump) | 3 Bytes | Full 64 KB space ($0000\text{H}-\text{FFFF}\text{H}$) | 16-bit direct address |

---

## 4. 10-Minute Rapid Revision Checklist

- [ ] What does `SWAP A` do? (Exchanges lower 4 bits with upper 4 bits of Accumulator).
- [ ] How does `DA A` work after `ADD A, R1`? (Adds 6 to nibbles greater than 9 or if half/full carry occurred).
- [ ] What is the control word to configure 8254 Counter 0 in Mode 3 (Square Wave) with 16-bit binary count? (`36H`).
- [ ] What is the function of the Counter Latch Command in 8254? (Latches count into output latch without halting the countdown).
- [ ] What flag does `CJNE` alter if the first operand is strictly less than the second? (Sets the Carry flag $\text{CY}=1$).

