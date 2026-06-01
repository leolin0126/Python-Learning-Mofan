# for循环语句。给定一个list，变量i依次赋值为list中的数字;
# 然后依次循环输出数字和字符串'inner of for';
# 在for循环全部完成输出后，再输出循环外的字符串'outer of for'。
print('for 循环语句 练习1')
example_list=[1,2,3,4,5,6,7,12,543,876,12,3,2,15]
for i in example_list:
    print(i)
    print('inner of for')
print('outer of for')
# 对于for循环，有一个内部函数range；
# 表示为在一个左闭右开的区间内按一定的步长step进行迭代；
# 函数range发挥迭代器的作用。
# 练习2中的步长step=1。
print('for 循环语句 练习2')
example_list=[1,2,3,4,5,6,7,12,543,876,12,3,2,15]
for i in range(1,10,1):
    print(i)
# 练习3中的步长step=2。
print('for 循环语句 练习3')
example_list=[1,2,3,4,5,6,7,12,543,876,12,3,2,15]
for i in range(1,10,2):
    print(i)
# 练习4中的步长step=5。
print('for 循环语句 练习4')
example_list=[1,2,3,4,5,6,7,12,543,876,12,3,2,15]
for i in range(1,10,5):
    print(i)