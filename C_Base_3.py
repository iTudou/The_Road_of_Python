#!/usr/bin/python
#coding:utf-8

##### 深浅拷贝
#数字字符串 ：对于 数字 和 字符串 而言，赋值、浅拷贝和深拷贝无意义，因为其永远指向同一个内存地址。
import copy
#定义变量   数字、字符串
n1 = 123
#n1 = 'nick'
print(id(n1))
#赋值
n2 = n1
print(id(n2))
#浅拷贝
n3 = copy.copy(n1)
print(id(n3))
#深拷贝
n4 = copy.deepcopy(n1)
print(id(n4))
#字典、元祖、列表:对于字典、元祖、列表 而言，进行赋值、浅拷贝和深拷贝时，其内存地址的变化是不同的
n1 = {"k1": "nick", "k2": 123, "k3": ["jenny", 666]}
n2 = n1
print(id(n1))
print(id(n2))
  
n1 = {"k1": "nick", "k2": 123, "k3": ["jenny", 666]}
n2 = copy.copy(n1)
print(id(n1))
print(id(n2))
#浅拷贝:在内存中只额外创建第一层数据
n1 = {"k1": "nick", "k2": 123, "k3": ["jenny", 666]}
n2 = copy.copy(n1)
print(id(n1))
print(id(n2))
print(id(n1["k3"]))
print(id(n2["k3"]))
#深拷贝:在内存中将所有的数据重新创建一份（排除最后一层，即：python内部对字符串和数字的优化
n1 = {"k1": "nick", "k2": 123, "k3": ["jenny", 666]}
n2 = copy.deepcopy(n1)
print(id(n1))
print(id(n2))
print(id(n1["k3"]))
print(id(n2["k3"]))

#####函数
###普通参数
def name(n):    #n 叫做函数 name 的形式参数，简称：形参
    print(n)
name('nick')    #'nick' 叫做函数 name 的实际参数，简称：实参

###默认参数
def func(name, age = 18):
    print("%s:%s")%(name,age)
func('nick', 19)    # 指定参数
func('nick')        # 使用默认参数

###动态参数
def func3(*args):
    print args
# 执行方式一
func3(11,22,33,55,66)
# 执行方式二
li = [11,22,33,55,66]
func3(*li)

def func4(**kwargs):
    print kwargs
# 执行方式一
# func4({'name':'nick','age':18})
# 执行方式二
li = {'name':'nick', 'age':18, 'job':'pythoner'}
func4(**li)

def hi(a,*args,**kwargs):
    print(a,type(a))
    print(args,type(args))
    print(kwargs,type(kwargs))
hi(11,22,33,k1='nick',k2='jenny')

#发送邮件实例
# def mail(mainobject,mail_context='test',mail_receiver='liwenzhen238@163.com'):
#     import smtplib
#     import smtplib
#     from email.mime.text import MIMEText
#     from email.utils import formataddr
# 
#     msg = MIMEText(mail_context, 'plain', 'utf-8')
#     msg['From'] = formataddr(["发件人", '发件人地址'])
#     msg['To'] = formataddr(["收件人", 'liwenzhen238@163.com'])
#     msg['Subject'] = mainobject
# 
#     server = smtplib.SMTP("smtp.sina.com", 25)
#     server.login("登录邮箱账号", "邮箱密码")
#     server.sendmail('发件邮箱地址账号', [收件人地址, ], msg.as_string())
#     server.quit()
# 
# mail('我是主题',mail_receiver='liwenzhen238@163.com',mail_context='邮件内容')
# mail(mainobject='我是主题',)

##全局与局部变量     全局变量在函数里可以随便调用，但要修改就必须用 global 声明
P = 'nick'
def NAME():
    global P        #声明修改全局变量
    P = 'jenny'     #局部变量
    print(P)
def NAME2():
    print(P)
NAME()
NAME2()

##内置函数
###### 求绝对值 #######
a = abs(-95)
print(a)
###### 只有一个为假就为假 ########
a = all([True,True,False])
print(a)
###### 只有一个为真就为真 ########
a = any([False,True,False])
print(a)
####### 返回一个可打印的对象字符串方式表示 ########
# a = ascii('0x\10000')
# b = ascii('b\x19')
# print(a,b)
######### 将整数转换为二进制字符串 ############
a = bin(95)
print(a)
######### 将一个数字转化为8进制 ##############
a = oct(95)
print(a)
######### 将一个数字转化为10进制 #############
a = int(95)
print(a)
######### 将整数转换为16进制字符串   ##########
a = hex(95)
print(a)
######### 转换为布尔类型 ###########
a = bool('')
print(a)
######### 转换为bytes ########
# a = bytes('索宁',encoding='utf-8')
# print(a)
######## chr 返回一个字符串，其ASCII码是一个整型.比如chr(97)返回字符串'a'。参数i的范围在0-255之间。 #######
a = chr(88)
print(a)
######## ord 参数是一个ascii字符，返回值是对应的十进制整数 #######
a = ord('X')
print(a)
######## 创建数据字典 ########
dict({'one': 2, 'two': 3})
dict(zip(('one', 'two'), (2, 3)))
dict([['two', 3], ['one', 2]])
dict(one=2, two=3)
###### dir 列出某个类型的所有可用方法 ########
a = dir(list)
print(a)
###### help 查看帮助文档 #########
help(list)
####### 分别取商和余数 ######
a = divmod(9,5)
print(a)
##### 计算表达式的值 #####
a = eval('1+2*2')
print(a)
###### exec 用来执行储存在字符串或文件中的Python语句 ######
# exec(print("Hi,girl."))
# exec("print(\"hello, world\")")
####### filter 过滤 #######
li = [1,2,3,4,5,6]
a = filter(lambda x:x>3,li)
for i in a:print(i)
##### float 浮点型 #####
a = float(1)
print(a)
###### 判断对象是不是属于int实例  #########
a = 5
b = isinstance(a,int)
print(b)
######## globals 返回全局变量 ########
######## locals 返回当前局部变量 ######
name = 'nick'
def HH():
    a = 1
    print(locals())
HH()
print(globals())
########## map 遍历序列，对序列中每个元素进行操作，最终获取新的序列。 ##########
li =  [11,22,33]
def func1(arg):
    return arg + 1  #这里乘除都可以
new_list = map(func1,li)  #这里map调用函数，函数的规则你可以自己指定，你函数定义成什么他就做什么操作！
for i in new_list:print(i)
###### max 返回集合中的最大值 ######
###### min 返回集合中的最小值 ######
a = [1,2,3,4,5]
s = max(a)
print(s)
n = min(a)
print(n)
####### pow 返回x的y次幂 ########
a = pow(2,10)
print(a)
a = pow(2,10,100)   #等于2**10%100，取模
print(a)
######## round 四舍五入 ########
a = round(9.5)
print(a)
######## sorted 队集合排序 ########
# char=['索',"123", "1", "25", "65","679999999999", "a","B","nick","c" ,"A", "_", "ᒲ",'a钱','孙','李',"余", '佘',"佗", "㽙", "铱", "啊啊啊啊"]
# new_chat = sorted(char)
# print(new_chat)
# for i in new_chat:
#     print(bytes(i, encoding='utf-8'))
######## sum 求和的内容 ########
a = sum([1,2,3,4,5])
print(a)
a = sum(range(6))
print(a)
######## __import__ 通过字符串的形式，导入模块 ########
# 通过字符串的形式，导入模块。起个别名ccas
# comm = input("Please:")
# ccas = __import__(comm)
# ccas.f1()
# # 需要做拼接时后加 fromlist=True
# m = __import__("lib."+comm, fromlist=True)
# lt(a, b) 相当于 a < b
# le(a,b) 相当于 a <= b
# eq(a,b) 相当于 a == b
# ne(a,b) 相当于 a != b
# gt(a,b) 相当于 a > b
# ge(a, b)相当于 a>= b
########    zip函数    ########
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print xyz
x = [1, 2, 3]
y = [4, 5, 6, 7]
xy = zip(x, y)
print xy
x = [1, 2, 3]
x = zip(x)
print x
x = zip()
print x
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
u = zip(*xyz)
print u
x = [1, 2, 3]
r = zip(* [x] * 3)
print r

##文件处理
###### w 写(会先清空！！！) ######
f = open('test.log','w')
a = f.write('car.\n索宁')
print(a)    #返回字符
####### r 读 #######
f = open('test.log','r')
a = f.read()
print(a)
####### a 追加（指针会先移动到最后） ########
f = open('test.log','a')
a = f.write('girl\n索宁')
print(a)    #返回字符
####### 读写 r+ ########
f = open('test.log','r+')
a = f.read()
print(a)
f.write('nick')
##### 写读 w+（会先清空！！！） ######
f = open('test.log','w+')
a = f.read()
print(a)
f.write('jenny')
######## 写读 a+（指针先移到最后） #########
f = open('test.log','a+')
f.seek(0)   #指针位置调为0
a = f.read()
print(a)
b = f.write('nick')
print(b)
####### rb #########
f = open('test.log','rb')
a = f.read()
print(str(a))
# ######## ab #########
f = open('test.log','ab')
f.write(bytes('索宁\ncar'))
f.write(b'jenny')
##### 关闭文件 ######
f.close()
# ##### 内存刷到硬盘 #####
# f.flush()
# ##### 获取指针位置 #####
# f.tell()
# ##### 指定文件中指针位置 #####
# f.seek(0)
# ###### 读取全部内容(如果设置了size，就读取size字节) ######
# f.read()
# f.read(9)
# ###### 读取一行 #####
# f.readline()
# ##### 读到的每一行内容作为列表的一个元素 #####
# f.readlines()
###### 从一文件挨行读取并写入二文件 #########
with open('test.log','r') as obj1 , open('test1.log','w') as obj2:
    for line in obj1:
        obj2.write(line)
        
##三元运算
name="nick" if 1==1 else "jenny"
print(name)

##lambda表达式
my_lambda = lambda arg : arg + 1
result = my_lambda(123)
print result
li = [11,15,9,21,1,2,68,95]
s = sorted(map(lambda x:x if x > 11 else x * 9,li))
print(s)
ret = sorted(filter(lambda x:x>22, [55,11,22,33,]))
print(ret)

##递归
def fact_iter(product,count_1,max_1):
    if count_1 > max_1:
        return product
    return fact_iter(product * count_1, count_1+1, max_1)
 
print(fact_iter(1,1,5))
print(fact_iter(1,2,5))
print(fact_iter(2,3,5))
print(fact_iter(6,4,5))
print(fact_iter(24,5,5))
print(fact_iter(120,6,5))
#递归编写斐波那契数列
def funx(arg1,arg2):
    if arg1 == 0:
        print arg1, arg2
    arg3 = arg1 + arg2
    print arg3
    funx(arg2, arg3)
# funx(0,1)
#写函数，利用递归获取斐波那契数列中的第 10 个数
#方法一
def fie(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fie(n-1)+fie(n-2))
ret = fie(10)
print(ret)