#!/usr/bin/python
#coding:utf-8

print "Hello World!"
print("Hello World!")
print("你好 世界!")

# sys.argv 用来捕获执行执行python脚本时传入的参数
import sys
print sys.argv[0]

# 输入
name = raw_input("请输入用户名:")
print name

# 输入密码时，如果想要不可见，需要利用getpass 模块中的 getpass方法
import getpass
pwd = getpass.getpass("请输入密码：")
print pwd

# break用于退出当层循环
num = 1
while num <6:
    print(num)
    num+=1
    break
    print("end")
    
# continue用于退出当前循环，继续下一次循环
num = 1
while num <6:
    print(num)
    num+=1
    continue
    print("end")