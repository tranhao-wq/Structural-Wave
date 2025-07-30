import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Cài đặt chung
fig, ax = plt.subplots(figsize=(14, 6))
plt.title("Biểu đồ Tích hợp Sóng Kondratiev (Sóng K) và Chu kỳ Juglar", fontsize=14, fontweight='bold')

# Vẽ nền cho Sóng K
wave_period = 50  # sóng K: 50 năm
juglar_period = 10  # chu kỳ Juglar: 10 năm

# Vẽ sóng Kondratiev bằng hàm sin kéo dài 50 năm
x = np.linspace(0, wave_period, 500)
y = np.sin(2 * np.pi * x / wave_period)
ax.plot(x, y, label="Sóng Kondratiev (K)", color="blue", linewidth=2)

# Đánh dấu giai đoạn A (tăng trưởng) và B (suy thoái)
ax.fill_between(x, y, where=(y >= 0), interpolate=True, color='skyblue', alpha=0.4, label="Giai đoạn A - Tăng trưởng")
ax.fill_between(x, y, where=(y < 0), interpolate=True, color='lightcoral', alpha=0.4, label="Giai đoạn B - Suy thoái")

# Thêm các chu kỳ Juglar bên trong Sóng K
for i in range(0, wave_period, juglar_period):
    ax.axvline(x=i, color='gray', linestyle='--', linewidth=1)
    ax.text(i + 1, -1.2, f"Juglar {i//juglar_period + 1}", rotation=90, va='bottom', fontsize=8)

# Thêm nhãn
ax.set_xlabel("Thời gian (năm)")
ax.set_ylabel("Biến động kinh tế")
ax.legend(loc='upper right')
ax.set_ylim(-1.5, 1.5)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
