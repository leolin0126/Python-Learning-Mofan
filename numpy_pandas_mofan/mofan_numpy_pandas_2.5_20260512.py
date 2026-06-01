# numpy的索引

import numpy as np

A1 = np.arange(3,18).reshape((3,5))
print(A1)
print(A1[2])
print(A1[1][1])
print(A1[1,1])
print(A1[2,:])  # 输出第3行整行的元素
print(A1[:,2])   # 输出第3列整列的元素
print(A1[1,1:3])   # 输出第2行从第2个到第3个的元素，1:3，为左闭右开的区间[1,3)
print(A1[1,1:5])   # 输出第2行从第2个到第5个的元素，1:5，为左闭右开的区间[1,5)

for row in A1:  # 用for...in循环迭代输出矩阵A1的 每一行 元素
    print(row)

for column in A1.T:  # 用for...in循环迭代输出矩阵A1的 每一列 元素，A1.T=np.transpose(A1)
    print(column)

for column in np.transpose(A1):  # 用for...in循环迭代输出矩阵A1的 每一列 元素，A1.T=np.transpose(A1)
    print(column)

for item in A1.flatten():  # 用for...in循环迭代输出矩阵A1的 每一个 元素，A1.flatten()含义为展平矩阵A1
    print(item)

for item in A1.flat:  # 用for...in循环迭代输出矩阵A1的 每一个 元素，A1.flat=A1.flatten()
    print(item)



 