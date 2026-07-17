import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import font_manager

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

# --- 2. 数据准备 (根据 image_f47f78.png 修改) ---
labels = ['社交媒体投放', '线下活动/非遗节', '产品研发/包装', '渠道建设', '品牌共创激励']
sizes = [35.0, 25.0, 20.0, 15.0, 5.0]

# --- 3. 颜色设置 (保留原代码逻辑) ---
palette_name = 'Spectral'
colors = sns.color_palette(palette_name, n_colors=len(labels))

# 添加透明度 (alpha=0.6)
colors = [(*color, 0.6) for color in colors]

# --- 4. 绘图 ---

# 绘制饼图
# startangle=140 是为了让最大的块(35%)大致位于左侧，模仿原图布局
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                  startangle=140, colors=colors,
                                  pctdistance=0.6, labeldistance=1.05)

# --- 5. 字体细节调整 ---

# 调整百分比标签 (autotexts)
plt.setp(autotexts, size=12, color="black")

# 调整品牌文本标签 (texts)
for text in texts:
    text.set_fontproperties(zh_font)
    text.set_size(12)

# --- 6. 标题与保存 ---

# 设置标题
ax.set_title("品牌焕新项目预算分配比例", fontproperties=zh_font, size=16, y=1.0)

plt.tight_layout()
plt.savefig('图9-1.png', dpi=300, bbox_inches='tight')
print(f"图表已生成，数据已更新为预算分配，使用 {palette_name} 配色。")
#plt.show()