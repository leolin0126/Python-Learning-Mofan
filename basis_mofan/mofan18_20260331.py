class Calculator:
    name = 'Good Calculator'  # 类Calculator的属性1，名称name
    price = 18  # 类Calculator的属性2，价格price
    def add(self,x,y):  # self类似于C++语言中的this，有传递参数的作用
        print(self.name)  # 在类Calculator中调用属性1name
        result = x + y
        print(result)
    def minus(self,x,y):
        print(self.name)  # 在类Calculator中调用属性1name
        result = x - y
        print(result)
    def times(self,x,y):
        print(self.name)  # 在类Calculator中调用属性1name
        result = x * y
        print(result)
    def divide(self,x,y):
        print(self.name)  # 在类Calculator中调用属性1name
        result = x / y
        print(result)

# 定义变量calcu为Calculator()，并输出其属性1name和属性2price
calcu = Calculator()
print(calcu.name)
print(calcu.price)

# 使用类Calculator中的功能
calcu.add(25,25)  # 使用类Calculator中的加法add功能
calcu.minus(25,25)  # 使用类Calculator中的减法minus功能
calcu.times(25,25)  # 使用类Calculator中的乘法times功能
calcu.divide(25,25)  # 使用类Calculator中的除法divide功能

