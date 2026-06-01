# numpy的基本属性
 
import numpy as np

array = np.array([[1,2,3],  # 在numpy中定义2维数组array，长3个单位，宽2个单位
                  [2,3,4]])

print(array)
print('number of dimension:', array.ndim)  # 显示数组array是几维的数组
print('shape:', array.shape)  # 显示数组的形状，输出结果第一个数字代表有多少行，第二个数字代表多少列
print('size:', array.size)  # 显示数组中有多少元素

