import matplotlib.pyplot as plt
import numpy as np

# 1. Mac 系统中文字体配置与 300 DPI 设置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 定义 5 号字大小 (10.5 pt)
FONT_SIZE = 13

# 2. 准备更新后的数据 (源自图片底部备注)
channels = ['TikTok Shop', 'Shopee', 'Lazada', 'Instagram', 'Facebook']
costs = [3, 5, 4, 6, 8]  # 单位：美元

# 定义颜色序列 (延续之前的清新马卡龙配色)
colors = ['#71D2CA', '#69BED6', '#A9D1C1', '#FDD47E', '#F8858B']

# 3. 创建画布并设置白色背景
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 4. 绘制柱状图
# 设置网格线
ax.grid(axis='y', color='#EEEEEE', linestyle='--', linewidth=0.8, zorder=0)

# 绘制条形，并确保其在网格线之上
bars = ax.bar(channels, costs, color=colors, edgecolor='grey', linewidth=0.5, width=0.6, zorder=100)

# 5. 添加数值标注 (柱子顶部的获客成本)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.2,
            f'{height} 美元', ha='center', va='bottom', fontsize=FONT_SIZE)

# 6. 设置文字和字号
ax.set_title('图4-2 各渠道获客成本对比', fontsize=FONT_SIZE, pad=10)
ax.set_xlabel('营销渠道', fontsize=FONT_SIZE)
ax.set_ylabel('获客成本 (美元)', fontsize=FONT_SIZE)

# 设置坐标轴范围 (留出空间展示标签)
ax.set_ylim(0, 10)

# 设置刻度字体大小
ax.tick_params(axis='both', labelsize=FONT_SIZE)

# --- 修改部分：设置黑色边框 ---
# 将所有脊柱（上下左右边框）设置为可见，并指定颜色为黑色
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1) # 可以调整边框宽度
# ---------------------------

# 7. 调整布局并显示
plt.tight_layout()

# 如需保存图片，请取消下行注释
# plt.savefig('图4-2_各渠道获客成本对比_黑框版.png', dpi=300, bbox_inches='tight')

plt.show()