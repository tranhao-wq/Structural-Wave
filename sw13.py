import matplotlib.pyplot as plt
import numpy as np

# Generate years
years = np.arange(1780, 2030)

# Simulate Kondratieff wave (approx. 55-year period)
main_wave = np.sin(2 * np.pi * (years - 1780) / 55)

# Simulate Juglar cycle (approx. 9-year period)
juglar_wave = 0.3 * np.sin(2 * np.pi * (years - 1780) / 9)

# Plotting
plt.figure()
plt.plot(years, main_wave, label='Sóng Kondratieff (mô phỏng)')
plt.plot(years, juglar_wave, label='Chu kỳ Juglar (mô phỏng)')
plt.axhline(0, linestyle='--')
plt.title('Mô phỏng Sóng K với lớp Chu kỳ J chồng lên (1780–2030)')
plt.xlabel('Năm')
plt.ylabel('Biên độ tương đối')
plt.grid(True)
plt.legend()
plt.show()
