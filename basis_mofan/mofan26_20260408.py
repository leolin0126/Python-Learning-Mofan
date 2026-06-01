# 使用自定义的模块，将其导入python
# 方法1：适用于主程序文件与自定义模块文件在同一文件夹
import mymokuai1

mymokuai1.printdata('I am Python 1')

# 方法2：将自定义的模块放入python的默认文件夹（E:\Python v3810\Lib\site-packages）中，将其导入python
import mymokuai2

mymokuai2.printdata('I am Python 2')

# 方法3：使用 Python 自带的 sys 模块，手动告诉 Python 模块的文件夹位置

# 第一步：导入sys系统模块
import sys

# 第二步：添加【自定义模块所在的文件夹路径】
# 重点：用 r"" 原始字符串，写文件夹的绝对路径！
sys.path.append(r"E:\lesson\my_tools")

# 第三步：现在可以正常导入你的自定义模块了！
import mymokuai3

# 测试：调用模块里的函数/变量
mymokuai3.printdata('I am Python 3')

# 方法4：正规工程写法（创建 Python 包）。如果你的模块文件夹是一个Python 包，可以直接用 文件夹.模块名 导入

# 在模块文件夹 my_tools 里新建一个空文件，命名为 __init__.py
# （这个文件是空的就行，作用是告诉 Python：这是一个包）
# 文件结构：
# E:\lesson\
# ├── main.py
# └── my_tools\
#     ├── __init__.py  # 新建的空文件
#     └── my_module.py

# 直接 文件夹名.模块名
import my_tools.mymokuai4

# 调用
my_tools.mymokuai4.printdata('I am Python 4')






