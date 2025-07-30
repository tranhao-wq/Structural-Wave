# Re-import libraries after code execution environment reset
import numpy as np
import matplotlib.pyplot as plt

# Thiết lập trục thời gian mở rộng (1940–2060)
years = np.arange(1940, 2061)
kondratiev_wave = np.sin(2 * np.pi * (years - 1940) / 50)  # Sóng Kondratiev: chu kỳ ~50 năm
juglar_wave = 0.4 * np.sin(2 * np.pi * (years - 1940) / 10)  # Sóng Juglar: chu kỳ ~10 năm

# Pha phân tích – chia chu kỳ Kondratiev thành các pha A (tăng trưởng) và B (suy thoái)
phase_labels = []
for y in years:
    phase_position = (y - 1940) % 50
    if 0 <= phase_position < 25:
        phase_labels.append("A")  # Pha A: phát triển, đổi mới
    else:
        phase_labels.append("B")  # Pha B: thoái trào, khủng hoảng

# Vẽ biểu đồ
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(years, kondratiev_wave, label="Sóng Kondratiev (~50 năm)", color="blue", linewidth=2)
ax.plot(years, juglar_wave, label="Sóng Juglar (~10 năm)", color="green", linestyle="--", linewidth=1.5)

# Tô nền theo pha A/B
for i in range(len(years) - 1):
    color = "#D0F0FF" if phase_labels[i] == "A" else "#FFE0E0"
    ax.axvspan(years[i], years[i+1], color=color, alpha=0.2)

# Ghi nhãn pha A/B
for y in range(1940, 2060, 5):
    idx = np.where(years == y)[0][0]
    ax.text(y, 1.7, phase_labels[idx], color="gray", ha='center', fontsize=9, alpha=0.8)

# Các mốc thực tế để phân tích thêm
highlight_years = [1950, 1973, 1990, 2008, 2020, 2025, 2035, 2050]
for y in highlight_years:
    ax.axvline(x=y, color='gray', linestyle=':', linewidth=1)
    ax.text(y + 0.2, -2.1, str(y), rotation=90, va='bottom', fontsize=8)

# Cấu hình đồ thị
ax.set_title("Phân tích Sóng Kondratiev & Chu kỳ Juglar (1940–2060)", fontsize=14, fontweight='bold')
ax.set_xlabel("Năm")
ax.set_ylabel("Cường độ chu kỳ")
ax.legend(loc="upper left")
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_ylim(-2.2, 2.2)

plt.tight_layout()
plt.show()
