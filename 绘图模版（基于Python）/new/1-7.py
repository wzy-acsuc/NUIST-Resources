import matplotlib.pyplot as plt
import numpy as np

# 1. Mac 系统中文字体配置与 300 DPI 设置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 定义 5 号字大小 (10.5 pt)
FONT_SIZE = 10.5

# 2. 准备数据
labels = np.array(['年龄适配度', '收入水平', '生活品质追求',
                   '文化认同感', '品牌故事关注度', '品质优先度'])
stats = np.array([90, 85, 92, 96, 88, 95])

# 3. 数据闭环处理
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))

# 4. 创建极坐标画布
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True), dpi=300)
# --- 修改背景为白色 ---
fig.patch.set_facecolor('white') # 设置整个画布边缘为白色
ax.set_facecolor('white')        # 设置雷达图内部区域为白色
# ----------------------

# 5. 绘制雷达图
main_color = '#71D2CA'
ax.plot(angles, stats, 'o-', linewidth=2, color=main_color, markersize=6)
ax.fill(angles, stats, alpha=0.35, color=main_color)

# 6. 设置刻度和标签
# 设置维度名称 (去掉了之前闭环处理带来的标签重复)
ax.set_thetagrids(angles[:-1] * 180/np.pi, labels, fontsize=FONT_SIZE, color='#555555')
ax.tick_params(pad=15)

# 修正：plt.yticks 仅设置文字属性
ax.set_ylim(0, 100)
plt.yticks([20, 40, 60, 80, 100], ['20', '40', '60', '80', '100'],
           color='#888888', size=FONT_SIZE)

# 修正：将线型属性统一在 grid 中设置
ax.grid(True, color='#BBBBBB', linestyle='--', linewidth=0.8)

# 移除外圈圆框
ax.spines['polar'].set_visible(False)

# 7. 设置标题
ax.set_title('图1-7 目标客群画像分析 (核心群体)', fontsize=FONT_SIZE, pad=30, color='#333333')

# 8. 调整布局并显示
plt.tight_layout()
plt.show()