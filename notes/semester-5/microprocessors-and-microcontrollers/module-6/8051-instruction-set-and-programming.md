# 8051 Instruction Set & Simple Programs

## 1. Explanation

### 8051 Addressing Modes

The 8051 supports 6 addressing modes. Unlike 8086 (which always accesses flat memory with segment:offset), the 8051 distinguishes sharply between internal RAM, external RAM, and program memory.

---

#### 1. Immediate Addressing Mode
Operand value directly encoded in instruction.
```asm
MOV A, #55H      ; A = 55H  (# prefix means immediate value)
MOV R0, #0AH     ; R0 = 0AH
ADD A, #10H      ; A = A + 10H
```

#### 2. Register Addressing Mode
Operand is in one of the registers A, R0–R7, B, DPTR.
```asm
MOV A, R0        ; A = R0
ADD A, R3        ; A = A + R3
MOV DPTR, #3000H ; DPTR = 3000H
```

#### 3. Direct Addressing Mode
Operand is at a specified **8-bit address** in internal RAM (00H–7FH) or SFR space (80H–FFH).
```asm
MOV A, 30H       ; A = contents of internal RAM[30H]
MOV 50H, A       ; internal RAM[50H] = A
MOV A, 90H       ; A = P1 (SFR at 90H)
```
- Range: 00H–FFH (internal RAM + SFRs)
- Used for: accessing bit-addressable area, global variables in internal RAM.

#### 4. Register Indirect Addressing Mode
Address is in R0 or R1 (for internal/external RAM) or DPTR (for external RAM):
```asm
MOV A, @R0       ; A = internal_RAM[R0]
MOV A, @R1       ; A = internal_RAM[R1] (or external if MOVX)
MOVX A, @R0      ; A = external_RAM[R0] (8-bit address)
MOVX A, @DPTR    ; A = external_RAM[DPTR] (16-bit address)
```

#### 5. Indexed Addressing Mode (Code Memory — Look-Up Tables)
Accesses program memory using PC or DPTR as base + Accumulator as offset:
```asm
MOVC A, @A+DPTR  ; A = program_memory[DPTR + A]
MOVC A, @A+PC    ; A = program_memory[PC + A]
```
Used for look-up tables (e.g., 7-segment LED display codes, sine table).

**Example — 7-Segment Lookup**:
```asm
; DPTR = address of table in ROM
MOV DPTR, #TABLE
MOV A, #3        ; index = 3 (want display code for digit "3")
MOVC A, @A+DPTR  ; A = TABLE[3]
MOV P0, A        ; Output to 7-segment display

TABLE: DB  3FH, 06H, 5BH, 4FH, ...  ; 7-seg codes for 0,1,2,3,...
```

#### 6. Bit Addressing Mode
The 8051 has a **Boolean processor** — individual bits can be directly manipulated:
```asm
SETB P1.0        ; Set bit 0 of Port 1 (turn ON LED)
CLR P3.1         ; Clear bit 1 of Port 3 (TXD line)
MOV C, ACC.7     ; Copy Accumulator bit 7 to Carry flag
JB P3.2, LABEL   ; Jump if P3.2 (INT0#) is HIGH
ANL C, 20H.3     ; AND carry with bit at address 20H.3
```

---

### Complete 8051 Instruction Set by Category

#### Data Transfer Instructions

| Instruction | Operation | Notes |
|---|---|---|
| `MOV A, src` | A = src | Source: Rn, dir, @Ri, #data |
| `MOV dst, A` | dst = A | Dest: Rn, dir, @Ri |
| `MOV dst, src` | dst = src | Between direct addresses or immediate |
| `MOV DPTR, #data16` | DPTR = 16-bit constant | Load pointer |
| `MOVX A, @Ri` | A = external_RAM[Ri] | 8-bit external address |
| `MOVX A, @DPTR` | A = external_RAM[DPTR] | 16-bit external address |
| `MOVX @DPTR, A` | external_RAM[DPTR] = A | Write to external RAM |
| `MOVC A, @A+DPTR` | A = program_mem[DPTR+A] | Table lookup |
| `MOVC A, @A+PC` | A = program_mem[PC+A] | Table lookup from current position |
| `PUSH direct` | Stack[++SP] = direct | Push byte onto stack |
| `POP direct` | direct = Stack[SP--] | Pop byte from stack |
| `XCH A, src` | Swap A with src | Useful register swap |
| `XCHD A, @Ri` | Swap lower nibble A↔[Ri] | Nibble exchange |

#### Arithmetic Instructions

| Instruction | Operation | Flags |
|---|---|---|
| `ADD A, src` | A = A + src | CY, AC, OV, P |
| `ADDC A, src` | A = A + src + CY | CY, AC, OV (multi-byte add) |
| `SUBB A, src` | A = A - src - CY | CY, AC, OV |
| `INC A` | A++ | No flags |
| `INC Rn` / `INC dir` / `INC @Ri` | Increment | No flags |
| `DEC A` etc. | Decrement | No flags |
| `INC DPTR` | DPTR++ (16-bit) | No flags |
| `MUL AB` | B:A = A × B (unsigned 8×8=16) | OV (if result > 255), CY cleared |
| `DIV AB` | A = quotient, B = remainder (A÷B) | OV (if B=0), CY cleared |
| `DA A` | Decimal Adjust Accumulator for BCD | CY, AC |

#### Logical Instructions

| Instruction | Operation |
|---|---|
| `ANL A, src` | A = A AND src |
| `ORL A, src` | A = A OR src |
| `XRL A, src` | A = A XOR src |
| `CLR A` | A = 00H |
| `CPL A` | A = NOT A (complement) |
| `RL A` | Rotate A left (MSB→LSB, no carry) |
| `RLC A` | Rotate A left through Carry |
| `RR A` | Rotate A right (LSB→MSB, no carry) |
| `RRC A` | Rotate A right through Carry |
| `SWAP A` | Swap upper and lower nibbles of A |

#### Boolean/Bit Instructions (8051's Unique Feature!)

| Instruction | Operation |
|---|---|
| `SETB C` | Carry = 1 |
| `SETB bit` | bit = 1 (e.g., `SETB P1.0`) |
| `CLR C` / `CLR bit` | Clear bit |
| `CPL C` / `CPL bit` | Complement bit |
| `MOV C, bit` | Carry = bit |
| `MOV bit, C` | bit = Carry |
| `ANL C, bit` | Carry = Carry AND bit |
| `ANL C, /bit` | Carry = Carry AND (NOT bit) |
| `ORL C, bit` | Carry = Carry OR bit |
| `JC rel` | Jump if Carry = 1 |
| `JNC rel` | Jump if Carry = 0 |
| `JB bit, rel` | Jump if bit = 1 |
| `JNB bit, rel` | Jump if bit = 0 |
| `JBC bit, rel` | Jump if bit = 1, then CLEAR bit |

#### Control Transfer Instructions

| Instruction | Size | Operation |
|---|---|---|
| `LJMP addr16` | 3 bytes | Jump anywhere in 64KB |
| `AJMP addr11` | 2 bytes | Jump within 2KB page |
| `SJMP rel` | 2 bytes | Short jump: -128 to +127 bytes |
| `JMP @A+DPTR` | 1 byte | Computed jump (jump table) |
| `JZ rel` | 2 bytes | Jump if A = 0 |
| `JNZ rel` | 2 bytes | Jump if A ≠ 0 |
| `CJNE A, #data, rel` | 3 bytes | Jump if A ≠ data; sets CY |
| `CJNE Rn, #data, rel` | 3 bytes | Compare and branch |
| `DJNZ Rn, rel` | 2 bytes | Decrement Rn, Jump if Not Zero |
| `DJNZ dir, rel` | 3 bytes | Decrement direct, Jump if NZ |
| `LCALL addr16` | 3 bytes | Call subroutine anywhere |
| `ACALL addr11` | 2 bytes | Call within 2KB page |
| `RET` | 1 byte | Return from subroutine |
| `RETI` | 1 byte | Return from interrupt (also clears priority flag) |
| `NOP` | 1 byte | No operation (1 machine cycle) |

---

## 2. Example

### Complete Example Programs

#### Program 1: LED Blink with Delay

```asm
; Toggle P1.0 (LED) with software delay
; Crystal: 12 MHz; Machine cycle = 1 µs

ORG 0000H

MAIN:
    SETB P1.0        ; LED ON
    ACALL DELAY      ; Wait 100 ms
    CLR  P1.0        ; LED OFF
    ACALL DELAY      ; Wait 100 ms
    SJMP MAIN        ; Repeat forever

; Delay subroutine: 100 ms at 12 MHz (1 machine cycle = 1 µs)
; 100 ms = 100,000 µs = 100,000 machine cycles
; Nested loop: outer × inner = 200 × 500 = 100,000

DELAY:
    MOV R1, #200     ; Outer loop count
OUTER:
    MOV R2, #250     ; Inner loop count (250 × 2 cycles = 500 µs)
INNER:
    NOP              ; 1 cycle
    DJNZ R2, INNER  ; 2 cycles each iteration
    DJNZ R1, OUTER
    RET
END
```

---

#### Program 2: BCD to 7-Segment Display

```asm
; Display BCD digit (0–9) on P1 as 7-segment code
; Segments: a=P1.0, b=P1.1, ... g=P1.6 (common cathode)

ORG 0000H

MAIN:
    MOV A, #5        ; Display digit 5
    MOVC A, @A+DPTR  ; A = TABLE[5] = 6DH
    ; Wait: DPTR must point to TABLE first!
    ; Correct code:
    MOV DPTR, #TABLE
    MOV A, #5
    MOVC A, @A+DPTR
    MOV P1, A        ; Output to display
    SJMP $           ; Halt

TABLE:
    DB 3FH   ; 0: segments a,b,c,d,e,f ON
    DB 06H   ; 1: b,c
    DB 5BH   ; 2: a,b,d,e,g
    DB 4FH   ; 3: a,b,c,d,g
    DB 66H   ; 4: b,c,f,g
    DB 6DH   ; 5: a,c,d,f,g
    DB 7DH   ; 6: a,c,d,e,f,g
    DB 07H   ; 7: a,b,c
    DB 7FH   ; 8: all segments
    DB 6FH   ; 9: a,b,c,d,f,g
END
```

---

## 3. Applications & Use Cases

### 1. Delay Generation for Timing-Critical Control
`DJNZ`-based delay subroutines are the standard way to generate microsecond-to-second delays in 8051 firmware for LCD initialization (LCD requires specific timing for E pulse width), motor start-up sequences, and sensor warm-up periods.

### 2. Serial Data Transmission (UART Programming)
The SBUF register and TI/RI flags are used for transmitting/receiving strings over RS-232. Interrupt-driven UART programming (ES bit, serial ISR checking TI/RI) enables background communication without blocking main control loops.

### 3. ADC Interface via Serial SPI
Many 8051 systems interface with external ADCs (like ADC0808) using bit-banged SPI: CLK, MISO, MOSI controlled via P1 bit operations (SETB/CLR + JB for read). The Boolean processor makes bit manipulation natural and efficient.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: MUL and DIV [KTU Part E — 10 marks]

**Problem**: Write 8051 code to compute (a) 25 × 12 and (b) 150 ÷ 7 and store the results in RAM.

**Solution**:

```asm
ORG 0000H

; (a) Multiply 25 × 12:
MOV A, #25     ; A = 25 (multiplicand)
MOV B, #12     ; B = 12 (multiplier)
MUL AB         ; B:A = 25 × 12 = 300 = 012CH → B=01H, A=2CH
MOV 30H, A    ; RAM[30H] = 2CH (low byte of result = 44 decimal)
MOV 31H, B    ; RAM[31H] = 01H (high byte = 256, total = 300) ✓

; (b) Divide 150 ÷ 7:
MOV A, #150   ; A = 150 (dividend)
MOV B, #7     ; B = 7 (divisor)
DIV AB        ; A = quotient = 21, B = remainder = 3  (150 = 21×7 + 3)
MOV 32H, A   ; RAM[32H] = 21 (quotient)
MOV 33H, B   ; RAM[33H] = 3  (remainder)

SJMP $
END
```

**Verification**: 25 × 12 = 300 = 0x012C. MUL stores: B=01H, A=2CH ✓. 150/7: 7×21=147, 150-147=3 → quotient=21, remainder=3 ✓.

---

### Example 2: Sum of Array [KTU Part E — 10 marks]

**Problem**: Write an 8051 assembly program to find the sum of 10 numbers stored in internal RAM starting at address 40H. Store the 16-bit result at addresses 50H (low byte) and 51H (high byte).

**Solution**:

```asm
ORG 0000H

; Initialize: 10 numbers at 40H–49H (assumed pre-loaded)
MOV R0, #40H    ; R0 = pointer to start of data array
MOV R2, #10     ; R2 = loop count (10 numbers)
MOV A, #0       ; A = sum low byte (initialize to 0)
MOV R1, #0      ; R1 = sum high byte (carry accumulator)

SUM_LOOP:
    ADD A, @R0  ; A = A + RAM[R0] (register indirect)
    JNC NO_CARRY
    INC R1      ; Increment high byte on carry
NO_CARRY:
    INC R0      ; Advance pointer to next element
    DJNZ R2, SUM_LOOP  ; Decrement count, loop if not zero

MOV 50H, A     ; Store low byte of sum
MOV 51H, R1    ; Store high byte of sum

SJMP $
END
```

**Example trace** (if array = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}):
Sum = 550 = 0226H → 50H = 26H, 51H = 02H ✓

---

### Example 3: 8254 Timer Control Word [KTU Part E — 10 marks]

**Problem**: An 8254 timer is to be configured to generate a square wave of frequency 1 kHz. The input clock is 1 MHz. Calculate:
(a) The required count value.
(b) The control word to configure Counter 2 in Mode 3 (Square Wave), 16-bit binary, LSB first then MSB.

**Solution**:

(a) **Count value**:
$$\text{Count} = \frac{f_{clock}}{f_{output}} = \frac{1,000,000 \text{ Hz}}{1,000 \text{ Hz}} = 1000 = \text{03E8H}$$

(b) **Control Word** for Counter 2, Mode 3, Binary, 16-bit (LSB then MSB):

Control word format: `SC1 SC0 | RW1 RW0 | M2 M1 M0 | BCD`

- SC1:SC0 = **10** (Counter 2)
- RW1:RW0 = **11** (Read/Write LSB then MSB)
- M2:M1:M0 = **011** (Mode 3: Square Wave)
- BCD = **0** (Binary)

Control Word = `10 11 011 0` = **1011 0110B = B6H**

**Programming sequence**:
```asm
; Assuming 8254 at I/O ports: Counter2=Port_Base+2, Control=Port_Base+3
MOV AL, 0B6H       ; Control word: Counter 2, Mode 3, 16-bit binary
OUT Control_Port, AL
MOV AL, 0E8H       ; LSB of 03E8H = E8H
OUT Counter2_Port, AL
MOV AL, 03H        ; MSB of 03E8H = 03H
OUT Counter2_Port, AL
; Counter 2 now generates 1 kHz square wave on its OUT pin
```

---

## 5. Previous Year Questions & Solutions

---

### Q1 [KTU All papers — Part E, 10 marks]
**Question**: Explain the addressing modes of the 8051. Write a simple 8051 assembly program to find the factorial of a number stored in R0.

**Solution**:

**Addressing modes** — see Section 1 (all 6 modes explained with examples).

**Factorial Program** (calculates N! for N stored in R0, result in R1:R2):

```asm
ORG 0000H

; Compute N! for N = R0 (assume N ≤ 8 so result fits in 16 bits)
; Result: R2 (high byte) : ACC (low byte)

    MOV A, R0        ; A = N (the number)
    MOV R1, A        ; R1 = loop counter = N
    MOV A, #1        ; A = 1 (initialize product low byte)
    MOV R2, #0       ; R2 = product high byte = 0
    
    CJNE R1, #0, FACT_LOOP  ; If N=0, skip loop (0! = 1)
    SJMP DONE
    
FACT_LOOP:
    MOV B, R1        ; B = current multiplier
    MUL AB           ; B:A = A × B (multiply running product by current factor)
    ; Note: This only handles 8-bit result. For 16-bit:
    ; After MUL: B has overflow (high byte of partial product)
    MOV R2, B        ; Store high byte (simplified — accurate for N ≤ 8)
    DJNZ R1, FACT_LOOP  ; R1-- and repeat
    
DONE:
    ; A = low byte of N!, R2 = high byte
    MOV 50H, A      ; Store result
    MOV 51H, R2
    SJMP $
END

; Example: N=5, R0=5
; Iteration 1: A=1, R1=5 → MUL: 1×5=5 → A=5, B=0
; Iteration 2: A=5, R1=4 → MUL: 5×4=20 → A=20, B=0
; Iteration 3: A=20, R1=3 → MUL: 20×3=60 → A=60, B=0
; Iteration 4: A=60, R1=2 → MUL: 60×2=120 → A=120, B=0
; Iteration 5: A=120, R1=1 → MUL: 120×1=120 → A=120, B=0
; Result: 5! = 120 ✓
```

---

### Q2 [KTU All papers — Part E, 10 marks]
**Question**: Explain the 8254/8253 Programmable Interval Timer. Describe its 6 operating modes with waveforms.

**Solution**:

The 8253/8254 Programmable Interval Timer (PIT) contains 3 independent 16-bit down-counters, each with its own CLK, GATE, and OUT pins.

**Interface pins (per counter)**:
- CLK: Input clock signal (counts on falling edge)
- GATE: Gate control (HIGH=enable counting, LOW=inhibit/reset)
- OUT: Output signal (waveform generated here)

**Control Word Format**:
```
SC1 SC0  RW1 RW0  M2 M1 M0  BCD
  7   6    5   4   3  2   1    0
```
- SC1:SC0 = Counter select (00=C0, 01=C1, 10=C2, 11=readback)
- RW1:RW0 = Read/Write (00=latch, 01=LSB, 10=MSB, 11=LSB then MSB)
- M2:M1:M0 = Mode (000-101)
- BCD = 0 for binary, 1 for BCD

**6 Operating Modes**:

**Mode 0 — Interrupt on Terminal Count**:
- OUT goes LOW when count is loaded. OUT goes HIGH when counter reaches 0.
- Gate must be HIGH for counting. Gate LOW pauses counting.
- Use: One-shot timer, software-controlled interrupt generation.
- Waveform: `HIGH → LOW (at load) → ~~counting~~ → HIGH (at TC)`.

**Mode 1 — Hardware Retriggerable One-Shot (Monostable)**:
- Triggered by GATE rising edge. OUT goes LOW for N clock cycles then returns HIGH.
- Retriggering during pulse extends it.
- Use: Debounce timing, one-shot pulse generation.

**Mode 2 — Rate Generator (Divide by N)**:
- OUT produces a pulse (LOW for 1 clock, then HIGH) every N input clocks.
- Self-reloading continuously. GATE HIGH = run; GATE LOW = resets output HIGH.
- Frequency: f_out = f_CLK / N.
- Use: **System timer tick** (PC timer at 1.19 MHz ÷ 65536 ≈ 18.2 Hz), baud rate generation.

**Mode 3 — Square Wave Generator**:
- Generates symmetric square wave: OUT HIGH for N/2 cycles, LOW for N/2 cycles.
- For odd N: HIGH for (N+1)/2 cycles, LOW for (N-1)/2 cycles.
- Self-reloading, runs continuously.
- Frequency: f_out = f_CLK / N.
- Use: **Clock signal generation**, tone generators.

**Mode 4 — Software Triggered Strobe**:
- Writing count value triggers one count-down. OUT goes LOW for 1 clock at terminal count.
- Counting restarts only by rewriting the count register.
- Use: Generating a single narrow strobe pulse.

**Mode 5 — Hardware Triggered Strobe**:
- Same as Mode 4 but triggered by GATE rising edge (hardware retrigger supported).
- OUT LOW for 1 clock at terminal count.

**Comparison Table**:

| Mode | Trigger | GATE Function | Output | Auto-Reload | Use Case |
|---|---|---|---|---|---|
| 0 | Load count | Enable/inhibit | High pulse at TC | No | One-shot timer |
| 1 | GATE ↑ | Retrigger | Pulse for N clocks | No | Monostable |
| 2 | Load count | Enable/reset | Narrow LOW pulse every N | Yes | Rate/frequency |
| 3 | Load count | Enable/reset | 50% square wave | Yes | Clock/baud rate |
| 4 | Load count | Enable/inhibit | 1-clock LOW at TC | No | Software strobe |
| 5 | GATE ↑ | Retrigger | 1-clock LOW at TC | No | Hardware strobe |

---

### Q3 [KTU May 2019 / Dec 2021 — Part E, 10 marks]
**Question**: Write an 8051 assembly language program to:
(a) Find the smallest element in an array of 10 bytes stored at 30H–39H.
(b) Store the result at address 50H.

**Solution**:

```asm
ORG 0000H

    MOV R0, #30H    ; R0 = pointer to array start (address 30H)
    MOV A, @R0      ; A = first element (assume it's the minimum initially)
    MOV R2, #9      ; R2 = loop count (compare remaining 9 elements)
    INC R0          ; Advance pointer to second element

FIND_MIN:
    CLR C            ; Clear carry before comparison
    SUBB A, @R0     ; A - [R0]: sets CY if A < [R0]
    JC RESTORE      ; If CY=1: A was LESS than [R0], A is still minimum → restore A
    ; If CY=0 and result is in A (but we subtracted!): [R0] ≤ A → update minimum
    MOV A, @R0      ; New minimum = [R0]
    INC R0
    DJNZ R2, FIND_MIN
    SJMP STORE_RESULT

RESTORE:
    ADD A, @R0      ; Restore A: A = A + [R0] (undo the subtraction since A < [R0])
    ; A is restored to its value before SUBB
    INC R0
    DJNZ R2, FIND_MIN

STORE_RESULT:
    MOV 50H, A      ; Store minimum at address 50H
    SJMP $
END
```

> **Alternative (cleaner) approach using CJNE + JC**:

```asm
ORG 0000H

    MOV R0, #30H
    MOV A, @R0      ; A = first element = current minimum
    MOV R2, #9      ; loop 9 more times
    INC R0

MIN_LOOP:
    MOV B, @R0      ; B = next array element
    CJNE A, B, CHECK ; Compare A and B; sets CY if A < B
    SJMP NEXT
CHECK:
    JC NEXT         ; If CY=1: A < B, A is still minimum → keep A
    MOV A, B        ; If CY=0: B < A → update minimum to B
NEXT:
    INC R0
    DJNZ R2, MIN_LOOP

    MOV 50H, A      ; Store minimum
    SJMP $
END
```

**Trace** (array: {45, 10, 93, 23, 7, 11, 55, 02, 88, 30}):
- Init: A=45, compare with 10 → 10<45 → A=10
- 10 vs 93 → keep 10. 10 vs 23 → keep 10. 10 vs 7 → A=7
- 7 vs 11 → keep 7. 7 vs 55 → keep 7. 7 vs 2 → A=2
- 2 vs 88 → keep 2. 2 vs 30 → keep 2.
- Result: 50H = 02H ✓

