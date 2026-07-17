import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter # 用于显示百分号


# 1. 准备数据 (根据你的表格输入)
labels = ['MACD', 'KDJ', 'MACD+KDJ']
w_total_data = [2200, 2500, 3500]   # 左轴数据 (柱状图)
win_rate_data = [0.20, 0.30, 0.55]  # 右轴数据 (折线图)
OUTPUT_PDF = '02.pdf'
OUTPUT_PNG = '02.png'

# 2. 全局字体设置
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'

# 3. 创建画布
fig, ax1 = plt.subplots(figsize=(6, 4), dpi=300)

# 定义柱子宽度
bar_width = 0.3
x = np.arange(len(labels))

# ==========================================
# 第一部分：绘制左轴 (柱状图 - W_total)
# ==========================================
# 颜色取自目标图的深蓝色
color_bar = '#B0A875'
ax1.bar(x, w_total_data, width=bar_width, color=color_bar, label='$W_{total}$', zorder=10)

# 设置左轴范围和刻度
ax1.set_ylim(-10, 4000)  # 控制柱子和X轴距离
ax1.set_yticks(np.arange(0, 4001, 500)) # 0到4000，每隔500

# 样式美化
# ax1.set_ylabel('$W_{total}$', fontweight='bold', fontsize=12, rotation=0, loc='top')
ax1.tick_params(axis='y', labelsize=11)

# ==========================================
# 第二部分：绘制右轴 (折线图 - Win rate)
# ==========================================
# 创建共享X轴的副坐标系
ax2 = ax1.twinx()

# 颜色取自目标图的深红色
color_line = '#AF7EC0'
# 绘制折线：marker='o'即圆形节点，linewidth=3加粗
ax2.plot(x, win_rate_data, color=color_line, marker='o', markersize=8,
         linewidth=3, label='Win rate', zorder=20)

# 设置右轴范围 (0% - 60%)
ax2.set_ylim(0, 0.60)
# 设置右轴刻度格式为百分比
ax2.yaxis.set_major_formatter(PercentFormatter(1.0))
ax2.set_yticks(np.arange(0, 0.61, 0.1)) # 0.0到0.6，每隔0.1

# 右轴刻度字体加粗
ax2.tick_params(axis='y', labelsize=11)
for label in ax2.get_yticklabels():
    label.set_fontweight('bold')

# ==========================================
# 第三部分：坐标轴与箭头美化
# ==========================================

# --- 处理边框 (Spines) ---
# ax1 (左轴): 隐藏上、右
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_linewidth(2)
ax1.spines['bottom'].set_linewidth(2)
ax1.spines['left'].set_zorder(30) # 确保轴线在最上层

# ax2 (右轴): 隐藏上、左、底 (底和左由ax1负责)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['right'].set_linewidth(2) # 加粗右侧轴线
ax2.spines['right'].set_zorder(30)

# --- 绘制箭头 ---
# 1. 左Y轴箭头 (ax1 Top-Left)
ax1.plot(0, 1, "^k", transform=ax1.transAxes, clip_on=False, markersize=8, zorder=30)
# 2. X轴箭头 (ax1 Bottom-Right)
ax1.plot(1, 0, ">k", transform=ax1.transAxes, clip_on=False, markersize=8, zorder=30)
# 3. 右Y轴箭头 (ax1 Top-Right)
# 注意：这里我们依然用 ax1.transAxes，位置 (1, 1) 就是右上角
ax1.plot(1, 1, "^k", transform=ax1.transAxes, clip_on=False, markersize=8, zorder=30)

# --- X轴标签设置 ---
ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontweight='bold', fontsize=12)
# 加粗左轴刻度
for label in ax1.get_yticklabels():
    label.set_fontweight('bold')

# ==========================================
# 第四部分：合并图例
# ==========================================
# 因为有两个不同的轴，我们需要手动收集图例句柄(handles)和标签(labels)
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

# 合并并在左上角显示
legend = ax1.legend(lines_1 + lines_2, labels_1 + labels_2,
                    loc='upper left', frameon=False, fontsize=11,
                    bbox_to_anchor=(0.05, 0.95))

for text in legend.get_texts():
    text.set_fontweight('bold')

plt.tight_layout()
plt.savefig(OUTPUT_PDF, format='pdf')
plt.savefig(OUTPUT_PNG, dpi=300)
plt.show()