from ctypes.wintypes import PLARGE_INTEGER


q = abs(-101)
print(q)#调用绝对值函数

a = max(2,3,-1,-4,9)
print(a)#调用最大值函数，从一群数值中取最大值

# int()函数可以把其他数据类型转换为整数
b = int('123')
print(b)

#float()可以把其他数据类型转成浮点数

c = float('23.2')
print(c)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-3))

n1 = 255
n2 = 1000
m = hex
print(m(n1),m(n2))