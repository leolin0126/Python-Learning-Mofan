# while循环语句。代码中，先定义condition=1，然后判断condition是否小于10。
# 1<10，判断为True，则输出结果为1，然后令原condition+1=2，把2赋值为新的condition，再次运行判断。
# 如此循环，直到当condition=10时，判断10<10为False，跳出循环，代码结束运行。
# 依次输出1至9，共9个结果。
condition = 1
while condition < 10:
    print(condition)
    condition = condition + 1