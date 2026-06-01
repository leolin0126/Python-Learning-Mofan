# 列表的功能,利用while循环依次删除列表a中多次出现的元素
a = [2,4,6,8,10,17,19,25,44,63,19,4,8,7,77,25,17,62]
print(a)
while 19 in a:
    a.remove(19)
    print(a)

b = [2,4,25,6,8,10,21,7,19,25,44,63,8,19,4,8,44,13,7,77,25,17,62,16,44]
print(b)
while 25 in b:
    b.remove(25)
    print(b)
while 44 in b:
    b.remove(44)
    print(b)