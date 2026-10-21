# CS207 — Electronic Devices and Circuits
## Sample Question Paper 3

**APJ Abdul Kalam Technological University**  
**Third Semester B.Tech Degree Examination**  
**Course Code: CS207 | Course Name: Electronic Devices and Circuits**  
**Max. Marks: 100 | Duration: 3 Hours**

---

## PART A

**Answer all questions. Each carries 3 marks.**

**1.** A triangle wave of 2kHz and amplitude ±6V is applied to an RC integrating circuit with R = 200kΩ, C = 0.1μF. State whether the output is a good integration. Sketch the expected output waveform.

**2.** Explain the three-pin IC 7805 voltage regulator with an application circuit. What is the minimum input voltage needed to maintain regulation? Why are external capacitors required?

**3.** Explain the JFET structure and list four advantages of FET over BJT.

**4.** A biased negative clipper has VR = -3V and input Vin = 10sin(ωt)V. Sketch the output waveform clearly showing clipped and unclipped regions.

---

## PART B

**Answer any two full questions. Each carries 9 marks.**

**5.**  
**(a)** Explain the transistor as a switch. Draw the simple sweep circuit using a transistor switch. With R = 100kΩ, C = 0.1μF, VCC = 10V, find the ramp rate and peak output voltage for a sweep time of 5ms. *(4 marks)*  
**(b)** Draw and explain the circuit of the IC 723 configured as a high voltage regulator (Vout = 15V). Derive the formula for output voltage and specify R1, R2 values. *(5 marks)*

**6.**  
**(a)** Design waveform conversion circuits using passive components:
   - (i) Convert a 1kHz triangular wave to a square wave
   - (ii) Convert a 5kHz square wave to a triangular wave
   Specify R, C values and justify your design. *(4 marks)*  
**(b)** Compare JFET and MOSFET (enhancement) in terms of structure, principle, biasing, characteristics, and applications. *(5 marks)*

**7.**  
**(a)** Explain the working of a voltage doubler (full-wave type). If Vin = 25V RMS, find the output voltage and the voltage rating required for each capacitor. *(4 marks)*  
**(b)** Draw and explain the circuit of a shunt regulator using a zener diode and transistor. A 9V regulated supply is needed; design the circuit for IL_max = 100mA, Vin = 15V. *(5 marks)*

---

## PART C

**Answer all questions. Each carries 3 marks.**

**8.** Define stability factor S for a transistor biasing circuit. For a voltage-divider bias with RTH = 2kΩ and RE = 1kΩ, β = 120, calculate S. Comment on the thermal stability.

**9.** Explain the crystal oscillator with its equivalent circuit. What are the series and parallel resonant frequencies and which one is used in oscillator circuits?

**10.** An RC coupled amplifier has two identical stages, each with fH = 150kHz. Find the overall upper cutoff frequency of the two-stage amplifier.

**11.** Explain how negative feedback in an amplifier improves: (a) gain stability, (b) bandwidth. Give formulas for both.

---

## PART D

**Answer any two full questions. Each carries 9 marks.**

**12.**  
**(a)** A self-bias (emitter bias) circuit has VCC = 12V, RC = 4.7kΩ, RE = 2.2kΩ, RB = 390kΩ, β = 100. Find IB, IC, VCE. Calculate the stability factor S and compare with fixed bias. *(5 marks)*  
**(b)** Explain the classification of amplifiers based on biasing (Class A, B, AB, C). Which class has the highest efficiency and which the lowest distortion? *(4 marks)*

**13.** With circuit diagrams and analysis, explain the Hartley oscillator:
(a) Draw the circuit and identify feedback elements  
(b) Derive the expression for oscillation frequency  
(c) Show that Barkhausen's criterion is satisfied  
(d) If L1 = 0.1mH, L2 = 0.2mH, C = 500pF (no mutual coupling), calculate f₀  
*(9 marks)*

**14.**  
**(a)** Explain the monostable multivibrator using transistors with full waveforms (trigger, Q1 base voltage, Q2 collector voltage, output). Derive the pulse width formula. Design for T = 5ms using C = 0.047μF. *(6 marks)*  
**(b)** What is a bistable multivibrator? How is it different from monostable? Draw the basic circuit and explain its two stable states. *(3 marks)*

---

## PART E

**Answer any four full questions. Each carries 10 marks.**

**15.**  
**(a)** Draw and explain the op-amp differentiator circuit. Derive the output expression. What is the problem with an ideal differentiator and how is it modified for practical use? If R = 10kΩ, C = 0.01μF, find the gain at 1kHz and 10kHz. *(6 marks)*  
**(b)** Using op-amps, realize: Vout = 4V1 - 3V2. Show the complete circuit with resistor values (assume Rf = 12kΩ for the first stage). *(4 marks)*

**16.**  
**(a)** Explain the working of the differential amplifier as the first stage of an op-amp. Derive expressions for differential-mode gain Ad and common-mode gain Ac. Why is CMRR important in ECG machines? *(6 marks)*  
**(b)** Design an active first-order low-pass filter with fc = 1kHz and gain of -5 (inverting). Specify all components. *(4 marks)*

**17.**  
**(a)** Explain the R-2R ladder DAC in detail. For a 4-bit R-2R DAC with Vref = 16V and Rf = R, find Vout for input code 1011₂. Show the node voltages at each stage of the ladder. *(6 marks)*  
**(b)** Explain the successive approximation ADC. Perform a 4-bit SAR conversion for Vin = 11.2V with Vref = 16V. Show all steps in tabular form. *(4 marks)*

**18.**  
**(a)** Draw and explain the circuit of an op-amp integrator. A square wave of ±5V amplitude and frequency 500Hz is applied to an integrator with R = 100kΩ, C = 0.01μF. Find: (i) τ, (ii) time constant vs period check, (iii) peak output voltage. Sketch output waveform. *(6 marks)*  
**(b)** An IC 555 is connected as a monostable multivibrator. Derive the pulse width formula from first principles (using capacitor charging equation). *(4 marks)*

**19.**  
**(a)** Design an astable multivibrator using IC 555 for frequency 1kHz and duty cycle exactly 50%. Explain why the standard 555 astable circuit cannot directly achieve 50% duty cycle and suggest a modification (use diode across RB). Specify component values. *(6 marks)*  
**(b)** Explain the concept of gain-bandwidth product (GBW) of an op-amp. If an op-amp has GBW = 1MHz, find: (i) closed-loop bandwidth at gain of 50, (ii) closed-loop bandwidth at gain of 200. *(4 marks)*

**20.**  
**(a)** Explain the Schmitt trigger using op-amp (inverting type). Derive UTP and LTP expressions. A Schmitt trigger has R1 = 47kΩ, Rf = 470kΩ, and Vsat = ±13V. Calculate UTP, LTP, and hysteresis. If a noisy sine wave of 12V amplitude is applied, sketch the output. *(6 marks)*  
**(b)** Explain the specifications of a DAC: resolution, accuracy, settling time, monotonicity, and linearity error. Give numerical examples for a 10-bit DAC with Vref = 10V. *(4 marks)*

---
*Total: 100 Marks | Pattern designed to match official KTU CS207 examination format.*
