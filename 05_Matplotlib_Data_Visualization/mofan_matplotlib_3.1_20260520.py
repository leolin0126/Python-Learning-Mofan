# Scatter 散点图

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

n = 1024
x1 = np.random.normal(0,1,n)  # 生成1024个，符合(0,1)的正态分布的随机数
y1 = np.random.normal(0,1,n)  # 生成1024个，符合(0,1)的正态分布的随机数
T = np.arctan2(y1, x1)    # for color later on

plt.scatter(x1, y1, s=75, c=T, alpha=.5,edgecolor='black',cmap='rainbow')  # 散点图及参数设置

plt.xlim(-1.5, 1.5)  # X轴取值范围
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)  # Y轴取值范围
plt.yticks(())  # ignore yticks

plt.show()

# 颜色不一样是你cmap默认设置不同（建议用chatgpt辅助学习，不会的代码问chatgpt）

