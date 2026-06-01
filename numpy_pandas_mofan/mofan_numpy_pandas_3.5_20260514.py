# pandas 导入和导出数据

import numpy as np
import pandas as pd

# 读取表格
data = pd.read_excel('F:\\工作\\个人\\python_test_读取表格.csv')
print(data)

# 保存表格
data.to_excel('F:\\工作\\个人\\python_test_读取表格.xls')








