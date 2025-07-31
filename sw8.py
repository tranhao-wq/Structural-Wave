import matplotlib.pyplot as plt
import numpy as np

# Tạo trục thời gian
years = np.linspace(0, 60, 1000)

# Sóng Kondratieff (dài hạn): chu kỳ 60 năm
k_wave = np.sin(2 * np.pi * years / 60)

# Chu kỳ Juglar (trung hạn): chu kỳ 10 năm
j_cycle = 0.4 * np.sin(2 * np.pi * years / 10)

# Tổng hợp: Sóng K chứa các chu kỳ J bên trong
combined = k_wave + j_cycle

# Vẽ biểu đồ
plt.figure(figsize=(14, 6))
plt.plot(years, combined, label='Tổng hợp (K + J)', color='black', linewidth=2)
plt.plot(years, k_wave, label='Sóng Kondratieff (60 năm)', linestyle='--', color='blue')
plt.plot(years, j_cycle, label='Chu kỳ Juglar (10 năm)', linestyle=':', color='red')

# Chú thích
plt.title('Biểu đồ tượng trưng: Sóng Kondratieff và Chu kỳ Juglar')
plt.xlabel('Năm (Tượng trưng)')
plt.ylabel('Mức độ hoạt động kinh tế')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
