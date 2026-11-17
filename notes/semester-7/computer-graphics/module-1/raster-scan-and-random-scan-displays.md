# Raster Scan and Random Scan (Vector) Displays

## 1. Explanation
Display architectures in computer graphics define how electronic signals are translated into illuminated images on physical screens. Historically rooted in Cathode Ray Tube (CRT) physics and modernized in solid-state flat panels, the two fundamental display paradigms are **Raster Scan Displays** and **Random Scan (Vector/Calligraphic) Displays**.

### The Cathode Ray Tube (CRT) Architecture
A CRT operates by generating, accelerating, focusing, and deflecting a high-velocity stream of electrons onto a phosphor-coated glass faceplate:
1. **Electron Gun**: Consists of a heated cathode filament emitting free electrons via thermionic emission, surrounded by a cylindrical control grid that regulates electron beam intensity (brightness).
2. **Focusing and Accelerating Anodes**: Electrostatic or magnetic lenses that converge electrons into a sharp, narrow beam and accelerate them toward the positively charged screen (+15 kV to +30 kV).
3. **Deflection System**: Two pairs of electromagnetic deflection coils (horizontal and vertical deflection yokes) that steer the beam across the display area using Lorentz force: $\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$.
4. **Phosphor Screen**: Absorbs the kinetic energy of striking electrons and emits visible photons (fluorescence during bombardment, and phosphorescence decay). The persistence of the phosphor (time taken for light to drop to 10% of initial intensity) dictates the required refresh rate (typically 60 Hz to 120 Hz) to avoid human visual flicker.

---

### Raster Scan Display Systems
In a **Raster Scan** architecture, the electron beam sweeps across the entire screen systematically, line by line, from top to bottom, regardless of scene complexity.

#### Beam Scanning Pattern
1. **Horizontal Scan**: The beam traverses horizontally from left to right along a row of pixels (scanline), with beam intensity modulated at each pixel clock cycle according to frame buffer data.
2. **Horizontal Retrace**: Upon reaching the right margin, the beam is blanked (turned off) and rapidly deflected back to the left margin of the next scanline below.
3. **Vertical Scan**: Scanlines are progressively painted from the top row to the bottom row of the screen.
4. **Vertical Retrace**: When the beam reaches the bottom-right corner, it is blanked and swept diagonally back to the top-left corner to initiate the next refresh cycle.
5. **Interlacing vs. Non-Interlacing**:
   - *Non-interlaced (Progressive)*: All scanlines (1, 2, 3, 4, ...) are refreshed sequentially in every frame cycle (standard in computer monitors).
   - *Interlaced*: Odd-numbered scanlines (1, 3, 5, ...) are painted in the first field (1/60 s), and even-numbered scanlines (2, 4, 6, ...) are painted in the second field (1/60 s), halving transmission bandwidth while maintaining 60 Hz perceived flicker rate (standard in legacy NTSC/PAL television).

#### System Architecture & Video Controller
The raster scan system operates via dedicated hardware pipelines:
- **Frame Buffer (Refresh Buffer)**: A dedicated region of high-speed memory holding the digital color value for every addressable pixel on screen.
- **Raster Display Controller**: Generates horizontal and vertical synchronization signals (HSync and VSync), increments row and column memory addresses, fetches pixel data from the frame buffer, and feeds it through a Digital-to-Analog Converter (DAC) or Color Lookup Table (LUT) to drive the electron gun.

---

### Random Scan (Vector / Calligraphic / Stroke) Displays
In a **Random Scan** architecture, the electron beam is directed **only** to the parts of the screen where lines and curves are to be drawn. It does not scan the whole screen row by row.

#### Operating Principle
1. The display receives a sequential list of line-drawing commands called a **Display File** (or Display Program) stored in system memory or dedicated display processor memory.
2. The **Display Controller (Display Processing Unit - DPU)** parses commands such as `MOVE_TO(X1, Y1)` and `LINE_TO(X2, Y2)`.
3. Deflection voltages are directly applied to the horizontal and vertical plates to sweep the illuminated beam in a continuous vector from $(X_1, Y_1)$ to $(X_2, Y_2)$.
4. The entire display program is cycled through 30 to 60 times per second to prevent visible phosphor flicker.

---

### Comprehensive Comparative Analysis: Raster Scan vs. Random Scan

| Parameter | Raster Scan Display | Random Scan (Vector) Display |
|---|---|---|
| **Beam Traversal** | Sweeps fixed grid pattern across entire screen (scanline by scanline). | Directed only to specific line segment coordinates (`Point-to-Point`). |
| **Refresh Rate Dependency** | Constant refresh rate (e.g. 60–144 Hz), independent of scene complexity. | Variable refresh rate; depends directly on the number of vectors in display file. If scene has too many lines, flicker occurs. |
| **Resolution** | Discrete pixel resolution (e.g., $1920 \times 1080$). Limited by frame buffer and phosphor pitch. | Extremely high, continuous vector resolution. Smooth lines without pixel discretization. |
| **Aliasing & Jaggies** | Inherently subject to staircase (aliasing) artifacts on diagonal and curved edges. | Zero aliasing; vectors are perfectly continuous, smooth physical line strokes. |
| **Realistic Shading & Image Display** | Excellent. Natively supports solid filled areas, color gradients, photographs, and complex textures. | Very poor. Cannot render solid filled areas or photorealistic shading; limited to wireframe outlines. |
| **Memory Architecture** | Requires a full frame buffer with memory capacity proportional to total pixel count $\times$ bit depth. | Requires a Display Buffer (Display File) storing vector drawing commands proportional to edge count. |
| **Deflection Circuitry** | Sawtooth wave generators; specialized high-speed resonant deflection circuits. | Linear deflection amplifiers; high precision, high voltage, and significantly more expensive. |
| **Primary Historical Applications** | Computer monitors, television, digital video, gaming, photorealistic 3D rendering. | Air traffic control radars, early vector arcade systems (Asteroids), wireframe CAD drafting. |

---

## 2. Example: System Architecture Diagrams

### A. Raster-Scan Architecture
```
+---------------+      System Bus      +--------------------+
|  Application  | <==================> | Frame Buffer (RAM) |
|   Processor   |                      +--------------------+
+---------------+                               │
       │                                        ▼
       ▼                               +--------------------+
+---------------+                      | Video Controller / |
| Memory / Host |                      | Display Controller |
+---------------+                      +--------------------+
                                                │ Pixel Color / Index
                                                ▼
                                       +--------------------+
                                       | Color Lookup Table |
                                       |      (LUT / DAC)   |
                                       +--------------------+
                                                │ Analog RGB Drive
                                                ▼
                                       +--------------------+
                                       |  CRT Display / TV  |
                                       +--------------------+
```

### B. Random-Scan (Vector) Architecture
```
+---------------+      System Bus      +--------------------+
|  Application  | <==================> | Display File (RAM) |
|   Processor   |                      +--------------------+
+---------------+                               │
                                                ▼
                                       +--------------------+
                                       | Display Processor  |
                                       |     Unit (DPU)     |
                                       +--------------------+
                                         │ X, Y Vector Deflection
                                         ▼
                                       +--------------------+
                                       | X-Y Deflection Amp |
                                       +--------------------+
                                                │
                                                ▼
                                       +--------------------+
                                       | Vector CRT Display |
                                       +--------------------+
```

---

## 3. Applications & Use Cases
1. **Air Traffic Control (ATC) Radar Screens**: Historically standardized on vector displays because raw radar returns consist of sharp aircraft track vectors, compass headings, and alphanumeric beacon codes requiring pinpoint sub-millimeter positional precision without aliasing.
2. **Modern GPU Frame Buffers & Video Output Engines**: Modern display pipelines (DisplayPort, HDMI) are the direct evolutionary descendants of raster-scan controllers, maintaining double-buffered and triple-buffered scanout pipelines driving active-matrix OLED/LCD panels at 120–240 Hz.
3. **Oscilloscopes & Medical Vector Monitors**: Vector deflection systems remain the standard for high-bandwidth analog and digital storage oscilloscopes (DSO) where real-time continuous electrical waveforms must be traced without rasterization latency.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Display File Capacity vs. Refresh Flicker in Vector Displays [KTU May 2019 / Dec 2018 Pattern]
**Problem**:
A calligraphic (random scan) vector display has an electron beam deflection speed of $0.5 \text{ mm}/\mu\text{s}$. The beam requires $2 \ \mu\text{s}$ to move without illumination between endpoints (beam positioning time) and $1 \ \mu\text{s}$ to turn the beam on/off.
1. If the average line segment drawn has a physical length of $50 \text{ mm}$, compute the total time required to draw one line segment.
2. To prevent visual flicker, the display file must be refreshed at a minimum rate of 40 Hz. Determine the maximum number of such line segments that can be rendered without introducing flicker.

**Step-by-step Solution**:
1. **Time per Line Segment**:
   - Deflection drawing time:
     $$T_{\text{draw}} = \frac{\text{Distance}}{\text{Speed}} = \frac{50 \text{ mm}}{0.5 \text{ mm}/\mu\text{s}} = 100 \ \mu\text{s}$$
   - Switching and positioning overhead:
     $$T_{\text{overhead}} = T_{\text{position}} + T_{\text{blanking}} = 2 \ \mu\text{s} + 1 \ \mu\text{s} = 3 \ \mu\text{s}$$
   - Total time per line:
     $$T_{\text{line}} = T_{\text{draw}} + T_{\text{overhead}} = 100 + 3 = 103 \ \mu\text{s}$$
2. **Maximum Line Count at 40 Hz**:
   - Available time per refresh period:
     $$T_{\text{period}} = \frac{1}{40 \text{ Hz}} = 0.025 \text{ s} = 25,000 \ \mu\text{s}$$
   - Maximum lines without flicker:
     $$N_{\max} = \left\lfloor \frac{T_{\text{period}}}{T_{\text{line}}} \right\rfloor = \left\lfloor \frac{25,000}{103} \right\rfloor = \lfloor 242.71 \rfloor = 242 \text{ lines}$$
   - If the scene exceeds 242 lines, the refresh rate drops below 40 Hz, causing the display to flicker noticeably.

---

### Example 2: Bandwidth and Memory Transfer Rate in High-Resolution Raster Systems [KTU Dec 2023 Pattern]
**Problem**:
A $4\text{K}$ UHD raster scan monitor with resolution $3840 \times 2160$ runs at 60 Hz non-interlaced with 32-bit color (RGBA).
1. Compute the minimum data transfer rate (bandwidth) required between the frame buffer and the display controller in gigabits per second (Gbps), assuming $20\%$ total blanking overhead (horizontal and vertical blanking combined).
2. What is the video clock frequency (pixel clock frequency) required for this monitor?

**Step-by-step Solution**:
1. **Total Clocked Pixels with Blanking Overhead**:
   $$\text{Active Pixels per Frame} = 3840 \times 2160 = 8,294,400 \text{ pixels}$$
   $$\text{Total Pixels per Frame (accounting for 20\% blanking)} = \frac{8,294,400}{1 - 0.20} = \frac{8,294,400}{0.80} = 10,368,000 \text{ pixels/frame}$$
2. **Pixel Clock Frequency**:
   $$f_{\text{pixel}} = \text{Total Pixels/Frame} \times \text{Refresh Rate} = 10,368,000 \times 60 = 622,080,000 \text{ Hz} \approx 622.08 \text{ MHz}$$
3. **Data Bandwidth**:
   - Bits per pixel $= 32 \text{ bits}$ (4 bytes).
   - Bit rate:
     $$\text{Bandwidth} = f_{\text{pixel}} \times 32 \text{ bits} = 622,080,000 \times 32 = 19,906,560,000 \text{ bps} \approx 19.91 \text{ Gbps}$$
   - This matches the transmission capacity required by modern DisplayPort 1.4 / HDMI 2.0 standards.

---

### Example 3: Shadow-Mask CRT Pitch and Triangular Phosphor Geometry [KTU June 2022 Pattern]
**Problem**:
In a shadow-mask color CRT, the circular holes in the shadow mask are arranged on a hexagonal grid with a center-to-center pitch of $a = 0.28 \text{ mm}$.
1. If the display width is 400 mm, what is the maximum theoretical horizontal resolution (number of addressable triad columns)?
2. Why does addressing the electron beam at a resolution higher than the shadow-mask dot pitch produce moiré fringing patterns rather than greater detail?

**Step-by-step Solution**:
1. **Horizontal Triad Columns**:
   $$\text{Horizontal Triad Count} = \frac{\text{Display Width}}{\text{Mask Pitch}} = \frac{400 \text{ mm}}{0.28 \text{ mm}} \approx 1428.57 \implies 1428 \text{ triads}$$
   The screen can display at most 1428 distinct color pixels along any horizontal scanline before individual triads begin overlapping.
2. **Moiré Fringing Explanation**:
   - When the digital sampling frequency of the scanline beam approaches or exceeds the spatial Nyquist frequency of the physical shadow mask grid ($f_{\text{sample}} \ge \frac{1}{2a}$), spatial optical aliasing occurs.
   - The interference between the regular geometric grid of the shadow mask and the periodic pixel beam pulses produces low-frequency spatial beat frequencies (moiré patterns), appearing as distracting wavy banding across the image.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / January 2023 / June 2024 - 4 Marks]
**Question**:
Differentiate between raster scan and random scan display systems.

**Solution**:
The fundamental differences between raster scan and random scan (vector) display systems are summarized below:

| Feature | Raster Scan Displays | Random Scan Displays |
|---|---|---|
| **Deflection Principle** | The electron beam is swept across the entire screen row-by-row (top to bottom) in a fixed raster pattern. | The electron beam is directed only to the parts of the screen where lines are to be drawn (point-to-point vector motion). |
| **Refresh Rate** | Fixed and constant (typically 60 Hz to 120 Hz), regardless of the complexity or number of primitives in the scene. | Variable; dependent on the total number of lines in the display list. Dense scenes cause the refresh rate to fall, leading to flicker. |
| **Resolution & Visual Quality** | Limited by discrete pixel matrix (e.g. $1920 \times 1080$). Diagonal lines exhibit aliasing ("staircase" or "jaggies"). | Exceptionally high continuous vector resolution. Lines are perfectly smooth with zero aliasing artifacts. |
| **Shading & Solid Areas** | Natively suited for solid filled areas, color gradations, textures, and photorealistic imagery. | Incapable of realistic shading or solid area filling; strictly confined to wireframe line drawings. |
| **Memory Buffer** | Employs a Frame Buffer storing color intensity values for every screen pixel. | Employs a Display Buffer storing drawing commands (`MOVE`, `LINE`). |
| **Circuitry & Cost** | Standard sawtooth sweep generators; low cost and widely commercialized. | Linear deflection amplifiers; highly precise, high voltage, and costly. |

---

### Question 2 [KTU December 2020 / December 2021 - 4 Marks]
**Question**:
Describe a simple raster scan system and draw its architecture.

**Solution**:
1. **Architectural Components**:
   - **System CPU**: Executes the application program and converts geometric descriptions into pixel color values.
   - **System Memory**: Stores application code, geometry data, and OS routines.
   - **Video Controller (Display Controller)**: A dedicated co-processor that directly controls the operation of the display device. It reads pixel data from the frame buffer and cycles through coordinates $(0, 0)$ to $(x_{\max}, y_{\max})$ synchronously with the horizontal and vertical sweeps.
   - **Frame Buffer**: High-speed digital memory mapped directly to the screen pixels. Each memory address corresponds to one pixel location on the screen.
   - **Lookup Table / Video DAC**: Converts digital color values fetched from the frame buffer into analog voltage levels that drive the Red, Green, and Blue electron guns of the CRT (or display panel drive circuits).
2. **Architectural Block Diagram**:
```
+-------------+         System Bus         +--------------+
|     CPU     | <========================> | System RAM   |
+-------------+                            +--------------+
       │                                          │
       ▼                                          ▼
+---------------------------------------------------------+
|                  System Bus Interface                   |
+---------------------------------------------------------+
             │                                │
             ▼                                ▼
   +--------------------+           +-------------------+
   |  Video Controller  |           | Frame Buffer(VRAM)|
   +--------------------+           +-------------------+
             │                                │
             │ Raster Address                 │ Digital Pixel Data
             ▼                                ▼
   +--------------------+           +-------------------+
   | Horizontal/Vertical|           |    Video DAC /    |
   |   Sync Circuits    |           | Color Lookup Table|
   +--------------------+           +-------------------+
             │ HSync, VSync                   │ Analog Video Signals
             ▼                                ▼
   +----------------------------------------------------+
   |               Raster Display Monitor               |
   +----------------------------------------------------+
```
3. **Working Principle**:
   At the start of every frame, the video controller initializes its address register to the origin $(0, 0)$. It issues raster addresses to the frame buffer, reads the color value for the pixel, and increments the address along the scanline. The digital data is converted by the video DAC into beam voltage. When the end of a scanline is reached, the controller issues a horizontal blanking and synchronization pulse (HSync) to reset the beam. When the bottom of the screen is reached, a vertical sync pulse (VSync) resets the beam to the top-left corner.

