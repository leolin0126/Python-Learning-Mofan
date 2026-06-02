# numpy的基础运算

import numpy as np

a1 = np.array([10,20,30,40])
b1 = np.arange(4)
print(a1,b1)

c1 = a1 - b1  # numpy的减法
print(c1)

c2 = a1 + b1  # numpy的加法
print(c2)

c3 = a1 * b1  # numpy的乘法
print(c3)

c4 =10 * np.sin(a1)  # numpy计算三角函数sin，输入为弧度制，不是角度
print(c4)  # 输出的结果为数值

# 如果你有角度制的角度（如 30°、45°），需要先转换成弧度制再传入。
# NumPy 提供了 np.radians() 函数进行转换，或者手动计算 角度 * π / 180。

# 正确：输入弧度
print(np.sin(np.pi / 2))   # 输出 1.0

# 错误：输入度数 90°，结果不对（因为 90 被当作弧度）
print(np.sin(90))           # 输出 0.893996... 不是 1

# 正确方式：将度数转为弧度
print(np.sin(np.radians(90)))   # 输出 1.0

print(b1)
print(b1<3)
print(b1==3)

a2 = np.array([[1,2,3],
               [2,4,6],
               [3,5,7]])
b2 = np.arange(9).reshape((3,3))

c2 = a2 * b2
c2_dot = np.dot(a2,b2)

print(c2)  # 结果为逐个元素相乘
print(c2_dot)  # 结果为矩阵乘法运算结果

# 根据 NumPy 的‌广播规则‌，两个数组要能进行逐元素运算，必须满足以下条件之一：
# 维度相同，且每个维度的大小相等；
# 或者，从右往左逐位比较，每个维度上‌要么相等，要么其中一个为 1‌。
# ValueError: operands could not be broadcast together with shapes (2,3) (3,2)

a3 = np.array([[1,2,3],
               [4,5,6]])
b3 = np.array([[7,8],
               [9,10],
               [11,12]])

c3 = a3 @ b3
print(c3)

a4 = np.random.random((2,4))  # random模块下的random方法
print(a4)
print(np.sum(a4))
print(np.min(a4))
print(np.max(a4))
print(np.sum(a4,axis=1))  # axis=1，对每一行求和
print(np.sum(a4,axis=0))  # axis=0，对每一列求和

