import matplotlib.pyplot as plt
import seaborn as sns
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

# --- 2. 数据准备 ---
brands = ["完香(旧)", "完香(新)", "竞品A", "竞品B"]
x_vals = [-2.0, 2.0, 1.0, -1.0]
y_vals = [1.0, 2.0, -2.0, -1.0]

# --- 3. 颜色与大小设置 ---
palette_name = 'deep'
colors = sns.color_palette(palette_name, n_colors=len(brands))

sizes = []
for brand in brands:
    if brand == "完香(新)":
        sizes.append(1000)
    else:
        sizes.append(600)

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(8, 7.5), dpi=300)

# 定义坐标轴范围 (提取到前面，方便画背景)
limit = 2.5

# 【核心修改】绘制四个象限的背景色
# 使用 fill_between 填充区域，zorder=0 确保在最底层
# 颜色选择：极淡的红、蓝、绿、黄，用于区分不同战略区域

# 第一象限 (右上)：高时尚 + 高价格 -> 淡蓝色背景
ax.fill_between([0, limit], 0, limit, color='#E3F2FD', alpha=0.5, zorder=0)

# 第二象限 (左上)：低时尚 + 高价格 -> 淡紫色背景
ax.fill_between([-limit, 0], 0, limit, color='#F3E5F5', alpha=0.5, zorder=0)

# 第三象限 (左下)：低时尚 + 低价格 -> 淡灰色背景
ax.fill_between([-limit, 0], -limit, 0, color='#F5F5F5', alpha=0.5, zorder=0)

# 第四象限 (右下)：高时尚 + 低价格 -> 淡绿色背景
ax.fill_between([0, limit], -limit, 0, color='#E8F5E9', alpha=0.5, zorder=0)


# 绘制散点 (zorder=3 确保在最上层)
ax.scatter(x_vals, y_vals, s=sizes, c=colors, alpha=0.9, zorder=3, edgecolors='white', linewidth=1.5)

# --- 5. 辅助元素 ---
# 绘制中心十字线 (zorder=1)
ax.axhline(y=0, color='black', linestyle='-', linewidth=1, zorder=1)
ax.axvline(x=0, color='black', linestyle='-', linewidth=1, zorder=1)

# 添加文字标签
offset_x = 0.15
offset_y = 0.05

for i, txt in enumerate(brands):
    ax.text(x_vals[i] + offset_x, y_vals[i] + offset_y, txt,
            fontproperties=zh_font, color='black',
            ha='left', va='center', fontsize=12, zorder=4) # 文字在更上层

# --- 6. 坐标轴与标题 ---
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

ticks = [-2.0, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2.0]
ax.set_xticks(ticks)
ax.set_yticks(ticks)

ax.set_xlabel("现代感/时尚度", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("价格/高端感", fontproperties=zh_font, fontsize=12)
ax.set_title("图 2-4：竞品心智坐标图", fontproperties=zh_font, fontsize=16, y=1.02)

# 边框设置
ax.grid(False) # 关闭默认网格，因为有了背景色块区分
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(1)

plt.tight_layout()
plt.savefig('图2-4.png', dpi=300, bbox_inches='tight')
print(f"图表已生成，四个象限已添加背景色。")
# plt.show()