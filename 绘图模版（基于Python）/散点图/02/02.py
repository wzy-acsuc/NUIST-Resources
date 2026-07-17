import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib.patches as patches
import seaborn as sns  # 用于生成配色
import numpy as np

# --- 1. 字体配置 (Mac M4 专用) ---
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.unicode_minus'] = False

# 自动寻找 Mac 宋体
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    print("未找到 Songti SC，尝试使用 STSong...")
    zh_font = font_manager.FontProperties(family='STSong', size=12)

# --- 2. 自动生成颜色 (Flare 主题) ---
# 使用 seaborn 生成 6 种颜色，flare 是从浅金到深紫的渐变
# as_cmap=False 表示生成离散的颜色列表
try:
    # 这一步自动生成颜色
    palette = sns.color_palette("flare", n_colors=6)
except ImportError:
    # 如果没有安装 seaborn，提供一组类似的备用颜色
    print("未检测到 seaborn，使用备用颜色")
    palette = ["#eeccb3", "#e6a19f", "#d67895", "#b75691", "#8d3b88", "#5d277b"]

# --- 3. 数据准备 ---
# 我们把颜色分配逻辑放进数据里
# 注意：为了视觉好看，我们可以根据"权重大小"或者"顺序"来分配颜色深浅
# 这里我们按列表顺序分配

data = [
    # 1. 健康养生 (权重最大)
    {"label": "健康、养生", "x": -5, "y": 6, "size": 2800, "id": "1"},
    # 2. 美容护肤
    {"label": "美容、护肤", "x": 2, "y": 7, "size": 1800, "id": "2"},
    # 3. 性价比
    {"label": "价格、实惠", "x": -7, "y": -2, "size": 1500, "id": "3"},
    # 4. 烹饪体验
    {"label": "口感、凉拌", "x": 5, "y": -1, "size": 1400, "id": "4"},
    # 5. 宿舍方便
    {"label": "宿舍、方便", "x": 6, "y": -5, "size": 1200, "id": "6"},
    # 6. 送礼场景
    {"label": "送礼、健康礼", "x": 1, "y": -7, "size": 1000, "id": "5"}
]

# 提取绘图数据
x_vals = [item['x'] for item in data]
y_vals = [item['y'] for item in data]
sizes = [item['size'] for item in data]
labels = [item['label'] for item in data]

# 将生成的 flare 颜色分配给数据 (反转一下，让大的气泡颜色深一点，或者保持默认)
# palette 得到的是 RGB 元组，Matplotlib 可以直接用
colors = palette

# --- 4. 绘图设置 ---
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# --- 5. 绘制象限背景 (增加层次感) ---
# 使用极淡的冷暖色区分
ax.add_patch(patches.Rectangle((-10, 0), 10, 10, color='#FFF8F0', alpha=0.3))  # 左上
ax.add_patch(patches.Rectangle((0, 0), 10, 10, color='#F0FFF0', alpha=0.3))  # 右上
ax.add_patch(patches.Rectangle((-10, -10), 10, 10, color='#F0F8FF', alpha=0.3))  # 左下
ax.add_patch(patches.Rectangle((0, -10), 10, 10, color='#FFF0F5', alpha=0.3))  # 右下

# --- 6. 绘制坐标轴 ---
ax.set_xticks([])
ax.set_yticks([])

# 中心十字线
ax.axhline(y=0, color='#888888', linestyle='--', linewidth=1, zorder=1)
ax.axvline(x=0, color='#888888', linestyle='--', linewidth=1, zorder=1)

# 使用 LaTeX 数学符号绘制箭头 (不会受中文字体缺字影响)
ax.text(-9.5, 0.3, r"$\leftarrow$ 功能性", fontproperties=zh_font, fontsize=12, color='#555555', ha='left', style='italic')
ax.text(9.5, 0.3, r"情感性 $\rightarrow$", fontproperties=zh_font, fontsize=12, color='#555555', ha='right', style='italic')
ax.text(0.2, 9.5, r"$\uparrow$ 个人维度", fontproperties=zh_font, fontsize=12, color='#555555', va='top', style='italic')
ax.text(0.2, -9.5, r"$\downarrow$ 社会维度", fontproperties=zh_font, fontsize=12, color='#555555', va='bottom', style='italic')

# --- 7. 绘制气泡 ---
# 使用 flare 颜色列表
scatter = ax.scatter(x_vals, y_vals, s=sizes, c=colors, alpha=0.9, edgecolors='white', linewidth=2, zorder=3)

# --- 8. 添加文字标注 ---
for i, txt in enumerate(labels):
    # 动态计算文字偏移量
    offset = (sizes[i] ** 0.5) / 15 * 0.3 + 0.2

    # 绘制标签
    ax.text(x_vals[i], y_vals[i] - offset, txt,
            fontproperties=zh_font, color='#333333',
            ha='center', va='top', fontsize=12, weight='medium')

# --- 9. 标题与标签 (修复报错符号) ---
ax.set_title("图2-1：LDA主题分布气泡图（基于用户评论分析）", fontproperties=zh_font, fontsize=18, y=1.0)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# 【关键修改】将 ↔ 替换为 - 以避免字体报错
ax.set_xlabel("主题维度1（功能性 vs 情感性）", fontproperties=zh_font, fontsize=14, labelpad=15)
ax.set_ylabel("主题维度2（个人 vs 社会）", fontproperties=zh_font, fontsize=14, labelpad=15)

plt.tight_layout()
plt.savefig('LDA主题分布图.png', dpi=300, bbox_inches='tight')
# plt.show()