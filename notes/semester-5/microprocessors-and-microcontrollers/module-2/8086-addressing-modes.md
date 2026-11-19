# 8086 Addressing Modes

## 1. Explanation

Addressing modes define **how the operand's location is specified** in an instruction. The 8086 supports 7 fundamental addressing modes, covering a spectrum from ultra-fast register operands to complex memory addressing with multiple displacement components.

Understanding addressing modes is critical because:
- They directly determine **instruction encoding size** (1 to 6 bytes per instruction)
- They determine **execution time** (register access: 2 clocks; complex memory: 7+ clocks)
- They enable efficient data structure access, array indexing, and stack frame manipulation

---

### Addressing Mode Categories

The effective address (EA) for memory operands is computed as:
$$\text{EA} = \text{Base Register} + \text{Index Register} + \text{Displacement}$$

Where Base ∈ {BX, BP}, Index ∈ {SI, DI}, Displacement = 0, 8-bit, or 16-bit signed constant.

---

#### 1. Immediate Addressing Mode
The **operand value itself** is embedded directly within the instruction bytes.

```
Instruction: MOV AX, 1234H
            ┌───┬────────────────┐
Encoding:   │ B8│  34  │  12    │  (little-endian: low byte first)
            └───┴────────────────┘
              Opcode  Immediate data
```

- No memory access required for the operand (fastest).
- Used for: loading constants, initializing registers, comparisons.
- **Examples**: `MOV CX, 100H`, `ADD AX, 0FFH`, `CMP BX, 0`

---

#### 2. Register Addressing Mode
Both source and destination operands are in **CPU registers**.

```
Instruction: MOV AX, BX
```
- Fastest non-immediate mode — no bus cycles required.
- **Examples**: `ADD AX, BX`, `MOV CL, DH`, `XOR AX, AX` (clear AX)

---

#### 3. Direct Addressing Mode
The **effective address (EA) is specified as a 16-bit constant** in the instruction. The physical address is computed as: PA = DS × 16 + EA.

```
Instruction: MOV AX, [2000H]
Physical address = DS × 16 + 2000H
```
- EA = 16-bit displacement in instruction.
- Segment default: DS (can be overridden: `CS: MOV AX, [2000H]`).
- **Examples**: `MOV AX, [1234H]`, `MOV [COUNT], CX` (where COUNT = 2000H defined with EQU or by assembler)

---

#### 4. Register Indirect Addressing Mode
The EA is the **contents of a base register** (BX, BP, SI, or DI):
$$\text{EA} = \text{Register}$$

```
Instruction: MOV AX, [BX]     ; EA = contents of BX
             MOV AL, [SI]     ; EA = contents of SI
             MOV [DI], CX     ; EA = contents of DI
```

| Register | Default Segment | Typical Use |
|---|---|---|
| BX | DS | Data structure pointer |
| BP | SS | Stack frame base pointer |
| SI | DS | Source pointer in string operations |
| DI | ES | Destination pointer in string operations |

- **Examples**: `MOV AX, [BX]`, `INC BYTE PTR [SI]`

---

#### 5. Based Addressing Mode
EA = Base Register (BX or BP) + 8-bit or 16-bit signed displacement:
$$\text{EA} = [BX] + d8/d16 \quad \text{or} \quad \text{EA} = [BP] + d8/d16$$

```
Instruction: MOV AX, [BX+4]   ; Access 4 bytes ahead of BX
             MOV DX, [BP+10]  ; Access stack parameter at BP+10
```
- **BX-based**: Useful for accessing fields within a record/structure at a known fixed offset.
- **BP-based**: Standard for accessing function **parameters** and **local variables** on the stack:
  - `[BP+2]` → first function parameter (after CALL instruction return address)
  - `[BP+4]` → second function parameter
  - `[BP-2]` → first local variable (below BP on stack)

---

#### 6. Indexed Addressing Mode
EA = Index Register (SI or DI) + 8-bit or 16-bit displacement:
$$\text{EA} = [SI] + d8/d16 \quad \text{or} \quad \text{EA} = [DI] + d8/d16$$

```
Instruction: MOV AX, ARRAY[SI]  ; ARRAY's base address + SI offset
             MOV AX, [SI+100H]  ; SI acts as array index
```
- **Classic array indexing**: `ARRAY[SI]` where ARRAY is the base address (displacement) and SI is the runtime index.
- SI/DI can be incremented/decremented to scan through arrays element by element.

---

#### 7. Based Indexed Addressing Mode
EA = Base Register + Index Register + (optional) displacement:
$$\text{EA} = [BX/BP] + [SI/DI] + d8/d16$$

```
Instruction: MOV AX, [BX+SI]        ; EA = BX + SI
             MOV AX, [BP+DI+8]      ; EA = BP + DI + 8
             MOV AX, MATRIX[BX+SI]  ; EA = MATRIX_BASE + BX + SI
```
- **2D array access**: `MATRIX[BX+SI]` where BX = row offset and SI = column offset.
- **BP+SI/DI**: For 2D access on the stack frame.
- Most complex addressing mode — requires 7+ clock cycles for EA calculation.

---

### Complete Addressing Mode Summary

| Mode | EA Formula | Speed | Use Case |
|---|---|---|---|
| Immediate | Constant in instruction | Fastest | Load constants |
| Register | Register value | Very Fast | Register-register ops |
| Direct | 16-bit constant | Medium | Fixed-location variables |
| Register Indirect | [Reg] | Medium | Pointer dereferencing |
| Based | [BX/BP] + disp | Medium | Structure field access |
| Indexed | [SI/DI] + disp | Medium | Array indexing |
| Based Indexed | [BX/BP]+[SI/DI]+disp | Slowest | 2D arrays, stack frames |

---

## 2. Example

### Demonstrating Each Mode in a Program Snippet

```asm
; Given: ARRAY starts at DS:1000H, N=10 elements (words)
; Task: Sum all array elements into AX

    MOV AX, 0           ; Immediate: AX = 0 (initialize sum)
    MOV CX, 10          ; Immediate: CX = 10 (loop count)
    MOV SI, 0           ; Register: SI = 0 (initialize index)
    MOV BX, 1000H       ; Immediate: BX = base address of ARRAY

LOOP1:
    ADD AX, [BX+SI]    ; Based Indexed: access ARRAY[0], ARRAY[2], ...
    ADD SI, 2           ; Register+Immediate: increment SI by 2 (word size)
    LOOP LOOP1          ; CX-- and loop until CX=0
```

---

## 3. Applications & Use Cases

### 1. Compiler Backend Code Generation
When a C compiler generates code for `a[i][j]` on an x86 target, it uses Based Indexed addressing: `[BX+SI+offset]` where BX = base of 2D array, SI = row_offset = i × row_size, offset = j × element_size.

### 2. Stack Frame Management (Function Calls)
Every C function call on x86 sets up a standard stack frame using BP-based addressing:
- `PUSH BP; MOV BP, SP` creates the frame.
- Parameters accessed via `[BP+4]`, `[BP+6]`, etc.
- Local variables via `[BP-2]`, `[BP-4]`, etc.
- This is exactly how Visual Studio's disassembler shows function prologues.

### 3. String Processing
Block memory moves, string searches, and byte-by-byte processing use Register Indirect (SI for source, DI for destination) with the REP prefix for hardware-accelerated repetition.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: EA and PA Calculation [KTU Part A — 3 marks]

**Problem**: Given BX = 1500H, SI = 0200H, DS = 2000H. The instruction is `MOV AX, [BX+SI+0100H]`. Find:
(a) Effective Address (EA)
(b) Physical Address (PA)
(c) The value range of data accessed

**Solution**:

(a) **Effective Address**:
$$\text{EA} = BX + SI + \text{Displacement} = 1500H + 0200H + 0100H = 1800H$$

(b) **Physical Address**:
$$\text{PA} = DS \times 16 + EA = 2000H \times 10H + 1800H = 20000H + 1800H = 21800H$$

(c) **Data accessed**: Since `MOV AX` is a 16-bit (word) transfer:
- Low byte at PA = 21800H
- High byte at PA = 21801H
- Data range: 0000H to FFFFH (16-bit word)

---

### Example 2: Identifying Addressing Modes [KTU Part A — 3 marks]

**Problem**: Identify the addressing mode used in each instruction:

```asm
(a) MOV AX, BX
(b) MOV AX, 5500H
(c) MOV [1234H], AX
(d) MOV AX, [SI]
(e) MOV AX, [BP+6]
(f) MOV AX, TABLE[BX+DI]
```

**Solution**:

| Instruction | Mode | Reason |
|---|---|---|
| (a) `MOV AX, BX` | Register | Operand is in register BX |
| (b) `MOV AX, 5500H` | Immediate | 5500H is a constant value embedded in instruction |
| (c) `MOV [1234H], AX` | Direct | Memory address 1234H specified as constant |
| (d) `MOV AX, [SI]` | Register Indirect | EA = content of SI register |
| (e) `MOV AX, [BP+6]` | Based | EA = BP + displacement 6; uses SS segment |
| (f) `MOV AX, TABLE[BX+DI]` | Based Indexed with Displacement | EA = TABLE_offset + BX + DI |

---

### Example 3: Array Access Program [KTU Part B analytical]

**Problem**: Write an 8086 assembly language program to find the largest element in an array of 10 unsigned bytes starting at memory location 2000H in DS.

**Solution**:

```asm
.MODEL SMALL
.DATA
    ARRAY   DB  45H, 23H, 7FH, 10H, 93H, 11H, 55H, 02H, 88H, 3CH

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV SI, OFFSET ARRAY   ; SI = base address of ARRAY (Indexed mode)
    MOV AL, [SI]           ; Register Indirect: AL = ARRAY[0] (initial max)
    MOV CX, 9              ; Immediate: CX = loop count (9 comparisons)
    INC SI                 ; Move to ARRAY[1]
    
FIND_MAX:
    CMP AL, [SI]           ; Register Indirect: compare current max with ARRAY[i]
    JAE SKIP               ; If AL >= [SI], skip update (unsigned: JAE)
    MOV AL, [SI]           ; Register Indirect: new max found, update AL
SKIP:
    INC SI                 ; Advance pointer
    LOOP FIND_MAX          ; Decrement CX, loop until CX=0
    
    ; AL now holds the maximum value = 93H
    ; In a real program: MOV MAX_RESULT, AL (Direct addressing to store result)
    
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN
```

**Trace (first 3 iterations)**:
- Init: AL=45H, SI points to ARRAY[1]=23H
- Iter 1: 45H vs 23H → 45H > 23H → no update. SI→ARRAY[2]
- Iter 2: 45H vs 7FH → 45H < 7FH → AL=7FH. SI→ARRAY[3]
- Iter 3: 7FH vs 10H → no update.
- ... continues ... Final: AL = 93H ✓

---

## 5. Previous Year Questions & Solutions

---

### Q1 [KTU All papers — Part A, 3 marks]
**Question**: Explain any 3 addressing modes of the 8086 with examples.

**Solution**:

**1. Register Addressing Mode**:
Both operands (source and destination) are CPU registers. No external memory access needed.
- Syntax: `MOV destination_reg, source_reg`
- Example: `MOV AX, BX` — copies 16-bit content of BX into AX.
- EA calculation: Not applicable (register, not memory).
- Execution speed: 2 clock cycles (fastest non-immediate).

**2. Direct Addressing Mode**:
The 16-bit effective address of the memory operand is specified as a constant in the instruction. Default segment is DS.
- Syntax: `MOV destination, [address_constant]`
- Example: `MOV AX, [0500H]` — reads 16-bit word from DS:0500H into AX.
- PA = DS × 16 + 0500H.
- Useful for: global variables at fixed known addresses.

**3. Register Indirect Addressing Mode**:
The effective address is the current 16-bit value in a base or index register (BX, BP, SI, or DI).
- Syntax: `MOV destination, [register]`
- Example: `MOV AX, [BX]` — if BX = 2000H, reads from DS:2000H.
- Moving a pointer: `INC BX; MOV AX, [BX]` — walks through memory sequentially.
- Useful for: linked list traversal, pointer-based data access.

---

### Q2 [KTU June 2022 / Dec 2018 — Part B, 9 marks]
**Question**: Explain all addressing modes of the 8086 with examples. How does based indexed addressing support 2D array access?

**Solution**:

**All 7 addressing modes are explained in Section 1 above.**

**2D Array Access via Based Indexed Addressing:**

Consider a 2D array `int MATRIX[3][4]` stored in memory, with each element being a 16-bit word (2 bytes).
- Base address (DS offset) of MATRIX = 1000H
- Row size = 4 elements × 2 bytes = 8 bytes
- To access `MATRIX[i][j]`:
  $$\text{EA} = 1000H + i \times 8 + j \times 2$$

In 8086 assembly:
```asm
; Access MATRIX[2][3]:
MOV BX, 2 * 8    ; BX = row offset = 2 × 8 = 16D = 0010H
MOV SI, 3 * 2    ; SI = column offset = 3 × 2 = 6D = 0006H
MOV AX, MATRIX[BX+SI]  ; EA = 1000H + 10H + 06H = 1016H
                        ; Reads MATRIX[2][3]
```

This is the **canonical use case** for Based Indexed addressing — the base register provides the row offset and the index register provides the column offset, together allowing arbitrary 2D array element access in a single instruction.

---

### Q3 [KTU May 2019 / Jan 2023 — Part B, 9 marks]
**Question**: Write an 8086 assembly language program to sort an array of 10 numbers in ascending order using bubble sort.

**Solution**:

```asm
.MODEL SMALL
.DATA
    ARRAY   DW  45H, 10H, 93H, 23H, 7FH, 11H, 55H, 88H, 02H, 3CH
    COUNT   EQU 10

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV CX, COUNT - 1    ; Outer loop: N-1 passes
    
OUTER_LOOP:
    PUSH CX              ; Save outer loop count on stack
    MOV SI, OFFSET ARRAY ; SI points to start of array
    MOV CX, COUNT - 1    ; Inner loop: N-1 comparisons

INNER_LOOP:
    MOV AX, [SI]         ; Register Indirect: AX = ARRAY[i]
    CMP AX, [SI+2]       ; Based: compare with ARRAY[i+1]
    JBE NO_SWAP          ; If ARRAY[i] <= ARRAY[i+1], no swap needed (unsigned)
    
    ; Swap ARRAY[i] and ARRAY[i+1]:
    MOV BX, [SI+2]       ; BX = ARRAY[i+1]
    MOV [SI], BX         ; ARRAY[i] = old ARRAY[i+1]
    MOV [SI+2], AX       ; ARRAY[i+1] = old ARRAY[i]
    
NO_SWAP:
    ADD SI, 2            ; Advance to next word element
    LOOP INNER_LOOP      ; Decrement CX and continue inner loop
    
    POP CX               ; Restore outer loop count
    LOOP OUTER_LOOP      ; Next pass
    
    MOV AH, 4CH
    INT 21H              ; Exit to DOS
MAIN ENDP
END MAIN
```

**Algorithm explanation**:
- **Outer loop**: N-1 passes guaranteed to fully sort N elements (worst case).
- **Inner loop**: Each pass compares adjacent pairs and swaps if out of order. After pass k, the k-th largest element is in its final position at the end.
- **Addressing modes used**: Register Indirect `[SI]`, Based `[SI+2]`, Register, Immediate.
- **Result**: After 9 passes, ARRAY = {02H, 10H, 11H, 23H, 3CH, 45H, 55H, 7FH, 88H, 93H}.

