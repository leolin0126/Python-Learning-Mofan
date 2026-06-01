# Matplotlib 中 Figure 的坐标轴设置1

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
curve1, = plt.plot(x1,y2,label='curve_01')
curve2, = plt.plot(x1,y1,color='red',linewidth=2.5,linestyle='--',label='curve_02')  
# label=，添加图例
# the "," is very important in here l1, = plt... and l2, = plt... for this step

plt.legend(handles=[curve1,curve2,],labels=['aaa','bbb'],loc='lower right')  # 显示特定参数的图例

# 坐标轴设置
plt.xlim((-7.5,7.5))  # X轴取值范围
plt.ylim((-60,120))  # Y轴取值范围
plt.xlabel('X axis')  # X轴名称
plt.ylabel('Y axis')  # Y轴名称

new_ticks = np.linspace(-10,12,12)  # 更改X轴的刻度线标记
print(new_ticks)
plt.xticks(new_ticks)
# plt.yticks([-60,-40,-20,0,20,40,60],
#            [r'$really\ bad$','pretty bad','bad','normal','good','quite good','damn good'])

# plt.legend()  # 显示图例
plt.show()  # 生成图表

# handles=[]，是plt.plot()的返回值，注意代表plt.plot()的变量要加逗号，表示句柄
# 加逗号是因为返回的是list,需要从list中获取handle
# labels=[]，是handles中对应的图例的名称
# loc='',表示图例的位置，除了'best',还可以是'upper left'、'lower right'
# #     The *loc* location codes are::

#           'best' : 0,          (currently not supported for figure legends)
#           'upper right'  : 1,
#           'upper left'   : 2,
#           'lower left'   : 3,
#           'lower right'  : 4,
#           'right'        : 5,
#           'center left'  : 6,
#           'center right' : 7,
#           'lower center' : 8,
#           'upper center' : 9,
#           'center'       : 10,"""

# r'$really\ bad$',可以更改刻度线标记的字体，也可以使用LaTex公式语法等转变为其他。
# \alpha，可读出希腊字母α




