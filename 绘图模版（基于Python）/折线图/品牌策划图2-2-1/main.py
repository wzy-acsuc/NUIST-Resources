import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import font_manager

# --- 1. 字体与画布设置 ---

# 设置全局西文字体为 Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

# 设置中文字体
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    try:
        zh_font = font_manager.FontProperties(family='SimSun', size=12)
    except:
        zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)

# --- 2. 数据准备 (根据图片估算) ---
k = np.arange(1, 11)
# 估算的 WCSS 值，模拟手肘形状
wcss = np.array([3500, 2500, 2200, 2020, 1860, 1780, 1700, 1650, 1570, 1530])

# --- 3. 绘图 ---

# 使用 Seaborn 的默认蓝色，或您可以换成 'viridis' 等模版颜色的第一个颜色
# 这里的 line_color 对应图中经典的蓝色
line_color = sns.color_palette('tab10')[0]

# 绘制折线图 (虚线 + 圆点)
ax.plot(k, wcss, color=line_color, marker='o', markersize=8,
        linestyle='--', linewidth=2, label='WCSS')

# --- 4. 标注与细节 (核心复刻) ---

# 添加箭头和文字标注 (指向 k=4)
ax.annotate('最佳聚类点 k=4',
            xy=(4, 2020),            # 箭头指向的点 (数据坐标)
            xytext=(5, 2400),        # 文字放置的位置 (数据坐标)
            arrowprops=dict(facecolor='black', shrink=0.05, width=2, headwidth=10),
            fontproperties=zh_font, fontsize=13)

# --- 5. 坐标轴与标题设置 ---

# 设置标题
ax.set_title("图 2-2-1：K-Means 聚类手肘法分析图", fontproperties=zh_font, size=16, y=1.02)

# 设置坐标轴标签
ax.set_xlabel("聚类数量 (k)", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("WCSS (组内平方和)", fontproperties=zh_font, fontsize=12)

# 设置刻度字体
ax.tick_params(axis='both', labelsize=12)
ax.set_xticks(np.arange(2, 11, 2)) # 设置X轴刻度 2, 4, 6, 8, 10

# 网格线 (保留全网格以匹配原图)
ax.grid(True, linestyle='-', alpha=0.6)

# (可选) 如果希望像之前的图一样去掉顶部和右侧边框，解开下面两行注释
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('Elbow_Method_Chart.png', dpi=300, bbox_inches='tight')
print("图表已生成：Elbow_Method_Chart.png")
# plt.show()