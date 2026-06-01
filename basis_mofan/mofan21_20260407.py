# 元组/tuple 和 列表/list
# for a in range(1,8):
#     print(a)

# 设计一个列表list
a_list = [1,2,3,6,7,67,45,89,82,115]

# for语句中，len函数表示a_list的长度为10，range函数表示[0,10)的整数区间，整个for语句表示，将[0,10)的整数依次赋值给变量index
# print语句中，index表示a_list中各个元素的位置，从0开始；number in list表示元素的具体数值
for index in range(len(a_list)):
    print('index=',index,'number in list=',a_list[index])

# 设计一个元组tuple
a_tuple = (85,62,456,41,2,78,99,285,167)

# 使用同样的for语句和print语句
print(' ')
for index2 in range(len(a_tuple)):
    print('index=',index2,'number in list=',a_tuple[index2])