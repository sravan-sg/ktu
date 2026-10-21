# Voltage Multipliers and Sweep Circuits

## 1. Explanation

### Voltage Multipliers — Core Intuition

A **voltage multiplier** is a circuit that produces a DC output voltage that is an exact integer multiple (2×, 3×, N×) of the AC input peak voltage. It achieves this using a cascade of **diode-capacitor stages**, where each stage adds another Vpeak increment to the output.

The fundamental principle is the **voltage doubler** — a series combination of a clamper (capacitor + diode that shifts the waveform) followed by a peak detector (capacitor + diode that samples the peak of the shifted wave).

**Key insight:** If a clamper can produce 2×Vpeak at its output, a second stage can add another Vpeak to produce 3×Vpeak, and so on.

**Why not use a simple transformer?** Voltage multipliers work without a step-up transformer — they convert the peak voltage of an AC source to a much higher DC voltage using only capacitors and diodes. This makes them compact, cheap, and suitable for high-voltage low-current applications (CRT displays, photocopiers, laser systems, X-ray generators).

### Half-Wave Voltage Doubler

```
Stage 1 (Clamper):        Stage 2 (Peak Detector):
       C1                        D2
Vin ───||───┬─── Vnode ──────|◁───┬─── Vout (DC ≈ 2Vpeak)
            │                     │
           ─|◁ D1            C2  ═══
            │                     │
           GND                   GND
```

**Operation:**
- **Negative half cycle:** D1 conducts, charges C1 to Vpeak. D2 reverse biased.
- **Positive half cycle:** D1 OFF. Vnode = Vin + Vc1 = Vpeak + Vpeak = 2Vpeak. D2 conducts, charges C2 to 2Vpeak.
- **Steady state:** C2 holds at Vout = 2Vpeak.

### Full-Wave Voltage Doubler

```
      D1
Vin ─|◁|─┬─────── Vout (+2Vpeak DC)
          │C1
         ═══
          │
GND ──────┤
          │
         ═══
          │C2
Vin ─|▷|─┴─────── (bottom)
      D2
```

Actually the standard full-wave doubler:
```
         D1          C1
 +Vin ──|◁|──┬──────═══──── +Vout
              │              │
              C1            ═══
              │              │
 -Vin ──|▷|──┴──────═══──── GND
         D2          C2
```

Each half cycle, one diode charges one capacitor to Vpeak. The two capacitors in series produce 2Vpeak across the output.

### Voltage Tripler

A half-wave voltage doubler extended by one more stage:

```
       C1         C3
Vin ───||───┬──── D3 ──|◁|───┬─── 3Vpeak
            │                │
           D1 ◁         C3  ═══
            │                │
           ───          ─────┘
            C2
Stage 2 (Doubler) → Node at 2Vpeak → third clamper adds another Vpeak → 3Vpeak output
```

**General Rule:** An N-stage voltage multiplier produces N × Vpeak DC output, at the cost of output current capability which decreases with N (since each capacitor must supply the full load current through a longer chain).

### Sweep Circuits Using Transistor as a Switch

A **sweep circuit** generates a linear voltage ramp (sawtooth wave) — a voltage that increases linearly from a minimum to a maximum, then resets rapidly to the minimum. This is used for horizontal deflection in CRTs, oscilloscope timebase generators, and radar ranging.

**Transistor as a Switch (Basic Principle):**

A BJT transistor can be driven between two states:
- **Saturation (ON):** Base overdrive → collector-emitter behaves as a closed switch (VCE ≈ 0.2V)
- **Cutoff (OFF):** Base voltage below threshold → transistor OFF → collector-emitter is open circuit

**Simple Transistor Sweep Circuit:**

```
        VCC
         │
         R
         │
         ├───── Vout
         │
        C (capacitor being charged)
         │
         ├───Collector
        Q (NPN BJT)
         │Emitter
         │
        GND

Control input → Base
```

**Operation:**
1. **Transistor OFF (base low):** C charges through R toward VCC. Vout rises as:
   ```
   Vout(t) = VCC × (1 - e^(-t/RC))
   ```
   For small t (initial region, τ >> T_sweep): Vout ≈ VCC × t/(RC) — approximately linear ramp.

2. **Transistor ON (base high):** C rapidly discharges through transistor (ON resistance ≈ 0). Vout drops to near 0V (flyback).

3. This produces a sawtooth/sweep waveform.

**Linearity improvement:** For a more linear ramp, the charging resistor R is replaced with a **constant current source** (since V = (I/C)×t is perfectly linear). Alternatively, only the initial linear portion of the exponential is used (keep the sweep to less than 10% of the full exponential curve).

---

## 2. Example

### Voltage Doubler — Steady State Calculation

**Input:** Vin = 120V RMS AC
**Peak voltage:** Vpeak = 120 × √2 = 169.7V ≈ 170V

**Output of voltage doubler:**
```
Vout = 2 × Vpeak = 2 × 170 = 340V DC
```

**Ripple consideration:** If the load requires 10mA and capacitor C2 = 100μF:
```
Ripple voltage = I/(f × C) = 10×10⁻³/(60 × 100×10⁻⁶) = 1.67V peak-to-peak
```

---

## 3. Applications and Use Cases

1. **CRT High-Voltage Supply:** TV picture tubes and oscilloscope CRTs require 15-30kV for electron acceleration. A high-order Cockcroft-Walton voltage multiplier (10-20 stages) generates this from a ~1kV source without heavy transformers.

2. **Photocopier Drum Charging:** Copiers use a corona wire at ~6-8kV to charge the selenium drum. A voltage multiplier supplies this from a standard 230V supply.

3. **X-Ray Tube Power Supply:** Medical and industrial X-ray generators use voltage multipliers to produce 40-150kV for X-ray tube operation.

4. **LASER Power Supplies:** Pulsed CO₂ and excimer lasers require short, high-voltage pulses — multiplier circuits generate these.

5. **Oscilloscope Timebase:** The sweep circuit generates the precisely linear horizontal sweep voltage that moves the electron beam from left to right, creating the time axis of the oscilloscope display.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Voltage Tripler Design

**Problem:** A 12V RMS AC source is connected to a voltage tripler circuit. Find:
(a) The peak AC input voltage
(b) The expected DC output voltage (ideal)
(c) If C = 100μF for each stage and load draws 5mA, estimate the ripple voltage at the output

**Solution:**

**(a) Peak AC input:**
```
Vpeak = Vrms × √2 = 12 × 1.414 = 16.97V ≈ 17V
```

**(b) Ideal DC output:**
```
Vout (tripler) = 3 × Vpeak = 3 × 17 = 51V DC
```

**(c) Ripple voltage:**
The output capacitor of the 3rd stage (C3) supplies the load current between charge cycles. At 50Hz:
```
Vripple = I_load / (f × C) = 5×10⁻³ / (50 × 100×10⁻⁶)
        = 5×10⁻³ / 5×10⁻³
        = 1V peak-to-peak
```

**Practical output:** Vout ≈ 51V - 0.5V (ripple midpoint) = approximately 50V with 1V ripple.

---

### Example 2: Transistor Sweep Circuit Timing

**Problem:** In a transistor sweep circuit, R = 220kΩ and C = 0.1μF. The transistor is switched off for 1ms to generate a sweep. VCC = 12V.
(a) Calculate τ
(b) Find the peak sweep voltage at the end of 1ms
(c) Calculate the sweep rate (linearity approximation)

**Solution:**

**(a) Time constant:**
```
τ = RC = 220×10³ × 0.1×10⁻⁶ = 22ms
```

**(b) Peak sweep voltage at t = 1ms:**
```
Vout(1ms) = VCC × (1 - e^(-t/τ))
           = 12 × (1 - e^(-1ms/22ms))
           = 12 × (1 - e^(-0.0455))
           = 12 × (1 - 0.9555)
           = 12 × 0.0445
           = 0.534V
```

**(c) Sweep rate:**
```
Since t/τ = 1/22 = 0.045 << 1, we are in the highly linear region.
Linear approximation: Vout ≈ VCC × t/τ = 12 × t/22ms

Sweep rate = VCC/τ = 12/22ms = 545 V/s = 0.545 mV/μs
```

For 1ms sweep: ΔV = 545 × 1ms = 0.545V (≈ 0.534V, 2% error due to non-linearity — excellent linearity since we used only 4.5% of the exponential curve).

---

### Example 3: Voltage Doubler with Non-Ideal Diodes

**Problem:** A half-wave voltage doubler uses silicon diodes (Vf = 0.7V each) with 10V peak AC input. Find the practical DC output voltage.

**Solution:**

**Ideal output:** 2 × Vpeak = 2 × 10 = 20V

**Losses due to diode drops:**
- D1 (clamper stage): 0.7V drop during charging → C1 charges to Vpeak - 0.7 = 10 - 0.7 = 9.3V
- At the peak detector stage: Vnode = Vin + Vc1 = 10 + 9.3 = 19.3V
- D2 (peak detector): 0.7V drop → C2 charges to 19.3 - 0.7 = 18.6V

**Practical output:** Vout = 18.6V (instead of ideal 20V)

**Efficiency:** 18.6/20 = 93%

**Conclusion:** For high-voltage multipliers (VCC >> Vf), diode drops are negligible. For low-voltage multipliers, Schottky diodes (Vf ≈ 0.3V) should be used to minimize losses.

---

## 5. Previous Year Questions and Solutions

### PYQ 1: Explain the working of a voltage doubler circuit with a circuit diagram. [9 marks]

**Complete Solution:**

**Circuit (Half-Wave Voltage Doubler):**

```
         D1 (1N4007)
Vin ─────|◁|─────┬───────────── Vout
                 │              │
    C1 (100μF)  ═══  C2 (100μF)═══  Load
                 │              │
               GND            GND

Note: Properly, the circuit has Vin to C1 to junction, D1 from junction to GND (clamp stage), 
and D2 from junction to C2 top (peak detector), C2 bottom to GND.
```

**Correct Configuration:**
```
                        D2
                  ┌────|◁|────┬─── Vout (+2Vpeak DC)
     C1           │           │
Vin─||─┬──────────┘      C2  ═══
       │                      │
      ─|◁ D1                 GND
       │
      GND
```

**Step-by-step operation:**

**Cycle 1 — Negative half (Vin = -Vpeak):**
- Output node goes negative → D1 (anode connected to output node after C1, cathode to GND) becomes forward biased
- Wait — let me use the correct standard description:

D1: anode at the junction between C1 and C2/D2; cathode at GND.
D2: anode at the same junction; cathode at Vout (C2 top).

**Negative Half Cycle:**
- Vin goes to -Vpeak. Through C1, the right plate of C1 tries to go to -Vpeak. 
- D1 forward biases (junction tries to go negative → D1 pulls it to ~0V).
- C1 charges to Vpeak with polarity: left = -Vpeak, right = 0V (D1 holds right plate at ~0V)
- VC1 = Vpeak (stored, left plate negative)

**Positive Half Cycle:**
- Vin goes to +Vpeak. Left plate of C1 goes to +Vpeak.
- Right plate of C1 (due to stored VC1): +Vpeak + Vpeak = +2Vpeak (D1 now reverse biased — OFF)
- Junction voltage = +2Vpeak → D2 conducts → C2 charges to 2Vpeak
- D1 is reverse biased (junction at +2Vpeak >> GND) — stays off

**Steady State:** C2 maintains Vout = 2 × Vpeak DC (ripples only during load discharge between half cycles).

**Voltage Doubler Summary:**

| Input | C1 Voltage | C2 Voltage (Output) |
|-------|------------|---------------------|
| Vpeak = 5V | 5V | 10V |
| Vpeak = 12V | 12V | 24V |
| Vpeak = 100V | 100V | 200V |

**Limitations:**
- Output voltage drops significantly under heavy loads (capacitors discharge between cycles)
- Not suitable for high current loads — limited to μA to mA range
- Each additional multiplier stage reduces output regulation further
