# Riemann Hypothesis Proof Visualization (Step 4) using SSTAFF in Blender

This repository contains a Blender script to visualize Step 4 ("Spectral Symmetry") of a proof attempt for the Riemann Hypothesis using the Supersymmetric Theory of Anomalous Phenomena (SSTAFF).

## Overview

The script `step4_blender.py` creates a 3D visualization of the integrals \(\psi(\rho, t)\) and \(\psi(1-\rho, t)\) for different values of \(\epsilon\). The goal is to confirm the Riemann Hypothesis by showing that these integrals intersect at \(\sigma = \frac{1}{2}\), which corresponds to the critical line where all non-trivial zeros of the zeta function \(\zeta(s)\) are expected to lie.

- **Red curves**: \(\psi(\rho, t)\)
- **Blue curves**: \(\psi(1-\rho, t)\)
- **Purple lines**: Critical line (\(\sigma = \frac{1}{2}\), scaled to \(x = 0\))
- **Z-axis**: Separates curves for different \(\epsilon\) values

## Prerequisites

1. **Blender**:
   - Download and install Blender (version 3.6 or later recommended) from [blender.org](https://www.blender.org/download/).
   
2. **Python Dependencies**:
   - Blender uses its own Python environment. You need to install the required libraries in Blender's Python:
     - Find Blender's Python executable:
       - Windows: `C:\Program Files\Blender Foundation\Blender 3.6\3.6\python\bin\python.exe`
       - macOS: `/Applications/Blender.app/Contents/Resources/3.6/python/bin/python3.10`
       - Linux: (e.g., `/usr/local/blender/3.6/python/bin/python3.10`)
     - Open a terminal (or Command Prompt on Windows) and run:
       ```
       /path/to/blender/python/bin/python3.10 -m pip install numpy mpmath scipy
       ```
       Example for Windows:
       ```
       "C:\Program Files\Blender Foundation\Blender 3.6\3.6\python\bin\python.exe" -m pip install numpy mpmath scipy
       ```

## Installation

1. **Clone or Download the Repository**:
   - Clone this repository using Git:
     ```
     git clone https://github.com/your-username/RiemannProofBlender.git
     ```
   - Alternatively, download the ZIP file from GitHub and extract it.

2. **Files**:
   - `step4_blender.py`: The main script to run in Blender.
   - `requirements.txt`: List of Python dependencies.
   - `README.md`: This file with instructions.

## Usage

1. **Open Blender**:
   - Launch Blender and switch to the **Scripting** tab (at the top).

2. **Load the Script**:
   - In the text editor (Scripting workspace), click **Open**.
   - Navigate to the folder where you downloaded/cloned the repository and select `step4_blender.py`.

3. **Run the Script**:
   - Click the **Run Script** button (triangle icon in the text editor).
   - The script will:
     - Compute the integrals \(\psi(\rho, t)\) and \(\psi(1-\rho, t)\).
     - Create a 3D visualization in Blender.
     - Render the scene and save it as `render_step4.png` in the same folder as your Blender project.

4. **Check the Console Output**:
   - If the Blender console is not visible, drag the bottom of the text editor down to reveal it.
   - Look for messages like:
     ```
     Вычисление для ε = 1e-05
     Значение интеграла для psi(rho, t) при sigma = 0.5: (value)
     Значение интеграла для psi(1-rho, t) при sigma = 0.5: (value)
     Разница между интегралами: (difference)
     ```
   - If the difference between the integrals at \(\sigma = \frac{1}{2}\) is small (e.g., less than \(10^{-5}\)), this supports the Riemann Hypothesis.

5. **View the 3D Graph**:
   - Switch to the **Layout** or **3D Viewport** tab in Blender to see the 3D graph.
   - Red curves represent \(\psi(\rho, t)\), blue curves represent \(\psi(1-\rho, t)\), and purple lines mark the critical line (\(\sigma = \frac{1}{2}\), scaled to \(x = 0\)).
   - Curves are separated along the Z-axis for each \(\epsilon\).

6. **View the Rendered Image**:
   - The script automatically renders the scene and saves it as `render_step4.png` in the same folder as your Blender project.
   - Open `render_step4.png` to see a 2D render of the 3D graph.

## Interpretation

- **Expected Result**:
  - The red and blue curves should intersect at \(x = 0\) (corresponding to \(\sigma = \frac{1}{2}\)) for each \(\epsilon\).
  - This intersection confirms spectral symmetry, supporting the Riemann Hypothesis: non-trivial zeros of \(\zeta(s)\) lie on the critical line (\(\text{Re}(s) = \frac{1}{2}\)).

- **If the Curves Do Not Intersect at \(x = 0\)**:
  - This may indicate numerical errors. To improve accuracy:
    - Increase \(N\) in the script (e.g., from 40 to 100):
      ```python
      N = 100
      t = np.linspace(-T, T, N)
      ```
    - Increase the number of points for \(\sigma\):
      ```python
      sigma_vals = np.linspace(0, 1, 100)
      ```
    - Test with different \(\gamma\) values (e.g., add a loop for multiple non-trivial zeros):
      ```python
      gamma_values = [14.1347, 21.0220, 25.0108]
      ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have questions or need help, feel free to open an issue in this repository.
