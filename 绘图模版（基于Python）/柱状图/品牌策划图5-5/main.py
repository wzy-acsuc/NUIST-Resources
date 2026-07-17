import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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

# --- 2. 数据准备 ---
data = {
    "Stage": [
        "注意 (Attention)",
        "兴趣 (Interest)",
        "搜索 (Search)",
        "行动 (Action)",
        "分享 (Share)"
    ],
    "Traffic": [10000, 6000, 3500, 1200, 800]
}
df = pd.DataFrame(data)

# --- 3. 颜色设置 ---
palette_name = "Blues_r"
colors = sns.color_palette(palette_name, n_colors=len(df))

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

# 【核心修改】增加 width 参数
# width=0.5 表示柱子占据行宽的 50%，剩下的 50% 是间隙
bars = sns.barplot(
    x="Traffic",
    y="Stage",
    data=df,
    palette=colors,
    hue="Stage",
    legend=False,
    width=0.5,        # <--- 这里修改粗细 (默认约0.8，改小即变细)
    ax=ax
)

# --- 5. 细节美化 ---
ax.set_title("图 5-5：AISAS 传播路径漏斗图 (模拟流量)", fontproperties=zh_font, size=16, y=1.02)
ax.set_xlabel("流量数值", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("")

ax.tick_params(axis='y', labelsize=11)
for label in ax.get_yticklabels():
    label.set_fontproperties(zh_font)

ax.tick_params(axis='x', labelsize=10)
ax.set_xlim(0, 10500)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# 数值标签
for i, v in enumerate(df["Traffic"]):
    ax.text(v + 100, i, str(v), color='black', va='center', fontsize=10, fontname='Times New Roman')

# --- 6. 保存与显示 ---
plt.tight_layout()
plt.savefig('图5-5.png', dpi=300, bbox_inches='tight')
print(f"图表已生成，柱子宽度已调整为 0.5 (变细)。")
plt.show()