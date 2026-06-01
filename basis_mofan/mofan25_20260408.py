# import 载入模块
# 导入模块time，输出当地时间
import time
print(time.localtime())

# 用简称代替全称较长的模块
print()
import time as t
print(t.localtime()) 

# 只使用模块中的某些特定功能
print()
from time import time,localtime
print(localtime())
print(time())

# 使用模块中的全部功能
print()
from time import *
print(localtime())
print(time())