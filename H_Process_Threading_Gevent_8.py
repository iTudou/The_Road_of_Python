#!/usr/bin/python
#coding:utf-8

#####线程@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Threading用于提供线程相关的操作。线程是应用程序中工作的最小单元，它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。
# threading 模块建立在 _thread 模块之上。thread 模块以低级、原始的方式来处理和控制线程，而 threading 模块通过对 thread 进行二次封装，提供了更方便的 api 来处理线程。
import threading
import time
def worker(num):
    time.sleep(1)
    print(num)
    return
for i in range(10):
    t = threading.Thread(target=worker, args=(i,), name="t.%d" % i)
    t.start()
    
# 继承式调用
class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
  
    def run(self):    #定义每个线程要运行的函数
        print("running on number:%s" %self.num)
        time.sleep(2)
if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
    
# thread方法：
# t.start() : 激活线程
# t.getName() : 获取线程的名称
# t.setName() ： 设置线程的名称 
# t.name : 获取或设置线程的名称
# t.is_alive() ： 判断线程是否为激活状态
# t.isAlive() ：判断线程是否为激活状态
# t.setDaemon() 设置为后台线程或前台线程（默认：False）;通过一个布尔值设置线程是否为守护线程，必须在执行start()方法之前才可以使用。如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止；如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
# t.isDaemon() ： 判断是否为守护线程
# t.ident ：获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None
# t.join() ：逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义
# t.run() ：线程被cpu调度后自动执行线程对象的run方法

##线程锁
# threading.RLock & threading.Lock
# 我们使用线程对数据进行操作的时候，如果多个线程同时修改某个数据，可能会出现不可预料的结果，为了保证数据的准确性，引入了锁的概念。

num = 0
lock = threading.RLock()    # 实例化锁类
def work():
    lock.acquire()  # 加锁
    global num
    num += 1
    time.sleep(1)
    print(num)
    lock.release()  # 解锁
for i in range(10):
    t = threading.Thread(target=work)
    t.start()
    
# threading.RLock和threading.Lock 的区别
# RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。 如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的锁。
# lock = threading.Lock()
# lock.acquire()
# lock.acquire()  # 产生死锁
# lock.release()
# lock.release()
# 
# rlock = threading.RLock()
# rlock.acquire()
# rlock.acquire()      # 在同一线程内，程序不会堵塞。
# rlock.release()
# rlock.release()
# print("end.")

#threading.Event
# Event是线程间通信最间的机制之一：一个线程发送一个event信号，其他的线程则等待这个信号。用于主线程控制其他线程的执行。 Events 管理一个flag，这个flag可以使用set()设置成True或者使用clear()重置为False，wait()则用于阻塞，在flag为True之前。flag默认为False。
# Event.wait([timeout]) ： 堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）
# Event.set() ：将标识位设为Ture
# Event.clear() ： 将标识伴设为False
# Event.isSet() ：判断标识位是否为Ture
# def do(event):
#     print('start')
#     event.wait()
#     print('execute')
# event_obj = threading.Event()
# for i in range(10):
#     t = threading.Thread(target=do, args=(event_obj,))
#     t.start()
# event_obj.clear()
# inp = input('input:')
# if inp == 'true':
#     event_obj.set()
    
import logging  
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)  
def workerr(event):  
    logging.debug('Waiting for redis ready...')  
    event.wait()  
    logging.debug('redis ready, and connect to redis server and do some work [%s]', time.ctime())  
    time.sleep(1)  
readis_ready = threading.Event()  
t1 = threading.Thread(target=workerr, args=(readis_ready,), name='t1')  
t1.start()  
t2 = threading.Thread(target=workerr, args=(readis_ready,), name='t2')  
t2.start()  
logging.debug('first of all, check redis server, make sure it is OK, and then trigger the redis ready event')  
time.sleep(5) # simulate the check progress   
readis_ready.set()