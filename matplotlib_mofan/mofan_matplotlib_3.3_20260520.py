# Contour 等高线图

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

# 计算高度值，the height function
# 定义一个二元函数，用于计算每个点 (x, y) 的高度值（z 值）
# 公式： (1 - x/2 + x**5 + y**3) * exp(-x**2 - y**2)
def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256  # 网格的采样点数（每个维度上的点数，共 n×n 个点）
x = np.linspace(-3, 3, n)  # 创建 x 坐标数组：从 -3 到 3 均匀取 n 个点
y = np.linspace(-3, 3, n)  # 创建 y 坐标数组：从 -3 到 3 均匀取 n 个点
X,Y = np.meshgrid(x, y)
# 将 x 和 y 数组转换为二维网格坐标矩阵 X 和 Y，用于计算每个网格点上的 z 值
# 把x，y网格化，也就是f（x y）这个二元函数它的地域为正方形区域

# 为每一块登高区域填充颜色，use plt.contourf to filling contours
# X, Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot) 

# 绘制填充等高线图（contour fill）
#   X, Y     : 网格点的 x 和 y 坐标矩阵
#   f(X, Y)  : 每个网格点上的 z 值（高度）
#   8        : 将高度范围分成 8 个区间（即绘制 8 层颜色填充）
#   alpha=0.75 : 填充颜色的透明度（0 完全透明，1 完全不透明）
#   cmap=plt.cm.hot : 颜色映射表，使用 'hot' 颜色方案（黑色-红-黄-白）

# 添加等高线，use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

# 绘制等高线（轮廓线）
#   X, Y, f(X,Y) : 同上的网格坐标和高度值
#   8            : 绘制 8 条等高线（与填充层数一致）
#   colors='black': 等高线的颜色为黑色
#   linewidth=0.5 : 等高线的线宽为 0.5 点

# 添加等高线的标签，adding label
plt.clabel(C, inline=True, fontsize=10,fmt='%.3f')

# 在等高线上添加数值标签
#   C            : 上面 plt.contour 返回的 ContourSet 对象
#   inline=True  : 标签内嵌在等高线中（打断线条，避免覆盖）
#   fontsize=10  : 标签字体大小为 10 点
#   fmt='%.3f'   : 标签保留小数点后三位

plt.xticks(())
plt.yticks(())
plt.show()





