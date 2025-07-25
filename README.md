# MFSU Simulations: Test the Unified Fractal-Stochastic Model at Home!

Welcome to this super repository with Python codes to simulate the MFSU, my model that resolves the Hubble tension using fractals and stochastics. Based on 2025 data from DESI, CMB-S4, and JWST.

This is designed for anyone to try at home—replicate the simulations, estimate fractal dimensions, and see how MFSU unifies early and late universe measurements!

## Requirements
- Python 3 (install from python.org if needed).
- Libraries: Run `pip install numpy scipy` in your terminal (these are the basics; no internet needed beyond that).

## How to Use
1. Download the repo: Click "Code" > "Download ZIP".
2. Unzip and navigate to the `/codes/` folder.
3. Open a script in your editor (like VS Code, Jupyter Notebook, or even IDLE).
4. Run it from the terminal, e.g., `python codes/simulacion_simple.py`.
5. Experiment! Modify parameters like δ_F or add real data from Planck/JWST.

## Included Codes
- **simulacion_simple.py**: Computes the fractal factor and resolves H0 based on MFSU principles.
- **analisis_wavelets.py**: Performs wavelet analysis to estimate fractal dimension in simulated CMB data (includes a log-log plot).
- More to come: Bootstrap resampling, MCMC, sensitivity analysis, etc. (feel free to contribute or add your own variations).

All codes are reproducible and based on the manuscript. Results should match the empirical validation, e.g., δ_F ≈ 0.92 and resolved H0 ≈ 73 km/s/Mpc.

## Link to Manuscript
For full details and theory: [Empirical Validation of MFSU on Zenodo](https://zenodo.org/records/16353348) (285+ downloads already!).

## Contribute or Contact
- Replicate and share your results! If you find improvements or applications (e.g., in AI or materials), open a pull request.
- Questions? Contact me on X: @yourusername (replace with your handle).
- Inspired by fractal pioneers like Mandelbrot—let's build the future of cosmology together!

License: MIT (free to use, modify, and share with credit).
