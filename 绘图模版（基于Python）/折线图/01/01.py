import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import numpy as np  # 需要导入 numpy 来计算刻度位置
import matplotlib.ticker as ticker

# -----------------------------------------------------------------------------
# 1. 配置区域 (Configuration)
# -----------------------------------------------------------------------------
# 输入文件名 (确保文件在同一目录下，或填写绝对路径)
FILE_NAME = '01.csv'
# 输出图片名
OUTPUT_PDF = '01.pdf'
OUTPUT_PNG = '01.png'

# -----------------------------------------------------------------------------
# 2. 数据读取与预处理 (Data Loading & Preprocessing)
# -----------------------------------------------------------------------------
try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{FILE_NAME}'。请检查文件名或路径是否正确。")
    exit()

# 获取第一列的列名（默认为 X 轴）
x_col = df.columns[0]

# 强制将第一列转为字符串，防止 pandas 自动识别为其他格式
df[x_col] = df[x_col].astype(str)

# 数据重塑：宽表转长表
df_long = df.melt(id_vars=[x_col], var_name='Parameter_a', value_name='Value')

# -----------------------------------------------------------------------------
# 3. 绘图 (Plotting)
# -----------------------------------------------------------------------------
sns.set_theme(style="ticks", font_scale=1.2)
# 强行修改全局字体为 Times New Roman，这一步必须在 sns.set_theme 之后运行
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(8, 5))
"""
font_scale:将图表中所有的字体（标题、坐标轴、图例）放大倍数
figsize:设置图片的宽度为 12 英寸，高度为 7 英寸
style:有无网格之类的，背景是否白底；ticks为加了刻度线的

推荐几个科研常用的色板名（直接替换）：
"mako"：冷色调（深蓝到青色），非常高端，适合严肃的图表。
"rocket"：暖色调（深紫到亮橙），非常有冲击力。
"flare"：比较淡雅的红紫色。
"crest"：比较清新的蓝绿色。
"Spectral"：红橙黄绿蓝紫全光谱（区分度很高）。
"Set2" 或 "Pastel1"：低饱和度的莫兰迪色系（如果不喜欢太刺眼的颜色）。
"""

# 绘制折线图
sns.lineplot(
    data=df_long,
    x=x_col,
    y='Value',
    hue='Parameter_a',
    palette="Spectral",
    linewidth=1.5,
    alpha=0.95,
    sort=False  # sort=False 确保按照 CSV 里的原始顺序画图，不自动排序
)


# -----------------------------------------------------------------------------
# 4. 坐标轴优化、图例优化
# -----------------------------------------------------------------------------
# plt.title("Picture 01", fontsize=18, weight='bold', pad=10)
plt.xlabel("Date", fontsize=14, weight='bold')
plt.ylabel("Value", fontsize=14, weight='bold')

# 设置 X 轴间隔
INTERVAL_STEP = 12
all_labels = df[x_col].unique()
tick_positions = np.arange(0, len(all_labels), INTERVAL_STEP)
tick_labels = all_labels[::INTERVAL_STEP]
plt.xticks(tick_positions, tick_labels, rotation=0,
           fontsize=12, fontweight='bold', fontfamily='Times New Roman')

plt.yticks(fontsize=12, fontweight='bold', fontfamily='Times New Roman')

# 【可选】如果你想让刻度线（那根小短线）也变粗：
ax = plt.gca() # 获取当前坐标轴
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=9))
ax.tick_params(direction='in', top=False, right=False, width=2, length=4)

# 图例设置
plt.legend(title='Parameter',
           loc='best',    # <--- 自动寻找最佳位置
           frameon=True,  # 开启边框和背景，挡住背后的线
           ncol=2,        # 关键参数：设置为 2 列，即一行显示两个
           prop={'family': 'Times New Roman', 'weight': 'bold', 'size': 10}
           )
plt.tight_layout()
"""
右上角（默认）： loc='upper right'
左上角： loc='upper left'
右下角： loc='lower right'
左下角： loc='lower left'
正中间： loc='center'
右侧中间： loc='center right'
"""
# -----------------------------------------------------------------------------
# 5. 保存
# -----------------------------------------------------------------------------
plt.savefig(OUTPUT_PDF, format='pdf')
plt.savefig(OUTPUT_PNG, dpi=300)

print(f"绘图完成！\n   - {OUTPUT_PNG}\n   - {OUTPUT_PDF}")
plt.show()