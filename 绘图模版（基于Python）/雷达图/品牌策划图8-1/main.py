import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import font_manager

# --- 1. 字体配置 (保持不变) ---
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.unicode_minus'] = False

try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    print("未找到 Songti SC，尝试使用 STSong...")
    zh_font = font_manager.FontProperties(family='STSong', size=12)

# --- 2. 准备数据 (仅修改此处数据，适配 image_f4efb8.png) ---
# 映射说明: 原图是1-5分制，这里保持原代码逻辑映射为20-100分制
# 映射关系: 1=20, 2=40, 3=60, 4=80, 5=100
data = {
    # 维度替换为 SERVQUAL 的五个维度
    '维度': ['可靠性', '有形性', '移情性', '保证性', '响应性'],

    # 数据替换为图中的两条线
    # 第一条线：期望 (Expectation) - 对应原代码的蓝色
    # 特征：外圈几乎全满，仅在"响应性"处略微收缩
    '期望 (Expectation)': [100, 100, 100, 100, 85],

    # 第二条线：感知 (Perception) - 对应原代码的橙色
    # 特征：可靠性与保证性较高，有形性与移情性较低
    '感知 (Perception)': [95, 70, 75, 90, 80]
}

df = pd.DataFrame(data)

# --- 3. 设置绘图参数 (保持不变) ---
categories = list(df['维度'])
N = len(categories)

# 计算角度
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# --- 4. 设置配色 (保持原代码 tab10 不变) ---
colors = sns.color_palette("rocket", n_colors=2)

# --- 5. 初始化绘图 (保持不变) ---
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=300)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# 网格设置
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)
ax.xaxis.grid(True, color='grey', linestyle='--', linewidth=1, alpha=0.5)

# 手动绘制多边形网格线
grid_levels = [20, 40, 60, 80, 100]

for level in grid_levels:
    grid_values = [level] * len(angles)
    ax.plot(angles, grid_values, color='grey', linestyle='-', linewidth=1, alpha=0.2, zorder=0)

# --- 6. 绘制每一列的数据 (保持不变) ---
labels = list(data.keys())[1:]

for idx, label in enumerate(labels):
    values = df[label].tolist()
    values += values[:1]

    # 绘制线条
    ax.plot(angles, values, color=colors[idx], linewidth=2.5, linestyle='solid', label=label, zorder=10)
    # 填充颜色
    ax.fill(angles, values, color=colors[idx], alpha=0.15, zorder=10)

# --- 7. 添加标签和刻度 (保持不变) ---
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
for label in ax.get_xticklabels():
    label.set_fontproperties(zh_font)
    label.set_fontsize(13)
    label.set_position((0, -0.05))

plt.ylim(0, 105)

# Y轴刻度标签
ax.set_yticks([20, 40, 60, 80])
ax.set_yticklabels(['1', '2', '3', '4'], color="#666666", size=10, fontfamily='Times New Roman')
ax.yaxis.set_zorder(20)
ax.set_rlabel_position(10)

# --- 8. 图例和标题 (保持不变，仅更新标题文字) ---
legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                    frameon=False, ncol=4, fontsize=12)
for text in legend.get_texts():
    text.set_fontproperties(zh_font)

plt.title("图 8-1：SERVQUAL 五维体验雷达图", fontproperties=zh_font, fontsize=16, y=1.15, weight='bold')

# --- 9. 保存 ---
plt.savefig('图8-1.png', dpi=300, bbox_inches='tight')
print("图表已生成：SERVQUAL_Radar_Chart_v2.png")
# plt.show()