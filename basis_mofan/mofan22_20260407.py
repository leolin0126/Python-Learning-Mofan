# 列表list的使用
a = [2,4,6,8,10,17,19,25,44,63]
print(a)
# append功能。在列表a末尾添加一个元素
a.append(19)
print(a)
# insert功能。在列表a中添加一个元素至指定位置
a.insert(3,99)
print(a)
# remove功能。删除列表a中的一个元素
a.remove(25)
print(a)
# pop功能。与remove功能类似。
a.pop()  # 删除列表中排在末尾的元素
print(a)
a.pop(2)  # 删除列表中指定位置的元素
print(a)
# 输出某个或某些位置的元素
print(a[3])  # 打印第3位的元素
print(a[2:5])  # 打印第2位至第4位的元素
# index功能。显示元素对应的索引
print(a.index(99))
# count功能。计算列表中有多少个该元素
print(a.count(99))
# sort功能。对列表进行从小到大或者从大到小排序
a.sort()  # 从小到大排序
print(a)
a.sort(reverse=True)  # 从大到小排序
print(a)