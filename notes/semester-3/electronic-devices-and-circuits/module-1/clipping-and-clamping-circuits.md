# Clipping and Clamping Circuits

## 1. Explanation

### Core Intuition

**Clipping circuits** and **clamping circuits** are two fundamental wave-shaping diode networks. While both use diodes, they serve completely different purposes:

- **Clipper**: Cuts off (clips) portions of a waveform that exceed a reference level — it **limits** the amplitude. Think of it as a voltage limiter.
- **Clamper**: Shifts the entire waveform up or down by adding a DC level — it **translates** the waveform. Think of it as a DC restorer or DC inserter.

The key to understanding both circuits is the **diode's switching action**: it conducts only when forward biased (Vforward > Vth ≈ 0.7V for silicon), and blocks current when reverse biased.

### Clipping Circuits

A clipper removes signal components above (positive clipper), below (negative clipper), or between (biased clipper) voltage thresholds.

#### Positive Clipper (Series)

```
        D
Vin ───▷|───┬─── Vout
            │
            R
            │
           GND
```

Actually, the standard shunt clipper is more common:

**Positive Shunt Clipper:**
```
        R
Vin ───┤├───┬─── Vout
            │
           ▽ D (anode to output, cathode to GND)
            │
           GND
```

**Operation:**
- When Vin > 0 (positive half): Diode forward biased → conducts → Vout ≈ 0 (or Vdiode ≈ 0.7V). Positive portion clipped.
- When Vin < 0 (negative half): Diode reverse biased → open circuit → Vout = Vin × R/(R+0) ≈ Vin (for ideal; full negative passes through)

Wait — the output is taken after R in a shunt clipper. When the diode conducts (clipping), the output is clamped near 0V. When diode is off, current flows through R and the load but with no diode shunt, Vout ≈ Vin (if load resistance >> R).

**Key formulas:** For ideal diode:
```
Positive clipper output:
Vout = 0V        when Vin > 0 (diode ON, clips positive)
Vout = Vin       when Vin < 0 (diode OFF, passes through)
```

#### Negative Clipper

Diode is reversed (cathode to output, anode to GND in shunt):
```
Vout = Vin       when Vin > 0 (diode OFF)
Vout = 0V        when Vin < 0 (diode ON, clips negative)
```

#### Biased Clipper

A reference voltage VR (battery) is placed in series with the diode to set the clipping level:
```
        R
Vin ───┤├───┬─── Vout
            │
           ▽ D
            │
           VR (reference battery)
            │
           GND
```

**Operation:**
- Diode conducts only when Vin > VR (for positive biased clipper)
- Clips all signal above VR
- For negative biased clipper (diode reversed, VR reversed): clips below -VR

**Output:**
```
Biased positive clipper:
Vout = VR        when Vin > VR (diode ON, clamps to VR)
Vout = Vin       when Vin < VR (diode OFF, passes through)
```

### Clamping Circuits

A clamper adds a DC level to the signal without changing its waveform shape or peak-to-peak amplitude.

#### Positive Clamper

```
       C
Vin ───||───┬─── Vout
            │
           ▷ D (anode to GND, cathode to output) — actually D with anode connected to output and cathode to GND reversed for positive clamper
            │
           GND
```

**Correct Positive Clamper (shifts signal up):**
```
       C
Vin ───||───┬─── Vout
            │
           ▽ D  (anode at GND, cathode at output node)
            │
           GND
```

**Operation Principle:**
- During the **negative half cycle** of Vin: Diode forward biased → conducts → capacitor charges to the peak negative value (|Vpeak|), with polarity that makes left plate negative, right plate positive. Vout ≈ 0 (clamped to ground through diode).
- During the **positive half cycle**: Diode reverse biased → open. Capacitor voltage (which is now a DC source = |Vpeak|) adds to the input signal:
  ```
  Vout = Vin + Vc = Vin + |Vpeak|
  ```

**Result:** The entire waveform is shifted up by |Vpeak|. The most negative point of the output is now clamped at 0V.

For a sine wave with amplitude Vm:
```
Output: Vout = Vm sinωt + Vm = Vm(1 + sinωt)
- Minimum value = 0V (clamped to ground)
- Maximum value = 2Vm
- Peak-to-peak amplitude = 2Vm (unchanged from input)
```

#### Negative Clamper

Diode is reversed (anode at output, cathode at ground):
```
- Capacitor charges to +Vpeak during positive half cycle
- Output is shifted down: Vout = Vin - Vpeak
- Maximum output = 0V (clamped at ground)
- Minimum output = -2Vpeak
```

#### Biased Clamper

A reference voltage VR in series with the diode sets the clamping level:
```
Clamping level = VR (instead of 0V)
Positive biased clamper: minimum output = +VR
Negative biased clamper: maximum output = -VR
```

### Key Distinction Summary

| Property | Clipper | Clamper |
|----------|---------|---------|
| Contains capacitor? | No (just R + D) | Yes (C is essential) |
| Changes waveform shape? | Yes (removes portions) | No (shape preserved) |
| Changes peak-to-peak amplitude? | Yes (reduced) | No (unchanged) |
| Changes DC level? | No | Yes (adds DC component) |
| Operation | Voltage limiting | DC restoration/shifting |
| Application | Overvoltage protection, waveform squaring | TV sync separator, DC restoration in video |

---

## 2. Example

### Positive Clipper with Sine Wave Input

**Input:** Vin = 10 sin(ωt) V
**Circuit:** Positive shunt clipper with ideal diode, R = 1kΩ

```
Input waveform:
+10V ─────╮    ╭─────
          │    │
 0V ──────╯    ╰──────  (sine wave)
-10V           ╰───╮

Output waveform (positive clipped):
 0V ─────────────────
-10V           ╰───╮  (only negative half survives)
```

The positive half is removed; output swings from 0 to -10V.

**Biased Clipper Example:**

With VR = +3V bias (positive biased clipper):
```
Input: 10 sin(ωt)
Output:
- When Vin > 3V → Vout = 3V (clipped to VR)
- When Vin < 3V → Vout = Vin (unchanged)

Output range: -10V to +3V (instead of -10V to +10V)
```

---

## 3. Applications and Use Cases

### Clipper Applications

1. **Overvoltage Protection**: Clippers at the input of sensitive amplifiers or ADCs prevent excessive input voltages from damaging the circuit. TVS (Transient Voltage Suppression) diodes are specialized clippers.

2. **Waveform Squaring**: A symmetric clipper (both positive and negative) applied to a sine wave produces an approximate square wave — used in zero-crossing detectors and frequency dividers.

3. **Amplitude Limiters in FM Receivers**: FM discriminators use limiters (clippers) to remove amplitude variations from the received signal, since FM information is in frequency only.

4. **Noise Clipping**: In communication systems, noise spikes exceeding the signal amplitude are clipped to prevent false triggering of digital circuits.

### Clamper Applications

1. **DC Restoration in Television**: Video signals lose their DC component when passed through AC-coupled amplifiers. A clamper (DC restorer) reinserts the correct DC level before the CRT or display, ensuring the black level is correctly positioned.

2. **Voltage Doublers**: The positive clamper is the first stage of a voltage doubler — it shifts the AC signal up by Vpeak, then a peak detector extracts 2Vpeak.

3. **Bias Clamping in Digital Systems**: Clampers ensure that digital signal levels remain within the specified logic thresholds even after passing through reactive components.

4. **Radar Pulse Processing**: Clampers restore the baseline (black level) of radar return pulses after amplification, ensuring accurate range measurement.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Biased Clipper Analysis [KTU Style]

**Problem:** A sinusoidal input of 20 sin(ωt) V is applied to a biased positive clipper with VR = 5V and an ideal diode. Sketch the output waveform and find:
(a) The clipping voltage level
(b) The fraction of the input cycle that is clipped

**Solution:**

**(a) Clipping voltage level = VR = 5V**

The diode conducts (clips) when Vin > VR = 5V.

Output:
```
Vout = 5V      when Vin > 5V
Vout = Vin     when Vin ≤ 5V
```

**Output waveform:**
```
+20V
+5V  ─ ─ ─ ╔══╗─ ─ ─ (clipped flat at +5V)
           ╱    ╲
0V ───────╱      ╲──────╱──────────
          ╲      ╱╲      ╱
-20V       ╲────╱  ╲────╱
```

**(b) Fraction of cycle clipped:**

Clipping starts when Vin = VR:
```
20 sin(ωt) = 5
sin(ωt) = 5/20 = 0.25
ωt = arcsin(0.25) = 14.48° = 0.253 rad

Clipping ends at: ωt = 180° - 14.48° = 165.52°
```

Duration of clipped portion per cycle:
```
Clipped angle = 165.52° - 14.48° = 151.04°
Fraction clipped = 151.04°/360° = 0.419 = 41.9%
```

**Answer:** 41.9% of the positive half cycle is clipped flat at 5V.

---

### Example 2: Positive Clamper Analysis

**Problem:** A square wave with amplitude ±8V and frequency 1 kHz is applied to a positive clamper with an ideal diode. Find the output waveform.

**Solution:**

**Given:** Vin alternates between +8V and -8V.

**Positive clamper operation (diode: anode to GND, cathode to output after capacitor):**

**During negative half cycle (Vin = -8V):**
- Diode forward biased → conducts
- Capacitor charges with polarity: left plate (vin side) = -8V, right plate = 0V (diode holds at 0V)
- Voltage across capacitor: Vc = +8V (left plate negative, right plate at anode = GND = 0V)
- So capacitor stores Vc = 8V

**During positive half cycle (Vin = +8V):**
- Diode reverse biased → open circuit
- Vout = Vin + Vc = +8V + 8V = +16V

**Output waveform:**
```
Input:   +8V ─────     ─────
              │   │   │   │
        -8V   ─────   ─────

Output: +16V ─────     ─────
              │   │   │   │
         0V   ─────   ─────
```

The output square wave: swings between 0V and +16V (clamped at 0V minimum). Peak-to-peak = 16V (same as input = 8-(-8) = 16V). ✓

---

### Example 3: Voltage Doubler as Combined Clamper + Peak Detector

**Problem:** A sinusoidal signal of 12V peak is applied to a half-wave voltage doubler. Find the output DC voltage.

**Solution:**

**Stage 1 — Positive Clamper:**
- Capacitor C1 charges to 12V (peak) during negative half cycle
- During positive half cycle, Vout1 = 12 + 12 = 24V (peak)

**Stage 2 — Peak Detector (capacitor C2 + diode D2):**
- D2 charges C2 to the peak of the clamped waveform
- Vout2 = 24V DC

**Result:** Output DC voltage = 2 × Vpeak = 2 × 12 = 24V

This is used in CRT high-voltage supplies, multiplier circuits in Cockcroft-Walton voltage multipliers, and LASER power supplies.

**Voltage Tripler:** Adds a third stage:
- Vout3 = 3 × Vpeak = 36V

The pattern: Voltage multiplier of order N → Vout = N × Vpeak.

---

## 5. Previous Year Questions and Solutions

### PYQ 1: Explain positive and negative clippers with waveforms. [6 marks]

**Complete Solution:**

**Positive Clipper:**

Circuit: Shunt diode (anode at output node, cathode at GND), series R at input.

```
        R
Vin ───┤├───┬─── Vout
            │
           ▷| D (anode → output, cathode → GND)
            │
           GND
```

Operation:
- Vin > 0 (positive cycle): Diode forward biased → short circuit → Vout ≈ 0V. Positive portion clipped.
- Vin < 0 (negative cycle): Diode reverse biased → open → Vout = Vin. Negative portion passes.

Output: Only negative half of signal appears at output. Positive half is removed (clipped to 0V).

```
Input  : Sine wave, ±10V
Output : 0 to -10V (positive clipped)

Waveform:
       +10V: ─╮     ╭─  (input only)
         0V: ─╰─────╯─  (clipped output stuck at 0V for positive)
       -10V: ──╰───╯──  (both input and output follow here)
```

**Negative Clipper:**

Same circuit but diode reversed (cathode at output, anode at GND).

- Vin > 0: Diode reverse biased → open → Vout = Vin. Positive passes.
- Vin < 0: Diode forward biased → short → Vout ≈ 0V. Negative clipped.

Output: Only positive half passes; negative half clipped to 0V.

---

### PYQ 2: Draw and explain the working of a clamper circuit. How does a positive clamper differ from a negative clamper? [9 marks]

**Complete Solution:**

**Positive Clamper Circuit:**
```
       C (10μF)
Vin ───||───────┬─── Vout
                │
               ─|◁─ D (cathode up, anode to GND)
                │
               GND
```

(Anode at GND, cathode at output node — diode points upward)

**Negative Half Cycle Operation (Vin = -Vpeak):**
1. Diode is forward biased (output node tries to go negative → diode conducts)
2. Capacitor charges rapidly to Vpeak, with left plate (+), right plate (-) relative to direction
3. Vout is clamped at ≈ 0V (diode hold it at GND potential)
4. Capacitor voltage: Vc = Vpeak (stored energy)

**Positive Half Cycle Operation (Vin = +Vpeak):**
1. Diode is reverse biased (anode at 0V GND, cathode at positive output — diode open)
2. Now the output node "sees" Vin AND the capacitor voltage Vc in series (aiding):
   ```
   Vout = Vin + Vc = Vpeak + Vpeak = 2×Vpeak
   ```
3. The minimum output voltage = 0V; maximum = 2Vpeak

**Result:** Entire waveform shifted up by Vpeak. Bottom of waveform is clamped at 0V.

**Negative Clamper:** Diode is reversed. The top of the waveform is clamped at 0V (waveform shifted down). Maximum output = 0V; minimum = -2Vpeak.

**Comparison Table:**

| Feature | Positive Clamper | Negative Clamper |
|---------|-----------------|-----------------|
| Diode orientation | Anode to GND, cathode to output | Cathode to GND, anode to output |
| Conduction cycle | Negative half cycle | Positive half cycle |
| DC shift direction | Upward (+Vpeak) | Downward (-Vpeak) |
| Clamped voltage level | Bottom at 0V (or +VR if biased) | Top at 0V (or -VR if biased) |
| Output peak | 2Vpeak | 0V |
| Output minimum | 0V | -2Vpeak |
