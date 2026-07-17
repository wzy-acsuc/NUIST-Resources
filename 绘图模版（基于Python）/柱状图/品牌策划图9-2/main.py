import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import font_manager

# --- 1. 字体与画布设置 ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    try:
        zh_font = font_manager.FontProperties(family='SimSun', size=12)
    except:
        zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# 创建画布
fig, ax = plt.subplots(figsize=(7, 5.5), dpi=300)

# --- 2. 数据准备 (根据 image_f47b20.png 修改) ---
labels = ['销售额增长', '品牌知名度', '复购率', 'ROI']
# 根据图片高度估算的数值
values = [25.0, 40.0, 15.0, 3.5]

# --- 3. 颜色设置 (保持原代码的 flare 模版) ---
palette_name = 'flare'
colors = sns.color_palette(palette_name, n_colors=len(labels))

# --- 4. 绘图 ---
# width=0.7 让柱子宽一点，符合原图视觉
bars = ax.bar(labels, values, color=colors, width=0.5, zorder=2)

# --- 5. 细节美化与标注 ---

# 标题更新
ax.set_title("表 9-2：关键绩效指标 (KPI) 目标设定", fontproperties=zh_font, size=16, y=1.02)

# X轴标签
ax.set_xticklabels(labels, fontproperties=zh_font, fontsize=12)

# 【修改】Y轴范围设为 0 到 42 (适应最大值 40)
ax.set_ylim(0, 42)
ax.tick_params(axis='y', labelsize=12)

# 边框设置
for spine in ax.spines.values():
    spine.set_linewidth(0.8)
    spine.set_color('black')

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{height}', ha='center', va='bottom', fontsize=11, fontname='Times New Roman')

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('图9-2.png', dpi=300, bbox_inches='tight')
print(f"图表已生成：数据已更新为 KPI 指标，使用 {palette_name} 配色")
#plt.show()