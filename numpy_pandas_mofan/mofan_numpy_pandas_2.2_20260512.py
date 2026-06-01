# numpy中创建各种形式的数组array

import numpy as np

a1 = np.array([2,23,4])  # 输出数组a1，与列表相比，输出没有逗号
print(a1)

a2 = np.array([2,23,4],dtype=int)  # 输出数组a2，用dtype定义为整数，注：np.int在新版本中已被弃用，可以直接用int
print(a2.dtype)  # 输出int32（默认32位？）

a3 = np.array([2,23,4],dtype=np.int64)  # 输出数组a3，用dtype定义为整数，注：np.int在新版本中已被弃用，可以直接用int
print(a3.dtype)  # 输出int64

a4 = np.array([2,23,4],dtype=float)  # 输出数组a4，用dtype定义为浮点数，注：np.int在新版本中已被弃用，可以直接用int
print(a4.dtype)  # 输出float64（默认64位？）

b1 = np.array([[2,23,4],  # 生成矩阵b1
               [5,45,8]])
print(b1)

b2 = np.zeros((3,4))  # 生成若干行（案例为3）、若干列（案例为4）的全为0的矩阵
print(b2)  # 输出浮点数矩阵（numpy默认输出浮点数）

b3 = np.ones((3,4))  # 生成若干行（案例为3）、若干列（案例为4）的全为1的矩阵
print(b3)  # 输出浮点数矩阵（numpy默认输出浮点数）

b4 = np.empty((2,4))  # 生成2行5列的接近为0的矩阵
print(b4)  # 输出浮点数矩阵（numpy默认输出浮点数）

b5 = np.arange(10,20,2)  # 生成有序数组b5,arange()函数类似于range()函数
print(b5)  # 输出结果[10 12 14 16 18]

b6 = np.arange(12).reshape((3,4))  # 生成有序数组b6,并重排为3行4列的矩阵
print(b6)

b7 = np.linspace(1,10,5)  #生成线段，区间[1,10]，分成4段5点
print(b7)

# 弹幕与评论：
# int默认是32 float 默认是64。。。
# 其他dtype的形式：complex64，128，256；bool；object；int8，16，32，64；float16，32，64，128；Unicode_








