# zip，lambda，map功能
# zip功能，竖向合并
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b)))
# zip的输出可以作为迭代器（for...in语句）的输入
for i,j in zip(a,b):
    print(i/2,j*2)
# zip功能可以整合2个或以上的元素
print(list(zip(a,a,b,b)))

# lambda功能。与def功能类似
def fun1(x,y):
    return(x+y)

print(fun1(2,3))

fun2 = lambda v,w:v+w  # lambda功能的作用是定义简单的函数或方程，减少代码行数
print(fun2 (2,3))

# map功能，用已知的功能，加上给定的参数一起运算
print(list(map(fun1,[1],[2])))

# map功能，给定的参数可以输入多个值
print(list(map(fun1,[1,3,6],[2,5,5]))) 
