import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager
import numpy as np

# --- 1. 字体与画布设置 ---
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# --- 2. 配色方案 (使用之前的模版配色) ---
colors = {
    "blue": "#4EA5F0",       # 蓝色
    "teal": "#2A9D8F",       # 青色
    "green": "#6ABD6E",      # 绿色
    "yellow": "#F4C126",     # 黄色
    "orange": "#FB9E28",     # 橙色
    "red": "#E64A45",        # 红色
    "purple": "#A55EEA",     # 紫色
}

# --- 3. 数据准备 ---
# 格式: (任务名称, 开始月份, 持续时长, 颜色Key)
tasks = [
    # 从下往上画，颜色依次变化
    ("品牌诊断", 1.0, 2.0, "blue"),    # 1-3月 (蓝色)
    ("VI设计", 3.0, 3.0, "teal"),     # 3-6月 (青色)
    ("产品焕新", 5.0, 4.0, "green"),   # 5-9月 (绿色)
    ("全域传播", 7.0, 5.0, "orange"),  # 7-12月 (橙色)
    ("效果评估", 11.0, 2.0, "red"),    # 11-13月 (红色)
]

# --- 4. 绘制甘特图 ---
y_positions = np.arange(len(tasks))
bar_height = 0.5

for i, (task, start, duration, color_key) in enumerate(tasks):
    c = colors[color_key]
    # 使用圆角矩形
    rect = patches.FancyBboxPatch(
        (start, i - bar_height / 2),
        duration, bar_height,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        fc=c, ec="none", alpha=0.9
    )
    ax.add_patch(rect)

# --- 5. 坐标轴与辅助线设置 ---

# Y轴刻度
ax.set_yticks(y_positions)
ax.set_yticklabels([t[0] for t in tasks], fontproperties=zh_font, fontsize=11)

# Y轴范围
ax.set_ylim(-0.6, len(tasks) - 0.4)

# X轴设置 (1月-13月)
ax.set_xlim(1, 13.5)
ax.set_xticks(np.arange(2, 14, 2))
ax.set_xticklabels([str(i) for i in range(2, 14, 2)], fontproperties=zh_font, fontsize=11)
ax.set_xlabel("月份", fontproperties=zh_font, fontsize=12)

# 标题
ax.set_title("图 9-3：营销执行甘特图 (12个月)", fontproperties=zh_font, fontsize=16, y=1.02)

# 辅助网格
ax.grid(axis='x', linestyle='--', alpha=0.5, color='lightgray', zorder=0)

# --- 6. 边框设置 ---
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(0.8)

# --- 7. 保存与展示 ---
plt.tight_layout()
plt.savefig('图9-3.png', dpi=300, bbox_inches='tight')
print("图片已生成：Marketing_Execution_Gantt_Colorful.png")
#plt.show()