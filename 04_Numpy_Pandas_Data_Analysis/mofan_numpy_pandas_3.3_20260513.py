# pandas 如何设置值/赋值 

import numpy as np
import pandas as pd

dates = pd.date_range('20260101',periods=8)
df1 = pd.DataFrame(np.arange(32).reshape((8,4)),index=dates,columns=['A','B','C','D'])
print(df1)

print()
df1.iloc[2,2] = 1111  # 用位置定位iloc[]将原数据框中第3行第3列的元素，从10改为1111
print(df1)

print()
df1.loc['20260106','D'] = 6666  # 用标签定位loc[]将原数据框中的23改为1111
print(df1)

# print()
# df1[df1.A>15] = 0  # 筛选出A>15的元素，并全部赋值为0
# print(df1)

# print()
# df1.A[df1.A>15] = 0  # 筛选出列A中A>15的元素，并把列A中符合筛选条件的元素全部赋值为0
# print(df1)

print()
df1['F'] = np.arange(100,900,100)  # 添加列F，arange()函数从100到800，步长为100
print(df1)

print()
df1['E'] = pd.Series([150,250,350,450,550,650,750,850],index=pd.date_range('20260101',periods=8))
print(df1)

# 添加列E，index=pd.date_range('20260101',periods=8表示与前面代码中的标签保持一致
# 或者不是Series也行，如 df['H'] =np.array(range(6))
# 可以直接df['E'] = [1, 2, 3, 4, 5, 6]加入新的一列E






