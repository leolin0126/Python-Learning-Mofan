# pickle模块，存放数据

import pickle

dict1 = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

# file = open(r'E:\lesson\pickle_example.pickle','ab')  # 在指定路径创建文件，并添加dict1的内容
# pickle.dump(dict1,file)  # 用pickle模块中dump功能把dict1的内容导入到文件中
# file.close()  # 关闭文件，必须写

file = open(r'E:\lesson\pickle_example.pickle','rb')  # 在指定路径只读文件
dict2 = pickle.load(file)  # 用pickle模块中的load功能把文件的内容导入到dict2中
file.close()  # 关闭文件，必须写
print(dict2)