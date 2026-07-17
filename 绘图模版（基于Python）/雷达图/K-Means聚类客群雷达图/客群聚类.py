import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import font_manager

# --- 1. 字体配置 (Mac M4 专用) ---
# 全局西文设置
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.unicode_minus'] = False

# 中文设置：自动寻找 Mac 宋体
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    print("未找到 Songti SC，尝试使用 STSong...")
    zh_font = font_manager.FontProperties(family='STSong', size=12)

# --- 2. 准备数据 (基于你的客群画像) ---
data = {
    '维度': ['健康意识', '消费能力', '价格敏感', '品牌忠诚', '社交分享'],
    '健康养生派': [95, 60, 40, 85, 70],
    '美容护肤派': [75, 95, 35, 70, 85],
    '精打细算派': [50, 45, 95, 60, 55],
    '场景尝鲜派': [65, 55, 60, 75, 80]
}

df = pd.DataFrame(data)

# --- 3. 设置绘图参数 ---
categories = list(df['维度'])
N = len(categories)

# 计算角度 (将圆周分为 N 份)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1] # 闭合角度

# --- 4. 设置配色 ---
# 推荐使用 "Set2" 或 "husl"，因为有4个类别，需要高区分度
# flare 是渐变色，容易导致某两个客群颜色太像分不清
colors = sns.color_palette("Set2", n_colors=4)

# --- 5. 初始化绘图 ---
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=300)

# 设置起始角度（90度，即12点钟方向）和方向（-1表示顺时针）
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# A. 关闭默认圆形网格
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)
ax.xaxis.grid(True, color='grey', linestyle='--', linewidth=1, alpha=0.5)

# B. 手动绘制多边形网格线 (0-100分制)
grid_levels = [25, 50, 75, 100]

for level in grid_levels:
    grid_values = [level] * len(angles)
    ax.plot(angles, grid_values, color='grey', linestyle='-', linewidth=1, alpha=0.2, zorder=0)

# --- 6. 绘制每一列的数据 ---
# 提取客群名称
labels = list(data.keys())[1:] # 跳过第一个 key '维度'

for idx, label in enumerate(labels):
    values = df[label].tolist()
    values += values[:1]  # 闭合数据

    # 绘制线条
    ax.plot(angles, values, color=colors[idx], linewidth=2.5, linestyle='solid', label=label, zorder=10)
    # 填充颜色
    ax.fill(angles, values, color=colors[idx], alpha=0.2, zorder=10)

# --- 7. 添加标签和刻度 ---

# A. 添加维度标签 (应用中文字体)
ax.set_xticks(angles[:-1])
# 这里不能直接用 set_xticklabels，因为无法直接传 fontproperties
# 我们需要手动设置标签属性
ax.set_xticklabels(categories)
for label in ax.get_xticklabels():
    label.set_fontproperties(zh_font)
    label.set_fontsize(13)
    # 稍微调整标签位置，避免和图形重叠
    label.set_position((0, -0.05))

# B. 设置 Y 轴范围
plt.ylim(0, 102)

# C. 设置 Y 轴刻度标签
ax.set_yticks(grid_levels)
ax.set_yticklabels([str(i) for i in grid_levels], color="#666666", size=9, fontfamily='Times New Roman')
ax.yaxis.set_zorder(20)
# 设置刻度显示的角度 (避开正上方的轴，稍微偏一点以免遮挡文字)
ax.set_rlabel_position(10)

# --- 8. 图例和标题 ---

# 图例 (应用中文字体)
legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                   frameon=False, ncol=4, fontsize=12)
# 修复图例中文显示
for text in legend.get_texts():
    text.set_fontproperties(zh_font)

# 添加标题
plt.title("图2-3：K-Means聚类客群雷达图（四类目标用户画像）", fontproperties=zh_font, fontsize=16, y=1.15, weight='bold')

# --- 9. 保存 ---
plt.savefig('客群聚类雷达图.png', dpi=300, bbox_inches='tight')
plt.savefig('客群聚类雷达图.pdf', bbox_inches='tight')

