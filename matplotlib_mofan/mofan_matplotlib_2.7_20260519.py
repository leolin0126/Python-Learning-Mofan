# Figure中的坐标轴刻度 axis tick

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

# ---------------------
# 这三行 = 永久解决中文方框
# ---------------------
# plt.rcParams['font.family'] = ['Microsoft YaHei']
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False

x1 = np.linspace(-10,10,50)
y1 = 5*x1 + 25

plt.figure(num=3,figsize=(8,5),)
plt.plot(x1,y1)

# 坐标轴设置
plt.xlim((-7.5,7.5))  # X轴取值范围
plt.ylim((-60,100))  # Y轴取值范围
plt.xlabel('X axis')  # X轴名称
plt.ylabel('Y axis')  # Y轴名称

new_ticks = np.linspace(-12,12,13)  # 更改X轴的刻度线标记
print(new_ticks)
plt.xticks(new_ticks)

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')  # 右轴颜色设为无
ax.spines['top'].set_color('none')  # 上轴颜色设为无

ax.xaxis.set_ticks_position('bottom')  # 把下轴设定为X轴
ax.yaxis.set_ticks_position('left')  # 把左轴设定为Y轴
# ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]

ax.spines['bottom'].set_position(('data',0))  # 把X轴（bottom轴）设在Y轴的'0'上
ax.spines['left'].set_position(('data',0))  # 把Y轴（left轴）设在X轴的'0'上

# 调整刻度线标记
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)  # 设置刻度线标记的字体大小
    label.set_bbox(dict(facecolor='white', edgecolor='black', alpha=0.8, zorder=2))

plt.show()



# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 9 - tick_visibility
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""
