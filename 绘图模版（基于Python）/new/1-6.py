import matplotlib.pyplot as plt
import numpy as np

# 1. Mac 系统中文字体配置与 300 DPI 设置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 定义 5 号字大小 (10.5 pt)
FONT_SIZE = 10.5

# 2. 准备数据 (根据文本分析模拟价值评分/权重)
# 传统工艺价值（核心）、文化内涵价值（独特资产）、品质保障体系（基础支撑）
values = ['品质保障体系', '文化内涵价值', '传统工艺价值']
scores = [88, 92, 98]  # 模拟品牌价值评分，工艺价值作为核心竞争力设定最高分

# 定义颜色序列 (延续之前的清新马卡龙配色：珊瑚红、青碧、暖黄)
colors = ['#FDD47E', '#71D2CA', '#F8858B']

# 3. 创建画布
fig, ax = plt.subplots(figsize=(7, 4), dpi=300)

# 设置背景颜色和网格
ax.set_facecolor('#EAEAF2')
ax.grid(color='white', linestyle='-', linewidth=0.6, alpha=0, axis='x')

# 4. 绘制横向柱状图
# height 设置为 0.6 使条形看起来不那么臃肿
bars = ax.barh(values, scores, color=colors, edgecolor='grey', linewidth=0.5, height=0.4)

# 5. 添加数值标注 (条形末端的价值指数)
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{int(width)}', ha='left', va='center', fontsize=FONT_SIZE)

# 6. 设置文字和字号
ax.set_title('图1-6 弗氏香铺品牌价值分析', fontsize=FONT_SIZE, pad=10)
ax.set_xlabel('价值维度评价指数', fontsize=FONT_SIZE)
# 移除纵轴标签，因为条形旁边已经有类别名了
ax.set_ylabel('', fontsize=FONT_SIZE)

# 设置坐标轴范围 (留出右侧空间展示标签)
ax.set_xlim(0, 110)

# 设置刻度字体大小
ax.tick_params(axis='both', labelsize=FONT_SIZE)

# 移除多余边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 7. 调整布局并显示
plt.tight_layout()

# 如需保存图片，请取消下行注释
# plt.savefig('图1-6_弗氏香铺品牌价值分析.png', dpi=300, bbox_inches='tight')

plt.show()