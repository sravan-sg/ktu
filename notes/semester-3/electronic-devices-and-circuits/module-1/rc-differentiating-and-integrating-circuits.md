# RC Differentiating and Integrating Circuits

## 1. Explanation

### The Core Intuition

An RC circuit is the simplest time-domain signal processing network. The key insight is this: **a capacitor is a frequency-sensitive element** — it offers low impedance to high-frequency signals (XC = 1/2πfC is small) and high impedance to low frequencies. By controlling which element (R or C) we measure the output voltage across, we fundamentally change the circuit's mathematical relationship between input and output.

**Why does this matter?** Because differentiation and integration are the two foundational operations in calculus — and RC circuits perform them *electronically*, in real time, on analog waveforms. This is the hardware implementation of the mathematical operators d/dt and ∫dt.

### RC Differentiating Circuit

**Configuration:** Output taken across the **resistor R**.

```
       C
Vin ───||───┬─── Vout
            │
            R
            │
           GND
```

**Mathematical Analysis:**

The voltage across the resistor is:
```
Vout = i(t) × R
```

The current through the series RC circuit:
```
i(t) = C × d(Vin)/dt
```

Therefore:
```
Vout = RC × d(Vin)/dt
```

This is a **true mathematical differentiator** when the time constant τ = RC << T (period of input signal), specifically when τ < T/10.

**Physical Interpretation:**
- When input changes rapidly → large d(Vin)/dt → large Vout (large current spike through C and R)
- When input is constant → d(Vin)/dt = 0 → Vout = 0 (capacitor blocks DC)
- The circuit responds to the **rate of change** of the input, not its absolute value

**Frequency Domain:** The transfer function is:
```
H(f) = Vout/Vin = jωRC / (1 + jωRC)
```
At high frequencies (ω >> 1/RC): |H(f)| → 1 (passes high frequencies)
At low frequencies (ω << 1/RC): |H(f)| → ωRC → 0 (blocks low frequencies)

This makes the differentiator essentially a **high-pass filter**.

### RC Integrating Circuit

**Configuration:** Output taken across the **capacitor C**.

```
       R
Vin ───┤├───┬─── Vout
            │
            C
            │
           GND
```

**Mathematical Analysis:**

The voltage across the capacitor:
```
Vout = (1/C) × ∫i(t)dt
```

For the series RC circuit where R >> XC (i.e., τ >> T):
```
i(t) ≈ Vin/R
```

Therefore:
```
Vout = (1/RC) × ∫Vin dt
```

This is a **true mathematical integrator** when τ = RC >> T, specifically τ > 10T.

**Physical Interpretation:**
- When τ is very large, the capacitor charges very slowly — it accumulates charge (integrates current over time)
- The output is proportional to the *area under the input curve* up to time t
- The circuit responds to the **accumulation** of the input signal over time

**Frequency Domain:** The transfer function is:
```
H(f) = Vout/Vin = 1 / (1 + jωRC)
```
At low frequencies (ω << 1/RC): |H(f)| → 1 (passes low frequencies)
At high frequencies (ω >> 1/RC): |H(f)| → 1/ωRC → 0 (blocks high frequencies)

This makes the integrator essentially a **low-pass filter**.

### The Fundamental Trade-off

| Property | Differentiator (output across R) | Integrator (output across C) |
|----------|----------------------------------|-------------------------------|
| Time constant condition | τ << T (RC << T) | τ >> T (RC >> T) |
| Mathematical operation | d(Vin)/dt | (1/RC)∫Vin dt |
| Filter behaviour | High-pass | Low-pass |
| Output magnitude | Small (τ small → R small → Vout small) | Large (τ large → slow charging) |
| Noise sensitivity | High (amplifies noise = high-freq changes) | Low (averages/smooths noise) |

---

## 2. Example — Square Wave Input Response

### Differentiator with Square Wave Input

**Input:** Square wave with amplitude 5V, period T = 1ms
**Circuit:** R = 100Ω, C = 0.1μF → τ = RC = 100 × 0.1×10⁻⁶ = 10μs
**Condition check:** τ = 10μs << T/2 = 500μs ✓ (good differentiator)

```
Input:
     5V ┌───────┐       ┌───────┐
        │       │       │       │
  0V ───┘       └───────┘       └───
        
Output (ideal differentiation):
        ↑ (positive spike at rising edge)
  0V ───┬───────────────┬──────────
        ↓ (negative spike at falling edge)
```

**Real output (exponential spikes):**
- At rising edge (t=0⁺): Vout jumps to 5V then decays exponentially: Vout(t) = 5e^(-t/10μs) V
- At falling edge: Vout jumps to -5V then returns to 0

**Waveform Conversions:**
- Square wave → Spikes/pulses (differentiator)
- Triangle wave → Square wave (differentiator, since d/dt of linear ramp = constant)

### Integrator with Square Wave Input

**Input:** Square wave with amplitude 5V, period T = 1ms
**Circuit:** R = 100kΩ, C = 10μF → τ = RC = 100×10³ × 10×10⁻⁶ = 1s
**Condition check:** τ = 1s >> T = 1ms ✓ (good integrator)

**Output:** Since ∫(constant A)dt = A×t, the output during the positive half cycle is:
```
Vout(t) = (Vin/RC) × t = (5/1) × t = 5t   [very slow linear ramp]
```

The output is approximately a **triangle wave** (since the ramp barely starts before the input switches polarity).

**Waveform Conversions:**
- Square wave → Triangle wave (integrator)
- Triangle wave → Sine-like wave (integrator)

---

## 3. Applications and Use Cases

### Real-World Applications of RC Differentiators

1. **Edge Detection Circuits**: In digital electronics, differentiators generate narrow trigger pulses from the rising/falling edges of clock signals. Used in flip-flop triggering and one-shot (monostable) circuits.

2. **Frequency Discrimination**: In FM demodulators, differentiators help extract the instantaneous frequency deviation from a modulated signal.

3. **Spike Noise Generation for Testing**: Controlled spike generation for testing circuit response to transients.

4. **Leading-edge Sharpening**: In pulse communication systems, differentiators sharpen the leading edges of pulses to improve timing accuracy.

### Real-World Applications of RC Integrators

1. **Averaging/Smoothing Filters**: RC integrators are the basis of low-pass RC filters used in audio applications (tone controls), power supply ripple filters, and sensor signal conditioning.

2. **Sweep Circuit Generation**: Integrators generate the linear voltage ramp (sawtooth wave) used in CRT display horizontal sweep, oscilloscope sweep circuits, and A/D converters.

3. **Signal Averaging**: In measurement systems, integrators compute the average of a noisy signal over time (temporal averaging), improving SNR.

4. **Analog Computing**: Before digital computers, RC integrators were fundamental building blocks of analog computers solving differential equations in real-time (missile guidance, aircraft flight control).

5. **Phase-Locked Loops (PLLs)**: The loop filter in a PLL is an integrator (or low-pass filter) that accumulates phase error over time to drive the VCO.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Differentiator Output for Square Wave Input [KTU Style]

**Problem:** A square wave of frequency 2 kHz and amplitude 10V peak is applied to an RC differentiating circuit with R = 1 kΩ and C = 0.01 μF. Determine:
(a) The time constant τ
(b) Whether the circuit acts as a good differentiator
(c) The peak output voltage and decay

**Solution:**

**(a) Time constant:**
```
τ = RC = 1×10³ × 0.01×10⁻⁶ = 10⁻⁵ s = 10 μs
```

**(b) Period of input:**
```
T = 1/f = 1/2000 = 500 μs
Half period = 250 μs
```

**Condition for good differentiator:** τ << T/2
```
10 μs << 250 μs ✓
```
Ratio: τ/(T/2) = 10/250 = 0.04 = 4% — excellent differentiator.

**(c) Peak output and decay:**

At the rising edge of the square wave, the capacitor appears as a short circuit momentarily. The input voltage appears across R:
```
Vout(peak) = +Vin = +10V  (at rising edge)
```

The output then decays exponentially:
```
Vout(t) = 10 × e^(-t/10μs)  V

At t = τ = 10μs:   Vout = 10 × e^(-1) = 3.68V
At t = 2τ = 20μs:  Vout = 10 × e^(-2) = 1.35V
At t = 5τ = 50μs:  Vout = 10 × e^(-5) = 0.067V ≈ 0V (fully decayed)
```

At falling edge (input drops to 0V):
```
Vout(peak) = -10V
Then decays: Vout(t) = -10 × e^(-t/10μs)
```

**Output:** Sharp positive and negative spikes of ±10V, decaying to zero in ~50μs (5τ), well within the 250μs half-period.

---

### Example 2: Integrator Output Waveform Calculation [KTU Style]

**Problem:** A square wave of amplitude ±5V and frequency 500 Hz is applied to an RC integrating circuit with R = 100 kΩ and C = 10 μF. 
(a) Find the time constant τ.
(b) Show that the circuit acts as a good integrator.
(c) Determine the output waveform and sketch it.

**Solution:**

**(a) Time constant:**
```
τ = RC = 100×10³ × 10×10⁻⁶ = 1 s
```

**(b) Period of input:**
```
T = 1/500 = 2 ms
Half period = 1 ms
```

**Condition for good integrator:** τ >> T/2
```
1s >> 1ms ✓
```
Ratio: τ/(T/2) = 1000/1 = 1000 — excellent integrator.

**(c) Output waveform:**

During positive half cycle (0 to T/2 = 1ms), Vin = +5V:
```
Vout(t) = Vin/(RC) × t = 5/1 × t = 5t V

At end of half cycle (t = 1ms):
Vout_max = 5 × 1×10⁻³ = 0.005V = 5mV
```

During negative half cycle (T/2 to T), Vin = -5V:
```
Starting from +5mV, discharging linearly:
Vout decreases at rate = -5/1 = -5 V/s
Change over 1ms = -5 × 1×10⁻³ = -5mV
Final value: 5mV - 5mV = 0mV (symmetric)
```

**Output:** Triangle wave with amplitude ±2.5mV (symmetric about zero), frequency 500Hz.

Note: The amplitude is massively reduced (5V input → 5mV output) due to the large τ — this is expected for an integrator operating far from its natural frequency.

---

### Example 3: Waveform Conversion — Triangle to Sine Approximation

**Problem:** Explain with waveforms how a triangle wave can be converted to a more sinusoidal output using an RC integrating circuit. If the triangle wave has amplitude 8V and frequency 1kHz, specify appropriate R and C values.

**Solution:**

**Wave conversion principle:**

The mathematical integration of a triangle wave (which is a piecewise linear function consisting of alternating positive and negative ramps) produces a parabolic output. A sum of parabolic segments approximates a sinusoid more closely than the triangle itself.

For good waveform shaping (rather than pure integration), we need moderate τ:
```
Condition: τ ≈ T/2π to T (moderately larger than period)
```

**Component selection:**
```
T = 1/f = 1/1000 = 1ms
Target τ ≈ T = 1ms (moderate integrator)

Choose: R = 10kΩ, C = 0.1μF
τ = RC = 10×10³ × 0.1×10⁻⁶ = 1ms ✓
```

**Output Analysis:**

During positive ramp of triangle (slope = +8V per 0.5ms = 16,000 V/s):
```
Vout = (1/RC) × ∫Vin dt = (1/10⁻³) × ∫(16000t) dt
     = 10³ × 8000t²   [parabolic curve, concave up]
```

The output transitions smoothly between positive and negative peaks in a rounded, approximately sinusoidal manner.

**Output waveform:** Rounded triangle (approaching sine wave) at same frequency (1kHz), with reduced amplitude due to RC attenuation.

---

## 5. Previous Year Questions and Solutions

### PYQ 1: Differentiate between RC differentiator and RC integrator. [3 marks]

**Complete Solution:**

| Parameter | RC Differentiator | RC Integrator |
|-----------|-------------------|---------------|
| Output voltage taken across | Resistor R | Capacitor C |
| Time constant condition | τ = RC << T | τ = RC >> T |
| Mathematical operation performed | Vout = RC × d(Vin)/dt | Vout = (1/RC) × ∫Vin dt |
| Frequency response type | High-pass filter | Low-pass filter |
| Square wave → output | Spikes/pulses | Triangle wave |
| Triangle wave → output | Square wave | Rounded/sine-like wave |
| Primary use | Edge detection, pulse sharpening | Waveform smoothing, averaging |

**Key insight:** The differentiator and integrator are duals of each other — same RC components, only the output node changes, producing mathematically inverse operations.

---

### PYQ 2: Draw the circuit of an RC differentiating circuit and derive the condition for it to work as a good differentiator. [9 marks]

**Complete Solution:**

**Circuit Diagram:**
```
         C (0.01μF)
Vin ─────||──────┬─────── Vout
                 │
                 R (1kΩ)
                 │
                GND
```

**Derivation:**

Applying KVL around the series RC loop:
```
Vin = Vc + VR = (Q/C) + iR

Where i = dQ/dt = C × d(Vc)/dt
```

The output is the voltage across R:
```
Vout = VR = i × R = RC × d(Vc)/dt
```

But Vc = Vin - Vout, so:
```
Vout = RC × d(Vin - Vout)/dt
Vout = RC × d(Vin)/dt - RC × d(Vout)/dt
```

For the circuit to be a **pure differentiator**, the term RC × d(Vout)/dt must be negligible compared to RC × d(Vin)/dt.

This requires that Vout << Vin at all times, which means the voltage drop across C must be much larger than across R:
```
Vc >> VR
(1/C)∫i dt >> iR
```

This is satisfied when **XC >> R** at the signal frequency, i.e.:
```
1/(2πfC) >> R
2πfRC << 1
2πτ/T << 1
τ << T/(2π) ≈ T/6.28
```

**Practical rule:** τ ≤ T/10 (time constant one-tenth of the period)

**Under this condition:**
```
Vc ≈ Vin  (capacitor voltage ≈ input voltage)
i = C × d(Vin)/dt
Vout = i × R = RC × d(Vin)/dt  ✓
```

The output is truly proportional to the derivative of the input.

**Conclusion:** For a good RC differentiator:
- τ = RC should be ≤ T/10 where T is the period of the input signal
- The output is a differentiated version: Vout = τ × (d Vin/dt)
- The circuit behaves as a high-pass filter with cutoff fc = 1/(2πRC)

---

### PYQ 3: For an RC integrating circuit with R = 470kΩ and C = 0.02μF, find the output if the input is a 100Hz square wave of 12V amplitude. [9 marks]

**Complete Solution:**

**Given:**
- R = 470 kΩ = 470 × 10³ Ω
- C = 0.02 μF = 0.02 × 10⁻⁶ F
- f = 100 Hz, Vin = 12V (square wave, assume ±6V symmetric or 0 to 12V — using 0 to 12V)

**Step 1: Calculate time constant:**
```
τ = RC = 470×10³ × 0.02×10⁻⁶
τ = 9.4 × 10⁻³ s = 9.4 ms
```

**Step 2: Calculate period of input:**
```
T = 1/f = 1/100 = 10 ms
Half period T/2 = 5 ms
```

**Step 3: Check integrator condition:**
```
τ/( T/2) = 9.4/5 = 1.88
```

Since τ ≈ T/2 (ratio ~2), this is a **moderate integrator**, not a perfect one. The output will be an exponential rather than a perfect linear ramp.

**Step 4: Charging analysis (positive half cycle, 0 to 5ms):**

Starting from 0V (assuming steady state reached), capacitor charges toward 12V:
```
Vout(t) = Vin × (1 - e^(-t/τ)) = 12 × (1 - e^(-t/9.4ms))
```

At end of positive half cycle (t = 5ms):
```
Vout(5ms) = 12 × (1 - e^(-5/9.4))
           = 12 × (1 - e^(-0.532))
           = 12 × (1 - 0.587)
           = 12 × 0.413
           = 4.96V ≈ 5V
```

**Step 5: Discharging analysis (negative half cycle, 5 to 10ms):**

Starting from 5V, input drops to 0V, capacitor discharges:
```
Vout(t) = 5 × e^(-(t-5ms)/9.4ms)
```

At end of negative half cycle (t = 10ms, i.e., t-5ms = 5ms):
```
Vout(10ms) = 5 × e^(-5/9.4) = 5 × 0.587 = 2.93V
```

**Output characteristics:**
- Output is an **exponential wave** (not a perfect triangle) oscillating between approximately 0V and 5V
- The circuit is not a perfect integrator (τ ≈ T/2, not τ >> T)
- For perfect integration, τ should be >> 10ms, e.g., R = 4.7MΩ, C = 0.02μF → τ = 94ms
