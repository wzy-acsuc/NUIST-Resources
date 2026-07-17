import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import font_manager

# --- 1. 字体与画布设置 ---

# 全局西文字体 (Times New Roman)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

# 中文字体设置
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    try:
        zh_font = font_manager.FontProperties(family='SimSun', size=12)
    except:
        zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

# 创建画布
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# --- 2. 数据准备 (根据图片估算) ---
brands = ['完香', '竞品A', '竞品B', '竞品C']
x_awareness = np.array([45, 85, 70, 60])   # X轴：知名度
y_reputation = np.array([75, 80, 65, 70])  # Y轴：美誉度
# 气泡大小 (模拟原图大小差异)
sizes = np.array([1200, 800, 800, 800])

# --- 3. 颜色设置 (使用模版 + 透明度) ---

# 选择模版: 'flare' (暖色), 'crest' (冷色), 'viridis', 'hls'
palette_name = 'flare'

# 生成基础颜色
base_colors = sns.color_palette(palette_name, n_colors=len(brands))

# 添加透明度 (0.7)
alpha_value = 1
colors = [(*c, alpha_value) for c in base_colors]

# --- 4. 绘图 ---

# 绘制散点 (气泡)
scatter = ax.scatter(x_awareness, y_reputation, s=sizes, c=colors,
                     edgecolors='white', linewidth=1.5) # 加个白边更好看

# 添加文字标签 (品牌名)
# 稍微调整位置 (x+1.5, y-0.5) 让文字不要挡住气泡中心
for i, txt in enumerate(brands):
    ax.text(x_awareness[i] + 1.5, y_reputation[i], txt,
            fontproperties=zh_font, fontsize=12, va='center')

# --- 5. 坐标轴与装饰 ---

# 标题
ax.set_title("图 1-4：品牌健康指数 (BHI) 三维散点图", fontproperties=zh_font, size=16, y=1.02)

# 坐标轴标签
ax.set_xlabel("知名度", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("美誉度", fontproperties=zh_font, fontsize=12)

# 设置坐标轴范围 (留出一点边距)
ax.set_xlim(42, 88)
ax.set_ylim(64, 82)

# 坐标轴刻度字体大小
ax.tick_params(axis='both', labelsize=11)

# 网格线
ax.grid(True, linestyle='-', alpha=0.5, color='gray', linewidth=0.5)

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('图1-4.png', dpi=300, bbox_inches='tight')
print(f"图表已生成，使用配色模版：{palette_name}")
# plt.show()