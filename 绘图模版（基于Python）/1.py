import matplotlib.pyplot as plt
import numpy as np

# --- 1. 数据准备 ---
labels = [
    'Temperature (25→45°C)',
    'Background current (0→150 mA)',
    'CPU/GPU load (1.0→1.3)',
    'Aging SOH (1.0→0.85)',
    'Weak signal (1.0→1.4)',
    'Brightness (1.0→1.5)'
]

# 对应的 ΔTTE 值
values = [-0.73, -0.80, -0.98, -1.00, -1.38, -3.92]

# --- 2. 颜色定制 (蓝色系渐变) ---
colors = [
    '#87CEFA', # Temperature (最浅)
    '#5DADE2',
    '#3498DB',
    '#2980B9',
    '#1F618D',
    '#154360'  # Brightness (最深)
]

# --- 3. 字体与绘图设置 ---
# 【修改点1】设置字体为 Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(8, 4), dpi=300)

# --- 4. 绘图 ---
# 【修改点2】height=0.45 (原为0.7)，让柱子变细
bars = ax.barh(labels, values, color=colors, height=0.45, edgecolor='none')

# --- 5. 细节美化 ---
# 0刻度线
ax.axvline(x=0, color='#333333', linewidth=1.5, zorder=3)

# 背景网格 (仅X轴)
ax.grid(axis='x', linestyle=':', alpha=0.5, color='gray', zorder=0)
ax.set_axisbelow(True)

# 移除多余边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#555555')

# 设置轴标签
ax.set_xlabel('ΔTTE (hours) relative to baseline', fontsize=12, color='#333333', labelpad=10)

# 调整刻度字体
ax.tick_params(axis='y', labelsize=11, colors='#222222', length=0)
ax.tick_params(axis='x', labelsize=11, colors='#333333')

# 还原右下角的文字标注
ax.text(0.99, 0.01, 'Baseline: TTE=6.70h, Q=7355mAh (median), n=30',
        transform=ax.transAxes, ha='right', va='bottom',
        fontsize=10, color='#555555', alpha=0.9)

# 设置X轴范围
ax.set_xlim(-4.2, 0.1)

# 紧凑布局
plt.tight_layout()

# 保存
plt.savefig('Battery_Life_Impact_TimesNewRoman.png', bbox_inches='tight')
plt.show()