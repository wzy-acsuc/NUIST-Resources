import matplotlib.pyplot as plt
import numpy as np

# 1. Mac 系统中文字体配置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
# --- 新增：设置全局显示 DPI ---
plt.rcParams['figure.dpi'] = 300
# 定义 5 号字大小 (10.5 pt)
FONT_SIZE = 10.5

# 2. 准备数据 (根据新的文本分析修改)
# 文本明确提及：茉莉花(85)，檀香(80)，沉香(65)
# 文本提及有基础但未给数值：薰衣草，柠檬草 (设定较低数值以符合描述)
scents = ['檀香', '茉莉花', '沉香', '薰衣草', '柠檬草']
preference_index = [80, 85, 65, 55, 48]

# 定义颜色序列 (重新挑选5种清新配色)
colors = ['#71D2CA', '#F8858B', '#A9D1C1', '#69BED6', '#FDD47E']

# 3. 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 设置背景颜色和网格
ax.set_facecolor('#EAEAF2')
ax.grid(color='white', linestyle='-', linewidth=0.6, alpha=0)

# 4. 绘制柱状图
# 添加细微的灰色边框以增加精致感
bars = ax.bar(scents, preference_index, color=colors, edgecolor='grey', linewidth=0.5, width=0.45)

# 5. 添加数值标注 (柱子顶部的偏好指数)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{int(height)}', ha='center', va='bottom', fontsize=FONT_SIZE)

# 6. 设置文字和字号
ax.set_title('图1-4 东南亚消费者香料偏好调研', fontsize=FONT_SIZE, pad=10)
ax.set_xlabel('香料类型', fontsize=FONT_SIZE)
ax.set_ylabel('偏好指数', fontsize=FONT_SIZE)

# 设置坐标轴范围 (留出顶部空间)
ax.set_ylim(0, 100)

# 设置刻度字体大小
ax.tick_params(axis='both', labelsize=FONT_SIZE)

# 移除多余边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 7. 调整布局并显示
plt.tight_layout()
plt.show()