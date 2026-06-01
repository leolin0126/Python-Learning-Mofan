# Matplotlib 中 figure 的使用

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

x1 = np.linspace(-10,10,50)
y1 = 2*x1 + 1
y2 = x1**2

plt.figure()  # 生成一个图表，Figure1
plt.plot(x1,y1)  # Figure1中包含哪些数据
plt.figure(num=5)  # 生成另一个图表，Figure2
# plt.plot(x1,y1)
plt.plot(x1,y2,color='red',linewidth=1.5,linestyle='--')  # Figure2中包含哪些数据
plt.show()

# plt.figure()的部分参数：
# num=，图表的数字，如Figure 3、Figure 5；
# figsize=，图表的尺寸，长（cm）*宽（cm）

# plt.plot()的部分参数：
# color=，线条颜色；linewidth=，线段粗细；linestyle=，线段形式；
