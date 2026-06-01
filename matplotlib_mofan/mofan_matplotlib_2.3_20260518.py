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
plt.plot(x1,y2)
plt.plot(x1,y1,color='red',linewidth=2.5,linestyle='--')  

# 坐标轴设置
plt.xlim((-7.5,7.5))  # X轴取值范围
plt.ylim((-60,60))  # Y轴取值范围
plt.xlabel('X轴名称：X')  # X轴名称
plt.ylabel('Y轴名称：Y')  # Y轴名称

new_ticks = np.linspace(-10,10,11)  # 更改X轴的刻度线标记
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-60,-40,-20,0,20,40,60],
           [r'$really\ bad$','pretty bad','bad','normal','good','quite good','damn good'])

# r'$really\ bad$',可以更改刻度线标记的字体，也可以使用LaTex公式语法等转变为其他。
# \alpha，可读出希腊字母α

plt.show()


