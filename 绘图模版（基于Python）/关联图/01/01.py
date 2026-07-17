import pandas as pd
import numpy as np
from pycirclize import Circos
import matplotlib.pyplot as plt

# ==========================================
# 1. 准备数据与全局设置
# ==========================================
# 强制清空画板 (防止旧图残留)
plt.clf()
plt.close('all')

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.sans-serif'] = ['Times New Roman']

# 数据标签
labels = [
    "Class A", "Class B",
    "Class C", "Class D",
    "Class E", "Class F",
    "Class G", "Class H"
]

# 矩阵数据
matrix_data = [
    #  A   B   C   D  |  E   F   G   H
    [  0,  0,  0,  0,   80, 60, 40, 20 ], # A 只连 E-H
    [  0,  0,  0,  0,   50, 40, 30, 10 ], # B 只连 E-H
    [  0,  0,  0,  0,   40, 30, 20,  5 ], # C 只连 E-H
    [  0,  0,  0,  0,   30, 20, 10,  5 ], # D 只连 E-H
    # ----------------------------------
    [ 70, 50, 40, 30,    0,  0,  0,  0 ], # E 回连 A-D
    [ 50, 40, 30, 20,    0,  0,  0,  0 ], # F 回连 A-D
    [ 30, 20, 10,  5,    0,  0,  0,  0 ], # G 回连 A-D
    [ 10,  5,  5,  2,    0,  0,  0,  0 ]  # H 回连 A-D
]

df = pd.DataFrame(matrix_data, index=labels, columns=labels)

# ==========================================
# 2. 生成颜色字典
# ==========================================
cmap = plt.get_cmap("viridis")
colors = [cmap(i) for i in np.linspace(0, 1, len(labels))]
sector_colors = dict(zip(labels, colors))
"""
其他配色方案：viridis
学术论文经典风 (tab10 或 tab20)：颜色区分度极高，每个类别颜色完全不一样，非常适合分类明确的数据。
强对比热力风 (magma 或 inferno)：深黑色到亮橙/黄色的渐变，视觉冲击力极强，背景如果是深色会非常酷炫。
清新柔和风 (Pastel1 或 Set3)：颜色很淡，像马卡龙色，看起来不累眼。
极简复古风 (RdBu 或 Spectral)：红蓝渐变或彩虹光谱，非常经典。
"""

# ==========================================
# 3. 核心对象初始化 (核武器级修复)
# ==========================================
print("正在初始化数据 (强制隐藏默认标签)...")

circos = Circos.initialize_from_matrix(
    df,
    space=5,  # space=5 此参数为圆环间距离
    cmap=sector_colors,
    link_kws=dict(ec="none", lw=0, alpha=0.45),
    # ec：边框颜色，lw：边框粗细；alpha：边框透明度

    # 【核心修改点】
    # 1. visible=False: 告诉 matplotlib 这个文字元素不要渲染
    # 2. color="none": 即使渲染了，也是透明的
    # 这样绝对不可能再显示出来了
    label_kws=dict(visible=False, color="none"),

    # 同样隐藏刻度
    ticks_interval=None
)

# ==========================================
# 4. 手动添加定制标签
# ==========================================
for sector in circos.sectors:
    # 获取颜色
    label_color = sector_colors[sector.name]

    # 手动添加我们想要的彩色标签
    sector.text(
        sector.name,
        r=102,  # 距离圆心距离
        size=16,  # 字号
        color=label_color,  # 颜色 (与圆环一致)
        fontweight="bold"  # 加粗
    )

# ==========================================
# 5. 执行绘图并保存
# ==========================================
print("正在绘图...")
fig = circos.plotfig(dpi=300)

output_file = "01.png"
fig.savefig(output_file, dpi=300, bbox_inches="tight")

print(f"成功！已生成只有彩色标签的完美图: {output_file}")
# plt.show()