# CS207 — Electronic Devices and Circuits

> 3 Credits | L-T-P: 3-0-0 | Prerequisite: BE101-04 Introduction to Electronics Engineering | Year of Introduction: 2016

---

## Grading Criteria

| Component | Details |
|-----------|---------|
| Internal Assessment | 2 Internal Exams (First Internal covers Modules 1-2, Second Internal covers Modules 3-4) |
| End Semester Exam | 5 Parts (A, B, C, D, E) — 100 Marks total |
| Per-Module Weightage | Modules 1 & 2: 15% each \| Modules 3 & 4: 15% each \| Modules 5 & 6: 20% each |

**Question Paper Pattern:**

| Part | Coverage | Format | Total Marks |
|------|----------|--------|-------------|
| A | Modules 1 & 2 | 4 × 3 marks (all compulsory) | 12 |
| B | Modules 1 & 2 | Answer 2/3 questions, 9 marks each (max 3 sub-parts) | 18 |
| C | Modules 3 & 4 | 4 × 3 marks (all compulsory) | 12 |
| D | Modules 3 & 4 | Answer 2/3 questions, 9 marks each (max 3 sub-parts) | 18 |
| E | Modules 5 & 6 | Answer 4/6 questions, 10 marks each (max 3 sub-parts) | 40 |
| **Total** | | | **100** |

> At least 60% of questions must be analytical/numerical/design type.

---

## Textbooks

1. **David A. Bell** — *Electronic Devices and Circuits*, Oxford University Press, 2008. *(Primary text — covers all modules)*
2. **Salivahanan S. and V. S. K. Bhaaskaran** — *Linear Integrated Circuits*, Tata McGraw Hill, 2008. *(Primarily Modules 5 & 6 — Op-Amps, ICs, Filters, DAC/ADC)*

**References:**
1. Neamen D. — *Electronic Circuits, Analysis and Design*, 3/e, TMH, 2007.
2. Robert Boylestad and L. Nashelsky — *Electronic Devices and Circuit Theory*, Pearson.
3. Bogart T. F. — *Electronic Devices Circuits*, 6/e, Pearson, 2012.
4. Maini A. K. and V. Agrawal — *Electronic Devices and Circuits*, Wiley India, 2011.
5. K. Gopakumar — *Design and Analysis of Electronic Circuits*, Phasor Books, Kollam, 2013.
6. Millman J. and C. Halkias — *Integrated Electronics*, 2/e, McGraw-Hill, 2010.

---

## Modules

### Module 1 — Wave Shaping and Diode Circuits (5 Hours | 15% Marks)

- Wave shaping circuits: Sinusoidal and non-sinusoidal wave shapes
- Principle and working of RC differentiating circuits
- Principle and working of RC integrating circuits
- Conversion of one non-sinusoidal wave shape into another
- Clipping circuits: Positive, negative, and biased clipper
- Clamping circuits: Positive, negative, and biased clamper
- Voltage multipliers: Voltage doubler and voltage tripler
- Simple sweep circuit using transistor as a switch

### Module 2 — Regulated Power Supplies and Field Effect Transistors (7 Hours | 15% Marks)

**Regulated Power Supplies (4 Hours):**
- Review of simple zener voltage regulator
- Shunt voltage regulator using transistors
- Series voltage regulator using transistors
- Current limiting and foldback protection
- 3-pin regulators: 78XX and 79XX series
- IC 723 and its use as low voltage regulator
- IC 723 and its use as high voltage regulator
- DC to DC conversion
- Circuit/block diagram and working of SMPS (Switch Mode Power Supply)

**Field Effect Transistors (3 Hours):**
- JFET: Structure, principle of operation and characteristics
- Comparison of JFET with BJT
- MOSFET: Structure, principle of operation and characteristics
- Enhancement type MOSFET: Structure and characteristics
- Depletion type MOSFET: Structure and characteristics

### Module 3 — Amplifiers and Feedback (7 Hours | 15% Marks)

- Introduction to transistor biasing: operating point, concept of load line, thermal stability
- Fixed bias circuit
- Self bias (emitter bias) circuit
- Voltage divider bias circuit
- Classification of amplifiers
- RC coupled amplifier: voltage gain and frequency response
- Multistage amplifiers: effect of cascading on gain and bandwidth
- Feedback in amplifiers: effect of negative feedback on amplifiers
- MOSFET Amplifier: circuit diagram and working of common source MOSFET amplifier

### Module 4 — Oscillators and Multivibrators (5 Hours | 15% Marks)

- Classification of oscillators
- Criterion for oscillation (Barkhausen criterion)
- Analysis of Wien bridge oscillator
- Analysis of Hartley oscillator
- Crystal oscillator
- Non-sinusoidal oscillators (design equations and working only; no analysis required):
  - Astable multivibrator using transistors
  - Monostable multivibrator using transistors
  - Bistable multivibrator using transistors

### Module 5 — Operational Amplifiers (8 Hours | 20% Marks)

- Differential amplifier circuit and operation
- Characteristics of op-amps: open-loop gain, bandwidth, slew rate, CMRR, offset voltage, offset current
- Comparison of ideal and practical op-amp (IC741)
- Applications of op-amps:
  - Scale changer (inverting amplifier)
  - Sign changer (unity-gain inverter)
  - Adder/summing amplifier
  - Subtractor
  - Integrator
  - Differentiator
  - Schmitt trigger
  - Wien bridge oscillator using op-amp

### Module 6 — ICs, Filters, DAC/ADC and Timer IC (8 Hours | 20% Marks)

**Active Filters (No analysis required):**
- First order low pass active filter using op-amp with gain
- Second order low pass active filter using op-amp with gain
- First order high pass active filter using op-amp with gain
- Second order high pass active filter using op-amp with gain

**D/A and A/D Converters:**
- Important specifications of DAC and ADC
- Sample and hold circuit
- Binary weighted resistor type D/A converter (concept only)
- R-2R ladder type D/A converter (concept only)
- Flash type A/D converter
- Dual slope type A/D converter
- Successive approximation type A/D converter

**Timer IC:**
- Circuit diagram and working of Timer IC 555
- Astable multivibrator using IC 555
- Monostable multivibrator using IC 555

---

## Exam Focus — What to Prioritize

1. **Modules 5 & 6 carry 40 marks (Part E)** — Op-amp applications (integrator, differentiator, summing amplifier) and ADC/DAC converter circuits are the highest-return study areas. Master all 8 op-amp application circuits with mathematical derivations.
2. **Op-Amp Characteristics (Module 5)** — Slew rate, CMRR, offset voltage/current, and gain-bandwidth product are standard numerical question targets.
3. **Oscillators — Wien Bridge & Hartley (Module 4)** — Design equations and frequency calculations are recurring numerical problems. Crystal oscillator is frequent in Part C/D short answers.
4. **RC Differentiator vs Integrator (Module 1)** — Wave-shape conversion, time-constant analysis, and conversion of square wave to triangle wave are classic analytical problems.
5. **Transistor Biasing (Module 3)** — Voltage divider bias Q-point calculation is a guaranteed 9-mark analytical question in Part D. RC coupled amplifier frequency response plots are also high-yield.
6. **Regulated Power Supplies — IC 723 (Module 2)** — Design of low/high voltage regulators using IC 723, current limiting, and foldback protection circuits are frequent design questions.
7. **ADC Comparisons (Module 6)** — Successive approximation vs dual slope vs flash ADC: speed, resolution, and working comparisons appear consistently as Part E questions.
8. **Multivibrators using transistors and 555 (Modules 4 & 6)** — Design equations for astable/monostable multivibrators are near-certain numerical questions in Part D and E.
