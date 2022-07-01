classmates = ['mark','lisa','tom','anna']
m = classmates[-1]#直接获取最后一个元素
n = len(classmates)#len()可以获取classmates元素个数；
print(m)
# .append()方法可以往list里面追加元素到末尾；
classmates.append('nova')
print(classmates[-1])#这边输出的值就变成了nova
#.insert()可以将元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'jack')#就是崽第一个元素之后插入‘jack’
print(classmates)#所以最后classmates输出变成'mark','jack','lisa','tom','anna','nova'
#删除list末尾元素用pop()方法
classmates.pop()
print(classmates)#输出结果变成'mark','jack','lisa','tom','anna'
#删除指定位置的元素用pop(i)
classmates.pop(3)
print(classmates)#会发现tom被删除，最后结果为mark，jack，lisa，anna
#元素替换直接可以赋值比如：
classmates[0]='Sara'#所以第一个从mark变成了Sara
print(classmates)
#list里面的元素的数据类型也可以不同，比如：
L = ['APPLE',123,True]
S = ['python','Java',['asp','php'],'go']
d = len(S)
print(d)#这边输出结果是4，即['asp','php']也被认为成1个元素

P = ['asp','php']
S = ['python','Java',P,'go']
print(S)#打印结果则跟上面S一样
print(P[0])
print(S[2][0])#这边的打印结果跟上面的P[0]结果都为asp

L = []#这个就是个空list

#tuple
name = ('Lisa','Zara','Mary','Lucy')#tuple一旦初始化就不能修改，不能改变
T = ()#这个就是空的tuple 
T= (1)#定义一个只有1个元素的tuple,注意：这边定义的是1这个数，不是代表这边只有1个元素
T = (1,)#这个才是定义只有1个元素的tuple
Q = ('a','b','c',['A','B','C'])
Q[3][0] = 'X'
Q[3][1] = 'Y'
Q[3][2] = 'Z'
print(Q)#结果输出为 ('a','b','c',['X','Y','Z'])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],L[1][1],L[2][2])