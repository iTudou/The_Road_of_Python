#!/usr/bin/python
#coding:utf-8

#####模块介绍@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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

#####time & datetime 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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

#####random 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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

#####os模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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
    
#####json & picle 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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

#####XML 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from xml.etree import ElementTree
############ 解析方式一 ############
# 打开文件，读取XML内容
str_xml = open('LPSX_1.xml', 'r').read()
# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root = ElementTree.XML(str_xml)

##修改节点内容
# 循环所有的year节点
for node in root.iter('year'):
    # 将year节点中的内容自增一
    new_year = int(node.text) + 1
    node.text = str(new_year)
    # 设置属性
    node.set('name', 'alex')
    node.set('age', '18')
    # 删除属性
    del node.attrib['name']
##删除节点
# 遍历data下的所有country节点
for country in root.findall('country'):
    # 获取每一个country节点下rank节点的内容
    rank = int(country.find('rank').text)

    if rank > 50:
        # 删除指定country节点
        root.remove(country)
############ 保存文件 ############
tree = ElementTree.ElementTree(root)
tree.write("newnew.xml", encoding='utf-8')

############ 解析方式二 ############
# 直接解析xml文件
tree = ElementTree.parse("LPSX_1.xml")
# 获取xml文件的根节点
root = tree.getroot()

##修改节点内容
# 循环所有的year节点
for node in root.iter('year'):
    # 将year节点中的内容自增一
    new_year = int(node.text) + 1
    node.text = str(new_year)
    # 设置属性
    node.set('name', 'alex')
    node.set('age', '18')
    # 删除属性
    del node.attrib['name']
##删除节点
# 遍历data下的所有country节点
for country in root.findall('country'):
    # 获取每一个country节点下rank节点的内容
    rank = int(country.find('rank').text)
    if rank > 50:
        # 删除指定country节点
        root.remove(country)
############ 保存文件 ############
tree.write("newnew.xml", encoding='utf-8')

### 操作
# 顶层标签
print(root.tag)

# 遍历XML文档的第二层
for child in root:
    # 第二层节点的标签名称和标签属性
    print(child.tag, child.attrib)
    # 遍历XML文档的第三层
    for i in child:
        # 第二层节点的标签名称和内容
        print(i.tag,i.text)
        
# 遍历XML中所有的year节点
for node in root.iter('year'):
    # 节点的标签名称和内容
    print(node.tag, node.text)
    
##3、创建XML文档
from xml.etree import ElementTree as ET
#######方法一#######
# 创建根节点
root = ET.Element("famliy")
# 创建节点大儿子
son1 = ET.Element('son', {'name': 'son1'})
# 创建小儿子
son2 = ET.Element('son', {"name": 'son2'})
# 在大儿子中创建两个孙子
grandson1 = ET.Element('grandson', {'name': 'son11'})
grandson2 = ET.Element('grandson', {'name': 'son12'})
son1.append(grandson1)
son1.append(grandson2)
# 把儿子添加到根节点中
root.append(son1)
root.append(son2)
tree = ET.ElementTree(root)
tree.write('oooo.xml',encoding='utf-8')
#######方法二#######
# 创建根节点
root = ET.Element("famliy")
# 创建大儿子
son1 = root.makeelement('son', {'name': 'son1'})
# 创建小儿子
son2 = root.makeelement('son', {"name": 'son2'})
# 在大儿子中创建两个孙子
grandson1 = son1.makeelement('grandson', {'name': 'son11'})
grandson2 = son1.makeelement('grandson', {'name': 'son12'})
son1.append(grandson1)
son1.append(grandson2)
# 把儿子添加到根节点中
root.append(son1)
root.append(son2)
tree = ET.ElementTree(root)
tree.write('oooo.xml',encoding='utf-8')
#######方法三#######
# 创建根节点
root = ET.Element("famliy")
# 创建节点大儿子
son1 = ET.SubElement(root, "son", attrib={'name': 'son1'})
# 创建小儿子
son2 = ET.SubElement(root, "son", attrib={"name": "son2"})
# 在大儿子中创建一个孙子
grandson1 = ET.SubElement(son1, "age", attrib={'name': 'son11'})
grandson1.text = 'sonson'
et = ET.ElementTree(root)  #生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

#由于原生保存的XML时默认无缩进，如果想要设置缩进的话， 需要修改保存方式：
from xml.dom import minidom
def prettify(elem):
    """将节点转换成字符串，并添加缩进。
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")
# 创建根节点
root = ET.Element("famliy")
# 创建大儿子
son1 = root.makeelement('son', {'name': 'son1'})
# 创建小儿子
son2 = root.makeelement('son', {"name": 'son2'})
# 在大儿子中创建两个孙子
grandson1 = son1.makeelement('grandson', {'name': 'son11'})
grandson2 = son1.makeelement('grandson', {'name': 'son12'})
son1.append(grandson1)
son1.append(grandson2)
# 把儿子添加到根节点中
root.append(son1)
root.append(son1)
raw_str = prettify(root)
f = open("xxxoo.xml",'w')
f.write(raw_str)
f.close()

##4、命名空间
ET.register_namespace('com',"http://www.company.com") #some name
# build a tree structure
root = ET.Element("{http://www.company.com}STUFF")
body = ET.SubElement(root, "{http://www.company.com}MORE_STUFF", attrib={"{http://www.company.com}hhh": "123"})
body.text = "STUFF EVERYWHERE!"
# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)
tree.write("page.xml",
           xml_declaration=True,
           encoding='utf-8',
           method="xml")

#####requests 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Python标准库中提供了：urllib等模块以供Http请求，但是，它的 API 太渣了。它是为另一个时代、另一个互联网所创建的。它需要巨量的工作，甚至包括各种方法覆盖，来完成最简单的任务。
#Requests 是使用 Apache2 Licensed 许可证的 基于Python开发的HTTP 库，其在Python内置模块的基础上进行了高度的封装，从而使得Pythoner进行网络请求时，变得美好了许多，使用Requests可以轻而易举的完成浏览器可有的任何操作。
##使用模块
#GET请求
# 1、无参数实例
import requests
ret = requests.get('https://github.com/timeline.json')
print(ret.url)
print(ret.text)
# 2、有参数实例
payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.get("http://httpbin.org/get", params=payload)
print(ret.url)
print(ret.text)

#POST请求
# 1、基本POST实例
payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.post("http://httpbin.org/post", data=payload)
print(ret.text)
# 2、发送请求头和数据实例
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
ret = requests.post(url, data=json.dumps(payload), headers=headers)
print(ret.text)
print(ret.cookies)

#其他请求
# requests.get(url, params=None, **kwargs)
# requests.post(url, data=None, json=None, **kwargs)
# requests.put(url, data=None, **kwargs)
# requests.head(url, **kwargs)
# requests.delete(url, **kwargs)
# requests.patch(url, data=None, **kwargs)
# requests.options(url, **kwargs)
# # 以上方法均是在此方法的基础上构建
# requests.request(method, url, **kwargs)
#更多requests模块相关的文档见：http://cn.python-requests.org/zh_CN/latest/

##Http请求和XML实例
#检测QQ账号是否在线
# 使用内置模块urllib发送HTTP请求，或者XML格式内容
# """
# f = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=630571017')
# result = f.read().decode('utf-8')
# """
# # 使用第三方模块requests发送HTTP请求，或者XML格式内容
# r = requests.get('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
# result = r.text
# # 解析XML格式内容
# node = ET.XML(result)
# # 获取内容
# if node.text == "Y":
#     print("在线")
# else:
#     print("离线")

#查看火车停靠信息
# 使用内置模块urllib发送HTTP请求，或者XML格式内容
# """
# f = urllib.request.urlopen('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=G666&UserID=')
# result = f.read().decode('utf-8')
# """
# # 使用第三方模块requests发送HTTP请求，或者XML格式内容
# r = requests.get('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=G666&UserID=')
# result = r.text
# # 解析XML格式内容
# root = ET.XML(result)
# for node in root.iter('TrainDetailInfo'):
#     print(node.find('TrainStation').text,node.find('StartTime').text,node.tag,node.attrib)

#查看天气信息
response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")
response.encoding = "utf-8"
result = response.text
print(result)

#####configparser 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#configparser用于处理特定格式的文件，其本质上是利用open来操作文件。
#1、获取所有节点
import ConfigParser
con = ConfigParser.ConfigParser()
con.read("ini")
result = con.sections()
print(result)
#2、获取指定节点下所有的键值对
# con = ConfigParser.ConfigParser()
# con.read("ini")
# result = con.items("nick")
# print(result)
#3、获取指定节点下所有的键
# con = ConfigParser.ConfigParser()
# con.read("ini")
# ret = con.options("nick")
# print(ret)
#4、获取指定节点下指定key的值
# con = ConfigParser.ConfigParser()
# con.read("ini",encoding="utf-8")
# v = con.get("nick","age")
# v = con.get("nick","gender")
# v = con.get("jenny","age")
# v = con.get("jenny","gender")
# print(v)
#5、检查、删除、添加节点
#检查、删除、添加节点
# con = ConfigParser.ConfigParser()
# con.read("ini")
# #检查
# has_sec = con.has_section("nick")
# print(has_sec)
# #添加节点
# con.add_section("car")
# con.write(open("ini","w"))
# #删除节点
# con.remove_section("car")
# con.write(open("ini","w"))
#6、检查、删除、设置指定组内的键值对
#检查、删除、设置指定组内的键值对
# con = ConfigParser.ConfigParser()
# con.read("ini",encoding="utf-8")
# #检查
# hac_opt = con.has_option("nick","age")
# print(hac_opt)
# #删除
# con.remove_option("nick","dearm")
# con.write(open("ini","w"))
# #设置
# con.set("nick","dearm","girl")
# con.write(open("ini","w"))

#####logging 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#用于便捷记录日志且线程安全的模块
import logging
#1、单日志文件
logging.basicConfig(filename="log.log",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S %p",
                    level=logging.INFO)
 
logging.critical("critical")
logging.fatal("fatal")
logging.error("error")
logging.warn("warn")
logging.warning("warning")
logging.info("info")
logging.debug("debug")
logging.log(8,"log")
#日志等级
"""
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
"""
#注：只有【当前写等级】大于【日志等级】时，日志文件才被记录。

#2、多文件日志
#对于上述记录日志的功能，只能将日志记录在单文件中，如果想要设置多个日志文件，logging.basicConfig将无法完成，需要自定义文件和日志操作对象。
#日志(一)
# 定义文件
file_1_1 = logging.FileHandler('l1_1.log', 'a')
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
file_1_1.setFormatter(fmt)
file_1_2 = logging.FileHandler('l1_2.log', 'a')
fmt = logging.Formatter()
file_1_2.setFormatter(fmt)
# 定义日志
logger1 = logging.Logger('s1', level=logging.ERROR)
logger1.addHandler(file_1_1)
logger1.addHandler(file_1_2)
# 写日志
logger1.critical('1111')
#日志(二)
# 定义文件
file_2_1 = logging.FileHandler('l2_1.log', 'a')
fmt = logging.Formatter()
file_2_1.setFormatter(fmt)
# 定义日志
logger2 = logging.Logger('s2', level=logging.INFO)
logger2.addHandler(file_2_1)

# 如上述创建的两个日志对象
# 当使用【logger1】写日志时，会将相应的内容写入 l1_1.log 和 l1_2.log 文件中
# 当使用【logger2】写日志时，会将相应的内容写入 l2_1.log 文件中

#记录日志及按天切割实例
# from logging.handlers import TimedRotatingFileHandler
#     base = os.path.abspath(os.path.dirname(__file__))
#     logfile = os.path.join(base, 'test', 'testlog')
#     handler = TimedRotatingFileHandler(filename=logfile, when='MIDNIGHT',
#                                                       interval=1, backupCount=365)
#     handler.suffix = "%Y%m%d.log"
#     handler.setFormatter(logging.Formatter('%(asctime)s\t%(levelname)-8s\t%(message)s'))
#     handler.setLevel(logging.DEBUG)
#     apipartnerlogger = logging.getLogger(logfile)
#     apipartnerlogger.addHandler(handler)
#     apipartnerlogger.setLevel(logging.INFO)

#####shutil 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#高级的 文件、文件夹、压缩包 处理模块
import shutil
#shutil.copyfileobj(fsrc, fdst[, length])    将文件内容拷贝到另一个文件中
shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))
#shutil.copyfile(src, dst)                    拷贝文件
shutil.copyfile('f1.log', 'f2.log')
#shutil.copymode(src, dst)                    仅拷贝权限。内容、组、用户均不变
shutil.copymode('f1.log', 'f2.log')
