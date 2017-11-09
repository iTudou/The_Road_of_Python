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

# threading.Condition
# Python提供的Condition对象提供了对复杂线程同步问题的支持。Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。线程首先acquire一个条件变量，然后判断一些条件。如果条件不满足则wait；如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。不断的重复这一过程，从而解决复杂的同步问题。
# 在典型的设计风格里，利用condition变量用锁去通许访问一些共享状态，线程在获取到它想得到的状态前，会反复调用wait()。修改状态的线程在他们状态改变时调用 notify() or notify_all()，用这种方式，线程会尽可能的获取到想要的一个等待者状态。

def consumer(cond):
    with cond:
        print("consumer before wait")
        cond.wait()
        print("consumer after wait")
  
def producer(cond):
    with cond:
        print("producer before notifyAll")
        cond.notifyAll()
        print("producer after notifyAll")
  
condition = threading.Condition()
c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
c2 = threading.Thread(name="c2", target=consumer, args=(condition,))
p = threading.Thread(name="p", target=producer, args=(condition,))
c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()
# consumer()线程要等待producer()设置了Condition之后才能继续。

# queue 队列
# 适用于多线程编程的先进先出数据结构，可以用来安全的传递多线程信息。
# queue 方法：
# q = queue.Queue(maxsize=0) # 构造一个先进显出队列，maxsize指定队列长度，为0 时，表示队列长度无限制。
# q.join() 　　# 等到队列为kong的时候，在执行别的操作
# q.qsize() 　 # 返回队列的大小 （不可靠）
# q.empty()    # 当队列为空的时候，返回True 否则返回False （不可靠）
# q.full()     # 当队列满的时候，返回True，否则返回False （不可靠）
# q.put(item, block=True, timeout=None) # 将item放入Queue尾部，item必须存在，可以参数block默认为True,表示当队列满时，会等待队列给出可用位置，为False时为非阻塞，此时如果队列已满，会引发queue.Full 异常。 可选参数timeout，表示 会阻塞设置的时间，过后，如果队列无法给出放入item的位置，则引发 queue.Full 异常
# q.get(block=True, timeout=None) # 移除并返回队列头部的一个值，可选参数block默认为True，表示获取值的时候，如果队列为空，则阻塞，为False时，不阻塞，若此时队列为空，则引发 queue.Empty异常。 可选参数timeout，表示会阻塞设置的时候，过后，如果队列为空，则引发Empty异常。
# q.put_nowait(item) # 等效于 put(item,block=False)
# q.get_nowait()     # 等效于 get(item,block=False)

#生产者消费者类型
import Queue
 
que = Queue.Queue(10)
def s(i):
    que.put(i)
    # print("size:", que.qsize())
def x(i):
    g = que.get(i)
    print("get:", g)
for i in range(1, 13):
    t = threading.Thread(target=s, args=(i,))
    t.start()
for i in range(1, 11):
    t = threading.Thread(target=x, args=(i,))
    t.start()
     
print("size:", que.qsize())

#自定义线程池一
class TreadPool:
    def __init__(self, max_num=20):
        self.queue = Queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        return self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)

def func(pool, n):
    time.sleep(1)
    print(n)
    pool.add_thread()

p = TreadPool(10)
for i in range(1, 100):
    thread = p.get_thread()
    t = thread(target=func, args=(p, i,))
    t.start()
    
#自定义线程池二
import contextlib

StopEvent = object()

class Threadpool:

    def __init__(self, max_num=10):
        self.q = Queue.Queue()
        self.max_num = max_num

        self.terminal = False
        self.generate_list = []     # 以创建线程列表
        self.free_list = []         # 以创建的线程空闲列表

    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()
        w = (func, args, callback,)
        self.q.put(w)

    def generate_thread(self):
        """
        创建一个线程
        """
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数
        """
        current_thread = threading.currentThread    # 当前线程
        self.generate_list.append(current_thread)

        event = self.q.get()
        while event != StopEvent:

            func, arguments, callback = event
            try:
                result = func(*arguments)
                status = True
            except Exception as e:
                status = False
                result = e

            if callback is not None:
                try:
                    callback(status, result)
                except Exception as e:
                    pass

            if self.terminal:
                event = StopEvent
            else:
                with self.worker_state(self.free_list, current_thread):
                    event = self.q.get()
                # self.free_list.append(current_thread)
                # event = self.q.get()
                # self.free_list.remove(current_thread)

        else:
            self.generate_list.remove(current_thread)

    def close(self):
        """
        执行完所有的任务后，所有线程停止
        """
        num = len(self.generate_list)
        while num:
            self.q.put(StopEvent)
            num -= 1

    def terminate(self):
        """
        无论是否还有任务，终止线程
        """
        self.terminal = True
        while self.generate_list:
            self.q.put(StopEvent)
        self.q.empty()  # 清空队列

    @contextlib.contextmanager      # with上下文管理
    def worker_state(self, frelist, val):
        """
        用于记录线程中正在等待的线程数
        """
        frelist.append(val)
        try:
            yield
        finally:
            frelist.remove(val)


def work_r(i):
    time.sleep(1)
    print(i)

pool = Threadpool()
for item in range(50):
    pool.run(func=work_r, args=(item,))
pool.close()
# pool.terminate()

#####进程@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from multiprocessing import Process
 
def work_s(name):
    print("Hello, %s" % name)
 
if __name__ == "__main__":
    p = Process(target=work_s, args=("nick",))
    p.start()
    p.join()
    
# 数据共享
# 不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法：
# Shared memory
# 数据可以用Value或Array存储在一个共享内存地图里，如下：
from multiprocessing import Value, Array
def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]
  
if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])
# 创建num和arr时，“d”和“i”参数由Array模块使用的typecodes创建：“d”表示一个双精度的浮点数，“i”表示一个有符号的整数，这些共享对象将被线程安全的处理。

temp = Array('i', [11,22,33,44])
def Foo(i):
    temp[i] = 100+i
    for item in temp:
        print i,'----->',item
  
for i in range(2):
    p = Process(target=Foo,args=(i,))
    p.start()
    
# Server process
# 由Manager()返回的manager提供list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array类型的支持。
from multiprocessing import Manager
def ff(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()
if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        p = Process(target=ff, args=(d, l))
        p.start()
        p.join()
        print(d)
        print(l)
# Server process manager比 shared memory 更灵活，因为它可以支持任意的对象类型。另外，一个单独的manager可以通过进程在网络上不同的计算机之间共享，不过他比shared memory要慢。
# manage.dict()共享数据
# manage = Manager()
# dic = manage.dict()
#   
# def Fooo(i):
#     dic[i] = 100+i
#     print dic.values()
#   
# for i in range(2):
#     p = Process(target=Fooo,args=(i,))
#     p.start()
#     p.join()
# 当创建进程时（非使用时），共享数据会被拿到子进程中，当进程中执行完毕后，再赋值给原值。

# #进程琐实例
# from multiprocessing import RLock
# 
# def Foox(lock,temp,i):
#     """
#     将第0个数加100
#     """
#     lock.acquire()
#     temp[0] = 100+i
#     for item in temp:
#         print i,'----->',item
#     lock.release()
# lock = RLock()
# temp = Array('i', [11, 22, 33, 44])
# for i in range(20):
#     p = Process(target=Foox,args=(lock,temp,i,))
#     p.start()

# 进程池
# 进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。
# 方法:
# apply(func[, args[, kwds]]) ：使用arg和kwds参数调用func函数，结果返回前会一直阻塞，由于这个原因，apply_async()更适合并发执行，另外，func函数仅被pool中的一个进程运行。
# apply_async(func[, args[, kwds[, callback[, error_callback]]]]) ： apply()方法的一个变体，会返回一个结果对象。如果callback被指定，那么callback可以接收一个参数然后被调用，当结果准备好回调时会调用callback，调用失败时，则用error_callback替换callback。 Callbacks应被立即完成，否则处理结果的线程会被阻塞。
# close() ： 阻止更多的任务提交到pool，待任务完成后，工作进程会退出。
# terminate() ： 不管任务是否完成，立即停止工作进程。在对pool对象进程垃圾回收的时候，会立即调用terminate()。
# join() : wait工作线程的退出，在调用join()前，必须调用close() or terminate()。这样是因为被终止的进程需要被父进程调用wait（join等价与wait），否则进程会成为僵尸进程
# 进程池中有两个方法：
# apply
# apply_async
from multiprocessing import Pool
def myFun(i):
    time.sleep(2)
    return i+100
 
def end_call(arg):
    print("end_call",arg)
 
p = Pool(5)
 
# print(p.map(myFun,range(10)))

for i in range(10):
    p.apply_async(func=myFun,args=(i,),callback=end_call)
 
print("end")
p.close()
p.join()

#官方实例
from multiprocessing import TimeoutError
import os
 
def fn(x):
    return x*x
 
if __name__ == '__main__':
    # 创建4个进程 
    with Pool(processes=4) as pool:
 
        # 打印 "[0, 1, 4,..., 81]" 
        print(pool.map(fn, range(10)))
 
        # 使用任意顺序输出相同的数字， 
        for i in pool.imap_unordered(fn, range(10)):
            print(i)
 
        # 异步执行"f(20)" 
        res = pool.apply_async(fn, (20,))      # 只运行一个进程 
        print(res.get(timeout=1))             # 输出 "400" 
 
        # 异步执行 "os.getpid()" 
        res = pool.apply_async(os.getpid, ()) # 只运行一个进程 
        print(res.get(timeout=1))             # 输出进程的 PID 
 
        # 运行多个异步执行可能会使用多个进程 
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])
 
        # 是一个进程睡10秒 
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("发现一个 multiprocessing.TimeoutError异常")
 
        print("目前，池中还有其他的工作")
 
    # 退出with块中已经停止的池 
    print("Now the pool is closed and no longer available")
    
#####协程@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 协程又叫微线程，从技术的角度来说，“协程就是你可以暂停执行的函数”。如果你把它理解成“就像生成器一样”，那么你就想对了。 线程和进程的操作是由程序触发系统接口，最后的执行者是系统；协程的操作则是程序员。
# 协程存在的意义：对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态，下次继续）。协程，则只使用一个线程，在一个线程中规定某个代码块执行顺序。
# 协程的适用场景：当程序中存在大量不需要CPU的操作时（IO），适用于协程。
# # 安装
# pip install gevent
# # 导入模块
# import gevent
# #greenlet
# from greenlet import greenlet
# def test1():
#     print(11)
#     gr2.switch()
#     print(22)
#     gr2.switch()
#  
# def test2():
#     print(33)
#     gr1.switch()
#     print(44)
#  
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()
# #gevent
# import gevent
#  
# def foo():
#     print("Running in foo")
#     gevent.sleep(0)
#     print("Explicit context switch to foo angin")
#  
# def bar():
#     print("Explicit context to bar")
#     gevent.sleep(0)
#     print("Implicit context swich back to bar")
#  
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

#遇到IO操作自动切换
# from gevent import monkey
# monkey.patch_all()
# import gevent
# import requests
# 
# def f(url):
#     print("FET: %s" % url)
#     resp = requests.get(url)
#     data = len(resp.text)
#     print(url, data)
# 
# gevent.joinall([
#     gevent.spawn(f, 'https://www.python.org/'),
#     gevent.spawn(f, 'https://www.yahoo.com/'),
#     gevent.spawn(f, 'https://github.com/'),
# ])