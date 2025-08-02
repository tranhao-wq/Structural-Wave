import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu thời gian
t = np.linspace(0, 120, 1000)  # khoảng 120 năm, tương ứng với 2 chu kỳ Kondratieff

# Sóng Kondratieff (K): chu kỳ dài, tần số thấp
K_wave = 1.5 * np.cos(2 * np.pi * t / 60)  # chu kỳ 60 năm

# Sóng Juglar (J): chu kỳ trung bình, điều biến theo K
J_wave = (1 + 0.5 * np.cos(2 * np.pi * t / 60)) * np.cos(2 * np.pi * t / 10)

# Sóng Kitchin: dao động ngắn, nằm trong J
Kitchin_wave = 0.5 * np.cos(2 * np.pi * t / 3.5)

# Tổng hợp biểu đồ
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(t, K_wave, label='Sóng K (Kondratieff)', color='blue', linewidth=2)
ax.plot(t, J_wave, label='Chu kỳ J (Juglar) – điều biến theo sóng K', color='orange', alpha=0.8)
ax.plot(t, Kitchin_wave, label='Chu kỳ Kitchin (ngắn hạn)', color='green', alpha=0.6, linestyle='--')

# Giao diện
ax.set_title("Biểu đồ Nested: Sóng K – J – Kitchin", fontsize=14)
ax.set_xlabel("Thời gian (năm giả định)")
ax.set_ylabel("Cường độ chu kỳ (ẩn dụ cho hoạt động kinh tế)")
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()

plt.tight_layout()
plt.show()
