import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- 1. 字体配置 (保持统一风格) ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# --- 2. 数据准备 (根据 image_e903e8.png 复刻) ---
dimensions = ['有形性', '可靠性', '响应性', '保证性', '移情性']
# Gap 值 (感知 - 期望)，均为负值
gap_values = [-0.7, -0.2, -0.4, -0.2, -0.4]

# --- 3. 颜色设置 (美化配色) ---
# 逻辑：第一项(有形性)差距最大，用深红色警示；其他项用暖橙色
# 使用了 Material Design 风格的色值，比默认颜色更有质感
colors = ['#D32F2F'] + ['#FFA000'] * 4

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

# 绘制柱状图
# zorder=3 确保柱子在网格线之上
bars = ax.bar(dimensions, gap_values, color=colors, width=0.4, zorder=3)

# --- 5. 辅助元素与细节 ---

# 添加 y=0 的基准线 (黑色实线)
ax.axhline(0, color='black', linewidth=1, zorder=4)

# 添加数值标签 (显示在柱子下方)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height - 0.02, # 位置稍微往下一点
            f'{height:.1f}',
            ha='center', va='top',
            fontsize=11, fontname='Times New Roman', color='black')

# (可选) 添加 -0.5 的预警线，呼应文字说明
ax.axhline(-0.5, color='gray', linestyle='--', linewidth=1, alpha=0.6)
ax.text(4.4, -0.51, '预警线 -0.5', color='gray', fontsize=9, fontproperties=zh_font)

# --- 6. 坐标轴与标题 ---

# 标题
ax.set_title("图 8-1-1：SERVQUAL 五维服务质量差距 (Gap) 分析", fontproperties=zh_font, size=16, y=1.02)

# Y轴标签
ax.set_ylabel("感知 - 期望 (Gap 值)", fontproperties=zh_font, fontsize=12)

# 设置刻度字体
ax.tick_params(axis='x', labelsize=12)
for label in ax.get_xticklabels():
    label.set_fontproperties(zh_font)

# Y轴范围 (留出一点空间)
ax.set_ylim(-0.8, 0.05)

# 网格线 (只显示Y轴网格)
ax.grid(axis='y', linestyle='--', alpha=0.4, color='gray', zorder=0)

# 边框设置
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.8)
ax.spines['bottom'].set_visible(False) # 底部边框隐藏，因为有了 y=0 线

# --- 7. 保存与显示 ---
plt.tight_layout()
plt.savefig('图8-1-1.png', dpi=300, bbox_inches='tight')
print("图表已生成：SERVQUAL_Gap_Analysis.png")
#plt.show()