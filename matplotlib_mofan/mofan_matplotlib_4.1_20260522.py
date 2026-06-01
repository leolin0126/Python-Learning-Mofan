# subplot 多个显示

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

# plt.figure()

# plt.subplot(2,2,1)  # 把若干图表在一个画布中分为2行2列，然后指定第1个位置
# plt.plot([0,1],[0,1])  # 在第1个小图中添加[0, 1]的X轴和[0, 1]的Y轴

# plt.subplot(2,2,2)  # 在第2个位置添加图表
# plt.plot([0,2], [0,2])

# plt.subplot(2,2,3)  # 在第3个位置添加图表
# plt.plot([0,3], [0,3])

# plt.subplot(2,2,4)  # 在第4个位置添加图表
# plt.plot([0,4], [0,4])

plt.figure(figsize=(6, 4))

plt.subplot(2,1,1)  # figure splits into 2 rows, 1 col, plot to the 1st sub-fig
plt.plot([0,10],[0,10])  # 在第1个小图中添加[0, 1]的X轴和[0, 1]的Y轴

plt.subplot(2,3,4)  # figure splits into 2 rows, 3 col, plot to the 4th sub-fig
plt.plot([0,2], [0,2])

plt.subplot(2,3,5)  # figure splits into 2 rows, 3 col, plot to the 5th sub-fig
plt.plot([0,3], [0,3])

plt.subplot(2,3,6)  # figure splits into 2 rows, 3 col, plot to the 6th sub-fig
plt.plot([0,4], [0,4])



plt.show()


