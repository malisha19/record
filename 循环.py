
# for in 循环
names = ['Jack','Jonny','Tim','Lucy','Mary']
for name in names:
    print(name)
#1-10的整数之和
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while循环

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello',name)

#break 
n = 1
while n <= 100:
    print(n)
    n = n+1
print('end')

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n+1
print('end')

n = 0
while n <= 8:
    n = n+2
    if n % 2 == 1:
        continue
    print(n)
# break语句可以在循环过程中直接退出循环,而continue语句可以提前结束本轮循环，并直接开始下一轮循环