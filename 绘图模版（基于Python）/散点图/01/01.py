import matplotlib.pyplot as plt
from matplotlib import font_manager

# --- 1. 字体配置 ---
# 全局设置：数字和英文使用 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.unicode_minus'] = False

# 中文设置：Mac 宋体 (Songti SC)
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    print("未找到 Songti SC，尝试使用 STSong...")
    zh_font = font_manager.FontProperties(family='STSong', size=12)

# --- 2. 数据准备 ---
color_palette = [
    "#D47F9D",  # 完香牌 (Flare红紫 - 最鲜艳)
    "#B08EA2",  # 欧丽薇兰 (深紫灰)
    "#9F9FBC",  # 鲁花 (静谧蓝紫)
    "#8EA0B0",  # 多力 (雾霾蓝)
    "#B2C8BB",  # 金龙鱼 (灰豆绿)
    "#D8C3B4",  # 西王 (浅褐粉)
    "#C0C0C0"   # 福临门 (经典银灰)
]
data = {
    "brand": ["完香牌", "欧丽薇兰", "鲁花", "多力", "金龙鱼", "西王", "福临门"],
    "x":      [55,       95,        75,    80,    70,      65,     60],
    "y":      [92,       85,        80,    78,    75,      72,     70],
    # "color":  ["#F2C93B", "#808080", "#808080", "#808080", "#808080", "#808080", "#808080"],
    "color": color_palette,
    "size":   [400,      250,       200,   200,   200,     200,    200]
}

# --- 3. 绘图 ---
fig, ax = plt.subplots(figsize=(10, 7), dpi=120)

# 绘制散点
ax.scatter(data['x'], data['y'], s=data['size'], c=data['color'], alpha=1.0, zorder=3)

# --- 4. 添加文字标签 (可调整距离) ---
# 【这里修改距离】：数字越小，文字离点越近
offset_distance = 1.2

for i, txt in enumerate(data['brand']):
    if txt == "完香牌":
        # 主角：文字颜色与球体一致，加粗，字号大
        ax.text(data['x'][i], data['y'][i] + offset_distance, txt,
                fontproperties=zh_font, color=data['color'][i], # 文字颜色跟随球体
                ha='center', va='bottom', fontsize=16, weight='bold')
    else:
        # 竞品：文字统一用深灰色 (为了保持整洁，建议竞品文字不要五颜六色，否则会乱)
        # 如果你希望竞品文字也跟着球体变色，把 color='#555555' 改为 color=data['color'][i] 即可
        ax.text(data['x'][i], data['y'][i] + offset_distance, txt,
                fontproperties=zh_font, color=data['color'][i],
                ha='center', va='bottom', fontsize=12)

# --- 5. 辅助线与注释 ---
ax.axvline(x=70, color='#C0C0C0', linestyle='--', linewidth=1.5, zorder=1)
ax.axhline(y=75, color='#C0C0C0', linestyle='--', linewidth=1.5, zorder=1)

# 【修改点1】定义新的高亮色：柔和的青绿色
highlight_color = "#739F8D"

quadrant_texts = [
    # 【修改点2】使用新变量替换原来的绿色
    (55, 96, "高健康\n中低价", highlight_color),
    (85, 96, "高健康\n高价格", "#808080"),
    (55, 68, "低健康\n中低价", "#808080"),
    (85, 68, "低健康\n高价格", "#808080")
]

for x, y, text, color in quadrant_texts:
    ax.text(x, y, text, fontproperties=zh_font, color=color, ha='center', va='center', fontsize=12)

# 【修改点3】方框的文字颜色(color)和边框颜色(ec)也同步修改
box_text = "市场空白区域\n(高健康+中低价位)"
ax.text(51, 88, box_text, fontproperties=zh_font,
        color=highlight_color, # 文字变色
        ha='left', va='center', fontsize=11,
        bbox=dict(boxstyle="round,pad=0.5", fc="white",
                  ec=highlight_color, # 边框变色
                  alpha=0.9))

# --- 6. 坐标轴设置 ---
ax.set_xlim(40, 110)
ax.set_ylim(60, 100)
ax.set_xlabel("价格定位指数", fontproperties=zh_font, fontsize=14)
ax.set_ylabel("健康认知指数", fontproperties=zh_font, fontsize=14)
ax.set_title("图1-2：竞品心智定位感知图", fontproperties=zh_font, fontsize=18, y=1.0)
ax.grid(True, linestyle='--', alpha=0.3, color='#E0E0E0', zorder=0)

plt.tight_layout()

# --- 7. 保存图片 (新增代码) ---
# dpi=300: 高清分辨率 (一般论文或打印用300)
# bbox_inches='tight': 自动裁剪白边，防止标题或坐标轴被切掉
plt.savefig('竞品分析图.png', dpi=300, bbox_inches='tight')
print("图片已保存为 '竞品分析图.png'")

# plt.show()