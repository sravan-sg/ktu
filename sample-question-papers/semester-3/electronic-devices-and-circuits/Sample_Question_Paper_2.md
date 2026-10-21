# CS207 — Electronic Devices and Circuits
## Sample Question Paper 2

**APJ Abdul Kalam Technological University**  
**Third Semester B.Tech Degree Examination**  
**Course Code: CS207 | Course Name: Electronic Devices and Circuits**  
**Max. Marks: 100 | Duration: 3 Hours**

---

## PART A

**Answer all questions. Each carries 3 marks.**

**1.** Derive the output-input relationship of an RC differentiating circuit. Clearly state the condition for it to act as a good differentiator in terms of RC and T.

**2.** A 3-pin 7812 regulator is used with Vin = 18V and IL = 500mA. Calculate the power dissipated in the regulator IC. Is a heatsink required? (Assume Pd(max) = 1.5W without heatsink.)

**3.** Sketch the ID vs VGS (transfer) characteristic of a JFET with IDSS = 8mA and VP = -5V. Find ID at VGS = -2.5V.

**4.** Distinguish between (i) shunt and series voltage regulators and (ii) positive and negative clampers.

---

## PART B

**Answer any two full questions. Each carries 9 marks.**

**5.**  
**(a)** Explain the working of a negative clamper circuit with a circuit diagram and waveforms for a square wave input ±10V. Where is the output waveform clamped? *(4 marks)*  
**(b)** Draw the block diagram of an SMPS and explain the function of each block. Compare SMPS and linear regulators in terms of efficiency and applications. *(5 marks)*

**6.**  
**(a)** A half-wave voltage doubler uses silicon diodes (Vf = 0.7V each) with Vin = 20V peak AC. Find the practical output voltage and percentage loss due to diode drops. *(3 marks)*  
**(b)** Explain the structure and operation of both enhancement and depletion type MOSFETs. Draw their symbols and ID vs VGS characteristics. *(6 marks)*

**7.**  
**(a)** A square wave of 1kHz and amplitude ±8V is applied to an RC differentiator with R = 500Ω, C = 0.01μF. Calculate τ, check if the circuit is a good differentiator, and find the output waveform peak voltage and decay. *(4 marks)*  
**(b)** Draw and explain the circuit of a shunt voltage regulator using transistors. Derive an expression for its output voltage and explain the self-correcting feedback mechanism. *(5 marks)*

---

## PART C

**Answer all questions. Each carries 3 marks.**

**8.** A BJT with β = 80 is biased with fixed bias (VCC = 10V, RB = 470kΩ, RC = 2.2kΩ). Find IB, IC, VCE, and the stability factor S.

**9.** What is a crystal oscillator? Why is its frequency stability far superior to LC oscillators? Explain the concept of series and parallel resonance in a crystal.

**10.** Explain the Barkhausen criterion for oscillations. For a Wien bridge oscillator, what gain must the amplifier provide and why?

**11.** A two-stage RC coupled amplifier has each stage with mid-band gain of 50 and upper cutoff frequency of 200kHz. Find the total gain and the overall upper cutoff frequency for the cascaded amplifier.

---

## PART D

**Answer any two full questions. Each carries 9 marks.**

**12.** An RC coupled amplifier (common emitter) has VCC = 12V, RC = 3.3kΩ, RE = 1kΩ, R1 = 82kΩ, R2 = 18kΩ, β = 150. Calculate:
(a) VB, VE, IE, IC, VCE (Q-point)
(b) Mid-band voltage gain Av
(c) Input impedance Zin *(9 marks)*

**13.**  
**(a)** Explain the effect of negative feedback on the gain, bandwidth, input impedance, and distortion of an amplifier. Why is it called "negative" feedback? *(4 marks)*  
**(b)** Draw and explain the circuit of a common-source MOSFET amplifier. Derive the expression for its voltage gain and compare with the common-emitter BJT amplifier. *(5 marks)*

**14.** Design an astable multivibrator using transistors for a frequency of 500Hz and equal on/off times. Specify all component values (RB1, RB2, C1, C2, RC1, RC2) with VCC = 6V, IC(sat) = 5mA. Sketch the output waveform showing exact timing. *(9 marks)*

---

## PART E

**Answer any four full questions. Each carries 10 marks.**

**15.**  
**(a)** Draw and explain the circuit of an op-amp integrator. Derive the output expression. If R = 100kΩ, C = 0.01μF, and Vin = +2V DC step, find Vout after 10ms. What is the problem with an ideal integrator at DC and how is it solved? *(6 marks)*  
**(b)** Explain the characteristics of an ideal op-amp vs practical IC741. Tabulate at least 5 parameters. *(4 marks)*

**16.**  
**(a)** Derive the expression for CMRR of a differential amplifier. An op-amp has Ad = 100,000 and CMRR = 80dB. Find the common-mode gain Ac and calculate the output due to a common-mode signal of 0.1V applied to both inputs. *(6 marks)*  
**(b)** Design a first-order high-pass active filter with fc = 500Hz and passband gain = 3. Specify all component values. *(4 marks)*

**17.**  
**(a)** Explain the sample and hold circuit with a circuit diagram. Explain the role of each component and derive the expression for droop rate. If C = 100pF and leakage = 1pA, find the droop rate in V/s. *(6 marks)*  
**(b)** Explain the flash (parallel type) ADC for n = 3 bits with a truth table showing the input code, comparator output pattern, and digital output. *(4 marks)*

**18.**  
**(a)** An op-amp non-inverting Schmitt trigger has R1 = 22kΩ, R2 = 220kΩ, and Vsat = ±15V. Find UTP, LTP, and the hysteresis width. Sketch the transfer characteristic (Vout vs Vin). *(5 marks)*  
**(b)** Explain the dual slope ADC. An ADC uses T1 = 100ms integration time. If Vref = 5V and Vin = 3V, find the de-integration time T2 and the count ratio. *(5 marks)*

**19.**  
**(a)** Realize Vout = -(5V1 + V2 + 4V3)/2 using a single inverting summing amplifier. Specify all resistor values if Rf = 20kΩ. *(5 marks)*  
**(b)** Design a monostable multivibrator using IC 555 for an output pulse width of 50ms. Choose C = 10μF. Find RA. Sketch the trigger pulse, capacitor voltage, and output pulse. *(5 marks)*

**20.**  
**(a)** Explain the Wien bridge oscillator using an op-amp. Derive the oscillation frequency and explain what gain is required and why. If R = 15kΩ, C = 0.01μF, find f₀ and specify the gain resistors for oscillation. *(6 marks)*  
**(b)** Compare the following ADC types: Flash, SAR, and Dual-slope — with respect to speed, accuracy, complexity, power, and applications. *(4 marks)*

---
*Total: 100 Marks | Pattern follows official KTU CS207 examination structure.*
