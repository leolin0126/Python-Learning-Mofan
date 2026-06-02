# Lock 锁
import threading

def job1():
    global A,lock  # 定义全局变量
    lock.acquire()  # 上锁线程job1
    for i in range(10):
        A = A + 1
        print('job1 ',A)
    lock.release()  # 解锁线程job1

def job2():
    global A  # 定义全局变量
    lock.acquire()  # 上锁线程job2
    for i in range(10):
        A = A +10
        print('job2 ',A)
    lock.release()  # 解锁线程job2

if __name__ == '__main__' :
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 弹幕：
# 什么时候用锁比较好？ 防止对方网站被自己搞崩溃的时候用锁最好，不然太高并发不行。
# 不小心写成target=job（）了，加了一对括号之后，就没有乱，为什么啊？ 
# 加括号就直接执行了，所以不乱；加了括号就相当于执行完此函数后在运行








