# Operational Amplifiers (Op-Amps)

## 1. Explanation

### Core Intuition: The Perfect Amplifier

An **Operational Amplifier (op-amp)** is a high-gain, direct-coupled differential amplifier with extremely high input impedance and very low output impedance. The name "operational" comes from its original purpose in analog computers: performing mathematical *operations* (addition, subtraction, integration, differentiation) on electrical signals.

The key insight is that when **negative feedback** is applied around an op-amp with very high open-loop gain (A_OL ≈ 10⁵ to 10⁶), the closed-loop behavior becomes determined almost entirely by the **external feedback network**, not the op-amp internals. This is the "virtual short" principle.

---

### Differential Amplifier — The Core Building Block

The first stage of every op-amp is a **differential amplifier** that amplifies the *difference* between two input signals while rejecting signals common to both inputs (noise).

**Circuit:**
```
               VCC (+12V)
                │
           [RC] [RC]   ← Equal, matched collector resistors
            │     │
            ├─────┤ ← Differential output Vo = Ad(V₁ - V₂)
       Q1-C     Q2-C
V1──B──Q1       Q2──B──V2
       Q1-E   Q2-E
            └──┬──┘ ← Emitters tied together at a common node
             [Iee] or [RE]   ← Constant current source (or RE)
               │
              VEE (-12V)
```

**Working — Differential Mode (V1 ≠ V2):**

Let V1 = +Vd/2 and V2 = -Vd/2 (pure differential signal):
- Q1 base is more positive → Q1 draws more IC → VCE1 drops → VC1 drops
- Q2 base is less positive → Q2 draws less IC → VCE2 rises → VC2 rises
- Differential output: Vod = VC2 - VC1 = Ad × (V1 - V2)
- Gain: Ad = gm × RC (differential mode voltage gain)

**Working — Common Mode (V1 = V2 = Vcm):**

Let V1 = V2 = Vcm (noise or interference signal, same on both):
- Both Q1 and Q2 receive identical signals → symmetric currents
- By matched symmetry: ΔVC1 = ΔVC2 (both change identically)
- Differential output: Vod = VC2 - VC1 = 0 (ideally, common signal cancels!)
- Common-mode gain: Ac → 0 for ideal matching
- With large RE (or constant current source): RE acts as a very high impedance to common-mode signals → forces even tighter rejection

**Why constant current source replaces RE?**

A resistor RE provides some common-mode rejection but its rejection ratio is limited by its finite impedance. A **constant current source** has near-infinite impedance — it forces Iee = constant regardless of common-mode voltage changes — giving maximum CMRR.

**Differential gain (Ad):**
```
Ad = gm × RC   (for differential output taken between both collectors)
Ad = gm × RC/2  (for single-ended output from one collector)

Where gm = IC/VT = IC/26mV at room temperature
```

**CMRR (Common Mode Rejection Ratio):**
```
CMRR = Ad/Ac

In dB: CMRR(dB) = 20 log₁₀(Ad/Ac)

For ideal op-amp: CMRR = ∞
For IC 741: CMRR(min) = 70dB, CMRR(typ) = 90dB
```

**CMRR depends on:**
1. Matching of Q1 and Q2 (hfe, VBE must be identical)
2. Matching of collector resistors RC
3. Quality of emitter current source (higher impedance → higher CMRR)
4. Layout symmetry (temperature matching)

**Application of high CMRR:**

In an ECG machine, the heart signal is ~1mV differential. The 50Hz mains hum appears equally on both leads (common-mode, ~50mV). A differential amplifier with 90dB CMRR:
```
Differential signal amplified: 1mV × 1000 = 1V (with Ad = 1000)
Common-mode hum at output: 50mV × Ac = 50mV × Ad/CMRR = 50mV × 1000/31623 = 1.58mV
SNR: 1V / 1.58mV = 633 → easily separable
```

---

### Op-Amp Characteristics — Ideal vs Practical (IC 741)

| Parameter | Ideal Op-Amp | IC 741 (Practical) | What it limits |
|-----------|-------------|---------------------|---------------|
| Open-loop gain AOL | ∞ | 200,000 (106dB) | Closed-loop accuracy |
| Input impedance Zin | ∞ Ω | 2 MΩ (differential) | Input loading |
| Output impedance Zout | 0 Ω | 75 Ω | Output current/loading |
| Bandwidth (GBW) | ∞ Hz | 1 MHz | High-frequency operation |
| CMRR | ∞ | 90 dB (typ), 70dB (min) | Noise rejection |
| Slew rate | ∞ V/μs | 0.5 V/μs | Large-signal speed |
| Input offset voltage Vio | 0 V | ±2 mV (max ±6mV) | DC accuracy |
| Input bias current IB | 0 A | 80 nA (typ), 500nA (max) | DC offset at output |
| Input offset current Iio | 0 A | 20 nA (typ), 200nA (max) | DC offset balance |
| Supply voltage range | Any | ±5V to ±18V | System voltage |
| Output voltage swing | ±∞ | ±(VCC - 1.5V) ≈ ±13V for ±15V supply | Dynamic range |
| Short-circuit protection | N/A | Yes (internal) | Fault protection |

**Open-Loop Gain (AOL):**

The gain without any feedback. For IC 741: AOL = 200,000 (at DC, 0Hz). This gain rolls off with frequency:
```
AOL(f) = AOL(0) / (1 + f/f3dB)

For 741: f3dB ≈ 5Hz (open-loop -3dB frequency)
AOL(0) = 200,000

The gain starts rolling off at just 5Hz! At 1MHz, gain = 1 (unity gain bandwidth).
```

**Gain-Bandwidth Product (GBW = fT = 1MHz for 741):**
```
GBW = AOL × f3dB = 200,000 × 5Hz = 1MHz = constant

Closed-loop bandwidth at a given gain:
f-3dB(closed-loop) = GBW / Af = 1MHz / Af

At Af = 1 (voltage follower): BW = 1MHz
At Af = 10: BW = 100kHz
At Af = 100: BW = 10kHz
At Af = 1000: BW = 1kHz
```

**Slew Rate (SR):**

The maximum rate at which the **output voltage can change**, regardless of input signal:
```
SR = |dVout/dt|_max

For IC 741: SR = 0.5 V/μs

Physical cause: The internal compensation capacitor (30pF in 741) can only be charged at a finite rate limited by the bias current of the input stage.
```

**Why slew rate limits large signals:**

The output of an op-amp slews when the input voltage change demands a rate of change that exceeds SR. For a sinusoidal output Vm×sin(ωt):
```
Maximum rate of change = dVout/dt|_max = ω × Vm (at zero crossing)

For no slew-rate distortion: ω × Vm ≤ SR
→ f ≤ SR / (2π × Vm)

Full-power bandwidth: fFP = SR / (2π × Vm)

For IC 741 with Vm = 10V:
fFP = 0.5×10⁶ / (2π × 10) = 7.96kHz

For Vm = 1V:
fFP = 0.5×10⁶ / (2π × 1) = 79.6kHz

Note: SR limits large-signal bandwidth; GBW limits small-signal bandwidth
```

**Slew rate vs GBW:**
- **GBW (small-signal bandwidth):** Applies for small amplitude signals where the output stays in the linear region. Determined by frequency compensation.
- **SR (large-signal rate):** Applies when the output voltage must change rapidly over a large voltage swing. Determined by available charging current for the compensation capacitor.

For IC 741 at Av = 1 (voltage follower, BW = 1MHz):
- A 1V peak sine wave at 1MHz: Required slope = 2π × 1MHz × 1 = 6.28 V/μs > 0.5 V/μs → **slew-rate limited even at 1MHz!**
- A 1mV peak sine wave at 1MHz: Required slope = 2π × 1MHz × 0.001 = 0.00628 V/μs < 0.5 V/μs → **not slew-rate limited (GBW is the limit)**

**Input Offset Voltage (Vio):**

The small differential voltage that must be applied between the inputs to make the output exactly zero. Caused by inherent mismatches in the differential pair transistors (unequal VBE, hfe, RC).

```
For IC 741: Vio = ±2mV (typ), ±6mV (max)

Effect on output: Vout(error) = Vio × (1 + Rf/R1)
For gain = 100: Vout(error) = ±2mV × 100 = ±200mV DC error!
```

**Correction:** Apply small voltage at offset-null pins (pins 1 and 5 of 741 with a 10kΩ potentiometer connected to the negative supply pin).

**Input Bias Current (IB):**

The average of the two input terminal currents (base currents of input differential pair BJTs):
```
IB = (IB+ + IB-) / 2

For IC 741: IB = 80nA (typ), 500nA (max)

Effect: Even with Vin = 0, bias current flows through feedback resistors → creates voltage offsets.
Error output: Vout(error) = IB × Rf (approximately, for inverting amp)
```

**Correction:** Add a compensation resistor Rcomp = R1 || Rf at the non-inverting (+) input. The equal bias current through Rcomp creates a compensating offset voltage that cancels the error from IB in the inverting path.

**Input Offset Current (Iio):**

The *difference* between the two input bias currents (caused by BJT mismatch):
```
Iio = |IB+ - IB-|

For IC 741: Iio = 20nA (typ), 200nA (max)

Note: Iio << IB typically. If compensation resistor is used, only Iio causes residual error.
Residual output error: Vout(error) = Iio × Rf
```

---

### The "Virtual Short" Principle — Complete Derivation

When negative feedback is applied to an op-amp with finite (very high) AOL:

```
Vout = AOL × (V+ - V-)   [open-loop equation]
Vout = AOL × Vd            [Vd = differential input]

Since AOL = 200,000 and Vout is bounded (±13V for ±15V supply):
|Vd| = |Vout|/AOL = 13/200,000 = 65μV ≈ 0

So: V+ ≈ V-  (the two inputs are essentially at the same potential)
```

This is called **"virtual short"** — the inputs appear shorted to each other in potential, but NOT in current (no current flows between them because the input impedance is still 2MΩ or higher).

**The Two Golden Rules of Op-Amp Analysis (for negative feedback circuits):**

1. **V+ = V-** (virtual short — the differential input voltage is driven to nearly zero by the feedback)
2. **I+ = I- = 0** (no current flows into either input terminal — ideal op-amp assumption)

These two rules are all you need to analyze any op-amp circuit with negative feedback.

---

### Op-Amp Applications

#### 1. Inverting Amplifier (Scale Changer)

**Circuit:**
```
         Rf
    ┌────┤├────────────────────── Vout
    │                │
Vin─┤ Rin ──── (−) ─┘
                (+)
                 │
                GND

Note: (+) input is grounded.
Resistor Rcomp = Rin || Rf at (+) input reduces offset error from IB.
```

**Derivation using virtual short:**

Step 1: V+ = GND = 0V. By virtual short: V- = V+ = 0V (V- is at "virtual ground").

Step 2: Current through Rin (into virtual ground):
```
I = Vin / Rin
```

Step 3: Since no current enters the op-amp (-) input, the entire current I flows through Rf:
```
Vout = V- - I × Rf = 0 - (Vin/Rin) × Rf = -(Rf/Rin) × Vin
```

**Result:**
```
Av = Vout/Vin = -Rf/Rin

Input impedance: Zin = Rin (input sees Rin to virtual ground)
Output impedance: Zout ≈ 0 (op-amp output)
Phase: 180° inversion
```

**Design:** Choose Rf and Rin to set gain magnitude. For gain = -10: Rf/Rin = 10, e.g., Rf = 100kΩ, Rin = 10kΩ.

---

#### 2. Sign Changer (Unity-Gain Inverter)

Special case of inverting amplifier with Rf = Rin:
```
Av = -Rf/Rin = -1

Vout = -Vin   (same amplitude, opposite polarity, 180° phase shift)
```

Use: Invert a signal's polarity without changing its amplitude. Common in analog computing, analog signal processing.

---

#### 3. Non-Inverting Amplifier

**Circuit:**
```
              Rf
    Vout ─────┤├──────── (−)
                    │
                   R1
                    │
                   GND

Vin ────────────── (+)
```

**Derivation:**

Step 1: V+ = Vin (input connects directly to + terminal).
Step 2: By virtual short: V- = V+ = Vin.
Step 3: V- is the junction of Rf and R1, forming a voltage divider from Vout to GND:
```
V- = Vout × R1/(R1 + Rf)
```

Step 4: Set V- = Vin:
```
Vin = Vout × R1/(R1 + Rf)
Vout/Vin = (R1 + Rf)/R1 = 1 + Rf/R1
```

**Result:**
```
Av = 1 + Rf/R1

Input impedance: Zin = AOL × (Rin of op-amp) → very large (100MΩ to GΩ)
Output impedance: Zout ≈ 0
Phase: 0° (non-inverting)
Minimum gain: 1 (when Rf = 0, R1 = ∞ → voltage follower)
```

---

#### 4. Voltage Follower (Buffer)

Special case of non-inverting amplifier with Rf = 0 (short), R1 = ∞ (open):
```
Av = 1 + 0/∞ = 1
Vout = Vin

Input impedance: Maximum (several GΩ with feedback)
Output impedance: Very low (< 1Ω)
```

**Use case:** Impedance buffer — connect a high-impedance source (e.g., pH electrode at 100MΩ) to a low-impedance load (amplifier at 10kΩ) without signal loss.

---

#### 5. Summing Amplifier (Inverting Adder)

**Circuit:**
```
              Rf
    ┌─────────┤├──────────────── Vout
    │                    │
V1 ─┤ R1 ─── (−) ────────┘
V2 ─┤ R2 ─── (+) = GND
V3 ─┤ R3
    │
   GND
```

**Derivation:**

V- is virtual ground (= 0V). Currents from all inputs flow into virtual ground:
```
I1 = V1/R1,  I2 = V2/R2,  I3 = V3/R3

Total current into V- node: I_total = I1 + I2 + I3

This total current flows through Rf:
Vout = -(I1 + I2 + I3) × Rf = -(V1×Rf/R1 + V2×Rf/R2 + V3×Rf/R3)
```

**Special case (R1 = R2 = R3 = Rf = R):**
```
Vout = -(V1 + V2 + V3)
```

**Equal gain, different gains:**
```
For V1 gain = -5, V2 gain = -3, V3 gain = -2 (with Rf = 10kΩ):
R1 = Rf/5 = 2kΩ
R2 = Rf/3 = 3.33kΩ ≈ 3.3kΩ
R3 = Rf/2 = 5kΩ

Vout = -(5V1 + 3V2 + 2V3)
```

---

#### 6. Subtractor (Difference Amplifier)

**Circuit:**
```
         R2
    ┌────┤├────────────────────── Vout
    │             │
V1 ─┤ R1 ──── (−)─┘
              (+)
               │
V2 ─┤ R3 ────┤├─── GND
              R4
```

**Derivation:**

Apply superposition. Use voltage divider for V+ and virtual short for V-:

**V+ (due to V2 through R3-R4 divider):**
```
V+ = V2 × R4/(R3 + R4)
```

**V- = V+ (virtual short):**
```
V- = V2 × R4/(R3 + R4)
```

**KCL at V- node:**
```
(V1 - V-)/R1 = (V- - Vout)/R2

Vout = V- × (1 + R2/R1) - V1 × (R2/R1)
     = V2 × [R4/(R3+R4)] × (1 + R2/R1) - V1 × (R2/R1)
```

**For equal resistors R1 = R2 = R3 = R4 = R:**
```
V+ = V2/2
Vout = (V2/2)(1 + 1) - V1 × 1 = V2 - V1

Av = Vout/(V2-V1) = 1   (unity gain differential)
```

**For R2/R1 = R4/R3 = K (general case):**
```
Vout = K × (V2 - V1)
```

**CMRR of subtractor:** Depends critically on resistor matching. If R2/R1 ≠ R4/R3, common-mode rejection degrades. Use precision (0.1%) resistors for good CMRR.

---

#### 7. Integrator (Miller Integrator)

**Circuit:**
```
              C
    ┌─────────||───────────────── Vout
    │                     │
Vin ─┤ R ──── (−) ─────────┘
              (+)
               │
              GND
```

**Derivation:**

V- = virtual ground = 0V.
Current through R: I = Vin/R
This current flows into/through C (no current into op-amp):
```
I = C × d(Vout)/dt

But I = Vin/R, and from the circuit: V- = 0, Vout is at op-amp output,
current direction: from V- through C to Vout → Vin/R = -C × d(Vout)/dt

∴ d(Vout)/dt = -Vin/(RC)

Integrating both sides:
Vout(t) = -(1/RC) × ∫₀ᵗ Vin(τ) dτ + Vout(0)
```

**Frequency domain (Laplace/jω):**
```
H(jω) = Vout/Vin = -1/(jωRC) = -Xc/R

At low frequency (ω → 0): |H| → ∞ (infinite gain for DC!)
At high frequency (ω → ∞): |H| → 0
```

**Input/output relationships:**

| Input waveform | Output waveform | Explanation |
|---------------|----------------|-------------|
| Square wave (±V) | Triangular wave (±slopes) | Integral of constant = ramp |
| Sine wave | Cosine wave (90° phase lead) | ∫sin = -cos |
| Triangle wave | Parabola | Integral of ramp = quadratic |

**Practical integrator (with RF across C):**

The ideal integrator has infinite DC gain → any tiny DC offset causes output to saturate. Solution: Add large resistor RF (= 10×R or more) in parallel with C:
```
This creates a low-pass filter with corner frequency fL = 1/(2π×RF×C)
For f >> fL: acts as ideal integrator
For f << fL: DC gain = -RF/R (finite, prevents saturation)

Choose RF ≥ 10R to maintain good integration over the desired frequency range.
```

**Integration formula:**
```
Vout = -(1/RC) × ∫Vin dt

Time constant: τ = RC

For square wave input ±V, period T:
Output triangular wave amplitude = V × T/(4RC)   [peak-to-peak = V×T/(2RC)]
```

---

#### 8. Differentiator

**Circuit:**
```
              R
    ┌─────────┤├──────────────── Vout
    │                    │
Vin ─┤ C ─── (−) ─────────┘
     ||       (+)
              │
             GND
```

**Derivation:**

V- = virtual ground = 0V.
Current through C: I = C × d(Vin)/dt
This current flows through R (no current into op-amp):
```
Vout = 0 - I × R = -RC × d(Vin)/dt
```

**Frequency domain:**
```
H(jω) = -jωRC

At low frequency: |H| → 0
At high frequency: |H| → ∞ (noise problem!)
```

**Input/output relationships:**

| Input waveform | Output waveform |
|---------------|----------------|
| Sine wave | Cosine wave (differentiation: d/dt sin = cos) |
| Triangle wave | Square wave |
| Square wave | Spikes/impulses at edges |

**Problem with ideal differentiator:** High-frequency noise is amplified without limit (gain increases with frequency). This makes the circuit practically useless without modification.

**Practical differentiator (with Rs in series with C):**
```
Add small resistor Rs (= R/10 typically) in series with C:

Modified gain: H(jω) = -jωRC / (1 + jωRsC)

This creates a pole at ωp = 1/(RsC), limiting the high-frequency gain to:
|H(ω >> ωp)| = R/Rs  (constant, doesn't blow up)

The circuit differentiates signals with frequency f < 1/(2πRsC)
and acts as a limited amplifier for higher frequencies.
```

---

#### 9. Schmitt Trigger (Comparator with Hysteresis)

**Non-Inverting Schmitt Trigger:**

**Circuit:**
```
Vin ──────────────── (+)
                       [Op-Amp] ──── Vout
                      (−) ─── GND

Positive feedback: Vout ──[Rf]── (+) input
                   GND  ──[R1]── (+) input (voltage divider)

V(+) = Vout × R1/(R1+Rf)   [when Vin = 0, from feedback divider]
```

Actually, the standard non-inverting Schmitt trigger:
- Vin applied to (+) through nothing
- Feedback: Vout divides through R1 and R2 back to (+)
- (-) input = GND

At any given moment:
```
V(+) = Vin × R2/(R1+R2) + Vout × R1/(R1+R2)   [superposition: Vin and Vout both drive (+)]
```

But in the simpler standard form (inverting Schmitt):

**Inverting Schmitt Trigger Circuit:**
```
Vin ──────────── (−)
                   [Op-Amp] ──── Vout
                  (+)
                   │
          Vout ─[R2]─┤─[R1]─ GND   ← feedback from Vout to (+)
                   V(+) = Vout × R1/(R1+R2)
```

**Threshold analysis:**

**Upper Threshold (UTP) — output switches from +Vsat to -Vsat:**

When output is at +Vsat:
```
V(+) = +Vsat × R1/(R1+R2)

Output switches when Vin rises to equal V(+):
UTP = +Vsat × R1/(R1+R2)
```

**Lower Threshold (LTP) — output switches from -Vsat to +Vsat:**

When output is at -Vsat:
```
V(+) = -Vsat × R1/(R1+R2) = LTP

Output switches when Vin falls to equal V(+):
LTP = -Vsat × R1/(R1+R2)
```

**Hysteresis:**
```
H = UTP - LTP = 2 × Vsat × R1/(R1+R2)

Design example: Vsat = 13V (for ±15V supply), desired H = 2V:
2 = 2 × 13 × R1/(R1+R2)
R1/(R1+R2) = 2/26 = 1/13
R2/R1 = 12 → choose R1 = 10kΩ, R2 = 120kΩ
```

**Transfer characteristic (output vs input):**
```
Vout
+Vsat ──────────────────────────────── (for Vin < UTP after being LOW)
       ↑ snaps here (at UTP)
       │
       │   HYSTERESIS WINDOW
       │
-Vsat ────────────────────────────────── (for Vin > LTP after being HIGH)
       ↑ snaps here (at LTP)
      LTP              UTP         Vin →
```

**Why hysteresis prevents noise chatter:**

Without hysteresis (simple comparator with one threshold), a noisy signal near the threshold causes rapid back-and-forth switching (chatter). With hysteresis, once the output switches at UTP, the threshold moves down to LTP — the noise must now swing an entire hysteresis window before causing another transition.

---

#### 10. Wien Bridge Oscillator using Op-Amp

**Circuit:**
```
                      Rf (= 2R1)
         ┌─────────────┤├──────────────────────────────────┐
         │                                                   │
        (−)                                                  │
    [Op-Amp] ── Vout ──── Series RC ──────────── (+) ──── Vout
        (+)           └── Parallel RC ──── GND
         │
        R1 (from (−) to GND)
```

**Working:**
- Wien bridge network (series R-C and parallel R-C between Vout and (+) input) provides positive feedback with 0° phase shift at f₀ = 1/(2πRC)
- At f₀, the Wien network passes exactly 1/3 of the output voltage back to (+) with 0° phase
- The negative feedback through Rf-R1 divider sets the closed-loop gain to exactly 3 (Rf = 2R1)
- Barkhausen: |Aβ| = 3 × (1/3) = 1 ✓ and phase = 0° ✓

**Design equations:**
```
Oscillation frequency: f₀ = 1/(2πRC)
Gain condition: Rf = 2R1   (for Av = 1 + Rf/R1 = 3)

Example: f₀ = 1kHz
Choose C = 0.01μF → R = 1/(2π × 1000 × 0.01×10⁻⁶) = 15.9kΩ ≈ 16kΩ
Choose R1 = 10kΩ → Rf = 20kΩ (or Rf = 22kΩ with thermistor NTC for amplitude stabilization)
```

**Amplitude stabilization:** Use a thermistor NTC in series with R1 (or in place of Rf). As oscillation amplitude grows → thermistor heats → resistance decreases (NTC) → gain decreases → amplitude stabilizes at a level where gain = 3 precisely.

---

## 2. Example

### Summing Amplifier Realization [May 2019, Q19a]

**Problem:** Realize the function Y(t) = 5V1 + 2V2 – 4V3 using op-amps.

**Solution:**

This requires gains of 5 and 2 (positive) for V1, V2 and gain of 4 (negative) for V3. We need two inverting stages to realize all positive signs for V1 and V2:

**Stage 1 — Inverting Summing Amplifier:**
```
Vout1 = -(5V1 + 2V2)

With Rf = 10kΩ:
R_V1 = Rf/5 = 10kΩ/5 = 2kΩ
R_V2 = Rf/2 = 10kΩ/2 = 5kΩ
```

**Stage 2 — Second Inverting Summing Amplifier (inverts Stage 1 output, adds -V3 term):**
```
Vout = -(Vout1 × gain1 + V3 × gain3)
     = -(-(5V1+2V2) × 1 + V3 × 4)   [choose gain1 = 1, gain3 = 4]
     = 5V1 + 2V2 - 4V3 ✓

With Rf2 = 4kΩ:
R_stage1 = Rf2/1 = 4kΩ   [for Stage 1 output with gain = 1]
R_V3 = Rf2/4 = 1kΩ       [for V3 with gain = 4]
```

**Component summary:**
- Stage 1: Rf = 10kΩ, R(V1) = 2kΩ, R(V2) = 5kΩ
- Stage 2: Rf = 4kΩ, R(Stage1) = 4kΩ, R(V3) = 1kΩ

---

## 3. Applications and Use Cases

1. **Summing amplifier in audio mixers:** Mixing multiple audio channels (guitar, vocals, bass) into a mono output. Each channel gain is set by its input resistor — the mixing engineer's volume faders.

2. **Integrator in analog computing and ADC:** Dual-slope ADC uses an op-amp integrator to convert analog voltage to a time interval (linear ramp), which is then digitized.

3. **Differentiator in signal edge detection:** Differentiators highlight sharp transitions — used in image processing (edge detection filters), motor control (detecting velocity from position sensors), and radar signal processing.

4. **Schmitt trigger in digital interfaces:** Every I²C, UART, USB receiver uses Schmitt trigger inputs to reject glitches and noise on the signal lines — specified by the logic threshold VIH and VIL with hysteresis.

5. **Differential amplifier in ECG/EEG machines:** Medical instrumentation amplifiers use cascaded differential stages (Instrumentation Amplifier = 3 op-amps) with CMRR > 100dB to extract μV-level bioelectric signals from the skin.

6. **Non-inverting amplifier in sensor signal conditioning:** Accelerometers, strain gauges, and temperature sensors output millivolt signals. A non-inverting amplifier with high input impedance buffers the sensor without loading it.

7. **Wien bridge oscillator in signal generators:** The HP 200A (1939), designed by Bill Hewlett (co-founder of HP), was the first Wien bridge oscillator in a commercial product. Today's function generators all derive from this principle.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: CMRR and Slew Rate [May 2019, Q17b]

**Problem:** Explain CMRR and Slew Rate. Give typical values for IC 741. [4 marks]

**CMRR:**

CMRR is the ability of the op-amp to reject signals common to both inputs (noise), while amplifying only the differential signal.

```
CMRR = Ad / Ac

where: Ad = differential gain (output per unit differential input)
       Ac = common-mode gain (output per unit common-mode input)

In dB: CMRR(dB) = 20 log(Ad/Ac)

For IC 741:
- Ad = 200,000 (open-loop DC)
- CMRR(typ) = 90dB → Ac = Ad/10^(90/20) = 200,000/31,623 = 6.3

Meaning: A common-mode signal is attenuated by 31,623× compared to a differential signal.
```

**Numerical significance:** A 1V common-mode hum appears as only 1/31,623 = 31.6μV at the output (referenced to input as common-mode error), while 1mV differential signal is fully amplified.

**Slew Rate:**

Maximum output voltage rate of change:
```
SR = |dVout/dt|_max = 0.5 V/μs for IC 741

If input demands faster rate of change than SR: output "slews" (changes linearly at SR rate, ignoring the input)

Full-power bandwidth: fFP = SR/(2π × Vm)

For Vm = 10V: fFP = 0.5×10⁶/(2π × 10) = 7.96kHz
For Vm = 1V:  fFP = 0.5×10⁶/(2π × 1)  = 79.6kHz
```

**Slew-rate distortion:** A high-frequency large-amplitude sine wave becomes a triangle wave at the output because the op-amp output simply ramps at SR, unable to follow the demanded slope.

---

### Example 2: Inverting and Non-Inverting Amplifier Design [May 2019, Q17a]

**Problem:** Derive the voltage gain of inverting and non-inverting amplifier using op-amp. [6 marks]

**Inverting Amplifier:**

```
Circuit: Vin → Rin → (−) → [Op-Amp] → Vout
                             (+) → GND
                Rf: from Vout back to (−)
```

**Derivation:**
1. V+ = 0V (grounded)
2. Virtual short: V- = V+ = 0V ("virtual ground")
3. Current through Rin: I = (Vin - 0)/Rin = Vin/Rin
4. KCL at V- node: I_Rin = I_Rf (since I into op-amp = 0)
5. Current through Rf: I = (0 - Vout)/Rf → Vout = -I × Rf

```
Vout = -(Vin/Rin) × Rf

Av(inverting) = Vout/Vin = -Rf/Rin
```

Negative sign = 180° phase inversion. Gain magnitude = Rf/Rin.

**Non-Inverting Amplifier:**

```
Circuit: Vin → (+) → [Op-Amp] → Vout
                      (−) ← R1 to GND, Rf to Vout
```

**Derivation:**
1. V+ = Vin (directly connected)
2. Virtual short: V- = V+ = Vin
3. V- is a voltage divider point: V- = Vout × R1/(R1+Rf)
4. Set V- = Vin:
   ```
   Vin = Vout × R1/(R1+Rf)
   Vout/Vin = (R1+Rf)/R1 = 1 + Rf/R1
   ```

```
Av(non-inverting) = 1 + Rf/R1
```

Always positive (0° phase). Minimum gain = 1 (voltage follower).

**Summary table:**

| Parameter | Inverting | Non-inverting |
|-----------|-----------|--------------|
| Gain | -Rf/Rin | 1 + Rf/R1 |
| Gain sign | Negative (inverts) | Positive |
| Min gain | No limit (< -1 for Rf > Rin) | 1 (always ≥ 1) |
| Zin | Rin | Very high (op-amp Zin × AOL) |
| Zout | ≈ 0 | ≈ 0 |
| Phase | 180° | 0° |

---

### Example 3: Integrator and Differentiator Waveforms [May 2019, Q18b]

**Problem:** Explain the op-amp integrator and differentiator with waveforms. Give the output for square wave input for both. [6 marks]

**Integrator:**

Circuit: R in series with (−) input, C as feedback from output to (−). (+) input grounded.

```
Transfer function: Vout = -(1/RC) × ∫Vin dt
```

**Square wave input → Triangular wave output:**

For a square wave of amplitude ±V and period T:
```
During positive half (Vin = +V, from 0 to T/2):
Vout(t) = Vout(0) - (V/RC) × t   [linearly decreasing ramp]

During negative half (Vin = -V, from T/2 to T):
Vout(t) = Vout(T/2) + (V/RC) × t   [linearly increasing ramp]
```

This produces a triangular wave. The amplitude of the triangle:
```
ΔVout = V × (T/2) / RC   [change in output per half-cycle]
```

**Waveforms:**
```
Vin (square):        +V ─────┐    ┌─────
                              │    │
                    -V        └────┘
                                    →t

Vout (triangular):
                    ╱╲    ╱╲    ╱╲
                   ╱  ╲  ╱  ╲  ╱  ╲
                         ↑
                    Amplitude = V×T/(4RC)
```

**Differentiator:**

Circuit: C in series with (−) input, R as feedback. (+) input grounded.

```
Vout = -RC × d(Vin)/dt
```

**Square wave input → Impulse/spike output:**

The derivative of a square wave is zero everywhere except at the edges (transitions), where it is theoretically infinite (impulse). In practice, spikes occur at the transitions:

```
Vin (square):        +V ─────┐    ┌─────
                              │    │
                    -V        └────┘

Vout (spikes):
                    ↑         ↑         ↑
                    │         │         │  (positive spikes at rising edges)
                    ─────────         ──────
                              ↓         ↓
                              │         │  (negative spikes at falling edges)
```

**Practical note:** In reality, the square wave has a finite rise time Tr, so the spikes have finite amplitude = 2V×RC/Tr and duration = Tr.

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q15a]: Draw and explain differential amplifier. [5 marks]

**Complete Solution:**

**Circuit:**
```
           VCC (+12V)
            │
       [RC] [RC]   ← Matched precision resistors
        │     │
        │     │ ← Differential output taken between collectors
   Q1-C     Q2-C
V1 ─B─Q1   Q2─B─ V2
   (NPN)   (NPN)
    Q1-E   Q2-E
       └──┬──┘   ← Emitters tied together
        [Iee]    ← Constant current source (replaces simple RE)
          │
        VEE (-12V)
```

**Operation:**

**Differential input (V1 ≠ V2):**

Let V1 = +1mV, V2 = 0V (pure differential signal):
- Q1 base more positive → Q1 IC increases → Q1 collector voltage (VC1) drops
- Q2 base less positive → Q2 IC decreases → Q2 collector voltage (VC2) rises
- Output Vo = VC2 - VC1 = Positive (large, amplified differential signal)

**Common-mode input (V1 = V2 = Vcm):**

Let V1 = V2 = 10mV (common-mode noise):
- Both Q1 and Q2 bases rise equally
- By perfect symmetry: ΔIC1 = ΔIC2 → ΔVC1 = ΔVC2
- Differential output: VC2 - VC1 = 0 (noise cancelled!)

**Key parameters:**
```
Differential gain: Ad = gm × RC   [double-ended output]
                 = gm × RC/2   [single-ended output]

Common-mode gain: Ac ≈ RC/(2×RE_source)
(smaller RE_source = constant current source → Ac → 0)

CMRR = Ad/Ac = gm × RC × 2×RE_source / RC = 2×gm×RE_source

For constant current source: RE_source → ∞ → CMRR → ∞ (ideal)
```

**Significance:** The differential amplifier is the input stage of every op-amp, ECG machine, instrumentation amplifier, and analog-to-digital converter front end.

---

### PYQ 2 [May 2019, Q16a]: Derive gain of inverting and non-inverting op-amp. [6 marks]

**Complete Solution:**

*(Full derivation given in Solved Example 2 — restated self-contained here)*

**Virtual short principle:** AOL = 200,000; Vout = AOL × (V+ - V-). For Vout bounded (±13V): V+ - V- = 13/200,000 = 65μV ≈ 0 → V+ ≈ V-.

**Two golden rules:**
1. V+ = V- (virtual short)
2. I+ = I- = 0 (no current into inputs)

**Inverting Amplifier (Av = -Rf/Rin):**

```
Step 1: V+ = 0 → V- = 0 (virtual ground)
Step 2: I_Rin = Vin/Rin (current from Vin to virtual ground through Rin)
Step 3: KCL: I_Rin = I_Rf (same current, since I_op-amp = 0)
Step 4: Vout = 0 - I_Rf × Rf = -(Vin/Rin) × Rf

→ Av = Vout/Vin = -Rf/Rin  ✓
```

**Non-Inverting Amplifier (Av = 1 + Rf/R1):**

```
Step 1: V+ = Vin (directly connected)
Step 2: V- = V+ = Vin (virtual short)
Step 3: V- = Vout × R1/(R1+Rf)  [voltage divider at output]
Step 4: Vin = Vout × R1/(R1+Rf)
→ Vout = Vin × (R1+Rf)/R1 = Vin × (1 + Rf/R1)

→ Av = 1 + Rf/R1  ✓
```

---

### PYQ 3 [May 2019, Q19b]: Draw the circuit of an op-amp integrator and differentiator. Explain with waveforms the output when a square wave is applied. [6 marks]

**Complete Solution:**

*(Full circuit, derivation, and waveforms given in Solved Example 3 — restated self-contained here)*

**Integrator Circuit:**
```
         C (feedback capacitor)
    ┌────||──────────────────── Vout
    │                  │
Vin ─┤ R ──── (−) ─────┘   ← RC is the integration time constant
              (+)
               │
              GND

Output: Vout = -(1/RC) × ∫Vin dt
```

For square wave ±V input: output is triangular wave (ramps linearly up/down).

**Differentiator Circuit:**
```
         R (feedback resistor)
    ┌────┤├──────────────────── Vout
    │                  │
Vin ─┤ C ──── (−) ─────┘   ← RC is the differentiation time constant
     ||       (+)
              │
             GND

Output: Vout = -RC × d(Vin)/dt
```

For square wave input: output is positive spikes at rising edges, negative spikes at falling edges (derivative of step function = impulse).

**Waveforms (see Solved Example 3 above for detailed waveform diagrams).**
