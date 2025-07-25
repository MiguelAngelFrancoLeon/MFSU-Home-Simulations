import numpy as np

# Simulated observations
H0_CMB_obs = np.random.normal(66.8, 0.5, 1000)  # Early universe samples
H0_local_obs = np.random.normal(75.0, 1.0, 1000) # Late universe samples

# Bootstrap: Resample 1000 times
n_boot = 1000
delta_F_boot = []
for _ in range(n_boot):
    cmb_sample = np.random.choice(H0_CMB_obs, len(H0_CMB_obs), replace=True)
    local_sample = np.random.choice(H0_local_obs, len(H0_local_obs), replace=True)
    delta_F = np.mean((local_sample - np.mean(cmb_sample)) / np.mean(cmb_sample))
    delta_F_boot.append(delta_F)

# Results
mean_delta_F = np.mean(delta_F_boot)
std_delta_F = np.std(delta_F_boot)
print(f"Mean δ_F: {mean_delta_F:.3f} ± {std_delta_F:.3f}")
