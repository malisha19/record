from bisect import bisect_right
from re import X
from tkinter import BitmapImage


age = 20
if age >= 18:
    print('you age is :',age)
    print('adult')

age = 3
if age >= 18:
    print('you age is',age)
    print('adult')
else:
    print('you age is',age)
    print('kid')

age = 2
if age >= 18 :
    print('adult')
elif age >= 6:
    print('teenager')
elif age >= 3:
    print('kid')
else:
    print('baby')

# 注意：if判断是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else

if X:
    print('true')

birth = input('请输入你的生日：')
last = int(birth)
if last >= 2000:
    print('00后')
else:
    print('00前')

height = 1.75
weight = 80.5
BMI = float(weight/(height*height))
if BMI > 32:
    print('严重肥胖')
elif 32>= BMI>28:
    print('肥胖')
elif 28>= BMI>25:
    print('过重')
elif 25>= BMI>18.5:
    print('正常')
else :
    print('过轻')
