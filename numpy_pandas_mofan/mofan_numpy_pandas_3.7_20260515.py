# pandas的合并 merge

import numpy as np
import pandas as pd

# merging two df by key/keys.(may be used in database)
# simple example

left1 = pd.DataFrame({'key':['K0','K1','K2','K3'],
                      'A':['A0','A1','A2','A3'],
                      'B':['B0','B1','B2','B3']})
right1 = pd.DataFrame({'key':['K0','K1','K2','K3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})
print('原始矩阵：')
print(left1)
print()
print(right1)

result1 = pd.merge(left1,right1)
print('\nmerge功能合并矩阵，左右合并：')
print(result1)

# merge功能，指定特定index或column进行合并
result2 = pd.merge(left1,right1,on='key')
print('\nmerge功能，指定特定index或column进行合并：')
print(result2)

# consider two keys
left2 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print('\nconsider two keys,原始矩阵：')
print(left2)
print()
print(right2)

result3 = pd.merge(left2,right2,on=['key1','key2'],how='inner')
print('\nconsider two keys的合并，默认以inner形式，合并同类项：')
print(result3)

result4 = pd.merge(left2,right2,on=['key1','key2'],how='outer')
print('\nconsider two keys的合并，以outer形式:')
print(result4)

result5 = pd.merge(left2,right2,on=['key1','key2'],how='left')
print('\nconsider two keys的合并，以how=\'left\'形式：')
print(result5)

result6 = pd.merge(left2,right2,on=['key1','key2'],how='right')
print('\nconsider two keys的合并，以how=\'right\'形式：')
print(result6)

# 同样地，是合并同类项，缺失的部分以NaN填充

# indicator,默认参数是False
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print('\nindicator，原始矩阵：')
print(df1)
print()
print(df2)
result7 = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print('\nindicator,合并2个矩阵：')
print(result7)

# give the indicator a custom name
result8 = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print('\nindicator,give the indicator a custom name：')
print(result8)

# merged by index
left3 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])
right3 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                       'D': ['D0', 'D2', 'D3']},
                       index=['K0', 'K2', 'K3'])
print('\nmerged by index,原始矩阵：')
print(left3)
print()
print(right3)

# left_index and right_index
result9 = pd.merge(left3, right3, left_index=True, right_index=True, how='outer')
print()
print(result9)

result10 = pd.merge(left3, right3, left_index=True, right_index=True, how='inner')
print()
print(result10)

# handle overlapping,对名字相同但内容不同的数据，用suffixes=[]加以区分
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
result11 = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print('\nhandle overlapping,原始矩阵：')
print(boys)
print()
print(girls)
print('\n对名字相同但内容不同的数据，用suffixes=[]加以区分：')
print(result11)

# join function in pandas is similar with merge. If know merge, you will understand join










