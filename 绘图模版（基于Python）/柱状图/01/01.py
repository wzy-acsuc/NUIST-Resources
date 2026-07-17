import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns  # 引入 seaborn 获取好看的配色

# 1. 准备数据 (来源于你的 Excel 截图)
labels = ['MACD', 'KDJ', 'Wzy']
short_data = [20000, 60000, 20000]
middle_data = [25000, 30000, 20000]
long_data = [30000, 32000, 20000]

OUTPUT_PDF = '01.pdf'
OUTPUT_PNG = '01.png'
# 2. 设置全局字体和风格
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

# 3. 创建画布
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)

# 4. 定义柱状图参数 【修改点：拆分位置和宽度】
x = np.arange(len(labels))
offset = 0.22     # 【偏移量】：决定柱子中心的位置（也就是柱子之间的中心距离）
bar_width = 0.16  # 【实际宽度】：比偏移量小 (0.17 < 0.22)，就能产生空隙

# 方法一：颜色自定义
# color_short = '#BFD9F2'  # 浅蓝
# color_middle = '#8FAADC' # 中蓝
# color_long = '#1F4E79'   # 深蓝

# 方法二：使用模版颜色
palette = sns.color_palette("flare", 3)  # 获取 mako 色盘的 3 个颜色，mako 默认顺序是：深色 -> 浅色
# 按照原图逻辑分配颜色：
color_long = palette[0]
color_middle = palette[1]
color_short = palette[2]
# 如果想要其他风格，可以尝试替换 "mako" 为：
# "viridis" (蓝绿黄), "rocket" (深红), "flare" (红橙), "crest" (另一种蓝绿)

# 5. 绘制柱子
# 注意：位置使用 offset 计算，宽度使用 bar_width
rects1 = ax.bar(x - offset, short_data, bar_width, label='Short', color=color_short, zorder=3)
rects2 = ax.bar(x, middle_data, bar_width, label='Middle', color=color_middle, zorder=3)
rects3 = ax.bar(x + offset, long_data, bar_width, label='Long', color=color_long, zorder=3)

# 6. 定制坐标轴样式
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

ax.set_ylim(0, 70000)
ax.set_yticks(np.arange(0, 70001, 10000))
# 【新增】提高坐标轴层级，防止被柱子遮挡
ax.spines['left'].set_zorder(10)
ax.spines['bottom'].set_zorder(10)

# 添加箭头
ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, markersize=8, zorder=11)
ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, markersize=8, zorder=11)

# 7. 设置标签和文字
ax.set_xticks(x)
ax.set_xticklabels(labels, fontweight='bold', fontsize=12)

ax.tick_params(axis='y', labelsize=11)
for label in ax.get_yticklabels():
    label.set_fontweight('bold')

# Y轴标题
ax.set_ylabel('$W_{total}$', fontweight='bold', fontsize=12)

# 8. 图例设置
legend = ax.legend(
    loc='upper left',           # 大致位置：左上角
    frameon=False,              # 去掉图例周围的方框边框（看起来更干净）
    fontsize=11,                # 字体大小
    bbox_to_anchor=(0.02, 0.98),# 【微调位置】：基于 loc='upper left' 的精确偏移。
                                # (0.02, 0.98) 意思是距离左边 2%，距离底部 98% 的位置。
    handlelength=1.2,           # 图例里那个彩色小色块的长度（默认比较长，改短点好看）
    handleheight=0.7            # 图例里那个彩色小色块的高度
)

# 循环遍历图例中的文字（Short, Middle, Long），把它们全部加粗
for text in legend.get_texts():
    text.set_fontweight('bold')

# 自动调整子图参数，使之填充整个图像区域，防止标签被切掉
plt.tight_layout()
plt.savefig(OUTPUT_PDF, format='pdf')
plt.savefig(OUTPUT_PNG, dpi=300)
# 渲染显示
plt.show()