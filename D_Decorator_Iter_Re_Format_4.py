#!/usr/bin/python
#coding:utf-8

#####装饰器
########## 基本装饰器 ##########
def orter(func):    #定义装饰器
    def inner():
        print("This is inner before.")
        s = func()    #调用原传入参数函数执行
        print("This is inner after.")
        return s        #return原函数返回值
    return inner      #将inner函数return给name函数

@orter    #调用装饰器（将函数name当参数传入orter装饰器）
def name():
    print("This is name.")
    return True        #name原函数return True 

ret = name()
print(ret)

############ 装饰器传参数 ###########
def orter2(func):
    def inner(a,b):      #接收传入的2个参数
        print("This is inner before.")
        s = func(a,b)    #接收传入的原函数2个参数
        print("This is inner after.")
        return s
    return inner

@orter2
def name2(a,b):    #接收传入的2个参数，并name整体函数当参数传入orter装饰器
    print("This is name.%s,%s"%(a,b))
    return True

ret = name2('nick','jenny')    #传入2个参数
print(ret)

########## 万能参数装饰器 ##########
def orter3(func):
    def inner(*args,**kwargs):        #万能参数接收多个参数
        print("This is inner before.")
        s = func(*args,**kwargs)       #万能参数接收多个参数
        print("This is inner after.")
        return s
    return inner

@orter3
def name3(a,b,c,k1='nick'):        #接受传入的多个参数
    print("This is name.%s,%s"%(a,b))
    return True

ret = name3('nick','jenny','car')
print(ret)

########### 一个函数应用多个装饰器 #########
def orter4(func):
    def inner(*args,**kwargs):
        print("This is inner one before.")
        print("This is inner one before angin.")
        s = func(*args,**kwargs)
        print("This is inner one after.")
        print("This is inner one after angin.")
        return s
    return inner

def orter_2(func):
    def inner(*args,**kwargs):
        print("This is inner two before.")
        print("This is inner two before angin.")
        s = func(*args,**kwargs)
        print("This is inner two after.")
        print("This is inner two after angin.")
        return s
    return inner

@orter4           #将以下函数整体当参数传入orter4装饰器
@orter_2          #将以下函数当参数传入orter_2装饰器somebody

def name4(a,b,c,k1='nick'):
    print("This is name.%s and %s."%(a,b))
    return True

ret = name4('nick','jenny','car')
print(ret)

#####迭代器 & 生成器
#迭代器
a = iter(range(5))
print a
print a.next()  # a.__next__()  python 3 版本用法
print a.next()
print a.next()
print a.next()
print a.next()
# print a.next()

#生成器
def xran():
    print("one")
    yield 1
    print("two")
    yield 2
    print("sr")
    yield 3

ret = xran()
#print(ret)      #<generator object xran at 0x00000000006ED308>
 
result = ret.next()
print'abcdefg'
print(result)
 
result = ret.next()
print(result)
 
result = ret.next()
print(result)
# ret.__next__()  #循环完毕抛出StopIteration
# ret.close()     #关闭生成器

#生成器表达式
a=[7,8,9]
b=[i**2 for i in a]
print b
ib=(i**2 for i in a)
print ib
print next(ib)
print next(ib)
print next(ib)

#####正则表达式
import re
s = 'nick jenny nice'
# 匹配方式（一）
b = re.match(r'nick',s)
q = b.group()
print b
print(q)
# 匹配方式（二）
# 生成Pattern对象实例,r表示匹配源字符串
a = re.compile(r'nick')
print(type(a))               #<class '_sre.SRE_Pattern'>
b = a.match(s)
print(b)                     #<_sre.SRE_Match object; span=(0, 4), match='nick'>
q = b.group()
print(q)
#被匹配的字符串放在string中
print(b.string)              #nick jenny nice
#要匹配的字符串放在re中
print(b.re)                  #re.compile('nick')

# "." 匹配任意字符（除了\n）
a = re.match(r".","95nick")
b = a.group()
print(b)
 
# [...] 匹配字符集
a = re.match(r"[a-zA-Z0-9]","123Nick")
b = a.group()
print(b)

# \d \D 匹配数字/非数字
a = re.match(r"\D","nick")
b = a.group()
print(b)
# \s \S 匹配空白/非空白字符
a = re.match(r"\s"," ")
b = a.group()
print(b)
# \w \W 匹配单词字符[a-zA-Z0-9]/非单词字符
a = re.match(r"\w","123Nick")
b = a.group()
print(b)
a = re.match(r"\W","+-*/")
b = a.group()
print(b)

# "*" 匹配前一个字符0次或者无限次
a = re.match(r"[A-Z][a-z]*","Aaaaaa123")    #可以只匹配A，123不会匹配上
b = a.group()
print(b)
# “+” 匹配前一个字符1次或者无限次
a = re.match(r"[_a-zA-Z]+","nick")
b = a.group()
print(b)
# “？” 匹配一个字符0次或者1次
a = re.match(r"[0-8]?[0-9]","95")   #(0-8)没有匹配上9
b = a.group()
print(b)
# {m} {m,n} 匹配前一个字符m次或者m到n次
a = re.match(r"[\w]{6,10}@qq.com","630571017@qq.com")
b = a.group()
print(b)
# *? +? ?? 匹配模式变为非贪婪（尽可能少匹配字符串）
a = re.match(r"[0-9][a-z]*?","9nick")
b = a.group()
print(b)
a = re.match(r"[0-9][a-z]+?","9nick")
b = a.group()
print(b)

# "^" 匹配字符串开头,多行模式中匹配每一行的开头。
li = "nick\nnjenny\nsuo"
a = re.search("^s.*",li,re.M)
b = a.group()
print(b)
# "$" 匹配字符串结尾,多行模式中匹配每一行的末尾。
li = "nick\njenny\nnick"
a = re.search(".*y$",li,re.M)
b = a.group()
print(b)
# \A 仅匹配字符串开头
li = "nickjennyk"
a = re.findall(r"\Anick",li)
print(a)
# \Z 仅匹配字符串结尾
li = "nickjennyk"
a = re.findall(r"nick\Z",li)
print(a)
# \b 匹配一个单词边界，也就是指单词和空格间的位置
a = re.search(r"\bnick\b","jenny nick car")
b = a.group()
print(b)

# "|" 匹配左右任意一个表达式
a = re.match(r"nick|jenny","jenny")
b = a.group()
print(b)
# (ab) 括号中表达式作为一个分组
a = re.match(r"[\w]{6,10}@(qq|163).com","630571017@qq.com")
b = a.group()
print(b)
# \<number> 引用编号为num的分组匹配到的字符串
a = re.match(r"<([\w]+>)[\w]+</\1","<book>nick</book>")
b = a.group()
print(b)
# (?P<key>vlace) 匹配输出字典
li = 'nick jenny nnnk'
a = re.match("(?P<k1>n)(?P<k2>\w+).*(?P<k3>n\w+)",li)
print(a.groupdict())
# (?P<name>) 分组起一个别名
# (?P=name) 引用别名为name的分组匹配字符串
a = re.match(r"<(?P<jenny>[\w]+>)[\w]+</(?P=jenny)","<book>nick</book>")
b = a.group()
print(b)

######## 模块方法介绍 #########
# match 从头匹配
# search 匹配整个字符串，直到找到一个匹配
# findall 找到匹配，返回所有匹配部分的列表
# findall 加括号
li = 'nick jenny nick car girl'
r = re.findall('n\w+',li)
print(r)
#输出结果：['nick', 'nny', 'nick']
r = re.findall('(n\w+)',li)
print(r)
#输出结果：['nick', 'nny', 'nick']
r = re.findall('n(\w+)',li)
print(r)
#输出结果：['ick', 'ny', 'ick']
r = re.findall('(n)(\w+)(k)',li)
print(r)
#输出结果：[('n', 'ic', 'k'), ('n', 'ic', 'k')]
r = re.findall('(n)((\w+)(c))(k)',li)
print(r)
#输出结果：[('n', 'ic', 'i', 'c', 'k'), ('n', 'ic', 'i', 'c', 'k')]
 
# finditer 返回一个迭代器，和findall一样
li = 'nick jenny nnnk'
a = re.finditer(r'n\w+',li)
for i in a:
    print(i.group())
 
# sub 将字符串中匹配正则表达式的部分替换为其他值
li = 'This is 95'
a = re.sub(r"\d+","100",li)
print(a)
 
li = "nick njenny ncar ngirl"
a = re.compile(r"\bn")
b = a.sub('cool',li,3)      #后边参数替换几次
print(b)
#输出结果：
#coolick cooljenny coolcar ngirl

# split 根据匹配分割字符串，返回分割字符串组成的列表
li = 'nick,suo jenny:nice car'
a = re.split(r":| |,",li)   #或|
print(a)
 
li = 'nick1jenny2car3girl5'
a = re.compile(r"\d")
b = a.split(li)
print(b)
#输出结果:
#['nick', 'jenny', 'car', 'girl', '']   #注意后边空元素

li = 'nick jenny nnnk'
a = re.match("n\w+",li)
print(a.group())
a = re.match("(n)(\w+)",li)
print(a.groups())
a = re.match("(?P<k1>n)(?P<k2>\w+).*(?P<k3>n\w+)",li)
print(a.groupdict())
#-----------------------------------------------
a = "123abc456"
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456
#group(1) #列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3)列出第三个括号匹配部分。

#re.I   使匹配对大小写不敏感
a = re.search(r"nick","NIck",re.I)
print(a.group())
#re.L   做本地化识别（locale-aware）匹配
#re.U   根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
#re.S：.将会匹配换行符，默认.逗号不会匹配换行符
a = re.findall(r".","nick\njenny",re.S)
print(a)
# 输出结果:
# ['n', 'i', 'c', 'k', '\n', 'j', 'e', 'n', 'n', 'y'] 
#re.M：^$标志将会匹配每一行，默认^只会匹配符合正则的第一行；默认$只会匹配符合正则的末行
n = """12 drummers drumming,
11 pipers piping, 10 lords a-leaping""" 
p = re.compile("^\d+")
p_multi = re.compile("^\d+",re.M)
print(re.findall(p,n))
print(re.findall(p_multi,n))

#常见正则列子：
# 匹配手机号
phone_num = '13001000000'
a = re.compile(r"^1[\d+]{10}")
b = a.match(phone_num)
print(b.group())
# 匹配IP地址
ip = '192.168.1.1'
a = re.compile(r"(((1?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}((1?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5]))$")
b = a.search(ip)
print(b.group())
# 匹配 email
email = '630571017@qq.com'
a = re.compile(r"(.*){0,26}@(\w+){0,20}.(\w+){0,8}")
b = a.search(email)
print(b.group())

#####字符串格式化
##百分号方式
tpl = "i am %s" % "nick"
print tpl
tpl = "i am %s age %d" % ("nick", 18)
print tpl
tpl = "i am %(name)s age %(age)d" % {"name": "nick", "age": 18}
print tpl
tpl = "percent %.2f" % 99.97623
print tpl 
tpl = "i am %(pp).2f" % {"pp": 123.425556, }
print tpl
# tpl = "i am %.2f %%" % {"pp": 123.425556, }

##Format方式
tpl = "i am {}, age {}, {}".format("nick", 18, 'jenny')
print tpl
tpl = "i am {}, age {}, {}".format(*["nick", 18, 'jenny'])
print tpl
tpl = "i am {0}, age {1}, really {0}".format("nick", 18)
print tpl
tpl = "i am {0}, age {1}, really {0}".format(*["nick", 18])
print tpl
tpl = "i am {name}, age {age}, really {name}".format(name="nick", age=18)
print tpl
tpl = "i am {name}, age {age}, really {name}".format(**{"name": "nick", "age": 18})
print tpl
tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
print tpl
tpl = "i am {:s}, age {:d}, money {:f}".format("nick", 18, 88888.1)
print tpl
tpl = "i am {:s}, age {:d}, money {:0.2f}".format("nick", 18, 88888.111111111111)
print tpl
tpl = "i am {:s}, age {:d}".format(*["nick", 18])
print tpl
tpl = "i am {name:s}, age {age:d}".format(name="nick", age=18)
print tpl
tpl = "i am {name:s}, age {age:d}".format(**{"name": "nick", "age": 18})
print tpl
tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print tpl
tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
print tpl
tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
print tpl