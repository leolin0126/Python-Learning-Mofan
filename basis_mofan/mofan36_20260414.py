# 正则表达式 regular expression

import re  # 导入模块，正则表达式re

# 简单python匹配，matching string
pattern1 = 'cat'
pattern2 = 'bird'
string1 = 'dog runs to cat'
print('简单python匹配, matching string')
print(pattern1 in string1)  # 输出为True
print(pattern2 in string1)  # 输出为False

# 用正则表达式匹配，regular expression
pattern3 = 'cat'
pattern4 = 'bird'
string2 = 'dog runs to cat'
print()
print('用正则表达式匹配, regular expression')
print(re.search(pattern3,string2))
print(re.search(pattern4,string2))

# 匹配多种可能，使用中括号[]
pattern5 = r'r[au]n'
print()
print('匹配多种可能, 使用中括号[]')
print(re.search(pattern5,'dog runs to cat'))
print(re.search(pattern5,'dog ran to cat'))

# 匹配更多种可能
print()
print('匹配更多种可能')
print(re.search(r'r[A-Z]n','dog runs to cat'))
print(re.search(r'r[a-z]n','dog runs to cat'))
print(re.search(r'r[0-9]n','dog runs to cat'))
print(re.search(r'r[0-9a-z]n','dog runs to cat'))

# 特殊类型匹配————数字
print()
print('特殊类型匹配————数字')
# \d : decimal digit
print(re.search(r'r\dn','run, r4n'))
# \D : any non-decimal digit
print(re.search(r'r\Dn','run, r4n'))

# 特殊类型匹配————空白
print()
print('特殊类型匹配————空白')
# \s : any white space [\t\n\r\f\v]
print(re.search(r'r\sn','r\nn, r4n'))
# \S : opposite to \s, any non-white space
print(re.search(r'r\Sn','r\nn, r4n'))

# 所有字母数字和下划线('_')
print()
print('所有字母数字和下划线"_"')
# \w : [a-zA-Z0-9_]
print(re.search(r'r\wn','r\nn, r4n'))
# \W : opposite to \w
print(re.search(r'r\wn','r\nn, r4n'))

# 空白字符
print()
print('空白字符')
# \b : empty string, only at the start or the end of a word
print(re.search(r'\bruns\b','dog runs to cat'))
# \B : empty string, but not at the start or the end of a word
print(re.search(r'\B runs \B','dog    runs     to   cat'))

# 特殊字符 和 任意字符
print()
print('特殊字符 和 任意字符')
# \\ : match \
print(re.search(r'runs\\','dog runs\ to me'))
# . : match anyyhing except \n
print(re.search(r'r.n','dog r[ns to me'))

# 句尾句首
print()
print('句尾句首')
# ^ : match line beginning
print(re.search(r'^dog','dog runs to cat'))
# $ : match line ending
print(re.search(r'cat$','dog runs to cat'))

# 是与否
print()
print('是与否')
# ? : may or may not occur
print(re.search(r'Mon(day)?','Monday'))
print(re.search(r'Mon(day)?','Mon'))

# 多行匹配
print()
print('多行匹配')
# multi lines
string3 = '''
dog runs to cat.
I run to dog.
'''
print(re.search(r'^I',string3))
print(re.search(r'^I',string3,flags=re.M))

# 0次或多次
print()
print('0次或多次')
# * : occur 0 or more times
print(re.search(r'ab*','a'))
print(re.search(r'ab*','abbbbb'))

# 1次或多次
print()
print('1次或多次')
# + : occur 1 or more times
print(re.search(r'ab+','a'))
print(re.search(r'ab+','abbbbb'))

# 可选次数
print()
print('可选次数')
# {n,m} : occur n to m times
print(re.search(r'ab{2,10}','a'))
print(re.search(r'ab{2,10}','abbbbb'))

# group 组
print()
print('group 组')
# group
match = re.search(r'(\d+),Date: (.+)','ID: 021523,Date: Feb/12/2017')
print(match.group())
print(match.group(1))
print(match.group(2))

print()
match = re.search(r'(?P<id>\d+),Date: (?P<date>.+)','ID: 021523,Date: Feb/12/2017')
print(match.group('id'))
print(match.group('date'))

# 寻找所有匹配
print()
print('寻找所有匹配')
# findall
print(re.findall(r'r[ua]n','ran run ren'))
# | : or
print(re.findall(r'ran|run','ran run ren'))

# 替换
print()
print('替换')
# re.sub() : replace
print(re.sub(r'r[au]ns','catches','dog runs to cat'))

# 分裂
print()
print('分裂')
# re.split()
print(re.split(r'[,;\.]','a;b,c.d;e'))

# compile()函数
# compile()函数允许程序员在运行时刻迅速生成代码对象，然后就可以用exec 语句或者内建函数eval()来执行这些对象或者对它们进行求值。
# compile()函数提供了一次性字节代码预编译，以后每次调用的时候，都不用编译了。
# https://cloud.tencent.com/developer/article/1569436, 腾讯云开发者社区-腾讯云
print()
print('compile()函数')
# compile()
compiled_re = re.compile(r'r[ua]n')
print(compiled_re.search('dog ran to cat'))




