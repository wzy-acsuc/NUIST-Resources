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

# --- 2. 数据准备 ---
labels = ['养生极客', '精致宝妈', '传统拥趸', '独居青年']
values = [0.85, 0.72, 0.65, 0.58]

# --- 3. 颜色设置 (使用模版配色) ---
# 【修改】使用 'mako' (冷色系渐变: 深蓝->青绿)
# 其他推荐: 'rocket' (暖色), 'viridis' (黄绿蓝), 'flare' (红紫)
palette_name = 'flare'
colors = sns.color_palette(palette_name, n_colors=len(labels))

# --- 4. 绘图 ---
# width=0.5 保持较细的柱子
bars = ax.bar(labels, values, color=colors, width=0.4, zorder=2)

# --- 5. 细节美化与标注 ---

# 标题
ax.set_title("图 7-3：不同细分人群 “信任→忠诚” 路径系数对比", fontproperties=zh_font, size=16, y=1.02)

# X轴标签
ax.set_xticklabels(labels, fontproperties=zh_font, fontsize=12)

# 【修改】Y轴范围设为 0 到 1
ax.set_ylim(0, 1.01)
ax.tick_params(axis='y', labelsize=12)

# 边框设置
for spine in ax.spines.values():
    spine.set_linewidth(0.8)
    spine.set_color('black')

# (可选) 添加数值标签，让数据更直观
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
            f'{height:.2f}', ha='center', va='bottom', fontsize=10, fontname='Times New Roman')

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('图7-3.png', dpi=300, bbox_inches='tight')
print(f"图表已生成：使用 {palette_name} 配色，Y轴最大值设为 1")
# plt.show()