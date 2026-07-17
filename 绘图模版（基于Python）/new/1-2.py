import matplotlib.pyplot as plt
import numpy as np

# 1. 针对 Mac 系统的中文字体配置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
# --- 新增：设置全局显示 DPI ---
plt.rcParams['figure.dpi'] = 300
# 定义 5 号字对应的大小
FONT_SIZE = 10.5

# 2. 准备数据
age_groups = ['18-25岁', '26-35岁', '36-45岁', '46-55岁', '55岁以上']
acceptance_rates = [78, 82, 75, 68, 45]

# 定义颜色（参考原图：粉红、淡橙、淡黄、淡蓝、淡绿）
colors = ['#FFAAAA', '#FFC388', '#FFD888', '#ADD6FF', '#AAFFAA']

# 3. 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 设置背景颜色和网格
ax.set_facecolor('#EAEAF2')
ax.grid(color='white', linestyle='-', linewidth=0.6, alpha=0)

# 4. 绘制柱状图
# edgecolor='grey' 和 linewidth 为柱子添加细微边框，更接近原图效果
bars = ax.bar(age_groups, acceptance_rates, color=colors, edgecolor='grey', linewidth=0.5, width=0.45)

# 5. 添加数值标注 (柱子顶部的百分比)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height}%', ha='center', va='bottom', fontsize=FONT_SIZE)

# 6. 设置文字和字号
ax.set_title('图1-2 不同年龄段对传统文化数字化接受度调研', fontsize=FONT_SIZE, pad=10)
ax.set_xlabel('年龄段', fontsize=FONT_SIZE)
ax.set_ylabel('接受度 (%)', fontsize=FONT_SIZE)

# 设置坐标轴范围
ax.set_ylim(0, 100)

# 设置刻度字体大小
ax.tick_params(axis='both', labelsize=FONT_SIZE)

# 移除多余边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 7. 调整布局并显示
plt.tight_layout()
plt.show()