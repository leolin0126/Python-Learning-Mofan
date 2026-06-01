# 矩阵运算，numpy 和 pandas

a = [0,1,2,0,1,2,0,1,2,0,1,2]
b = [0,0,0,10,10,10,20,20,20,30,30,30]
print(list(zip(a,b)))

result = [i + j for i, j in zip(a, b)]  # 列表推导式
print(result)

result = list(map(lambda x: x[0] + x[1], zip(a, b)))  # 使用 map() + lambda
print(result)

result = []                     # 先创建一个空列表
for i, j in zip(a, b):
    result.append(i + j)        # 把每次的和追加进去
print(result)                   # 最后打印整个列表