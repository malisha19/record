def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(3))
def nop ():
    pass#定义一个空函数

def abs_2(y):
    if not isinstance(y,(int,float)):
        raise TypeError('not this type')
    if y >= 0:
        return y
    else:
        return -y
# print(abs_2('A'))#这时候会提示错误。
print(abs_2(-3))

import math
from tkinter import Y
def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny
r = move(100,100,60,math.pi/6)
print(r)

