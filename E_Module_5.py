#!/usr/bin/python
#coding:utf-8

#####模块介绍
#获取路径
import sys
for i in sys.path:
    print(i)
#输出结果：
# S:\Myproject
# S:\Python 3.5.1\python35.zip
# S:\Python 3.5.1\DLLs
# S:\Python 3.5.1\lib                  #存放标准库
# S:\Python 3.5.1
# S:\Python 3.5.1\lib\site-packages    #存放第三方库，扩充库

#添加路径
import os
pre_path = os.path.abspath('../')
sys.path.append(pre_path)

#开源模块：
#先安装 gcc 编译和 python 开发环境
# yum install gcc
# yum install python-devel
# 或
# apt-get python-dev
# #安装方式（安装成功后，模块会自动安装到 sys.path 中的某个目录中）
# yum
# pip
# apt-get
# ...
# #进入python环境，导入模块检查是否安装成功

#####time & datetime 模块
import time
print time.time()                               #返回当前系统时间戳（1970年1月1日0时0分0秒开始）
print time.ctime()                              #输出Tue May 17 16:07:11 2016，当前系统时间
print time.ctime(time.time() - 86400)           #将时间戳转换为字符串格式
print time.gmtime(time.time() - 86400)          #将时间戳转换为struct_time格式
print time.localtime(time.time() - 86400)       #将时间戳转换为struct_time格式，返回本地时间
print time.mktime(time.localtime())             #与time.localtime()功能相反，将struct_time格式转回成时间戳格式
print time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())  #将struct_time格式转成指定的字符串格式
print time.strptime("2016-05-17","%Y-%m-%d")            #将字符串格式转换成struct_time格式
print("----------------------------------------------------------------")
import datetime
print datetime.date.today()                             #输出格式 2016-05-17
print datetime.date.fromtimestamp(time.time() - 86400)  #2016-05-16 将时间戳转成日期格式
current_time = datetime.datetime.now()
print current_time
print current_time.timetuple()                          #返回struct_time格式
print current_time.replace(2008,8,8)                    #输出2008-08-08 16:21:34.798203,返回当前时间,但指定的值将被替换
str_to_date = datetime.datetime.strptime("28/7/08 11:20","%d/%m/%y %H:%M")  #将字符串转换成日期格式
print str_to_date
new_date = datetime.datetime.now() + datetime.timedelta(days=10)    #比现在加10天
print new_date
new_date = datetime.datetime.now() + datetime.timedelta(days=-10)   #比现在减10天
print new_date
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10)  #比现在减10小时
print new_date
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120)#比现在+120s
print new_date

#####random 模块
##随机数
import random
print(random.random())          #用于生成一个0到1的随机符点数: 0 <= n < 1.0
print(random.randint(1,2))      #用于生成一个指定范围内的整数
print(random.randrange(1,10))   #从指定范围内，按指定基数递增的集合中获取一个随机数
print(random.uniform(1,10))     #用于生成一个指定范围内的随机符点数
print(random.choice('nick'))    #从序列中获取一个随机元素
li = ['nick','jenny','car',]
random.shuffle(li)              #用于将一个列表中的元素打乱
print(li)
li_new = random.sample(li,2)    #从指定序列中随机获取指定长度的片断(从li中随机获取2个元素，作为一个片断返回)
print(li_new)

##生成随机验证码
temp = ''
for i in range(4):
    num = random.randrange(0,4)
    if num == 0 or num == 3:        #一半的概率
        rad2 = random.randrange(0,10)
        temp = temp + str(rad2)
    else:
        rad1 = random.randrange(65,91)
        c1 = chr(rad1)
        temp = temp + c1
print(temp)

##os模块
print os.getcwd()             #获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")         改变当前脚本工作目录；相当于shell下cd
# os.curdir                   返回当前目录: ('.')
# os.pardir                   获取当前目录的父目录字符串名：('..')
# os.makedirs('dir1/dir2')    可生成多层递归目录
# os.removedirs('dirname1')   若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')         生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')         删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')       列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove()                 删除一个文件
# os.rename("oldname","new")  重命名文件/目录
# os.stat('path/filename')    获取文件/目录信息
# os.sep                      操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep                  当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.pathsep                  用于分割文件路径的字符串
# os.name                     字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")   运行shell命令，直接显示
# os.environ                  获取系统环境变量
# os.path.abspath(path)       返回path规范化的绝对路径
# os.path.split(path)         将path分割成目录和文件名二元组返回
# os.path.dirname(path)       返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)      返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)        如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)         如果path是绝对路径，返回True
# os.path.isfile(path)        如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)         如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)      返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)      返回path所指向的文件或者目录的最后修改时间

##sys模块
# sys.argv           命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0)
# sys.version        获取Python解释程序的版本信息
# sys.maxint         最大的Int值
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       返回操作系统平台名称
# sys.stdin          输入相关
# sys.stdout         输出相关
# sys.stderror       错误相关
# 手写进度条
for ii in range(101):
    sys.stdout.write('\r')  #每一次清空原行。
    sys.stdout.write("%s%%  |%s|"%(int(int(ii)/100*100),int(int(ii)/100*100) * '#'))     #一共次数除当前次数算进度
    sys.stdout.flush()      #强制刷新到屏幕
    time.sleep(0.001)
    
##json & picle 模块
# json，用于字符串 和 python数据类型间进行转换
# pickle，用于python特有的类型 和 python的数据类型间进行转换
# Json模块提供了四个功能：dumps、dump、loads、load
# pickle模块提供了四个功能：dumps、dump、loads、load
# dump()函数接受一个文件句柄和一个数据对象作为参数，把数据对象以特定的格式保存 到给定的文件中。当我们使用load()函数从文件中取出已保存的对象时，pickle知道如何恢复这些对象到它们本来的格式。
# dumps()函数执行和dump() 函数相同的序列化。取代接受流对象并将序列化后的数据保存到磁盘文件，这个函数简单的返回序列化的数据。
# loads()函数执行和load() 函数一样的反序列化。取代接受一个流对象并去文件读取序列化后的数据，它接受包含序列化后的数据的str对象, 直接返回的对象

import pickle
data = {'k1':123,'k2':'Hello'}
#pickle.dumps 将数据通过特殊的形式转换为只有python语言认识的字符串 
p_str = pickle.dumps(data)
print p_str
#pickle.dumps 将数据通过特殊的形式转换为只有python语言认识的字符串 ,并写入文件
with open('D:/python/The_Road_of_Python/result.pk','w') as fp:
    pickle.dump(data,fp)
import json
#json.dumps 将数据通过特殊的形式转换为所有语言认识的字符串 
j_str = json.dumps(data)
print j_str
#json.dump 将数据通过特殊的形式转换为所有语言认识的字符串 ，并写入文件
with open('D:/python/The_Road_of_Python/result.json','w') as fp:
    json.dump(j_str,fp)
print '-------------------------------------------------'
##### json.loads 将字符串转换为python基本数据类型 列表字典 #####
l = '["nick","jenny","car"]'
print(l,type(l))
l = json.loads(l)
print(l,type(l))
 
l = '{"k1":"nick","k2:":"jenny"}'
print(l,type(l))
l = json.loads(l)
print(l,type(l))
 
##### json.dumps 将python的数据类型列表字典转换为字符串 ######
l = ["nick","jenny","car"]
print(l,type(l))
l = json.dumps(l)
print(l,type(l))
 
l = {"k1":"nick","k2:":"jenny"}
print(l,type(l))
l = json.dumps(l)
print(l,type(l))
 
##### json dump、load 文件相关 #####
l = {"k1":"nick","k2:":"jenny"}
json.dump(l,open('db','w'))
 
ret = json.load(open('db'))
print(ret)

#####hashlib 模块
#用于加密相关的操作，代替了md5模块和sha模块，主要提供md5(), sha1(), sha224(), sha256(), sha384(), and sha512()算法
import hashlib

# ######## md5 ########
hashl = hashlib.md5()
# help(hash.update)
hashl.update(bytes('admin'))
print hashl.hexdigest()
print hashl.digest()

######## sha1 ########
hashl = hashlib.sha1()
hashl.update(bytes('admin'))
print hashl.hexdigest()

# ######## sha256 ########
hashl = hashlib.sha256()
hashl.update(bytes('admin'))
print(hashl.hexdigest())

# ######## sha384 ########
hashl = hashlib.sha384()
hashl.update(bytes('admin'))
print(hashl.hexdigest())

# ######## sha512 ########
hashl = hashlib.sha512()
hashl.update(bytes('admin'))
print(hashl.hexdigest())

##### 加盐 ######
# ######## md5 ########
hashl = hashlib.md5(bytes('898oaFs09f'))
hashl.update(bytes('admin'))
print(hashl.hexdigest())
#python内置还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密
import hmac
h = hmac.new(bytes('898oaFs09f'))
h.update(bytes('admin'))
print(h.hexdigest())