# numpy中 array 的分割

import numpy as np

A1 = np.arange(10,34,2).reshape((3,4))
print(A1)

# axis=1,行不变，列变；axis=0,行变，列不变
# axis=0，对列操作；axis=1，对行操作

print(np.split(A1,2,axis=1))
print()
print(np.split(A1,3,axis=0))

# split()函数只能进行均等的分割

print(np.array_split(A1,3,axis=1))
# array_split()函数进行不等分割
# 总数L分成n个部分，分法是L除以n取余个大小为L除以n取商 + 1的数组，其余大小为L除以n取商

print(np.vsplit(A1,3))  # vertical split，上下分割（横切）
print(np.hsplit(A1,2))  # horizontal stack，左右分割（竖切）

# 按列块分割：1列、2列、1列
col_blocks = np.hsplit(A1, [1, 3])
print("\n第一块 (1列):\n", col_blocks[0])
print("第二块 (2列):\n", col_blocks[1])
print("第三块 (1列):\n", col_blocks[2])

# 方法：np.hsplit(A1, [1, 3])
# [1, 3] 表示在索引 1 和索引 3（即第 2 列之前和第 4 列之前）的位置切开。
# 结果是一个由三个子数组组成的列表：
# 第一块：索引 0 列（宽度 1）
# 第二块：索引 1～2 列（宽度 2）
# 第三块：索引 3 列（宽度 1）



