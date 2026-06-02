# 多线程 threading 之 不一定有效率

import threading
import time
import copy
from queue import Queue

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l),q),name='T%i'%i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
s_t=time.time()
normal(l*4)
print('normal:',time.time()-s_t)  # 方法一，不使用多线程，将列表扩大4倍后，逐个运算
s_t=time.time()
multithreading(l)
print('multithreading:',time.time()-s_t)  # 方法二，使用多线程，使用4个线程进行运算，同时处理4遍

# 输出结果：
# normal：0.2387 秒
# multithreading：0.2221 秒

# 扣除掉读写的时间
# 要用到multi processor 或者 multi processing，才能实现真正的并行

# 弹幕：
# 单核都是并发，多核才能并行
# 可以不使用cpython，用jpython，pypy，或者多进程
# 所以有了process










