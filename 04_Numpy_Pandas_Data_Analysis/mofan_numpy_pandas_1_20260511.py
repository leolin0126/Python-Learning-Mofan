# numpy 和 pandas 的安装

# 安装numpy （参考mofan14.py）
# 安装命令（豆包）：pip install numpy==1.24.3
# 测试numpy是否安装成功

import numpy as np

# 创建一个 NumPy 数组
arr = np.array([1, 2, 3, 4])
print(arr)
print("NumPy 版本：", np.__version__)

# 安装pandas
# 安装命令（豆包）：pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple

# 测试pandas是否安装成功

import pandas as pd

# 打印版本号，不报错就说明成功了
print("pandas 安装成功！版本：", pd.__version__)

# 再测试
import numpy as np
import pandas as pd

# 创建一个数据表（DataFrame）
data = {
    "姓名": ["小明", "小红", "小刚"],
    "年龄": [20, 21, 22],
    "分数": [90, 85, 88]
}

df = pd.DataFrame(data)
print(df)