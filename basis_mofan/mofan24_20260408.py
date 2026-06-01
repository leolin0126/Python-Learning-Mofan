# 字典，以key-value的形式存在
d = {'apple':1,'pear':2,'orange':3,'banana':4,
     'cherry':5,'kiwi':6,'pineapple':7,'grape':8,
     'strawberry':9,'peach':10,'lemon':11,'mango':12,
     'watermelon':13,'blueberry':14,'papaya':15,'coconut':16,
     'lychee':17,'avocado':18,'durian':19,'starfruit':20}

# 取出字典中的值
print(d['apple'])
print(d['starfruit'])
print(d['lychee'])

# 删除字典中的值（del功能 或者 pop功能）
# del功能
print()
del d['pear']
print(d)
# pop功能
print()
print(d.pop('kiwi'))
print(d)

# 增加字典中的值
print()
d['longan'] = 21
d['fig'] = 22
d['mulberry'] = 23
d['lime'] = 24
print(d)

# 字典有多种形式
print()
d2 = {'apple2':[1,2,3],'pear2':{1:3,3:'a'},'orange2':2}
print(d2['pear2'][3])