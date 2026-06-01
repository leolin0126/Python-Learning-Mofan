# 在已创建的文件中新增内容
append_text = '''\n\nThis is the fourth line.
This is the fifth line.
this is the sixth line.'''

my_file = open(r'E:\lesson\my_file.txt', 'a')
my_file.write(append_text)
my_file.close()