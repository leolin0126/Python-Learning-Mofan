# animation 动画

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

fig,ax = plt.subplots()  # 创建图形窗口 figure 和一个坐标轴 ax

x = np.arange(0,2*np.pi,0.01)  # 生成 x 数组：从 0 到 2π，步长 0.01（共约 628 个点）
line, = ax.plot(x,np.sin(x))  # 绘制初始的正弦曲线（sin(x)）；ax.plot 返回一个包含线条对象的列表， 
                              # 用逗号解包将第一个（也是唯一）线条对象赋值给 line

def animate(i):  # 定义动画的更新函数，i 为帧索引
    line.set_ydata(np.sin(x+2*i/10))   # 更新线条的 y 数据：改变正弦波的相位（每帧增加 0.1 弧度）
    return line,  # 返回需要重绘的图形对象（逗号表示返回一个元组）

def init():  # 定义初始化函数（用于动画开始前的第一帧）
    line.set_ydata(np.sin(x))  # 将线条 y 数据重置为 sin(x)
    return line,  # 返回线条对象

ani = animation.FuncAnimation(fig=fig,  # 指定动画所在的 figure
                              func=animate,  # 指定每帧调用的更新函数
                              frames=100,  # 总帧数（动画将运行 100 帧）
                              init_func=init,  # 指定初始化函数（可选）
                              interval=20,  # 每两帧之间的间隔（毫秒），20ms 对应 50 帧/秒
                              blit=False)  # 是否使用 blit 技术（只重绘变化部分），False 表示重绘整个区域


plt.show()


