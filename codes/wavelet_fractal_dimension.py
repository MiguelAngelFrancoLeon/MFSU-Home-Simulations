import numpy as np
from scipy.signal import cwt, ricker
import matplotlib.pyplot as plt

# Simulated CMB data
data_cmb = np.random.randn(1000)  # Placeholder; replace with real data

# Wavelet widths
widths = np.arange(1, 31)

# CWT with Ricker wavelet
cwtmatr = cwt(data_cmb, ricker, widths)

# Average power
power = np.mean(np.abs(cwtmatr)**2, axis=1)

# Log-log fit for slope
log_scale = np.log(widths[5:15])  # Scaling region
log_power = np.log(power[5:15])
slope = np.polyfit(log_scale, log_power, 1)[0]
D_f = 3 + slope / 2  # Approximate fractal dimension

plt.plot(np.log(widths), np.log(power))
plt.xlabel('Log Scale')
plt.ylabel('Log Power')
plt.title('Wavelet Power Spectrum')
plt.show()
print(f"Slope: {slope:.2f}, Fractal Dimension: {D_f:.3f}")
