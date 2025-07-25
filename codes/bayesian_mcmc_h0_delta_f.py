import numpy as np

# Observations
H0_CMB_obs, sigma_CMB = 66.8, 0.5
H0_local_obs, sigma_local = 75.0, 1.0

# Log prior (uniform)
def log_prior(H0_true, delta_F):
    if 60 < H0_true < 80 and 0 < delta_F < 0.2:
        return 0.0
    return -np.inf

# Log likelihood
def log_likelihood(H0_true, delta_F):
    mu_CMB = H0_true / (1 + delta_F)
    term1 = -0.5 * ((H0_CMB_obs - mu_CMB) / sigma_CMB)**2
    term2 = -0.5 * ((H0_local_obs - H0_true) / sigma_local)**2
    return term1 + term2

# Log posterior
def log_posterior(theta):
    H0_true, delta_F = theta
    lp = log_prior(H0_true, delta_F)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(H0_true, delta_F)

# MCMC setup
n_steps = 10000
burn_in = 2000
theta = [70.0, 0.1]
samples = []
for _ in range(n_steps):
    new_theta = theta + np.random.normal(0, [1.0, 0.01])
    log_ratio = log_posterior(new_theta) - log_posterior(theta)
    if log_ratio > np.log(np.random.uniform()):
        theta = new_theta
    samples.append(theta)

samples = np.array(samples)[burn_in:]
print(f"Mean H0_true: {np.mean(samples[:, 0]):.2f}")
print(f"Mean δ_F: {np.mean(samples[:, 1]):.3f}")
