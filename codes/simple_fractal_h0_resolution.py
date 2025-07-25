import numpy as np

# Parameters from 2025 data
delta_F = 0.2511  # Universal fractal constant
H0_CMB = 67.24    # Early universe (e.g., CMB)
H0_local = 73.0   # Late universe (e.g., SHOES)

# Compute fractal factor
factor_fractal = np.log(H0_local / H0_CMB)

# Resolve H0 with MFSU
H0_resolved = H0_CMB * (1 + delta_F + factor_fractal)

print(f"Fractal factor: {factor_fractal:.3f}")
print(f"Resolved H0: {H0_resolved:.2f} km/s/Mpc")
