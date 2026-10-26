# Oscillators and Multivibrators

## 1. Explanation

### What is an Oscillator? — Core Intuition

An oscillator is a **self-sustaining signal generator** — it produces a periodic waveform (sinusoidal or non-sinusoidal) from a DC power supply, without any AC input signal.

**The fundamental paradox:** How can a circuit sustain oscillations without an external signal?

**Answer:** Small amounts of electrical noise (present in every circuit due to thermal agitation of electrons) contain energy at all frequencies. A circuit with **positive feedback** selectively amplifies noise at one specific frequency f₀, grows until limited by nonlinearity, and sustains itself at that frequency.

**Two key requirements:**
1. **Energy source:** DC power supply (VCC, VDD)
2. **Frequency selection:** A frequency-selective network (RC, LC, or crystal) that allows only f₀ to build up

### Barkhausen Criterion — The Mathematics of Oscillation

**General feedback amplifier model:**

```
        +───[A(jω)]───────── Vout
Vin ──► Σ              │
        -◄─[β(jω)]────┘
```

For an oscillator: Vin = 0, but circuit sustains Vout ≠ 0 due to noise bootstrapping.

**Loop gain condition:**

At the oscillation frequency f₀, the signal must return to its starting point with the same amplitude AND phase:

```
A(jω₀) × β(jω₀) = 1 + j0

This requires:
1. |A × β| = 1        (magnitude condition)
2. ∠(A × β) = 0°      (phase condition — net phase = 0° or 360°)
```

**Physical interpretation:**
- **|Aβ| < 1:** Each trip around the loop, signal loses energy → oscillations die out (damped)
- **|Aβ| > 1:** Signal grows each trip → amplitude increases until amplifier saturates (clips) and effective gain drops to |Aβ| = 1
- **|Aβ| = 1:** Signal reproduces itself exactly every trip → sustained steady oscillation ✓

**Start-up condition:** Practical oscillators are designed with initial |Aβ| > 1 so that oscillations build up from noise. As amplitude grows, the amplifier enters mild saturation → effective gain decreases → eventually |Aβ| → 1 at the desired amplitude.

**Amplitude stabilization mechanisms:**
- **Thermistor or tungsten lamp** (Wien bridge): Resistance increases with temperature → feedback ratio decreases as amplitude grows → limits gain to exactly 3
- **Automatic Gain Control (AGC) with FET:** FET in feedback path, VGS controlled by rectified Vout → gain adjusts automatically
- **Diode clipping** (crude): Diodes clamp the amplitude but add harmonic distortion

---

### RC Phase-Shift Oscillator

**Principle:** A single BJT CE amplifier provides 180° phase shift from base to collector. An RC ladder network provides the remaining 180° phase shift required for positive feedback (total: 360° = 0°).

**Why 180° from RC ladder?**

A single RC section provides maximum 90° phase shift (at very high frequency, output lags input by 90°). To get exactly 180° at a specific frequency, we need a minimum of **3 RC sections** (each contributes 60° at the oscillation frequency).

**Circuit:**
```
             VCC
              │
            [RC]
              │ Collector
           [NPN BJT]
              │ Base ◄─────────────────── feedback (from output)
              │ Emitter ── GND
              │
         [CE bypass capacitor]
              │
             GND

Three-section RC feedback network:
Vout ──[R]──┬──[R]──┬──[R]──┬─── Back to Base
            [C]    [C]    [C]
             │      │      │
            GND    GND    GND
```

**Transfer function of 3-section RC ladder:**

Each section: T(jω) = (jωRC) / (1 + jωRC) — this is a high-pass filter section.

For three identical sections in a ladder (with loading between stages):
```
β(jω) = [−1] / [1 - 5/(ω²R²C²) + j(6ωRC - 1/(ω³R³C³)) × ...  ]
```

At the oscillation frequency, the imaginary part must be zero:
```
Setting Im[β] = 0 → at ω₀:

ω₀ = 1/(RC√6)   →   f₀ = 1/(2π × RC × √6)

Note: The '√6' factor distinguishes this from Wien bridge (f₀ = 1/2πRC)
```

**Feedback fraction at f₀:**
```
|β| at ω₀ = 1/29

For |Aβ| = 1: |A| = 29

The BJT CE amplifier must have |Av| ≥ 29 for oscillation to sustain.
```

**Key design formulas:**
```
f₀ = 1 / (2π√6 × RC) = 0.065 / RC

Minimum gain required: A ≥ 29
This means: gm × RC ≥ 29 → IC × RC/VT ≥ 29

For RC = 10kΩ, R (phase-shift) = 10kΩ, C = 0.01μF:
f₀ = 1/(2π√6 × 10⁴ × 0.01×10⁻⁶) = 1/(2π × 2.449 × 10⁻⁴) = 650Hz
```

**Advantages:** Simple circuit, low cost, no inductors. Sinusoidal output (low distortion with proper gain control).

**Disadvantages:** Difficult to vary frequency (would need 3 ganged capacitors/resistors); minimum gain requirement (≥29) is higher than Wien bridge (≥3); less frequency stable than LC or crystal.

---

### Wien Bridge Oscillator — Complete Analysis

**Circuit (op-amp version):**
```
                  Rf
        ┌─────────┤├──────────────────────┐
        │                                  │
        │    R1                            │
        │ ───┤├── (-) ──────[Op-Amp]────── Vout
        │         (+)                      │
        │          │                       │
        │       Wien network:              │
        │    Vout──[R]──┬──[C]── to (+)  │
        │               │                  │
        │              [C] [R] in parallel │
        │               │                  │
        │              GND                 │
        └──────────────────────────────────┘
```

**BJT version:** Two-stage (each stage provides 180° → total 360°) with Wien network.

**Wien bridge feedback network — Transfer function derivation:**

```
The feedback network consists of:
Series arm: Z1 = R + 1/(jωC) = (jωRC + 1)/(jωC)
Parallel arm: Z2 = R || (1/jωC) = R/(1 + jωRC)

β = Z2 / (Z1 + Z2)

Let x = ωRC:
β = [R/(1+jx)] / [(1+jx)/jxC×(1/jω) + R/(1+jx)]

After simplification:
β = jx / (3 + jx - j/x + ... )  → At ω₀ = 1/RC (x=1):
β = j1 / (3 + j - j) = 1/3 ∠0°
```

So at exactly ω₀ = 1/(RC):
- β = 1/3 (no imaginary part → zero phase shift)
- The network passes 1/3 of the output back to the input with 0° phase shift

**For the phase condition:** Total loop phase must be 0°.

With op-amp inverting configuration (180° phase): one more 180° from RC feedback won't work — use **non-inverting** with β = 1/3 at 0°, and inverting negative feedback for gain control.

```
Actually: Op-amp non-inverting configuration:
- Output of op-amp (non-inverting) → through Wien network → back to (+) input [positive feedback]
- Resistors Rf, R1 → negative feedback to (-) input [negative feedback]

For oscillation: β(Wien) × A = 1
Since A = 1 + Rf/R1 (non-inverting gain)
And β = 1/3 at f₀:
(1 + Rf/R1) × (1/3) = 1 → 1 + Rf/R1 = 3 → Rf = 2R1
```

**Oscillation frequency:**
```
f₀ = 1/(2πRC)

Design example: f₀ = 1kHz
Choose C = 0.01μF:
R = 1/(2π × 1000 × 0.01×10⁻⁶) = 1/(2π×10⁻⁵) = 15.9kΩ → use 16kΩ or 15kΩ + trimmer
Gain: Rf = 2R1; choose R1 = 10kΩ, Rf = 20kΩ
```

**Amplitude stabilization (practical):**

At start-up, set Rf/R1 slightly > 2 (e.g., Rf = 22kΩ, R1 = 10kΩ → gain = 3.2 > 3). Oscillation builds up. A thermistor NTC (negative temperature coefficient) in series with R1: as Vout amplitude increases → thermistor dissipates more → resistance drops → gain approaches 3 → amplitude stabilizes.

**Tunable Wien bridge:** Use a twin-gang potentiometer for both R values simultaneously (ensuring R1 = R2 always), and a ganged capacitor switch for frequency range selection.

---

### Hartley Oscillator — Complete Analysis

**Circuit (Colpitts-Hartley principle):**

```
             VCC
              │
            [RFC] ← RF Choke (high impedance at RF, low DC resistance)
              │
         ────Collector────
        │    [NPN BJT]    │
        │    ────Base─────┤ ← feedback tap on L
        │    ────Emitter──┤
        │                  │
       [C] bypass to GND  │
                           │
              ┌──────── L1 ─┐ (total inductor)
              │  tap        │
              └──────── L2 ─┘
              │              │
              │             [C] (tuning)
              │              │
             GND            GND
```

**Frequency determination:**
```
f₀ = 1 / (2π√(L_total × C))

L_total = L1 + L2 + 2M   [if magnetically coupled, M = mutual inductance]
L_total = L1 + L2         [if no coupling, just a tapped inductor]
```

**Phase analysis:**
- CE BJT: collector is 180° out of phase with base
- The tapped inductor: L2 is 180° out of phase with L1 (they are in the same wound coil — voltages at opposite ends of a center-tapped inductor are 180° apart)
- Total: 180° + 180° = 360° = 0° → positive feedback ✓

**Feedback fraction:**
```
β = VL2 / V(L1+L2) = L2/L_total   [for Colpitts: use capacitors as feedback divider]

For Barkhausen: A × β ≥ 1
gm × RLC × (L2/Ltotal) ≥ 1
```

**Variable frequency tuning:**

The capacitor C is a variable capacitor (tuning capacitor). Changing C changes f₀:
```
f₀ = 1/(2π√(L×C))

C changes → f₀ changes → tunable oscillator

AM radio tuner: L = fixed; C varies from ~10pF to 400pF
f₀ range = 1/(2π) × [1/√(L×C_max) to 1/√(L×C_min)]
         = 540kHz to 1600kHz (AM broadcast band)
```

---

### Colpitts Oscillator

**Principle:** Similar to Hartley but uses a **capacitive voltage divider** instead of an inductive tap for feedback. The tank circuit consists of a single inductor L and two capacitors C1, C2.

**Circuit:**
```
             VCC
              │
            [RFC]
              │
         ────Collector────
        │    [NPN BJT]    │
        │                  │
        └── Emitter ──── L ──── GND (inductor from emitter to GND)
             │
           Base ◄── feedback from junction of C1-C2
                      │
          Collector ──C1──┬── junction (feedback point)
                          C2
                          │
                         GND
```

**Working:**
- L, C1, C2 form a parallel tank circuit
- C2 provides the feedback voltage to the base (voltage divider: C1 and C2)
- Junction of C1, C2 feeds back to base; inductor completes the tank circuit

**Frequency:**
```
Ceq = C1 × C2 / (C1 + C2)   [series combination of C1 and C2]

f₀ = 1 / (2π√(L × Ceq)) = 1 / (2π√(L × C1C2/(C1+C2)))
```

**Feedback fraction:**
```
β = VC2 / V(tank) = C1/(C1+C2)   [capacitive divider: larger C → more voltage across it]

Wait — for capacitors in series: V divides INVERSELY with C
β = XC2/(XC1+XC2) = (1/ωC2)/(1/ωC1 + 1/ωC2) = C1/(C1+C2)
```

**Hartley vs Colpitts comparison:**

| Aspect | Hartley | Colpitts |
|--------|---------|---------|
| Frequency element | Tapped inductor L | Two capacitors C1, C2 |
| Feedback | Inductive tap | Capacitive divider |
| Frequency tuning | Change C (variable cap) | Change L or change C1/C2 together |
| Purity of output | Good | Excellent (capacitors have no stray inductance issues) |
| Disadvantage | Mutual coupling between L1, L2 adds complexity | Two capacitors (but they're cheap) |
| Frequency range | RF (20kHz-10MHz) | RF to microwave |

---

### Crystal Oscillator — Deep Analysis

**Piezoelectric effect:**

When mechanical stress is applied to a quartz crystal (SiO₂), a voltage appears across its surfaces (direct piezoelectric effect). Conversely, applying a voltage mechanically deforms the crystal (inverse piezoelectric effect). At the **natural resonant frequency** of the crystal (determined by its physical dimensions and cut), this electromechanical coupling is maximum.

**Crystal equivalent circuit:**
```
       Ls (series inductor — mechanical mass)
       │
       Cs (series capacitor — mechanical compliance/elasticity)
       │
       Rs (series resistor — mechanical friction/damping)

All three in series, and the whole series combination is in parallel with:
       Cp (parallel capacitor — plate capacitance of crystal holder)
```

**Two resonance frequencies:**

1. **Series resonant frequency fs:** Ls-Cs series combination resonates:
   ```
   fs = 1/(2π√(Ls × Cs))
   At fs: Series impedance = Rs (minimum, purely resistive) — crystal is a near short-circuit
   ```

2. **Parallel resonant frequency fp:** The series arm becomes inductive (above fs) and resonates with Cp:
   ```
   fp ≈ fs × √(1 + Cs/Cp)
   
   Since Cs << Cp (typically Cs/Cp ≈ 0.001):
   fp ≈ fs × (1 + Cs/(2Cp)) ≈ fs + 0.05%×fs
   ```

The crystal operates as an oscillator between fs and fp — an extremely narrow band (less than 0.1% of fs). Only within this tiny frequency band does the crystal look inductive (needed for the LC tank circuit to oscillate).

**Q factor — why crystals are so stable:**

```
Q = ω₀ × Ls / Rs = ω₀ × (energy stored)/(energy dissipated per cycle)

Typical quartz crystal: Q = 10,000 to 10,000,000
Typical LC resonant circuit: Q = 50 to 200

Higher Q → sharper frequency selectivity → oscillation frequency more precisely determined
→ Less drift with temperature or component aging
```

**Frequency stability comparison:**

| Oscillator type | Frequency stability (drift) |
|----------------|---------------------------|
| RC phase-shift | ±500 ppm/°C (poor) |
| LC (Hartley/Colpitts) | ±100-500 ppm/°C (fair) |
| Crystal (fundamental mode) | ±0.1-10 ppm/°C (excellent) |
| OCXO (Oven-Controlled Crystal) | ±0.01 ppm/°C or better |
| TCXO (Temp-Comp Crystal) | ±1 ppm (excellent) |

ppm = parts per million. 1 ppm at 10MHz = 10Hz frequency error.

**Crystal oscillator circuit:**
```
             VCC
              │
            [RD]
              │
              ├───── Vout
              │
           [MOSFET] ← D-MOSFET or N-ch enhancement
              │ Gate ─ connected to crystal (gate-source) and to drain via feedback
              │
             [CRYSTAL] ── between Gate and Drain (Pierce oscillator configuration)
              │
             [C1] Gate to GND
             [C2] Drain to GND
```

**Pierce oscillator (most common CMOS crystal oscillator):**

```
         C1          XTAL              C2
Gate ────||──── ●───[■ Crystal ■]───● ────||──── Drain (=Vout)
                │                   │
               GND                 GND
```

The inverter (MOSFET amplifier) + crystal + C1, C2 forms the Pierce oscillator. The crystal is used near its series resonant frequency. The inverter provides the required 180° phase, and C1, C2 provide additional 180° to make total 360°.

**Why 32.768kHz for watches?**
```
32768 = 2¹⁵

A 15-bit binary counter divides 32768Hz by 2¹⁵ = 32768 → 1Hz output
The 1Hz signal directly drives the seconds display/mechanism
No complex prescalers needed — purely digital power-of-two division!
Crystal cut (tuning fork cut) is physically shaped as a tuning fork for 32.768kHz
```

---

### Multivibrators — Complete Analysis

#### Astable Multivibrator (Free-Running)

**Circuit:**
```
VCC ─────────────────────────────────────────── VCC
  │                                                │
 [RC1]               [RC2]
  │                   │
Q1─Collector ──C1── Q2─Base        Q1─Base ──C2── Q2─Collector
  │NPN BJT         NPN BJT│
Q1─Base──[RB1]    [RB2]──Q2─Base
  │                            │
Q1─Emitter──GND      GND──Q2─Emitter
```

**State analysis:**

**Assumption:** Initially, Q1 is ON (saturated), Q2 is OFF (cut off).

**State 1 (Q1 ON, Q2 OFF):**

- Q1 collector ≈ VCE(sat) ≈ 0.2V (LOW)
- C1 (left plate at Q1 collector) was charged to ~(VCC - 0.7V) during previous state. Now left plate drops to 0.2V. **Instantaneous voltage across capacitor cannot change:** right plate also drops by (VCC - 0.2V)
  → VB2 drops by (VCC - 0.2V) from its previous +0.7V → VB2 = 0.7 - (VCC - 0.2) = -(VCC - 0.9) ≈ -VCC for VCC >> 0.9V
  → **Q2 is strongly reverse biased → OFF ✓**

- C1 now charges through RB2 from VCC (right plate charging from -VCC toward +VCC):
  ```
  VB2(t) = VCC - 2VCC × e^(-t/RB2C1)   [starts at -VCC, approaches VCC]
  ```

- C2 was discharged (Q2 was OFF in previous state, Q2 collector was HIGH ≈ VCC). C2 now charges through RC2 and Q1-CE path.

**Q2 turns ON when VB2 = +0.7V:**
```
VCC - 2VCC × e^(-t1/RB2C1) = 0.7

For VCC >> 0.7V (approximating VBE ≈ 0):
VCC - 2VCC × e^(-t1/τ1) = 0   → e^(-t1/τ1) = 0.5 → t1 = τ1 × ln2 = 0.693 × RB2 × C1
```

This is the time Q1 stays ON (= one half-period of Q2-Collector output).

**State 2 (Q2 ON, Q1 OFF):** Mirror image. Duration t2 = 0.693 × RB1 × C2.

**Complete timing:**
```
t1 = 0.693 × RB2 × C1   (Q1 ON duration; Q2 output HIGH duration)
t2 = 0.693 × RB1 × C2   (Q2 ON duration; Q1 output HIGH duration)

T = t1 + t2
f = 1/T = 1/[0.693(RB1C2 + RB2C1)]

For symmetric (RB1=RB2=R, C1=C2=C):
T = 1.386RC ≈ 1.38RC
f = 1/(1.386RC) = 0.72/RC
Duty cycle = 50% (symmetric square wave)
```

**Design constraints:**
```
RC must ensure saturation: IC(sat) = VCC/RC >> hFE × IB(min)
RB determines timing but also IB: IB = VCC/RB (approximately)
Need IB > IC(sat)/hFE for saturation

Rule: RC1 = RC2 = RC where VCC/RC × hFE >> VCC/RB
→ RB >> hFE × RC   (this is the timing resistor constraint)
```

---

#### Monostable Multivibrator (One-Shot Trigger)

**Key concept:** Has one **stable state** and one **quasi-stable state** (times out after T).

**Circuit:**
```
VCC ──────────────────────────────── VCC
  │                                    │
 [RC1]               [RC2]
  │                   │
Q1─Collector ──C── Q2─Base       [RB2]──Q2─Base
  │NPN                │NPN              from VCC
  │                   │
Q1─Base──Trigger    [RD]──Q2─Emitter──GND
  │                   │
  │                  GND
[C_trigger][RB1]
  │
 GND
```

**Stable state (Q1 OFF, Q2 ON):**
- Q2 base held at +0.7V by RB2 → Q2 saturated ON
- Q2 collector ≈ 0.2V (LOW)
- C is charged to: VCC - 0.7V (Q1 collector HIGH, Q2 base 0.7V)
- Q1 is OFF (no forward bias on base)

**Trigger arrives (negative pulse or positive differentiated trigger at Q1 base):**
1. Q1 turns ON → Q1 collector drops to 0.2V
2. Capacitor C: left plate drops from ~VCC to 0.2V → right plate (Q2 Base) drops by ~VCC
   → VB2 = 0.7 - VCC ≈ -VCC (strongly reverse biased) → **Q2 turns OFF immediately**

**Quasi-stable state (Q1 ON, Q2 OFF) — duration T:**

- Q2 OFF → Q2 collector goes HIGH to VCC
- C charges through R (or RB2) from VCC: right plate (Q2 Base) rises exponentially
  ```
  VB2(t) = VCC - (VCC + VCC)×e^(-t/RC) = VCC - 2VCC×e^(-t/τ)   [starts at -VCC, approaches VCC]
  ```
- Q2 turns ON when VB2 = 0.7V:
  ```
  T ≈ 0.693 × R × C   (pulse width)
  ```

**Return to stable state:**
- Q2 turns ON → Q2 collector drops to 0.2V → Q1 base driven negative → Q1 turns OFF → stable state ✓

**Output:**
```
Q2 Collector:
HIGH (VCC)            HIGH
       ┌──────────────┐
       │      T       │
LOW ───┘              └────── (stable LOW, Q2 ON)

Q1 Collector:
LOW                LOW
       ───────────────  (stays HIGH only during T)
HIGH ─┘              └─ but this is the Q1 inverted output
```

**Recovery time:** After the pulse, C must fully recharge to its stable-state voltage before another trigger can produce a full-width pulse. Recovery time ≈ 5RC.

---

#### Bistable Multivibrator (Flip-Flop)

**Key concept:** Has **two stable states**. Remains in either state indefinitely until an external trigger forces it to switch. No timing — it's a memory element.

**Circuit:**
```
VCC ──────────────────────────────── VCC
  │                                    │
 [RC1]               [RC2]
  │                   │
Q1─Collector──RB12──Q2─Base   Q2─Collector──RB21──Q1─Base
  │NPN                │NPN
  │                   │
Q1─Base              Q2─Base
  │S (Set input)      │R (Reset input) ← via differentiators and diodes
  │                   │
 GND                 GND
```

**Stable state 1 (Q1 ON, Q2 OFF):**
- Q1 saturated → Q1 Collector ≈ 0.2V → via RB12 → Q2 Base held low → Q2 OFF
- Q2 OFF → Q2 Collector ≈ VCC → via RB21 → Q1 Base held HIGH → Q1 stays ON ✓

**Stable state 2 (Q1 OFF, Q2 ON):** Mirror image, sustained by Q2 keeping Q1 base pulled low.

**Triggering:**

To switch from State 1 to State 2:
- Apply trigger pulse to Q2 Base (Set): Q2 turns ON → Q2 Collector drops → Q1 Base goes low → Q1 turns OFF → Q2 stays ON (new stable state 2)

**Applications of bistable:** SR flip-flop (basic digital memory bit), debounce circuits, frequency dividers (binary counter = bistable triggered by clock).

---

### Summary: Comparison of All Oscillators

| Oscillator | Frequency formula | Range | Output | Frequency stability | Key advantage |
|-----------|-----------------|-------|--------|--------------------|--------------| 
| RC Phase-Shift | f = 1/(2π√6 RC) | Audio (Hz-kHz) | Sinusoidal | Poor | No inductors |
| Wien Bridge | f = 1/(2πRC) | Audio (Hz-kHz) | Sinusoidal (low distortion) | Moderate | Tunable, simple |
| Hartley | f = 1/(2π√(L_total×C)) | RF (kHz-MHz) | Sinusoidal | Good | Easy to tune |
| Colpitts | f = 1/(2π√(L×Ceq)) | RF to microwave | Sinusoidal (excellent purity) | Good | No mutual coupling issue |
| Crystal | f = fs (crystal) | kHz to hundreds of MHz | Sinusoidal | Excellent (< 10ppm) | Extreme stability |
| Astable MV | f = 0.72/RC | Audio to RF | Square/pulse | Poor | Simple, no frequency-selective network |
| Monostable MV | T = 0.69RC (pulse) | — | One-shot pulse | N/A | Timer, pulse stretcher |
| Bistable MV | No frequency | — | Square (triggered) | N/A | Memory, flip-flop |

---

## 2. Example

### Wien Bridge Frequency and Gain Calculation

**Given:** R = 12kΩ, C = 0.02μF. Calculate oscillation frequency and required gain.

```
f₀ = 1/(2πRC) = 1/(2π × 12×10³ × 0.02×10⁻⁶)
   = 1/(2π × 2.4×10⁻⁴)
   = 1/1.508×10⁻³
   = 663Hz

Required amplifier gain: Av = 3 (exactly)
(Since Wien network attenuation = 1/3 and |Aβ| = 1)
```

For BJT version with voltage divider bias: select IC such that:
```
gm = IC/VT; with RC set to give: gm × RC = 3
gm × RC = 3 → IC = 3 × VT/RC = 3 × 26mV/12kΩ = 6.5μA (for that same RC value)
But typically use larger IC for stability: IC = 1mA, RC = 3kΩ (dedicated feedback resistor controls gain to exactly 3)
```

---

## 3. Applications and Use Cases

1. **Crystal oscillators in microcontrollers:** Arduino, STM32, ESP32 — every microcontroller clock source uses an external crystal oscillator (2-80MHz) for baud rate accuracy (UART requires better than ±2% timing).

2. **Wien bridge in laboratory signal generators:** Bench function generators (HP33120A, Rigol DG4000) use Wien bridge circuits (with AGC using FET or OTA) for 0.003% THD sinusoidal outputs from 1Hz to 1MHz.

3. **Hartley/Colpitts in AM/FM superheterodyne radio:** The local oscillator in a superheterodyne receiver uses a Colpitts LC oscillator tunable by a variable capacitor (varactor diode in modern circuits).

4. **Astable multivibrator in LED flashers and buzzers:** The classic NE555 astable and transistor astable — used in LED flashers, alarm buzzers, motor speed controllers (PWM), and clock signals for simple digital logic.

5. **Monostable for switch debouncing:** Keyboard controllers and embedded systems use monostable circuits (hardware or 555 timer) to generate a single clean pulse from a bouncy mechanical keypress.

6. **OCXO in GPS receivers:** GPS receivers require timing accuracy better than 100ns for 30m positional accuracy. The GPS receiver's reference oscillator is an OCXO (oven-controlled crystal oscillator, stable to ±0.01ppm) to maintain sync.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: RC Phase-Shift Oscillator Design [KTU Style]

**Problem:** Design an RC phase-shift oscillator for f₀ = 1kHz. Choose appropriate R and C values and find the minimum transistor gain required. [5 marks]

**Solution:**

**Step 1: Choose C = 0.01μF and find R:**
```
f₀ = 1/(2π√6 × RC)
1000 = 1/(2π × 2.449 × R × 0.01×10⁻⁶)
R = 1/(2π × 2.449 × 0.01×10⁻⁶ × 1000)
R = 1/(1.539×10⁻⁴)
R = 6.5kΩ → use 6.8kΩ (standard)
```

**Verification:**
```
f₀ = 1/(2π × √6 × 6800 × 0.01×10⁻⁶) = 1/(2π × 2.449 × 6.8×10⁻⁵) = 957Hz ≈ 1kHz ✓
```

**Step 2: Minimum gain requirement:**
```
|Av| ≥ 29

For CE amplifier: Av = gm × RC_collector
With IC = 2mA: gm = IC/VT = 2mA/26mV = 76.9mA/V
RC_collector = 29/gm = 29/76.9mA/V = 377Ω → use 390Ω (standard)
```

**Summary:**
- R (phase-shift sections) = 6.8kΩ × 3
- C (phase-shift sections) = 0.01μF × 3
- RC (collector) = 390Ω minimum
- Transistor must have β × gm × RC ≥ 29

---

### Example 2: Crystal Oscillator Frequency Calculation [KTU Style]

**Problem:** A quartz crystal has Ls = 0.5H, Cs = 0.05pF, Cp = 15pF, Rs = 100Ω. Calculate: (a) series resonant frequency fs, (b) parallel resonant frequency fp, (c) Q factor.

**Solution:**

**(a) Series resonant frequency:**
```
fs = 1/(2π√(Ls × Cs))
   = 1/(2π√(0.5 × 0.05×10⁻¹²))
   = 1/(2π√(2.5×10⁻¹⁴))
   = 1/(2π × 1.581×10⁻⁷)
   = 1/(9.932×10⁻⁷)
   = 1.007 × 10⁶ Hz ≈ 1.007 MHz
```

**(b) Parallel resonant frequency:**
```
fp = fs × √(1 + Cs/Cp)
   = 1.007MHz × √(1 + 0.05pF/15pF)
   = 1.007MHz × √(1 + 0.00333)
   = 1.007MHz × √(1.00333)
   = 1.007MHz × 1.001666
   = 1.0087 MHz

Difference: fp - fs = 0.0017MHz = 1.7kHz  (only 0.17% apart!)
```

**(c) Q factor:**
```
Q = ω₀ × Ls / Rs = 2π × fs × Ls / Rs
  = 2π × 1.007×10⁶ × 0.5 / 100
  = 2π × 5.035×10⁵ / 100
  = 31,643

Q ≈ 31,643   (extremely high — confirms excellent frequency stability)
```

---

### Example 3: Astable Multivibrator Waveform and Timing [May 2019, Q14]

**Problem:** Design an astable multivibrator for f = 2kHz with 60% duty cycle. VCC = 5V, hFE = 100.

**Solution:**

**Duty cycle = t1/T = 60% (Q1 ON = 60% of period)**

```
t1 = 0.693 × RB2 × C  = 0.60T
t2 = 0.693 × RB1 × C  = 0.40T

Ratio: RB2/RB1 = 0.60/0.40 = 1.5
```

**Choose T = 1/2kHz = 0.5ms:**
```
t1 = 0.6 × 0.5ms = 0.3ms
t2 = 0.4 × 0.5ms = 0.2ms
```

**Choose C = 0.01μF:**
```
From t1 = 0.693 × RB2 × C:
RB2 = t1/(0.693 × C) = 0.3×10⁻³ / (0.693 × 0.01×10⁻⁶) = 3×10⁻⁴/6.93×10⁻⁹ = 43.3kΩ → use 43kΩ

From t2 = 0.693 × RB1 × C:
RB1 = t2/(0.693 × C) = 0.2×10⁻³ / 6.93×10⁻⁹ = 28.9kΩ → use 27kΩ

Check ratio: RB2/RB1 = 43/27 = 1.59 ≈ 1.5 ✓ (close enough)
```

**Collector resistors:**
```
VCC/RC = IC(sat) → set IC = 5mA for adequate saturation:
RC = VCC/IC = 5V/5mA = 1kΩ

Verify saturation: IB = VCC/RB2 = 5/43kΩ = 116μA
IC(sat)/hFE = 5mA/100 = 50μA < 116μA ✓ (over-saturated, good)
```

**Final design:**
- RB1 = 27kΩ, RB2 = 43kΩ
- C1 = C2 = 0.01μF
- RC1 = RC2 = 1kΩ
- f ≈ 2kHz, duty cycle ≈ 61% ✓

**Waveform sketch (Q1 Collector):**
```
5V  ┌────────────┐    ┌───────────
    │            │    │
0V ─┘            └────┘
   │← t1=0.3ms →│← t2 →│
   │  60% HIGH         40% LOW
```

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q11]: State and explain Barkhausen Criterion. [3 marks]

**Complete Solution:**

**Statement:** For a feedback amplifier to produce and sustain sinusoidal oscillations, the following two conditions (Barkhausen Criterion) must be simultaneously satisfied at the frequency of oscillation f₀:

**Condition 1 — Magnitude:** |A × β| = 1

The product of the open-loop amplifier gain |A| and the feedback fraction |β| must equal exactly unity. If |Aβ| < 1, oscillations die out. If |Aβ| > 1, oscillations grow until amplitude limiting occurs.

**Condition 2 — Phase:** ∠(A × β) = 0° (or n×360°)

The total phase shift around the closed feedback loop must be 0° (or 360°, 720°...) — meaning the fedback signal must arrive at the input in phase with the original signal, constituting **positive feedback**.

**Physical mechanism:**
```
1. Noise at f₀ appears at amplifier input
2. Amplified by A → output = A × Vin
3. Feedback network returns β × output = Aβ × Vin to input
4. For |Aβ| = 1, ∠Aβ = 0°: the returned signal equals the original → self-sustaining!
5. Frequency f₀ is selected by the phase network: only at f₀ does phase = 0°
```

**Example (Wien Bridge Oscillator):**
- A = 3 (non-inverting amplifier gain with Rf/R1 = 2)
- β = 1/3 at f₀ = 1/(2πRC), with 0° phase shift
- |Aβ| = 3 × 1/3 = 1 ✓ and ∠(Aβ) = 0° ✓ → oscillates at f₀ = 1/(2πRC)

**Note:** Barkhausen criterion is necessary but not sufficient. It doesn't explain how oscillations START (noise trigger) or how amplitude is STABILIZED (requires nonlinearity or AGC).

---

### PYQ 2 [May 2019, Q9]: Draw and explain monostable multivibrator. [3 marks]

**Complete Solution:**

**Circuit (transistor monostable multivibrator):**
```
VCC ───┬────[RC1]────┬─────────────────────┬────[RC2]──── VCC
       │             │                     │              │
      [RB1]    Q1-Collector         Q2-Collector        [RB2]──VCC
       │       Q1-Base─── Trigger    Q2-Base─C──Q1-Coll │
       │        (NPN BJT)             (NPN BJT)          │
       │         Q1-Emitter           Q2-Emitter         │
       │              │                    │              │
      GND            GND                 GND         Timing: R and C
                                                    C from Q1-Coll to Q2-Base
                                                    R from VCC to Q2-Base
```

**Stable state (no trigger):**
- Q2: Base held at +0.7V via RB2 → Q2 saturated ON, Collector ≈ 0.2V (output LOW)
- C: Charged to (VCC - 0.7) ≈ 4.3V (Q1-Coll side positive)
- Q1: Base at 0V (no forward bias) → Q1 OFF, Collector ≈ VCC

**Trigger arrives (positive pulse to Q1 base):**
1. Q1 turns ON → Q1 Collector drops to 0.2V
2. Capacitor C: voltage cannot change instantly. Left plate drops by (VCC - 0.2V) → Right plate (Q2 Base) drops: VB2 = 0.7 - (VCC-0.2) ≈ -VCC+0.9 ≈ -VCC → Q2 turns OFF
3. Q2 Collector rises to VCC → output goes HIGH

**Quasi-stable state (Q2 OFF):**
- C charges through R toward VCC (right plate rising from -VCC toward +VCC)
- VB2(t) = VCC - 2VCC × e^(-t/RC)

**Q2 turns ON when VB2 = 0.7V (approximately 0 for calculation):**
```
T ≈ 0.693 × R × C   (pulse width)
```

**Output (Q2 Collector):**
```
HIGH ─────────────┐    T    ┌─────
                  └─────────┘
LOW (stable)      (quasi-stable)  (stable again)
```

Pulse width: **T = 0.693 × R × C**

---

### PYQ 3 [May 2019, Q20a]: Hartley oscillator circuit and oscillation frequency. [5 marks]

**Complete Solution:**

**Hartley Oscillator — Circuit:**

```
           VCC
            │
          [RFC] ← RF Choke (large inductance, blocks HF from entering supply)
            │
     ┌──────Collector───────────────────────────────┐
     │      │NPN BJT                                 │
     │      │Base                                    │
     │      │Emitter ──────────────── [C bypass] ── GND
     │      │                     │
     │      │                     │
     │   [RB1]                   [C] ← Tuning capacitor
     │      │ (bias resistors)    │
     │   [RB2]                   │
     │      │                    │
     └──────┘           L1 ──┬── │
            GND              │  L2 ──── Back to Base (feedback)
                           Tap │
                             GND
```

**Working:**

1. **Tank circuit:** L1 + L2 (total inductance) resonates with C at frequency f₀.
2. **Feedback:** The tap between L1 and L2 provides the feedback voltage. The voltage across L2 is fed to the transistor's base.
3. **Phase analysis:**
   - CE BJT (Collector to Base): 180° phase inversion
   - Inductive tap: Voltage across L2 is 180° out of phase with voltage across L1 (for center-tapped, resonant inductor)
   - Total: 180° + 180° = 360° = 0° → positive feedback ✓
4. **Oscillation starts** with noise; grows as Q1 amplifies → limited by nonlinearity → sustained oscillation.

**Frequency of oscillation:**
```
f₀ = 1 / (2π √(L_total × C))

Where:
L_total = L1 + L2   [no mutual coupling]
L_total = L1 + L2 + 2M   [with mutual coupling M]
C = tank capacitor

Example: L1 = 50μH, L2 = 25μH, C = 500pF, no mutual coupling:
L_total = 75μH
f₀ = 1/(2π√(75×10⁻⁶ × 500×10⁻¹²))
   = 1/(2π√(3.75×10⁻¹⁴))
   = 1/(2π × 1.936×10⁻⁷)
   = 1/(1.217×10⁻⁶)
   = 822 kHz
```

**Feedback fraction:**
```
β = L2 / (L1+L2) = 25/(75) = 1/3

Required gain: A ≥ 1/β = 3
gm × (output impedance) ≥ 3
```

**Advantages:** Variable frequency by changing C (variable capacitor); good frequency stability; widely used in AM radio tuner oscillators.
