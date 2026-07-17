import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager
import numpy as np

# --- 1. 字体与画布设置 ---
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
try:
    # 优先使用 macOS 的 Songti SC，Windows 可换为 Microsoft YaHei
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='Microsoft YaHei', size=12)

fig, ax = plt.subplots(figsize=(16, 9), dpi=150)

# --- 2. 数据准备 ---
# 状态颜色映射
status_colors = {
    "已完成": "#4CAF50",  # 绿色
    "进行中": "#FBC02D",  # 金色
    "待开始": "#9E9E9E"  # 灰色
}

# 里程碑数据 (时间坐标, 标题, 状态, 上下位置偏移)
# M1-M3: 第一阶段
milestones_stage1 = [
    (1.0, "M1: 品牌定位确认", "已完成", 1),
    (1.5, "M1.5: 团队组建完成", "已完成", -1),
    (2.0, "M2: 小红书账号上线", "已完成", 1),
    (2.5, "M2.5: 首批KOC签约", "进行中", -1),
    (3.0, "M3: 首月内容发布50篇", "已完成", 1),
]

# M4-M6: 第二阶段
milestones_stage2 = [
    (4.0, "M4: 618大促筹备", "待开始", 1),
    (4.5, "M4.5: 直播带货首秀", "待开始", -1),
    (5.0, "M5: 618大促执行", "待开始", 1),
    (5.5, "M5.5: 私域社群上线", "待开始", -1),
    (6.0, "M6: 618复盘优化", "待开始", 1),
]

# M7-M12: 第三阶段 (跨度较大，坐标手动调整以美观)
milestones_stage3 = [
    (7.0, "M7: 暑期专项活动", "待开始", -1),
    (9.0, "M9: 双11策略制定", "待开始", 1),
    (10.0, "M10: 双11预热启动", "待开始", -1),
    (11.0, "M11: 双11大促执行", "待开始", 1),
    (12.0, "M12: 年度复盘规划", "待开始", -1),
]

all_milestones = milestones_stage1 + milestones_stage2 + milestones_stage3

# --- 3. 绘制背景区域 (三阶段) ---
# 定义阶段区间
stages = [
    (0.5, 3.5, "第一阶段：基础建设期 (M1-M3)", "#E3F2FD"),  # 浅蓝
    (3.5, 6.5, "第二阶段：增长加速期 (M4-M6)", "#F3E5F5"),  # 浅紫
    (6.5, 12.5, "第三阶段：规模放大期 (M7-M12)", "#E8F5E9")  # 浅绿
]

for start, end, label, color in stages:
    # 绘制背景块
    ax.axvspan(start, end, color=color, alpha=0.6, zorder=0)
    # 绘制阶段标题
    ax.text((start + end) / 2, 1.8, label, fontproperties=zh_font, fontsize=14,
            fontweight='bold', color="#555555", ha='center', va='center',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.3'))

# --- 4. 绘制时间主轴 ---
ax.axhline(y=0, color='#B0BEC5', linewidth=4, zorder=1)  # 灰色粗线作为主轴

# --- 5. 绘制里程碑节点 (Stem Plot 风格) ---
for x, label, status, offset in all_milestones:
    color = status_colors[status]
    y_pos = offset * 0.8  # 控制高度幅度

    # 1. 画垂直连接线
    ax.vlines(x=x, ymin=0, ymax=y_pos, color=color, linewidth=2, linestyle='--', zorder=2)

    # 2. 画圆点
    ax.scatter(x, y_pos, color=color, s=400, zorder=3, edgecolors='white', linewidth=1.5)

    # 3. 画文字标签 (带背景框以防重叠)
    # 根据上下位置调整文字偏移
    text_y_offset = 0.3 if offset > 0 else -0.3
    va = 'bottom' if offset > 0 else 'top'

    # 将 "M1: 标题" 换行显示，更美观
    display_text = label.replace(": ", "\n")

    ax.text(x, y_pos + text_y_offset, display_text, fontproperties=zh_font, fontsize=10,
            ha='center', va=va, color="#333333", fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor=color, boxstyle='round,pad=0.3', linewidth=1))

    # 4. 在圆点中间写上 M序号 (可选，这里为了简洁省略，直接标在旁边)
    # ax.text(x, y_pos, label.split(":")[0], color='white', ha='center', va='center', fontsize=8, fontproperties=zh_font)

# --- 6. 装饰与图例 ---

# 图例
legend_elements = [
    patches.Patch(facecolor=status_colors["已完成"], label='已完成'),
    patches.Patch(facecolor=status_colors["进行中"], label='进行中'),
    patches.Patch(facecolor=status_colors["待开始"], label='待开始')
]
ax.legend(handles=legend_elements, loc='upper right', prop=zh_font, fontsize=12, frameon=True, framealpha=1)

# 坐标轴设置
ax.set_xlim(0.5, 12.5)
ax.set_ylim(-2, 2.2)
ax.set_xticks(np.arange(1, 13))
ax.set_xticklabels([f"{i}月" for i in range(1, 13)], fontproperties=zh_font, fontsize=12)
ax.set_xlabel("时间线（月度）", fontproperties=zh_font, fontsize=14)

# 隐藏Y轴
ax.get_yaxis().set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)

# 标题
ax.set_title("图10-1：三阶段项目推进路线图（里程碑管理）", fontproperties=zh_font, fontsize=20, y=1.02)

plt.tight_layout()
plt.savefig('Project_Milestone_Roadmap.png', dpi=300, bbox_inches='tight')
print("图片已生成：Project_Milestone_Roadmap.png")
# plt.show()