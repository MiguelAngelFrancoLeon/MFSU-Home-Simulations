import numpy as np

# String parameters (simplified vibrational modes)
string_modes = 10  # Number of modes (hilos)
delta_F = 0.08     # Fractal factor
H0_CMB = 67.24     # Base H0

# Stochastic noise for strings (fractal-like)
noise = np.random.normal(0, 0.01, string_modes)  # Gaussian stochastic
string_vib = np.cumsum(noise)  # Cumulative "hilos infinitos"

# Integrate with MFSU: Adjust H0 by string-stochastic factor
factor_string = np.mean(np.abs(string_vib)) * delta_F
H0_unified = H0_CMB * (1 + factor_string)

print(f"String modes factor: {factor_string:.3f}")
print(f"Unified H0 with strings: {H0_unified:.2f} km/s/Mpc")
