d = {'mark':95,'bob':63,'anna':78}
print(d['anna'])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['bb'] = 82
print(d['bb'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['lucy'] = 89
print(d['lucy'])
d['lucy'] = 92
print(d['lucy'])
# 一：通过in判断key是否存在
'mini' in d
# 二：通过dict提供的get()方法
d.get('mini')
d.get('mini',1)
print(d.get('mini'))
# 如果key不存在，可以返回None，或者自己指定的value
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('bob')
print(d)
# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
#
#  而list相反：
#  查找和插入的时间随着元素的增加而增加；
#  占用空间小，浪费内存很少。

#set
s = set([1,2,3,4])
print(s)
# 注意:传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
# 重复元素在set中自动被过滤：
s = set([1,2,3,3,4,4,5,6])
print(s)
# 通过add(key)方法可以添加元素到set中
s.add(7)
print(s)
# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

a = ['a','d','c','b']
a.sort()#按顺序排序
print(a)

a = 'abc'
a.replace('a','A')
print(a)#输出结果仍是'abc'
#以上要改成如下：

a = 'abc'
b = a.replace('a','A')
print(b)#这时候输出就是ABC