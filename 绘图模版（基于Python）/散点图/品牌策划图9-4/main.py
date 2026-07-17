import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- 1. 字体配置 ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# --- 2. 数据准备 (根据 image_f4d96f.png 复刻) ---
risks = [
    "公关舆情风险",
    "市场竞争加剧",
    "执行进度滞后",
    "原材料价格波动",
    "品牌焕新认知偏差"
]

# X轴: 发生概率 (Probability)
x_vals = [2.0, 3.0, 2.0, 4.0, 4.0]

# Y轴: 影响程度 (Impact)
y_vals = [5.0, 4.0, 3.0, 3.0, 2.0]

# 气泡颜色 (对应图片: 紫、蓝、红、橙、绿)
# 使用 Matplotlib 的标准 tab 颜色
colors = ["#9467BD", "#1F77B4", "#D62728", "#FF7F0E", "#2CA02C"]

# 气泡大小
sizes = [500, 500, 500, 500, 500]

# --- 3. 阈值设定 (风险矩阵分割线) ---
x_split = 3.0
y_split = 3.0

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(8, 6.5), dpi=300)

# 定义坐标轴显示范围 (0 到 6)
limit_min, limit_max = 0, 6

# --- (可选) 绘制象限背景色 ---
# 原图是白底网格，所以我注释掉了背景色。
# 如果您想要之前的彩色象限风格，请取消下面几行的注释：

ax.fill_between([limit_min, x_split], y_split, limit_max, color='#FFF8E1', alpha=0.4) # 左上
ax.fill_between([x_split, limit_max], y_split, limit_max, color='#FFEBEE', alpha=0.4) # 右上(高风险)
ax.fill_between([limit_min, x_split], limit_min, y_split, color='#E8F5E9', alpha=0.4) # 左下(低风险)
ax.fill_between([x_split, limit_max], limit_min, y_split, color='#FFF8E1', alpha=0.4) # 右下

# --- 绘制散点 ---
ax.scatter(x_vals, y_vals, s=sizes, c=colors, alpha=0.9, zorder=3, edgecolors='white', linewidth=1.5)

# --- 5. 辅助元素 ---

# 绘制虚线分割线
ax.axvline(x=x_split, color='gray', linestyle='--', linewidth=1.5, zorder=2)
ax.axhline(y=y_split, color='gray', linestyle='--', linewidth=1.5, zorder=2)

# 添加文字标签
for i, txt in enumerate(risks):
    # 文字位置：在气泡上方居中
    offset_y = 0.25
    ax.text(x_vals[i], y_vals[i] + offset_y, txt,
            fontproperties=zh_font, color='#333333',
            ha='center', va='center', fontsize=11, zorder=4)

# --- 6. 坐标轴与标题 ---
ax.set_xlim(limit_min, limit_max)
ax.set_ylim(limit_min, limit_max)

# 设置标题和轴标签
ax.set_title("项目风险评估矩阵 (影响程度 vs 发生概率)", fontproperties=zh_font, fontsize=14, y=1.02)
ax.set_xlabel("发生概率", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("影响程度", fontproperties=zh_font, fontsize=12)

# 开启网格 (原图有网格)
ax.grid(True, linestyle='-', alpha=0.3, color='lightgray', zorder=0)

# 边框设置
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(0.8)

plt.tight_layout()
plt.savefig('图9-4.png', dpi=300, bbox_inches='tight')
print("图表已生成：Risk_Matrix_Chart.png")
#plt.show()