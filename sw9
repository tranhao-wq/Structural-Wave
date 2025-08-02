import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Thiết lập thời gian trục x: năm từ 1800 đến 2020
years = list(range(1800, 2021))

# Các chu kỳ đại diện (sơ đồ hóa)
# Sóng Kondratieff (K) ~ 50-60 năm
k_cycles = [(1800, 1850), (1850, 1900), (1900, 1950), (1950, 2000)]

# Chu kỳ Kuznets ~ 15-25 năm, chủ yếu ở Mỹ
kuznets_cycles = [(1815, 1835), (1840, 1860), (1870, 1890), (1910, 1930), (1945, 1965), (1975, 1995)]

# Chu kỳ J (Juglar) ~ 7-11 năm, phổ biến toàn cầu
j_cycles = [(1820, 1830), (1838, 1848), (1856, 1866), (1874, 1884), (1892, 1902),
            (1910, 1920), (1928, 1938), (1946, 1956), (1964, 1974), (1982, 1992)]

fig, ax = plt.subplots(figsize=(14, 6))

# Vẽ sóng K (dài, nền xanh nhạt)
for start, end in k_cycles:
    ax.axvspan(start, end, color='lightblue', alpha=0.4)

# Vẽ chu kỳ Kuznets (nền cam nhạt)
for start, end in kuznets_cycles:
    ax.axvspan(start, end, color='orange', alpha=0.3)

# Vẽ chu kỳ J (nền hồng nhạt)
for start, end in j_cycles:
    ax.axvspan(start, end, color='pink', alpha=0.3)

# Ghi chú
ax.set_xlim(1800, 2020)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title("Biểu đồ trực quan hóa mối quan hệ giữa các chu kỳ: Kondratieff (K), Kuznets, và Juglar (J)", fontsize=14)

# Chú thích
legend_patches = [
    mpatches.Patch(color='lightblue', alpha=0.4, label='Sóng K (Kondratieff) ~ 50-60 năm'),
    mpatches.Patch(color='orange', alpha=0.3, label='Chu kỳ Kuznets ~ 15-25 năm'),
    mpatches.Patch(color='pink', alpha=0.3, label='Chu kỳ J (Juglar) ~ 7-11 năm')
]
ax.legend(handles=legend_patches, loc='upper right')

plt.tight_layout()
plt.show()
