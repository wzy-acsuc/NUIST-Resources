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

# --- 2. 数据准备 (BCG矩阵数据) ---
products = ["完香喷雾油", "完香小瓶装", "完香礼盒装", "完香胡麻油(5L)"]
# X轴: 相对市场份额 (%)
x_vals = [5.0, 10.0, 15.0, 40.0]
# Y轴: 市场增长率 (%)
y_vals = [25.0, 15.0, 8.0, 5.0]
# 气泡大小 (根据图片估算)
sizes = [800, 800, 800, 800]
# 气泡颜色 (对应图片: 红、蓝紫、橙、绿)
colors = ["#FF7F7F", "#7F7FFF", "#FFCC66", "#73B87E"]

# --- 3. 阈值设定 (BCG矩阵的分割线) ---
x_split = 20.0  # 相对市场份额分割线
y_split = 10.0  # 市场增长率分割线

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(9, 9), dpi=300)

# 定义坐标轴显示范围
x_min, x_max = 3, 42
y_min, y_max = 4, 27

# --- 【核心修改】绘制四个象限的背景色 ---
# 根据分割线 x_split=20, y_split=10 进行填充

# 左上 (问题产品: 高增长/低份额) -> 淡红色背景
ax.fill_between([x_min, x_split], y_split, y_max, color='#FFEBEE', alpha=0.6, zorder=0)

# 右上 (明星产品: 高增长/高份额) -> 淡蓝色背景 (图中此区域为空，但为了美观填上)
ax.fill_between([x_split, x_max], y_split, y_max, color='#E3F2FD', alpha=0.6, zorder=0)

# 左下 (瘦狗产品: 低增长/低份额) -> 淡黄色背景
ax.fill_between([x_min, x_split], y_min, y_split, color='#FFF8E1', alpha=0.6, zorder=0)

# 右下 (金牛产品: 低增长/高份额) -> 淡绿色背景
ax.fill_between([x_split, x_max], y_min, y_split, color='#E8F5E9', alpha=0.6, zorder=0)


# --- 绘制散点 ---
# zorder=3 确保气泡在背景之上
ax.scatter(x_vals, y_vals, s=sizes, c=colors, alpha=0.9, zorder=3, edgecolors='white', linewidth=1.5)

# --- 5. 辅助元素 ---

# 绘制虚线分割线 (zorder=2)
ax.axvline(x=x_split, color='gray', linestyle='--', linewidth=1.5, zorder=2)
ax.axhline(y=y_split, color='gray', linestyle='--', linewidth=1.5, zorder=2)

# 添加文字标签
for i, txt in enumerate(products):
    # 文字位置稍微向右偏移
    ax.text(x_vals[i] + 1.2, y_vals[i], txt,
            fontproperties=zh_font, color='#333333',
            ha='left', va='center', fontsize=12, zorder=4)

# --- 6. 坐标轴与标题 ---
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# 设置标题和轴标签
ax.set_title("图 4-1：BCG 产品矩阵", fontproperties=zh_font, fontsize=16, y=1.02)
ax.set_xlabel("相对市场份额 (%)", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("市场增长率 (%)", fontproperties=zh_font, fontsize=12)

# 边框设置 (只保留外框，看起来更整洁)
ax.grid(False) # 关闭默认网格，因为有了背景区分
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(0.8)

plt.tight_layout()
plt.savefig('BCG_Matrix.png', dpi=300, bbox_inches='tight')
print("图表已生成：BCG_Matrix.png (含背景分区)")
# plt.show()