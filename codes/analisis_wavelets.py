import numpy as np

# Parámetros basados en datos 2025 y MFSU
delta_F = 0.2511  # Constante fractal universal
H0_CMB = 67.24    # Valor del universo temprano (e.g., SPT-3G + ACT)
H0_local = 73.0   # Valor del universo tardío (e.g., SHOES)

# Calcula factor fractal (basado en invariancia de escala)
factor_fractal = np.log(H0_local / H0_CMB)

# Resuelve H0 con MFSU
H0_resolved = H0_CMB * (1 + delta_F + factor_fractal)

# Imprime resultados
print(f"Fractal factor calculated: {factor_fractal:.3f}")
print(f"H0 resolved with MFSU: {H0_resolved:.2f} km/s/Mpc")
