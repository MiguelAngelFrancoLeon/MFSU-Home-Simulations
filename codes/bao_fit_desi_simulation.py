import numpy as np
from scipy.optimize import minimize

# Simulated BAO data (e.g., D_M / r_d at z=0.38)
bao_data = {'z': 0.38, 'D_M_rd': 7.475, 'sigma': 0.15}

# χ² for MFSU (simple model)
def chi2(theta):
    H0, delta_F = theta
    pred = H0 / (1 + delta_F) / bao_data['z']  # Simplified prediction
    return ((pred - bao_data['D_M_rd']) / bao_data['sigma'])**2

# Minimize
result = minimize(chi2, [70.0, 0.1])
print(f"Best-fit H0: {result.x[0]:.2f}, δ_F: {result.x[1]:.3f}")
print(f"χ²: {result.fun:.2f}")
