#!/usr/bin/python
#coding:utf-8

#此部分有很多文档信息具体请看http://www.cnblogs.com/suoning/p/5589039.html

#####Socket@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 功能：
# sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
# 参数一：地址簇
# 　　socket.AF_INET IPv4（默认）
# 　　socket.AF_INET6 IPv6
# 　　socket.AF_UNIX 只能够用于单一的Unix系统进程间通信
# 参数二：类型
# 　　socket.SOCK_STREAM　　流式socket , for TCP （默认）
# 　　socket.SOCK_DGRAM　　 数据报式socket , for UDP
# 　　socket.SOCK_RAW 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。
# 　　socket.SOCK_RDM 是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。
# 　　socket.SOCK_SEQPACKET 可靠的连续数据包服务
# 参数三：协议
# 　　0　　（默认）与特定的地址家族相关的协议,如果是 0 ，则系统就会根据地址格式和套接类别,自动选择一个合适的协议
##UDP例子
# #服务器端
# import socket
# ip_port = ('127.0.0.1',9999)
# sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
# sk.bind(ip_port)
# while True:
#     data = sk.recv(1024)
#     print data

# #客户端
# import socket
# ip_port = ('127.0.0.1',9999)
# sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
# while True:
#     inp = raw_input('数据：').strip()
#     if inp == 'exit':
#         break
#     sk.sendto(inp,ip_port)
# sk.close()

# sk.bind(address)
# 　　s.bind(address) 将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。
# sk.listen(backlog)
# 　　开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
#       backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
#       这个值不能无限大，因为要在内核中维护连接队列
# sk.setblocking(bool)
# 　　是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
# sk.accept()
# 　　接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
# 　　接收TCP 客户的连接（阻塞式）等待连接的到来
# sk.connect(address)
# 　　连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。
# sk.connect_ex(address)
# 　　同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061
# sk.close()
# 　　关闭套接字
# sk.recv(bufsize[,flag])
# 　　接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。
# sk.recvfrom(bufsize[.flag])
# 　　与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
# sk.send(string[,flag])
# 　　将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。
# sk.sendall(string[,flag])
#       将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
#       内部通过递归调用send，将所有内容发送出去。
# sk.sendto(string[,flag],address)
# 　　将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。
# sk.settimeout(timeout)
# 　　设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如 client 连接最多等待5s ）
# sk.getpeername()
# 　　返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
# sk.getsockname()
# 　　返回套接字自己的地址。通常是一个元组(ipaddr,port)
# sk.fileno()
# 　　套接字的文件描述符

#####IO 多路复用@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# I/O多路复用指：通过一种机制，可以监视多个描述符，一旦某个描述符就绪（一般是读就绪或者写就绪），能够通知程序进行相应的读写操作。
# Linux中的 select，poll，epoll 都是IO多路复用的机制。
# select
# select最早于1983年出现在4.2BSD中，它通过一个select()系统调用来监视多个文件描述符的数组，当select()返回后，该数组中就绪的文件描述符便会被内核修改标志位，使得进程可以获得这些文件描述符从而进行后续的读写操作。
# select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点，事实上从现在看来，这也是它所剩不多的优点之一。
# select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，不过可以通过修改宏定义甚至重新编译内核的方式提升这一限制。
# 另外，select()所维护的存储大量文件描述符的数据结构，随着文件描述符数量的增大，其复制的开销也线性增长。同时，由于网络响应时间的延迟使得大量TCP连接处于非活跃状态，但调用select()会对所有socket进行一次线性扫描，所以这也浪费了一定的开销。
#   
# poll
# poll在1986年诞生于System V Release 3，它和select在本质上没有多大差别，但是poll没有最大文件描述符数量的限制。
# poll和select同样存在一个缺点就是，包含大量文件描述符的数组被整体复制于用户态和内核的地址空间之间，而不论这些文件描述符是否就绪，它的开销随着文件描述符数量的增加而线性增大。
# 另外，select()和poll()将就绪的文件描述符告诉进程后，如果进程没有对其进行IO操作，那么下次调用select()和poll()的时候将再次报告这些文件描述符，所以它们一般不会丢失就绪的消息，这种方式称为水平触发（Level Triggered）。
#   
# epoll
# 直到Linux2.6才出现了由内核直接支持的实现方法，那就是epoll，它几乎具备了之前所说的一切优点，被公认为Linux2.6下性能最好的多路I/O就绪通知方法。
# epoll可以同时支持水平触发和边缘触发（Edge Triggered，只告诉进程哪些文件描述符刚刚变为就绪状态，它只说一遍，如果我们没有采取行动，那么它将不会再次告知，这种方式称为边缘触发），理论上边缘触发的性能要更高一些，但是代码实现相当复杂。
# epoll同样只告知那些就绪的文件描述符，而且当我们调用epoll_wait()获得就绪文件描述符时，返回的不是实际的描述符，而是一个代表就绪描述符数量的值，你只需要去epoll指定的一个数组中依次取得相应数量的文件描述符即可，这里也使用了内存映射（mmap）技术，这样便彻底省掉了这些文件描述符在系统调用时复制的开销。
# 另一个本质的改进在于epoll采用基于事件的就绪通知方式。在select/poll中，进程只有在调用一定的方法后，内核才对所有监视的文件描述符进行扫描，而epoll事先通过epoll_ctl()来注册一个文件描述符，一旦基于某个文件描述符就绪时，内核会采用类似callback的回调机制，迅速激活这个文件描述符，当进程调用epoll_wait()时便得到通知。

# Python中有一个select模块，其中提供了：select、poll、epoll三个方法，分别调用系统的 select，poll，epoll 从而实现IO多路复用。
# Windows Python：
#     提供： select
# Mac Python：
#     提供： select
# Linux Python：
#     提供： select、poll、epoll
# 注意：网络操作、文件操作、终端操作等均属于IO操作，对于windows只支持Socket操作，其他系统支持其他IO操作，但是无法检测 普通文件操作 自动上次读取是否已经变化。
# 对于select方法：
# 句柄列表11, 句柄列表22, 句柄列表33 = select.select(句柄序列1, 句柄序列2, 句柄序列3, 超时时间)
# 参数： 可接受四个参数（前三个必须）
# 返回值：三个列表
# select方法用来监视文件句柄，如果句柄发生变化，则获取该句柄。
# 1、当 参数1 序列中的句柄发生可读时（accetp和read），则获取发生变化的句柄并添加到 返回值1 序列中
# 2、当 参数2 序列中含有句柄时，则将该序列中所有的句柄添加到 返回值2 序列中
# 3、当 参数3 序列中的句柄发生错误时，则将该发生错误的句柄添加到 返回值3 序列中
# 4、当 超时时间 未设置，则select会一直阻塞，直到监听的句柄发生变化
#    当 超时时间 ＝ 1时，那么如果监听的句柄均无任何变化，则select会阻塞 1 秒，之后返回三个空列表，如果监听的句柄有变化，则直接执行。

#利用select监听终端操作实例
# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import select
# import threading
# import sys
# while True:
#     readable, writeable, error = select.select([sys.stdin,],[],[],1)
#     if sys.stdin in readable:
#         print 'select get stdin',sys.stdin.readline()

#利用select实现伪同时处理多个socket客户端请求：服务端
# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import socket
# import select
# sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sk1.bind(('127.0.0.1',8002))
# sk1.listen(5)
# sk1.setblocking(0)
# inputs = [sk1,]
# while True:
#     readable_list, writeable_list, error_list = select.select(inputs, [], inputs, 1)
#     for r in readable_list:
#         # 当客户端第一次连接服务端时
#         if sk1 == r:
#             print 'accept'
#             request, address = r.accept()
#             request.setblocking(0)
#             inputs.append(request)
#         # 当客户端连接上服务端之后，再次发送数据时
#         else:
#             received = r.recv(1024)
#             # 当正常接收客户端发送的数据时
#             if received:
#                 print 'received data:', received
#             # 当客户端关闭程序时
#             else:
#                 inputs.remove(r)
# sk1.close()

#利用select实现伪同时处理多个socket客户端请求：客户端
# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import socket
# ip_port = ('127.0.0.1',8002)
# sk = socket.socket()
# sk.connect(ip_port)
# while True:
#     inp = raw_input('please input:')
#     sk.sendall(inp)
# sk.close()
# 此处的Socket服务端相比与原生的Socket，他支持当某一个请求不再发送数据时，服务器端不会等待而是可以去处理其他请求的数据。但是，如果每个请求的耗时比较长时，select版本的服务器端也无法完成同时操作。

#基于select实现socket服务端
# #!/usr/bin/env python
# #coding:utf8
# '''
#  服务器的实现 采用select的方式
# '''
# import select
# import socket
# import sys
# import Queue
# #创建套接字并设置该套接字为非阻塞模式
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.setblocking(0)
# #绑定套接字
# server_address = ('localhost',10000)
# print >>sys.stderr,'starting up on %s port %s'% server_address
# server.bind(server_address)
# #将该socket变成服务模式
# #backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
# #这个值不能无限大，因为要在内核中维护连接队列
# server.listen(5)
# #初始化读取数据的监听列表,最开始时希望从server这个套接字上读取数据
# inputs = [server]
# #初始化写入数据的监听列表，最开始并没有客户端连接进来，所以列表为空
# outputs = []
# #要发往客户端的数据
# message_queues = {}
# while inputs:
#     print >>sys.stderr,'waiting for the next event'
#     #调用select监听所有监听列表中的套接字，并将准备好的套接字加入到对应的列表中
#     readable,writable,exceptional = select.select(inputs,outputs,inputs)#列表中的socket 套接字  如果是文件呢？ 
#     #监控文件句柄有某一处发生了变化 可写 可读  异常属于Linux中的网络编程 
#     #属于同步I/O操作，属于I/O复用模型的一种
#     #rlist--等待到准备好读
#     #wlist--等待到准备好写
#     #xlist--等待到一种异常
#     #处理可读取的套接字
#     '''
#         如果server这个套接字可读，则说明有新链接到来
#         此时在server套接字上调用accept,生成一个与客户端通讯的套接字
#         并将与客户端通讯的套接字加入inputs列表，下一次可以通过select检查连接是否可读
#         然后在发往客户端的缓冲中加入一项，键名为:与客户端通讯的套接字，键值为空队列
#         select系统调用是用来让我们的程序监视多个文件句柄(file descrīptor)的状态变化的。程序会停在select这里等待，
#         直到被监视的文件句柄有某一个或多个发生了状态改变
#         '''
#     '''
#         若可读的套接字不是server套接字,有两种情况:一种是有数据到来，另一种是链接断开
#         如果有数据到来,先接收数据,然后将收到的数据填入往客户端的缓存区中的对应位置，最后
#         将于客户端通讯的套接字加入到写数据的监听列表:
#         如果套接字可读.但没有接收到数据，则说明客户端已经断开。这时需要关闭与客户端连接的套接字
#         进行资源清理
#         '''
#     for s in readable: 
#         if s is server:
#             connection,client_address = s.accept()
#             print >>sys.stderr,'connection from',client_address
#             connection.setblocking(0)#设置非阻塞
#             inputs.append(connection)
#             message_queues[connection] = Queue.Queue()
#         else:
#             data = s.recv(1024)
#             if data:
#                 print >>sys.stderr,'received "%s" from %s'% \
#                 (data,s.getpeername())
#                 message_queues[s].put(data)
#                 if s not in outputs:
#                     outputs.append(s)
#             else:
#                 print >>sys.stderr,'closing',client_address
#                 if s in outputs:
#                     outputs.remove(s)
#                 inputs.remove(s)
#                 s.close()
#                 del message_queues[s]
#                     
#     #处理可写的套接字
#     '''
#         在发送缓冲区中取出响应的数据，发往客户端。
#         如果没有数据需要写，则将套接字从发送队列中移除，select中不再监视
#         '''
#     for s in writable:
#         try:
#             next_msg = message_queues[s].get_nowait()
# 
#         except Queue.Empty:
#             print >>sys.stderr,'  ',s,getpeername(),'queue empty'
#             outputs.remove(s)
#         else:
#             print >>sys.stderr,'sending "%s" to %s'% \
#             (next_msg,s.getpeername())
#             s.send(next_msg)
#     #处理异常情况
#     for s in exceptional:
#         for s in exceptional:
#             print >>sys.stderr,'exception condition on',s.getpeername()
#             inputs.remove(s)
#             if s in outputs:
#                 outputs.remove(s)
#             s.close()
#             del message_queues[s]

#####SocketServer 模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# SocketServer内部使用 IO多路复用 以及 “多线程” 和 “多进程” ，从而实现并发处理多个客户端请求的Socket服务端。
# 
# +------------+
# | BaseServer |
# +------------+
#       |
#       v
# +-----------+        +------------------+
# | TCPServer |------->| UnixStreamServer |
# +-----------+        +------------------+
#       |
#       v
# +-----------+        +--------------------+
# | UDPServer |------->| UnixDatagramServer |
# +-----------+        +--------------------+
# 
# SocketServer简化了网络服务器的编写。它有4个类：TCPServer，UDPServer，UnixStreamServer，UnixDatagramServer。
# 这4个类是同步进行处理的，另外通过ForkingMixIn和ThreadingMixIn类来支持异步。
# 
# ThreadingTCPServer
# ThreadingTCPServer实现的Soket服务器内部会为每个client创建一个 “线程”，该线程用来和客户端进行交互。
# 
# 1、ThreadingTCPServer基础
# 
# 使用ThreadingTCPServer:
# 
# 创建一个继承自 SocketServer.BaseRequestHandler 的类
# 类中必须定义一个名称为 handle 的方法
# 启动ThreadingTCPServer
# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import SocketServer
# class MyServer(SocketServer.BaseRequestHandler):
#     def handle(self):
#         pass
# if __name__ == '__main__':
#     server = SocketServer.ThreadingTCPServer(('127.0.0.1',8766), MyServer)
#     server.serve_forever()

# 2、ThreadingTCPServer源码剖析
# ThreadingTCPServer的类图关系如下：（具体见网页）
# 内部调用流程为：
# 启动服务端程序
# 执行 TCPServer.__init__ 方法，创建服务端Socket对象并绑定 IP 和 端口
# 执行 BaseServer.__init__ 方法，将自定义的继承自SocketServer.BaseRequestHandler 的类 MyRequestHandle赋值给self.RequestHandlerClass
# 执行 BaseServer.server_forever 方法，While 循环一直监听是否有客户端请求到达 ...
# 当客户端连接到达服务器
# 执行 ThreadingMixIn.process_request 方法，创建一个 “线程” 用来处理请求
# 执行 ThreadingMixIn.process_request_thread 方法
# 执行 BaseServer.finish_request 方法，执行 self.RequestHandlerClass()  即：执行 自定义 MyRequestHandler 的构造方法（自动调用基类BaseRequestHandler的构造方法，在该构造方法中又会调用 MyRequestHandler的handle方法）
# ThreadingTCPServer相关源码：（具体见网页）
# BaseServer
# TCPServer
# ThreadingMixIn
# ThreadingTCPServer
# RequestHandler相关源码:（具体见网页）
# SocketServer.BaseRequestHandler
# SocketServer的ThreadingTCPServer之所以可以同时处理请求得益于 select 和 Threading 两个东西，其实本质上就是在服务器端为每一个客户端创建一个线程，当前线程用来处理对应客户端的请求，所以，可以支持同时n个客户端链接（长连接）。

# ForkingTCPServer
# ForkingTCPServer和ThreadingTCPServer的使用和执行流程基本一致，只不过在内部分别为请求者建立 “线程”  和 “进程”。
# 基本使用：
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import SocketServer
class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        pass
if __name__ == '__main__':
    server = SocketServer.ForkingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()