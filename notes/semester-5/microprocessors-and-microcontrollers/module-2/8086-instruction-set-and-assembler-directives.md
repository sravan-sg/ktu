# 8086 Instruction Set and Assembler Directives

## 1. Explanation

The 8086 microprocessor features a rich, orthogonal instruction set designed for 16-bit register-memory architectures. Instructions range from 1 to 6 bytes in length, depending on addressing modes and operand types.

---

### Classification of the 8086 Instruction Set

The instructions are functionally categorized into six groups:

#### 1. Data Transfer Instructions
- **`MOV destination, source`**: Transfers a byte or word. Cannot transfer memory-to-memory directly, nor immediate-to-segment register directly.
- **`PUSH source` / `POP destination`**: Pushes operand onto stack (decrements `SP` by 2, then writes word at `SS:SP`); POP reads word from `SS:SP`, then increments `SP` by 2.
- **`XCHG op1, op2`**: Swaps contents of two registers or a register and a memory location.
- **`XLAT` (Translate)**: Table look-up translation: `AL ← [BX + AL]`. Used for code conversion (e.g., ASCII to 7-segment).
- **`IN accumulator, port` / `OUT port, accumulator`**: Fixed port ($0\text{–}255$) or variable port via register `DX` ($0\text{–}65535$).
- **`LEA reg16, memory` (Load Effective Address)**: Loads the 16-bit offset address of memory operand into a register (e.g., `LEA SI, ARRAY`).
- **`LDS reg16, mem32` / `LES reg16, mem32`**: Loads a 16-bit offset into `reg16` and the next 16-bit segment base into `DS` or `ES`.

#### 2. Arithmetic Instructions
- **Addition**: `ADD dst, src`, `ADC dst, src` (Add with carry), `INC dst` (does not affect CF).
- **Subtraction**: `SUB dst, src`, `SBB dst, src` (Subtract with borrow), `DEC dst`, `NEG dst` (2's complement negation), `CMP dst, src` (evaluates `dst - src`, updates flags, discards result).
- **Multiplication**:
  - `MUL src` (Unsigned): Byte: `AX = AL * src`. Word: `DX:AX = AX * src`.
  - `IMUL src` (Signed): Signed multiplication preserving 2's complement signs.
- **Division**:
  - `DIV src` (Unsigned): Byte: `AL = AX / src` (Quotient), `AH = AX % src` (Remainder). Word: `AX = (DX:AX) / src`, `DX = (DX:AX) % src`.
  - `IDIV src` (Signed): Signed integer division.
- **Sign Extension**: `CBW` (Convert Byte to Word: signs `AL` into `AH`), `CWD` (Convert Word to Doubleword: signs `AX` into `DX`).
- **BCD & ASCII Adjustments**: `DAA` (Decimal Adjust after Addition), `DAS` (Decimal Adjust after Subtraction), `AAA`, `AAS`, `AAM` (ASCII Adjust for Multiply), `AAD` (ASCII Adjust before Division).

#### 3. Logical & Bit Manipulation Instructions
- **Boolean Logic**: `AND dst, src`, `OR dst, src`, `XOR dst, src`, `NOT dst`, `TEST dst, src` (performs `AND`, updates flags, discards result).
- **Shift Operations**:
  - `SHL` / `SAL`: Logical/Arithmetic shift left (vacated LSB filled with 0, MSB enters CF).
  - `SHR`: Logical shift right (vacated MSB filled with 0, LSB enters CF).
  - `SAR`: Arithmetic shift right (preserves MSB sign bit, LSB enters CF).
- **Rotate Operations**:
  - `ROL` / `ROR`: Rotate left/right without carry.
  - `RCL` / `RCR`: Rotate left/right through carry flag (`CF` acts as 9th or 17th bit).

#### 4. String Manipulation Instructions
Operate on arrays of bytes or words using `DS:SI` (source) and `ES:DI` (destination). If Direction Flag `DF = 0` (`CLD`), pointers auto-increment; if `DF = 1` (`STD`), pointers auto-decrement.
- **`MOVSB` / `MOVSW`**: Move string byte/word from `DS:SI` to `ES:DI`.
- **`CMPSB` / `CMPSW`**: Compare string elements (`[DS:SI] - [ES:DI]`).
- **`SCASB` / `SCASW`**: Scan string (`AL/AX - [ES:DI]`).
- **`LODSB` / `LODSW`**: Load string byte/word into `AL/AX` from `DS:SI`.
- **`STOSB` / `STOSW`**: Store `AL/AX` into `ES:DI`.
- **Repeat Prefixes**:
  - `REP`: Repeat while `CX != 0` (used with `MOVS`, `STOS`).
  - `REPE` / `REPZ`: Repeat while `CX != 0` and `ZF = 1` (used with `CMPS`, `SCAS`).
  - `REPNE` / `REPNZ`: Repeat while `CX != 0` and `ZF = 0`.

#### 5. Control Transfer Instructions
- **Unconditional Jump**: `JMP target` (Short: 8-bit displacement; Near: 16-bit intrasegment; Far: 32-bit intersegment).
- **Conditional Jumps**:
  - Based on general flags: `JZ`/`JE` ($ZF=1$), `JNZ`/`JNE` ($ZF=0$), `JC`/`JB` ($CF=1$), `JNC`/`JNB` ($CF=0$), `JS` ($SF=1$), `JNS` ($SF=0$), `JO` ($OF=1$), `JNO` ($OF=0$).
  - For unsigned comparisons: `JA`/`JNBE` ($CF=0 \land ZF=0$), `JAE`/`JNB` ($CF=0$), `JB`/`JNAE` ($CF=1$), `JBE`/`JNA` ($CF=1 \lor ZF=1$).
  - For signed comparisons: `JG`/`JNLE` ($ZF=0 \land SF=OF$), `JGE`/`JNL` ($SF=OF$), `JL`/`JNGE` ($SF \ne OF$), `JLE`/`JNG` ($ZF=1 \lor SF \ne OF$).
- **Iteration Controls**: `LOOP target` (`CX ← CX - 1`, jump if `CX != 0`), `LOOPZ`/`LOOPE` (jump if `CX != 0` and `ZF = 1`), `LOOPNZ`/`LOOPNE` (jump if `CX != 0` and `ZF = 0`), `JCXZ target` (jump if `CX == 0`).
- **Subroutine Call and Return**: `CALL proc_name` (pushes return address onto stack), `RET` / `RET n` (pops return address, optionally adds $n$ to SP).
- **Software Interrupts**: `INT n` (pushes Flags, CS, IP; jumps to vector $n$), `IRET` (pops IP, CS, Flags).

#### 6. Processor Control & Machine Instructions
- `CLC` (Clear CF), `STC` (Set CF), `CMC` (Complement CF).
- `CLD` (Clear DF), `STD` (Set DF).
- `CLI` (Clear IF — disable maskable interrupts), `STI` (Set IF — enable interrupts).
- `NOP` (No Operation), `HLT` (Halt CPU until interrupt/reset), `WAIT` (Wait for TEST# pin), `LOCK` (Bus lock prefix).

---

### Assembler Directives

Assembler directives are commands to the assembler tool (MASM/TASM) that govern segment allocation, variable declarations, memory sizing, and symbols. They **do not generate machine code instructions** directly.

1. **Data Allocation Directives**:
   - `DB` (Define Byte — 8 bits): `VAR1 DB 55H, 'A', ?`
   - `DW` (Define Word — 16 bits): `VAR2 DW 1234H, 10 DUP(0)`
   - `DD` (Define Doubleword — 32 bits): `PTR1 DD 12345678H`
   - `DQ` (Define Quadword — 64 bits): `FLOAT1 DQ 1.25`
   - `DT` (Define Ten Bytes — 80 bits BCD): `PACKED DT 1234567890H`
   - `DUP`: Duplication operator for arrays: `BUFFER DB 100 DUP(?)`

2. **Segment Definition Directives**:
   - `SEGMENT` and `ENDS`: Delineate the boundary of a logical memory segment:
     ```asm
     DATA_SEG SEGMENT
         NUM1 DW 1234H
     DATA_SEG ENDS
     ```
   - `ASSUME`: Informs the assembler which physical segment register corresponds to which logical segment:
     ```asm
     ASSUME CS:CODE_SEG, DS:DATA_SEG, SS:STACK_SEG
     ```

3. **Symbolic & Address Directives**:
   - `EQU` (Equate): Defines constants without allocating memory: `COUNT EQU 100`.
   - `OFFSET`: Returns the 16-bit displacement of a variable relative to segment start: `MOV SI, OFFSET ARRAY`.
   - `SEG`: Returns the 16-bit segment base of a variable: `MOV AX, SEG ARRAY`.
   - `PTR`: Type-override operator specifying operand memory size: `MOV BYTE PTR [BX], 0` vs `MOV WORD PTR [BX], 0`.
   - `ORG` (Origin): Sets the assembler location counter: `ORG 0100H`.
   - `PROC` and `ENDP`: Demarcates a procedure/subroutine (with `NEAR` or `FAR` attribute).
   - `END`: Marks the physical end of source code and specifies entry-point label: `END START`.

---

## 2. Example: 8086 Assembly Program Structure

```asm
DATA SEGMENT
    NUM1    DW  0005H
    FACT    DW  ?
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
START:
    MOV AX, DATA        ; Initialize DS segment register
    MOV DS, AX
    
    MOV CX, NUM1        ; Load N into CX
    MOV AX, 1           ; Accumulator holds product
    
CALC:
    MUL CX              ; DX:AX = AX * CX
    LOOP CALC           ; CX = CX - 1; loop if CX != 0
    
    MOV FACT, AX        ; Store 16-bit factorial result
    
    MOV AH, 4CH         ; DOS exit interrupt
    INT 21H
CODE ENDS
END START
```

---

## 3. Applications & Use Cases

1. **Embedded Firmware Development**: Industrial automation boards running x86 processors use low-level bit manipulation (`TEST`, `AND`, `OR`, `XOR`) for sensor reading and actuator toggling.
2. **Device Driver Development**: Drivers interact with peripheral controller registers using direct and indirect I/O instructions (`IN`, `OUT` via `DX`).
3. **High-Performance Assembly Routines**: Modern C/C++ compilers inline optimized x86 assembly for cryptographic hash evaluation and string scanning (`REP MOVSB`).

---

## 4. Solved Numerical / Analytical Examples

### Example 1: DAA Arithmetic Adjustment [Analytical]
**Problem**:
Show how the 8086 executes packed BCD addition using the `DAA` instruction for:
$38\text{H} + 49\text{H}$ (representing decimal $38 + 49 = 87$).

**Solution**:
1. Binary addition executed by `ADD AL, BL`:
   $$\text{AL} = 38\text{H} = 0011\ 1000_2$$
   $$\text{BL} = 49\text{H} = 0100\ 1001_2$$
   $$\text{Sum} = 0011\ 1000_2 + 0100\ 1001_2 = 1000\ 0001_2 = 81\text{H}$$
   - Lower nibble sum: $8 + 9 = 17 = 11\text{H} > 9 \implies$ Auxiliary Carry `AF` = 1.
2. `DAA` Execution Rules:
   - Rule 1: Since lower nibble is $> 9$ or $\text{AF} = 1$, add $06\text{H}$ to AL:
     $$\text{AL} = 81\text{H} + 06\text{H} = 87\text{H}$$
   - Rule 2: Upper nibble is $8 \le 9$ and Carry Flag `CF` = 0, so no upper adjustment needed.
3. Final Result in AL: **$87\text{H}$** (decimal 87 in packed BCD representation).

---

### Example 2: Packed BCD to ASCII Conversion
**Problem**:
Write an 8086 assembly snippet to convert a packed BCD byte in `AL` (e.g., $59\text{H}$) into its two ASCII character equivalents in `AH` and `AL` (ASCII '5' = $35\text{H}$, '9' = $39\text{H}$).

**Solution**:
```asm
    MOV BL, AL          ; Copy original packed byte to BL (BL = 59H)
    AND AL, 0FH         ; Mask upper nibble: AL = 09H
    OR  AL, 30H         ; Convert to ASCII: AL = 39H ('9')
    
    MOV AH, BL          ; Restore original byte: AH = 59H
    AND AH, 0F0H        ; Mask lower nibble: AH = 50H
    SHR AH, 4           ; Shift right 4 bits: AH = 05H
    OR  AH, 30H         ; Convert to ASCII: AH = 35H ('5')
    ; Result: AH = 35H ('5'), AL = 39H ('9')
```

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [KTU Dec 2018 / May 2019 — 9 Marks]
**Question**:
Explain the following 8086 instructions with examples:
(a) `XLAT`
(b) `LEA`
(c) `DAA`
(d) `CBW`
(e) `LOOP`

**Solution**:

**(a) `XLAT` (Translate Byte)**:
- Replaces the byte in `AL` with a byte from a lookup table in memory addressed by `DS:[BX + AL]`.
- Register `BX` holds the 16-bit offset of the table start, and `AL` holds the 8-bit index.
- *Example*: Translating a hex digit ($0\text{–}15$) to ASCII:
  ```asm
  LEA BX, HEX_TABLE
  MOV AL, 0BH          ; Index 11 (corresponds to 'B')
  XLAT                 ; AL becomes 'B' (42H)
  ```

**(b) `LEA` (Load Effective Address)**:
- Computes the 16-bit memory offset (effective address) of the source operand and loads it into the destination register without accessing memory contents.
- *Example*: `LEA SI, [BX + DI + 10H]` computes $\text{EA} = \text{BX} + \text{DI} + 10\text{H}$ and stores the address in `SI`.

**(c) `DAA` (Decimal Adjust after Addition)**:
- Adjusts the 8-bit binary sum in `AL` into packed BCD format after an `ADD` or `ADC` instruction.
- If lower nibble $> 9$ or $\text{AF}=1$, it adds $06\text{H}$ to AL. If upper nibble $> 9$ or $\text{CF}=1$, it adds $60\text{H}$ to AL and sets $\text{CF}=1$.

**(d) `CBW` (Convert Byte to Word)**:
- Extends the sign bit (bit 7) of `AL` through all bits of `AH`, converting a signed 8-bit integer in `AL` into a signed 16-bit integer in `AX`.
- *Example*: If `AL = 85H` (negative), `CBW` sets `AH = FFH`, making `AX = FF85H`.

**(e) `LOOP target`**:
- Decrements `CX` by 1 (`CX ← CX - 1`). If `CX != 0`, it branches to `target`. If `CX == 0`, execution continues with the next sequential instruction.

---

### Question 2 [KTU June 2022 / Dec 2021 — 3 Marks]
**Question**:
What are assembler directives? Explain `ASSUME`, `EQU`, and `ORG`.

**Solution**:

**Assembler Directives** are instructions addressed specifically to the assembler program (such as MASM or TASM) during translation of assembly code into machine code. They do not generate machine execution instructions.

1. **`ASSUME`**: Informs the assembler of the association between logical segment names defined in code and the physical segment registers (`CS`, `DS`, `SS`, `ES`):
   ```asm
   ASSUME CS:CODE_SEG, DS:DATA_SEG
   ```
2. **`EQU` (Equate)**: Assigns a fixed symbolic name to a numerical constant or string without allocating physical memory storage:
   ```asm
   ARRAY_SIZE EQU 50
   ```
3. **`ORG` (Origin)**: Sets the assembler's location counter to a specified address offset, determining where subsequent instructions or data will be positioned in memory:
   ```asm
   ORG 0100H    ; Standard entry point offset for .COM executable files
   ```

