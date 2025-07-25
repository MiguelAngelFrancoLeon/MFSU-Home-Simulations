import numpy as np
from scipy.integrate import quad

# Hubble function (simplified ΛCDM + neutrinos + fractal)
def H_z(z, Omega_m, H0, sum_m_nu, delta_F):
    Omega_L = 1 - Omega_m
    Omega_nu = sum_m_nu / (93.14 * H0**2)
    return H0 * np.sqrt(Omega_m * (1 + z)**3 + Omega_L + Omega_nu * (1 + z)**4 + delta_F)

# Integrated distance (simplified)
def D_M(z, params):
    return quad(lambda zp: 1 / H_z(zp, *params), 0, z)[0]

# Test with parameters
params = (0.3, 67.5, 0.06, 0.08)  # Omega_m, H0, sum_m_nu, delta_F
print(f"Comoving distance at z=1: {D_M(1, params):.2f} Mpc")
