# 8051 Microcontroller Architecture

## 1. Explanation

### Microcontroller vs Microprocessor — The Core Distinction

A **microprocessor** (like the 8086) is a CPU chip that requires external chips for memory, I/O, timers, and serial ports. A **microcontroller** integrates ALL of these on a **single chip**:

```
Microprocessor System:         Microcontroller (8051):
┌─────┐ ┌─────┐ ┌─────┐      ┌──────────────────────────┐
│ CPU │ │ ROM │ │ RAM │      │          8051             │
└──┬──┘ └──┬──┘ └──┬──┘      │  ┌─────┐ ┌──────────┐   │
   │       │       │          │  │ CPU │ │  4KB ROM │   │
   └───────┴───────┘          │  └─────┘ └──────────┘   │
   External Bus               │  ┌────────┐ ┌────────┐  │
┌────────┐ ┌────────┐         │  │128B RAM│ │I/O Port│  │
│Timer IC│ │UART IC │         │  └────────┘ └────────┘  │
└────────┘ └────────┘         │  ┌────────┐ ┌────────┐  │
                              │  │Timers  │ │  UART  │  │
                              │  └────────┘ └────────┘  │
                              └──────────────────────────┘
```

**Key advantages of microcontrollers**:
- Single-chip solution → smaller PCB, lower cost, lower power
- Deterministic response time → critical for real-time embedded systems
- No external bus contention → simpler hardware design
- Self-contained → runs standalone without operating system

---

### 8051 Architecture — Complete Overview

The Intel 8051 (1980) is an 8-bit microcontroller that became the **universal embedded controller standard**. Billions of 8051-compatible devices (Atmel AT89, Silicon Labs C8051, Philips P89) are still manufactured annually.

```
┌──────────────────────────────────────────────────────────────────────┐
│                        8051 MICROCONTROLLER                          │
│                                                                      │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────────────────┐ │
│  │  PROGRAM     │   │   DATA RAM   │   │  SPECIAL FUNCTION        │ │
│  │  MEMORY      │   │  128 Bytes   │   │  REGISTERS (SFR)         │ │
│  │  (ROM 4KB)   │   │  00H–7FH     │   │  ACC, B, PSW, SP,        │ │
│  │  0000H-0FFFH │   │              │   │  DPTR, P0-P3,            │ │
│  └──────┬───────┘   └──────┬───────┘   │  TMOD, TCON,            │ │
│         │                  │            │  SCON, SBUF, IE, IP      │ │
│         │           ┌──────┴───────┐   └──────────────────────────┘ │
│         │           │  REGISTER    │                                  │
│         │           │  BANKS 0-3   │                                  │
│         │           │  R0–R7       │                                  │
│         │           │  (00H-1FH)   │                                  │
│         │           └──────────────┘                                  │
│  ┌──────┴──────────────────────────────────────────────────────────┐ │
│  │                     CPU CORE                                    │ │
│  │  ALU (8-bit) │ Accumulator A │ B Register │ PSW                │ │
│  │  Program Counter PC (16-bit) │ DPTR (DPH:DPL, 16-bit)         │ │
│  │  Stack Pointer SP (8-bit)    │ Instruction Decoder             │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌─────────┐ ┌─────────┐ ┌──────────────────┐ ┌──────────────────┐ │
│  │  PORT 0 │ │  PORT 1 │ │  TIMER/COUNTER   │ │  SERIAL PORT     │ │
│  │ (AD0-7) │ │ (I/O)   │ │  Timer 0 & 1     │ │  (TXD/RXD)       │ │
│  └─────────┘ └─────────┘ └──────────────────┘ └──────────────────┘ │
│  ┌─────────┐ ┌─────────┐ ┌──────────────────┐                       │
│  │  PORT 2 │ │  PORT 3 │ │  INTERRUPT       │                       │
│  │(A8-A15) │ │ Dual fn │ │  CONTROLLER      │                       │
│  └─────────┘ └─────────┘ └──────────────────┘                       │
└──────────────────────────────────────────────────────────────────────┘
```

---

### CPU Registers

#### Accumulator (A / ACC) — The Central Register
The 8-bit Accumulator is the **primary register** involved in virtually all arithmetic, logical, and data transfer operations. In the SFR space it is at address E0H and is **bit-addressable** (each bit can be set/cleared individually by name: ACC.0 through ACC.7).

#### B Register — The Multiply/Divide Partner
8-bit register used as the second operand in `MUL AB` and `DIV AB` instructions. After MUL AB: 16-bit product in B:A (B = high byte, A = low byte). After DIV AB: quotient in A, remainder in B.

#### Program Status Word (PSW) — Flags Register
8-bit SFR at address D0H (bit-addressable):

| Bit | Symbol | Name | Function |
|---|---|---|---|
| PSW.7 | CY | Carry Flag | Carry from ALU operation |
| PSW.6 | AC | Auxiliary Carry | Carry from bit 3 (BCD arithmetic) |
| PSW.5 | F0 | User Flag 0 | General-purpose flag for user code |
| PSW.4 | RS1 | Register Bank Select 1 | With RS0: selects active register bank |
| PSW.3 | RS0 | Register Bank Select 0 | RS1:RS0 = 00(B0), 01(B1), 10(B2), 11(B3) |
| PSW.2 | OV | Overflow Flag | Signed arithmetic overflow |
| PSW.1 | — | (User Flag 1) | Reserved/User |
| PSW.0 | P | Parity Flag | Even parity of Accumulator (1 if odd number of 1-bits) |

#### Stack Pointer (SP)
8-bit register initialized to 07H by RESET. Stack grows **upward** (toward higher addresses) in internal RAM. PUSH increments SP first, then stores; POP reads first, then decrements SP.
> **Critical**: Unlike 8086 (stack grows downward), the 8051 stack grows **upward**!

#### Data Pointer (DPTR = DPH:DPL)
16-bit register (made of two 8-bit SFRs: DPH at 83H and DPL at 82H). Used as a 16-bit pointer for:
- `MOVX @DPTR` — access external data memory (up to 64KB external RAM)
- `MOVC A, @A+DPTR` — look up table in program memory

#### Program Counter (PC)
16-bit counter automatically managed by the CPU. Points to the next instruction byte. After RESET: PC = 0000H → executes from the beginning of internal ROM.

---

### Internal RAM Organization (00H–7FH)

The 128-byte internal RAM is divided into three functional areas:

```
Memory Map:
7FH ┌──────────────────────────────────────────┐
    │                                          │
    │   GENERAL-PURPOSE RAM (scratch pad)      │
    │   30H–7FH (80 bytes)                     │
    │   Stack typically resides here            │
    │                                          │
30H ├──────────────────────────────────────────┤
    │                                          │
    │   BIT-ADDRESSABLE AREA                   │
    │   20H–2FH (16 bytes = 128 bits)          │
    │   Bit addresses: 00H–7FH                 │
    │   SETB 20H.3  → bit address 03H          │
    │   CLR 2FH.7   → bit address 7FH          │
    │                                          │
20H ├──────────────────────────────────────────┤
    │                                          │
    │   REGISTER BANKS (0 to 3)                │
    │   Bank 0: R0–R7 at 00H–07H (default)    │
    │   Bank 1: R0–R7 at 08H–0FH              │
    │   Bank 2: R0–R7 at 10H–17H              │
    │   Bank 3: R0–R7 at 18H–1FH              │
    │   Selected by PSW.4 (RS1) : PSW.3 (RS0) │
    │                                          │
00H └──────────────────────────────────────────┘
```

**Register Banks**: The 8051 has 4 banks of 8 general-purpose registers (R0–R7). Only one bank is active at a time, selected by RS1:RS0 in PSW:

| RS1 | RS0 | Active Bank | RAM Addresses |
|---|---|---|---|
| 0 | 0 | Bank 0 | 00H–07H (default after RESET) |
| 0 | 1 | Bank 1 | 08H–0FH |
| 1 | 0 | Bank 2 | 10H–17H |
| 1 | 1 | Bank 3 | 18H–1FH |

This multi-bank structure allows **fast context switching** in ISRs — the interrupt service routine switches to Bank 1, uses R0–R7 freely, then switches back without saving the main program's registers.

---

### I/O Ports — Detailed Description

#### Port 0 (P0, SFR 80H) — Bidirectional / Address-Data Bus
- Primary function: **Bidirectional I/O port** (8 pins, all bit-addressable).
- Alternate function: **Multiplexed address (A0–A7) and data (D0–D7) bus** when external memory is used (like 8086 ALE demultiplexing). No internal pull-ups → requires external pull-up resistors for I/O use.

#### Port 1 (P1, SFR 90H) — True Bidirectional I/O
- **True bidirectional I/O** with internal pull-up resistors.
- No alternate function in original 8051. (8052 uses P1.0=T2, P1.1=T2EX)
- Each bit independently read/write. Write 1 → pin released to pull-up (configure as input). Write 0 → pin driven LOW.

#### Port 2 (P2, SFR A0H) — High Byte Address
- Primary function: Bidirectional I/O with internal pull-ups.
- Alternate function: **High address byte (A8–A15)** for external memory addressing.

#### Port 3 (P3, SFR B0H) — Dual Function (Most Important!)

| Pin | Name | Alternate Function |
|---|---|---|
| P3.0 | RXD | Serial Port Receive Data |
| P3.1 | TXD | Serial Port Transmit Data |
| P3.2 | INT0# | External Interrupt 0 (edge/level triggered) |
| P3.3 | INT1# | External Interrupt 1 (edge/level triggered) |
| P3.4 | T0 | Timer 0 External Clock Input |
| P3.5 | T1 | Timer 1 External Clock Input |
| P3.6 | WR# | External Data Memory Write Strobe |
| P3.7 | RD# | External Data Memory Read Strobe |

> **Exam tip**: Memorize P3 alternate functions — they appear in almost every paper.

---

### Timer/Counter Architecture

The 8051 has **two independent 16-bit Timer/Counters** (Timer 0 and Timer 1). Each has:
- **TH** (High byte SFR) and **TL** (Low byte SFR)
- Configured by **TMOD** (Timer Mode) and **TCON** (Timer Control) registers

**TMOD Register (Timer Mode, 89H)**:
```
Bits 7-4: Timer 1 configuration  |  Bits 3-0: Timer 0 configuration
  GATE  C/T#  M1  M0            |    GATE  C/T#  M1  M0
```
- GATE: If 1, timer runs only while INT0#/INT1# is HIGH (hardware gating)
- C/T#: 0 = Timer (counts internal clock cycles), 1 = Counter (counts external T0/T1 pulses)
- M1:M0 → Mode selection:

| M1 | M0 | Mode | Description |
|---|---|---|---|
| 0 | 0 | Mode 0 | 13-bit timer (TH8:TL5 — legacy 8048 compatible) |
| 0 | 1 | Mode 1 | 16-bit timer (TH8:TL8) — maximum range |
| 1 | 0 | Mode 2 | 8-bit auto-reload (TL counts, TH holds reload value) |
| 1 | 1 | Mode 3 | Split 8-bit timers (Timer 0 only: TL0 and TH0 as two independent 8-bit timers) |

**Mode 2 (Auto-reload)** is most used for **baud rate generation**: set TH = reload_value; when TL overflows to FFH, it reloads from TH automatically — generating precise fixed-period pulses.

---

### Serial Port

Full-duplex UART built into the 8051:
- **SBUF** (Serial Buffer, SFR 99H): Writing to SBUF initiates transmission; reading SBUF returns received byte.
- **SCON** (Serial Control, SFR 98H): Contains TI (Transmit Interrupt flag), RI (Receive Interrupt flag), REN (Receive Enable), SM0:SM1 (Mode select), TB8/RB8 (9th bit in Mode 2/3).

**Serial modes**:

| Mode | Type | Baud Rate | Description |
|---|---|---|---|
| 0 | Shift Register | f_osc/12 | Fixed, synchronous serial I/O |
| 1 | 8-bit UART | Variable (Timer 1) | Standard async serial |
| 2 | 9-bit UART | f_osc/32 or /64 | Fixed baud, 9th bit for multiprocessor |
| 3 | 9-bit UART | Variable (Timer 1) | Variable baud, 9th bit for multiprocessor |

**Baud rate calculation** (Mode 1/3 using Timer 1 Mode 2):
$$\text{Baud} = \frac{f_{osc}}{32 \times 12 \times (256 - \text{TH1})}$$

Solve for TH1 to set desired baud rate.

**Example** (9600 baud, $f_{osc}$ = 11.0592 MHz):
$$\text{TH1} = 256 - \frac{11,059,200}{32 \times 12 \times 9600} = 256 - \frac{11,059,200}{3,686,400} = 256 - 3 = 253 = \text{FDH}$$

---

### Interrupt System

The 8051 supports **5 interrupt sources** (8052 adds a 6th: Timer 2):

| Interrupt | Source | Vector Address | Type |
|---|---|---|---|
| External 0 | INT0# pin (P3.2) | **0003H** | Edge (falling) or Level (LOW) |
| Timer 0 | TF0 overflow | **000BH** | Internal |
| External 1 | INT1# pin (P3.3) | **0013H** | Edge or Level |
| Timer 1 | TF1 overflow | **001BH** | Internal |
| Serial | RI or TI | **0023H** | Internal |

> **Memorize these 5 vector addresses — they appear in every paper.**

**IE (Interrupt Enable, SFR A8H)**:
```
EA  -  ET2  ES  ET1  EX1  ET0  EX0
7   6   5    4    3    2    1    0
```
- EA (bit 7): Global interrupt enable. Must be 1 for ANY interrupt to work.
- EX0, ET0, EX1, ET1, ES: Individual enables for each source.

**IP (Interrupt Priority, SFR B8H)**: 
- Each bit selects HIGH (1) or LOW (0) priority for the corresponding interrupt.
- Higher priority interrupt can interrupt a lower priority ISR (nested interrupts).
- If two same-priority interrupts occur simultaneously: priority order = INT0 > TF0 > INT1 > TF1 > Serial.

**Interrupt Response Sequence**:
1. Source flags (IE0, TF0, IE1, TF1, RI/TI) are set by hardware events.
2. If EA=1 and corresponding enable bit = 1 and no higher-priority ISR running:
3. CPU completes current instruction.
4. Pushes PC (2 bytes) onto stack. SP += 2.
5. Clears interrupt flag (auto-cleared for TF0, TF1; must be manually cleared for RI, TI).
6. PC ← interrupt vector address.
7. ISR executes. Must end with RETI.
8. RETI pops PC from stack. Main program resumes.

---

## 2. Example

### Internal RAM Mapping for a Practical Program

```
Memory at 00H–7FH during execution:

00H: R0 = 25H  ← Working register, Bank 0 active
01H: R1 = 00H
02H: R2 = 0AH  ← Loop counter
...
07H: R7 = ...

20H: 0xAB      ← Bit-addressable data (bit 20H.0=1, 20H.1=1, 20H.2=0...)
...
2FH: ...

30H: ...       ← Stack (SP starts at 07H; after several PUSH operations, stack grows up into 30H+)
...
7FH: (top of internal RAM)
```

---

## 3. Applications & Use Cases

### 1. Industrial Automation
8051-compatible microcontrollers (AT89C51) run PLC-like ladder logic programs for motor control, sensor reading (ADC via serial SPI), and relay switching. The deterministic interrupt response (Timer ISR guaranteed at fixed intervals) makes it ideal for time-critical control loops.

### 2. Consumer Electronics
8051 descendants run dishwashers, washing machines, microwave ovens, and digital thermostats — hundreds of millions of units worldwide. The 8051's low power, low cost, and ease of programming in C (Keil µVision IDE) make it the first choice for cost-sensitive consumer products.

### 3. Medical Devices
Pulse oximeters, digital thermometers, and infusion pump controllers use 8051-class microcontrollers for their real-time interrupt response and built-in UART (for RS-232 communication with display/logging hardware).

### 4. IoT Edge Nodes
Modern IoT devices often use ARM Cortex-M (the successor philosophy to 8051: single-chip integration) but the 8051's architectural concepts directly map to understanding Cortex-M peripherals — Timer Control registers, Interrupt Enable registers, UART FIFO operation.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Physical Address Computation — External Memory [KTU Part A — 3 marks]

**Problem**: The 8051 executes `MOVX A, @DPTR` with DPTR = 2050H. P2 and P0 provide the address. What is the external RAM address accessed?

**Solution**:
- DPTR = 2050H = DPH:DPL = 20H:50H
- During MOVX @DPTR:
  - P2 drives the high address byte: A8–A15 = DPH = 20H
  - P0 multiplexes address then data: A0–A7 = DPL = 50H (during ALE high)
  - External address = {P2, P0_addr} = {20H, 50H} = **2050H** in external RAM
- RD# (P3.7) goes LOW — external RAM places data at P0.
- Data latched into Accumulator A.

---

### Example 2: Timer 1 Baud Rate Calculation [KTU Part B — 9 marks]

**Problem**: An 8051 operates with 11.0592 MHz crystal. Configure Timer 1 in Mode 2 to generate 4800 baud for the serial port. Write the initialization code.

**Solution**:

Baud rate formula (Timer 1 Mode 2, SMOD=0 by default):
$$\text{Baud} = \frac{f_{osc}}{32 \times 12 \times (256 - \text{TH1})}$$

Solving for TH1 at 4800 baud:
$$4800 = \frac{11,059,200}{32 \times 12 \times (256 - \text{TH1})} = \frac{11,059,200}{384 \times (256 - \text{TH1})}$$
$$256 - \text{TH1} = \frac{11,059,200}{384 \times 4800} = \frac{11,059,200}{1,843,200} = 6$$
$$\text{TH1} = 256 - 6 = 250 = \textbf{FAH}$$

Assembly initialization code:
```asm
; 8051 Serial Port Initialization — 4800 baud, Mode 1 (8-bit UART)
; Crystal: 11.0592 MHz

MOV TMOD, #20H    ; Timer 1, Mode 2 (8-bit auto-reload)
                  ; TMOD = 0010 0000B: T1 in Mode 2, T0 unused
MOV TH1, #0FAH   ; Reload value for 4800 baud
MOV TL1, #0FAH   ; Initial count same as reload (optional for clean startup)
SETB TR1          ; Start Timer 1 (TCON bit TR1 = 1)

MOV SCON, #50H   ; Serial Mode 1 (8-bit UART), REN=1 (receive enable)
                  ; SCON = 0101 0000B: SM0=0, SM1=1 (Mode 1), REN=1
SETB EA           ; Enable global interrupts
SETB ES           ; Enable Serial interrupt (optional — for interrupt-driven serial)
```

---

### Example 3: Interrupt Priority and ISR Design [KTU Part B — 9 marks]

**Problem**: Design an 8051 interrupt system where:
- External Interrupt 0 (INT0#) triggers on falling edge and has HIGH priority.
- Timer 0 overflow triggers and has LOW priority.
- In the INT0 ISR, read Port 1 data into A.
- In the Timer 0 ISR, increment a counter at address 50H.

Write the complete initialization and ISR code.

**Solution**:

```asm
ORG 0000H           ; RESET vector
    LJMP MAIN       ; Jump to main program

ORG 0003H           ; INT0 vector address (External Interrupt 0)
    LJMP INT0_ISR   ; Jump to INT0 service routine

ORG 000BH           ; TF0 vector address (Timer 0 overflow)
    LJMP T0_ISR     ; Jump to Timer 0 service routine

ORG 0100H           ; Main program starts here

MAIN:
    ; Configure External Interrupt 0:
    SETB IT0        ; IT0 = TCON.0 = 1 → Edge-triggered (falling edge)
    
    ; Configure Timer 0 for overflow interrupt (Mode 1, 16-bit):
    MOV TMOD, #01H  ; Timer 0 in Mode 1 (16-bit)
    MOV TH0, #3CH   ; Load TH0 (for ~50ms delay at 12 MHz)
    MOV TL0, #0B0H  ; Load TL0
    SETB TR0        ; Start Timer 0
    
    ; Set Interrupt Priorities:
    SETB PX0        ; IP.0 = PX0 = 1 → INT0 HIGH priority
    CLR PT0         ; IP.1 = PT0 = 0 → Timer 0 LOW priority
    
    ; Enable Interrupts:
    SETB EX0        ; Enable External Interrupt 0
    SETB ET0        ; Enable Timer 0 interrupt
    SETB EA         ; Global enable
    
    MOV 50H, #00H   ; Initialize counter at address 50H
    
HERE: SJMP HERE     ; Main program loops (waits for interrupts)

INT0_ISR:           ; INT0 ISR at vector 0003H
    PUSH ACC        ; Save Accumulator
    PUSH PSW        ; Save PSW (flags)
    MOV A, P1       ; Read Port 1 data into Accumulator
    ; Process data in A here (e.g., output to LCD, store in buffer)
    POP PSW
    POP ACC
    RETI            ; Return from interrupt (restores PC from stack)

T0_ISR:             ; Timer 0 ISR at vector 000BH
    PUSH ACC
    PUSH PSW
    MOV TH0, #3CH  ; Reload Timer 0 (Mode 1 doesn't auto-reload!)
    MOV TL0, #0B0H
    INC 50H         ; Increment counter at RAM address 50H
    POP PSW
    POP ACC
    RETI
```

---

## 5. Previous Year Questions & Solutions

---

### Q1 [KTU All papers — Part E, 10 marks]
**Question**: Draw and explain the internal architecture of the 8051 microcontroller. Explain its memory organization.

**Solution**:

**Internal Architecture** (refer to block diagram in Section 1):

The 8051 is an 8-bit microcontroller with the following on-chip resources:

**CPU Core**:
- 8-bit ALU supporting arithmetic (ADD, SUBB, MUL, DIV), logical (ANL, ORL, XRL), and bit operations.
- **Accumulator (A)**: Primary working register in SFR space at E0H.
- **B Register** (F0H): Used in MUL AB and DIV AB.
- **PSW** (D0H): 8-bit flags register with CY, AC, F0, RS1, RS0, OV, P.
- **PC**: 16-bit program counter; starts at 0000H after reset.
- **DPTR** (DPH:DPL, 83H:82H): 16-bit data pointer for external memory.
- **SP** (81H): Stack pointer, initializes to 07H.

**Memory Architecture**:

The 8051 uses a **Harvard architecture** — separate address spaces for program and data memory:

*Program Memory (ROM)*:
- 4KB internal ROM (0000H–0FFFH) for user program.
- When EA# = 1 (tied to VCC): Internal ROM used first; external extends from 1000H–FFFFH.
- When EA# = 0 (tied to GND): All fetches from external ROM (up to 64KB).
- Accessed via MOVC instruction and during instruction fetch (PSEN# strobe).

*Data Memory (RAM)*:
- 128 bytes internal RAM (00H–7FH): Register banks (00H-1FH), Bit-addressable area (20H-2FH), GP RAM (30H-7FH).
- SFR space (80H–FFH): Only specific addresses are valid SFRs.
- External RAM: Up to 64KB via MOVX instruction (P0 as AD0-7, P2 as A8-15, RD#/WR# on P3.7/P3.6).

**I/O Ports**: P0 (bidirectional/address-data), P1 (pure I/O with pull-ups), P2 (high address), P3 (dual function: TXD, RXD, INT0#, INT1#, T0, T1, WR#, RD#).

**Timers**: Two 16-bit Timer/Counters (T0, T1) with 4 modes each. Timer 2 in 8052.

**Serial Port**: Full-duplex UART with 4 modes (Modes 0–3). Baud rate controlled by Timer 1.

**Interrupt System**: 5 sources (INT0, TF0, INT1, TF1, Serial) with 2-level priority (IP register) and vector addresses at 0003H, 000BH, 0013H, 001BH, 0023H.

---

### Q2 [KTU June 2022 / Dec 2021 / May 2019 — Part E, 10 marks]
**Question**: Explain the register organization and memory map of the 8051. How are register banks selected?

**Solution**:

**Register Banks (00H–1FH)**:
The 8051 has 4 register banks, each containing 8 general-purpose registers R0–R7:
- Bank 0: 00H–07H (active after RESET)
- Bank 1: 08H–0FH
- Bank 2: 10H–17H
- Bank 3: 18H–1FH

Selection is via **RS1:RS0 bits in PSW** (bits 4 and 3):
```asm
; Select Bank 1:
SETB PSW.4   ; RS1 = 1
CLR  PSW.3   ; RS0 = 0
; Now R0 refers to RAM address 08H, R7 to 0FH
```
Alternatively: `MOV PSW, #08H` (RS0=1 → Bank 1).

**Use in ISRs**: Interrupt Service Routines can switch to a different bank instead of pushing registers:
```asm
INT0_ISR:
    PUSH PSW          ; Save current PSW (bank selection)
    MOV PSW, #08H     ; Switch to Bank 1 (ISR uses its own R0-R7)
    ; Use R0-R7 freely here (Bank 1 — different from main program's Bank 0)
    POP PSW           ; Restore original bank
    RETI
```

**Bit-Addressable Area (20H–2FH)**:
- 16 bytes, 128 individual addressable bits.
- Bit addresses 00H–7FH map to: Byte 20H.bit0=00H, 20H.bit1=01H, ... 20H.bit7=07H, Byte 21H.bit0=08H, ...
- Instructions: SETB 25H (set bit at address 25H), CLR 32H, MOV C, 44H.

**Complete RAM map summary**:
```
7FH ─── GP RAM (30H–7FH): Stack, local variables ─── 30H
2FH ─── Bit-addressable (20H–2FH: 128 bit flags) ─── 20H
1FH ─── Bank 3 (R0–R7 at 18H–1FH) ─── 18H
17H ─── Bank 2 (R0–R7 at 10H–17H) ─── 10H
0FH ─── Bank 1 (R0–R7 at 08H–0FH) ─── 08H
07H ─── Bank 0 (R0–R7 at 00H–07H) ─── 00H  ← active after RESET
```

---

### Q3 [KTU Dec 2021 / May 2019 / All papers — Part E, 10 marks]
**Question**: Explain the interrupt structure of the 8051. What are the interrupt vector addresses? How are interrupt priorities handled?

**Solution**:

**Interrupt Sources and Vectors**:

| Source | Trigger | Flag | Vector | IE Bit |
|---|---|---|---|---|
| External INT0# | Falling edge or LOW level (IT0=0: level, IT0=1: edge) | IE0 | **0003H** | EX0 |
| Timer 0 Overflow | TH0:TL0 rolls over from FFFFH to 0000H | TF0 | **000BH** | ET0 |
| External INT1# | Falling edge or LOW level (IT1=0: level, IT1=1: edge) | IE1 | **0013H** | EX1 |
| Timer 1 Overflow | TH1:TL1 rolls over from FFFFH to 0000H | TF1 | **001BH** | ET1 |
| Serial Port | RI (receive complete) OR TI (transmit complete) | RI/TI | **0023H** | ES |

**Interrupt Enable Register (IE at A8H)**:
```
EA  —  —  ES  ET1  EX1  ET0  EX0
7   6  5   4    3    2    1    0
```
- EA must be 1 to enable any interrupt.
- Example: Enable all interrupts: `MOV IE, #8FH` (EA=1, ES=1, ET1=0, EX1=0, ET0=1, EX0=1) = 10001111B = 8FH.

**Interrupt Priority Register (IP at B8H)**:
- 0 = LOW priority, 1 = HIGH priority for each source.
- Two priority levels: HIGH priority ISR can interrupt a LOW priority ISR (nested interrupts).
- If two equal-priority interrupts occur simultaneously, polling order determines winner: INT0 → TF0 → INT1 → TF1 → Serial.

**Example priority setup**:
```asm
MOV IP, #05H   ; IP = 00000101B: EX0=1 (HIGH), ET0=1 (HIGH), rest LOW
               ; INT0 and Timer 0 get HIGH priority
```

**Interrupt Response Sequence** (step by step):
1. Hardware sets interrupt flag (IE0, TF0, etc.).
2. CPU checks: EA=1? AND individual enable bit=1? AND no same/higher priority ISR running?
3. If YES: CPU completes the current instruction.
4. CPU automatically pushes the **return address** (PC) onto stack: SPH first, then SPL. SP incremented twice.
5. PC is loaded with the vector address (e.g., 0003H for INT0).
6. ISR executes.
7. ISR ends with RETI: Pops PC from stack. SP decremented twice. Resumes main program.

> **Important**: RETI is different from RET — RETI also **re-enables the interrupt priority level** (clears the internal priority flag), allowing the same-priority interrupt to occur again after return.

---

### Q4 [KTU All papers — Part A, 3 marks]
**Question**: What are the differences between microprocessors and microcontrollers? Give examples.

**Solution**:

| Feature | Microprocessor (8086) | Microcontroller (8051) |
|---|---|---|
| **Integration** | CPU only on chip | CPU + RAM + ROM + I/O + Timer + UART on single chip |
| **External Memory** | Always required | Optional (can run from internal ROM) |
| **I/O** | Via external chips (8255) | Built-in I/O ports (P0–P3) |
| **Timers** | External 8253/8254 needed | Internal timers (T0, T1) |
| **Serial Port** | External 8250/8251 needed | Built-in UART |
| **Cost** | High system cost (many chips) | Low system cost (single chip) |
| **Power** | Higher (more chips) | Lower (single chip) |
| **Applications** | PCs, workstations, servers | Washing machines, toys, industrial control |
| **Data Bus** | 16-bit (8086) | 8-bit |
| **Addressable Memory** | 1 MB external | 4KB internal ROM, 64KB external |

**Examples**:
- Microprocessors: Intel 8086, 80286, 80386, Pentium, Core i9; AMD Ryzen.
- Microcontrollers: Intel 8051, Atmel AT89C51, PIC16F877, Arduino ATmega328P, STM32 (ARM Cortex-M).

