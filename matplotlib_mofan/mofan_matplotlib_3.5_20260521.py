# 3D plot 3D数据

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

fig = plt.figure()  # 定义一个图表fig
ax = fig.add_subplot(111, projection='3d')  # 替代 Axes3D(fig)，核心修复：高版本Matplotlib的3D轴初始化方式
# 参数111 是 1, 1, 1 的缩写，表示将画布（figure）分成 1 行 1 列，并选择第 1 个子图（也就是唯一的那个子图）
# 参数projection='3d'必须提供，没有 projection='3d'，后面的 plot_surface、contourf 等 3D 绘图方法将无法调用
# ax = Axes3D(fig)  # 没用的，可以删掉，用Axes3D将fig进行3D化
# fig.add_axes(ax)
# 3.9以上版本需要在ax=Axes3D语句下面再写一行fig.add_axes(ax)

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # 将 X 和 Y 数组转换为二维网格坐标矩阵 X 和 Y，用于计算每个网格点上的 z 值
R = np.sqrt(X ** 2 + Y ** 2)

# height value
Z = np.sin(R)

# 画出曲面积分图
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
"""
============= ================================================
        Argument      Description
        ============= ================================================
        *X*, *Y*, *Z* Data values as 2D arrays
        *rstride*     Array row stride (step size), defaults to 10
        *cstride*     Array column stride (step size), defaults to 10
        *color*       Color of the surface patches
        *cmap*        A colormap for the surface patches.
        *facecolors*  Face colors for the individual patches
        *norm*        An instance of Normalize to map values to colors
        *vmin*        Minimum value to map
        *vmax*        Maximum value to map
        *shade*       Whether to shade the facecolors
        ============= ================================================
"""

ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
"""
==========  ================================================
        Argument    Description
        ==========  ================================================
        *X*, *Y*,   Data values as numpy.arrays
        *Z*
        *zdir*      The direction to use: x, y or z (default)
        *offset*    If specified plot a projection of the filled contour
                    on this position in plane normal to zdir
        ==========  ================================================
"""
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-2, 2)

plt.show()

