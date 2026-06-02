# numpy的copy和deep copy

import numpy as np

a1 = np.arange(6)
print(a1)

b1 = a1
c1 = a1
d1 = b1

a1[0] = 999
print(a1)
print()
print(b1)

print()
print(b1 is a1)  # 判断变量b1是否与a1完全一致，输出结果为True，指向原地址 
print(c1 is a1)  # 输出结果为True，c1同样被改变，类似java中的引用传递
print(d1 is a1)  # 输出结果为True，d1同样被改变

# numpy中引用的地址一致，内存地址一样，共用一个地址，当原地址改变，其他一并改变

d1[2:5] = [222,444,666]
print()
print(d1)
print(a1)
print(b1)
print(c1)

b2 = a1.copy()  # deep copy，只拿了a1的值，但没有把b2和a1关联起来
a1[5] = 888
print()
print(a1)
print(b2)

# 都错了 在numpy中a=b 不拷贝 view()浅拷贝 copy()深拷贝（？）
# 传值和传引用的区别。Python赋值语句默认传引用，和C++不同。
# python 中的深浅拷贝是要引用copy模块的，浅拷贝：copy.copy，深拷贝：copy.deepcopy
# 回答一下，python的copy模块中copy方法代表浅拷贝，deepcopy方法是深拷贝，这里numpy中的copy方法和copy模块的copy方法不是同一个，它就是深拷贝




