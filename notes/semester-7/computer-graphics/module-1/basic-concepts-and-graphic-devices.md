# Basic Concepts in Computer Graphics & Graphic Devices

## 1. Explanation

Computer graphics is the art and science of synthesizing, manipulating, and displaying visual content using computational processors and dedicated display hardware. At its mathematical core, computer graphics establishes a bridge between abstract numerical models (points, lines, algebraic curves, 3D meshes) and physical display rasters composed of discrete light-emitting elements (pixels).

The discipline answers three fundamental engineering questions:
- **What** to display (scene representation, geometry, materials, lighting)
- **How** to display it (rendering pipeline, rasterization, shading)
- **Which hardware** handles the input and output of that information

---

### The Classical Graphics Pipeline

The generation of imagery on a digital screen follows an algorithmic progression — each stage transforms data closer to what the display hardware can consume:

```
Application Model
    │
    ▼  [Geometric Modeling — objects defined in local/model coordinates]
World Coordinates
    │
    ▼  [Viewing & Camera Transform — world seen from eye/camera origin]
View/Eye Coordinates
    │
    ▼  [Clipping — frustum culling removes geometry outside view volume]
Clip Coordinates
    │
    ▼  [Perspective Division → NDC: [-1,1]³ or [0,1]³]
Normalized Device Coordinates (NDC)
    │
    ▼  [Viewport Mapping — NDC mapped to physical screen pixels]
Device / Screen Coordinates
    │
    ▼  [Rasterization — vector primitives discretized to pixel grid]
Frame Buffer (pixels × bits-per-pixel)
    │
    ▼  [Scanout — Video Controller reads frame buffer; DAC drives signal]
Physical Display Pixels
```

**Coordinate System Details:**
1. **Model Coordinates (MC)**: Geometry defined in object-local frame. A car model's wheel is centered at the wheel hub origin.
2. **World Coordinates (WC)**: Multiple objects assembled in a shared virtual environment via model matrix transforms (translate, rotate, scale).
3. **View Coordinates (VC)**: World transformed relative to the observer's virtual camera. The camera sits at origin looking down the -Z axis.
4. **Clip/Homogeneous Coordinates**: 4D homogeneous representation enables perspective division and allows the hardware frustum culling to test against the view volume in a unified way.
5. **NDC (Normalized Device Coordinates)**: The clip cube mapped to [-1, 1]³. Hardware-independent. OpenGL uses this.
6. **Device Coordinates (DC)**: The viewport transform maps NDC into pixel addresses (integers) on the actual framebuffer.

---

### The OpenGL Programmable Graphics Pipeline (GPU Stages)

Modern real-time graphics replaced the fixed-function pipeline with a **fully programmable GPU pipeline**. Understanding each stage is essential:

```
CPU Application
    │  Vertex Buffer Objects (VBOs), Index Buffers → GPU
    ▼
┌──────────────────────────────────────────┐
│          VERTEX SHADER (Programmable)     │
│  Input: per-vertex attributes             │
│  (position, normal, UV, color)            │
│  Output: gl_Position (clip coordinates)  │
│  Operations: MVP transform, lighting calc │
└──────────────────────────┬───────────────┘
                           │
                           ▼
┌──────────────────────────────────────────┐
│       GEOMETRY SHADER (Optional/Prog.)    │
│  Input: complete primitive (triangle)     │
│  Can emit NEW primitives (particle sys.)  │
│  Used in: shadow volume generation,       │
│  cube-map rendering, tessellation         │
└──────────────────────────┬───────────────┘
                           │
                           ▼
┌──────────────────────────────────────────┐
│     RASTERIZATION (Fixed Function)        │
│  Converts vector triangles → fragments    │
│  (potential pixels). Interpolates:        │
│  UV, colors, normals across each triangle │
│  Performs depth (Z) interpolation         │
│  Applies perspective-correct interpolation│
└──────────────────────────┬───────────────┘
                           │
                           ▼
┌──────────────────────────────────────────┐
│       FRAGMENT SHADER (Programmable)      │
│  Input: interpolated fragment data        │
│  Output: final RGBA color                 │
│  Operations: texture sampling, lighting,  │
│  per-pixel effects, shadow mapping,       │
│  bump/normal mapping, PBR shading         │
└──────────────────────────┬───────────────┘
                           │
                           ▼
┌──────────────────────────────────────────┐
│       OUTPUT MERGER / ROP Stage           │
│  Depth Test (Z-buffer): discard occluded  │
│  Stencil Test: masking effects            │
│  Alpha Blending: transparency compositing │
│  Final write to: Color Buffer + Depth Buf │
└──────────────────────────────────────────┘
```

**Why each stage matters:**
- **Vertex Shader** runs once per vertex (thousands of calls per frame). Costly geometric transforms happen here.
- **Geometry Shader** can amplify or reduce primitive count. Particle systems emit many quads from one point.
- **Rasterization** is *fixed hardware* — it cannot be programmed but is extremely fast (billions of samples per second).
- **Fragment Shader** runs once per *fragment* (screen pixel candidate). With 4K at 60 Hz, this is billions of invocations per second — the most expensive stage in photorealistic rendering.
- **Output Merger** ensures correct depth ordering and blending without requiring scene-level sorting.

---

### Taxonomy of Graphic Devices

Graphic devices are partitioned into **Input Devices** (capturing human spatial intent) and **Display/Output Devices** (rendering spatial signals).

#### Logical Input Device Classes (Foley & Van Dam Classification)

Interactive computer graphics categorizes input hardware not merely by physical packaging, but by the **logical input primitive** it delivers to the operating system:

| Class | Data Returned | Physical Examples |
|---|---|---|
| **Locator** | Single (x, y) coordinate position | Mouse, graphics tablet, trackball, joystick |
| **Stroke** | Ordered sequence of (x, y) positions | Stylus on digitizer tablet, light pen |
| **String** | ASCII/Unicode character sequence | Keyboard, touch-screen IME |
| **Valuator** | Single scalar floating-point number | Rotary potentiometer, slide fader, scroll wheel |
| **Choice** | Discrete integer from an enumeration | Function keys, hardware buttons, mouse click |
| **Pick** | Identifier of an existing rendered object | Mouse pick-ray, touch-screen hit test |

---

#### Physical Input Device Deep Dives

##### 1. Mouse (Optical Quadrature Encoder)
Modern optical mice use an LED illuminator (or laser diode) shining onto the desk surface. A CMOS image sensor captures frames at 3,000–6,000 FPS. A DSP chip performs cross-correlation between consecutive frames to compute ΔX and ΔY displacement vectors. These deltas are reported to the OS, which translates them to screen cursor motion.

**Key physics:** The system acts as a locator device. Picking up and placing a mouse does NOT change the cursor position because there is no absolute position tracking — only incremental displacement reporting. The sensor only measures relative motion between consecutive frames; when lifted, there is no surface feedback, so no motion is reported.

> **[Dec 2018, Q13a Insight]:** A mouse is picked up and placed in another position — does the pointer move? **No.** The optical sensor requires surface contact (tracked texture changes) to register motion. Lifting the mouse breaks optical correlation. The pointer only moves in response to relative displacement while the mouse is in contact with a tracking surface.

##### 2. Joystick (Potentiometer Voltage Divider Mechanism)
A joystick encodes position using **dual-axis potentiometers** — one for X-axis, one for Y-axis.

**Physics of operation:**
```
+Vcc (5V)
   │
  [R_total (10kΩ)]  ← Full resistance of potentiometer wire
   │
  Wiper ──────────► ADC Pin (Analog-to-Digital Converter)
   │
  GND (0V)
```

When the joystick stick is at center, the wiper is at midpoint of the resistive element: V_out = Vcc/2 = 2.5V. When pushed fully forward (X+), the wiper sweeps to one end: V_out → 5V. When pushed fully backward (X−), V_out → 0V. The microcontroller's ADC samples V_out at 10-bit resolution (0–1023), giving 1024 discrete positions per axis.

**Deadzone compensation:** A software deadzone (typically ±5% of center voltage = 2.375V to 2.625V) prevents cursor drift from mechanical slack at neutral position.

**Logical classification:** Joystick acts as a **Locator** (reports absolute X, Y within its range) or as a **Valuator** (when only one axis is used, e.g., throttle control).

##### 3. Light Pen (Photodiode + Raster Synchronization)
A light pen is a photosensitive stylus pressed directly against the CRT screen surface to identify which pixel location is being scanned.

**Detailed operation:**
1. The CRT electron beam sweeps each scanline at a precisely synchronized rate governed by horizontal sync pulses.
2. Inside the light pen tip is a **photodiode** (or phototransistor) sensitive to visible light emission.
3. When the raster beam sweeps past the exact spot where the pen is resting, the phosphor flashes. This creates a sharp pulse of photocurrent in the photodiode.
4. This photocurrent pulse is amplified and fed to an interrupt line connected to the video controller.
5. The video controller reads its **current X (column counter) and Y (scanline counter)** register values at the instant the interrupt fires. These register values directly correspond to the beam's current $(x, y)$ position on the screen — which is the pen's location.

**Timing precision:** Because the beam sweeps the full screen in ~16.67 ms (60 Hz), and horizontal resolution may be 1280 pixels, each pixel column represents only ~6–10 nanoseconds. The interrupt must be detected within this window.

**Limitation:** Cannot work in ambient light (sunlight triggers false positives). Cannot work on flat panel LCDs (no scanning electron beam).

##### 4. Touch Panel (Resistive vs. Capacitive)
Touch panels are surface overlays detecting finger/stylus contact without mechanical parts.

**Resistive Touch Panel (4-wire):**
```
Top ITO Layer (flexible, horizontal electrode)
         ┊ (air gap, ~0.1mm)
Bottom ITO Layer (rigid, vertical electrode)
```
When pressed, the flexible top layer contacts the bottom layer. The controller alternately:
- Applies voltage across X-axis electrodes → measures Y position from ADC on opposite pair
- Applies voltage across Y-axis electrodes → measures X position from ADC on opposite pair

**Advantages:** Works with glove, stylus, or any object. Low cost. High accuracy with stylus.
**Disadvantages:** Requires physical pressure. Layers wear over time. Poorer optical clarity.

**Capacitive Touch Panel (Projected Capacitance — PCAP):**
A grid of ITO (Indium Tin Oxide) electrodes creates a sensing matrix. Each finger's conductive skin capacitively couples to the nearest grid electrodes. A touch controller IC measures the change in capacitance at each intersection point (mutual capacitance method) or at each electrode (self-capacitance). Multi-touch tracking is native — multiple fingers show multiple distinct capacitance anomalies simultaneously.

**Advantages:** No pressure required. Multi-touch capable. No mechanical wear. High optical transparency.
**Disadvantages:** Requires conductive input (bare finger). Cannot work with regular gloves.

##### 5. Data Tablet / Digitizing Tablet (Electromagnetic Induction)
A data tablet (digitizer) uses **electromagnetic induction** between a powered grid of wires embedded in the tablet surface and a passive stylus (pen) containing a resonant LC circuit.

**Operating principle:**
1. The tablet electronics sequentially activate horizontal and vertical grid wires with an AC electromagnetic pulse.
2. The stylus tip contains an inductor (coil) and capacitor forming a resonant LC circuit tuned to the tablet's frequency.
3. When a grid wire is energized, it magnetically couples to the stylus coil, inducing an AC voltage. When the drive pulse ends, the stylus LC circuit rings at its resonant frequency.
4. The tablet electronics sense this echo response from each horizontal and vertical strip to triangulate the stylus's exact (X, Y) position with sub-millimeter precision.
5. Additionally, the stylus tip acts as a pressure transducer — compression changes the LC resonant frequency, enabling **pressure sensitivity** (up to 8192 pressure levels in professional Wacom tablets).

**Key advantage:** The stylus is completely passive — no battery required. The energy comes inductively from the tablet's electromagnetic field.

##### 6. Digital Glove (Flex Sensor Array)
A data glove encodes finger joint angles by embedding **flex sensors** along each finger.

**Flex sensor physics:**
A flex sensor consists of a resistive carbon-polymer film printed on a flexible polyester substrate. When the sensor bends:
- **Unbent (straight finger):** Resistance ≈ 10 kΩ
- **Bent 90°:** Resistance ≈ 25–35 kΩ
- **Bent 180°:** Resistance ≈ 60–90 kΩ

This change in resistance is read using a voltage divider circuit, converted by ADC, and mapped to joint angles via calibration tables. A typical glove uses 5 flex sensors (one per finger) or 10–18 for more precision (metacarpal + proximal joints). An IMU (accelerometer + gyroscope) on the back of the hand tracks orientation.

**Application in VR:** The digital glove provides a **stroke device** (continuous trajectory as hand gestures unfold) and a **choice device** (specific hand poses map to commands).

---

### Color Representation Systems

#### RGB Color Model
The additive primary color model used in all self-luminous displays (CRT, OLED, QLED):
$$\text{Color} = (R, G, B), \quad R, G, B \in [0, 1] \text{ or } [0, 255]$$

Color mixing is **additive**: R + G = Yellow, R + B = Magenta, G + B = Cyan, R + G + B = White.

**Why additive?** Display pixels emit light. Combining different wavelength emissions simply adds photon flux (energy), producing brighter mixed colors.

#### CMY/CMYK Color Model
The subtractive primary model used in physical printing:
$$C = 1 - R, \quad M = 1 - G, \quad Y = 1 - B$$

Color mixing is **subtractive**: pigments absorb (subtract) wavelengths from white incident light. Cyan absorbs red, Magenta absorbs green, Yellow absorbs blue.

**Conversion from RGB to CMY:**
$$\begin{pmatrix}C \\ M \\ Y\end{pmatrix} = \begin{pmatrix}1 \\ 1 \\ 1\end{pmatrix} - \begin{pmatrix}R \\ G \\ B\end{pmatrix}$$

#### HSV (Hue-Saturation-Value) Color Model
A perceptually intuitive cylindrical color model matching human perception of color:
- **Hue (H)**: Angular position on color wheel, 0°–360°. 0°=Red, 120°=Green, 240°=Blue.
- **Saturation (S)**: Purity of color; 0 = gray (fully desaturated), 1 = fully saturated vivid color.
- **Value (V)**: Brightness; 0 = black, 1 = maximum brightness.

**RGB → HSV Conversion algorithm:**
```
Given: R, G, B ∈ [0, 1]
  Cmax = max(R, G, B)
  Cmin = min(R, G, B)
  Δ    = Cmax - Cmin

  V = Cmax

  S = 0           if Cmax = 0
  S = Δ / Cmax    otherwise

  H = 0 if Δ = 0
  H = 60 × [(G − B)/Δ mod 6]   if Cmax = R
  H = 60 × [(B − R)/Δ + 2]     if Cmax = G
  H = 60 × [(R − G)/Δ + 4]     if Cmax = B
```

**Why HSV is preferred for color pickers:** Designers naturally think in terms of "choose a hue, then adjust brightness/saturation" — the HSV model matches this mental model directly. RGB is a hardware model, not a perceptual one.

---

### Pixel Storage Formats and Frame Buffer Sizing

#### Common Pixel Formats

| Format | Bits/Pixel | Channel Layout | Notes |
|---|---|---|---|
| **1bpp Monochrome** | 1 | B&W only | Bitmap text |
| **4bpp Indexed** | 4 | 16-color palette index | CGA era |
| **8bpp Indexed** | 8 | 256-color LUT index | GIF, 256-color VGA |
| **RGB565** | 16 | R(5) G(6) B(5) | Mobile/embedded displays |
| **RGB888 / 24bpp** | 24 | R(8) G(8) B(8) | True Color |
| **ARGB8888 / 32bpp** | 32 | A(8) R(8) G(8) B(8) | True Color + Alpha channel |
| **HDR10 (10bpp/ch)** | 30+ | R(10) G(10) B(10) | High Dynamic Range displays |

**Why RGB565 uses 6 bits for green:** The human eye has approximately 3× more green photoreceptors (M-cones) than red or blue. Human green sensitivity covers a wider spectral range, so more gray levels in green produce more perceptually uniform results.

**ARGB8888 (32-bit) memory layout:**
```
Bit 31-24   │  Bit 23-16  │  Bit 15-8   │  Bit 7-0
  Alpha (A) │   Red (R)   │  Green (G)  │  Blue (B)
  8 bits    │   8 bits    │   8 bits    │  8 bits
  0–255     │   0–255     │   0–255     │  0–255
  transparency             color data
```

#### Frame Buffer Size Formula

$$\text{Frame Buffer Size (bytes)} = \frac{H \times V \times B}{8}$$

Where:
- $H$ = Horizontal pixel count (width)
- $V$ = Vertical pixel count (height)
- $B$ = Bits per pixel (color depth)

**Example quick reference:**

| Resolution | 1 bpp | 8 bpp | 12 bpp | 24 bpp | 32 bpp |
|---|---|---|---|---|---|
| 640 × 480 | 37.5 KB | 300 KB | 450 KB | 900 KB | 1.2 MB |
| 1280 × 1024 | 160 KB | 1.28 MB | 1.92 MB | 3.84 MB | 5.12 MB |
| 1920 × 1080 | 247.5 KB | 1.98 MB | 2.97 MB | 5.93 MB | 7.91 MB |
| 2560 × 2048 | 640 KB | 5.12 MB | 7.68 MB | 15.36 MB | 20.48 MB |

---

### Display Resolution and Aspect Ratio — Formal Definitions

**Resolution:** The total number of distinct addressable pixel positions the display can render across horizontal ($H$) and vertical ($V$) dimensions, stated as $H \times V$ (e.g., $1920 \times 1080$).

**Aspect Ratio:** The ratio of the display's physical width to its physical height, expressed in lowest integer terms:
$$\text{AR} = \frac{W}{H} = \frac{W/\gcd(W,H)}{H/\gcd(W,H)}$$

For square pixels (which modern monitors assume): the pixel aspect ratio equals the display aspect ratio.

**Common Aspect Ratios:**

| Resolution | Aspect Ratio | Standard |
|---|---|---|
| 640 × 480 | 4:3 | VGA (NTSC) |
| 1024 × 768 | 4:3 | XGA |
| 1280 × 720 | 16:9 | HD |
| 1920 × 1080 | 16:9 | Full HD (FHD) |
| 2560 × 1600 | 16:10 | WQXGA |
| 3840 × 2160 | 16:9 | 4K UHD |
| 800 × 1000 | 4:5 | Portrait (8"×10" at 100 PPI) |

---

## 2. Example: System Diagrams

### A. Logical Input Device Classification Architecture

```
+-------------------------------------------------------------------------+
|                         APPLICATION PROGRAM                             |
|  "What data type does this operation need?"                             |
+-------------------------------------------------------------------------+
        ▲                     ▲                      ▲               ▲
        | (x, y)              | [(x₁,y₁)…(xₙ,yₙ)]   | Scalar value  | Object ID
        ▼                     ▼                      ▼               ▼
+---------------+     +---------------+     +---------------+ +---------------+
| LOCATOR CLASS |     |  STROKE CLASS |     | VALUATOR CLASS| |  PICK CLASS   |
| "Position"    |     | "Path/Trace"  |     | "Quantity"    | | "Select Obj." |
+---------------+     +---------------+     +---------------+ +---------------+
        ▲                     ▲                      ▲               ▲
  Mouse/Tablet          Stylus/Light Pen        Potentiometer    Ray-Caster
  Joystick/Touch        Finger swipe            Slider/Dial      Bounding Box
```

### B. Raster-Scan System with Frame Buffer Architecture

```
+------------------+       PCI-e Bus        +--------------------+
|    CPU           | ══════════════════════► | GPU Frame Buffer   |
| (Application)    |                         | (VRAM — GDDR6)     |
+------------------+                         +--------------------+
                                                        │
                              ┌─────────────────────────┘
                              ▼
                    +--------------------+
                    | Video Controller   |
                    | (Display Engine)   |
                    | • HSync / VSync    |
                    | • Scanline counter |
                    | • Address gen.     |
                    +--------------------+
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
      +-------------+   +---------+   +-------------+
      | Color LUT   |   |  DAC-R  |   |  DAC-G/B    |
      | (Palette)   |   +---------+   +-------------+
      +-------------+         │               │
                              ▼               ▼
                    +------------------------------------+
                    |   Analog RGB Signals to Display    |
                    |   (or Digital HDMI/DisplayPort)    |
                    +------------------------------------+
                                   │
                                   ▼
                    +------------------------------------+
                    |     Physical Display Monitor       |
                    |   (CRT / LCD / OLED / QLED)       |
                    +------------------------------------+
```

---

## 3. Applications & Use Cases

### 1. Computer-Aided Design (CAD/CAM)
High-precision digitizing tablets (stroke + locator devices) allow structural engineers to trace physical engineering blueprints directly into vector CAD representations (AutoCAD, CATIA, SolidWorks). The electromagnetic induction pen delivers sub-millimeter accuracy unachievable by mouse. Pressure sensitivity enables line weight variation in technical drafting.

### 2. Medical Imaging (PACS Workstations)
Radiologists use 3D space-mice (6-DOF locator + valuator devices) to slice, rotate, and pick anatomical landmarks in volumetric MRI and CT scan reconstructions. The touch panel overlay on diagnostic monitors allows natural pointing to lesion locations without click latency.

### 3. Virtual Reality / VR Systems
Digital gloves (flex sensor arrays) enable natural hand gesture recognition in VR environments. Combined with IMUs for hand orientation tracking, they provide immersive pick and stroke interactions without controller buttons. Used in surgical training simulators and industrial assembly VR.

### 4. Digital Audio Workstations (DAW)
Hardware mixing boards utilize arrays of motorized slide faders (valuator devices) and rotary encoders to control track gain and panning in real time. When a saved mix project is recalled, the motorized faders physically move to their saved positions — a mechanical feedback form of actuated valuator.

### 5. Gaming and Interactive Entertainment
Modern gaming mice (8,000+ DPI optical sensors) are precision locator devices. Joystick gamepads with analog thumbsticks (potentiometer voltage dividers) provide smooth continuous directional control, contrasting with binary digital D-pads.

### 6. Industrial Control and Robotics
Touchscreens (capacitive) in PLC control panels use the choice class — operators tap pre-rendered buttons on screen. For precision robotic arm positioning, 3D digitizing tablets with active electromagnetic styli provide full 6-DOF coordinate input (x, y, z, roll, pitch, yaw).

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Aspect Ratio of 8×10 Inch Screen at 100 Pixels/Inch [KTU June 2022, Q2 / Dec 2019 Q1]

**Problem:**
A raster system uses an 8 inch × 10 inch screen (width × height) with a resolution of 100 pixels per inch in each direction.
1. Find the total number of pixels (horizontal × vertical).
2. Determine the aspect ratio of the display.
3. If 6 bits are stored per pixel, calculate the required frame buffer size in bytes.

**Step-by-step Solution:**

**Step 1: Total Pixel Count**
$$H = 8 \text{ inches} \times 100 \text{ pixels/inch} = 800 \text{ pixels (horizontal)}$$
$$V = 10 \text{ inches} \times 100 \text{ pixels/inch} = 1000 \text{ pixels (vertical)}$$

**Step 2: Aspect Ratio**
$$\gcd(800, 1000) = 200$$
$$\text{Aspect Ratio} = \frac{800/200}{1000/200} = \frac{4}{5} = 4:5$$

The screen is taller than it is wide (portrait orientation). Note: 8-inch width × 10-inch height → 4:5 (width:height).

**Step 3: Frame Buffer Size at 6 bpp**
$$\text{Frame Buffer} = \frac{H \times V \times B}{8} = \frac{800 \times 1000 \times 6}{8} = \frac{4,800,000}{8} = 600,000 \text{ bytes} = 600 \text{ KB}$$

**Conclusion:** The 8×10 inch monitor at 100 PPI has 800×1000 pixel resolution, a 4:5 aspect ratio, and requires 600 KB of frame buffer memory at 6 bits per pixel.

---

### Example 2: Frame Buffer Sizes for Multiple Resolutions at 12-bit and 24-bit Color [KTU Dec 2020, Q11a / May 2019]

**Problem:**
Consider three different raster systems with resolutions of:
- System A: 640 × 480
- System B: 1280 × 1024
- System C: 2560 × 2048

For each system, compute the frame buffer size (in bytes) needed to store:
(i) 12 bits per pixel
(ii) 24 bits per pixel

**Step-by-step Solution:**

**Formula:**
$$\text{Frame Buffer (bytes)} = \frac{H \times V \times \text{bpp}}{8}$$

**System A: 640 × 480**

Total pixels $= 640 \times 480 = 307,200$

At 12 bpp:
$$\text{Size} = \frac{307,200 \times 12}{8} = \frac{3,686,400}{8} = 460,800 \text{ bytes} \approx 450 \text{ KB}$$

At 24 bpp:
$$\text{Size} = \frac{307,200 \times 24}{8} = \frac{7,372,800}{8} = 921,600 \text{ bytes} = 900 \text{ KB}$$

**System B: 1280 × 1024**

Total pixels $= 1,310,720$

At 12 bpp:
$$\text{Size} = \frac{1,310,720 \times 12}{8} = \frac{15,728,640}{8} = 1,966,080 \text{ bytes} = 1.875 \text{ MB}$$

At 24 bpp:
$$\text{Size} = \frac{1,310,720 \times 24}{8} = \frac{31,457,280}{8} = 3,932,160 \text{ bytes} = 3.75 \text{ MB}$$

**System C: 2560 × 2048**

Total pixels $= 2,560 \times 2,048 = 5,242,880$

At 12 bpp:
$$\text{Size} = \frac{5,242,880 \times 12}{8} = \frac{62,914,560}{8} = 7,864,320 \text{ bytes} \approx 7.5 \text{ MB}$$

At 24 bpp:
$$\text{Size} = \frac{5,242,880 \times 24}{8} = \frac{125,829,120}{8} = 15,728,640 \text{ bytes} = 15 \text{ MB}$$

**Summary Table:**

| System | Resolution | Pixels | 12-bit Buffer | 24-bit Buffer |
|---|---|---|---|---|
| A | 640 × 480 | 307,200 | 450 KB | 900 KB |
| B | 1280 × 1024 | 1,310,720 | 1.875 MB | 3.75 MB |
| C | 2560 × 2048 | 5,242,880 | 7.5 MB | 15 MB |

---

### Example 3: Color Lookup Table (LUT) Memory Analysis & RGB→HSV Color Conversion [KTU Dec 2021 / May 2019 Pattern]

**Part A: Color Lookup Table Memory Comparison**

**Problem:**
A legacy graphics display system uses an 8-bit frame buffer indexing a 24-bit True Color DAC.
1. How many colors are simultaneously displayable?
2. What is the total palette size?
3. Compare LUT memory vs. direct 24-bit True Color for 1024 × 768 resolution.

**Solution:**

1. **Simultaneously Displayable Colors:**
   - 8-bit index → $2^8 = 256$ distinct colors on screen at once.

2. **Total Palette:**
   - Each LUT entry = 24 bits (8R + 8G + 8B) → $2^{24} = 16,777,216$ possible colors to choose from.

3. **Memory Comparison (1024 × 768 screen):**
   - **LUT Architecture:**
     - Frame Buffer: $1024 \times 768 \times 1\text{ byte} = 786,432\text{ bytes} = 768\text{ KB}$
     - LUT Table: $256 \text{ entries} \times 3\text{ bytes/entry} = 768\text{ bytes}$
     - Total: $768\text{ KB} + 0.75\text{ KB} \approx 768.75\text{ KB}$
   - **Direct 24-bit True Color:**
     - Frame Buffer: $1024 \times 768 \times 3\text{ bytes} = 2,359,296\text{ bytes} = 2.25\text{ MB}$
   - **Memory savings factor:** $2304\text{ KB} / 768.75\text{ KB} \approx 3\times$ reduction using LUT.

**Part B: RGB to HSV Conversion**

**Problem:** Convert the pure blue color RGB = (0, 0, 255) to HSV notation.

**Solution:**

Normalize to [0,1]: R = 0, G = 0, B = 1.

$$C_{max} = \max(0, 0, 1) = 1 \quad (B \text{ is maximum})$$
$$C_{min} = \min(0, 0, 1) = 0$$
$$\Delta = C_{max} - C_{min} = 1 - 0 = 1$$

**Value (V):**
$$V = C_{max} = 1 \quad (\text{full brightness})$$

**Saturation (S):**
$$S = \frac{\Delta}{C_{max}} = \frac{1}{1} = 1 \quad (\text{fully saturated})$$

**Hue (H):** (Since B = Cmax):
$$H = 60 \times \left[\frac{R - G}{\Delta} + 4\right] = 60 \times \left[\frac{0 - 0}{1} + 4\right] = 60 \times 4 = 240°$$

**Result:** Pure blue RGB(0, 0, 255) = **HSV(240°, 1.0, 1.0)** — 240° on the color wheel, fully saturated, full brightness.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [KTU January 2023, Q11b / June 2024, Q11b — 5 Marks]
**Question:** Explain the architecture of a raster graphics system with suitable diagrams.

**Solution:**

A raster graphics system is built around the concept of a **frame buffer** — a region of memory in which every pixel of the display has a corresponding storage location. The system architecture consists of these functional blocks:

**1. Central Processor Unit (CPU):**
Executes the application program. Computes the geometric model, applies transformations, and writes the resulting pixel color values into the frame buffer. In modern systems, the CPU delegates rendering work to the GPU.

**2. System Memory (RAM):**
Stores application code, scene geometry (vertex data, textures), and OS data. Connected to the CPU via the memory bus.

**3. GPU / Video Controller:**
The dedicated graphics processor that:
- Reads pixel data from the frame buffer (VRAM) sequentially.
- Generates **HSync (Horizontal Synchronization)** pulses to signal line start to the display.
- Generates **VSync (Vertical Synchronization)** pulses to signal frame start.
- Increments the raster address (column, then row) in sync with the display's beam position.

**4. Frame Buffer (VRAM):**
High-speed video RAM (GDDR6 in modern GPUs; SRAM in older CRTs) holding the digital color value for every screen pixel. Addressed as a 2D array: `pixel[row][col]`. Size = H × V × bpp / 8 bytes.

**5. Color Lookup Table (LUT) / Video DAC:**
- **LUT mode:** Each pixel stores an 8-bit palette index. The LUT maps this index to a 24-bit RGB value. Saves memory but limits simultaneous colors to 256.
- **True Color mode:** Pixels store full 24-bit RGB directly, fed to separate Red, Green, Blue DACs producing three analog voltage signals.

**6. Display Monitor (CRT/LCD/OLED):**
Receives the analog RGB signals (or digital DisplayPort/HDMI) and renders each pixel accordingly.

**Block Diagram:**
```
+------------------+      System Bus      +------------------+
|       CPU        | ◄══════════════════► |   System RAM     |
+------------------+                      +------------------+
        │
        │  PCI-e / AGP Bus
        ▼
+------------------+      VRAM Bus        +------------------+
|  GPU / Video     | ◄══════════════════► |  Frame Buffer    |
|  Controller      |                      |  (VRAM/GDDR6)    |
+------------------+                      +------------------+
        │
   ┌────┴────┐
   ▼         ▼
+--------+  +--------+
| HSync  |  | DAC    | ← converts digital pixel to analog signal
| VSync  |  | R/G/B  |   (or TMDS encoder for HDMI)
+--------+  +--------+
                │  Analog RGB / HDMI / DisplayPort
                ▼
+-------------------------------------+
|     Raster Display Monitor          |
|   (CRT, LCD, OLED, QLED)           |
+-------------------------------------+
```

**Working Principle:**
At the start of every frame, the video controller initializes its address register to $(0,0)$. It reads the color value for pixel $(0,0)$ from the frame buffer, feeds it to the DAC/LUT to produce analog drive voltage, and illuminates the first pixel. The address increments across the row (0, 1, 2 ... H-1). At end of row, a **HSync** pulse fires and the row counter increments. After all $V$ rows, a **VSync** pulse fires, returning the address to $(0,0)$ for the next frame, completing one refresh cycle at 60 Hz (or 144 Hz in gaming monitors).

---

### Question 2 [KTU January 2023, Q13c — 4 Marks]
**Question:** Explain the working of joysticks as a graphics input device.

**Solution:**

A joystick is a **locator-class** interactive input device that reports a 2D coordinate position $(x, y)$ based on the physical angle of its stick in two orthogonal axes.

**Mechanical Construction:**
- A central stick pivots on a universal joint (gimbal) allowing free movement in X and Y axes.
- Attached to each axis pivot is a **linear or rotary potentiometer** — a variable resistor with a sliding wiper.

**Electrical Working Principle:**
Each potentiometer forms a **voltage divider circuit**:
```
+5V (Vcc)
   │
  [R_total — full resistive element (10kΩ)]
   │
  Wiper (tapped position) ───► ADC Input
   │
  GND (0V)
```
The wiper position along the resistive element determines the output voltage. With the stick at center neutral:
$$V_{out} = \frac{V_{cc}}{2} = 2.5\text{ V}$$
Pushing the stick fully in one direction: $V_{out} \rightarrow 5\text{ V}$.
Pushing in the opposite direction: $V_{out} \rightarrow 0\text{ V}$.

**Digital Conversion:**
The ADC converts the continuous voltage (0–5V) into a 10-bit digital value (0–1023). Software maps this to game/graphics coordinates. A calibration routine identifies the exact center, minimum, and maximum ADC readings for each physical device, compensating for manufacturing variance.

**Deadzone Logic:**
Near the center, small mechanical vibrations or imperfect spring return cause non-zero ADC readings. A deadzone radius (e.g., ±5% of full scale = ±25 ADC units) forces readings within this band to zero, preventing cursor drift at neutral position.

**Example of ADC to Coordinate Mapping:**
If ADC reads 762 on X-axis (range 0–1023), center = 512:
$$X_{normalized} = \frac{762 - 512}{511} \approx +0.49 \quad \text{(49% rightward deflection)}$$

---

### Question 3 [KTU December 2021, Q12a — 5 Marks]
**Question:** Explain the working of (i) Digital glove (ii) Light pen.

**Solution:**

**Part (i): Digital Glove**

A digital glove (data glove) is a wearable device that captures hand and finger joint angles to provide natural gesture input in computer graphics, VR, and robotic systems.

**Working Mechanism:**
1. **Flex Sensors on Fingers:** Each finger has 1–3 flex sensors (resistive carbon-film strips) that change electrical resistance proportional to bend angle:
   - Straight finger → R ≈ 10 kΩ
   - 90° bend → R ≈ 25–35 kΩ
   - 180° bend → R ≈ 60–90 kΩ

2. **Voltage Divider Circuit:** Each flex sensor forms a voltage divider with a fixed reference resistor. The output voltage is proportional to the bend angle.

3. **ADC Conversion:** A microcontroller's ADC samples all sensor voltages simultaneously (multiplexed), producing digital bend angle values.

4. **IMU for Wrist/Hand Orientation:** An Inertial Measurement Unit (accelerometer + gyroscope) on the wrist/back-of-hand tracks the absolute orientation (roll, pitch, yaw) of the entire hand.

5. **Gesture Recognition:** Software maps ADC readings + IMU angles to recognized hand gestures (e.g., finger pinch = select object, fist = grab, open hand = release).

**Output as a Graphics Input Device:**
- **Pick device:** Pointing gesture selects an object in a 3D scene.
- **Stroke device:** Hand-writing gesture traces character strokes.
- **Valuator device:** Squeezing pressure controls object scale/volume.

**Applications:** VR surgical training, 3D modelling without controller, sign-language recognition, industrial robotic teleoperation.

---

**Part (ii): Light Pen**

A light pen is a photosensitive stylus pressed directly against a CRT screen surface to identify the exact pixel location the beam is currently illuminating.

**Detailed Working:**
1. **Photosensitive Tip:** The pen contains a **photodiode** (or phototransistor) at its tip, sensitive to visible light pulses.

2. **Raster Synchronization:** The CRT's electron beam sweeps each scanline at a precise rate (e.g., 1280 columns × 1024 rows in 16.67 ms at 60 Hz). The video controller maintains a column counter (0–H) and row counter (0–V) synchronized with the beam.

3. **Detection Event:** When the electron beam passes the exact phosphor spot where the pen tip is touching the screen, the phosphor emits a brief flash of light. This flash creates a photocurrent pulse in the photodiode.

4. **Interrupt Signal:** The photocurrent pulse is amplified by the pen's electronics and sent as an interrupt signal to the graphics controller's **pen interrupt input**.

5. **Coordinate Capture:** At the moment the interrupt fires, the graphics controller reads its current column counter (X) and row counter (Y) values. These registers directly correspond to the beam's current $(x, y)$ position — which is exactly where the pen is on the screen.

6. **Position Reporting:** The captured $(x, y)$ coordinate is reported to the application as a stroke or locator input.

**Timing Precision:** At 1280-pixel resolution and 60 Hz refresh, each pixel column represents approximately 9.6 nanoseconds. The interrupt latency and ADC sampling must resolve within this window.

**Limitations:**
- Works only with CRT screens (requires a physical electron beam — not applicable to LCDs/OLEDs).
- Cannot work in bright ambient light (sunlight creates false photodiode triggers).
- Requires the user to hold the pen against the screen, causing arm fatigue over time.

---

### Question 4 [KTU June 2022, Q2 / Sep 2020, Q2 / Dec 2019, Q11a — 4 Marks]
**Question:** Define the different categories of interactive graphic input devices with examples. OR: Describe flat panel display categories. (This answer addresses input device categories — see raster-scan file for flat panel display answer.)

**Solution:**

Interactive computer graphics defines **six logical input device classes** based on the data type returned to the application, regardless of the physical hardware:

**1. Locator Devices:**
Return a single 2D coordinate position $(x, y)$ representing a point in the display coordinate space.
- *Examples:* Optical mouse (reports ΔX, ΔY incremental), graphics tablet (reports absolute X, Y), trackball, joystick.
- *Use case:* Placing crosshairs, moving tool cursor, positioning objects in CAD.

**2. Stroke Devices:**
Return a time-ordered sequence of coordinate positions $(p_1, p_2, \ldots, p_n)$ tracing a continuous motion path.
- *Examples:* Electromagnetic stylus on a data tablet, light pen dragged across a CRT, finger swipe on touchscreen.
- *Use case:* Freehand curve drawing, signature capture, gesture input.

**3. String Devices:**
Return a sequence of ASCII or Unicode characters.
- *Examples:* Physical QWERTY keyboard, on-screen virtual keyboard, voice recognition (speech-to-text).
- *Use case:* Entering text annotations in a CAD drawing, file naming, command input.

**4. Valuator Devices:**
Return a single scalar real number along a calibrated physical range.
- *Examples:* Rotary potentiometer dial, linear slide fader, mouse scroll wheel, flight simulator throttle.
- *Use case:* Adjusting object rotation angle (0°–360°), zoom level, brush opacity (0%–100%).

**5. Choice Devices:**
Return a discrete integer selection from a fixed enumeration (menu of options).
- *Examples:* Keyboard function keys (F1–F12), dedicated hardware buttons on a graphics tablet stylus, mouse click buttons, touch-screen menu buttons.
- *Use case:* Selecting a drawing tool (pen/erase/fill), triggering a command (save/open/print).

**6. Pick Devices:**
Return the identifier (handle/ID) of an existing graphical object rendered on screen, determined by spatial hit testing.
- *Examples:* Mouse cursor + pick-ray intersection test, touch-screen bounding-box hit detection.
- *Use case:* Selecting an object in a CAD model to transform, clicking on a UI widget, selecting a 3D mesh vertex.

---

### Question 5 [KTU Dec 2020, Q11a / Sep 2020, Q12b / Dec 2019, Q13 — 4 Marks]
**Question:** Write a note on any two interactive graphics input devices.

**Solution:**

**Device 1: Graphics Tablet (Digitizing Tablet)**

A graphics tablet is a flat electronic input surface used with an electromagnetic stylus (pen) to provide precise 2D coordinate input.

**Working Principle:**
The tablet contains a grid of horizontal and vertical copper wires embedded beneath its surface. The control electronics sequentially energize each wire with AC pulses at a specific frequency. The stylus contains a passive LC (inductor-capacitor) resonant circuit tuned to this frequency. When a grid wire is active near the stylus:
1. Mutual inductance couples energy into the stylus coil (resonance).
2. When the drive pulse ends, the stylus LC circuit rings at its resonant frequency.
3. The tablet's receiver electronics detect which grid wires are most strongly coupled to the stylus echo.
4. Triangulation of the echo strength from adjacent wires gives sub-millimeter $(x, y)$ resolution.

**Key Features:** Pressure sensitivity (up to 8192 levels), tilt detection, passive stylus (no battery), accuracy to ±0.01 mm. Classified as a **locator** (absolute position) and **stroke** (continuous path) device.

**Applications:** Digital illustration (Wacom Cintiq), architectural drafting, medical image annotation, photo retouching.

---

**Device 2: Optical Mouse**

An optical mouse is a hand-held locator device that reports relative XY movement using optical cross-correlation of surface texture.

**Working Principle:**
1. A red/infrared LED illuminates the desk surface at a low angle, creating shadow texture from surface irregularities.
2. A CMOS image sensor captures frames at 3,000–8,000 FPS.
3. A DSP chip performs **cross-correlation** between consecutive image frames to compute ΔX and ΔY displacement.
4. These displacement deltas are accumulated and sent to the OS as HID (Human Interface Device) reports at typically 125–1000 Hz (polling rate).

**Key Properties:**
- Reports **relative displacement** only — not absolute position. Hence picking up and moving the mouse does NOT change cursor position.
- DPI (Dots Per Inch) setting controls the sensitivity scaling factor between physical motion and cursor movement.

**Applications:** General desktop navigation, gaming (high DPI for fast aiming), CAD navigation.

---

### Question 6 [KTU June 2024, Q12a / Dec 2023, Q13a / June 2022, Q13b / Dec 2018, Q1 — 4 Marks]
**Question:** Define the terms: (i) Aspect Ratio (ii) Resolution.

**Solution:**

**Resolution:**
Resolution is the total number of distinct visual picture elements (pixels) that a display screen can render across its horizontal ($H$) and vertical ($V$) dimensions, stated as $H \times V$.

- Example: $1920 \times 1080$ means 1920 pixel columns × 1080 pixel rows = 2,073,600 total pixels (≈ 2.07 megapixels).
- **Physical significance:** A higher resolution allows finer geometric details to be rendered with reduced aliasing (jagged staircase artifacts on diagonal lines). The maximum achievable resolution of a CRT is limited by the electron beam spot size (focus quality) and the phosphor dot pitch. For LCD/OLED panels, it is limited by the manufacturing precision of pixel electrode arrays.
- **Pixel density (PPI):** $\text{PPI} = \frac{\sqrt{H^2 + V^2}}{\text{screen diagonal (inches)}}$.

**Aspect Ratio:**
The aspect ratio is the ratio of the physical width of the display image to its physical height, expressed in lowest integer proportions.

$$\text{Aspect Ratio} = \frac{W}{H} = \frac{W/\gcd(W,H)}{H/\gcd(W,H)}$$

- Example: $1920 \times 1080$: $\gcd(1920, 1080) = 120$, so AR = $16:9$.
- **Significance in graphics:** To maintain geometric fidelity (ensuring a circle appears circular rather than as an ellipse), coordinate transformations must account for the aspect ratio. If $\Delta x_{pixel} \neq \Delta y_{pixel}$ (non-square pixels), the viewport transformation must apply correction:
  $$s_y = s_x \times \frac{\Delta x_{pixel}}{\Delta y_{pixel}}$$
- **Common standards:**
  - $4:3$ — Traditional CRT monitors, NTSC television
  - $16:9$ — Modern widescreen HD/UHD monitors
  - $16:10$ — Professional graphics and photography monitors
  - $4:5$ — 8×10 inch portrait (screen width 8", height 10")
