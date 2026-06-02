# input功能
# a_input = input('Please gvie a number:')
# print('The input number is: ', a_input)

# input功能之，当你制作一个终端，需要用户输入特定信息，并对所输入的信息进行判断时
a_input = input('Please give a number:')  # return a str 返回的是字符串
if int(a_input) < 10:  # 判断时，要将a_input的格式转换为整数，即int(a_input)
    print('This is a good one')
elif 10<= int(a_input) <= 100:  # 判断时，要将a_input的格式转换为整数，即int(a_input)
    print('That\'s not bad')
else:  # 判断时，要将a_input的格式转换为整数，即int(a_input)
    print('Oh, That\'s excellent')















