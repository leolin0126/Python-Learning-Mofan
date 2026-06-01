# pandas 处理丢失数据

import numpy as np
import pandas as pd

dates = pd.date_range('20260101',periods=8)
df1 = pd.DataFrame(np.arange(32).reshape((8,4)),index=dates,columns=['A','B','C','D'])
print('原始矩阵：')
print(df1)

# 假设矩阵丢失了其中的一些数据
df1.iloc[2,0] = np.nan
df1.iloc[4,1] = np.nan
df1.iloc[6,2] = np.nan
print('\n部分数据丢失后的矩阵：')
print(df1)

# 丢弃已丢失的数据 
# print('\n执行dropna(axis=0,how=\'any\')命令后的矩阵：')
# print(df1.dropna(axis=0,how='any'))
# axis=0,按行丢弃；axis=1,按列丢弃
# how='any'，表示行有任意一个数据丢失就整行丢掉
# how='all'，表示行的所有数据均丢失时才整行丢掉

# 重新填上已丢失的数据
print(df1.fillna(value=111))

# 检查矩阵中是否有丢失的数据（矩阵或数据表庞大时使用）
print(df1.isnull())  # 结果反馈True或False，判断数据是否丢失
print(np.any(df1.isnull())==True)  # 表格数据更庞大时，返回是否至少有一个数据丢失为True


