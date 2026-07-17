import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
import matplotlib.patches as mpatches

# --- 1. 字体与画布设置 ---
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
try:
    # 优先使用 macOS 的 Songti SC，Windows 可换为 Microsoft YaHei
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# 创建画布
fig, ax1 = plt.subplots(figsize=(12, 8), dpi=300)

# --- 2. 数据准备 (模拟原图趋势) ---
months = np.arange(1, 13)

# LTV: 稳步增长 (模拟线性+轻微指数增长)
ltv = np.array([150, 165, 185, 210, 240, 275, 310, 350, 390, 435, 480, 530])

# CAC: 逐渐下降并趋于稳定 (模拟前期高投放，后期优化)
cac = np.array([118, 109, 95, 85, 78, 72, 68, 65, 62, 60, 58, 55])

# Ratio: 自动计算
ratio = ltv / cac

# --- 3. 绘图 (双轴) ---

# 左轴 (金额: LTV & CAC)
ax1.set_xlabel('运营月份', fontproperties=zh_font, fontsize=14)
ax1.set_ylabel('金额（元）', fontproperties=zh_font, fontsize=14)
ax1.set_ylim(30, 560) # 根据原图设置范围

# 绘制 LTV (绿色实线，圆点)
l1, = ax1.plot(months, ltv, color='#4CAF50', marker='o', markersize=8,
               linewidth=3, label='LTV（用户生命周期价值）')

# 绘制 CAC (红色实线，方块)
l2, = ax1.plot(months, cac, color='#E53935', marker='s', markersize=8,
               linewidth=3, label='CAC（获客成本）')

# 右轴 (比率: LTV/CAC)
ax2 = ax1.twinx() # 共享X轴
ax2.set_ylabel('LTV/CAC比率', fontproperties=zh_font, fontsize=14, color='#F9A825')
ax2.set_ylim(0, 12) # 根据原图设置范围
ax2.tick_params(axis='y', labelcolor='#F9A825')

# 绘制 Ratio (黄色虚线，三角)
l3, = ax2.plot(months, ratio, color='#F9A825', marker='^', markersize=9,
               linewidth=3, linestyle='--', label='LTV/CAC比率')

# --- 4. 辅助线与区域填充 ---

# 绘制健康阈值线 (y=3.0)
threshold_line = ax2.axhline(y=3.0, color='#999999', linestyle='--', linewidth=2, label='健康阈值（3.0）')

# 填充健康区间 (Ratio > 3.0 的部分)
# 使用 fill_between，where 参数控制只填充大于3的部分
ax2.fill_between(months, ratio, 3.0, where=(ratio >= 3.0),
                 interpolate=True, color='#4CAF50', alpha=0.15, label='健康区间')

# --- 5. 图例设置 (合并双轴图例) ---
# 获取两个轴的图例句柄和标签
lines = [l1, l2, l3, threshold_line]
labels = [l.get_label() for l in lines]

# 手动添加"健康区间"的图例块
patch = mpatches.Patch(color='#4CAF50', alpha=0.15, label='健康区间')
lines.append(patch)
labels.append('健康区间')

# 绘制图例
ax1.legend(lines, labels, loc='upper left', prop=zh_font, frameon=True,
           facecolor='white', framealpha=0.9, fontsize=10, borderpad=1)

# --- 6. 其他装饰 ---
ax1.set_title("图9-1：LTV/CAC动态趋势预测图（12个月运营周期）", fontproperties=zh_font, fontsize=18, y=1.02)
ax1.set_xticks(months)
ax1.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('LTV_CAC_Trend_Chart.png', dpi=300, bbox_inches='tight')
print("图片已生成：LTV_CAC_Trend_Chart.png")
# plt.show()