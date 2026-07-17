import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

# --- 2. 创建画布 ---
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')  # 关闭坐标轴


# --- 3. 绘图辅助函数 ---
def draw_fancy_box(x, y, width, height, color, title, subtitle=None, ax=ax):
    # 绘制圆角矩形
    box = mpatches.FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.2,rounding_size=0.3",
        ec="black", fc=color, alpha=0.9, zorder=2, linewidth=1
    )
    ax.add_patch(box)

    # 计算中心点
    cx = x + width / 2
    cy = y + height / 2

    # 绘制标题
    ax.text(cx, cy + (0.15 if subtitle else 0), title,
            fontproperties=zh_font, fontsize=13, fontweight='bold',
            ha='center', va='center', color='#333333', zorder=3)

    # 绘制副标题 (如果有)
    if subtitle:
        ax.text(cx, cy - 0.2, subtitle,
                fontproperties=zh_font, fontsize=10,
                ha='center', va='center', color='#555555', zorder=3)
    return cx, cy, x + width, x  # 返回中心坐标和边缘X以便画线


# --- 4. 绘制核心模块 ---

# A. 线上渠道 (左上) - 粉色系
cx_online, cy_online, right_online, left_online = draw_fancy_box(
    1, 5.5, 3, 1.2, "#FFCDD2", "线上渠道", "天猫 / 京东 / 抖音"
)

# B. 线下渠道 (左下) - 蓝色系
cx_offline, cy_offline, right_offline, left_offline = draw_fancy_box(
    1, 1.5, 3, 1.2, "#B3E5FC", "线下渠道", "高端商超 / 社区生鲜店"
)

# C. 全渠道融合 O2O (中间核心) - 绿色系
# 画一个大一点的框表示核心地位
cx_o2o, cy_o2o, right_o2o, left_o2o = draw_fancy_box(
    5.5, 3.2, 2.5, 1.8, "#C8E6C9", "全渠道融合\n(O2O Core)", "数据打通 | 库存共享"
)

# D. 消费者 (右侧) - 橙色系
cx_user, cy_user, right_user, left_user = draw_fancy_box(
    10, 3.5, 1.5, 1.2, "#FFE0B2", "消费者", "Target"
)


# --- 5. 绘制连接线与功能说明 ---

# 函数：绘制带文字的箭头
def draw_arrow_text(start_xy, end_xy, text, text_offset=(0, 0.3), color='gray'):
    # 箭头
    ax.annotate("", xy=end_xy, xytext=start_xy,
                arrowprops=dict(arrowstyle="->", color=color, lw=2, shrinkA=5, shrinkB=5))

    # 文字 (位于箭头中间)
    mid_x = (start_xy[0] + end_xy[0]) / 2
    mid_y = (start_xy[1] + end_xy[1]) / 2
    ax.text(mid_x + text_offset[0], mid_y + text_offset[1], text,
            fontproperties=zh_font, fontsize=10, color='#444444',
            ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8))


# 路径 1: 线上 -> O2O
# 功能: 品牌曝光 & 流量导入
draw_arrow_text(
    (right_online + 0.2, cy_online),  # 出发点 (框右侧)
    (left_o2o - 0.2, cy_o2o + 0.4),  # 结束点 (O2O框左上侧)
    "品牌曝光 & 流量导入"
)

# 路径 2: 线下 -> O2O
# 功能: 产品体验 & 即时交付
draw_arrow_text(
    (right_offline + 0.2, cy_offline),  # 出发点
    (left_o2o - 0.2, cy_o2o - 0.4),  # 结束点 (O2O框左下侧)
    "产品体验 & 即时交付",
    text_offset=(0, -0.1)
)

# 路径 3: O2O -> 消费者
# 功能: 优质服务
draw_arrow_text(
    (right_o2o + 0.2, cy_o2o),
    (left_user - 0.2, cy_user),
    "无缝体验 & 服务",
    text_offset=(0, 0.2)
)

# --- 6. 装饰与标题 ---
ax.set_title("图 6-1：线上线下融合 (O2O) 通路模式图", fontproperties=zh_font, fontsize=16, y=0.95)

# 底部说明文字
desc = "图表说明：新通路以O2O为核心，整合线上流量与线下体验，实现对消费者的全方位覆盖。"
ax.text(6, 0.5, desc, fontproperties=zh_font, fontsize=11, color='#666666', ha='center')

# --- 7. 保存 ---
plt.tight_layout()
#plt.savefig('O2O_Integration_Chart.png', dpi=300, bbox_inches='tight')
print("图表已生成：O2O_Integration_Chart.png")
plt.show()