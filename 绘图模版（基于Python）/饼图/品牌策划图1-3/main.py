import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import font_manager
from sympy.abc import alpha

# --- 1. 字体与画布设置 ---

# 设置全局西文字体为 Times New Roman (影响百分比数字)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

# 设置中文字体 (用于标题和标签)
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=14)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    try:
        zh_font = font_manager.FontProperties(family='SimSun', size=14)
    except:
        zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=14)

# 创建画布
fig, ax = plt.subplots(figsize=(8, 8), dpi=300)

# --- 2. 数据准备 ---
labels = ['金龙鱼', '鲁花', '福临门', '完香', '其他']
sizes = [35.0, 25.0, 20.0, 5.0, 15.0]

# --- 3. 颜色设置 ---
palette_name = 'Spectral'
colors = sns.color_palette(palette_name, n_colors=len(labels))

# 【核心修改】在此处添加透明度
# alpha 取值范围 0 (全透明) - 1 (不透明)
# 这里设置为 0.7 (70% 不透明)
colors = [(*color, 0.6) for color in colors]

# --- 4. 绘图 ---

# 绘制饼图
# startangle=45 只是为了让扇区角度更接近原图的视觉分布
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                  startangle=45, colors=colors,
                                  pctdistance=0.6, labeldistance=1.05)

# --- 5. 字体细节调整 ---

# 调整百分比标签 (autotexts) -> 使用全局设置的新罗马字体
plt.setp(autotexts, size=11, color="black") # 或者是 white，看颜色深浅

# 调整品牌文本标签 (texts) -> 强制使用中文字体
for text in texts:
    text.set_fontproperties(zh_font)
    text.set_size(12)

# --- 6. 标题与保存 ---

# 设置标题
ax.set_title("品牌策划图1-3：中国食用油市场主要品牌份额比较", fontproperties=zh_font, size=16, y=1.0)

plt.tight_layout()
plt.savefig('品牌策划图1-3', dpi=300, bbox_inches='tight')
print(f"图表已生成，当前配色模版：{palette_name}")
# plt.show()