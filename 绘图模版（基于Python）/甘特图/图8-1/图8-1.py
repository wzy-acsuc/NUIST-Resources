import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager
import numpy as np

# --- 1. 字体与画布设置 ---
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
try:
    # 优先使用 macOS 的 Songti SC，如果没有则使用 Windows 的 Microsoft YaHei
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# 创建画布
fig, ax = plt.subplots(figsize=(16, 9), dpi=300)

# --- 2. 数据准备 ---
tasks = [
    # --- 底部 ---
    ("品牌官网上线", 1.0, 2.0, "blue"),
    ("首批KOC招募", 1.5, 3.0, "teal"),
    ("小红书账号运营", 2.0, 11.0, "yellow"),
    ("抖音短视频矩阵", 3.0, 10.0, "pink"),
    ("618大促", 5.5, 1.0, "green"),
    ("暑期学生专属活动", 7.0, 2.0, "orange"),
    ("双11大促", 10.5, 1.5, "red"),
    ("年货节大促", 12.0, 1.0, "purple"),
    ("私域社群运营", 2.0, 11.0, "brown"),
    ("会员体系上线", 3.0, 2.0, "light_blue"),
    # --- 顶部 ---
]

# --- 3. 配色方案 ---
colors = {
    "blue": "#4EA5F0", "teal": "#2A9D8F", "yellow": "#F4C126",
    "pink": "#E75384", "green": "#6ABD6E", "orange": "#FB9E28",
    "red": "#E64A45", "purple": "#A55EEA", "brown": "#8D6E63",
    "light_blue": "#4FC3F7"
}

# --- 4. 绘制甘特图 ---
y_positions = np.arange(len(tasks))
bar_height = 0.4

for i, (task, start, duration, color_key) in enumerate(tasks):
    c = colors[color_key]
    rect = patches.FancyBboxPatch(
        (start, i - bar_height / 2),
        duration, bar_height,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        fc=c, ec="none", alpha=0.9
    )
    ax.add_patch(rect)

# --- 5. 坐标轴与辅助线设置 ---

# Y轴刻度
ax.set_yticks(y_positions)
ax.set_yticklabels([t[0] for t in tasks], fontproperties=zh_font, fontsize=11)

# 【核心修改点】手动设置Y轴范围，防止顶部和底部被切掉
# -1 表示底部留出空间，len(tasks) 表示顶部留出空间
ax.set_ylim(-0.5, len(tasks)-0.5)

# X轴设置
ax.set_xlim(1, 13)
ax.set_xticks(np.arange(1, 14))
ax.set_xticklabels([f"{i}月" for i in range(1, 14)], fontproperties=zh_font, fontsize=11)
ax.set_xlabel("时间 (月份)", fontproperties=zh_font, fontsize=14)

# 标题
ax.set_title("图8-1：年度营销节奏甘特图（大促节点与内容波峰规划）", fontproperties=zh_font, fontsize=18, y=1.03)

# 辅助网格
ax.grid(axis='x', linestyle='--', alpha=0.3, color='gray', zorder=0)

# --- 6. 添加特殊标注 ---
# 618 线
ax.axvline(x=6.0, color='#E64A45', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(6.1, len(tasks) - 0.8, "618大促", color='#E64A45', fontproperties=zh_font, fontsize=10) # 这里的坐标也可以微调

# 双11 线
ax.axvline(x=11.0, color='#E64A45', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(11.1, len(tasks) - 0.8, "双11", color='#E64A45', fontproperties=zh_font, fontsize=10)

# --- 7. 添加图例 ---
legend_handles = [
    patches.Patch(color=colors["yellow"], label='日常运营'),
    patches.Patch(color=colors["green"], label='电商大促'),
    patches.Patch(color=colors["pink"], label='内容营销')
]
ax.legend(handles=legend_handles, loc='upper right', prop=zh_font, frameon=True, fontsize=12)

# --- 8. 保存与展示 ---
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.tight_layout()
plt.savefig('Marketing_Gantt_Chart.png', dpi=300, bbox_inches='tight')
print("图片已生成：Marketing_Gantt_Chart_Fixed.png")
# plt.show()