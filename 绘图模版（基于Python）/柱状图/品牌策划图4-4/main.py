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

# 创建画布 (调整宽高比以匹配原图)
fig, ax = plt.subplots(figsize=(4, 3.5), dpi=300)

# --- 2. 数据准备 (根据图片 image_626d3c.png) ---
labels = ['暖金', '翠绿', '古铜', '纯白']
values = [45, 25, 20, 10]

# --- 3. 颜色设置 ---
# 原图使用的是 Seaborn 的 "Set2" 配色
# 顺序正好是：0-蓝绿, 1-橙色, 2-灰蓝, 3-粉色
palette_name = 'Set2'
colors = sns.color_palette(palette_name, n_colors=len(labels))

# --- 4. 绘图 ---
# width=0.75 让柱子较宽，符合原图的视觉比例
bars = ax.bar(labels, values, color=colors, width=0.6, zorder=2)

# --- 5. 细节美化与标注 ---

# 设置标题
ax.set_title("图 4-4：新包装色彩偏好感知测试 (%)", fontproperties=zh_font, size=16, y=1.02)

# 设置X轴标签
ax.set_xticklabels(labels, fontproperties=zh_font, fontsize=12)

# 设置Y轴范围 (留出一点头部空间)
ax.set_ylim(0, 48)
ax.tick_params(axis='y', labelsize=12)

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('图4-4.png', dpi=300, bbox_inches='tight')
print(f"图表已生成：使用 Set2 配色，柱子宽度 0.75")
#plt.show()