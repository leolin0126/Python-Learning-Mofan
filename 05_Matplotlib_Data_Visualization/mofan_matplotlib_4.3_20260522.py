# plot in plot 图中图

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

# 先做大图
fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left,bottom,width,height = 0.1,0.1,0.8,0.8  # 百分比形式设定大图的大小
ax1 = fig.add_axes([left,bottom,width,height])  # 传递参数
ax1.plot(x,y,color='red')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_title('ax1 title')

# 再做小图1
left,bottom,width,height = 0.2,0.55,0.25,0.25  # 百分比形式设定大图的大小
ax2 = fig.add_axes([left,bottom,width,height])  # 传递参数
ax2.plot(x,y,color='blue')
ax2.set_xlabel('X axis') 
ax2.set_ylabel('Y axis')
ax2.set_title('inside1 title')

# 再做小图2
plt.axes([0.6,0.2,0.25,0.25])
plt.plot(y[::-1], x, 'g')  # 这里y[::-1]表示从后往前，间隔为-1，等价于list(reversed(y))
plt.xlabel('x')
plt.ylabel('y')
plt.title('inside2 title')

plt.show()

# 切片语法回顾
# [start:stop:step]：
# start：起始索引（包含），默认为开头（正步长）或结尾（负步长）
# stop：结束索引（不包含），默认为结尾（正步长）或开头（负步长）
# step：步长，正数向右，负数向左

# y[::-1] 的含义
# step = -1：从最后一个元素开始，每次向前移动一步，直到第一个元素。
# start 和 stop 都省略，表示遍历整个序列。
# 结果是一个反转后的新对象（不修改原 y）。





