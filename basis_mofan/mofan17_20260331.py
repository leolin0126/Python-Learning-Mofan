# 读取文件并打印文件中内容
file = open(r'E:\lesson\my_file2.txt','r')
content = file.read()
content = file.readlines()
print(content)