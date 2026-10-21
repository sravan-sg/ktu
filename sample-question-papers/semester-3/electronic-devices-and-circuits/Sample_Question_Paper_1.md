# CS207 — Electronic Devices and Circuits
## Sample Question Paper 1

**APJ Abdul Kalam Technological University**  
**Third Semester B.Tech Degree Examination**  
**Course Code: CS207 | Course Name: Electronic Devices and Circuits**  
**Max. Marks: 100 | Duration: 3 Hours**  

> At least 60% analytical/numerical/design questions.

---

## PART A

**Answer all questions. Each carries 3 marks.**

**1.** An RC integrating circuit has R = 68kΩ and C = 0.047μF. A 1kHz square wave of amplitude 12V is applied. Calculate τ, check if it is a good integrator, and find the peak output voltage at the end of the positive half cycle.

**2.** Design a zener voltage regulator to provide a regulated output of 6.2V for a load current of 30mA. The input is 15V DC. Assume IZ(knee) = 5mA. Find Rs and its power rating.

**3.** Explain the depletion type MOSFET with its structure and transfer characteristic. Can VGS be both positive and negative? Justify.

**4.** Explain current limiting and foldback protection in a series voltage regulator. What is the advantage of foldback over simple current limiting?

---

## PART B

**Answer any two full questions. Each carries 9 marks.**

**5.**  
**(a)** Draw the circuit of a positive clamper. Explain its operation with waveforms for a sinusoidal input of amplitude 10V. Derive an expression for the output peak voltage. *(4 marks)*  
**(b)** Explain the working of a series voltage regulator using a transistor with a block diagram and feedback mechanism. Derive the expression for its output voltage. *(5 marks)*

**6.**  
**(a)** A biased positive clipper has VR = 4V, and the input is 15 sin(ωt) V. Find the clipping voltage, the fraction of the cycle that is clipped, and sketch the output waveform. *(4 marks)*  
**(b)** With the help of characteristic curves, explain the principle of operation of an enhancement type MOSFET (N-channel). Mark the regions of operation. *(5 marks)*

**7.**  
**(a)** Draw the circuit diagram of a half-wave voltage tripler and explain its working. If the input is 15V peak AC, find the output DC voltage. *(4 marks)*  
**(b)** Design an IC 723 low-voltage regulator to produce Vout = 3.3V. Also calculate the current-limiting resistor for an output current limit of 150mA. *(5 marks)*

---

## PART C

**Answer all questions. Each carries 3 marks.**

**8.** State and explain Barkhausen's criterion for oscillation. What happens if the loop gain |Aβ| > 1?

**9.** Compare enhancement-type and depletion-type MOSFETs with respect to structure, operation, and applications.

**10.** A BJT amplifier has a stability factor S = 3 and ΔICBO = 1μA for a 20°C rise. Find the change in IC. Comment on whether thermal runaway is likely.

**11.** Explain the concept of load line and operating point (Q-point) for a BJT in common-emitter configuration with a DC load line diagram.

---

## PART D

**Answer any two full questions. Each carries 9 marks.**

**12.** Design a voltage divider bias circuit for a BJT amplifier with the following specifications: VCC = 9V, IC = 1.5mA, β = 100, VCE = 4.5V, VE = 0.9V. Find R1, R2, RC, and RE. *(9 marks)*

**13.**  
**(a)** Derive the expression for the frequency of oscillation of a Hartley oscillator. What is the phase shift provided by the tapped LC tank circuit? *(4 marks)*  
**(b)** Explain the working of an astable multivibrator using transistors. If R1 = R2 = 47kΩ and C1 = C2 = 0.01μF, find the frequency and duty cycle of oscillation. *(5 marks)*

**14.** With circuit diagrams and waveforms, explain the working of a monostable multivibrator using transistors. A pulse width of 2ms is required. Design the timing components (R and C). Show the trigger pulse, base voltage, and output voltage waveforms. *(9 marks)*

---

## PART E

**Answer any four full questions. Each carries 10 marks.**

**15.**  
**(a)** Design an inverting amplifier using an op-amp to realize Vout = -8 × Vin. Calculate the output if V1 = 2.5V is applied. Also find the output impedance and phase of the output. *(5 marks)*  
**(b)** Design a second-order Butterworth low-pass filter with cutoff frequency 2kHz and passband gain of 1. Specify all component values. *(5 marks)*

**16.**  
**(a)** Derive the expression for voltage gain of a summing amplifier (inverting) using op-amp. A mixer uses this amplifier with V1 = 1V, V2 = 2V, V3 = 0.5V, R1 = 10kΩ, R2 = 5kΩ, R3 = 20kΩ, Rf = 20kΩ. Calculate Vout. *(6 marks)*  
**(b)** An op-amp has a slew rate of 0.5V/μs. Find the full-power bandwidth for a sinusoidal output of 8V amplitude. What happens to the output waveform above this frequency? *(4 marks)*

**17.**  
**(a)** Explain the successive approximation ADC with a block diagram. Trace the 4-bit SAR conversion for Vin = 7.2V with Vref = 10V. *(6 marks)*  
**(b)** Explain the R-2R ladder DAC. For a 3-bit DAC with Vref = 8V, find the output for input 101₂. *(4 marks)*

**18.**  
**(a)** Design a Schmitt trigger using op-amp for UTP = +3V and LTP = -3V. Assume Vsat = ±12V. Find R1 and R2. Sketch the output waveform for a sinusoidal input of 10V amplitude. *(5 marks)*  
**(b)** Explain the dual slope ADC with a timing diagram. Why is its accuracy independent of R, C, and clock frequency? *(5 marks)*

**19.**  
**(a)** Realize the function Vout = 3V1 - 2V2 using op-amps. Justify the choice of resistor values. *(5 marks)*  
**(b)** Design an astable multivibrator using IC 555 for a frequency of 5kHz and duty cycle of 70%. Specify RA, RB, and C. *(5 marks)*

**20.**  
**(a)** Draw the circuit of a differentiator using an op-amp. Derive the output expression. If R = 10kΩ, C = 0.1μF, and the input is a 500Hz square wave of amplitude 6V, sketch the output waveform. *(5 marks)*  
**(b)** Draw and explain the flash (parallel) ADC for 3-bit conversion. What are its advantages and limitations compared to SAR ADC? *(5 marks)*

---
*Total: 100 Marks | Minimum 60% analytical/numerical questions satisfied.*
