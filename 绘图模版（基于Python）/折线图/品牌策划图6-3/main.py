import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- 1. 字体配置 ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# --- 2. 数据准备 (根据图片估算) ---
years = np.array([2026, 2027, 2028, 2029, 2030])
# 估算的 Y 轴数值 (万元)
values = np.array([285, 330, 385, 450, 525])

# --- 3. 颜色设置 ---
# 原图是紫色，我们使用 hex 代码或颜色名
main_color = 'purple'

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(7, 5), dpi=300)

# 绘制折线 (紫色、虚线、方形标记)
ax.plot(years, values, color=main_color, linestyle='--', marker='s',
        markersize=6, linewidth=1.5, zorder=2)

# 【核心修改】添加线下阴影 (填充区域)
# alpha=0.15 控制透明度，让网格线能透出来
# y2=0 表示填充到X轴，或者填充到Y轴下限 (这里设为270让底部平整)
ax.fill_between(years, values, 270, color=main_color, alpha=0.15, zorder=1)

# --- 5. 细节美化 ---

# 标题
ax.set_title("图 6-3：2026-2030 完香胡麻油市场规模预测 (万元)", fontproperties=zh_font, size=14, y=1.02)

# 设置坐标轴范围
ax.set_ylim(270, 535)
ax.set_xlim(2025.8, 2030.2) # 左右留一点空隙

# 设置刻度字体
ax.tick_params(axis='both', labelsize=10)

# 网格线 (保留全网格)
ax.grid(True, linestyle='-', alpha=0.8)

# 保留四周边框 (Spines)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(0.8)

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('Market_Forecast_Line.png', dpi=300, bbox_inches='tight')
print(f"图表已生成，已添加紫色阴影填充。")
plt.show()