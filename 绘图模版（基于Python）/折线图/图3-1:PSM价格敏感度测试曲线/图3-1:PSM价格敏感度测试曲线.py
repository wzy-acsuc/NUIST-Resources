import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib.patches as patches
import seaborn as sns
import pandas as pd
import numpy as np
import os

# --- 1. 字体配置 (自动寻找 Mac 宋体) ---
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    print("未找到 Songti SC，尝试使用 STSong...")
    zh_font = font_manager.FontProperties(family='STSong', size=12)

# 全局西文配置 (Times New Roman)
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.unicode_minus'] = False

# --- 2. 数据准备 ---
prices = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
data = {
    'Price': prices,
    'Too Cheap': [85, 70, 50, 30, 15, 8, 4, 2, 1, 0],
    'Cheap':     [90, 80, 75, 55, 35, 20, 10, 5, 3, 1],
    'Expensive': [2, 10, 25, 45, 65, 80, 92, 97, 99, 100],
    'Too Expensive': [0, 2, 8, 20, 35, 55, 75, 90, 96, 100]
}
df = pd.DataFrame(data)

# --- 3. 配色设置 (Flare 主题) ---
palette = sns.color_palette("flare", n_colors=4)
c_too_cheap = palette[0]
c_cheap = palette[1]
c_exp = palette[2]
c_too_exp = palette[3]

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# 绘制四条曲线 (zorder=10)
ax.plot(df['Price'], df['Too Cheap'], marker='s', markersize=6, linewidth=2,
        color=c_too_cheap, label='太便宜', zorder=10)
ax.plot(df['Price'], df['Cheap'], marker='^', markersize=6, linewidth=2,
        color=c_cheap, label='便宜', zorder=10)
ax.plot(df['Price'], df['Expensive'], marker='o', markersize=6, linewidth=2,
        color=c_exp, label='贵', zorder=10)
ax.plot(df['Price'], df['Too Expensive'], marker='D', markersize=6, linewidth=2,
        color=c_too_exp, label='太贵', zorder=10)

# --- 5. 关键分析区域绘制 ---
# A. 最优价格区间
ax.axvspan(50, 68, color='#E0F2F1', alpha=0.6, zorder=0, label='最优价格区间')

# B. 最优价格点
optimal_price = 59
optimal_percent = 53
ax.axvline(x=optimal_price, color='#D4AF37', linestyle='--', linewidth=1.5, zorder=5)

# C. 标注
ax.annotate(f"最优价格点\n¥{optimal_price}",
            xy=(optimal_price, optimal_percent),
            xytext=(optimal_price + 2, optimal_percent + 10),
            fontproperties=zh_font, fontsize=10, color='#B8860B',
            arrowprops=dict(arrowstyle='->', color='#B8860B', lw=1.5))

# --- 6. 坐标轴与标签美化 ---
ax.set_title("图3-1：PSM价格敏感度测试曲线", fontproperties=zh_font, fontsize=16, y=1.0, weight='light')
ax.set_xlabel("价格（元/500ml）", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("累积选择比例（%）", fontproperties=zh_font, fontsize=12)
ax.set_xlim(25, 125)
ax.set_ylim(0, 105)
plt.xticks(fontname='Times New Roman', fontsize=10)
plt.yticks(fontname='Times New Roman', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.4, color='#CCCCCC', zorder=0)

# --- 7. 图例设置 (修复报错的关键部分) ---
# 先生成图例对象，不传 zorder 参数
legend = ax.legend(loc='upper left', frameon=True, fancybox=False,
                   edgecolor='#DDDDDD', framealpha=0.9)

# 【核心修复】单独设置图例的 zorder
legend.set_zorder(1000)

# 设置图例字体
for text in legend.get_texts():
    text.set_fontproperties(zh_font)
    text.set_fontsize(10)

# --- 8. 保存与显示 ---
plt.tight_layout()
plt.savefig('图3-1：PSM价格敏感度测试曲线.png', dpi=300, bbox_inches='tight')
# plt.show()
print("✅ 图片已生成，报错已修复。")