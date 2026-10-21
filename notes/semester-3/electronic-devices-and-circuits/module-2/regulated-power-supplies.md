# Regulated Power Supplies

## 1. Explanation

### The Core Intuition: Why Do We Need Regulation?

An unregulated DC power supply (rectifier + filter) produces a voltage that **varies** with load current and AC line fluctuations. Consider what happens in a digital circuit or an op-amp when the supply voltage drops by 10% under load — the logic levels shift, gain changes, and noise margins collapse. **Regulation** is the art of maintaining a stable, fixed DC output regardless of load or supply variations.

The fundamental requirement is: maintain Vout = constant despite:
1. Changes in load current (IL varies from 0 to full load)
2. Changes in input AC supply voltage (±10% variation)
3. Temperature changes

**Two regulation strategies:**
- **Shunt regulator**: Wastes excess power in parallel with the load (less efficient, simpler)
- **Series regulator**: Controls a series pass element to drop just enough voltage (more efficient)

### Zener Voltage Regulator (Review)

The zener diode operates in its **reverse breakdown region**, maintaining a nearly constant voltage (VZ) across itself for a wide range of reverse current. The regulator exploits this property:

```
         Rs
Vin ─────┤├─────┬───── Vout = VZ
                │
               ─|← Zener (VZ)
                │
               GND
```

**Key equations:**
```
Rs = (Vin - VZ) / (IZ + IL)
IZ(min) = IZ(knee) [typically 5mA for small zeners]
IZ(max) = PZ(max) / VZ

For stable regulation: IZ(min) ≤ IZ ≤ IZ(max) for all IL conditions
```

**Limitation:** Zener alone has poor current capacity and poor regulation under heavy loads.

### Shunt Voltage Regulator (Transistor-Assisted)

A transistor is placed in **parallel (shunt) with the load**, controlled by the zener diode:

```
         Rs
Vin ─────┤├──────────┬──── Vout
                     │
                  [Load RL]
                     │
        ┌────────────┤Collector
        │         Q (NPN)
        │            │Emitter
       ─|← Zener     │
        │         ───┘
       GND
```

**Operation:**
- Zener sets the base voltage: VB = VZ
- Emitter (= Vout) = VZ − VBE ≈ VZ − 0.7V
- If Vout tries to rise: more base current → more IC → transistor conducts more → shunts more current → Vout drops back.
- Self-correcting feedback maintains Vout ≈ VZ − 0.7V

**Disadvantage:** Always dissipates power (transistor always conducting). Not efficient for high-current applications.

### Series Voltage Regulator

A transistor is placed in **series with the load** as a controllable resistance (emitter follower):

```
         VCC
          │
        [Q1 NPN] ← Series pass transistor
          │Emitter
          ├──────── Vout
          │
        [Load]
          │
         GND

Control circuit:
- Zener sets reference Vref
- Comparator (error amplifier) compares Vout with Vref
- Drives Q1 base to correct Vout
```

**Full Series Regulator Block Diagram:**

```
Vin ──── [Q1 pass transistor] ──── Vout
                │Base                │
         [Error amplifier]       [Voltage
                │                 divider R1/R2]
         [Reference: Zener Vref]      │
                                    [Load]
                                      │
                                     GND
```

**Feedback mechanism:**
```
Vout ↑ → Vsense ↑ → Error amp output ↓ → Q1 Base ↓ → Q1 less conductive → more VCE → Vout ↓
```

The loop continuously corrects Vout.

**Output voltage:** Set by voltage divider:
```
Vout = Vref × (1 + R1/R2)
```

### Current Limiting and Foldback Protection

Without current limiting, a short circuit (RL = 0) causes excessive current through Q1, destroying it.

**Simple Current Limiting:**
```
Add RSC (current sense resistor) in series with Vout:

Vin ─── [Q1] ─── RSC ─── Vout
                  │
              [Q2 NPN]
              Base ─── junction at RSC
```

When IL × RSC = 0.7V → Q2 turns ON → diverts Q1 base current → Q1 limits conduction.

The output current is limited to:
```
I_SC = VBE(Q2) / RSC ≈ 0.7 / RSC
```

**Foldback Current Limiting:** More advanced — as output voltage drops (during overload), the maximum current also decreases (foldback). This prevents sustained overload dissipation. Used in precision lab power supplies and battery chargers.

### 3-Pin Regulators (78XX and 79XX)

The 78XX series (positive) and 79XX series (negative) are **complete, integrated series regulators** in a single 3-pin package (Input, Output, Ground).

```
          1 (Input)
    Vin ──[  78XX  ]── Vout
         └──2 (GND)─┘
              │
             GND
```

**78XX series:** Positive voltages
- 7805: +5V, 7808: +8V, 7812: +12V, 7815: +15V
- Output current: up to 1A (with heatsink)
- Required: Cin ≥ 0.33μF, Cout ≥ 0.1μF for stability

**79XX series:** Negative voltages (same numbering: 7905 = -5V, 7912 = -12V)

**Internal structure of 78XX:**
- Bandgap reference (1.25V stable with temperature)
- Differential error amplifier
- Series pass transistor
- Thermal shutdown protection
- Short-circuit protection
- Safe operating area (SOA) protection

**Key specifications:**
```
Dropout voltage: Vin - Vout(min) ≈ 2-3V (LDO types can be <1V)
Load regulation: <0.1% typical
Line regulation: <0.01%/V
PSRR (Power Supply Rejection Ratio): ~60-70dB
```

### IC 723 Voltage Regulator

The LM723 is a **flexible, programmable linear voltage regulator IC** that can be configured for a wide range of output voltages (2V to 37V) and extended for high-current operation.

**Internal blocks:**
1. Stable voltage reference (Vref ≈ 7.15V)
2. Error amplifier (comparator)
3. Series pass transistor (NPN)
4. Current limiting transistor

**Pin description:**
- Vref: 7.15V reference output
- V+, V-: Error amplifier inputs (non-inverting, inverting)
- VCC, VEE: Supply pins
- VC: Collector of pass transistor (connect to Vin)
- Vout: Output
- CS, ILIM: Current sense pins

**Low Voltage Regulator (Vout < 7.15V):**
```
Vout = Vref × [R2 / (R1 + R2)]

For Vout = 5V with Vref = 7.15V:
R2/(R1+R2) = 5/7.15 = 0.699
If R2 = 3.48kΩ, R1 = 1.5kΩ (use voltage divider at V+ input)
```

**High Voltage Regulator (Vout > 7.15V):**
```
Vout = Vref × (1 + R1/R2)

For Vout = 12V:
12 = 7.15 × (1 + R1/R2)
R1/R2 = (12/7.15) - 1 = 0.678
If R2 = 7.5kΩ, R1 = 5kΩ
```

### SMPS (Switched-Mode Power Supply)

**Fundamental difference from linear regulators:** Instead of dissipating excess power as heat, an SMPS **switches** the input voltage on and off at high frequency (20kHz-1MHz), then uses an inductor/transformer to store energy and a rectifier/filter to produce the desired DC output.

**Basic SMPS block diagram:**
```
AC Mains → [Rectifier + Filter] → Vdc(raw) → [High-freq Switch] → [Transformer/Inductor] → [Rectifier] → [Filter] → Vout
                                                     ↑
                                              [Feedback/Control] ← [Vout sensing]
```

**Key advantages over linear:**
- Efficiency: 75-90% vs 30-50% for linear
- Can step down (buck), step up (boost), or invert (inverter)
- Small, lightweight (high-frequency transformer is tiny)

**Types:**
- **Buck (step-down):** Vout < Vin
- **Boost (step-up):** Vout > Vin
- **Buck-boost (inverting):** Vout can be higher or lower, opposite polarity

**Applications:** Computer power supplies (ATX), phone chargers (SMPS in the charger brick), industrial motor drives, solar inverters.

---

## 2. Example

### Zener Regulator Design

**Input:** Vin = 12V DC, Vout = 5.1V (Zener), IL = 20mA, IZ(knee) = 5mA

**Solution:**
```
Total current: IT = IL + IZ(min) = 20 + 5 = 25mA
Series resistance: Rs = (Vin - VZ)/IT = (12 - 5.1)/25mA = 6.9V/25mA = 276Ω → use 270Ω

Check power in zener:
IZ(max) = (Vin - VZ)/Rs - IL = (12-5.1)/270 - 0 = 25.56mA (with no load)
PZ = VZ × IZ(max) = 5.1 × 25.56mA = 130mW → use 0.5W zener for safety margin

Power in Rs:
PR = IT² × Rs = (25mA)² × 270 = 168mW
```

---

## 3. Applications and Use Cases

1. **78XX in microcontroller boards**: Arduino, Raspberry Pi use 7805/LM1117 series regulators to convert 9-12V input to 5V/3.3V for logic circuits.
2. **IC 723 in lab power supplies**: Variable output lab power supplies (0-30V, 0-5A) use IC 723 as the control element.
3. **SMPS in ATX PC PSU**: Desktop computers use SMPS to generate +12V, +5V, +3.3V, -12V simultaneously at high efficiency.
4. **Battery charging**: SMPS with current-limiting feedback is used in Li-ion, NiMH battery chargers.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Zener Regulator Design [May 2019 PYQ, Q3]

**Problem:** Design a loaded 5.1V zener diode voltage regulator for a load current of 20mA. Input voltage is 12V DC. Assume that zener knee current is 5mA. [3 marks]

**Solution:**

**Step 1: Choose the zener diode**
- Zener voltage: VZ = 5.1V
- Required minimum zener current: IZ(knee) = 5mA

**Step 2: Calculate series resistance Rs**

Maximum load → zener carries only IZ(min):
```
Rs = (Vin - VZ) / (IL + IZ(min))
   = (12 - 5.1) / (20 × 10⁻³ + 5 × 10⁻³)
   = 6.9 / 25 × 10⁻³
   = 276Ω

Standard value: Rs = 270Ω
```

**Step 3: Power rating of Rs**
```
PR(max) = (Vin - VZ)² / Rs = (6.9)² / 270 = 47.61/270 = 176mW → use 0.5W resistor
```

**Step 4: Power rating of zener**

When no load (IL = 0):
```
IZ(max) = (Vin - VZ) / Rs = 6.9/270 = 25.6mA
PZ(max) = VZ × IZ(max) = 5.1 × 25.6mA = 130mW → use 500mW (0.5W) zener
```

**Final Design:**
- Zener: 5.1V, 0.5W
- Rs = 270Ω, 0.5W resistor

---

### Example 2: 78XX Regulator Circuit [May 2019 PYQ, Q2]

**Problem:** Draw and explain the circuit of a 78XX IC based voltage regulator. [3 marks]

**Solution:**

**Circuit:**
```
         C1 (0.33μF)            C2 (0.1μF)
Vin ─────||─────┬────[78XX]────┬─────||────── Vout
                │    1  3  2   │
               ═══              ═══
                │                │
               GND              GND
```

Pin assignments: Pin 1 = Input, Pin 2 = Ground, Pin 3 = Output.

**Working:**
1. The 78XX contains an internal bandgap reference, error amplifier, and NPN pass transistor.
2. The error amplifier compares a fraction of Vout with the internal reference (~1.25V).
3. The pass transistor adjusts its VCE to maintain Vout constant.
4. C1 prevents oscillation by bypassing lead inductance on input.
5. C2 improves transient response and stability on output.

**Key characteristics of 7805:**
- Output voltage: +5V ±4%
- Output current: up to 1A (with heatsink)
- Minimum input: 7V (2V dropout)
- Internal short-circuit protection
- Thermal shutdown at 150°C junction temperature

---

### Example 3: IC 723 High Voltage Regulator Design

**Problem:** Design an IC 723 based high voltage regulator to produce Vout = 12V. 

**Solution:**

For IC 723 high voltage mode (Vout > Vref = 7.15V):
```
Vout = Vref × (1 + R1/R2)
12 = 7.15 × (1 + R1/R2)
1 + R1/R2 = 12/7.15 = 1.678
R1/R2 = 0.678
```

Choose R2 = 7.5kΩ (standard value):
```
R1 = 0.678 × 7.5kΩ = 5.08kΩ ≈ 5.1kΩ (use 5.1kΩ)
```

Current limiting resistor (for I_limit = 100mA):
```
RSC = 0.7V / I_limit = 0.7 / 0.1 = 7Ω → use 6.8Ω standard value
```

**Summary:**
- R1 = 5.1kΩ, R2 = 7.5kΩ → Vout = 7.15 × (1 + 5.1/7.5) = 7.15 × 1.68 = 12.01V ✓
- RSC = 6.8Ω → I_limit ≈ 0.7/6.8 = 103mA
- Bypass capacitor on V+ pin: 100pF to prevent oscillation

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q2]: Draw and explain the circuit of a 78XX IC based voltage regulator. [3 marks]

**Complete Solution:** *(See Solved Example 2 above — fully self-contained solution provided there)*

**Full answer restated here:**

The 78XX fixed positive voltage regulator IC has 3 pins: Input, Ground, Output.

```
Input ─── [78XX] ─── Output
              │
             GND
```

Internally it contains:
- **Bandgap reference** (~1.25V, temperature-stable)
- **Differential error amplifier**: compares scaled output voltage to the bandgap reference
- **NPN darlington pass transistor**: series element that drops the excess voltage
- **Short-circuit current limiting**: limits output current if output is shorted
- **Thermal shutdown**: turns off at 150°C to prevent die damage

External capacitors are required:
- Cin = 0.33μF (ceramic) at input: stabilizes against supply lead inductance
- Cout = 0.1μF (ceramic) at output: improves transient load step response

Common 78XX types: 7805 (+5V), 7808 (+8V), 7809 (+9V), 7812 (+12V), 7815 (+15V), 7818 (+18V), 7824 (+24V). All rated at 1A continuous output current.

---

### PYQ 2 [May 2019, Q6b]: Draw and explain the circuit of a series voltage regulator. [5 marks]

**Complete Solution:**

**Series Regulator Circuit:**

```
         VCC (unregulated, e.g., 15V)
          │
        [Q1 NPN] ← Series pass transistor (e.g., 2N3055)
          │ Emitter
          ├─────────────────── Vout (regulated, e.g., 12V)
          │                         │
        Base────[R1]───┐       [Load RL]
                       │            │
                [Q2 NPN] ← Error amplifier transistor
                       │
               [Zener VZ = 5.1V]
                       │
                      GND

Voltage divider R2, R3 from Vout to GND
R3 midpoint connected to Q2 base
```

**Simplified working:**

1. **Zener VZ** sets the reference voltage.
2. **Q2 error amplifier**: Compares a sample of Vout (from R2/R3 divider) with Vref (VZ + VBE(Q2)).
3. **Q1 pass transistor**: Acts as a variable resistor in series with load.
4. **Feedback loop**: 
   - If Vout tries to increase → VB(Q2) increases → IC(Q2) increases → VRC1 increases (drops more across collector resistor) → VB(Q1) decreases → Q1 less conductive → VCE(Q1) increases → Vout pulled back down.
5. The output voltage is set by:
   ```
   Vout = VZ + VBE(Q2) = 5.1 + 0.7 = 5.8V (for this configuration)
   ```
   Or with a voltage divider sensing Vout, by: Vout = Vref × (1 + R2/R3)

**Advantages over shunt regulator:**
- Higher efficiency (no constant shunt current path)
- Better load regulation (tight control via negative feedback)
- Higher output current capability (pass transistor can be a power transistor)

**Advantages over zener-only regulator:**
- Can supply much higher currents (up to amperes with power transistors)
- Better line and load regulation (error amplifier actively corrects)

---

### PYQ 3 [May 2019, Q7b]: Draw and explain the block diagram of SMPS. [5 marks]

**Complete Solution:**

**SMPS Block Diagram:**

```
AC Mains (230V/50Hz)
        │
  ┌─────▼─────┐
  │  EMI Filter│
  └─────┬─────┘
        │
  ┌─────▼──────┐
  │Input Rectifier│
  │  + Filter C │  → Vbus ≈ 325V DC (for 230V AC)
  └─────┬──────┘
        │
  ┌─────▼──────┐
  │High-frequency│
  │   Switch   │  (MOSFET/IGBT, switching at 20kHz-1MHz)
  └─────┬──────┘
        │
  ┌─────▼──────┐
  │ Transformer │  (small ferrite core, HF operation)
  └─────┬──────┘
        │
  ┌─────▼──────┐
  │Output Rectifier│
  │  + Filter  │  → Vout DC (e.g., 5V, 12V, 24V)
  └─────┬──────┘
        │
      Vout ────── Load
        │
  ┌─────▼──────┐
  │  Feedback  │ (optocoupler for isolation)
  │  Circuit   │
  └─────┬──────┘
        │
  ┌─────▼──────┐
  │PWM Controller│ (e.g., UC3842, TL494)
  │  + Oscillator│
  └─────┬──────┘
        │
    (controls switch duty cycle)
```

**Block-by-block explanation:**

1. **EMI Filter**: Prevents switching noise from reaching the AC mains and vice versa. Uses X and Y capacitors plus common-mode chokes.

2. **Input Rectifier + Filter**: Bridge rectifier converts 230V AC to ~325V DC. Large electrolytic capacitor smooths the rectified waveform.

3. **High-frequency Switch (MOSFET)**: The main transistor (usually a power MOSFET) switches the 325V DC on/off at 20kHz-1MHz. Controls how much energy is transferred per cycle.

4. **Transformer**: A ferrite-core transformer steps down (or steps up) the high-frequency switched voltage. Ferrite core handles HF with low losses (vs. iron core used at 50Hz only). Provides **galvanic isolation** between mains and output.

5. **Output Rectifier + Filter**: Fast Schottky diodes rectify the transformer secondary voltage. Small inductor + capacitor filter the output.

6. **Feedback/Control**: An optocoupler senses the output voltage and feeds back to the PWM controller while maintaining isolation. PWM controller adjusts the duty cycle of the switch:
   - Vout too low → increase duty cycle → more energy per cycle → Vout rises
   - Vout too high → decrease duty cycle → less energy → Vout falls

**Advantages of SMPS:**
- Efficiency 80-90% (vs. 30-50% for linear regulators)
- High power density (compact, lightweight)
- Wide input voltage range possible
- Multiple output voltages from one transformer

**Disadvantages:**
- Complex design, more components
- Generates EMI (requires filtering)
- Can cause interference in audio and precision measurement equipment
