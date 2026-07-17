import matplotlib.pyplot as plt
import numpy as np

# 1. Mac 系统中文字体配置与 300 DPI 设置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 定义 5 号字大小 (10.5 pt)
FONT_SIZE = 10.5

# 2. 准备数据 (根据文本分析内容)
# 文本提及：天猫(82%)，淘宝(75%)，小红书(72%)，抖音电商(68%)
platforms = ['天猫', '淘宝', '小红书', '抖音电商']
preference_rates = [82, 75, 72, 68]

# 定义颜色序列 (延续之前的清新马卡龙配色)
colors = ['#F8858B', '#71D2CA', '#FDD47E', '#69BED6']

# 3. 创建画布
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# 设置背景颜色和网格
ax.set_facecolor('#EAEAF2')
ax.grid(color='white', linestyle='-', linewidth=0.6, alpha=0)

# 4. 绘制柱状图
# 设置宽度为 0.65 使图表比例协调
bars = ax.bar(platforms, preference_rates, color=colors, edgecolor='grey', linewidth=0.5, width=0.4)

# 5. 添加数值标注 (柱子顶部的偏好度百分比)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1.5,
            f'{int(height)}%', ha='center', va='bottom', fontsize=FONT_SIZE)

# 6. 设置文字和字号
ax.set_title('图1-5 消费者电商平台选择偏好', fontsize=FONT_SIZE, pad=10)
ax.set_xlabel('电商平台', fontsize=FONT_SIZE)
ax.set_ylabel('偏好度 (%)', fontsize=FONT_SIZE)

# 设置坐标轴范围
ax.set_ylim(0, 100)

# 设置刻度字体大小
ax.tick_params(axis='both', labelsize=FONT_SIZE)

# 移除多余边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 7. 调整布局并显示
plt.tight_layout()

# 如需保存图片，请取消下行注释
# plt.savefig('图1-5_消费者电商平台偏好.png', dpi=300, bbox_inches='tight')

plt.show()