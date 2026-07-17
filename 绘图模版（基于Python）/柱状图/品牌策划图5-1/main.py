import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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

# --- 2. 数据准备 ---
data = {
    "Factor": [
        "信任", "品质感知", "品牌认知", "知名度", "价值匹配",
        "风味", "设计", "设计吸引", "产地", "健康",
        "形象老旧", "价格", "社交"
    ],
    "Score": [
        0.405, 0.102, 0.088, 0.085, 0.055,
        0.048, 0.045, 0.042, 0.038, 0.032,
        0.022, 0.020, 0.015
    ]
}

df = pd.DataFrame(data)

# --- 3. 颜色设置 ---
palette_name = "Spectral"
colors = sns.color_palette(palette_name, n_colors=len(df))

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# 【修复1】添加 hue="Factor" 和 legend=False
# 这样 Seaborn 就知道是用颜色来区分 Factor，符合新版规范
sns.barplot(
    x="Score",
    y="Factor",
    data=df,
    palette=colors,
    hue="Factor",
    legend=False,
    ax=ax
)

# --- 5. 细节美化 ---

# 标题
ax.set_title("图5-1:购买意向驱动因子重要性 Top10", fontproperties=zh_font, size=16, y=1.02)

# X轴标签
ax.set_xlabel("重要性得分", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("")

# 【修复2】更安全地设置 Y 轴中文字体
# 不直接 set_yticklabels，而是遍历修改现有标签的属性
# 这样避免了 "FixedFormatter used without FixedLocator" 警告
ax.tick_params(axis='y', labelsize=11)
for label in ax.get_yticklabels():
    label.set_fontproperties(zh_font)

# 设置X轴数值字体
ax.tick_params(axis='x', labelsize=10)

# 设置X轴范围
ax.set_xlim(0, 0.45)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('品牌策划图5-5.png', dpi=300, bbox_inches='tight')
print(f"图表已生成，警告已全部修复。")
# plt.show()