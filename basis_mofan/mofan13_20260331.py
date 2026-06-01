# 全局变量APPLE（全大写），函数内部变量a
APPLE = 500
def fun():
    a = 10
    return a + 100
print(APPLE)
print(fun())
# 全局变量BANANA，函数局部变量b
BANANA = 250
def fun_2():
    b = BANANA
    return b + 100
print(BANANA)
print(fun_2())
# 在函数内部定义全局变量，使用global命令,在外部要把c定义为None
CAT = 666
c = None
def fun_3():
    global c
    c = 250
    return c + 888
print(CAT)
print('c past=', c)  # 函数fun_3运行前的c的值为None，此时c为global，即全局变量
print(fun_3())
print('c now=', c)  # 函数fun_3运行后，c的值为250，此时c为local，即局部变量；若global命令删去，则c在函数运行前后均为global全局变量