import matplotlib.pyplot as plt
from matplotlib import font_manager

# --- 1. 字体配置 ---
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.unicode_minus'] = False

# 中文设置：优先尝试 Mac 宋体，若无则尝试其他
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    try:
        zh_font = font_manager.FontProperties(family='STSong', size=12)
    except:
        # 如果以上都没有，使用系统默认 sans-serif (可能会乱码，需确保环境有中文字体)
        zh_font = font_manager.FontProperties(family='sans-serif', size=12)

# --- 2. 数据准备 (更新为您提供的新数据) ---
data_points = [
    {"name": "亚麻酸科普", "x": 75, "y": 85, "color": "#6FAEE5"},  # 蓝色
    {"name": "减肥食谱", "x": 70, "y": 80, "color": "#8CC183"},    # 绿色
    {"name": "成分解读", "x": 65, "y": 75, "color": "#4FB0A8"},    # 青色
    {"name": "宿舍美食", "x": 75, "y": 55, "color": "#F06E98"},    # 粉红
    {"name": "送礼指南", "x": 60, "y": 45, "color": "#AF6BB8"},    # 紫色
    {"name": "联名活动", "x": 40, "y": 50, "color": "#A08678"},    # 褐色
    {"name": "开箱测评", "x": 50, "y": 55, "color": "#FFA845"},    # 橙色
    {"name": "用户证言", "x": 60, "y": 70, "color": "#F2C336"},    # 黄色
]

# 提取绘图列表
names = [d["name"] for d in data_points]
xs = [d["x"] for d in data_points]
ys = [d["y"] for d in data_points]
colors = [d["color"] for d in data_points]
sizes = [1000] * len(data_points)  # 统一大点

# --- 3. 绘图 ---
fig, ax = plt.subplots(figsize=(12, 9), dpi=300)

# 绘制散点
ax.scatter(xs, ys, s=sizes, c=colors, alpha=1.0, zorder=3)

# --- 4. 添加文字标签 ---
offset_y = 2.0  # 文字向上偏移量

for i, txt in enumerate(names):
    # 1. 绘制名称 (上方)
    ax.text(xs[i], ys[i] + offset_y, txt,
            fontproperties=zh_font, color='black',
            ha='center', va='bottom', fontsize=13)

    # 2. 绘制坐标值 (下方小字)
    coord_text = f"({xs[i]},{ys[i]})"
    ax.text(xs[i], ys[i] - offset_y / 1.5, coord_text,
            fontproperties=zh_font, color='#666666',
            ha='center', va='top', fontsize=10)

# --- 5. 辅助线 (中心分割线) ---
# 根据数据分布，保持 x=60, y=65 作为分割线比较合理
line_x = 60
line_y = 65
ax.axvline(x=line_x, color='#C0C0C0', linestyle='--', linewidth=1.5, zorder=1)
ax.axhline(y=line_y, color='#C0C0C0', linestyle='--', linewidth=1.5, zorder=1)

# --- 6. 四象限策略标签 (位置已调整适配新坐标轴) ---
quadrants = [
    # 第一象限 (右上: 高互动 高转化) -> 明星内容
    {"x": 82, "y": 90, "title": "明星内容", "sub": "高互动·高转化", "color": "#6BBE76"},
    # 第二象限 (左上: 低互动 高转化) -> 潜力内容
    {"x": 40, "y": 90, "title": "潜力内容", "sub": "需优化·提互动", "color": "#F2C336"},
    # 第三象限 (左下: 低互动 低转化) -> 淘汰内容
    {"x": 40, "y": 35, "title": "淘汰内容", "sub": "低互动·低转化", "color": "#909399"},
    # 第四象限 (右下: 高互动 低转化) -> 问题内容
    {"x": 82, "y": 35, "title": "问题内容", "sub": "高互动·低转化", "color": "#F56C6C"},
]

for q in quadrants:
    text_content = f"{q['title']}\n{q['sub']}"
    ax.text(q['x'], q['y'], text_content, fontproperties=zh_font,
            color=q['color'],
            ha='center', va='center', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.6",
                      fc="white",
                      ec=q['color'],
                      linewidth=1,
                      alpha=0.9))

# --- 7. 坐标轴与标题设置 ---
# 用户要求: 起始都为30
ax.set_xlim(30, 95)
ax.set_ylim(30, 95)

# 用户要求: 横坐标是互动，纵坐标是转化
ax.set_xlabel("互动指数", fontproperties=zh_font, fontsize=14)
ax.set_ylabel("转化指数", fontproperties=zh_font, fontsize=14)
ax.set_title("图5-1：内容主题矩阵分布图（四象限策略）", fontproperties=zh_font, fontsize=18, y=1.01)

# 网格线
ax.grid(True, linestyle='--', alpha=0.3, color='#E0E0E0', zorder=0)

plt.tight_layout()

# --- 8. 保存与显示 ---
plt.savefig('内容主题矩阵分布图_修正版.png', dpi=300, bbox_inches='tight')
plt.show()