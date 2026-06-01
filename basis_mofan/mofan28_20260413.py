# 错误处理 try语句
# try:  # 处理错误语句
#     file = open(r'E:\lesson\my_file_eeee.txt','r')  # 在指定位置只读打开文件
# except Exception as e:  # 接受错误，并把错误结果赋值给变量e
#     print(e)  # 打印变量e

# 对错误判断的后续处理
try:  # 处理错误语句
    file = open(r'E:\lesson\my_file_eeee.txt','r')  # 在指定位置只读打开文件
except Exception as e:  # 接受错误，并把错误结果赋值给变量e
    print('there is mo file named as my_file_eeee.txt')
    response = input('do you want to create a new file')  # 反馈结果
    if response == "y":
        file = open(r'E:\lesson\my_file_eeee.txt','w')  # 如果需要创建新文件，则创建文件
    else:
        pass
else:  # 如果在指定路径有相应文件，则不运行except语句的内容
    file.write('ssss')
file.close()

    





