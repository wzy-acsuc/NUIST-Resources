import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- 1. 字体配置 (保持不变) ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# --- 2. 数据准备 (替换为 SERVQUAL IPA 数据) ---
# 根据 image_f4e099.png 估算的坐标
products = ["可靠性", "保证性", "有形性", "响应性", "移情性"]

# X轴: 实际感知 (Performance)
x_vals = [3.05, 2.82, 2.78, 2.53, 2.61]

# Y轴: 期望程度 (Importance/Expectation)
y_vals = [4.65, 4.56, 4.48, 4.46, 4.25]

# 气泡大小 (保持统一，稍微调小一点适配密集区域)
sizes = [600, 600, 600, 600, 600]

# 气泡颜色 (原代码只有4色，补一个紫色以适配5个点)
colors = ["#FF7F7F", "#7F7FFF", "#FFCC66", "#73B87E", "#B39DDB"]

# --- 3. 阈值设定 (IPA 矩阵的分割线) ---
# 根据图片观测：X轴分割线约在 2.75，Y轴分割线约在 4.48
x_split = 2.75
y_split = 4.48

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(9, 9), dpi=300)

# 定义坐标轴显示范围 (根据数据分布调整)
x_min, x_max = 2.4, 3.2
y_min, y_max = 4.2, 4.7

# --- 绘制四个象限的背景色 ---
# 逻辑映射：
# 左上 (高期望/低感知) -> 重点改进区 (红色背景)
ax.fill_between([x_min, x_split], y_split, y_max, color='#FFEBEE', alpha=0.6, zorder=0)

# 右上 (高期望/高感知) -> 继续保持区 (蓝色背景)
ax.fill_between([x_split, x_max], y_split, y_max, color='#E3F2FD', alpha=0.6, zorder=0)

# 左下 (低期望/低感知) -> 低优先级区 (黄色背景)
ax.fill_between([x_min, x_split], y_min, y_split, color='#FFF8E1', alpha=0.6, zorder=0)

# 右下 (低期望/高感知) -> 供给过度区 (绿色背景)
ax.fill_between([x_split, x_max], y_min, y_split, color='#E8F5E9', alpha=0.6, zorder=0)

# --- 绘制散点 ---
ax.scatter(x_vals, y_vals, s=sizes, c=colors, alpha=0.9, zorder=3, edgecolors='white', linewidth=1.5)

# --- 5. 辅助元素 ---

# 绘制虚线分割线
ax.axvline(x=x_split, color='gray', linestyle='--', linewidth=1.5, zorder=2)
ax.axhline(y=y_split, color='gray', linestyle='--', linewidth=1.5, zorder=2)

# 添加文字标签
for i, txt in enumerate(products):
    # 【注意】因为坐标数值很小，偏移量从原来的 1.2 改为 0.03，否则文字会飞出图外
    # 并根据点的位置微调：将文字统一放在点的上方或右侧
    offset_x = 0.03
    offset_y = 0.01

    # 特殊处理：有形性和响应性离线很近，微调位置避免遮挡
    if txt == "有形性":
        offset_y = 0.02

    ax.text(x_vals[i] + offset_x, y_vals[i] + offset_y, txt,
            fontproperties=zh_font, color='#333333',
            ha='left', va='center', fontsize=12, zorder=4)

# --- 6. 坐标轴与标题 ---
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# 设置标题和轴标签 (根据图片 image_f4e099.png 修改)
ax.set_title("图 8-2：SERVQUAL IPA 象限图", fontproperties=zh_font, fontsize=16, y=1.02)
ax.set_xlabel("实际感知 (Performance)", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("期望程度 (Importance/Expectation)", fontproperties=zh_font, fontsize=12)

# 边框设置
ax.grid(False)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(0.8)

plt.tight_layout()
plt.savefig('图8-2.png', dpi=300, bbox_inches='tight')
print("图表已生成：SERVQUAL_IPA_Chart.png (保留原格式设置)")
# plt.show()