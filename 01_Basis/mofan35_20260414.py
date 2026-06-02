# set 找不同
char_list = ['a','b','c','c','d','d']
print(set(char_list))

sentence = 'Welcome Back to This Tutorial'
print(set(sentence))  # 输出结果区分大小写

unique_chat = set(char_list)
unique_chat.add('x')  # 在set中只能逐个添加新元素
# unique_chat.clear()  # 清除现有set的所有元素，输出空的set()
# unique_chat.remove()  # 删除现有set的指定元素，要输入print才能输出删除后的set 
# unique_chat.discard()  # 删除不存在的元素时避免报错

print(unique_chat)

set1 = unique_chat
set2 = set(sentence)

print()
print(set1.difference(set2))
print(set1.intersection(set2))