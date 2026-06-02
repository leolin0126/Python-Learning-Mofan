# continue语句 和 break语句
# a = True
# while a:
#     b = input('type something')
#     if b =="1":
#         a = False
#     else:
#         pass

# print('finish run')

# break语句
a = True  # d定义变量a为True
while a:  
    b = input('type something')
    if b =="1":  # 判断输入的字符b等于'1'时
        a = False
        break  # break语句跳出while循环
    else:  # 判断输入的字符b不等于'1'时
        pass  # 继续循环
        print('still in while')  # 继续while循环输出字符

print('finish run')  # break语句打断循环后输出字符

# （from liaoxuefeng5.6）如果想跳过某些循环，可以用continue语句
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

