# Module 1: Revision Notes — Quick Review Guide

## 1. High-Yield Summary
- **Computer Graphics Core Paradigm**: Maps abstract continuous mathematical geometry into discrete, quantized pixel grids stored in frame buffer memory.
- **Interactive Input Classes**:
  - *Locator*: Returns coordinate $(x, y)$ (Mouse, Trackball).
  - *Stroke*: Returns coordinate sequence $(\vec{p}_1, \dots, \vec{p}_n)$ (Stylus, Digitizer).
  - *String*: Returns character text (Keyboard).
  - *Valuator*: Returns continuous scalar value (Potentiometer dial, Fader).
  - *Choice*: Returns discrete enumerated menu option (Function key, Buttons).
  - *Pick*: Returns object handle/primitive ID (Mouse pick-ray, Touch hit).
- **Raster Scan vs. Random Scan**:
  - *Raster Scan*: Scans all lines top-to-bottom sequentially. Constant refresh rate (60–144 Hz). Suffers from aliasing/staircasing. Natively supports solid filling, photos, textures. Uses Frame Buffer.
  - *Random Scan*: Deflects beam directly between vector endpoints. Refresh rate depends on scene complexity (lines drawn). Zero aliasing (continuous strokes). Cannot render realistic solid shading. Uses Display File.

---

## 2. Essential Mathematical Formulas & Calculations

### Aspect Ratio
$$\text{Aspect Ratio} = \frac{\text{Width}}{\text{Height}} = \frac{W}{H}$$

### Pixel Density & Dot Pitch
$$D_{\text{pixels}} = \sqrt{W^2 + H^2}$$
$$\text{PPI} = \frac{D_{\text{pixels}}}{\text{Diagonal Size in Inches}}, \quad \text{Dot Pitch (mm)} = \frac{25.4}{\text{PPI}}$$

### Frame Buffer Memory Capacity
$$\text{Capacity (Bytes)} = \frac{W \times H \times \text{Bits per Pixel (bpp)}}{8}$$

### Color Palette with Lookup Table (LUT)
$$\text{Simultaneous Colors} = 2^{\text{Frame Buffer Bit Depth}}$$
$$\text{Total Color Palette} = 2^{\text{LUT Entry Bit Depth}}$$
*(Example: 8-bit frame buffer with 24-bit LUT entries allows 256 simultaneous colors from a palette of 16.7 million colors).*

### Video Display Bandwidth
$$f_{\text{pixel}} = \frac{W \times H}{1 - \text{Retrace Fraction}} \times \text{Refresh Rate (Hz)}$$
$$\text{Bandwidth (bps)} = f_{\text{pixel}} \times \text{bpp}$$

---

## 3. Core Comparison Table: Raster vs. Random Scan

| Parameter | Raster Scan Displays | Random Scan Displays |
|---|---|---|
| **Beam Deflection** | Systematic row-by-row sawtooth sweep | Point-to-point line segments |
| **Refresh Rate** | Fixed (60–120 Hz); independent of complexity | Variable; drops if line count is high (flicker) |
| **Aliasing** | Present (jaggies on non-aligned edges) | Zero aliasing (smooth physical vector lines) |
| **Area Fill & Shading** | Natively supported (polygons, photorealism) | Not supported (wireframe outlines only) |
| **Memory Buffer** | Frame Buffer (stores color per pixel) | Display Buffer (stores drawing commands) |

---

## 4. Top 3 Exam Traps & Tips
1. **Don't Forget the Color Lookup Table**: When asked how to display 256 colors from a 16.7 million color palette, do not say "use 24 bits in the frame buffer". Explain that each pixel in the frame buffer stores an **8-bit index** into a $256 \times 24$-bit LUT.
2. **Horizontal vs. Vertical Retrace**: Remember that horizontal retrace occurs at the end of **every single scanline**, while vertical retrace occurs **once per full frame refresh**.
3. **Random Scan Flicker Threshold**: If a numerical question asks for the maximum number of vectors in a random scan display, ensure you account for both line drawing time and beam repositioning/blanking overhead: $T_{\text{line}} = T_{\text{draw}} + T_{\text{position}} + T_{\text{blanking}}$.

