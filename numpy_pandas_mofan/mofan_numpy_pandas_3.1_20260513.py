# pandas 基本介绍

import numpy as np
import pandas as pd

s1 = pd.Series([1,3,6,np.nan,44,1])
print(s1)

dates = pd.date_range('20260513',periods=8)
print()
print(dates)

df = pd.DataFrame(np.random.randn(8,4),index=dates,columns=['a','b','c','d'])
print()
print(df)
# pd.DataFrame是一个大矩阵，相当于2维的numpy
# np.random.randn(8,4)是numpy的数据,randn是产生随机数，这些随机数服从正态分布
# index=dates是行的索引
# columns=['a','b','c','d']是列的索引

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print()
print(df1)

df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20260101'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print()
print(df2)
# 字典中各参数的含义：
# 'A'、'B'、'C'、'D'、'E'、'F'：表格中列的名称
# 0、1、2、3：行的名称，默认用0123等数字排列
print()
print(df2.dtypes)  # 输出数据框df2中每列的数据类型
print(df2.index)  # 输出数据框df2中每行的标签/名字
print(df2.columns)  # 输出数据框df2中每列的标签/名字
print(df2.values)  # 输出数据框df2中每个值
print(df2.describe())  # 描述数据框df2(只能运算数字形式)
print()
print(df2.transpose())  # 转置
print()
print(df2.sort_index(axis=1,ascending=False))  # axis=1,行不变，按列进行排列，ascending=False，降序排列
print()
print(df2.sort_index(axis=0,ascending=False))  # axis=0,列不变，按行进行排列，ascending=False，降序排列
print()
print(df2.sort_values(by='E'))  # 按E列的值为顺序进行排序

