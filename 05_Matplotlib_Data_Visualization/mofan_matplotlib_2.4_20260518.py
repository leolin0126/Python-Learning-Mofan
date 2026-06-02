# Matplotlib 中 Figure 的坐标轴设置2

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

# ---------------------
# 这三行 = 永久解决中文方框
# ---------------------
plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

x1 = np.linspace(-10,10,50)
y1 = 5*x1 + 25
y2 = x1**2

plt.figure()
plt.plot(x1,y2)
plt.plot(x1,y1,color='red',linewidth=2.5,linestyle='--')  

# 坐标轴设置
plt.xlim((-7.5,7.5))  # X轴取值范围
plt.ylim((-60,120))  # Y轴取值范围
plt.xlabel('X轴名称：X')  # X轴名称
plt.ylabel('Y轴名称：Y')  # Y轴名称

new_ticks = np.linspace(-10,12,12)  # 更改X轴的刻度线标记
print(new_ticks)
plt.xticks(new_ticks)
# plt.yticks([-60,-40,-20,0,20,40,60],
#            [r'$really\ bad$','pretty bad','bad','normal','good','quite good','damn good'])

# r'$really\ bad$',可以更改刻度线标记的字体，也可以使用LaTex公式语法等转变为其他。
# \alpha，可读出希腊字母α

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')  # 右轴颜色设为无
ax.spines['top'].set_color('none')  # 上轴颜色设为无

ax.xaxis.set_ticks_position('bottom')  # 把下轴设定为X轴
ax.yaxis.set_ticks_position('left')  # 把左轴设定为Y轴
# ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]

ax.spines['bottom'].set_position(('data',0))  # 把X轴（bottom轴）设在Y轴的'0'上
ax.spines['left'].set_position(('data',0))  # 把Y轴（left轴）设在X轴的'0'上

# set_position(('data',0))中的'data'，还可以是：
# outward，将边框从默认位置向外（远离绘图区域）移动指定的点数
# axes，定位在轴的百分比位置

# the 1st is in 'outward' | 'axes' | 'data'
# axes: percentage of y axis
# data: depend on y data

plt.show()


