# Module 2 Revision Notes — Regulated Power Supplies and FETs

## Regulator Formulas

| Regulator | Output Voltage | Key Formula |
|-----------|---------------|-------------|
| Zener | VZ | Rs = (Vin - VZ)/(IZ + IL) |
| Series (IC 723 HV) | Vref × (1 + R1/R2) | Vout = 7.15 × (1 + R1/R2) |
| Series (IC 723 LV) | Vref × R2/(R1+R2) | Vout = 7.15 × R2/(R1+R2) |
| 78XX | Fixed (05=5V, 12=12V) | Min Vin = Vout + 2V (dropout) |
| SMPS Buck | Vin × D | D = duty cycle |

## FET Quick Reference

| Parameter | JFET | Enhancement MOSFET | Depletion MOSFET |
|-----------|------|-------------------|-----------------|
| Channel at VGS=0 | Yes (N-ch) | No | Yes |
| ID equation | IDSS(1-VGS/VP)² | K(VGS-VT)² | IDSS(1-VGS/VP)² |
| Gate current | ~nA | ~pA | ~pA |
| Typical use | LNA, analog switch | CMOS logic | Analog switch |

## SMPS Block Sequence

AC Mains → EMI Filter → Bridge Rectifier + C → HF Switch (MOSFET) → Transformer → Output Rectifier + Filter → Vout → Feedback → PWM Controller → back to Switch

## Key Points

- IC 723: Vref = 7.15V internally. Low voltage mode: Vout < 7.15V (voltage divider at V+). High voltage: Vout > 7.15V (R1 from Vout, R2 to V-).
- SMPS efficiency 80-90% vs linear 30-50% — the trade-off is complexity and EMI.
- Current limiting resistor: RSC = 0.7V / I_limit (simple constant-current limiting)
- Foldback protection reduces current as voltage drops — safer for the pass transistor.
