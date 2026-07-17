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

# --- 2. 数据模拟 ---
n_samples = 1000
data = {
    "品质感知": np.random.normal(loc=1.2, scale=1.5, size=n_samples),
    "信任":     np.random.normal(loc=0.5, scale=1.2, size=n_samples),
    "健康价值": np.random.normal(loc=0.2, scale=0.8, size=n_samples),
    "设计吸引": np.random.normal(loc=-0.1, scale=1.0, size=n_samples),
    "价格敏感": np.random.normal(loc=-1.5, scale=1.1, size=n_samples),
    "社交影响": np.random.normal(loc=0.8, scale=1.3, size=n_samples),
}

df = pd.DataFrame(data)
df_melted = df.melt(var_name="Feature", value_name="SHAP Value")

# --- 3. 颜色设置 ---
palette_name = "Spectral"

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

sns.violinplot(
    x="SHAP Value",
    y="Feature",
    data=df_melted,
    palette=palette_name,
    hue="Feature",
    legend=False,
    inner='box',
    linewidth=1.2,
    density_norm='width',
    orient='h',
    ax=ax
)

# --- 5. 细节美化 ---
ax.set_title("图 5-1-1：XGBoost 特征贡献 SHAP 摘要图", fontproperties=zh_font, size=16, y=1.02)
ax.set_xlabel("对购买意向的影响 (SHAP Value)", fontproperties=zh_font, fontsize=12)
ax.set_ylabel("")

# 设置字体
ax.tick_params(axis='y', labelsize=11)
for label in ax.get_yticklabels():
    label.set_fontproperties(zh_font)
ax.tick_params(axis='x', labelsize=11)

# 【核心修改】恢复四周方框
# 将上下左右的边框全部显示，并设置统一线宽
for spine in ['top', 'bottom', 'left', 'right']:
    ax.spines[spine].set_visible(True)
    ax.spines[spine].set_linewidth(0.8)
    ax.spines[spine].set_color('black')

plt.tight_layout()
plt.savefig('图5-1-1.png', dpi=300, bbox_inches='tight')
print(f"图表已生成，已恢复四周黑色边框。")
#plt.show()