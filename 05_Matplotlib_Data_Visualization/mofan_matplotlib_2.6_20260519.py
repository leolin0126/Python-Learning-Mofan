# Figure中的标注 Annotation

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

# 给曲线上的某个点添加标注
x10 = 6
y10 = 5*x10 + 25
plt.scatter(x10,y10,s=50,color='red')
plt.plot([x10,x10],[y10,0],color='black',linewidth=2.5,linestyle='--')
# linewidth=2.5可简写成lw=2.5，color='black',linestyle='--'可简写成'k--'

# ---------------
# 添加标注annotation的方法一
# ---------------
plt.annotate(r'$5x1+25=%s$' % y10,  # 1. 要显示的文字，注释文本
             xy=(x10, y10),  # 2. 箭头指向哪里，被指向的点（箭头终点）
             xycoords='data',  # 3. 箭头坐标用什么单位，xy 的坐标系
             xytext=(+30, -30),  # 4. 文字放在哪里，文本起始位置（相对于 xy 的偏移）
             textcoords='offset points',  # 5. 文字坐标用什么单位，xytext 的坐标系
             fontsize=16,  # 6. 文字大小，字体大小
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2")  #7. 箭头样式 
             )

# r''是row string的意思，不是正则表达式。r是原生字符串的意思，表示忽视转义，看做它本来的符号

# ---------------
# 添加标注annotation的方法二
# ---------------
plt.text(-14, 70, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16,'color': 'red'})

plt.text(-14, 30, r'This is the some text.',
         fontdict={'size': 16,'color': 'red','family':'Times New Roman'})

plt.show()





