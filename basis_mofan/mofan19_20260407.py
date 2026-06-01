# 类 init，定义初始状态
class Calculator:
    name = 'Good Calculator'  # 类Calculator的属性1，名称name
    price = 18  # 类Calculator的属性2，价格price
    def __init__(self, name, price, height, width, weight):
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.weight = weight
    def add(self,x,y):  # self类似于C++语言中的this，有传递参数的作用
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        result = x * y
        print(result)
    def divide(self,x,y):
        result = x / y
        print(result)

ex = Calculator('Bad calculator', 12, 30, 15, 19)
print(ex.name)

print(ex.weight)
print(ex.price)

# 可以在init状态中，为参数定义某个具体的数值

class Calculator2:
    name = 'Good Calculator2'  # 类Calculator的属性1，名称name
    price = 81  # 类Calculator的属性2，价格price
    def __init__(self, name, price, height=33, width=66, weight=250):
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.weight = weight
    def add(self,x,y):  # self类似于C++语言中的this，有传递参数的作用
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        result = x * y
        print(result)
    def divide(self,x,y):
        result = x / y
        print(result)

ex2 = Calculator2('Bad calculator2', 12)
print(ex2.name)

print(ex2.weight)
print(ex2.price)
print(ex2.height)
print(ex2.width)



