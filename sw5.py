import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu cho 2 đồ thị sóng K: một lý tưởng và một bị lệch
x1 = np.linspace(0, 6 * np.pi, 600)
y1 = np.sin(x1)  # Sóng K lý tưởng

x2 = np.linspace(0, 6 * np.pi, 600)
y2 = np.piecewise(
    x2,
    [x2 < 3 * np.pi, x2 >= 3 * np.pi],
    [lambda x: np.sin(x / 1.2), lambda x: np.sin(x / 0.8)]
)  # Sóng K bị kéo lệch (pha A dài hơn, pha B ngắn hơn)

# Tạo biểu đồ
fig, axs = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

# Biểu đồ 1: Sóng K lý tưởng
axs[0].plot(x1, y1, label="Sóng K lý tưởng", color='blue')
axs[0].axvline(x=3*np.pi, color='gray', linestyle='--', label="Ranh giới pha A/B")
axs[0].fill_between(x1, y1, 0, where=(x1 < 3*np.pi), alpha=0.2, color='green', label='Pha A (Lạc quan)')
axs[0].fill_between(x1, y1, 0, where=(x1 >= 3*np.pi), alpha=0.2, color='red', label='Pha B (Bi quan)')
axs[0].set_title("Sóng K lý tưởng (Pha A và B cân bằng)")
axs[0].legend(loc='upper right')
axs[0].set_ylabel("Tâm trạng kinh tế")

# Biểu đồ 2: Sóng K bị kéo lệch
axs[1].plot(x2, y2, label="Sóng K bị kéo lệch", color='purple')
axs[1].axvline(x=3*np.pi, color='gray', linestyle='--', label="Ranh giới pha A/B")
axs[1].fill_between(x2, y2, 0, where=(x2 < 3*np.pi), alpha=0.2, color='green', label='Pha A (Mở rộng)')
axs[1].fill_between(x2, y2, 0, where=(x2 >= 3*np.pi), alpha=0.2, color='red', label='Pha B (Rút ngắn)')
axs[1].set_title("Sóng K bị kéo lệch (Pha A dài hơn)")
axs[1].legend(loc='upper right')
axs[1].set_xlabel("Thời gian")
axs[1].set_ylabel("Tâm trạng kinh tế")

plt.tight_layout()
plt.show()
