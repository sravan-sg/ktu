# Module 2: 8086 Instruction Set & Assembly Programming — Revision Notes

## 1. Addressing Modes Summary
- **Immediate**: `MOV AX, 1234H` (Data embedded in opcode).
- **Register**: `MOV AX, BX` (Both operands in CPU registers).
- **Direct**: `MOV AX, [1000H]` ($\text{EA} = 1000\text{H}$; $\text{PA} = \text{DS} \times 16 + 1000\text{H}$).
- **Register Indirect**: `MOV AX, [BX]` ($\text{EA} = [\text{BX}]$).
- **Based**: `MOV AX, [BX + 4]` ($\text{EA} = [\text{BX}/\text{BP}] + \text{disp}$).
- **Indexed**: `MOV AX, ARRAY[SI]` ($\text{EA} = [\text{SI}/\text{DI}] + \text{disp}$).
- **Based Indexed**: `MOV AX, [BX + SI + 10H]` ($\text{EA} = [\text{BX}/\text{BP}] + [\text{SI}/\text{DI}] + \text{disp}$).

---

## 2. Key High-Yield Instructions
- **`XLAT`**: Table lookup: `AL ← [BX + AL]`.
- **`LEA reg, mem`**: Loads 16-bit offset address into register without memory dereference.
- **`DAA` / `DAS`**: Decimal adjust after addition/subtraction for packed BCD ($+06\text{H}$ or $+60\text{H}$).
- **`CBW` / `CWD`**: Sign extension (`AL` to `AX`; `AX` to `DX:AX`).
- **`REP` / `REPE` / `REPNE`**: String loop prefixes decrementing `CX`.

---

## 3. Procedures vs. Macros
- **Procedure (`PROC`)**: Single instance in memory; called at runtime via `CALL`/`RET`; saves memory, incurs stack/branch latency.
- **Macro (`MACRO`)**: Code textually expanded inline at assembly time; zero call latency, high code bloat.

---

## 4. Stack Frame with Base Pointer (`BP`)
- Function Prologue: `PUSH BP; MOV BP, SP; SUB SP, num_locals`.
- Access Parameters: `[BP + 4]`, `[BP + 6]`.
- Access Locals: `[BP - 2]`, `[BP - 4]`.
- Function Epilogue: `MOV SP, BP; POP BP; RET num_params`.

