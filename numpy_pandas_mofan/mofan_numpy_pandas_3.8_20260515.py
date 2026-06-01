# pandas 数据可视化/数据图表化

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')  # 不弹窗、保存图片

# plot data

# Series
# data = pd.Series(np.random.randn(1000), index=np.arange(1000))  # 生成1000个随机数，横轴X轴最大是1000
# data = data.cumsum()  # 把生成的1000个随机数累加
# data.plot()  # 计算结果存储在data.plot中

# # 保存到你能找到的地方
# plt.savefig(r"E:\lesson\matplotlib\lesson_plot_01.png", dpi=300)
# plt.close()

# print("✅ 图片已生成：E:\\lesson\\matplotlib\\lesson_plot_01.png")

# DataFrame
data2 = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))  # 创建一个 1000 行 × 4 列 的 pandas 数据表（DataFrame），里面填充随机正态分布数据。
data2 = data2.cumsum()  # 把生成的1000个随机数累加
data2.plot()  # 计算结果存储在data.plot中

# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', scatter','hexbin', 'pie'
# 'bar'      柱状图
# 'hist'     直方图（看分布）
# 'box'      箱型图（看异常值）
# 'kde'      密度图（看分布曲线）
# 'area'     面积图
# 'scatter'  散点图（你现在用的）
# 'hexbin'   六边形密度图
# 'pie'      饼图
ax = data2.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data2.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax)  # ax=ax 表示：画在同一张图里，不新建画布！

# 保存到你能找到的地方
plt.savefig(r"E:\lesson\matplotlib\lesson_plot_03.png", dpi=300)
plt.close()

print("✅ 图片已生成：E:\\lesson\\matplotlib\\lesson_plot_03.png")








