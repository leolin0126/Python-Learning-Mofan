# numpy中 array 的合并

import numpy as np

A1 = np.array([1,1,1])
B1 = np.array([4,4,4])
C1 = np.array([9,9,9])

print(np.vstack((A1,B1,C1)))  # vertical stack，上下合并，合并数组A1、B1和C1

D1 = np.vstack((A1,B1,C1))
print(A1.shape,D1.shape)

# 这里(3,)表示这是一个一维数组，一般这种数据格式参与计算非常容易出错误 
# 这里的(3，)是因为shape返回tuple类型，单个元素情况下必须写逗号

D2 = np.hstack((A1,B1,C1))  # horizontal stack， 左右合并
print(D2)
print(A1.shape,D2.shape)

D3 = A1.reshape(-1,1)  # 更具备普适性，reshape(-1,1)函数，改变一维数组A1的形状，为一个3行1列的矩阵
print(D3)
print(D3.shape)

D4 = B1[np.newaxis,:]  # np.newaxis,: 表示在列上增加一个轴，：展示整列；如果是:,np.newaxis，表示在行上增加一个轴
print(D4)  # 输出结果[[4 4 4]]
print(D4.shape)  # 输出结果(1, 3)，即1行3列

D5 = B1[:,np.newaxis]  # np.newaxis,: 表示在列上增加一个轴，：展示整列；如果是:,np.newaxis，表示在行上增加一个轴
print(D5)  # 输出结果
print(D5.shape)  # 输出结果(3, 1)，即3行1列

D6 = A1[:,np.newaxis]
D7 = C1[:,np.newaxis]
D8 = np.hstack((D6,D5,D7))  # horizontal stack， 左右合并
print(D8)

D9 = np.concatenate((A1,B1,C1),axis=0)  # axis=0，在列的维度上合并；axis=1，在行的维度上合并
print(D9)
print(D9.shape)  # 输出结果(9,)，即表示有9个元素的一个一维数组
D10 = D9[np.newaxis,:]  # np.newaxis,: 表示在列上增加一个轴，：展示整列
print(D10)
print(D10.shape)  # 输出结果(1,9)，即1行9列

A2 = A1.reshape(-1,1)  # 转置A1为3行1列的矩阵A2
B2 = B1.reshape(-1,1)  # 转置B1为3行1列的矩阵B2
C2 = C1.reshape(-1,1)  # 转置C1为3行1列的矩阵C2
D11 = np.concatenate((A2,B2,C2),axis=0)  # 在列的维度合并A2、B2、C2，列数不变，成为9行1列的矩阵
print(D11)
print(D11.shape)  # 输出结果(9,1)，即9行1列
D12 = np.concatenate((A2,B2,C2),axis=1)  # 在行的维度合并A2、B2、C2，行数不变，成为3行3列的矩阵
print(D12)
print(D12.shape)  # 输出结果(3,3)，即3行3列



