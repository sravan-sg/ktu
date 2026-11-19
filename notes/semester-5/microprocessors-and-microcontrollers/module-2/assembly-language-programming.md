# Assembly Language Programming: Subroutines, Macros, Parameter Passing & Stack

## 1. Explanation

Modular assembly programming structures software into reusable, maintainable, and readable components. In x86 assembly, modularity is achieved through two distinct constructs: **Subroutines (Procedures)** and **Macros**.

---

### Procedures vs. Macros: Comparative Architectural Analysis

| Dimension | Subroutine / Procedure (`PROC`) | Macro (`MACRO`) |
|---|---|---|
| **Mechanism** | Subroutine code exists **once** in memory. Invoked at runtime via `CALL` and `RET` instructions. | Source code block is **textually expanded inline** by the assembler at each point of invocation. |
| **Memory Footprint** | Extremely compact. Reuses single copy of code regardless of invocation frequency. | High memory footprint. Duplicates code bytes at every macro call. |
| **Execution Speed** | Slower. Incurs hardware overhead: pushing/popping IP/CS to/from stack and branch latency. | Faster. Zero call/return overhead; executes straight-line instructions inline. |
| **Parameter Passing** | Runtime: passed via registers, stack frames, or memory pointers. | Assembly time: macro parameters are literally substituted as text during assembly. |
| **Scope of Directives** | Delimited by `PROC` and `ENDP`. | Delimited by `MACRO` and `ENDM`. |

---

### Subroutine Mechanics: `CALL` and `RET`

#### 1. Procedure Types: NEAR vs. FAR
- **NEAR Procedure (`PROC NEAR`)**:
  - The procedure resides in the **same code segment** as the calling code (`CS` remains unchanged).
  - `CALL`: Pushes only the $16\text{-bit}$ return offset (`IP`) onto the stack. `SP ← SP - 2`.
  - `RET`: Pops $16\text{-bit}$ return address from stack into `IP`. `SP ← SP + 2`.
- **FAR Procedure (`PROC FAR`)**:
  - The procedure resides in a **different code segment**.
  - `CALL`: Pushes `CS` first, then `IP` onto the stack. `SP ← SP - 4`.
  - `RET`: Pops `IP` first, then `CS` from the stack. `SP ← SP + 4`.

#### 2. The Stack Frame & Base Pointer (`BP`)
When subroutines are nested or functions require local variables and parameters, a standardized **stack frame** is constructed using `BP`:

```
               HIGH MEMORY (Stack Bottom)
             ┌─────────────────────────────┐
             │ Parameter 2 (e.g., [BP+6])  │
             ├─────────────────────────────┤
             │ Parameter 1 (e.g., [BP+4])  │
             ├─────────────────────────────┤
             │ Return Address (IP)         │
             ├─────────────────────────────┤
    BP ────► │ Saved Caller BP             │  ◄── PUSH BP / MOV BP, SP
             ├─────────────────────────────┤
             │ Local Variable 1 ([BP-2])   │  ◄── SUB SP, 4
             ├─────────────────────────────┤
    SP ────► │ Local Variable 2 ([BP-4])   │
             └─────────────────────────────┘
               LOW MEMORY (Stack Top)
```

**Standard Function Prologue**:
```asm
PUSH BP          ; Save old base pointer
MOV  BP, SP      ; Establish new stack frame base
SUB  SP, 4       ; Allocate 4 bytes for local variables
```

**Standard Function Epilogue**:
```asm
MOV  SP, BP      ; Deallocate local variables
POP  BP          ; Restore caller's base pointer
RET  4           ; Return and remove 4 bytes of parameters from stack
```

---

### Parameter Passing Mechanisms

There are three primary methods for passing parameters between calling code and procedures:

1. **Passing in General Purpose Registers**:
   - Fastest method. Parameters placed directly in `AX`, `BX`, `CX`, `DX`, `SI`, `DI`.
   - *Limitation*: Limited number of CPU registers; registers must be preserved if caller needs them.
2. **Passing via Memory Tables / Global Pointers**:
   - Parameters placed in a contiguous data block; memory offset loaded into `BX` or `SI`.
3. **Passing on the Stack (C-Calling Convention / Standard Pascal)**:
   - Caller pushes arguments onto the stack before `CALL`.
   - Callee reads arguments using based addressing `[BP + offset]`.
   - Highly flexible; supports recursive functions and arbitrary numbers of arguments.

---

### Macro Definition & Expansion

A macro is declared using the `MACRO` and `ENDM` directives:

```asm
DISPLAY_CHAR MACRO CHAR_VAL
    MOV AH, 02H
    MOV DL, CHAR_VAL
    INT 21H
ENDM
```

When the assembler encounters:
```asm
DISPLAY_CHAR 'A'
DISPLAY_CHAR 'B'
```
It replaces each line directly with the 3 machine instructions during pass 1 of assembly.

---

## 2. Example: Complete Modular Program with Stack Parameter Passing

```asm
DATA SEGMENT
    A       DW  0010H
    B       DW  0020H
    RESULT  DW  ?
DATA ENDS

STACK SEGMENT STACK
    DW  64 DUP(?)
STACK ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA, SS:STACK
START:
    MOV AX, DATA
    MOV DS, AX
    
    ; Pass parameters via Stack
    PUSH A              ; Push first argument ([BP+6])
    PUSH B              ; Push second argument ([BP+4])
    CALL ADD_NUMS       ; Call near procedure
    MOV RESULT, AX      ; Return value in AX
    
    MOV AH, 4CH
    INT 21H

; Subroutine: ADD_NUMS (Near Procedure)
ADD_NUMS PROC NEAR
    PUSH BP             ; Save caller BP
    MOV  BP, SP         ; Set up stack frame
    
    MOV  AX, [BP + 6]   ; Read Parameter A
    ADD  AX, [BP + 4]   ; Add Parameter B
    
    POP  BP             ; Restore caller BP
    RET  4              ; Return and pop 4 bytes of parameters
ADD_NUMS ENDP

CODE ENDS
END START
```

---

## 3. Applications & Use Cases

1. **C Compiler Code Generation**: C and C++ compilers implement function calls via the cdecl or stdcall calling conventions, establishing stack frames via `EBP/RBP` as described above.
2. **Real-Time Operating System (RTOS) Context Switching**: An RTOS saves the entire task context (all general registers, segment registers, and flags) onto the task's private stack frame during a timer interrupt tick.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Recursive Factorial Stack Trace [Analytical]
**Problem**:
Trace the stack contents during the execution of a recursive procedure computing $3!$ ($N=3$).

**Solution**:
1. Main pushes $N=3$, executes `CALL FACT`:
   - Stack contains: `[Param: 3]`, `[Return IP]`
2. Iteration 1 (`FACT` for $N=3$):
   - Pushes $N-1 = 2$, executes `CALL FACT`:
   - Stack: `[3], [Ret1], [2], [Ret2]`
3. Iteration 2 (`FACT` for $N=2$):
   - Pushes $N-1 = 1$, executes `CALL FACT`:
   - Stack: `[3], [Ret1], [2], [Ret2], [1], [Ret3]`
4. Base Case ($N=1$):
   - Returns $AX = 1$, unwinds stack, multiplies:
     $AX = 1 \times 2 = 2 \implies AX = 2 \times 3 = 6$.
   - Final return to main: $AX = 6$.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [KTU All Papers — 9 Marks]
**Question**:
Differentiate between macros and subroutines in the 8086. Explain parameter passing through the stack with an example.

**Solution**:

#### Part (a): Macros vs. Subroutines
- **Macros** are expanded textually inline at compile time; they have zero runtime call/return overhead but consume extra memory if invoked frequently.
- **Subroutines** are compiled once into memory and jumped to via `CALL` at runtime, saving memory at the cost of `CALL`/`RET` stack execution cycles.

*(Refer to detailed comparison table in Section 1).*

#### Part (b): Parameter Passing Through Stack
When passing parameters via the stack:
1. The calling program pushes arguments onto the stack using `PUSH`:
   ```asm
   PUSH ARG1
   PUSH ARG2
   CALL MYSUB
   ```
2. The `CALL` instruction automatically pushes the return address (`IP`) onto the stack.
3. Inside the procedure, the stack frame is initialized:
   ```asm
   PUSH BP
   MOV BP, SP
   ```
4. Parameters are accessed relative to `BP`:
   - `[BP + 4]` accesses `ARG2` (last pushed).
   - `[BP + 6]` accesses `ARG1` (first pushed).
5. Before returning, `POP BP` restores the caller's frame, and `RET 4` cleans up the parameters from the stack.

