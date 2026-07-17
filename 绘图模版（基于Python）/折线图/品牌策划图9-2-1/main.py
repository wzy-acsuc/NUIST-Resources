import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- 1. 字体配置 (保持统一风格) ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# --- 2. 数据准备 (根据 image_e90f6c.png 提取) ---
# X轴: 预算投入 (万元)
budget = [50, 80, 100, 120, 150]

# Y轴: 预期 ROI
# 绿线 (乐观估计)
roi_optimistic = [2.5, 3.2, 4.0, 3.8, 3.5]
# 红线 (保守估计)
roi_conservative = [1.5, 2.0, 2.5, 2.2, 2.0]

# --- 3. 绘图 ---
fig, ax = plt.subplots(figsize=(9, 6), dpi=300)

# 绘制阴影区域 (敏感度范围)
# alpha=0.15 保证阴影很淡，不干扰线条
ax.fill_between(budget, roi_conservative, roi_optimistic, color='gray', alpha=0.15, label='_nolegend_')

# 绘制折线 1: 乐观估计 (绿色，三角形标记)
ax.plot(budget, roi_optimistic, color='#009900', linestyle='-', linewidth=1.5,
        marker='^', markersize=6, label='乐观估计', zorder=3)

# 绘制折线 2: 保守估计 (红色，圆形标记)
ax.plot(budget, roi_conservative, color='#E60000', linestyle='-', linewidth=1.5,
        marker='o', markersize=6, label='保守估计', zorder=3)

# --- 4. 细节美化 ---

# 标题
ax.set_title("图 9-2-1：营销预算投入与 ROI 敏感度分析", fontproperties=zh_font, size=16, y=1.02)

# 坐标轴标签
ax.set_xlabel("预算投入 (万元)", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("预期 ROI", fontproperties=zh_font, fontsize=12)

# 设置刻度字体
ax.tick_params(labelsize=11)

# 网格线 (保留全网格，颜色调淡)
ax.grid(True, linestyle='-', alpha=0.6, color='#D3D3D3')

# 图例 (右上角)
legend = ax.legend(loc='upper right', prop=zh_font, frameon=True, fontsize=10)

# --- 5. 边框设置 ---
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(0.8)

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('ROI_Sensitivity_Analysis.png', dpi=300, bbox_inches='tight')
print("图表已生成：ROI_Sensitivity_Analysis.png")
plt.show()