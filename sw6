import matplotlib.pyplot as plt

# Dữ liệu
phases = ['Pha A', 'Pha B']
durations = [9.0, 10.25]  # thời lượng trung bình chu kỳ J
errors = [[0.7], [0.05]]  # sai số hoặc độ biến thiên (ví dụ 9.0 ± 0.7)

# Tạo biểu đồ
fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(phases, durations, color=['green', 'red'], alpha=0.7)
ax.errorbar(phases, durations, yerr=[[0.7], [0.05]], fmt='none', ecolor='black', capsize=8)

# Gắn nhãn
for bar, label in zip(bars, ['3–4 chu kỳ J\n(~8.3–9.1 năm)', '2 chu kỳ J\n(~10.2–10.3 năm)']):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.2, label, ha='center', fontsize=10)

# Chú thích
ax.set_title("Thời lượng trung bình của chu kỳ Juglar (pha A vs B trong sóng K)", fontsize=12)
ax.set_ylabel("Số năm (trung bình mỗi chu kỳ J)")
ax.set_ylim(0, 12)

plt.tight_layout()
plt.show()
