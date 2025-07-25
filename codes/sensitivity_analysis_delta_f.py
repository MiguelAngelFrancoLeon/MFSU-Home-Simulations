import numpy as np
import matplotlib.pyplot as plt

# Base parameters
H0_CMB = 67.24
delta_F_values = np.linspace(0.01, 0.2, 100)  # Range to test

# Compute resolved H0 for each δ_F
H0_resolved = H0_CMB * (1 + delta_F_values)

# Plot
plt.plot(delta_F_values, H0_resolved)
plt.xlabel('δ_F')
plt.ylabel('Resolved H0 (km/s/Mpc)')
plt.title('Sensitivity of H0 to Fractal Factor')
plt.show()
print(f"Example at δ_F=0.08: H0={H0_CMB * (1 + 0.08):.2f}")
