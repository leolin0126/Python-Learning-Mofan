append_text = '''\n\nThis is the fourth line.
This is the fifth line.
this is the sixth line.'''

# 用with语句，自动管理文件关闭，路径同样支持绝对/相对路径
with open(r'E:\lesson\my_file2.txt', 'a') as my_file2:
    my_file2.write('\n\n这是一行新的内容')
    my_file2.write(append_text)