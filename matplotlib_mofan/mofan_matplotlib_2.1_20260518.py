# Matplotlib的基本用法

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

x1 = np.linspace(-10,10,50)
y1 = 2*x1 + 1
plt.plot(x1,y1)
plt.show()

# 保存到你能找到的地方
# plt.savefig(r"E:\lesson\matplotlib\matplotlib_2.1_01.png", dpi=300)
# plt.close()




