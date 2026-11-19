# CS305 — Microprocessors and Microcontrollers

> 3 Credits | L-T-P: 2-1-0 | Semester 5 | Prerequisite: CS202 Computer Organisation and Architecture

---

## Grading Criteria

| Component | Coverage | Marks |
|---|---|---|
| **Part A** | Modules I & II (all 4 compulsory × 3 marks) | 12 |
| **Part B** | Modules I & II (2 of 3 questions × 9 marks) | 18 |
| **Part C** | Modules III & IV (all 4 compulsory × 3 marks) | 12 |
| **Part D** | Modules III & IV (2 of 3 questions × 9 marks) | 18 |
| **Part E** | Modules V & VI (4 of 6 questions × 10 marks) | 40 |
| **Total End-Sem** | | 100 |

- **Part A + C**: Short answer questions (3 marks each) — all compulsory. Test definitions, working, diagrams.
- **Part B + D**: 9-mark questions with up to 3 sub-parts — choose 2 of 3. Test detailed understanding and analytical problems.
- **Part E**: 10-mark questions (up to 3 sub-parts) — choose 4 of 6. This is the **heaviest section (40 marks)** covering 8051 architecture and instruction set.
- **At least 60% analytical/numerical questions** in the paper — expect timing diagrams, assembly programs, addressing mode problems, interface calculations.
- **First Internal Exam**: After Modules I & II
- **Second Internal Exam**: After Modules III & IV
- **End Semester Exam**: All 6 modules

**Per-Module End-Sem Weightage:**
- Module I: 15% | Module II: 15% | Module III: 15% | Module IV: 15%
- Module V: 20% | Module VI: 20%

---

## Textbooks

1. **Bhurchandi and Ray** — *Advanced Microprocessors and Peripherals*, 3rd Edition, McGraw Hill, 2012.
   - Primary reference for 8086 architecture, instruction set, timing diagrams, and peripheral interfaces (8255, 8259, 8257, 8279).
2. **Raj Kamal** — *Microcontrollers: Architecture, Programming, Interfacing and System Design*, Pearson Education, 2011.
   - Primary reference for Modules V & VI: 8051 microcontroller architecture, instruction set, and programming.
3. **Douglas V. Hall, SSSP Rao** — *Microprocessors and Interfacing*, 3rd Edition, McGraw Hill Education, 2012.
   - Supplementary reference for 8086 assembly programming and I/O interfacing.

**References:**
- Barry B. Brey — *The Intel Microprocessors*, 8th Edition, Pearson Education, 2015.
- A. NagoorKani — *Microprocessors and Microcontrollers*, 2nd Edition, Tata McGraw Hill, 2012.

---

## Modules

### Module I — 8086 Microprocessor Architecture (7 Hours | 15%)
- Evolution of microprocessors (4-bit → 8-bit → 16-bit → 32-bit → 64-bit history)
- **8086 Internal Architecture**:
  - Bus Interface Unit (BIU): Segment registers (CS, DS, SS, ES), Instruction Pointer (IP), 6-byte instruction queue (pre-fetch pipeline)
  - Execution Unit (EU): ALU, general-purpose registers (AX, BX, CX, DX), index registers (SI, DI), pointer registers (SP, BP), Flag register
  - 20-bit physical address formation: `Physical Address = Segment × 16 + Offset`
- **8086 Signals**: Address/Data multiplexed bus (AD0–AD15, A16–A19), ALE, BHE#, RD#, WR#, M/IO#, DT/R#, DEN#, HOLD/HLDA, INTR, NMI, RESET, CLK
- **Memory Organisation**: Even banks and odd banks (BHE# and A0 select byte/word), segmented memory model, segment:offset notation
- **Minimum Mode vs Maximum Mode**:
  - Minimum Mode: MN/MX# = VCC; 8086 generates its own bus control signals. Single processor configuration.
  - Maximum Mode: MN/MX# = GND; 8288 Bus Controller generates bus control signals. Multi-processor configuration. Additional signals: S0#, S1#, S2# (status), QS0, QS1 (queue status), RQ/GT0#, RQ/GT1#
- **Minimum Mode Timing Diagram**: Read cycle (4 T-states), Write cycle (4 T-states), Wait states (Tw), ALE pulse timing, data valid window
- **Comparison of 8086 and 8088**:
  - 8086: 16-bit external data bus, 20-bit address bus
  - 8088: 8-bit external data bus, 20-bit address bus (used in IBM PC XT)

### Module II — 8086 Instruction Set & Assembly Programming (8 Hours | 15%)
- **8086 Addressing Modes**:
  - Immediate: MOV AX, 1234H
  - Register: MOV AX, BX
  - Direct: MOV AX, [2000H]
  - Register Indirect: MOV AX, [BX]
  - Based/Indexed: MOV AX, [BX+SI], MOV AX, [BP+DI]
  - Based Indexed with Displacement: MOV AX, [BX+SI+10H]
  - String/Auto-increment modes (REP MOVS, REP CMPS)
- **8086 Instruction Set**:
  - Data Transfer: MOV, PUSH, POP, XCHG, XLAT, IN, OUT, LEA, LDS, LES
  - Arithmetic: ADD, ADC, SUB, SBB, MUL, IMUL, DIV, IDIV, INC, DEC, NEG, CBW, CWD, DAA, DAS, AAA, AAS, AAM, AAD
  - Logical: AND, OR, XOR, NOT, TEST
  - Shift/Rotate: SHL, SHR, SAL, SAR, ROL, ROR, RCL, RCR
  - String: MOVS, CMPS, SCAS, LODS, STOS with REP/REPE/REPNE prefixes
  - Control Transfer: JMP, Jxx (conditional jumps), CALL, RET, LOOP, LOOPZ, LOOPNZ, INT, IRET
  - Processor Control: NOP, HLT, WAIT, ESC, LOCK, segment overrides
- **Assembler Directives**: DB, DW, DD, DQ, DT; SEGMENT, ENDS; ASSUME; EQU; LABEL; PROC, ENDP; END; OFFSET, SEG; ORG; PUBLIC, EXTRN
- **Assembly Language Programming**:
  - Program structure: Code segment, Data segment, Stack segment; full program skeleton
  - Subroutines: NEAR vs FAR procedures, CALL/RET mechanics, stack frame setup
  - Macros: MACRO/ENDM directives, macro expansion, parameters
  - Passing Parameters: via registers, via stack, via memory
  - Use of Stack: PUSH/POP for register saving/restoring, stack-based parameter passing

### Module III — Interrupts & 8259 PIC (7 Hours | 15%)
- **Types of Interrupts**:
  - Hardware interrupts: Maskable (INTR pin, via 8259) and Non-maskable (NMI pin, e.g. memory parity error)
  - Software interrupts: INT n (n = 0 to 255) — INT 21H (DOS services), INT 10H (BIOS video), INT 16H (BIOS keyboard)
  - Internal interrupts: Divide by zero (Type 0), Single-step (Type 1), Breakpoint (Type 3), Overflow (Type 4)
- **Interrupt Service Routine (ISR)**: Vector table (1KB at 0000:0000 — 256 × 4 bytes each = IP + CS), saving registers, IRET instruction
- **Handling Interrupts in 8086**: INTR signal asserted → 8086 completes current instruction → sends INTA pulses → reads interrupt type number from data bus → pushes FLAGS, CS, IP → jumps to ISR
- **Interrupt Programming**: Writing ISRs in assembly, setting interrupt vector table entries, enabling/disabling interrupts (STI/CLI, IF flag)
- **8259 Programmable Interrupt Controller (PIC)**:
  - Architecture: IRQ0–IRQ7 input lines, Priority Resolver, Interrupt Request Register (IRR), In-Service Register (ISR), Interrupt Mask Register (IMR)
  - Initialization Command Words (ICW1–ICW4) and Operational Command Words (OCW1–OCW3)
  - Priority modes: Fixed priority, Rotating priority, Special fully nested mode
  - Cascading: Master 8259 + up to 8 Slave 8259s = 64 interrupt inputs

### Module IV — Memory/IO Interfacing, 8255, 8279, 8257 (7 Hours | 15%)
- **Memory Interfacing with 8086**:
  - Address decoding: full decoding vs partial decoding
  - Bank structure: even bank (A0=0, BHE#=1) for even bytes, odd bank (A0=1, BHE#=0) for odd bytes
  - Interface design: selecting SRAM/EPROM chips using address decoder (74138/74139)
- **I/O Interfacing with 8086**:
  - I/O-mapped I/O vs memory-mapped I/O
  - IN/OUT instructions, 8-bit and 16-bit I/O ports, isolated I/O
- **8255 Programmable Peripheral Interface (PPI)**:
  - Architecture: Port A (8-bit), Port B (8-bit), Port C (8-bit, split into upper/lower), Control Register
  - **Mode 0 (Basic I/O)**: Simple input/output for all ports. Each port independently configurable as input or output.
  - **Mode 1 (Strobed I/O)**: Handshake-based I/O. Port C bits serve as handshake signals (IBF, OBF, STB, ACK, INTR).
  - **Mode 2 (Bidirectional Bus)**: Port A only. Full bidirectional 8-bit bus with handshake (OBF, ACK, STB, IBF, INTR).
  - **Control Word Format** (Mode Set): D7=1 (mode set); D6-D5 (Mode for Port A: 00=Mode0, 01=Mode1, 1x=Mode2); D4 (Port A direction); D3 (Port C upper); D2-D1 (Mode for Port B: 0=Mode0, 1=Mode1); D1 (Port B direction); D0 (Port C lower)
  - Bit Set/Reset: D7=0, D3-D1 (bit number), D0 (1=set, 0=reset)
- **8279 Programmable Keyboard/Display Interface**:
  - Architecture: Keyboard section (scanned matrix up to 8×8 = 64 keys), Display section (up to 16 7-segment or 16×8 dot-matrix characters), FIFO/sensor RAM (8 entries × 8-bit)
  - Keyboard scan: Scan counter drives SL0-SL3 output lines; return lines RL0-RL7 detect key closures; debounce logic
  - Display: Characters written to display RAM; internal counter scans anodes; cathode data from RAM
  - Control word modes: Keyboard: Encoded/Decoded/Sensor matrix; Display: Left/Right entry modes; Clock programming
  - *(Note: No need to memorize exact control word format per syllabus note)*
- **8257 Programmable DMA Controller**:
  - Architecture: 4 DMA channels, each with: DMA Address Register (16-bit), Terminal Count Register (14-bit), Mode Set Register
  - DMA operation: CPU→8257 initiates DMA, 8257 asserts HOLD, CPU asserts HLDA, 8257 controls bus, transfers data directly Memory↔I/O without CPU
  - Modes: Verify transfer, Write transfer, Read transfer; Auto-load mode; Rotating priority
  - *(Note: No need to memorize exact control word format per syllabus note)*

### Module V — 8051 Microcontroller Architecture (8 Hours | 20%)
- **Types of Microcontrollers**: 4-bit (old toys/appliances), 8-bit (8051, PIC16, AVR ATmega), 16-bit (MSP430, 8096), 32-bit (ARM Cortex-M, STM32)
- **Criteria for Selecting a Microcontroller**: Word length, on-chip memory (ROM/RAM), I/O pins, timers, serial ports, interrupt structure, power consumption, development tools, cost, supply voltage
- **Example Applications**: Washing machines, digital thermometers, industrial controllers, automotive ECUs, medical devices, consumer electronics
- **Characteristics & Resources of a Typical Microcontroller**: CPU core, on-chip ROM (program memory), on-chip RAM (data memory), I/O ports, timers/counters, serial communication (UART), interrupt controller — all on a single chip
- **8051 Architecture**:
  - **CPU**: 8-bit ALU, 8-bit Accumulator (A), 8-bit B register (for multiply/divide), 8-bit PSW (flags: CY, AC, F0, RS1, RS0, OV, P), 8-bit Stack Pointer (SP, initially 07H)
  - **Program Counter (PC)**: 16-bit (addresses 64KB program memory space)
  - **Data Pointer (DPTR)**: 16-bit (DPH:DPL) for external data memory access
  - **On-Chip Memory**:
    - **Internal ROM**: 4KB (0000H–0FFFH) program memory
    - **Internal RAM**: 128 bytes (00H–7FH): Register banks (00H–1FH, 4 banks × 8 regs), Bit-addressable area (20H–2FH, 128 bits), General-purpose RAM (30H–7FH)
    - **SFR (Special Function Register) area**: 80H–FFH (only specific addresses valid)
  - **Register Organisation**: Bank 0 (R0–R7 at 00H–07H), Bank 1 (08H–0FH), Bank 2 (10H–17H), Bank 3 (18H–1FH); selected by RS1:RS0 in PSW
  - **I/O Ports**: P0 (bidirectional, also AD0–AD7 in external bus mode), P1 (true bidirectional I/O), P2 (also A8–A15 in external bus mode), P3 (dual function: TXD, RXD, INT0#, INT1#, T0, T1, WR#, RD#)
  - **External Memory Addressing**: EA# pin = 0 → all program fetches from external memory; = 1 → internal ROM first (up to 4KB), then external. External address: MOVX @DPTR for 16-bit external data memory; ALE/PSEN# for program memory fetch
  - **Timers/Counters**: Timer 0 and Timer 1 — each 16-bit (TH, TL). Modes: Mode 0 (13-bit), Mode 1 (16-bit auto-reload), Mode 2 (8-bit auto-reload), Mode 3 (split timer). TMOD and TCON registers.
  - **Serial Port**: Full-duplex UART. SBUF (transmit + receive buffer). Modes: Mode 0 (shift register), Mode 1 (8-bit UART), Mode 2 (9-bit UART fixed baud), Mode 3 (9-bit UART variable baud). SCON register.
  - **Interrupts**:
    - 5 interrupt sources: External INT0# (IE0), External INT1# (IE1), Timer 0 overflow (TF0), Timer 1 overflow (TF1), Serial (RI/TI)
    - IE (Interrupt Enable) register: EA, -, ET2, ES, ET1, EX1, ET0, EX0
    - IP (Interrupt Priority) register: selects high/low priority for each source
    - Interrupt vector addresses: INT0=0003H, TF0=000BH, INT1=0013H, TF1=001BH, Serial=0023H
  - **Stack**: Stack Pointer (SP) starts at 07H; stack grows upward in internal RAM. PUSH/POP instructions.

### Module VI — 8051 Instruction Set, Programming & 8254 (8 Hours | 20%)
- **8051 Addressing Modes**:
  - Immediate: MOV A, #55H
  - Register: MOV A, R0
  - Direct: MOV A, 30H (address in internal RAM or SFR)
  - Register Indirect: MOV A, @R0 (R0/R1 as pointer to internal RAM or external RAM)
  - Indexed: MOVC A, @A+DPTR; MOVC A, @A+PC (read from program memory — look-up tables)
  - External: MOVX A, @DPTR; MOVX A, @R0 (external data memory)
  - Bit: SETB CY; CLR P1.0; MOV C, bit_address
- **8051 Instruction Set** (by function):
  - *Data Transfer*: MOV, MOVX, MOVC, PUSH, POP, XCH, XCHD
  - *Arithmetic*: ADD, ADDC, SUBB, MUL AB, DIV AB, INC, DEC, DA A
  - *Logical*: ANL, ORL, XRL, CLR, CPL, RL, RR, RLC, RRC, SWAP
  - *Boolean/Bit*: MOV C,bit; SETB; CLR; CPL; ANL C,bit; ORL C,bit; JC; JNC; JB; JNB; JBC
  - *Control Transfer*: LJMP (3-byte), AJMP (2-byte), SJMP (2-byte short), LCALL, ACALL, RET, RETI, JZ, JNZ, CJNE, DJNZ, NOP
- **Simple 8051 Programs**:
  - Arithmetic: add/subtract/multiply two 8-bit numbers
  - Array operations: sum of an array, largest/smallest in array
  - BCD to ASCII conversion, ASCII to BCD
  - Delay subroutines using DJNZ
  - Bit manipulation: LED control on P1
  - Serial communication setup (computing baud rate using Timer 1 Mode 2)
- **8254/8253 Programmable Interval Timer (PIT)**:
  - Architecture: 3 independent 16-bit down-counters (Counter 0, Counter 1, Counter 2). Each has CLK, GATE, OUT pins.
  - **6 Operating Modes**:
    - Mode 0: Interrupt on Terminal Count
    - Mode 1: Programmable One-Shot
    - Mode 2: Rate Generator (divide-by-N frequency divider)
    - Mode 3: Square Wave Generator (symmetric divide-by-N)
    - Mode 4: Software Triggered Strobe
    - Mode 5: Hardware Triggered Strobe
  - Control Word Format: SC1-SC0 (counter select), RW1-RW0 (read/write mode: LSB only/MSB only/LSB then MSB), M2-M1-M0 (mode), BCD (binary or BCD count)
  - Application: PC timer interrupt (18.2 Hz system clock), UART baud rate generation, event counting

---

## Exam Focus — What to Prioritize

> **Professor's High-Yield Synthesis (based on mark distribution)**

1. **8086 Architecture Drawing** (Module I, repeated every year in Part B): The BIU/EU block diagram with all registers, 20-bit address generation formula ($PA = Segment \times 16 + Offset$), and minimum-mode timing diagram (4 T-states, ALE pulse, data valid window) — this alone can appear as a full 9-mark Part B question.

2. **8255 Modes — Control Word + Interface Design** (Module IV, Part D): The control word format for Mode 0/1/2 and a numerical problem asking you to design an interface (compute control word) for a given I/O configuration. Mode 1 handshake signals (IBF, OBF, STB, ACK, INTR) must be memorized. This is the most numerically tested topic in Part D.

3. **8051 Architecture (Module V, 20% weight, Part E)**: The internal architecture diagram, register banks, internal RAM map (00H-1FH register banks, 20H-2FH bit-addressable, 30H-7FH GPR, 80H-FFH SFR), interrupt vector addresses (INT0=0003H, TF0=000BH, INT1=0013H, TF1=001BH, Serial=0023H), and I/O port functions (P3 alternate functions especially) — expect one full 10-mark Part E question entirely on this.

4. **8051 Assembly Programming** (Module VI, 20% weight): Writing programs for arithmetic (addition/subtraction of multi-byte numbers, BCD arithmetic), array processing (sum/max/min), and delay generation using DJNZ. Expect at least 2 of the 6 Part E questions to be programming problems. Practice writing programs from scratch.

5. **8086 Addressing Modes + Instruction Set** (Module II, Part A/B): Short 3-mark Part A questions consistently ask for definitions and examples of each addressing mode. Know all 7 modes with one opcode example each. For Part B, subroutine and macro writing questions appear.

6. **Interrupt Handling in 8086** (Module III, Part C/D): The vector table structure (256 × 4 bytes), how INTR→INTA→type→ISR sequence works, ISR writing with register save/restore and IRET. The 8259 PIC architecture (IRR, ISR, IMR, ICW1-ICW4) is tested in Part D.

7. **8254 Timer Modes** (Module VI, Part E): The 6 operating modes must be distinguished by waveform shape and use case. Mode 2 (Rate Generator) and Mode 3 (Square Wave) are most tested — know the output waveform and counter reload behavior. Control word calculation for a given frequency is a common numerical.

8. **Minimum vs Maximum Mode** (Module I): A direct comparison question appears in almost every paper. Know which signals differ, the role of the 8288 Bus Controller, and when each mode is used.

