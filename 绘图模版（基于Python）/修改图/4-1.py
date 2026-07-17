import matplotlib.pyplot as plt

# 1. Mac 系统中文字体配置与 300 DPI 设置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 定义 5 号字大小 (10.5 pt)
FONT_SIZE = 13

# 2. 准备更新后的数据 (源自图片底部文字要求)
labels = ['TikTok Shop', 'Shopee & Lazada', '独立站 & Brand.com']
sizes = [45.0, 40.0, 15.0]

# 延续之前的马卡龙配色方案
# 珊瑚红 (TikTok)、青碧 (Shopee)、湖蓝 (独立站)
colors = ['#FF858B', '#71D2CA', '#69BED6']

# 3. 创建画布并设置白色背景
fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 4. 绘制饼图
# explode 设置为 (0.05, 0, 0) 使占比最大的 TikTok Shop 稍微分离，增加视觉重点
explode = (0.05, 0, 0)

patches, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    shadow=False,
    startangle=140, # 调整起始角度使构图更美观
    textprops={'fontsize': FONT_SIZE}
)

# 5. 设置标题
ax.set_title('图4-1 各渠道销售占比', fontsize=FONT_SIZE, pad=0)

# 确保饼图是正圆形
ax.axis('equal')

# 6. 调整布局并显示
plt.tight_layout()

# 如需保存图片，请取消下行注释
# plt.savefig('图4-1_各渠道销售占比_修正版.png', dpi=300, bbox_inches='tight')

plt.show()