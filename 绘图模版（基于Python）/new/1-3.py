import matplotlib.pyplot as plt
import numpy as np

# 1. Mac 系统中文字体配置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
# --- 新增：设置全局显示 DPI ---
plt.rcParams['figure.dpi'] = 300
# 定义 5 号字大小
FONT_SIZE = 10.5

# 2. 准备数据 (基于文字描述进行模拟估算)
years = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027']
# 市场规模 (亿元) - 严格遵循 16% 复合增长及关键年份节点
market_size = [320, 371, 431, 500, 580, 696, 835, 1000]
# 电商渠道占比 (%) - 严格遵循 2020(18%) -> 2024(35%) -> 2028(52%) 的趋势
ecommerce_rate = [18, 22, 26, 31, 35, 39, 44, 48]

# 3. 创建画布
fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.set_facecolor('#F7F7F9') # 浅灰色背景

# 4. 绘制柱状图 (市场规模)
color_bar = '#FF9999' # 浅珊瑚红
bars = ax1.bar(years, market_size, color=color_bar, alpha=0.8, label='市场规模 (亿元)', width=0.6)

# 5. 绘制折线图 (双坐标轴 - 电商占比)
ax2 = ax1.twinx()
color_line = '#4C72B0' # 深蓝色
line = ax2.plot(years, ecommerce_rate, color=color_line, marker='o', linewidth=2, label='电商渠道占比 (%)')

# 6. 添加数值标注
# 柱状图标注
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 10, f'{int(height)}',
             ha='center', va='bottom', fontsize=FONT_SIZE)

# 折线图标注
for i, txt in enumerate(ecommerce_rate):
    ax2.annotate(f'{txt}%', (years[i], ecommerce_rate[i]), textcoords="offset points",
                 xytext=(0,10), ha='center', fontsize=FONT_SIZE, color=color_line)

# 7. 设置标题和轴标签
ax1.set_title('图1-3 中国香薰产品市场规模趋势', fontsize=FONT_SIZE, pad=10)
ax1.set_xlabel('年份', fontsize=FONT_SIZE)
ax1.set_ylabel('市场规模 (亿元)', fontsize=FONT_SIZE)
ax2.set_ylabel('电商渠道占比 (%)', fontsize=FONT_SIZE)

# 设置刻度大小
ax1.tick_params(axis='both', labelsize=FONT_SIZE)
ax2.tick_params(axis='both', labelsize=FONT_SIZE)

# 设置坐标轴范围
ax1.set_ylim(0, 1201)
ax2.set_ylim(0, 51)

# 合并图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=FONT_SIZE)

# 移除冗余边框
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()