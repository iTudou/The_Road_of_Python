#!/usr/bin/python
#coding:utf-8

##### 基本数据类型
### 数字

#返回表示该数字的时占用的最少位数
print (951).bit_length()

#返回绝对值
print (95).__abs__()
print (-95).__abs__()

#用来区分数字和字符串的
print (95).__add__(1)
print (95).__add__("1")

#判断一个整数对象是否为0，如果为0,则返回False，如果不为0，则返回True
#print (95).__bool__()
#print (0).__bool__()

#判断两个值是否相等 __eq__ 不等于 __ne__ 大于等于 __ge__ 大于 __gt__ 小于等于__le__ 小于__lt__
print ('95').__eq__('95')
print ('95').__eq__('9')
print ('95').__ne__('9')

#加法运算
print (95).__add__(5)
#减法运算
print (95).__sub__(5)
#乘法运算
print (95).__mul__(10)
#除法运算
print (95).__truediv__(5)
#取模运算
print (95).__mod__(9)
#幂运算
print (2).__pow__(10)
#整除，保留结果的整数部分
print (95).__floordiv__(9)
#转换为整型
print (9.5).__int__()
#返回一个对象的整数部分
print (9.5).__trunc__()
#将正数变为负数，将负数变为正数
print (95).__neg__()
print (-95).__neg__()
#将一个正数转为字符串
a = 95
a = a.__str__()
print(type(a))
#将一个整数转换成浮点型
print (95).__float__()
#转换对象的类型
print (95).__format__('f')
print (95).__format__('b')
#在内存中占多少个字节
a = 95
print a.__sizeof__()

### 字符串
s = "nick"
#索引
print s[0]
print s[1]
print s[2]
print s[3]
#长度
print len(s)
#切片
print s[1:3]
print s.rsplit("ic")
#替换
name = "Nick is good, Today is nice day."
a = name.replace("good","man")
print(a)
#连接两个字符串
li = ["nick","serven"]
a = "".join(li)
b = "_".join(li)
print(a)
print(b)
#指定的分隔符将字符串进行分割
a = s.rpartition("i")
print(a)
#分割，前，中，后三部分
name = "Nick is good, Today is nice day."
a = name.partition("good")
print(a)
#for循环
for i in s:
    print(i)
for i in range(5):
    print(i)
# 反转
s = 'ssssssssss111'
print(s[::-1])  # 111ssssssssss

### 列表
#在列表末尾添加新的对象
list = ['Google', 'baidu', 'T']
list.append('taobao')
print(list)
#将指定对象插入列表
list = ['Google', 'baidu', 'T','baidu']
list.insert(1,"Nick")
print(list)
#在列表末尾追加另一个序列中的多个值
list = ['Google', 'baidu', 'T','baidu']
list2 = ['nick','baidu']
list.extend(list2)
print(list)
#统计某个元素在列表中出现的次数
list = ['Google', 'baidu', 'T','baidu']
a = list.count('baidu')
print(a)
#从列表中找出某个值第一个匹配项的索引位置
list = ['Google', 'baidu', 'T','baidu']
a = list.index('Google')
print(a)
#移除列表中的一个元素（默认最后一个元素）
list = ['Google', 'baidu', 'T','baidu']
list.pop()
print(list)
#移除列表中某个值的第一个匹配项
list = ['Google', 'baidu', 'T','baidu']
list.remove('baidu')
print(list)
#清空列表
a = ['Google', 'baidu', 'T']
del a[:]  # a.clear()
print(a)
#删除指定索引位置
list = ['Google', 'baidu', 'T','baidu']
del list[2]
print(list)
list = ['Google', 'baidu', 'T','baidu']
del list[1:3]    #顾头不顾尾
print(list)
#复制列表  python 3 版本
# list = ['Google', 'baidu', 'T']
# list2 = list.copy()
# print(list2)
#对原列表进行排序
list = ['Google', 'baidu', 'T','baidu']
list.sort()
print(list)
#反向列表中元素
list = ['Google', 'baidu', 'T','baidu']
list.reverse()
print(list)

# 元组
#索引
name = ('nick','jenney')
a = name[0]
print(a)
#获取指定元素的索引位置
name = ('nick','jenney')
a = name.index('nick')
print(a)
#切片
name = ('nick','jenney')
a = name[0:1]
print(a)
#计算元素出现的个数
name = ('nick','jenney')
a = name.count('nick')
print(a)
#长度
name = ('nick','jenney')
a = len(name)
print(a)
#for循环
name = ('nick','jenney')
for i in name:
    print(i)
    
# 字典
user_info = {
    "name":"nick",
    "age":18,
    "job":"pythoner"
}
#根据key获取值
a = user_info.get("age")
print(a)
a = user_info.get("Age",19)
print(a)
#所有的key 列表
a = user_info.keys()
print(a)
#所有的值，values
a = user_info.values()
print(a)
#所有项的列表形式
a = user_info.items()
print(a)
#获取并在字典中移除
user_info.pop('age')
print(user_info)
#随机并在字典中移除
user_info.popitem()
user_info.popitem()
print(user_info)
#清除内容
a = user_info.clear()
print(a)
#浅拷贝
a = user_info.copy()
print(a)
#如果key不存在，则创建，如果存在，则返回已存在的值且不修改
a = user_info.setdefault("age")
print(a)
user_info.setdefault("cool")
print(user_info)
#从序列键和值设置为value来创建一个新的字典
user_info = {
    "name":"nick",
    "age":18,
    "job":"pythoner"
}
a = dict.fromkeys(user_info)
print(("new dict: %s") % str(a))
#更新（两个字典）
user_info2 = {
    "wage":800000000,
    "drem":"The knife girl"
}
user_info.update(user_info2)
print(user_info)

# 集合
#添加元素
a = {'nick','jenny','suo'}
a.add('The knife girl')
print(a)
#更新
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
a.update(b)
print(a)
#a中存在。b中不存在，赋给新值
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
set = a.difference(b)
print(set)
#a中存在。b中不存在,并更新a
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
a.difference_update(b)
print(a)
#交集,赋给新值
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
set = a.intersection(b)
print(set)
#交集，更新a
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
a.intersection_update(b)
print(a)
#对称交集
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
set = a.symmetric_difference(b)
print(set)
#对称交集，更新a
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
a.symmetric_difference_update(b)
print(a)
#并集，赋给新值
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
set = a.union(b)
print(set)
#如果没有交集，返回True，否则返回False
a = {'nick','jenny','suo'}
b = {'nick','jenny','The knife girl'}
set = a.isdisjoint(b)
print(set)
#是否是子序列
a = {'nick','jenny','suo'}
b = {'nick','jenny'}
set = b.issubset(a)
print(set)
#是否是父序列
a = {'nick','jenny','suo'}
b = {'nick','jenny'}
set = a.issuperset(b)
print(set)
#移除指定元素，不存在不报错
a = {'nick','jenny','suo'}
a.discard('suo')
print(a)
#移除指定元素，不存在则报错
a = {'nick','jenny','suo'}
a.remove('suo')
print(a)
# a.remove('suo')
# print(a)
#移除随机元素，并赋给新值
a = {'nick','jenny','suo'}
set = a.pop()
set2 = a
print(set)
print(set2)
#清空
a = {'nick','jenny','suo'}
a.clear()
print(a)

# 冻结的集合 它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法
name = frozenset({"suoning"})
print name


#####其他
#for循环
name = ('nick','jenney')
for i in name:
    print(i)
#enumrate
user_info = {
    "name":"nick",
    "age":18,
    "job":"pythoner"
}
for k,v in enumerate(user_info,1):
    print(k,v,user_info.get(v))
#range和xrange
print range(1, 10)
print range(1, 10, 2)
print range(30, 0, -2)
#编码与进制转换
#utf-8与gbk编码转换 中间通过 unicode
#进制的转换
#hex 可以 十进制转16进制    二进制转16进制     结果都是字符串
print hex(0b10)
print hex(10)
#bin 可以 十进制转2进制    16进制转2进制    结果都是字符串
print bin(10)
print bin(0x2)
#int 可以16进制转换十进制    2进制转换十进制
print int(0xe)
print int(0b100)
#把自己名字用进制表示出来
name = "索宁"
# a = bytes(name,encoding='utf-8')
# print(a)
# for i in a:
#     print(i,bin(i))
# b = bytes(name,encoding='gbk')
# print(b)
# for i in b:
#     print(i,bin(i))