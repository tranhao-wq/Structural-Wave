import matplotlib.pyplot as plt
import numpy as np

# Generate years and simulated Kondratieff wave
years = np.arange(1780, 2030)
kondratieff = []
for year in years:
    cycle = (year - 1780) / 55  # average 55 years per full wave
    value = np.sin(2 * np.pi * cycle)
    kondratieff.append(value)

# Plotting
plt.figure()
plt.plot(years, kondratieff, label='Sóng Kondratieff mô phỏng')
plt.axhline(0, linestyle='--')
plt.title('Mô phỏng Sóng Kondratieff (1780–2030)')
plt.xlabel('Năm')
plt.ylabel('Pha tăng/trầm')
plt.grid(True)
plt.legend()
plt.show()
