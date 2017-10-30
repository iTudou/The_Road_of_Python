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
