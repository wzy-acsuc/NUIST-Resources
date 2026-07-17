import matplotlib.pyplot as plt
import numpy as np

# 1. 针对 Mac 系统的中文字体配置
# 'Arial Unicode MS' 或 'STHeiti' 是 Mac 自带且支持中文的字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
# --- 新增：设置全局显示 DPI ---
plt.rcParams['figure.dpi'] = 300
# 定义 5 号字对应的大小 (通常 5 号字对应 10.5 pt)
FONT_SIZE = 10.5

# 2. 准备数据
countries = ['新加坡', '马来西亚', '泰国', '印尼', '越南', '菲律宾']
import_volume = [2800, 2100, 1800, 3200, 1200, 800]
export_volume = [2600, 1900, 1600, 2900, 1100, 750]

x = np.arange(len(countries))
width = 0.35

# 3. 创建画布
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#EAEAF2')
ax.grid(color='white', linestyle='-', linewidth=0.5, alpha=0)

# 4. 绘制柱状图
ax.bar(x - width/2, import_volume, width, label='进口量', color='#FF8888')
ax.bar(x + width/2, export_volume, width, label='出口量', color='#70D3CC')

# 5. 设置文字和字号（全部统一为 5 号字）
ax.set_title('图1-1 数字丝绸之路沿线国家香料贸易数据对比', fontsize=FONT_SIZE, pad=10)
ax.set_xlabel('沿线国家', fontsize=FONT_SIZE)
ax.set_ylabel('贸易量 (吨)', fontsize=FONT_SIZE)

# 设置刻度字体大小
ax.tick_params(axis='both', labelsize=FONT_SIZE)
ax.set_xticks(x)
ax.set_xticklabels(countries, fontsize=FONT_SIZE)

# 设置图例字体大小
ax.legend(fontsize=FONT_SIZE)

# 移除边框
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()