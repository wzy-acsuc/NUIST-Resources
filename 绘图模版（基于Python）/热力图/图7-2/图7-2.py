import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- 1. 字体设置 ---
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
try:
    zh_font = font_manager.FontProperties(family='Songti SC', size=12)
    font_manager.findfont(zh_font, fallback_to_default=False)
except:
    zh_font = font_manager.FontProperties(family='SimHei', size=12)

# --- 2. 数据准备 (核心修改部分) ---
# 我们保持 Y轴从上到下是 R=5 -> R=1
# 修改 X轴从左到右是 F=1 -> F=5 (低频到高频)

# 行：R5, R4, R3, R2, R1
# 列：F1, F2, F3, F4, F5
labels_data = [
    # R=5 (最近购买 - 最上面一行)
    [("潜力客户", "重点激活"), ("潜力客户", "引导复购"), ("一般发展", "提升客单"), ("重要发展", "升级转化"), ("重要价值", "VIP服务")],
    # R=4
    [("新客户", "新手礼包"), ("潜力客户", "培养习惯"), ("一般价值", "专属优惠"), ("重要发展", "消费激励"), ("重要价值", "优先体验")],
    # R=3
    [("待激活", "新品推荐"), ("待激活", "活动通知"), ("一般保持", "会员权益"), ("重要保持", "定期关怀"), ("重要保持", "防流失")],
    # R=2
    [("流失预警", "短信唤醒"), ("需挽回", "问卷调查"), ("需挽回", "优惠券"), ("重要挽留", "专人对接"), ("重要挽留", "紧急干预")],
    # R=1 (很久没买 - 最下面一行)
    [("完全流失", "降低成本"), ("流失客户", "尝试召回"), ("流失边缘", "强力挽留"), ("重要挽留", "回归礼包"), ("重要挽留", "最后尝试")]
]

# 价值分数矩阵 (用于颜色深浅)
# 逻辑：右上角(R5, F5)分数最高(绿色)，左下角(R1, F1)分数最低(红色)
value_matrix = np.array([
    [6, 7, 8, 9, 10], # R=5 (分数高)
    [5, 6, 7, 8, 9],  # R=4
    [4, 5, 6, 7, 8],  # R=3
    [3, 4, 5, 6, 7],  # R=2
    [2, 3, 4, 5, 6]   # R=1 (分数低)
])

# --- 3. 配色方案 ---
# 使用 RdYlGn (红-黄-绿)，分数越高越绿(右上)，分数越低越红(左下)
cmap_name = 'RdYlGn'

# --- 4. 绘图 ---
fig, ax = plt.subplots(figsize=(10, 8), dpi=150)

# 绘制热力图
im = ax.imshow(value_matrix, cmap=cmap_name, aspect='auto', alpha=0.8)

# --- 5. 添加文字 ---
rows, cols = 5, 5
for i in range(rows):
    for j in range(cols):
        main_label, sub_label = labels_data[i][j]

        # 智能文字颜色：背景太深或太浅时用白色，中间色用黑色
        # value_matrix范围大概是2-10
        val = value_matrix[i][j]
        text_color = 'white' if val >= 9 or val <= 3 else '#333333'

        # 主标题
        ax.text(j, i - 0.1, main_label, ha="center", va="center",
                color=text_color, fontproperties=zh_font, fontsize=11, fontweight='bold')
        # 副标题
        ax.text(j, i + 0.15, sub_label, ha="center", va="center",
                color=text_color, fontproperties=zh_font, fontsize=9, alpha=0.9)

# --- 6. 坐标轴设置 (关键修正) ---

# X轴：从 F=1 (左) 到 F=5 (右)
ax.set_xticks(np.arange(cols))
ax.set_xticklabels(['F=1\n低频', 'F=2', 'F=3', 'F=4', 'F=5\n高频'], fontproperties=zh_font, fontsize=12)

# Y轴：从 R=5 (上) 到 R=1 (下)
ax.set_yticks(np.arange(rows))
ax.set_yticklabels(['R=5\n最近', 'R=4', 'R=3', 'R=2', 'R=1\n久远'], fontproperties=zh_font, fontsize=12)

# 轴标签
ax.set_title("图7-2：RFM客户分层运营策略图", fontproperties=zh_font, fontsize=18, y=1.02)
ax.set_xlabel("消费频次 (F)", fontproperties=zh_font, fontsize=14, labelpad=15)
ax.set_ylabel("最近购买时间 (R)", fontproperties=zh_font, fontsize=14, labelpad=15)

# 去除刻度线
ax.tick_params(which="both", bottom=False, left=False)

# 添加颜色条
cbar = ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("客户价值指数", fontproperties=zh_font, rotation=270, labelpad=15)

plt.tight_layout()
plt.savefig('RFM.png', dpi=300, bbox_inches='tight')
# plt.show()