import numpy as np
import matplotlib.pyplot as plt

# Thiết lập thời gian thực tế từ 1980 đến 2040
years = np.arange(1980, 2041)
total_years = len(years)

# Sóng Kondratiev (khoảng 50 năm một chu kỳ)
k_wave = np.sin(2 * np.pi * (years - 1980) / 50)

# Sóng Juglar (~10 năm một chu kỳ)
juglar_wave = 0.4 * np.sin(2 * np.pi * (years - 1980) / 10) - 1.2  # hạ thấp để phân biệt

# Dự đoán structural wave theo giai đoạn (vẽ như step chart)
structural_waves = np.zeros_like(years, dtype=float)

# Gán giá trị 1 cho các giai đoạn sóng công nghệ lớn
for i, year in enumerate(years):
    if 1980 <= year < 1995:
        structural_waves[i] = 0.3  # PC & Internet đầu
    elif 1995 <= year < 2008:
        structural_waves[i] = 0.6  # Web 1.0 + Mobile
    elif 2008 <= year < 2020:
        structural_waves[i] = 0.9  # Cloud + Mobile + AI sơ khai
    elif 2020 <= year < 2025:
        structural_waves[i] = 1.2  # AI, Data, Remote Work
    elif 2025 <= year < 2035:
        structural_waves[i] = 1.5  # AGI, AI Everywhere, Automation at scale
    elif year >= 2035:
        structural_waves[i] = 1.8  # Gen AI, BioTech + Human augmentation

# Vẽ biểu đồ
fig, ax = plt.subplots(figsize=(16, 8))
plt.title("Sóng Kondratiev, Chu kỳ Juglar và Structural Tech Waves (1980–2040)", fontsize=14, fontweight='bold')

# Vẽ các sóng
ax.plot(years, k_wave, label="Sóng Kondratiev (~50 năm)", color="blue", linewidth=2)
ax.plot(years, juglar_wave, label="Chu kỳ Juglar (~10 năm)", color="green", linestyle="--", linewidth=1.5)
ax.plot(years, structural_waves, label="Sóng Công nghệ - Structural Wave", color="orange", linewidth=3)

# Điểm mốc lịch sử
highlight_years = [1980, 1995, 2008, 2020, 2025, 2035]
for y in highlight_years:
    ax.axvline(x=y, color='gray', linestyle=':', linewidth=1)
    ax.text(y + 0.2, 2.0, str(y), rotation=90, va='bottom', fontsize=8)

# Thiết lập
ax.set_xlabel("Năm")
ax.set_ylabel("Biến động / Cường độ")
ax.legend(loc="upper left")
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.show()
