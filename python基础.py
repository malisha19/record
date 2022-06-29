# python基础-数据类型和变量
# print('I\'m\"OK\"') 转义字符\的应用
# print('I\'m learning\n python') \n 换行的应用
# print('\\\n\\')转义中\\表示\
# print('\\\t\\')
# print(r'\\\t\\')r''表示内部的内容不转义
# print('''line1 
# line2
# line3''') '''  ''' 表示内部有很多行
# print(r'''hello,\n
# world''')  ''' ''' 前面加r也适用于不转义

# 布尔值
# 真真为真，真假为假，假假为假 and
# 真真为真，真假为真，假假为假 or
# 非真即假，非假即真 not
# 空值用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

# 变量
# a = 123 #a是整数
# print(a)
# a ='abc'#a是字符串
# print(a)
# 变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
# 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

# a = 'ABC'
# b = a 
# a = 'XYZ'
# print(b)
# 除法有两种，一种是/ 表示除法结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
# 9/3 结果是3.0
# 还有一种是//，即为地板除，两个数相除仍是整数
# 10//3 结果为3
# %为余数运算，如：10%3，结果为1

#字符串和编码
# print('包含中文的str')

# q = ord('A')
# w = ord('中')
# print(w) ord()函数获取字符的整数表示

# chr(66)
# chr(25991)chr()函数把编码转成对应的字符

# 'ABC'.encode('ascii')输出结果为 b'ABC'
# '中文'.encode('utf-8')输出结果为 b'\xe4\xb8\xad\xe6\x96\x87'
# Unicode表示的str通过encode()方法可以编码为指定的bytes
# str 转化为bytes 用encode()

# bytes变为str，用decode()
# b'ABC'.decode('ascii') 输出结果为'ABC'
#  b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') 输出结果为'中文'

# 如果bytes中包含无法解码的字节，decode()方法会报错
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
# b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# 输出结果则为'中'

# len()函数 可以计算str包含多少个字符；
# 如：len('ABC'),len('中文')

# len()函数也可计算bytes字节数；
# 如：len(b'ABC');len(b'\xe4\xb8\xad\xe6\x96\x87');len('中文'.encode('utf-8'))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print('hello,%s'%'lisa') %表示格式化字符串
# %s表示用字符串替换，%d表示用整数替换，
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
# print('hi,%s,you have %d元'%('lisa',10000))
# print('%d-%01d' % (3, 1))
# print('%.f' % 3.1415926)
# 'Age: %s. Gender: %s' % (25, True) %s永远起作用，可以将任何数据类型转化成字符
# 'growth rate: %d %%' % 7  %%来表示一个%

# format()
# print('hello,{0},你的成绩提升了{1:.2f}绩点,上升了{2}名'.format('小明',13.234,3))

# f-string
#  r = 2.5
# >>> s = 3.14 * r ** 2
# >>> print(f'The area of a circle with radius {r} is {s:.2f}')
# The area of a circle with radius 2.5 is 19.62

# s1 = 72
# s2 = 85 
# r = (s2-s1)/s1*100
# print('小明成绩提升的百分点为%.1f%%'%r)
# print('小明成绩提升的百分比为{0:.1f}%'.format(r))
# print(f'小明成绩提升的百分比为{r:.1f}%')