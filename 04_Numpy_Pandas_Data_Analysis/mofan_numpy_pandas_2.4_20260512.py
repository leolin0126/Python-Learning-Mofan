# numpy 的基础运算 2

import numpy as np

A1 = np.arange(2,14).reshape((3,4))
print(A1)
print(np.argmin(A1))  # argmin表示使得函数取最小值时的变量值
print(np.argmax(A1))  # argmax表示使得函数取最大值时的变量值
print(np.mean(A1))  # 数组A1的平均值
print(np.average(A1))  # 数组A1的平均值 

# mean()计算平均数，average()可以计算加权平均数

print(np.median(A1))  # 数组A1的中位数
print(np.cumsum(A1))  # 累加，累积和
print(np.diff(A1))  # 差值，离散差分
print(np.nonzero(A1))

A2 = np.arange(14,2,-1).reshape((3,4))
print(A2)            
print(np.sort(A2))  # 按行排序，默认axis==-1
print(A2.flatten())  # 展平数组，数字按从大到小排列
print(A2.flatten().reshape((3,4)))  # 展平数组，数字按从大到小排列，重排为3行4列的矩阵

# 按列升序排序（axis=0）
col_sorted = np.sort(A2, axis=0)
print("按列升序排序：")
print(col_sorted)

# 按列降序排序
col_sorted_desc = np.sort(A2, axis=0)[::-1]
print("按列降序排序：")
print(col_sorted_desc)

# 整体降序排序（先升序，再反转）
flat_desc = np.sort(A2.flatten())[::-1]
print("整体降序排序结果：")
print(flat_desc.reshape((3,4)))

print(np.transpose(A2))  # 转置数组A2并输出

A3 = np.transpose(A2)  # 转置数组A2
print(A3@A2)  # 数组A3和数组A2的矩阵乘法，输出结果为4×4的矩阵

print(np.clip(A1,5,9))  # 截取数组A1，令小于5的元素等于5，令大于9的元素等于9，保留5至9之间的元素
print(np.clip(A2,5,9))  # 截取数组A2，令小于5的元素等于5，令大于9的元素等于9，保留5至9之间的元素

print(np.mean(A1,axis=0))  # 对每一列求平均值
print(np.mean(A1,axis=1))  # 对每一行求平均值
