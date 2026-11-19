# 8259 Programmable Interrupt Controller (PIC)

> **Senior CS Professor Notes** | Semester 5 — CS305 Microprocessors & Microcontrollers | Module III

---

## 1. Explanation

### Why an External Interrupt Controller is Essential
The Intel 8086 microprocessor has only two hardware interrupt pins:
1. **NMI (Non-Maskable Interrupt)**: Edge-triggered, non-maskable, hardwired to vector Type 2 (reserved for catastrophic system events like power failure or bus parity error).
2. **INTR (Interrupt Request)**: Level-triggered, maskable via the Interrupt Flag (`IF`), which enters the CPU via a single pin.

In complex embedded and computing systems (such as the original IBM PC/XT/AT architectures, avionics, and factory automated test benches), dozens of peripheral devices—keyboards, serial ports, timer channels, disk controllers, ADC modules—demand immediate CPU attention. If multiple peripherals were tied directly to the single `INTR` line using open-collector wired-OR logic:
- The CPU would have no hardware mechanism to prioritize which device to serve first.
- The CPU would have to execute a polling loop over all peripheral status registers via I/O reads, incurring massive latency ($O(N)$ overhead where $N$ is the number of peripherals).
- Polling wastes CPU cycles and cannot meet hard real-time deadlines.

The **Intel 8259A Programmable Interrupt Controller (PIC)** solves this fundamental bottleneck. It acts as an intelligent hardware arbitrator between 8 external interrupt request lines ($\text{IR}_0$ to $\text{IR}_7$) and the single `INTR` input of the 8086 CPU. By cascading 8259 devices in a Master-Slave hierarchy, a single CPU can manage up to **64 vectored priority interrupt levels** using only 9 chips (1 Master + 8 Slaves).

---

### Internal Architecture of the 8259A

The internal architecture of the 8259A consists of eight primary functional blocks:

```
                  +-------------------------------------------+
                  |         8259A Internal Architecture       |
                  +-------------------------------------------+
                                        |
  +---------------+   +-----------------+-----------------+   +------------------+
  |  Data Bus     |<->| Interrupt Request Register (IRR)  |<--| IR0 - IR7        |
  |  Buffer       |   | (Latches incoming raw requests)   |   | (Interrupt Pins) |
  |  (D0 - D7)    |   +-----------------------------------+   +------------------+
  +---------------+                     |
          |           +-----------------+-----------------+
          |           |        Priority Resolver          |
          |           | (Determines highest priority bit) |
          |           +-----------------------------------+
          |                             |
  +---------------+   +-----------------+-----------------+
  |  Control      |   |   In-Service Register (ISR)       |
  |  Logic        |   | (Stores request currently served) |
  |  (RD#, WR#,   |   +-----------------------------------+
  |   CS#, A0)    |                     |
  +---------------+   +-----------------+-----------------+
          |           | Interrupt Mask Register (IMR)     |
          |           | (Masks individual IR lines, 1=off)|
          |           +-----------------------------------+
          |                             |
  +---------------+   +-----------------+-----------------+   +------------------+
  | Cascade       |<->|    Read/Write Logic & Control     |-->| INT (to 8086 INTR)|
  | Buffer /      |   |    (Processes ICWs and OCWs)      |<--| INTA# (from CPU) |
  | Comparator    |   +-----------------------------------+   +------------------+
  | (CAS0 - CAS2, |
  |  SP#/EN#)     |
  +---------------+
```

#### Detailed Functional Blocks:

1. **Interrupt Request Register (IRR)**:
   - An 8-bit register that stores the asynchronous interrupt requests arriving on pins $\text{IR}_0$ through $\text{IR}_7$.
   - Bit $i$ is set to 1 when a valid request is detected on line $\text{IR}_i$.
   - Depending on programming (ICW1), inputs can be configured as **level-sensitive** (high level) or **edge-triggered** (low-to-high transition).

2. **In-Service Register (ISR)**:
   - An 8-bit register that tracks which interrupt level is currently being serviced by the 8086 CPU.
   - When the CPU acknowledges an interrupt via the $\overline{\text{INTA}}$ handshake, the highest-priority bit in the IRR is cleared, and the corresponding bit in the ISR is set to 1.
   - This bit remains 1 until an **End of Interrupt (EOI)** command is issued (either automatically via AEOI mode or explicitly by software at the end of the ISR routine via OCW2).

3. **Interrupt Mask Register (IMR)**:
   - An 8-bit register operated through software (via OCW1).
   - Writing a `1` to bit $M_i$ selectively **masks** (disables) interrupt input $\text{IR}_i$ without affecting other inputs.
   - Writing a `0` unmasks line $\text{IR}_i$.
   - Masking an interrupt prevents it from passing through to the Priority Resolver; however, the state of the physical pin can still be read by interrogating the IRR.

4. **Priority Resolver (PR)**:
   - Combinational logic block that compares the unmasked bits in the IRR ($\text{IRR} \land \neg \text{IMR}$) against the bits currently active in the ISR.
   - It determines whether an incoming request has higher priority than the routine currently being executed by the CPU. If so, it asserts the `INT` output pin to interrupt the CPU.

5. **Read/Write and Control Logic**:
   - Manages communication with the 8086 host processor across the system bus.
   - Decodes control signals: $\overline{\text{RD}}$, $\overline{\text{WR}}$, $\overline{\text{CS}}$, and address line $A_0$.
   - Decodes and routes **Initialization Command Words (ICW1–ICW4)** and **Operational Command Words (OCW1–OCW3)**.

6. **Data Bus Buffer**:
   - Tri-state, bidirectional 8-bit buffer interfacing internal 8259 registers to the system data bus ($D_0 - D_7$).
   - Transmits control words, status register contents (IRR, ISR, IMR), and the 8-bit **Interrupt Vector Type Byte** to the CPU during the second $\overline{\text{INTA}}$ cycle.

7. **Cascade Buffer / Comparator**:
   - Handles multi-8259 cascading.
   - In a Master 8259, lines $\text{CAS}_0, \text{CAS}_1, \text{CAS}_2$ act as outputs broadcasting the 3-bit binary ID of the slave device currently being serviced.
   - In a Slave 8259, $\text{CAS}_0 - \text{CAS}_2$ act as inputs; the slave compares the incoming ID with its hardwired address programmed during initialization (ICW3).
   - $\overline{\text{SP}}/\overline{\text{EN}}$: Slave Program / Enable Buffer pin. Tied to $V_{CC}$ for Master mode, tied to GND for Slave mode (in non-buffered mode), or used to control transceiver buffers in buffered mode.

---

### The 8086-8259 Handshake Protocol (Two INTA Cycles)

The interaction between the 8086 CPU and the 8259A during an interrupt is governed by a precise two-cycle bus protocol:

```
CLK (8086)   ___|---|___|---|___|---|___|---|___|---|___|---|___|---|___|---|___
INTR (8259)  __________/-------------------------------------------------------
INTA# (Pulse 1) _______/-----------\_______________________/-----------\_______
                        ^ Cycle 1 (Freeze IRR/Set ISR)      ^ Cycle 2 (Put Vector on D0-D7)
Data Bus (D0-D7) -----------------High-Z-------------------<=== Type Byte N ===>
```

1. **Assertion of INTR**: An unmasked peripheral asserts $\text{IR}_i$. If $\text{IR}_i$ has higher priority than any active bit in the ISR, the 8259 asserts its `INT` output pin, driving the 8086 `INTR` pin HIGH.
2. **CPU Acknowledgment**: If the 8086 Interrupt Flag is set ($\text{IF}=1$), the 8086 finishes executing its current instruction and issues the **first** negative-going pulse on $\overline{\text{INTA}}$.
3. **Cycle 1 Actions**:
   - On the leading edge of the first $\overline{\text{INTA}}$ pulse, the 8259 freezes the state of the IRR and resolves priority.
   - The highest priority bit in the IRR is reset, and the corresponding bit in the ISR is set.
   - The 8259 data bus buffer remains in the high-impedance (floating) state.
   - If the active interrupt belongs to a cascaded Slave, the Master outputs the 3-bit slave address onto $\text{CAS}_0 - \text{CAS}_2$.
4. **Cycle 2 Actions**:
   - The 8086 CPU issues a **second** negative-going pulse on $\overline{\text{INTA}}$.
   - In response, the active 8259 (Master, or selected Slave) places an 8-bit **Interrupt Vector Type Byte** ($N$) onto the data bus ($D_0 - D_7$).
5. **CPU Vector Processing**:
   - The 8086 reads $N$ from the bus.
   - It multiplies $N$ by 4 to locate the vector table entry at address $00000H + 4N$.
   - It pushes the Flag Register, clears `IF` and `TF`, pushes `CS`, pushes `IP`, and loads the new `CS:IP` from the vector table.

---

### Command Word Architecture

The 8259A operation is governed by two sets of control words:
1. **Initialization Command Words (ICW1 through ICW4)**: Programmed once upon system reset to establish base addresses, cascading modes, and CPU architecture.
2. **Operational Command Words (OCW1 through OCW3)**: Issued dynamically during runtime to change masks, send EOI commands, and read internal status.

#### Initialization Command Words (ICWs)

The initialization sequence follows a strict hardware state machine:

```
Reset / Power-On
      |
      v
Write ICW1 (A0 = 0, D4 = 1)
      |
      v
Write ICW2 (A0 = 1)   --> Sets Vector Base Address (T7 - T3)
      |
      v
Is SNGL = 0 (Cascaded)?
   /        \
 (Yes)      (No)
  /            \
Write ICW3     |
(A0 = 1)       |
  \            /
   \          /
    v        v
Is IC4 = 1?
   /        \
 (Yes)      (No)
  /            \
Write ICW4     |
(A0 = 1)       |
  \            /
   \          /
    v        v
Initialization Complete (Ready for OCWs)
```

1. **ICW1 ($A_0 = 0, D_4 = 1$)**:
   - $D_0$ (**IC4**): $1 = \text{ICW4 required}$; $0 = \text{ICW4 not required}$. (Always 1 for 8086).
   - $D_1$ (**SNGL**): $1 = \text{Single 8259}$; $0 = \text{Cascade mode}$ (requires ICW3).
   - $D_2$ (**ADI**): Address interval ($1 = 4$ bytes, $0 = 8$ bytes; used only for MCS-80/85).
   - $D_3$ (**LTIM**): $1 = \text{Level-triggered inputs}$; $0 = \text{Edge-triggered}$ (low-to-high transition).
   - $D_4$: Must be `1` (identifies the byte as ICW1).
   - $D_5 - D_7$: Interrupt vector address for MCS-80/85 mode (don't care for 8086).

2. **ICW2 ($A_0 = 1$)**:
   - Sets the base vector type number for the 8 inputs ($\text{IR}_0 - \text{IR}_7$).
   - For 8086: Bits $D_7 - D_3$ provide the upper 5 bits ($T_7 - T_3$) of the vector type.
   - The 8259 automatically inserts the 3-bit binary value ($000_2$ to $111_2$) corresponding to $\text{IR}_0 - \text{IR}_7$ into bits $D_2 - D_0$.
   - *Example*: If ICW2 is written with `08H` (`0000 1000B`), $\text{IR}_0$ generates type `08H`, $\text{IR}_1$ generates `09H`, ..., $\text{IR}_7$ generates `0FH`.
   - *Example*: In PC-AT, Master ICW2 is `08H` (Types `08H–0FH`), Slave ICW2 is `70H` (Types `70H–77H`).

3. **ICW3 ($A_0 = 1$, required only if $\text{SNGL}=0$)**:
   - **For Master 8259**: Each bit $S_7 - S_0$ represents whether an $\text{IR}$ pin is connected to a Slave.
     - Bit $S_i = 1 \implies \text{Slave is connected to } \text{IR}_i$.
     - Bit $S_i = 0 \implies \text{Normal peripheral connected to } \text{IR}_i$.
     - *Example*: If Slaves are attached to $\text{IR}_2$ and $\text{IR}_4$, Master ICW3 = `0001 0100B` = `14H`.
   - **For Slave 8259**: Bits $D_2 - D_0$ store the 3-bit Slave ID ($000_2$ to $111_2$) identifying which Master $\text{IR}$ line feeds this slave. Bits $D_7 - D_3$ must be `00000`.
     - *Example*: If Slave is connected to Master $\text{IR}_2$, Slave ICW3 = `0000 0010B` = `02H`.

4. **ICW4 ($A_0 = 1$, required if $\text{IC4}=1$ in ICW1)**:
   - $D_0$ ($\mu\text{PM}$): Microprocessor mode. $1 = \text{8086/8088 mode}$; $0 = \text{MCS-80/85 mode}$.
   - $D_1$ (**AEOI**): Automatic End of Interrupt. $1 = \text{AEOI enabled}$; $0 = \text{Normal EOI (software must issue OCW2)}$.
   - $D_2$ (**M/S**): Master/Slave selection when in buffered mode ($1 = \text{Master}$, $0 = \text{Slave}$). Ignored if non-buffered.
   - $D_3$ (**BUF**): Buffered mode. $1 = \text{Buffered mode enabled}$; $0 = \text{Non-buffered mode}$.
   - $D_4$ (**SFNM**): Special Fully Nested Mode. $1 = \text{SFNM enabled}$ (used in Master when cascading); $0 = \text{Disabled}$.
   - $D_7 - D_5$: Must be `000`.

---

#### Operational Command Words (OCWs)

Once initialized, the 8259 is controlled dynamically via OCW1, OCW2, and OCW3:

1. **OCW1 ($A_0 = 1$)**:
   - Directly reads or writes the **Interrupt Mask Register (IMR)**.
   - Bits $M_7 - M_0$: A `1` masks (disables) the corresponding $\text{IR}_i$ channel; a `0` enables it.

2. **OCW2 ($A_0 = 0, D_4=0, D_3=0$)**:
   - Controls End of Interrupt (EOI) and priority rotation commands.
   - Bits:
     - $D_7$ (**R**): Rotate priority.
     - $D_6$ (**SL**): Specific level select.
     - $D_5$ (**EOI**): End of interrupt command.
     - $D_2 - D_0$ ($L_2 - L_0$): Specific interrupt level (0 to 7) to be acted upon when $\text{SL}=1$.

| Command Description | R | SL | EOI | Hex Code ($L_2 L_1 L_0 = 000$) |
|---|---|---|---|---|
| **Non-Specific EOI** (Clears highest active ISR bit) | 0 | 0 | 1 | `20H` |
| **Specific EOI** (Clears ISR bit specified by $L_2 L_1 L_0$) | 0 | 1 | 1 | `60H` + Level |
| **Rotate on Non-Specific EOI** | 1 | 0 | 1 | `A0H` |
| **Rotate in Automatic EOI Mode (Set)** | 1 | 0 | 0 | `80H` |
| **Rotate in Automatic EOI Mode (Clear)** | 0 | 0 | 0 | `00H` |
| **Rotate on Specific EOI** | 1 | 1 | 1 | `E0H` + Level |
| **Set Priority Command** (Lowest priority set to $L_2 L_1 L_0$) | 1 | 1 | 0 | `C0H` + Level |
| **No Operation** | 0 | 1 | 0 | `40H` |

3. **OCW3 ($A_0 = 0, D_4=0, D_3=1$)**:
   - Used for Special Mask Mode and Polling, and to select whether the IRR or ISR register is read during CPU input cycles at $A_0 = 0$.
   - $D_7$: Reserved (0).
   - $D_6 - D_5$ (**ESMM, SMM**): Enable/Disable Special Mask Mode.
   - $D_2$ (**RR**): Read Register command.
   - $D_1$ (**RIS**): $1 = \text{Read ISR on next read}$; $0 = \text{Read IRR on next read}$.
   - $D_0$: Reserved (0).
   - $D_4=0, D_3=1$: Identifies the byte as OCW3.

---

### Priority Modes of Operation

1. **Fully Nested Mode (Default)**:
   - Priority is fixed: $\text{IR}_0$ has the highest priority; $\text{IR}_7$ has the lowest.
   - When an interrupt is acknowledged, all lower-priority interrupts are automatically inhibited from interrupting the CPU until the current ISR finishes and issues an EOI.
   - Higher-priority interrupts can still interrupt the current service routine (if CPU `IF` is set via `STI`).

2. **Special Fully Nested Mode (SFNM)**:
   - Configured via ICW4 ($D_4=1$) in the Master 8259 of a cascaded system.
   - Allows a Slave 8259 to service an even higher-priority interrupt on its own inputs while one of its interrupts is already in service on the Master.
   - Without SFNM, the Master's ISR bit locks out all further requests from that entire Slave chip!

3. **Rotating Priority (Equal Priority) Mode**:
   - Used when several devices have equal urgency (e.g., identical DMA channels or communication buffers).
   - **Rotate on Non-Specific EOI**: The device just serviced is assigned the *lowest* priority ($\text{IR}_k \to \text{lowest}$), and the device immediately following it ($\text{IR}_{(k+1) \pmod 8}$) becomes the *highest* priority.
   - **Rotate on Specific EOI**: Software explicitly dictates which channel becomes lowest priority.

4. **Special Mask Mode (SMM)**:
   - Configured via OCW3.
   - In standard mode, while an ISR bit is set, all interrupts at that level and below are locked out.
   - SMM allows software to dynamically mask a specific level (via OCW1) while simultaneously unmasking lower-priority lines, allowing selected lower-priority routines to run.

5. **Polled Mode**:
   - Configured via OCW3 ($D_2 = 1$).
   - The CPU disables hardware interrupts (`CLI`) and polls the 8259 by reading it with $A_0=0$.
   - The 8259 returns an 8-bit status byte: Bit $D_7 = 1$ indicates an interrupt is pending, and bits $D_2 - D_0$ contain the binary code of the highest-priority pending request.

---

## 2. Example: System Interconnection & Cascading Scheme

### Cascading 1 Master and 2 Slaves for 22 Interrupts

```
                      +-------------------+
                      |     8086 CPU      |
                      |                   |
                      | INTR         INTA#|
                      +--^-------------v--+
                         |             |
           +-------------+             +-----------------------+
           | INT                                               | INTA#
+-----------------------+                             +-----------------------+
|     MASTER 8259A      |                             |     MASTER 8259A      |
| IR0 (Timer)           |                             |                       |
| IR1 (Keyboard)        |                             | CAS0, CAS1, CAS2      |
| IR2 ------------------------------------------------+---|-----|-----|---------+
| IR3 (COM2)            |                             |   |     |     |         |
| IR4 ----------------------------------------------------+-----|-----|-----+   |
| IR5 (LPT2)            |                             |   |     |     |     |   |
| IR6 (Floppy Disk)     |                             |   |     |     |     |   |
| IR7 (LPT1)            |                             +---|-----|-----|-----+   |
+-----------------------+                                 |     |     |     |   |
                                                          |     |     |     |   |
         +------------------------------------------------+     |     |     |   |
         |         +--------------------------------------------+     |     |   |
         |         |         +----------------------------------------+     |   |
         |         |         |                                              |   |
+--------v---------v---------v--+                          +----------------v---v---v--+
|      SLAVE 1 (Addr = 2)       |                          |      SLAVE 2 (Addr = 4)   |
| CAS0    CAS1    CAS2    INTA# |                          | CAS0    CAS1    CAS2    INTA# |
| IR0 - IR7 (8 Serial Channels) |                          | IR0 - IR7 (8 Sensor Lines)|
| INT --------------------------+                          | INT ----------------------+
+-------------------------------+                          +---------------------------+
        (Feeds Master IR2)                                         (Feeds Master IR4)
```

#### Connection Details:
- **Master $\text{IR}_2$** is connected to **Slave 1's `INT` output**.
- **Master $\text{IR}_4$** is connected to **Slave 2's `INT` output**.
- $\text{CAS}_0, \text{CAS}_1, \text{CAS}_2$ lines of the Master are wired in parallel to $\text{CAS}_0, \text{CAS}_1, \text{CAS}_2$ of both Slave 1 and Slave 2.
- The 8086 $\overline{\text{INTA}}$ signal is broadcast in parallel to all three 8259 chips.
- Master $\overline{\text{SP}}/\overline{\text{EN}}$ is tied to $+5\text{V}$ (Master configuration).
- Slave $\overline{\text{SP}}/\overline{\text{EN}}$ pins are tied to $\text{GND}$ (Slave configuration).

---

## 3. Applications & Real-World Use Cases

1. **IBM PC/XT and PC/AT System Architecture**:
   - The seminal IBM PC/XT utilized a single 8259A to manage 8 system interrupts ($\text{IRQ}_0$ = System Timer 8253, $\text{IRQ}_1$ = Keyboard, $\text{IRQ}_6$ = Floppy Controller).
   - The IBM PC/AT introduced an 8259 cascading architecture where Slave PIC was attached to $\text{IRQ}_2$ of Master PIC, unlocking $\text{IRQ}_8 - \text{IRQ}_{15}$ (Real-Time Clock, IDE Hard Disk controller, PS/2 Mouse).
2. **Industrial Process Control & Automated Test Equipment (ATE)**:
   - Embedded automated packaging lines use 8259 controllers in **Rotating Priority Mode** to ensure equal-opportunity processing for multiple identical optical sorting sensors.
3. **Avionics & Hard Real-Time Telemetry**:
   - In fly-by-wire flight management computers, critical emergency warning sensors are tied to $\text{IR}_0$ under **Fully Nested Mode**, ensuring life-critical warnings instantly pre-empt routine navigation logging tasks.

---

## 4. Solved Numerical & Analytical Examples

### Example 1: Calculating Initialization Command Words for Master and Slave
**Problem**: An 8086-based system has a Master 8259 and two Slave 8259s.
- Slave 1 is connected to Master line $\text{IR}_3$.
- Slave 2 is connected to Master line $\text{IR}_7$.
- Master base interrupt type number is `40H`.
- Slave 1 base interrupt type number is `80H`.
- Slave 2 base interrupt type number is `90H`.
- The system uses: Edge-triggered inputs, Cascade mode, 8086 CPU mode, Normal EOI, Non-buffered mode, and Special Fully Nested Mode on the Master.

Determine the exact hexadecimal values of **ICW1, ICW2, ICW3, and ICW4** for:
1. The Master 8259.
2. Slave 1.

#### Solution:

**Part (A): Master 8259 Initialization Words**
1. **ICW1**:
   - $D_7 - D_5 = 000$ (Don't care in 8086).
   - $D_4 = 1$ (ICW1 signature bit).
   - $D_3 (\text{LTIM}) = 0$ (Edge-triggered).
   - $D_2 (\text{ADI}) = 0$ (Call address interval 8 bytes - don't care in 8086).
   - $D_1 (\text{SNGL}) = 0$ (Cascade mode, multiple 8259s).
   - $D_0 (\text{IC4}) = 1$ (ICW4 required for 8086).
   - Binary: `0001 0001B` = **`11H`**.

2. **ICW2**:
   - Base vector type is `40H` (`0100 0000B`).
   - Bits $D_7 - D_3 = 01000_2$. Bits $D_2 - D_0 = 000_2$.
   - Hex value = **`40H`**.

3. **ICW3**:
   - Master has slaves on $\text{IR}_3$ and $\text{IR}_7$.
   - Bit representation: $S_7 S_6 S_5 S_4 S_3 S_2 S_1 S_0 = 1000\ 1000B$.
   - Hex value = **`88H`**.

4. **ICW4**:
   - $D_7 - D_5 = 000$ (Reserved).
   - $D_4 (\text{SFNM}) = 1$ (Special Fully Nested Mode enabled for Master).
   - $D_3 (\text{BUF}) = 0$ (Non-buffered mode).
   - $D_2 (\text{M/S}) = 0$ (Ignored when non-buffered).
   - $D_1 (\text{AEOI}) = 0$ (Normal EOI).
   - $D_0 (\mu\text{PM}) = 1$ (8086 mode).
   - Binary: `0001 0001B` = **`11H`**.

---

**Part (B): Slave 1 Initialization Words**
1. **ICW1**:
   - Same fundamental mode as Master: Edge-triggered, Cascade mode, ICW4 needed.
   - Binary: `0001 0001B` = **`11H`**.

2. **ICW2**:
   - Base vector type is `80H` (`1000 0000B`).
   - Binary: `1000 0000B` = **`80H`**.

3. **ICW3**:
   - Slave 1 is connected to Master $\text{IR}_3$.
   - For a Slave, ICW3 format is: $D_7 - D_3 = 00000$, and bits $D_2 - D_0 = \text{Slave ID} = 3 = 011_2$.
   - Binary: `0000 0011B` = **`03H`**.

4. **ICW4**:
   - $D_4 (\text{SFNM}) = 0$ (SFNM is only enabled on Master, disabled on Slaves).
   - $D_3 (\text{BUF}) = 0$ (Non-buffered).
   - $D_2 (\text{M/S}) = 0$.
   - $D_1 (\text{AEOI}) = 0$ (Normal EOI).
   - $D_0 (\mu\text{PM}) = 1$ (8086 mode).
   - Binary: `0000 0001B` = **`01H`**.

---

### Example 2: Determining Physical IVT Addresses and Vector Offsets
**Problem**: In the system configured in Example 1:
1. When peripheral device connected to Slave 1's $\text{IR}_5$ line fires an interrupt, what is the Interrupt Vector Type Number generated?
2. What are the starting and ending physical memory addresses in the 8086 Interrupt Vector Table (IVT) where the corresponding ISR pointer is stored?
3. Show the exact byte mapping in IVT memory if the target ISR is located at physical segment address `7000H` and offset `0240H`.

#### Solution:
1. **Vector Type Calculation**:
   - Slave 1 base vector type = `80H`.
   - The input channel is $\text{IR}_5$.
   - Generated Type Number = $\text{Base} + \text{Channel Number} = 80\text{H} + 5 = \mathbf{85H}$ ($133_{10}$).

2. **IVT Address Calculation**:
   - In 8086 architecture, each interrupt type occupies 4 contiguous bytes in memory beginning at address:
     $$\text{Start Address} = \text{Type Number} \times 4 = 85\text{H} \times 4$$
     Converting to decimal: $133 \times 4 = 532_{10} = \mathbf{00214H}$.
   - The 4 bytes span:
     $$\mathbf{00214H \quad \text{to} \quad 00217H}$$

3. **Byte Storage Layout (Little-Endian Architecture)**:
   - Target Address: Segment = `7000H`, Offset = `0240H`.
   - The 8086 architecture stores the 16-bit Offset first (Low byte, then High byte), followed by the 16-bit Segment (Low byte, then High byte):

| Physical Address | Content | Register Field |
|---|---|---|
| `00214H` | `40H` | Offset Low Byte (`IP_L`) |
| `00215H` | `02H` | Offset High Byte (`IP_H`) |
| `00216H` | `00H` | Segment Low Byte (`CS_L`) |
| `00217H` | `70H` | Segment High Byte (`CS_H`) |

---

### Example 3: Decoding Operational Command Words (OCW1, OCW2, OCW3)
**Problem**: An 8259 has I/O base port address `20H` ($A_0 = 0$) and `21H` ($A_0 = 1$). An assembly sequence writes the following bytes:
```assembly
MOV AL, 0B8H
OUT 21H, AL

MOV AL, 63H
OUT 20H, AL

MOV AL, 0BH
OUT 20H, AL
IN  AL, 20H
```
Explain the exact hardware operation and system status resulting from each instruction.

#### Solution:

1. **`OUT 21H, AL` with `AL = 0B8H`**:
   - Address pin $A_0 = 1$ during runtime writes to **OCW1 (Interrupt Mask Register)**.
   - `0B8H` = `1011 1000B`.
   - Bit mapping ($M_7 \dots M_0$):
     - $M_7 = 1$ (IR7 masked/disabled)
     - $M_6 = 0$ (IR6 enabled)
     - $M_5 = 1$ (IR5 masked/disabled)
     - $M_4 = 1$ (IR4 masked/disabled)
     - $M_3 = 1$ (IR3 masked/disabled)
     - $M_2 = 0$ (IR2 enabled)
     - $M_1 = 0$ (IR1 enabled)
     - $M_0 = 0$ (IR0 enabled)
   - **Result**: Channels $\text{IR}_0, \text{IR}_1, \text{IR}_2$, and $\text{IR}_6$ are active and can interrupt the CPU. Channels $\text{IR}_3, \text{IR}_4, \text{IR}_5$, and $\text{IR}_7$ are completely inhibited.

2. **`OUT 20H, AL` with `AL = 63H`**:
   - Address pin $A_0 = 0$.
   - Byte `63H` = `0110 0011B`.
   - Bit analysis:
     - $D_4 D_3 = 00_2 \implies$ Decoded as **OCW2**.
     - $D_7 (\text{R}) = 0$ (No rotation).
     - $D_6 (\text{SL}) = 1$ (Specific level).
     - $D_5 (\text{EOI}) = 1$ (End of Interrupt command).
     - Bits $D_2 D_1 D_0 = 011_2 = 3$.
   - **Result**: Issues a **Specific EOI command for Interrupt Level 3 ($\text{IR}_3$)**, forcing bit 3 of the In-Service Register (ISR) to be cleared to `0`.

3. **`OUT 20H, AL` with `AL = 0BH` followed by `IN AL, 20H`**:
   - Address pin $A_0 = 0$.
   - Byte `0BH` = `0000 1011B`.
   - Bit analysis:
     - $D_4 D_3 = 01_2 \implies$ Decoded as **OCW3**.
     - $D_7 = 0$ (Reserved).
     - $D_6 D_5 = 00_2$ (Special Mask Mode disabled / no change).
     - $D_2 (\text{RR}) = 1$ (Enable Read Register).
     - $D_1 (\text{RIS}) = 1$ (Select In-Service Register ISR for reading; $0$ would select IRR).
     - $D_0 = 0$.
   - Next, `IN AL, 20H` reads the internal register at $A_0 = 0$.
   - **Result**: Reads the current contents of the **In-Service Register (ISR)** into register `AL`, enabling software to inspect which interrupt routines are currently executing.

---

## 5. Previous Year Questions & Solutions

### Question 1 (KTU B.Tech Examination)
**Draw the internal architecture of 8259 Programmable Interrupt Controller and explain the function of each block.** [9 Marks]

#### Complete Self-Contained Solution:
1. **Architecture Diagram**:
   *(Draw the 8-block functional block diagram showing Data Bus Buffer, Read/Write Logic, Cascade Buffer/Comparator, Control Logic, Interrupt Request Register (IRR), In-Service Register (ISR), Interrupt Mask Register (IMR), and Priority Resolver as detailed in Section 1).*
2. **Detailed Block Explanation**:
   - **Interrupt Request Register (IRR)**: An 8-bit register holding bits for all unserviced interrupt requests arriving at $\text{IR}_0 - \text{IR}_7$. Configurable via ICW1 as positive edge-triggered or active high level-sensitive.
   - **Interrupt Mask Register (IMR)**: An 8-bit register storing masking bits loaded via OCW1 ($A_0 = 1$). A `1` prevents the corresponding $\text{IR}$ line from generating an interrupt; a `0` allows normal operation.
   - **Priority Resolver (PR)**: Combinational logic that continuously evaluates unmasked bits from IRR and compares their priority against the highest bit set in the ISR. In default fully nested mode, priority is ranked $\text{IR}_0 > \text{IR}_1 > \dots > \text{IR}_7$. It signals the Control Logic to assert the `INT` pin if an unmasked request exceeds the current in-service priority.
   - **In-Service Register (ISR)**: An 8-bit register tracking which interrupt line is currently being serviced by the CPU. The bit is set on the second $\overline{\text{INTA}}$ pulse and cleared when an EOI command (OCW2) is received or automatically if AEOI is enabled.
   - **Data Bus Buffer**: An 8-bit bidirectional tri-state buffer interfacing internal registers to system data lines $D_0 - D_7$. Transmits the vector type byte to the CPU during the second $\overline{\text{INTA}}$ cycle and receives ICW/OCW control words.
   - **Read/Write and Control Logic**: Decodes $\overline{\text{RD}}, \overline{\text{WR}}, \overline{\text{CS}}$, and $A_0$ bus control lines to control internal data transfers. Asserts `INT` to the 8086 `INTR` pin and accepts two consecutive $\overline{\text{INTA}}$ acknowledge pulses from the 8086.
   - **Cascade Buffer/Comparator**: Generates (in Master mode) or evaluates (in Slave mode) the 3-bit cascade code on lines $\text{CAS}_0, \text{CAS}_1, \text{CAS}_2$ to coordinate multi-chip operation across up to 64 interrupt channels.

---

### Question 2 (KTU B.Tech Examination)
**Explain the sequence of command words written to initialize an 8259 PIC in an 8086 system. What is the difference between ICW and OCW?** [9 Marks]

#### Complete Self-Contained Solution:
1. **Distinction Between ICW and OCW**:
   - **Initialization Command Words (ICW1–ICW4)** are configured during system initialization/bootup immediately after power-on reset. They establish fixed hardware operating parameters (microprocessor type, single/cascade mode, call address interval, trigger type, and base vector address). Once programmed, they cannot be modified without issuing a full re-initialization sequence starting with ICW1.
   - **Operational Command Words (OCW1–OCW3)** are issued dynamically at any time during program execution to perform runtime management (altering interrupt mask bits in IMR via OCW1, sending End-of-Interrupt commands or changing priority modes via OCW2, and reading status registers IRR/ISR or entering polled mode via OCW3).

2. **Initialization Sequence (ICW1 to ICW4)**:
   - **Step 1: Write ICW1 ($A_0 = 0$)**:
     Writing a byte to port $A_0 = 0$ with bit $D_4 = 1$ resets the 8259 state machine and begins initialization. It sets:
     - $D_0 (\text{IC4}) = 1$ (Informs 8259 that ICW4 will follow; essential for 8086).
     - $D_1 (\text{SNGL}) = 0$ for Cascaded configuration, $1$ for Single PIC.
     - $D_3 (\text{LTIM}) = 0$ for edge-triggered inputs, $1$ for level-triggered inputs.
   - **Step 2: Write ICW2 ($A_0 = 1$)**:
     Defines the base interrupt vector number. Bits $D_7 - D_3$ provide the high-order bits ($T_7 - T_3$) of the 8-bit vector passed to the 8086 data bus. Bits $D_2 - D_0$ are automatically overwritten by the 8259 with the active channel number ($000_2$ to $111_2$).
   - **Step 3: Write ICW3 ($A_0 = 1$)** (Executed only if $\text{SNGL} = 0$):
     - For Master PIC: Sets an 8-bit mask where bit $S_k = 1$ indicates a slave PIC is wired to line $\text{IR}_k$.
     - For Slave PIC: Sets bits $D_2 - D_0$ to specify its 3-bit Slave ID ($000_2$ to $111_2$) matching the Master $\text{IR}$ line to which its `INT` pin is attached.
   - **Step 4: Write ICW4 ($A_0 = 1$)** (Executed only if $\text{IC4} = 1$ in ICW1):
     - $D_0 (\mu\text{PM}) = 1$ sets **8086/8088 mode** (instructs the 8259 to output an 8-bit vector on the second $\overline{\text{INTA}}$ pulse instead of MCS-85 3-byte `CALL` instructions).
     - $D_1 (\text{AEOI}) = 0$ for normal EOI via software, $1$ for automatic EOI.
     - $D_3 (\text{BUF}) = 1$ enables buffered mode with $D_2 (\text{M/S})$ selecting Master/Slave role.
     - $D_4 (\text{SFNM}) = 1$ enables Special Fully Nested Mode on Master PICs.

---

### Question 3 (KTU B.Tech Examination)
**Explain how cascading is implemented in 8259 to handle more than 8 interrupts. Draw the Master-Slave connection diagram.** [9 Marks]

#### Complete Self-Contained Solution:
1. **Cascading Principle**:
   - A single 8259 supports 8 interrupt lines. To handle up to 64 interrupts, 8259 controllers are cascaded in a tree structure comprising **1 Master 8259** and up to **8 Slave 8259s**.
   - Each Slave's `INT` pin is wired directly to one of the Master's $\text{IR}_0 - \text{IR}_7$ inputs.
   - The Master's 3-bit cascade bus ($\text{CAS}_0, \text{CAS}_1, \text{CAS}_2$) is connected in parallel to the $\text{CAS}_0, \text{CAS}_1, \text{CAS}_2$ inputs of all Slaves.
   - The 8086 $\overline{\text{INTA}}$ signal connects in parallel to the $\overline{\text{INTA}}$ pin of the Master and all Slaves.

2. **Step-by-Step Handshake during Cascaded Operation**:
   - **Step 1**: A peripheral asserts an $\text{IR}$ line on a Slave. The Slave asserts its `INT` pin, which in turn asserts an $\text{IR}_k$ pin on the Master.
   - **Step 2**: The Master resolves priority and asserts its `INT` output to the 8086 CPU `INTR` pin.
   - **Step 3**: The 8086 acknowledges by pulsing $\overline{\text{INTA}}$ low (Cycle 1). Both Master and Slaves receive this pulse.
   - **Step 4**: The Master recognizes that the active interrupt originates from a Slave on pin $\text{IR}_k$. The Master outputs the 3-bit binary code of $k$ onto the $\text{CAS}_0 - \text{CAS}_2$ lines. The Master's data bus remains tri-stated.
   - **Step 5**: All Slaves compare their internal ID (programmed via ICW3) with $\text{CAS}_0 - \text{CAS}_2$. The matching Slave enables its data bus buffer.
   - **Step 6**: The 8086 pulses $\overline{\text{INTA}}$ low for the second time (Cycle 2). The selected Slave places its 8-bit vector type byte on the data bus $D_0 - D_7$, which the 8086 reads to fetch the ISR address.
   - **Step 7 (EOI Handling)**: When the service routine finishes, software must send an End of Interrupt (EOI) command to **both** the Slave 8259 and the Master 8259 (to clear the in-service bits in both chips).

