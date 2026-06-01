# subplot in grid 多个分格显示

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
# matplotlib.use('Agg')  # 不弹窗、保存图片
matplotlib.use('Qt5Agg')  # 👈 就这一行！替换掉 Agg

# # method 1: subplot2grid
# # -----------------------------
# plt.figure()
# ax1 = plt.subplot2grid((3, 3),(0, 0),colspan=3,rowspan=1) 
# # (3, 3)，画布分为3行3列共9格，
# # (0, 0)，第一个图表从画布的第1行第1列开始
# # colspan=3，第一个图表横跨第1行的3列
# # rowspan=1,第一个图表占用第1行
# ax1.plot([0.5,8.5], [0.5,1.5])
# ax1.set_title('ax1_title')
# ax1.set_xlim((0,9))
# ax1.set_xlabel('ax1_X_axis')
# # 同理，plt.xlim() 改为ax1.set_xlim()，plt.xlabel()改为ax1.set_xlabel()
# ax2 = plt.subplot2grid((3, 3),(1, 0),colspan=2,rowspan=1)
# ax3 = plt.subplot2grid((3, 3),(1, 2),colspan=1,rowspan=2)
# ax4 = plt.subplot2grid((3, 3),(2, 0),colspan=1,rowspan=1)
# ax4.scatter([1, 2], [2, 2])
# ax4.set_xlabel('ax4_x')
# ax4.set_ylabel('ax4_y')
# ax5 = plt.subplot2grid((3, 3), (2, 1))


# # method 2: gridspec
# # -----------------------------
# plt.figure()
# gs = gridspec.GridSpec(3, 3)
# # use index from 0
# ax6 = plt.subplot(gs[0, :])
# ax6.set_title('ax6_title')
# ax7 = plt.subplot(gs[1, :2])
# ax7.set_title('ax7_title')
# ax8 = plt.subplot(gs[1:, 2])
# ax8.set_title('ax8_title')
# ax9 = plt.subplot(gs[-1, 0])  # 等价于 gs[2, 0]：取最后一行、第一列的子图。
# ax9.set_title('ax9_title')
# ax10 = plt.subplot(gs[-1, -2])  # 等价于 gs[2, 1]：取最后一行、倒数第二列（即第二列）的子图。
# ax10.set_title('ax10_title')


# method 3: easy to define structure
# # -----------------------------
f,((ax11,ax12),(ax13,ax14)) = plt.subplots(2, 2, sharex=False, sharey=False)
ax11.scatter([1,2], [1,2])

# (ax11,ax12)，定义第一行的格式
# (ax13,ax14)，定义第一行的格式
# sharex=True,共享X轴
# sharey=True,共享Y轴

plt.tight_layout()
plt.show()









