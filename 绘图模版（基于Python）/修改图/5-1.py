import matplotlib.pyplot as plt

# 1. Mac 系统中文字体配置与 300 DPI 设置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 2. 设置较大的字号 (13 pt)
FONT_SIZE_LARGE = 13

# 3. 准备数据 (源自图片 image_0267c2.png)
departments = ['运营部', '销售部', '内容部', '客服部', '供应链', '财务部']
counts = [4, 3, 2, 3, 2, 1]

# 匹配图片中的马卡龙配色：珊瑚红、青碧、湖蓝、薄荷绿、淡黄、浅紫
colors = ['#FF6B6B', '#57D1C9', '#4DBBDB', '#9AD3BC', '#FDE49C', '#D395D0']

# 4. 创建画布并设置白色背景
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 5. 绘制柱状图
# 设置虚线背景网格 (zorder=0 确保网格在柱子后面)
ax.grid(axis='y', color='#EEEEEE', linestyle='--', linewidth=0.8, zorder=0)

# 绘制条形，添加黑色细边框
bars = ax.bar(departments, counts, color=colors, edgecolor='black',
              linewidth=0.8, width=0.5, zorder=3)

# 6. 添加数值标注 (柱子顶部人数，字号加大)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{int(height)}', ha='center', va='bottom',
            fontsize=FONT_SIZE_LARGE, fontweight='bold')

# 7. 设置标题与轴标签 (字号加大)
ax.set_title('图5-1 团队架构人数分布', fontsize=FONT_SIZE_LARGE + 2, pad=10, fontweight='bold')
ax.set_ylabel('人数', fontsize=FONT_SIZE_LARGE)

# 设置刻度字体大小
ax.tick_params(axis='both', labelsize=FONT_SIZE_LARGE)

# 8. 设置黑色边框 (黑框要求)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.2)

# 设置 Y 轴范围，确保顶部标签不被遮挡
ax.set_ylim(0, 4.5)

# 9. 调整布局并显示
plt.tight_layout()

# 如需保存图片，请取消下行注释
# plt.savefig('图5-1_团队架构人数分布_大字版.png', dpi=300, bbox_inches='tight')

plt.show()