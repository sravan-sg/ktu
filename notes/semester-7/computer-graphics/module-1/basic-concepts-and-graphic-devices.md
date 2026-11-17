# Basic Concepts in Computer Graphics & Graphic Devices

## 1. Explanation
Computer graphics is the art and science of synthesizing, manipulating, and displaying visual content using computational processors and dedicated display hardware. At its mathematical core, computer graphics establishes a bridge between abstract numerical models (points, lines, algebraic curves, 3D meshes) and physical display rasters composed of discrete light-emitting elements (pixels).

### The Graphics Pipeline Overview
The generation of imagery on a digital screen follows an algorithmic progression:
$$\text{Application Model} \xrightarrow{\text{Geometric Modeling}} \text{World Coordinates} \xrightarrow{\text{Viewing \& Clipping}} \text{Normalized Coordinates} \xrightarrow{\text{Rasterization}} \text{Frame Buffer} \xrightarrow{\text{Video Display}} \text{Physical Pixels}$$

1. **Modeling Coordinates (MC)**: Geometry is defined in a local coordinate frame specific to the object.
2. **World Coordinates (WC)**: Multiple objects are transformed and assembled into a shared virtual environment.
3. **Viewing Coordinates (VC)**: The world is transformed relative to the observer's virtual camera.
4. **Normalized Device Coordinates (NDC)**: The viewing frustum is mapped into a normalized unit cube ($[-1, 1]^3$ or $[0, 1]^3$) independent of display hardware.
5. **Device Coordinates (DC)**: The final viewport maps normalized coordinates directly to physical screen pixels $(x_{\min}, y_{\min})$ to $(x_{\max}, y_{\max})$.

### Taxonomy of Graphic Devices
Graphic devices are partitioned into **Input Devices** (capturing human spatial intent) and **Display/Output Devices** (rendering spatial signals).

#### Interactive Graphic Input Devices
Interactive computer graphics categorizes input hardware not merely by physical packaging, but by the **logical input primitive** it delivers to the operating system:

1. **Locator Devices**:
   - *Function:* Provide a continuous 2D or 3D coordinate position $(x, y)$ or $(x, y, z)$.
   - *Hardware Examples:* Computer mouse (optical quadrature encoder), graphics tablet/digitizer (electromagnetic induction grid), trackball, joystick (potentiometer voltage divider).
2. **Stroke Devices**:
   - *Function:* Generate a time-ordered sequence of coordinate positions $(\vec{p}_1, \vec{p}_2, \dots, \vec{p}_n)$ tracing continuous path motion.
   - *Hardware Examples:* Digital stylus on an active digitizer tablet (Wacom EMR), light pen drawing curves directly on a phosphor screen.
3. **String Devices**:
   - *Function:* Return arbitrary alphanumeric text sequences.
   - *Hardware Examples:* Physical QWERTY keyboard, virtual software keypad.
4. **Valuator Devices**:
   - *Function:* Deliver a scalar real number (floating-point value) along a calibrated physical continuum.
   - *Hardware Examples:* Rotary potentiometer dials, linear slide faders, volume knobs.
5. **Choice Devices**:
   - *Function:* Select a single action or discrete option from a predefined enumeration set.
   - *Hardware Examples:* Function keys ($F_1 - F_{12}$), touch-screen menu buttons, mouse pushbuttons.
6. **Pick Devices**:
   - *Function:* Select an existing graphical object or primitive component rendered on screen.
   - *Hardware Examples:* Mouse cursor pick-ray intersection test, touch-screen tap with spatial bounding-box hit detection.

---

## 2. Example: Logical Input Device Mapping Architecture
```
+-------------------------------------------------------------------------+
|                         APPLICATION PROGRAM                             |
+-------------------------------------------------------------------------+
        ▲                     ▲                      ▲               ▲
        | (x, y)              | (x_i, y_i) seq       | Scalar value  | Object ID
        ▼                     ▼                      ▼               ▼
+---------------+     +---------------+     +---------------+ +---------------+
| LOCATOR CLASS |     |  STROKE CLASS |     | VALUATOR CLASS| |  PICK CLASS   |
+---------------+     +---------------+     +---------------+ +---------------+
        ▲                     ▲                      ▲               ▲
        | Coordinates         | Packet stream        | Resistance    | Ray hit
+---------------+     +---------------+     +---------------+ +---------------+
| Optical Mouse |     | Digitizer Pen |     | Rotary Dial   | | Ray-Caster    |
+---------------+     +---------------+     +---------------+ +---------------+
```

---

## 3. Applications & Use Cases
1. **Computer-Aided Design (CAD / CAM)**: High-precision digitizing tablets (locator and stroke devices) allow structural engineers to trace physical engineering blueprints directly into vector CAD representations (AutoCAD, CATIA).
2. **Digital Audio Workstations (DAW) & Mixing Consoles**: Hardware mixing boards utilize arrays of motorized slide faders and rotary encoders (valuator devices) to control track gain, equalization parameters, and panning in real time.
3. **Medical Imaging Workstations (PACS)**: Radiologists utilize 3D space-mice (multi-axis locators) to slice, rotate, and pick anatomical landmarks within volumetric MRI and CT scan reconstructions.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Aspect Ratio and Resolution Calculations [Sample Question Paper Pattern]
**Problem**:
A high-definition medical diagnostic monitor has a display resolution of $2560 \times 1440$ pixels.
1. Determine the monitor's aspect ratio in lowest integer terms.
2. If the monitor's physical diagonal screen dimension is 27 inches, compute the pixel density in Pixels Per Inch (PPI) and the physical size (width and height) of an individual pixel assuming square pixels.

**Step-by-step Solution**:
1. **Aspect Ratio Calculation**:
   $$\text{Horizontal resolution } W = 2560, \quad \text{Vertical resolution } H = 1440$$
   $$\text{GCD}(2560, 1440) = 160$$
   $$\text{Aspect Ratio} = \frac{2560 / 160}{1440 / 160} = \frac{16}{9} \implies 16:9$$
2. **Pixel Density (PPI)**:
   $$\text{Diagonal pixel count } D_p = \sqrt{W^2 + H^2} = \sqrt{2560^2 + 1440^2} = \sqrt{6553600 + 2073600} = \sqrt{8627200} \approx 2937.21 \text{ pixels}$$
   $$\text{PPI} = \frac{D_p}{\text{Diagonal in inches}} = \frac{2937.21}{27} \approx 108.79 \text{ PPI}$$
3. **Pixel Dimensions**:
   $$\text{Dot Pitch (pixel size)} = \frac{1}{\text{PPI}} = \frac{1}{108.79} \approx 0.00919 \text{ inches} \approx 0.00919 \times 25.4 \text{ mm} \approx 0.233 \text{ mm}$$
   Each individual pixel has a physical width and height of $0.233 \text{ mm} \times 0.233 \text{ mm}$.

---

### Example 2: Frame Buffer Memory and Dwell Time Analysis [KTU June 2024 / Dec 2020 Pattern]
**Problem**:
A graphics workstation operates at a screen resolution of $1280 \times 1024$ at a non-interlaced refresh rate of 60 Hz.
1. Compute the uncompressed frame buffer size in megabytes (MB) required to support 24-bit True Color (8 bits each for Red, Green, Blue).
2. If the horizontal retrace time accounts for $18\%$ of each scanline and vertical retrace accounts for $8\%$ of each frame refresh cycle, determine the effective time available to display each pixel (pixel dwell time).

**Step-by-step Solution**:
1. **Frame Buffer Size**:
   $$\text{Total pixels} = 1280 \times 1024 = 1,310,720 \text{ pixels}$$
   $$\text{Bits per pixel (bpp)} = 24 \text{ bits} = 3 \text{ bytes}$$
   $$\text{Frame Buffer Size (bytes)} = 1,310,720 \times 3 = 3,932,160 \text{ bytes}$$
   $$\text{Frame Buffer Size (MB)} = \frac{3,932,160}{1024 \times 1024} = 3.75 \text{ MB}$$
2. **Pixel Dwell Time**:
   - Total time for one complete frame refresh cycle:
     $$T_{\text{frame}} = \frac{1}{60 \text{ Hz}} \approx 16.667 \text{ ms} = 16,666.67 \ \mu\text{s}$$
   - Accounting for $8\%$ vertical retrace time, the active vertical display time is:
     $$T_{\text{active\_frame}} = 16,666.67 \times (1 - 0.08) = 15,333.34 \ \mu\text{s}$$
   - Time allocated per scanline across 1024 lines:
     $$T_{\text{scanline}} = \frac{15,333.34 \ \mu\text{s}}{1024} \approx 14.974 \ \mu\text{s}$$
   - Accounting for $18\%$ horizontal retrace time, active scanline trace time is:
     $$T_{\text{active\_line}} = 14.974 \times (1 - 0.18) = 12.279 \ \mu\text{s}$$
   - Pixel dwell time (time the electron beam illuminates one pixel across 1280 pixels):
     $$T_{\text{pixel}} = \frac{12.279 \ \mu\text{s}}{1280} \approx 9.59 \text{ nanoseconds}$$

---

### Example 3: Color Lookup Table (LUT) Bit Savings Analysis [KTU May 2019 / Dec 2021 Pattern]
**Problem**:
A legacy graphics display system utilizes a Color Lookup Table (LUT) architecture with an 8-bit frame buffer indexing into a 24-bit True Color digital-to-analog converter (DAC).
1. How many distinct colors can be displayed on screen simultaneously?
2. What is the total size of the color palette from which these colors can be chosen?
3. Compare the memory required for a $1024 \times 768$ screen using this LUT architecture versus a direct True Color frame buffer.

**Step-by-step Solution**:
1. **Simultaneously Displayable Colors**:
   - Each pixel in the frame buffer stores an 8-bit index.
   - With 8 bits, the maximum number of distinct indices is $2^8 = 256$ colors.
2. **Total Color Palette**:
   - Each entry in the LUT has 24 bits (8 bits Red, 8 bits Green, 8 bits Blue).
   - Total possible colors in the palette $= 2^{24} = 16,777,216$ colors (16.7 million colors).
   - Thus, any 256 colors can be selected from a total palette of 16.7 million colors.
3. **Memory Comparison**:
   - **LUT Architecture**:
     $$\text{Frame Buffer} = 1024 \times 768 \times 1 \text{ byte} = 786,432 \text{ bytes} = 768 \text{ KB}$$
     $$\text{LUT Table} = 256 \text{ entries} \times 3 \text{ bytes} = 768 \text{ bytes}$$
     $$\text{Total Memory} = 768 \text{ KB} + 0.75 \text{ KB} \approx 768.75 \text{ KB}$$
   - **Direct 24-bit True Color**:
     $$\text{Total Memory} = 1024 \times 768 \times 3 \text{ bytes} = 2,359,296 \text{ bytes} = 2304 \text{ KB} = 2.25 \text{ MB}$$
   - **Memory Reduction**: The LUT achieves a memory reduction factor of $\frac{2304}{768.75} \approx 3\times$ savings, which was crucial for early graphics hardware.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU January 2023 / June 2022 - 4 Marks]
**Question**:
Define the different logical classes of interactive graphic input devices with suitable examples.

**Solution**:
In interactive computer graphics, physical input hardware is abstracted into six distinct logical input device classes based on the data type returned to the application:
1. **Locator Devices**: Return a single coordinate position $(x, y)$ in world or screen space. Used for positioning markers, crosshairs, and selecting points.
   - *Examples:* Optical mouse, graphic digitizer tablet, trackball, joystick.
2. **Stroke Devices**: Return a time-ordered sequence of coordinate positions $(\vec{p}_1, \vec{p}_2, \dots, \vec{p}_n)$ capturing continuous motion paths. Used for freehand sketch drafting and signature capture.
   - *Examples:* Electromagnetic stylus pen on active digitizers, light pen.
3. **String Devices**: Return an arbitrary sequence of ASCII/Unicode character strings. Used for text annotations and command typing.
   - *Examples:* Physical QWERTY keyboard, on-screen virtual keyboard.
4. **Valuator Devices**: Return a single scalar floating-point value. Used for adjusting physical quantities such as rotation angles, scale factors, and audio volume.
   - *Examples:* Rotary potentiometer knobs, physical slide faders, mouse scroll-wheel.
5. **Choice Devices**: Return a discrete integer selection from an enumerated menu or command set.
   - *Examples:* Keyboard function keys ($F_1 - F_{12}$), dedicated hardware macro buttons, mouse click switches.
6. **Pick Devices**: Return the identifier (ID) or memory handle of an existing graphical primitive rendered on display. Used for selecting rendered geometric objects in CAD or game scenes.
   - *Examples:* Mouse cursor pick-ray intersection test, touch screen hit-testing.

---

### Question 2 [KTU December 2018 / December 2021 - 4 Marks]
**Question**:
What do you understand by the aspect ratio and resolution of a display screen in a raster scan display?

**Solution**:
1. **Resolution**:
   - *Definition:* Resolution is the total number of distinct visual picture elements (pixels) that a display screen can render across its horizontal and vertical dimensions without overlap.
   - *Mathematical Representation:* Stated as $N_{\text{horizontal}} \times N_{\text{vertical}}$ (e.g., $1920 \times 1080$, $1024 \times 768$).
   - *Physical Implication:* The maximum resolution of a CRT or flat panel monitor depends on the focus of the electron beam, the physical dot pitch (spacing between adjacent phosphor triads), and the deflection circuitry bandwidth. Higher resolution enables the display of finer geometric details with reduced aliasing (staircasing).
2. **Aspect Ratio**:
   - *Definition:* The aspect ratio is the ratio of the physical width of the display image to its physical height, expressed in simplest integer proportions.
   - *Mathematical Formulation:*
     $$\text{Aspect Ratio} = \frac{\text{Width}}{\text{Height}} = \frac{W}{H}$$
   - *Significance in Graphics:* To maintain geometric fidelity (e.g., ensuring a circle of radius $r$ appears circular rather than distorted into an ellipse), the aspect ratio must be factored into coordinate transformations. If a display has non-square pixels, scaling factors $s_x$ and $s_y$ must be adjusted proportionally:
     $$\Delta x_{\text{pixel}} \ne \Delta y_{\text{pixel}} \implies s_y = s_x \times \left(\frac{\Delta x_{\text{pixel}}}{\Delta y_{\text{pixel}}}\right)$$
   - *Common Standards:* $4:3$ (traditional CRT displays), $16:9$ (modern widescreen monitors), $16:10$ (professional graphics monitors).

