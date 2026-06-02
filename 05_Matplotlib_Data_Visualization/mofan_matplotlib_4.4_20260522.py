# secondary axis 次坐标

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

plt.figure()
x = np.arange(0,10,0.1)
y1 = 0.05*x**2
y2 = -1*y1

ax1 = plt.subplot()  # 创建一个图形窗口（figure）和一个坐标轴对象（ax1），使用默认设置（单图）
ax2 = ax1.twinx()  # 创建次坐标轴 ax2，与 ax1 共享 x 轴，但 y 轴独立（位于右侧）
ax1.plot(x,y1,color='blue')
ax2.plot(x,y2,color='green',linestyle='--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='b')
ax2.set_ylabel('Y2 data', color='g')

plt.show()

