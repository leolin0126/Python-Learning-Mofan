# pandas的合并 concatenating

import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*5,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*10,columns=['a','b','c','d'])
print('原始矩阵：')
print(df1)
print()
print(df2)
print()
print(df3)

# axis=0,行变列不变，进行上下合并（纵向合并）；
# axis=1,行不变列变，进行左右合并（横向合并）；
result1 = pd.concat([df1,df2,df3],axis=0)
print('\n3个DataFrame纵向合并后矩阵：')
print(result1)

# 纵向合并后行索引变成连续不重复的数字
result2 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print('\n纵向合并后行索引变成连续不重复的数字：')
print(result2)

# join功能（pd.concat()函数中的一个参数）
df4 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*12,columns=['c','d','e','f'],index=[2,3,4])
print('\n原始矩阵：')
print(df4)
print()
print(df5)

# join功能默认outer模式，缺失的部分用NaN填充
result3 = pd.concat([df4,df5],join='outer')
print('\njoin功能默认outer模式')
print(result3)

# join功能的inner模式则会裁减掉不重合的部分
result4 = pd.concat([df4,df5],join='inner')
print('\njoin功能的inner模式')
print(result4)

# join_axes功能（新版本中已删除）
result5 = pd.concat([df1,df2,df3],axis=1)
print('\n左右合并，axis=1')
print(result5)

# join_axes已经被弃用了，现在用reindex或者reindex_like
# 新版本删掉了join_axes，用merge代替了

# append功能
df6 = pd.DataFrame(np.ones((3,4))*3,columns=['a','b','c','d'])
df7 = pd.DataFrame(np.ones((3,4))*6,columns=['a','b','c','d'])
df8 = pd.DataFrame(np.ones((3,4))*9,columns=['b','c','d','e'],index=[2,3,4])

result6 = df6._append(df7,ignore_index=True)
print('\nappend功能，默认状态是在下方加数据')
print(result6)

# 可添加多个dataframe
result7 = df6._append([df7,df8],ignore_index=True)
print('\nappend功能，可添加多个dataframe')
print(result7)

# concat普适，join用于左右合并，append用于上下合并，join_axes和ignore_index可用于前面三者进行修饰。

# 只添加单行
df9 = pd.DataFrame(np.ones((3,4))*8,columns=['a','b','c','d'])
s1 = pd.Series([18,28,38,48],index=['a','b','c','d'])
result8 = df9._append(s1,ignore_index=True)
print('\nappend功能，只添加单行')
print(result8)

