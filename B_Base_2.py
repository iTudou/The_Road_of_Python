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