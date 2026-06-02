# pandas 数据可视化/数据图表化

# import matplotlib
# print("matplotlib 安装成功！版本：", matplotlib.__version__)

# import matplotlib
# matplotlib.use('Agg')   # 👈 就改这一个单词！

# import matplotlib.pyplot as plt
# import numpy as np

# # 解决中文显示
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# x = np.linspace(0,10,100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.title("测试画图")

# # 保存图片，而不是弹出窗口
# plt.savefig(r"E:\lesson\test_plot.png")
# print("✅ 图片已保存！打开 test_plot.png 就能看到图")

# 3. 顺便给你一套不用弹窗、不报错、直接保存图片的完整可用代码

# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import numpy as np
# import os

# # 打印当前路径，方便找图片
# print(r"E:\lesson\test_plot_2.png", os.getcwd())

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.title("测试正弦曲线")
# plt.savefig(r"E:\lesson\test_plot_2.png")
# plt.close()  # 释放内存

# ✅ 最终完美代码（中文 100% 显示）

import matplotlib
matplotlib.use('Agg')  # 不弹窗、保存图片
import matplotlib.pyplot as plt
import numpy as np

# ---------------------
# 这三行 = 永久解决中文方框
# ---------------------
plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 画图
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("我是中文标题，正常显示！", fontsize=14)
plt.xlabel("X 轴", fontsize=12)
plt.ylabel("Y 轴", fontsize=12)

# 保存到你能找到的地方
plt.savefig(r"E:\lesson\matplotlib\final_plot_2.png", dpi=300)
plt.close()

print("✅ 图片已生成：E:\\lesson\\matplotlib\\final_plot_2.png")

