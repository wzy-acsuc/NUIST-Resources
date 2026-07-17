import matplotlib.pyplot as plt
import numpy as np

# --- 1. 数据准备 (基于 image_56574a.png 提取) ---
# 注意：barh 是从下往上画的，为了让 "WiFi Mixed" 在最上面，
# 我们将数据按从小到大排列（或者按原图的从下到上顺序）
labels = [
    'News+Music (0.5h, 5G)',
    'Genshin (1h, 5G)',
    'MOBA (1.5h, 5G)',
    'WiFi Mixed (3h)'
]

# 对应的电流贡献值 (mA)
values = [88, 246, 342, 392]

# --- 2. 颜色定制 (蓝色系渐变) ---
# 逻辑：数值越小颜色越浅，数值越大颜色越深 (Deep Blue)
colors = [
    '#87CEFA', # News+Music (最浅)
    '#5DADE2', # Genshin
    '#2E86C1', # MOBA
    '#154360'  # WiFi Mixed (最深)
]

# --- 3. 字体与绘图设置 ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(7.5, 4), dpi=300)

# --- 4. 绘图 ---
# 保持 height=0.45 让柱子纤细
bars = ax.barh(labels, values, color=colors, height=0.45, edgecolor='none')

# --- 5. 细节美化 ---
# 垂直网格线 (仅X轴)
ax.grid(axis='x', linestyle=':', alpha=0.5, color='gray', zorder=0)
ax.set_axisbelow(True)

# 移除多余边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#555555') # 左轴保留一点颜色区分标签
ax.spines['bottom'].set_color('#555555')

# 设置轴标签
ax.set_xlabel('Average Contribution to Equivalent Current (mA)', fontsize=12, color='#333333', labelpad=10)
ax.set_ylabel('Activity Segment', fontsize=12, color='#333333', labelpad=10)

# 调整刻度字体
ax.tick_params(axis='y', labelsize=11, colors='#222222')
ax.tick_params(axis='x', labelsize=11, colors='#333333')

# 设置X轴范围 (让右侧稍微留白)
ax.set_xlim(0, 420)

# 紧凑布局
plt.tight_layout()

# 保存
plt.savefig('Driver_Attribution_Blue.png', bbox_inches='tight')
plt.show()