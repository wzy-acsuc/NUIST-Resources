import matplotlib.pyplot as plt

# 1. Mac 系统中文字体配置与 300 DPI 设置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 2. 设置较大的字号 (13 pt)
FONT_SIZE_LARGE = 13

# 3. 准备数据 (源自图片 image_0263a1.png)
# 顺序：从底部往上画
stages = ['曝光', '点击', '加购', '下单', '付款']
counts = ['1,000,000', '50,000', '10,000', '3,000', '2,500']
conv_rates = ['(100%)', '(5%)', '(20%)', '(30%)', '(83%)']
# 绘图宽度：基于转化率百分比进行视觉还原
widths = [100, 5, 20, 30, 83]

# 匹配图片中的马卡龙色系：红、橙、青、蓝、绿
colors = ['#FF6B6B', '#FDD47E', '#71D2CA', '#69BED6', '#A9D1C1']

# 4. 创建画布并设置白色背景
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 5. 绘制水平条形图并使其居中
# 使用 barh 绘制，left 参数设为 (100 - width) / 2 以实现居中效果
y_pos = range(len(stages))
for i in range(len(stages)):
    left = (100 - widths[i]) / 2
    ax.barh(y_pos[i], widths[i], left=left, color=colors[i], height=0.7, zorder=3)

    # 6. 在条形内部添加文本标注 (字号加大)
    label_text = f"{stages[i]}\n{counts[i]}\n{conv_rates[i]}"
    ax.text(50, y_pos[i], label_text, ha='center', va='center',
            fontsize=FONT_SIZE_LARGE - 2, color='white', fontweight='bold')

# 7. 设置坐标轴与标题
ax.set_title('图4-4 流量转化漏斗', fontsize=FONT_SIZE_LARGE + 2, pad=10, fontweight='bold')
ax.set_xlabel('占比 (%)', fontsize=FONT_SIZE_LARGE)
ax.set_xlim(0, 100)
ax.set_xticks([0, 20, 40, 60, 80, 100])
ax.set_yticks([])  # 隐藏 Y 轴刻度，因为名称已在条形内

# 8. 设置黑色边框 (黑框要求)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.2)

# 9. 调整布局并显示
plt.tight_layout()

# 如需保存图片，请取消下行注释
# plt.savefig('图4-4_流量转化漏斗_大字版.png', dpi=300, bbox_inches='tight')

plt.show()