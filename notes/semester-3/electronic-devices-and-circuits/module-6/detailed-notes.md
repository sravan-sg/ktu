# Module 6 — ICs, Filters, DAC/ADC, and Timer IC 555: Detailed Notes Index

## Topics

| # | Topic | File | Key Concepts |
|---|-------|------|-------------|
| 1 | Active Filters, DAC/ADC, Timer 555 | [ics-filters-dac-adc-timer555.md](ics-filters-dac-adc-timer555.md) | LPF/HPF 1st/2nd order, R-2R DAC, Binary weighted DAC, S&H, Flash/Dual-slope/SAR ADC, IC 555 astable/monostable |

## Module Summary

Module 6 is also a **20% module** (Part E, 40 marks shared with Module 5):

- **Active LPF/HPF**: Op-amp with RC — 1st order (-20dB/dec), 2nd order (-40dB/dec)
- **DAC specs**: Resolution (1/2ⁿ), monotonicity, settling time
- **Binary weighted DAC**: Simple but needs wide resistor range (impractical for >8 bits)
- **R-2R Ladder DAC**: Only 2 resistor values — preferred for high resolution
- **Sample and Hold**: Captures analog value for ADC conversion; needs low-leakage cap
- **Flash ADC**: Fastest (1 cycle), uses 2ⁿ-1 comparators — for oscilloscopes, radar
- **Dual Slope ADC**: Highest accuracy, noise rejecting — for multimeters
- **SAR ADC**: Best all-around (n cycles, medium accuracy) — for MCUs, sensors
- **IC 555**: 
  - Astable: f = 1.44/(RA+2RB)C, duty = (RA+RB)/(RA+2RB)
  - Monostable: T = 1.1×RA×C

## Previous Year Questions (May 2019)

- Q18b (Part E): Compare binary weighted and R-2R DAC [4 marks]
- Q19b (Part E): Monostable multivibrator using IC 555 [5 marks]
- Q20b (Part E): Design astable 555 for 2kHz, 60% duty cycle [5 marks]
