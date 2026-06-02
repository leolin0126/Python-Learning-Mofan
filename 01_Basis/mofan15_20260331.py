text = '''\nThis is the first line.\nThis is the second line.\nThis is the last line.'''
print(text)

text2 = '''\nThis is the first line.
This is the second line.
This is the last line.'''
print(text2)

# 在默认路径下新建.txt文件，'w'新生成+覆盖；'a'追加内容不覆盖；'r'只读
my_file = open('my_file.txt', 'a')
my_file.write('''\n\n这是新追加的一行内容\n''')
my_file.write(text)
my_file.close()

# 在制定路径下新建.txt文件
my_file = open(r'E:\lesson\my_file.txt', 'a')
my_file.write('''\n\n这是新追加的一行内容\n''')
my_file.write(text2)
my_file.close()