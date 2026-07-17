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

# --- 2. 准备数据 (已根据上传图片 image_63caf0.png 修改) ---
# 原图是1-5分制，这里映射为20-100分制以适配坐标轴
# 映射关系: 1=20, 2=40, 3=60, 4=80, 5=100
# --- 2. 准备数据 (根据 image_63caf0.png 重新精准复刻) ---
# 映射说明: 图中刻度 1=20, 2=40, 3=60, 4=80, 5=100
data = {
    '维度': ['知名度', '健康', '价格', '设计', '产地', '风味', '社交'],

    # 蓝色 (养生极客):
    # 特征: 知名度中等偏上，健康较高，价格适中，设计极低，产地/风味中等
    '养生极客': [70, 80, 60, 35, 60, 65, 50],

    # 橙色 (精致宝妈):
    # 特征: 图形面积最大。知名度满分(5)，设计/产地/风味都接近满分，唯独价格敏感度低
    '精致宝妈': [95, 95, 50, 90, 80, 85, 80],

    # 绿色 (传统拥趸):
    # 特征: 图形面积较小。价格敏感度高(接近4)，其他维度普遍在2-3之间徘徊
    '传统拥趸': [50, 60, 85, 40, 50, 55, 40],

    # 红色 (独居青年):
    # 特征: 价格敏感度极高(接近5)，社交属性较高(接近4)，设计也尚可
    '独居青年': [65, 55, 95, 65, 50, 60, 75]
}

df = pd.DataFrame(data)

# --- 3. 设置绘图参数 ---
categories = list(df['维度'])
N = len(categories)

# 计算角度
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# --- 4. 设置配色 (修改) ---
# 原图颜色顺序显然是: 蓝(Blue), 橙(Orange), 绿(Green), 红(Red)
# tab10 是 matplotlib 默认色板，前四个颜色正好符合这个顺序
colors = sns.color_palette("tab10", n_colors=4)

# --- 5. 初始化绘图 ---
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=300)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# 网格设置
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)
ax.xaxis.grid(True, color='grey', linestyle='--', linewidth=1, alpha=0.5)

# 手动绘制多边形网格线 (0-100分制，对应原图的1-5分)
# 20=1分, 40=2分, 60=3分, 80=4分, 100=5分
grid_levels = [20, 40, 60, 80, 100]

for level in grid_levels:
    grid_values = [level] * len(angles)
    ax.plot(angles, grid_values, color='grey', linestyle='-', linewidth=1, alpha=0.2, zorder=0)

# --- 6. 绘制每一列的数据 ---
labels = list(data.keys())[1:]

for idx, label in enumerate(labels):
    values = df[label].tolist()
    values += values[:1]

    # 绘制线条
    ax.plot(angles, values, color=colors[idx], linewidth=2.5, linestyle='solid', label=label, zorder=10)
    # 填充颜色
    ax.fill(angles, values, color=colors[idx], alpha=0.15, zorder=10)

# --- 7. 添加标签和刻度 ---
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
for label in ax.get_xticklabels():
    label.set_fontproperties(zh_font)
    label.set_fontsize(13)
    label.set_position((0, -0.05))

plt.ylim(0, 105)

# Y轴刻度标签 (为了美观，模拟原图的1-4显示，虽然实际数据是20-80)
ax.set_yticks([20, 40, 60, 80])
ax.set_yticklabels(['1', '2', '3', '4'], color="#666666", size=10, fontfamily='Times New Roman')
ax.yaxis.set_zorder(20)
ax.set_rlabel_position(10)

# --- 8. 图例和标题 ---
legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                    frameon=False, ncol=4, fontsize=12)
for text in legend.get_texts():
    text.set_fontproperties(zh_font)

plt.title("图2-3：四类消费者人群画像雷达图", fontproperties=zh_font, fontsize=16, y=1.15, weight='bold')

# --- 9. 保存 ---
plt.savefig('图2-2.png', dpi=300, bbox_inches='tight')
print("图表已生成：四类人群雷达图_复刻.png")
# plt.show()