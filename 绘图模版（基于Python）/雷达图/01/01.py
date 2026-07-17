import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. 设置字体为 Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

# 2. 设置全局字体加粗
plt.rcParams['font.weight'] = 'bold'        # 全局文字加粗
plt.rcParams['axes.labelweight'] = 'bold'   # 坐标轴标签加粗

# 3. 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 1. 准备数据
data = {
    'Metric': ['Sharpe ratio', 'wzy1', 'wzy2', 'wzy3', 'wzy4'],
    'MACD': [0.8, 2.2, 2.0, 3.0, 7.0],
    'KDJ': [0.6, 1.6, 4.0, 2.0, 4.8],
    'MACD+KDJ': [1.4, 3.8, 6.0, 5.0, 7.8]
}

df = pd.DataFrame(data)

# 2. 设置绘图参数
categories = list(df['Metric'])
N = len(categories)
# 计算角度
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# 3. 设置配色
colors = sns.color_palette("flare", n_colors=3)
"""
推荐几个科研常用的色板名（直接替换）：
"mako"：冷色调（深蓝到青色），非常高端，适合严肃的图表。
"rocket"：暖色调（深紫到亮橙），非常有冲击力。
"flare"：比较淡雅的红紫色。
"crest"：比较清新的蓝绿色。
"Spectral"：红橙黄绿蓝紫全光谱（区分度很高）。
"Set2" 或 "Pastel1"：低饱和度的莫兰迪色系（如果不喜欢太刺眼的颜色）。
"""
# 4. 初始化绘图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 设置起始角度和方向
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# A. 关闭默认的圆形网格和边界
ax.spines['polar'].set_visible(False) # 去掉最外圈圆
ax.yaxis.grid(False) # 去掉默认的圆形刻度网格
ax.xaxis.grid(True, color='grey', linestyle='solid', linewidth=2.5, alpha=0.9) # 保留放射状的轴线

# B. 手动绘制多边形网格线 (关键步骤)
# 定义你想要显示的刻度值
grid_levels = [2.5, 5, 8]

for level in grid_levels:
    # 创建一个这一层级数值的列表，长度需和 angles 一致以闭合
    grid_values = [level] * len(angles)
    # 绘制多边形线条 (zorder=0 确保在最底层)
    ax.plot(angles, grid_values, color='grey', linestyle='solid', linewidth=3, alpha=0.38, zorder=0)

# 5. 绘制每一列的数据
labels = ['MACD', 'KDJ', 'MACD+KDJ']

for idx, label in enumerate(labels):
    values = df[label].tolist()
    values += values[:1]  # 闭合数据环

    # 绘制线条 (zorder=10 确保在线条之上)
    ax.plot(angles, values, color=colors[idx], linewidth=2, linestyle='solid', label=label, zorder=10)
    # 填充颜色
    ax.fill(angles, values, color=colors[idx], alpha=0.25, zorder=10)

# 6. 添加标签和刻度
# 添加 x 轴标签 (维度名称)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=12)

# 添加 y 轴刻度 (数字) --放射线范围
plt.ylim(0, 9) # 设置数据范围

# 设置显示的刻度值
ax.set_yticks(grid_levels)
# 设置刻度标签文字，颜色设为黑色(black)以确保清晰
ax.set_yticklabels([str(i) for i in grid_levels], color="black", size=10)

# 【关键】设置刻度标签显示的角度位置
# 0 表示显示在最右侧的水平轴上，你可以改成 angles[0] 让它显示在第一根轴上
ax.set_rlabel_position(0)

# 确保 y 轴标签可见
ax.tick_params(axis='y', labelsize=10, labelcolor='black')

# 7. 添加图例和标题
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), frameon=False, ncol=3)
"""
右上角（默认）： loc='upper right'
左上角： loc='upper left'
右下角： loc='lower right'
左下角： loc='lower left'
正中间： loc='center'
右侧中间： loc='center right'
"""
# 8. 保存图片
plt.savefig('01.png', dpi=300, bbox_inches='tight')
plt.savefig('01.pdf', bbox_inches='tight')

# 显示图片
plt.show()

print("图表已生成并保存")