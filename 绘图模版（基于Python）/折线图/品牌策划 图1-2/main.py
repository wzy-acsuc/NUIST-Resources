import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- 1. 字体与画布设置 ---

# 设置全局西文字体为 Times New Roman
# 这确保了坐标轴上的数字 (2020, 2021... 和 0, 5, 10...) 显示为新罗马字体
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

# 设置中文字体 (用于标题)
# 【修改点】这里 size=16 决定了标题的大小
try:
    # macOS 优先使用宋体 (Songti SC)
    zh_font = font_manager.FontProperties(family='Songti SC', size=16)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    # Windows 备用方案
    try:
        zh_font = font_manager.FontProperties(family='SimSun', size=16)
    except:
        zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=16)

# 创建画布
fig, ax = plt.subplots(figsize=(9, 6), dpi=300)

# --- 2. 数据准备 ---
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
rates = np.array([12, 14, 18, 23, 29, 35])

# --- 3. 绘图 ---

# 绘制折线 (绿色实线，圆形标记)
ax.plot(years, rates, color='green', marker='o', markersize=9,
        linewidth=3, zorder=2)

# 区域填充 (浅绿色)
ax.fill_between(years, rates, 0, color='green', alpha=0.15, zorder=1)

# --- 4. 坐标轴与网格设置 ---

# 设置标题
# fontproperties=zh_font 会应用上面设置的 size=16
ax.set_title("图 1-2：胡麻油市场渗透率增长趋势 (%)", fontproperties=zh_font, y=1.02)

# 设置X轴刻度
ax.set_xticks(years)

# 设置Y轴范围和刻度
ax.set_ylim(-1, 38)
ax.set_yticks(np.arange(0, 40, 5))

# 设置刻度标签大小 (此时应用的是 Times New Roman)
ax.tick_params(axis='both', labelsize=12)

# 网格线
ax.grid(True, linestyle='--', alpha=0.5)

# --- 5. 保存与显示 ---
plt.tight_layout()
plt.savefig('图1-2.png', dpi=300, bbox_inches='tight')
print("图表已生成：图1-2.png (标题字号已调整为16)")
plt.show()