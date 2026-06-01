# def函数，且为def函数添加参数。
def fun(a,b):
    c = a*b
    print('the c is',c)
fun(2,5)
fun(10,7)
fun(105,85)

# 豆包：学习函数的「返回值」—— 用 return 把计算结果带出来，而不是只打印
def fun(a, b):
    c = a * b
    return c  # 把结果返回给调用处

result1 = fun(2,5)
result2 = fun(8,10)
print("\n两次乘积的和:", result1 + result2)

# 用return改写函数
def fun(a, b):
    c = a * b
    return c  # 返回乘积

# 调用函数，并接收结果
r1 = fun(2,5)
r2 = fun(10,7)
r3 = fun(105,85)

# 现在可以对结果做任何操作
print("\n第一次结果：", r1)
print("第二次结果：", r2)
print("第三次结果：", r3)
print("三次结果总和：", r1 + r2 + r3)