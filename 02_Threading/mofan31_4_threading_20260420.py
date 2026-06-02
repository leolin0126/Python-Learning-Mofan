# 多线程 Queen 功能
import threading
# import time
from queue import Queue  # 是 Python 中用于‌多线程编程‌的常用导入语句，它从标准库的 queue 模块中导入 ‌FIFO（先进先出）队列类‌，适用于线程间安全通信。

def job(l,q):  # 定义job
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)  # 返回值l

def multithreading():  # Queue 和 Thread 都是object对象
    q = Queue()  # 定义q=Queue，放入q.put(l)，即计算后的返回值，替代return功能
    threads = []  # 将所有线程放入此列表中，这里的threads是元素为类的列表，即<class 'list'>
    data = [[1,2,3],[3,4,5],[4,5,6],[5,6,7]]
    for i in range(4):  # 第一个for...in循环
        t = threading.Thread(target=job,args=(data[i],q))  # target索引到 def job(l,q)，args表示传递进线程中的参数
        t.start()
        threads.append(t)  # 将参数t放入线程列表threads中
    for thread in threads:
        thread.join()  # 加载到主线程中
    results = []
    for _ in range(4):
        results.append(q.get())  # 传进去q的参数有4次，所以results提取也要4次
    print(results)

# 弹幕：
# 这里用第二循环是为了让四个子进程能够异步执行
# 但这里的场景是让四个子进程并发执行
# 所以用了两个循环
# 如果join直接放在第一个循环里，相当于让四个子进程依次执行
# 我直接t.join()在这个循环是否也可以？
# t.join的话就相当于是下一个还没启动，这个就开始执行了，那还是串行的，多线程就没意义了

if __name__=='__main__':  # 判断模块是否直接运行
    multithreading()

# 整个程序的大致运行过程：
# 把data中4批数据作为参数分批放进t的线程中，每个线程对4批数据分别运算一次，返回结果q.put(l)，
# 把计算的结果放到q里面等全部线程运算完成后，再把结果一次一次用q.get()拿出来，放到results里，
# 最后输出results

# 异步执行模式：是指语句执行结束的顺序与语句执行开始的顺序并不一定相同的一种编程模式。
# 异步执行允许同时执行多个操作，一个操作触发后不需等待完成即可进行其他操作
# 程序并发执行：程序并发执行程序并发执行指多个程序或程序段在时间上重叠运行的计算机处理方式，具有间断性、不可再现等特性，其实现需通过锁机制控制操作可行性。
# 该技术属于操作系统领域，通过进程和线程实现逻辑程序的时间重叠执行，单核处理器通过任务调度创造并发假象，多核处理器可实现真正并行处理。

# 1、同步与异步
#   同步：多个任务情况下，一个任务A执行结束，才可以执行另一个任务B。只存在一个线程。
#   异步：多个任务情况下，一个任务A正在执行，同时可以执行另一个任务B。任务B不用等待任务A结束才执行。存在多条线程。

# 2、并发与并行
#   并行：是指两个或者多个事件在同一时刻发生。
#   并发：是指两个或多个事件在同一时间间隔发生。
        
# 3、串行
#   串行：它是同步线程的实现方式，就是任务A执行结束才能开始执行B，单个线程只能执行一个任务。


















