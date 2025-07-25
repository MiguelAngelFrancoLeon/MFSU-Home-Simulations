import numpy as np
import matplotlib.pyplot as plt

# Parameters for void simulation
void_size = 100  # Mpc scale
fractal_dim = 2.415  # From wavelet analysis
grid_size = 1000  # Simulation grid

# Generate fractal void distribution (simple noise-based)
x = np.linspace(-void_size, void_size, grid_size)
y = np.linspace(-void_size, void_size, grid_size)
X, Y = np.meshgrid(x, y)
r = np.sqrt(X**2 + Y**2)
void_density = (r / void_size)**(fractal_dim - 2)  # Power-law for fractal voids

# Adjust H0 for void effects
H0_base = 73.0
delta_void = np.mean(void_density) * 0.05  # Fractal correction from voids
H0_adjusted = H0_base * (1 + delta_void)

# Plot void map
plt.imshow(void_density, extent=[-void_size, void_size, -void_size, void_size], cmap='plasma')
plt.title('Fractal Void Simulation')
plt.xlabel('Mpc')
plt.ylabel('Mpc')
plt.colorbar(label='Density')
plt.show()

print(f"Adjusted H0 due to voids: {H0_adjusted:.2f} km/s/Mpc")
