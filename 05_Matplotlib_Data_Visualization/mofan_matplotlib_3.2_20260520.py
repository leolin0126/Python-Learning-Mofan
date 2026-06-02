# Bar 柱状图

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

# a1 = np.array([0,1,2,0,1,2,0,1,2,0,1,2]).reshape((4,3))
# b1 = np.array([0,0,0,10,10,10,20,20,20,30,30,30]).reshape((4,3))
# c1 = a1 + b1
# print(c1)

n = 12
X = np.arange(n) 
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

# 从一个均匀分布[low,high)中随机采样，定义域是左闭右开

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):  # zip()的作用，把变量X和Y1打包传递给变量x，y，以便添加对应的标注
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0, -y - 0.05, '-%.2f' % y, ha='center', va='top')

# zip 在 3.7 版本 返回生成器，应该用z1 = list（zip(x,y1)）

plt.xlim(-.5, n)
# plt.xticks(())
plt.ylim(-1.25, 1.25)
# plt.yticks(())

plt.show()
