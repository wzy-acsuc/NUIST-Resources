import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# --- 1. 数据准备 (基于原图数据估算) ---
# 变量名 (从下到上)
variables = [
    'bright_mul', 'net_mul', 'w_genshin', 'cpu_mul',
    'T_env', 'w_moba', 'lbg', 'w_news', 'SOH', 'w_wifi'
]
# 相关性数值
values = [-0.86, -0.22, -0.21, -0.17, -0.16, -0.13, -0.05, 0.01, 0.19, 0.27]

# --- 2. 颜色生成逻辑 (核心修改) ---
# 要求：不同柱子不同颜色，但基本为蓝色。
# 我们使用 Matplotlib 的颜色映射，从不同的蓝色系中取样，混合 teal (蓝绿) 和 blue (纯蓝)
# 这样能保证每根柱子颜色都不一样，但整体看起来很协调。

# 创建一个颜色列表
# 负值部分用偏深邃的蓝绿色/海蓝色，正值部分用明亮的蓝色
colors = [
    '#104e8b', # bright_mul (深钢蓝)
    '#1c6ca1', # net_mul
    '#2887b7', # w_genshin
    '#3aa2cd', # cpu_mul
    '#56bde3', # T_env
    '#7ad7f0', # w_moba (浅蓝)
    '#8beeff', # lbg
    '#5DADE2', # w_news (稍微换个色调区分正负界限)
    '#2E86C1', # SOH
    '#1B4F72'  # w_wifi (深蓝)
]

# 或者，为了更平滑的“不同蓝色”，我们可以使用 colormap 自动生成：
# import matplotlib.cm as cm
# colors = cm.GnBu(np.linspace(0.4, 1, len(values))) # 备用方案

# --- 3. 绘图设置 ---
plt.rcParams['font.sans-serif'] = ['Arial', 'SimHei'] # 优先使用 Arial 显示英文
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(9, 5), dpi=300)

# 绘制水平条形图
bars = ax.barh(variables, values, color=colors, height=0.75, edgecolor='none')

# --- 4. 细节美化 ---
# 添加 0 刻度线 (基准线)
ax.axvline(x=0, color='#34495e', linewidth=1.5, zorder=3)

# 设置背景网格 (仅X轴)
ax.grid(axis='x', linestyle='--', alpha=0.4, color='gray', zorder=0)
ax.set_axisbelow(True)

# 移除顶部和右侧的脊柱 (Spines)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# 左侧和底部脊柱颜色淡化
ax.spines['left'].set_color('#888888')
ax.spines['bottom'].set_color('#888888')

# 设置轴标签
ax.set_xlabel('Spearman correlation with TTE', fontsize=12, color='#333333', labelpad=10)

# 调整刻度字体大小
ax.tick_params(axis='y', labelsize=11, colors='#333333')
ax.tick_params(axis='x', labelsize=10, colors='#333333')

# 调整X轴范围，留出一点空间
ax.set_xlim(-0.95, 0.35)

# --- 5. 确保没有标题 ---
# ax.set_title(...)  <-- 已注释掉

plt.tight_layout()

# 保存或显示
plt.savefig('Blue_Sensitivity_Chart.png', bbox_inches='tight')
plt.show()