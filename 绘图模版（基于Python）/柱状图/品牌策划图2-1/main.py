import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import font_manager

# --- 1. 字体与画布设置 ---

# 设置全局西文字体为 Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

# 设置中文字体
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    try:
        zh_font = font_manager.FontProperties(family='SimSun', size=12)
    except:
        zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# 创建画布
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)

# --- 2. 数据准备 ---
regions = ['山西', '北京', '河北', '陕西', '山东', '其他']
counts = [210, 85, 60, 55, 45, 45]

# --- 3. 颜色设置 ---
"""
推荐几个科研常用的色板名（直接替换）：
"mako"：冷色调（深蓝到青色），非常高端，适合严肃的图表。
"rocket"：暖色调（深紫到亮橙），非常有冲击力。
"flare"：比较淡雅的红紫色。
"crest"：比较清新的蓝绿色。
"Spectral"：红橙黄绿蓝紫全光谱（区分度很高）。
"Set2" 或 "Pastel1"：低饱和度的莫兰迪色系（如果不喜欢太刺眼的颜色）。
"""
palette_name = 'crest'
colors = sns.color_palette(palette_name, n_colors=len(regions))

# --- 4. 绘图 (核心修改) ---

# 【修改说明】
# width 参数控制柱子宽度。
# 设为 0.8 表示柱子占据刻度间距的 80%，留白 20%，这样看起来既宽又紧凑。
# 如果想要几乎没有缝隙，可以设为 0.95
bars = ax.bar(regions, counts, color=colors, width=0.5, zorder=2)

# --- 5. 细节美化与标注 ---

# 设置标题
ax.set_title("图 2-1：调研样本区域分布图 (频数)", fontproperties=zh_font, size=16, y=1.02)

# 设置X轴标签
ax.set_xticklabels(regions, fontproperties=zh_font, fontsize=12)

# 设置Y轴范围和字体
ax.set_ylim(0, 225)
ax.tick_params(axis='y', labelsize=12)

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('图2-1.png', dpi=300, bbox_inches='tight')
print(f"图表已生成，柱子宽度已调整为 0.8 (更紧凑)")
# plt.show()