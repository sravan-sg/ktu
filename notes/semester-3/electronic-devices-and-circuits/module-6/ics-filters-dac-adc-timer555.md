# ICs: Active Filters, DAC/ADC Converters, and Timer IC 555

## 1. Explanation

### Active Filters — Using Op-Amps for Frequency Selection

**Why Active Filters?**

A **passive filter** (LC or RC only) attenuates signals but cannot amplify them. Its insertion loss and impedance characteristics depend on the load — difficult to cascade. An **active filter** uses an op-amp with resistors and capacitors to implement frequency-selective circuits that:
1. Can provide gain (amplification in the passband)
2. Have low output impedance (easy to drive loads)
3. Are easy to cascade (output of one stage doesn't load the previous)
4. Eliminate the need for bulky, expensive inductors (especially at audio frequencies)

**First-Order Low-Pass Active Filter:**

```
         R1
Vin ─────┤├───┬─────(+)──── Vout
              │      (−)
              C      │
              │   Rf ┤├─┐
             GND     └──┘ (feedback for gain)
                    R2
                GND──┤├──(−)
```

**Transfer function:**
```
H(s) = (1 + Rf/R2) × [1/(1 + sR1C)]

DC gain (s=0): A0 = 1 + Rf/R2   (non-inverting amplifier gain)
Cutoff frequency: fc = 1/(2πR1C)

Magnitude: |H(jω)| = A0 / √(1 + (f/fc)²)
Roll-off: -20 dB/decade above fc
```

**Second-Order Low-Pass Active Filter (Sallen-Key):**

```
         R1        R2
Vin ─────┤├────────┤├──────┬──(+)── Vout
                           │  (−)
         ┌─── C1 ──┘      C2
         │                │
        GND              GND
                          │
              Unity gain (Rf = 0, R2 = ∞) or with gain
```

**Transfer function:**
```
H(s) = A0 × ωn² / (s² + (ωn/Q)s + ωn²)

Where: ωn = 1/√(R1R2C1C2) (natural frequency = 2πfc)
       Q = quality factor (determines frequency response shape near cutoff)
       A0 = passband gain

Roll-off: -40 dB/decade above fc (steeper than 1st order)
```

**Q-factor effect:**
- Q = 0.707 (Butterworth): maximally flat response (no peaking)
- Q > 0.707: Peaking near cutoff (Chebyshev: sharp roll-off, passband ripple)
- Q < 0.707 (Bessel): Linear phase response (best for pulse fidelity)

**High-Pass Active Filters:**

Exactly dual to low-pass — swap R and C positions:
- First order HP: Replace RC in low-pass with CR
- Cutoff frequency: fc = 1/(2πRC) (same formula)
- Response: |H(jω)| = A0 × (f/fc) / √(1 + (f/fc)²)
- Roll-off: -20dB/decade BELOW fc (attenuates low frequencies)

### D/A Converters (DAC)

A **Digital-to-Analog Converter (DAC)** converts an n-bit binary number to a proportional analog voltage or current.

**Important Specifications:**

| Specification | Definition |
|--------------|------------|
| Resolution | 1/2ⁿ of full scale (n = number of bits); smaller = better |
| Accuracy | How close actual output is to ideal; ±½ LSB ideal |
| Full Scale Output | Maximum output voltage (when all bits = 1) |
| Settling Time | Time for output to reach final value within ±½ LSB after input change |
| Linearity Error | Deviation from ideal straight-line transfer function |
| Monotonicity | Output always increases as input increases (1-bit LSB step) |

**LSB voltage:** VLSB = VFS / 2ⁿ

**1. Binary Weighted Resistor DAC:**

```
         RF
D3 (MSB) ──[R]──┬────────────────── Vout
D2       ──[2R]─┤
D1       ──[4R]─┤ (op-amp summer)
D0 (LSB) ──[8R]─┘
```

Each bit has a resistor inversely proportional to its binary weight.

**Output:**
```
Vout = -Vref × RF × [D3/R + D2/2R + D1/4R + D0/8R]

For RF = R:
Vout = -Vref × [D3 + D2/2 + D1/4 + D0/8]
     = -Vref/8 × [8D3 + 4D2 + 2D1 + D0]
```

**Problem:** Requires many different precision resistor values (R, 2R, 4R, 8R... up to 2^(n-1)×R). For 16-bit DAC, resistors range from R to 65536R — difficult to match precisely.

**2. R-2R Ladder DAC:**

Uses only two resistor values (R and 2R), regardless of n:

```
         R         R         R
Vref ────┤├──┬─────┤├──┬─────┤├──┬──── (virtual ground)
             │         │         │
            [2R]      [2R]      [2R]
             │         │         │
            D2(MSB)   D1        D0(LSB)
```

**Working:** Each node sees looking left: 2R (previous ladder looking back), giving 2R || 2R = R at each junction. The circuit creates a natural binary-weighted voltage division.

**Output:**
```
Vout = -Vref × RF/R × [D(n-1)/2 + D(n-2)/4 + ... + D0/2ⁿ]
```

**Advantage over binary-weighted:** Only two resistor values (R and 2R) — easily manufactured as precision resistor arrays.

**Sample and Hold (S&H) Circuit:**

A **sample and hold** circuit captures (samples) the analog input at a specific instant and maintains (holds) that value until the ADC completes conversion (which takes finite time).

```
          S (switch: FET or CMOS analog switch)
Vin ───┤/──┬─────── (to ADC)
           │
           C (hold capacitor: small leakage)
           │
          GND
          
Buffer op-amps on both input and output sides isolate the capacitor from loading.
```

**Operation:**
- **Sample mode (switch closed):** C charges to Vin rapidly. Output tracks Vin.
- **Hold mode (switch open):** C retains voltage. Output holds the sampled value.
- **Aperture time:** The instant the switch opens defines the sampling moment (must be precise for AC signals).
- **Droop rate:** Capacitor slowly discharges due to leakage → imposes maximum hold time.

**Shannon's Sampling Theorem:** To reconstruct an analog signal from samples without aliasing, the sampling frequency must be at least twice the highest signal frequency: fs ≥ 2 × fmax.

### A/D Converters (ADC)

An **Analog-to-Digital Converter (ADC)** converts a continuous analog voltage to a discrete digital binary code.

**1. Flash (Parallel) ADC:**

```
Vref ─── [Resistor ladder R/R/R/R...] ─── 2ⁿ-1 comparators ─── Priority encoder ─── n-bit output
```

- For n bits, uses 2ⁿ-1 comparators and 2ⁿ resistors
- Each comparator compares Vin to a different reference level
- Priority encoder converts comparator outputs to binary

**Speed:** Extremely fast — single clock cycle (1 comparison step). Used in oscilloscopes, radar (1Gsps+)
**Resolution limitation:** 8-bit flash needs 255 comparators — expensive, high power.

**2. Dual Slope ADC:**

**Phase 1 — Integrate (fixed time):** Integrator charges for exactly T1 seconds with Vin as input.
```
Vintegrator = (Vin/RC) × T1  (proportional to Vin)
```

**Phase 2 — De-integrate (variable time):** Switch flips to reference -Vref. Counter counts while integrator discharges from peak to zero:
```
(-Vref/RC) × T2 = -Vout,peak
→ T2 = (Vin/Vref) × T1
→ Digital count N2 = N1 × (Vin/Vref)
```

**Advantages:**
- Very accurate — independent of R, C, and clock frequency values (cancels out)
- Excellent noise rejection (integrates noise over T1, averages to near zero)
- Slow (suitable for multimeters, temperature sensors)

**3. Successive Approximation ADC (SAR ADC):**

Most widely used ADC architecture. Uses binary search algorithm:

```
Input Vin
   │
   ▼
Comparator ──── SAR Register ──── DAC ──── back to Comparator
                    │
                n-bit output
```

**Algorithm (n-bit SAR for n steps):**
1. Set MSB = 1 (try: 1000...0 in binary)
2. DAC generates Vdac = Vref/2
3. Compare Vin to Vdac:
   - If Vin > Vdac: keep MSB = 1 → try next bit
   - If Vin < Vdac: clear MSB = 0 → try next bit
4. Repeat for all n bits (n comparisons total)

**Example (4-bit SAR, Vref = 16V, Vin = 9.5V):**
```
Step 1: Try 1000 → Vdac = 8V. Vin=9.5 > 8 → Keep: 1000
Step 2: Try 1100 → Vdac = 12V. Vin=9.5 < 12 → Clear: 1000
Step 3: Try 1010 → Vdac = 10V. Vin=9.5 < 10 → Clear: 1000
Step 4: Try 1001 → Vdac = 9V. Vin=9.5 > 9 → Keep: 1001

Result: 1001 = 9 (error < 1 LSB = 1V) ✓
```

**Conversion time: n clock cycles** (much faster than dual slope for same resolution).
**Applications:** Audio codecs, sensor interfaces, portable instruments (8-16 bits, 100ksps to 1Msps).

**ADC Comparison:**

| ADC Type | Speed | Accuracy | Complexity | Applications |
|----------|-------|----------|------------|-------------|
| Flash | Fastest (1 cycle) | Low-Medium | High (2ⁿ comparators) | Oscilloscopes, radar |
| SAR | Medium (n cycles) | High | Medium | Audio, sensors, MCUs |
| Dual Slope | Slow (2T cycles) | Very High | Low-Medium | Multimeters, scales |
| Sigma-Delta | Slow-Medium (oversampled) | Very High | Low hardware | Audio, precision instruments |

### Timer IC 555

The **555 timer IC** is one of the most popular ICs ever made, capable of operating as an astable oscillator, monostable one-shot, or PWM generator.

**Internal structure:**
```
VCC ──┬──── Discharge (pin 7) via internal NPN transistor
      │
     [R_internal] 5kΩ
      │
     [Threshold comparator] (pin 6 > 2/3 VCC → output low, flip-flop resets)
      │
     [R_internal] 5kΩ
      │
     [Trigger comparator] (pin 2 < 1/3 VCC → output high, flip-flop sets)
      │
     [R_internal] 5kΩ
      │
     GND

Output (pin 3) = flip-flop Q̄ through output stage
Control Voltage (pin 5): normally 2/3 VCC (can be changed externally)
Reset (pin 4): active low — grounds output when pulled low
```

**Three reference levels generated internally:**
- 2/3 VCC: Upper threshold
- 1/3 VCC: Lower threshold
- 1/3 VCC: Between the two resistor divider taps

**Astable Multivibrator using IC 555:**

```
VCC
 │
[RA]
 │
 ├─── Discharge (pin 7)
[RB]
 │
 ├─── Threshold (pin 6) AND Trigger (pin 2) [connected together]
 C
 │
GND
```

**Operation:**
- Capacitor charges through RA + RB until reaching 2/3 VCC → discharge transistor turns ON → capacitor discharges through RB to 1/3 VCC → discharge transistor turns OFF → cycle repeats

**Timing:**
```
Charge time (output HIGH): t_HIGH = 0.693 × (RA + RB) × C
Discharge time (output LOW): t_LOW = 0.693 × RB × C
Period: T = t_HIGH + t_LOW = 0.693 × (RA + 2RB) × C
Frequency: f = 1/T = 1.44 / [(RA + 2RB) × C]
Duty cycle: D = t_HIGH/T = (RA + RB)/(RA + 2RB)
```

Note: Duty cycle is always > 50% (since t_HIGH always > t_LOW with this configuration). For 50% duty cycle, add a diode across RB to bypass it during charging.

**Monostable Multivibrator using IC 555:**

```
VCC ─── RA ─── Threshold (pin 6)
                     │
                     C
                     │
                    GND
Discharge (pin 7) ─── between RA and C
Trigger (pin 2) ← negative trigger pulse
Output (pin 3) → goes HIGH for time T after trigger
```

**Timing:**
```
Output pulse width: T = 1.1 × RA × C

For T = 10ms with C = 10μF:
RA = T/(1.1 × C) = 10×10⁻³/(1.1 × 10×10⁻⁶) = 909Ω → use 1kΩ

Trigger: pin 2 must be pulled below 1/3 VCC momentarily to start the timing cycle.
```

---

## 2. Example

### First Order High-Pass Filter Design [May 2019, Q15b]

**Problem:** Realize an active first order high pass filter for lower cut-off frequency of 1kHz and passband gain of 2.

**Solution:**
```
fc = 1kHz, gain = 2 (non-inverting = 1 + Rf/R1 = 2 → Rf = R1)

For high-pass:
fc = 1/(2πRC) → RC = 1/(2π×1000) = 1.59×10⁻⁴

Choose C = 0.01μF:
R = 1.59×10⁻⁴ / 0.01×10⁻⁶ = 15.9kΩ → use 15kΩ (or 16kΩ)

Gain resistors: R1 = Rf = 10kΩ (for gain = 2)
```

---

## 3. Applications and Use Cases

1. **SAR ADC in Microcontrollers**: STM32, ATmega, PIC microcontrollers all include on-chip SAR ADCs (10-12 bits, 1 Msps) for reading sensors (temperature, pressure, light).

2. **Dual Slope in Digital Multimeters**: DMMs use dual slope ADCs for their excellent accuracy and noise rejection — measurement time is slow (100ms) but precision is ±0.1%.

3. **R-2R DAC in Audio Systems**: CD players and digital audio interfaces use R-2R or sigma-delta DACs to convert 16-24 bit PCM data to analog audio.

4. **555 in Pulse Width Modulation (PWM)**: Motor speed controllers, LED dimmers, and switching regulators use 555 astable circuits with variable RB to produce variable duty cycle PWM signals.

5. **Active Low-Pass Filter in Anti-Aliasing**: Before any ADC input, a low-pass filter (often 2nd order Butterworth) limits the signal bandwidth to below fs/2, preventing aliasing — required by Nyquist theorem.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: 555 Astable Design [May 2019, Q20b]

**Problem:** Design an Astable Multivibrator using IC 555 for frequency of operation 2kHz and duty cycle 60%.

**Solution:**

**Given:** f = 2kHz, duty cycle D = 60% = 0.6

**From duty cycle:**
```
D = (RA + RB)/(RA + 2RB) = 0.6
RA + RB = 0.6(RA + 2RB)
RA + RB = 0.6RA + 1.2RB
0.4RA = 0.2RB
RA = 0.5RB
```

**From frequency:**
```
f = 1.44/[(RA + 2RB) × C]
2000 = 1.44/[(0.5RB + 2RB) × C]
2000 = 1.44/[2.5RB × C]
RB × C = 1.44/(2000 × 2.5) = 2.88×10⁻⁴

Choose C = 0.1μF:
RB = 2.88×10⁻⁴ / 0.1×10⁻⁶ = 2880Ω → use 2.7kΩ
RA = 0.5 × 2.7kΩ = 1.35kΩ → use 1.5kΩ
```

**Verification:**
```
T = 0.693 × (RA + 2RB) × C
  = 0.693 × (1.5 + 2×2.7) × 10³ × 0.1×10⁻⁶
  = 0.693 × 6.9 × 10³ × 10⁻⁷
  = 0.693 × 6.9 × 10⁻⁴
  = 4.78×10⁻⁴ s
f = 1/T = 2092 Hz ≈ 2kHz ✓

Duty cycle = (RA+RB)/(RA+2RB) = (1.5+2.7)/(1.5+5.4) = 4.2/6.9 = 0.609 ≈ 61% ✓
```

**Final design:** RA = 1.5kΩ, RB = 2.7kΩ, C = 0.1μF, VCC = 5V to 15V.

---

### Example 2: SAR ADC Step-by-Step Conversion

**Problem:** A 4-bit SAR ADC has Vref = 5V. Find the digital output for Vin = 3.2V. Show all comparison steps.

**Solution:**

**LSB = Vref/2ⁿ = 5/16 = 0.3125V**

| Step | Trial Bit | DAC Output | Vin vs DAC | Decision | Register |
|------|-----------|-----------|-----------|----------|---------|
| 1 | MSB (b3) = 1 | 5×8/16 = 2.5V | 3.2 > 2.5 | Keep | 1000 |
| 2 | b2 = 1 | 5×12/16 = 3.75V | 3.2 < 3.75 | Clear | 1000 |
| 3 | b1 = 1 | 5×10/16 = 3.125V | 3.2 > 3.125 | Keep | 1010 |
| 4 | b0 = 1 | 5×11/16 = 3.4375V | 3.2 < 3.4375 | Clear | 1010 |

**Digital output: 1010₂ = 10 in decimal**

**Actual voltage represented:** 10 × 0.3125 = 3.125V
**Quantization error:** |3.2 - 3.125| = 0.075V < 1 LSB = 0.3125V ✓

---

### Example 3: Sample and Hold Circuit Analysis [May 2019, Q17a]

**Problem:** Draw and explain a sample and hold circuit. Quote a few of its applications. [6 marks]

**Solution:**

**Circuit:**
```
                S (CMOS analog switch, e.g., CD4066)
Vin ──────── Buffer1 ──── ┤/ ──── ┬──── Buffer2 ──── Vout (to ADC)
                                   │
                                   C (hold capacitor, e.g., 10nF low-leakage)
                                   │
                                  GND
```

**Component roles:**
- **Buffer1** (unity-gain op-amp): High input impedance to avoid loading the signal source; low output impedance to charge C rapidly.
- **Analog switch S**: CMOS bilateral switch controlled by SAMPLE/HOLD logic signal.
- **Hold capacitor C**: Stores the sampled voltage. Uses high-quality capacitor (polypropylene, polystyrene) with very low leakage current.
- **Buffer2**: High input impedance so it doesn't discharge C; provides low output impedance to drive ADC input.

**Operation — two modes:**

**Sample mode (S closed):**
- Capacitor charges to Vin rapidly (time constant = Ron × C, where Ron ≈ 50-500Ω for CMOS switch)
- Acquisition time: typically < 1μs for small C
- Output tracks input: Vout ≈ Vin

**Hold mode (S open):**
- Capacitor voltage held constant (isolated from input)
- Vout remains at the value of Vin at the moment S opened
- ADC now has a stable input to convert (without S&H, ADC would see changing Vin during multi-clock conversion)
- **Droop rate:** C slowly discharges through input impedance of Buffer2. For 10nF cap, 1pA leakage: droop = I/C = 10⁻¹²/10⁻⁸ = 100μV/s — acceptable for most applications.

**Applications:**
1. **ADC front-end**: All high-speed SAR and pipeline ADCs use on-chip S&H to freeze the input during the n-clock conversion process.
2. **Data acquisition systems**: Simultaneously sample multiple channels, then multiplex to single ADC.
3. **Peak detector**: Hold the peak value of a fast transient signal for slow measurement.
4. **Track-and-hold in PLLs**: Phase-locked loops use S&H to store the phase error signal during dead zones in the phase detector.
5. **Demodulation**: AM envelope detection and communications systems use S&H to reconstruct analog signals from sampled digital transmissions.

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q18b]: Compare binary weighted and R-2R ladder D/A Converters. [4 marks]

**Complete Solution:**

| Feature | Binary Weighted Resistor DAC | R-2R Ladder DAC |
|---------|------------------------------|-----------------|
| Number of resistor values | n distinct values: R, 2R, 4R, ..., 2^(n-1)R | Only 2 values: R and 2R |
| Resistor ratio range | 1:2^(n-1) (e.g., 1:32768 for 16-bit) | Maximum ratio 1:2 |
| Precision requirement | Very high — large spread makes matching difficult | Easier — only 2 values to match |
| Cost and complexity | High (custom resistors, laser trimmed) | Lower (standard resistor arrays) |
| Speed | Fast (direct weighted summing) | Moderate (ladder settles) |
| Suitable bits | Best for ≤ 8 bits | Preferred for 8-16 bits |
| Principle | Each bit drives a proportionally scaled current into virtual ground | Ladder network creates binary-weighted currents using identical node impedance |
| Scaling equation | Vout = -Vref×RF×Σ(Di/2^i × R) | Vout = -Vref×Σ(Di/2^i) |

**Conclusion:** For high-resolution (12-16 bit) DACs, R-2R ladder is strongly preferred because maintaining 1:65536 resistor ratio accuracy in binary-weighted design is impractical without laser trimming.

---

### PYQ 2 [May 2019, Q16b]: Compare active and passive filters. [4 marks]

**Complete Solution:**

| Feature | Passive Filter (RC, LC) | Active Filter (Op-Amp + RC) |
|---------|------------------------|------------------------------|
| Active components | No (resistors, capacitors, inductors only) | Yes (op-amp required, needs power supply) |
| Signal amplification | No (insertion loss — attenuates even in passband) | Yes (op-amp can provide gain) |
| Inductor required | Yes (for L-type filters) | No (eliminates inductors at audio frequencies) |
| Frequency range | DC to microwave (LC filters used at RF) | Best for DC to ~1MHz (op-amp bandwidth limits) |
| Loading effect | Dependent on source/load impedance | Low output impedance — easily cascaded |
| Adjustability | Harder to tune | Easy to tune (change R or C) |
| Cost | Low (no active devices) | Slightly higher (op-amp, power supply) |
| Size | Larger (inductors are bulky at audio freq) | Compact (no inductors) |
| Q achievable | Limited by coil resistance | High Q possible with feedback |
| Applications | Power supplies (50Hz ripple filter), RF matching networks | Audio crossover networks, anti-aliasing filters, biomedical instruments |

**At audio frequencies (20Hz-20kHz):** Active filters are universally preferred due to elimination of inductors (bulky, non-ideal at low frequencies) and ease of cascading.

**At RF (MHz+):** Passive LC filters or transmission line filters are preferred — op-amps cannot operate at these frequencies.

---

### PYQ 3 [May 2019, Q19b]: Sketch and explain the circuit of a monostable multivibrator using IC 555. [5 marks]

**Complete Solution:**

**Circuit:**
```
VCC ──┬──────────────── pin 8 (VCC)
      │
     [RA]
      │
      ├─── pin 7 (Discharge)
      │
      ├─── pin 6 (Threshold)
      │
      C
      │
     GND ─── pin 1 (GND)

pin 4 (Reset) → VCC (held high: inactive)
pin 5 (Control) → 0.01μF → GND (noise bypass)
pin 2 (Trigger) → trigger input (active LOW < 1/3 VCC)
pin 3 (Output) → Vout (HIGH during pulse)
```

**Operation:**

**Stable State (before trigger):**
- Internal flip-flop: Q = 0 → Output (pin 3) = LOW (0V)
- Discharge transistor (pin 7) is ON → C is held discharged (near 0V)
- Threshold comparator: C voltage (0V) < 2/3 VCC → no reset
- Trigger comparator: pin 2 > 1/3 VCC → no set

**Trigger Arrives (pin 2 goes below 1/3 VCC):**
1. Trigger comparator sets flip-flop: Q → 1
2. Output (pin 3) → HIGH (= VCC - Vsat ≈ VCC)
3. Discharge transistor turns OFF (pin 7 open)
4. Capacitor C begins charging through RA toward VCC

**Timing (Quasi-stable state):**
- C charges: Vc(t) = VCC(1 - e^(-t/RaC))
- When Vc reaches 2/3 VCC → Threshold comparator resets flip-flop: Q → 0
- Output (pin 3) → LOW
- Discharge transistor turns ON → C rapidly discharges to 0V through pin 7

**Pulse width calculation:**
```
At t = T: Vc = 2/3 VCC
VCC(1 - e^(-T/RAC)) = 2/3 VCC
1 - e^(-T/RAC) = 2/3
e^(-T/RAC) = 1/3
-T/RAC = ln(1/3) = -1.099
T = 1.099 × RA × C ≈ 1.1 × RA × C
```

**Design Example:**

For T = 5ms, C = 10μF:
```
RA = T/(1.1 × C) = 5×10⁻³/(1.1 × 10×10⁻⁶) = 5×10⁻³/1.1×10⁻⁵ = 454Ω → use 470Ω

Verification: T = 1.1 × 470 × 10×10⁻⁶ = 1.1 × 4.7×10⁻³ = 5.17ms ≈ 5ms ✓
```

**Key features of 555 monostable:**
- Re-triggering: If trigger appears before timing cycle completes, the timing continues from where it is (not retriggerable in standard configuration)
- Reset pin (pin 4): Immediately terminates the timing cycle when pulled LOW
- Timing accuracy: ±1% typical for good quality R and C components
- Applications: Debouncing, pulse-width generation, missing-pulse detector, frequency divider
