# pandas 的选择数据

import numpy as np
import pandas as pd

dates = pd.date_range('20260101',periods=8)
df1 = pd.DataFrame(np.arange(32).reshape((8,4)),index=dates,columns=['A','B','C','D'])
print(df1)

print()
print(df1['A'])  # 输出列A的数据
print()
print(df1.A)  # 同义，输出列A的数据

print()
print(df1[2:5])  # 输出第3至第5行的数据
print()
print(df1['20260103':'20260105'])  # 输出第3至第5行的数据

# 高级形式，select by label:loc
# loc是取行数据，直接[]是取列数据
print()
print(df1.loc['20260104'])  # 用loc[]根据行标签'20260104'选择数据
print(df1.loc[:,['A','B']])  # 用loc[]根据所有行标签:，和列标签A','B'选择数据
print(df1.loc['20260108',['A','B']])  # 用loc[]根据行标签'20260108'，和列标签A','B'选择数据

# 高级形式2，select by position:iloc
print()
print(df1.iloc[3])  # 用iloc[]选择位置在第4行的数据
print(df1.iloc[3,2])  # 用iloc[]选择位置在第4行第3位的数据
print(df1.iloc[3:6,1:3])  # 切片，用iloc[]选择位置在第4~6行、第2~3位的数据
print(df1.iloc[[0,2,7],1:3])  # 切片，不连续筛选

# 高级形式3，结合local和position进行筛选，mixed selection:ix
# ix已经被弃用了，现在loc就可以标签位置双指了QwQ
print()
print(df1.loc['20260103'].iloc[0])  # 先用loc[]筛选指定标签'20260103'的数据，再用iloc[]筛选位置是第1位的数据

# 对数据框df1进行是True和否False的筛选，Boolean indexing
print()
print(df1)
print(df1[df1.A>8])  # 从数据框df1中筛选列A大于8的数据
