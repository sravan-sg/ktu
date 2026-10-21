# Oscillators and Multivibrators

## 1. Explanation

### What is an Oscillator? — Core Intuition

An oscillator is a circuit that generates a periodic signal (sinusoidal or non-sinusoidal) **without any external input signal** — it sustains itself through **positive feedback**. The fundamental question is: how can a system sustain oscillations without continuously injecting energy?

**Answer:** A small noise signal is amplified, fed back to the input in phase with itself, amplified again, and this bootstrapping cycle results in a sustained oscillation. The amplitude stabilizes when the amplifier gain equals the feedback loss (nonlinear saturation balances the growth).

### Barkhausen Criterion — The Mathematics of Oscillation

For an amplifier with gain A and feedback network with fraction β:

```
Loop gain = A × β

For self-sustaining oscillation:
1. |Aβ| = 1 (magnitude condition)
2. ∠Aβ = 0° or 360° (phase condition — net feedback must be positive)
```

**Physical interpretation:**
- If |Aβ| > 1: Oscillations grow (amplifier overdrives the feedback, amplitude increases)
- If |Aβ| < 1: Oscillations decay (losses exceed gain, amplitude decreases)
- If |Aβ| = 1: Sustained oscillation at constant amplitude ✓

The oscillation frequency is the specific frequency at which the phase condition (∠Aβ = 0°) is satisfied. The feedback network is **frequency-selective** — only at one specific frequency does the phase work out to 0°.

### Classification of Oscillators

**By output waveform:**
1. **Sinusoidal oscillators**: Wien bridge, Hartley, Colpitts, Crystal, RC phase shift
2. **Non-sinusoidal (relaxation) oscillators**: Astable, monostable, bistable multivibrators; sawtooth generators

**By frequency range:**
- Audio frequency (20Hz-20kHz): Wien bridge, RC oscillators
- Radio frequency (20kHz-30MHz): LC oscillators (Hartley, Colpitts)
- High frequency (30MHz+): Crystal oscillators

### Wien Bridge Oscillator

**Circuit principle:** A two-stage BJT amplifier (or inverting op-amp) with Wien RC network for frequency selection.

**Wien feedback network:**
```
        R          C
Vout ──┤├──┬──────||──── To amplifier input
           │
          [C]
           │
          [R]
           │
          GND
```

The series arm (R + C) and parallel arm (C || R) together form the Wien network.

**Transfer function at resonance frequency f₀:**
```
At ω = ω₀ = 1/(RC):
β(ω₀) = 1/3  (exactly 1/3 attenuation)
Phase = 0° (no phase shift at this frequency)
```

For Barkhausen: A × β = 1 → A = 3 (amplifier must have gain of exactly 3)

**Oscillation frequency:**
```
f₀ = 1 / (2πRC)

Example: R = 10kΩ, C = 0.016μF
f₀ = 1 / (2π × 10⁴ × 0.016×10⁻⁶) = 1000 Hz = 1kHz
```

**Amplitude stabilization:** In practice, a tungsten lamp or thermistor with positive temperature coefficient in the feedback network automatically adjusts gain to exactly 3 through nonlinear resistance change, ensuring stable amplitude.

### Hartley Oscillator (LC Oscillator, RF Range)

**Circuit:** Uses a tapped inductor (or two inductors L1, L2) as the feedback and frequency-determining element, with capacitor C.

```
         VCC
          │
         [RFC] (RF choke)
          │
     Collector
    [NPN BJT]
     Emitter ──────────┬─── C (capacitor to GND)
          │             │
         [C_bypass]    L1 ─┐ Tapped inductor
          │             │  │
         GND           L2 ─┘
                        │
                    ── to Base ── (feedback tap)
```

**Resonant frequency:**
```
f₀ = 1 / (2π√(L_total × C))

Where: L_total = L1 + L2 + 2M (M = mutual inductance if coupled)
If L1 and L2 are independent taps of a single inductor: L_total = L1 + L2
```

**Feedback fraction (at resonance):**
```
β = V_L1 / V_L2+L1 ≈ L1/L_total
```

**Phase analysis:**
- Common-emitter BJT inverts signal: 180° from base to collector
- Tapped inductor provides 180° additional phase shift (L2 voltage is 180° out of phase with L1 voltage in center-tapped coil)
- Total phase: 360° = 0° ✓

**Advantages:** Easy to tune (just change C for variable frequency), good frequency stability, commonly used in AM radio oscillators (455kHz IF, 540-1600kHz RF stages).

### Crystal Oscillator

**Principle:** A piezoelectric crystal (quartz) exhibits **mechanical resonance** at an extremely precise frequency, determined by its physical dimensions. The electrical equivalent circuit:

```
Crystal equivalent circuit:
          Ls       Cs     Rs
  ┌──────mmm──────||──────┤├──────┐
  │                                │
  └─────────────||──────────────── ┘
                  Cp (parallel capacitance)
```

**Two resonance frequencies:**
1. **Series resonance (fs)**: Ls, Cs, Rs in series resonate (crystal acts as near-short circuit)
   ```
   fs = 1 / (2π√(Ls × Cs))
   ```
2. **Parallel resonance (fp)**: Crystal acts as high impedance
   ```
   fp ≈ fs × √(1 + Cs/Cp) ≈ fs + small amount (fp - fs < 1%)
   ```

**Q factor:** Crystal Q is extremely high: 10,000 to 10,000,000 (vs LC tank circuit Q of 50-200). This makes crystal oscillators extraordinarily frequency stable.

**Frequency stability:** Crystal oscillator: < 1 ppm (part per million) drift. LC oscillator: 100-1000 ppm.

**Applications:** Quartz watches (32.768kHz crystal), microprocessor clocks (8MHz, 16MHz, etc.), GPS receivers, communication systems.

**Why 32.768kHz for watches?** 32768 = 2¹⁵. Dividing 15 times gives exactly 1Hz for the second hand — purely digital, no complex prescaler needed.

### Non-Sinusoidal Oscillators: Multivibrators

Multivibrators generate **square, pulse, or trigger waveforms** using transistors driven between saturation and cutoff. Three types:

**1. Astable Multivibrator (Free-running):**
- No stable states — continuously switches between two quasi-stable states
- Self-oscillating: generates square wave without external trigger
- Frequency: f = 0.72/(RC) [symmetric]
- Applications: Clock generators, tone generators, LED flashers

**2. Monostable Multivibrator (One-shot):**
- One stable state, one quasi-stable state
- Triggered by external pulse → switches to quasi-stable state for time T → returns to stable state
- Pulse width: T = 0.69 × R × C
- Applications: Debouncing switches, pulse width generation, timing delays

**3. Bistable Multivibrator (Flip-flop):**
- Two stable states — remains in either state indefinitely until externally triggered
- Requires trigger pulse at Set input (goes to state 1) or Reset input (goes to state 0)
- No oscillation — it's a memory element
- Applications: SR flip-flop, binary counter, shift register

**Design equations (BJT multivibrators):**

| Type | Stable States | Timing | Trigger |
|------|--------------|--------|---------|
| Astable | 0 (free-running) | T = 0.69(R₁C₁ + R₂C₂) | None needed |
| Monostable | 1 | T_quasi = 0.69 × R × C | Single trigger |
| Bistable | 2 | No timing (latches) | Two triggers (S, R) |

---

## 2. Example

### Hartley Oscillator Frequency Calculation

**Given:** L1 = 50μH, L2 = 25μH, C = 500pF
**Find:** Oscillation frequency

```
L_total = L1 + L2 = 50 + 25 = 75μH (assuming no mutual coupling)

f₀ = 1 / (2π√(L_total × C))
   = 1 / (2π√(75×10⁻⁶ × 500×10⁻¹²))
   = 1 / (2π√(37.5×10⁻¹⁵))
   = 1 / (2π × 6.12×10⁻⁸)
   = 1 / (3.847×10⁻⁷)
   = 2.6 MHz
```

---

## 3. Applications and Use Cases

1. **Wien Bridge in Function Generators**: Laboratory signal generators use Wien bridge oscillators with variable RC to produce sinusoidal outputs from 1Hz to 1MHz.

2. **Crystal Oscillators in Microcontrollers**: Arduino, STM32, and all microcontrollers use external crystal oscillators (typically 8-20MHz) for precise timing of instruction cycles and communication protocols (UART, SPI, I²C baud rates).

3. **Hartley/Colpitts in AM/FM Radios**: The local oscillator in superheterodyne AM radios uses Hartley or Colpitts LC oscillators to track the received frequency (tuned by variable capacitor).

4. **Astable 555 in LED Flashers**: Simple LED flashers, alarm circuits, and pulse width modulators use 555 timer or astable multivibrator configurations.

5. **Monostable for Switch Debouncing**: Mechanical switches produce multiple contact bounces. A monostable multivibrator ignores all bounces within its timing window T, outputting a single clean pulse.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Wien Bridge Oscillator Frequency [May 2019, Q13b, Q20a]

**Problem:** Sketch and explain a Wien Bridge oscillator using transistors. Find the frequency if R = 12kΩ and C = 0.02μF.

**Solution:**

**Frequency calculation:**
```
f₀ = 1 / (2πRC)
   = 1 / (2π × 12×10³ × 0.02×10⁻⁶)
   = 1 / (2π × 2.4×10⁻⁴)
   = 1 / (1.508×10⁻³)
   = 663 Hz
```

**Barkhausen criterion analysis:**

At f₀ = 663Hz:
- Wien network feedback fraction: β = 1/3 (0° phase shift)
- Required amplifier gain: A = 1/β = 3

For two-stage BJT amplifier:
- Stage 1 (common emitter): gain = −Av1 (inverts, 180°)
- Stage 2 (common emitter): gain = −Av2 (inverts, 180°)
- Total: 360° = 0° phase ✓ (same as positive feedback)
- Total gain: Av1 × Av2 = 3

**Condition for sustained oscillation:** Each stage must provide gain √3 = 1.73, OR one stage can have gain 3 and the other gain 1 (emitter follower).

---

### Example 2: Astable Multivibrator Design [May 2019, Q14]

**Problem:** Design an astable multivibrator using transistors for f = 2kHz and 50% duty cycle.

**Solution:**

**Given:** f = 2kHz, duty cycle = 50% (symmetric: R₁=R₂=R, C₁=C₂=C)

**From timing equation:**
```
T = 1.38 × R × C    (for symmetric astable)
T = 1/f = 1/2000 = 0.5ms

R × C = T/1.38 = 0.5×10⁻³/1.38 = 3.62×10⁻⁴

Choose C = 0.01μF (10nF):
R = 3.62×10⁻⁴ / 10×10⁻⁹ = 36.2kΩ → use 33kΩ (standard value)

Verification: T = 1.38 × 33k × 10nF = 1.38 × 3.3×10⁻⁴ = 454μs
f = 1/454μs = 2.2kHz (close to 2kHz; fine-tune R slightly)
```

**Collector resistors (RC):**
```
RC = VCC / IC(sat) × 0.1   [rule of thumb: ensure deep saturation]
With VCC = 5V, IC = 5mA:
RC = 5 / 5mA = 1kΩ → use 1kΩ
```

**Final design values:**
- R1 = R2 = 33kΩ (base resistors)
- C1 = C2 = 0.01μF (timing capacitors)
- RC1 = RC2 = 1kΩ (collector resistors)
- VCC = 5V
- Transistors: 2N2222 or BC547 (NPN, low power)

---

### Example 3: Monostable Multivibrator Timing [May 2019, Q9]

**Problem:** Draw the circuit of a monostable multivibrator using transistors. Find the pulse width if R = 100kΩ, C = 0.1μF.

**Solution:**

**Pulse width:**
```
T_pulse = 0.69 × R × C
        = 0.69 × 100×10³ × 0.1×10⁻⁶
        = 0.69 × 10⁻²
        = 6.9ms
```

**Circuit description:**

- Q1: Normally OFF (stable state)
- Q2: Normally ON (base held positive through R2 from VCC)
- C: Coupling capacitor from Q1 collector to Q2 base

**Trigger pulse arrives (negative pulse at Q1 base):**
1. Q1 base goes positive (via differentiated trigger): Q1 turns ON
2. Q1 collector drops to near 0V (saturation)
3. C (which had Q2-base voltage on it) now causes Q2 base to go negative (C cannot change voltage instantaneously)
4. Q2 turns OFF

**Quasi-stable state (Q1 ON, Q2 OFF):**
- C charges through R toward VCC
- When C charges enough to bring Q2 base to +0.7V: Q2 turns ON again
- Q2 ON → Q2 collector drops → Q1 base driven negative (if cross-coupled) → Q1 OFF
- Returns to stable state

**Timing:** T = 0.69 × R × C = 6.9ms is the pulse width of the quasi-stable state.

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q11]: State and explain Barkhausen Criteria. [3 marks]

**Complete Solution:**

**Barkhausen Criterion:** For a feedback amplifier to oscillate (self-sustain oscillations), the **loop gain must simultaneously satisfy two conditions**:

**1. Magnitude condition:**
```
|Aβ| = 1

Where A = open-loop voltage gain of the amplifier
      β = feedback fraction (ratio of fed-back signal to output signal)
```

If |Aβ| < 1: oscillations die out (insufficient loop gain to overcome losses)
If |Aβ| > 1: oscillations grow until amplifier saturates (clips), then settles at |Aβ| = 1 at a new amplitude

**2. Phase condition:**
```
∠(Aβ) = 0° (or 360°, 720°, ... i.e., any integer multiple of 360°)
```

The total phase shift around the feedback loop must be zero (or 360°), ensuring that the fed-back signal is exactly in phase with the original input, constituting **positive feedback** at the frequency of oscillation.

**Physical meaning:**
- A small noise signal at frequency f₀ is amplified with gain A
- The feedback network sends fraction β of the output back to the input
- If the feedback arrives **in phase** (∠Aβ = 0°) and with **exactly the right amplitude** (|Aβ| = 1), the loop is self-sustaining
- The feedback network is designed to be frequency-selective: only at f₀ does the phase condition satisfy — this selects the oscillation frequency

**Example (Wien Bridge):**
- A = 3 (amplifier gain)
- β = 1/3 (Wien network at f₀)
- |Aβ| = 3 × 1/3 = 1 ✓
- Phase: Wien network provides 0° at f₀, two-stage amplifier provides 360° → total 0° ✓

**Note:** Barkhausen criterion gives necessary but not sufficient conditions. Practical oscillators need a mechanism to start (noise trigger) and stabilize amplitude (AGC or nonlinearity).

---

### PYQ 2 [May 2019, Q9]: Draw the circuit of a monostable multivibrator using transistors. [3 marks]

**Complete Solution:**

**Circuit:**
```
VCC ────┬──[RC1]──┬──────────────┬──[RC2]──┬──── VCC
        │         │              │          │
       [RB1]    C(Q1)          C(Q2)      [RB2]
        │      B───┤ Q1   Q2 ├───B          │
       Trig    E   │          │  E          VCC
        │       │  │          │  │           │
       [C_trig] │ GND        GND │          [R] (timing R)
        │       │                │            │
       GND    [R_E1]           [C] (timing capacitor)
               │                │
              GND              [D] (steering diode)
                                │
                               GND
```

**Simplified monostable circuit (standard BJT monostable):**

```
VCC ──┬────[RC1]────┬─────[RC2]────┬──── VCC
      │             │              │
     [RB]       Q1-C  C-Q2      (none for Q2, base driven by C)
      │        B─┤    ├─B         │
     Trig    (NPN)  (NPN)      ──────
      │          │    │          │ C (timing)
     GND       [RE1] [RE2]    [R] (timing)
                │     │          │
               GND   GND        GND
```

**Stable state:** Q2 ON (saturated), Q1 OFF (blocked)
**Trigger arrives at Q1 base:** Q1 turns ON → C rapidly discharges through Q1, driving Q2 base negative → Q2 OFF
**Quasi-stable state (duration T):** C charges through R → when VB(Q2) reaches 0.7V, Q2 turns ON again → stable state restored
**Output** taken from Q2 collector: normally LOW (Q2 sat), goes HIGH for period T after trigger.

Pulse width: **T = 0.69 × R × C**
